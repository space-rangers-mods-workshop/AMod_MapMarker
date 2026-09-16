## 📖 Description

**AMod_MapMarker** adds two small buttons to the galaxy (star) map that place and remove a map marker — an arrow on the chosen system or planet.

- **Left button** — asks for the name of a system or planet, searches the current galaxy for it, and places the marker on it. Works with Russian and English names.
- **Right button** — removes the placed marker.

Marker coordinates are tuned to the standard-size galaxy map (768x527 area). This mod **conflicts with XenoBigGalaxy** (which resizes the galaxy and embeds its own marker buttons), so the two must not be installed together. The search loop is guarded the way Xenomorphchyma does it in XenoBigGalaxy — invisible/far sectors are skipped and planets are walked per star with bounds checks.

## 📦 Installation instructions

### 🤖 Automatic — Mod Organizer 2

The easiest way is to install the mod through **Mod Organizer 2** using the plugin for Space Rangers HD: A War Apart:

- [Mod Organizer 2 plugin for Space Rangers HD](https://www.nexusmods.com/spacerangersawarapart/mods/57)

Download the mod with MO2 mod manager and deploy it — the plugin places the mod in the correct `Mods\` folder for you.

### ✋ Manual

1. Make sure the game loads mods from its `Mods\` folder.
2. Take the assembled [`mod/`](../mod) folder from this repository.
3. Copy it into the game's `Mods\` folder so that the mod folder ends up at:
   ```
   <game root>\Mods\Miscellaneous\AMod_MapMarker
   ```
   (The folder must contain `ModuleInfo.txt` at its root — do not nest it an extra level down.)
4. Launch the game. Open the galaxy map to use the marker.

To remove the mod, delete the `AMod_MapMarker` folder.

## ✨ Main features

- Place a marker on a system or planet by name.
- Remove the placed marker.
- Works on the standard-size galaxy map (768x527).
- English and Russian supported.

## 🎮 How to use

- Open the galaxy (star) map in game.
- **Left marker button** — a prompt appears asking for the system/planet name. Type it (Cyrillic or Latin, matching your galaxy names) and confirm. The arrow appears on that system/planet. If nothing is found, a message says so and no marker is placed.
- **Right marker button** — removes the marker (with a confirmation prompt).

## ✅ Requirements

No other mods required.

## ❌ Conflicts

XenoBigGalaxy (by Xenomorphchyma)

## 🙏 Shout outs

- **Huk** — author of the original AMod_MapMarker.
- **Xenomorphchyma** — the guarded star/planet search pattern in XenoBigGalaxy that this version ports into the marker code.
- **ringill** — ported the guarded search, added English support.

## 🔗 Source

- [https://github.com/space-rangers-mods-museum/AMod_MapMarker](https://github.com/space-rangers-mods-museum/AMod_MapMarker) — the preserved original (Huk).

## ⚖️ Licence

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

**Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).**
