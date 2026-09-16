"""Build AMod_MapMarker mod/ from readable sources (pure ML panel overlay route).

Run from workshop/AMod_MapMarker:
    ..\\..\\.venv\\Scripts\\python.exe build_amod_mapmarker.py

This mod is a pure ML panel overlay on the base galaxy map: it has NO scenario
script (.scr) and no Data/Script registration. The marker logic lives entirely in
the OnPressCode bodies of the two GraphButtons in src/Main.txt, so the build is
just: encode the four .dat files, copy the 7 .gi textures, render ModuleInfo.txt
from the YAML info block.

Improvements over the museum original (see AMod_MapMarker.yaml acquire notes):
  - Guarded star/planet search (from Xenomorphchyma's XenoBigGalaxy): null star/planet
    checks and invisible/far-sector skip via StarToCon/SectorVisible, with cached
    GalaxyStars()/StarPlanets() loop bounds.
  - English support: the three panel literals are now CT('Script.AMod_MapMarker.*')
    lookups whose values live in per-language Lang.dat (Rus + Eng).

Compatibility: the marker is tuned to the standard 768x527 galaxy map and declares
Conflict=XenoBigGalaxy (ModuleInfo). The earlier CT('Constellations.GalaxySizeX/Y')
scaling was reverted - those constants are XenoBigGalaxy's own (0 on a vanilla
install, so scaling divided by zero); this mod must NOT run beside XenoBigGalaxy.

Layout produced (conventions from installed game reference mods):
  mod/ModuleInfo.txt            UTF-16 LE BOM (rendered from AMod_MapMarker.yaml info)
  mod/CFG/Main.dat              from src/Main.txt        fmt=HDMain   unsigned
  mod/CFG/CacheData.dat         from src/CacheData.txt   fmt=HDCache  unsigned
  mod/CFG/Rus/Lang.dat          from src/Lang_Rus.txt    fmt=HDMain   signed
  mod/CFG/Eng/Lang.dat          from src/Lang_Eng.txt    fmt=HDMain   signed
  mod/Data/Image/*.gi           the 7 panel textures (copied from src/resources/Data/Image/)
"""
from pathlib import Path

import rangers.dat as d
import yaml

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
MOD = ROOT / "mod"
CFG = MOD / "CFG"
RUS = CFG / "Rus"
ENG = CFG / "Eng"
TEXTURES = MOD / "Data" / "Image"
RES_TEX = SRC / "resources" / "Data" / "Image"

# The 7 .gi textures the marker references (Bm.Image.*) — bundled into the mod.
PANEL_GI = [
    "Arrows.gi",
    "leftButton_A.gi",
    "leftButton_D.gi",
    "leftButton_N.gi",
    "rightButton_A.gi",
    "rightButton_D.gi",
    "rightButton_N.gi",
]

YAML_PATH = ROOT / "AMod_MapMarker.yaml"


def build_module_info(mod: str, info: dict) -> str:
    """Render ModuleInfo.txt content from the mod YAML ``info`` block.

    The ``info`` keys mirror ModuleInfo.txt exactly (Name, Author, Conflict,
    Priority, Section, SectionEng, Languages, SmallDescription,
    SmallDescriptionEng, FullDescription, FullDescriptionEng); ``Name`` falls
    back to the top-level ``mod`` key.
    """

    def val(key):
        v = info.get(key)
        return "" if v is None else str(v)

    pairs = [
        ("Name", val("Name") or mod),
        ("Author", val("Author")),
        ("Conflict", val("Conflict")),
        ("Priority", val("Priority")),
        ("Section", val("Section")),
        ("SectionEng", val("SectionEng")),
        ("Languages", val("Languages")),
        ("SmallDescription", val("SmallDescription")),
        ("SmallDescriptionEng", val("SmallDescriptionEng")),
        ("FullDescription", val("FullDescription")),
        ("FullDescriptionEng", val("FullDescriptionEng")),
    ]
    return "\n".join(f"{key}={value}" for key, value in pairs)


def write_module_info():
    MOD.mkdir(parents=True, exist_ok=True)
    with open(YAML_PATH, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    mod = (data.get("mod") or "").strip()
    info = data.get("info") or {}
    module_info = build_module_info(mod, info)
    # UTF-16 LE with BOM
    (MOD / "ModuleInfo.txt").write_bytes(
        b"\xff\xfe" + module_info.encode("utf-16-le")
    )
    print("wrote mod/ModuleInfo.txt (UTF-16 LE BOM,", len(module_info), "chars)")


def read_source_text(src):
    """Decode a readable BlockPar source. Sources are UTF-16 LE with BOM (the
    convention Main.txt/BlockPar sources are saved in); fall back to UTF-8, the
    SRHD legacy codepage (win-1251), or UTF-16 BE.

    A BOM byte-order mark, if present, is stripped from the returned text: a
    surviving U+FEFF at the head of the content would otherwise be embedded in
    the DAT before ``ML`` and break the engine's root-key parse, silently
    dropping the whole overlay (marker buttons never render).
    """
    data = src.read_bytes()
    text = data.decode("utf-8-sig") if data[:3] == b"\xef\xbb\xbf" else None
    if text is None:
        if data[:2] == b"\xff\xfe":
            text = data.decode("utf-16-le")
        elif data[:2] == b"\xfe\xff":
            text = data.decode("utf-16-be")
        else:
            try:
                text = data.decode("utf8")
            except UnicodeDecodeError:
                text = data.decode("cp1251")
    # utf-16-le/-be do not consume the BOM the way 'utf-16' does; drop it.
    return text.lstrip("\ufeff")


def encode(src_rel, out_rel, fmt, sign):
    src = SRC / src_rel
    out = MOD / out_rel
    text = read_source_text(src)
    dat = d.DAT.from_str(text)
    dat.to_dat(out, fmt=fmt, sign=sign)
    b = out.read_bytes()
    ok = d.check_signed(b) == sign
    back = d.DAT.from_dat(out)
    print(
        f"encoded {out_rel}: fmt={dat.fmt} sign={sign} len={len(b)} "
        f"reparse_fmt={back.fmt} sig_match={ok}"
    )
    return out


def check_textures():
    missing = [name for name in PANEL_GI if not (RES_TEX / name).exists()]
    if missing:
        print(
            "ERROR: missing bundled panel textures in src/resources/Data/Image/:\n  "
            + "\n  ".join(missing),
            file=__import__("sys").stderr,
        )
        __import__("sys").exit(1)
    print(f"source textures present: {len(PANEL_GI)} .gi in src/resources/Data/Image/")


def copy_textures():
    TEXTURES.mkdir(parents=True, exist_ok=True)
    for name in PANEL_GI:
        (TEXTURES / name).write_bytes((RES_TEX / name).read_bytes())
    print(f"copied {len(PANEL_GI)} .gi into mod/Data/Image/")


def main():
    # sanity: sources exist
    for name in ["Main.txt", "CacheData.txt", "Lang_Rus.txt", "Lang_Eng.txt"]:
        if not (SRC / name).exists():
            print(f"ERROR: missing source {name}", file=__import__("sys").stderr)
            __import__("sys").exit(1)

    check_textures()
    write_module_info()
    encode("Main.txt", "CFG/Main.dat", "HDMain", False)
    encode("CacheData.txt", "CFG/CacheData.dat", "HDCache", False)
    encode("Lang_Rus.txt", "CFG/Rus/Lang.dat", "HDMain", True)
    encode("Lang_Eng.txt", "CFG/Eng/Lang.dat", "HDMain", True)
    copy_textures()
    print("build complete (pure ML overlay: no .scr route needed)")


if __name__ == "__main__":
    main()
