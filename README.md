# 🚀 AMod_MapMarker

* **Name:** AMod_MapMarker
* **Author:** Huk, Xenomorphchyma, ringill
* **License:** Creative Commons BY-NC-SA 4.0

### Summary

Adds the ability to place a marker on a galaxy-map system

---

## 📖 Description

Two buttons on the galaxy map place and remove a marker (arrow) on the chosen system or planet. Marker coordinates are tuned to the standard-size galaxy map. The mod conflicts with XenoBigGalaxy, which resizes the galaxy and embeds its own marker buttons. English and Russian are supported.

---

## 🔗 Based on

```yaml
based_on:
  - source: 🏛️ https://github.com/space-rangers-mods-museum/AMod_MapMarker
    note: AMod_MapMarker - Huk (the original marker)
  - source: Xenomorphchyma - XenoBigGalaxy (SRHD-XenoModKit)
    note: >-
      Guarded star/planet search idiom ported from XenoBigGalaxy into the marker code (null star/planet
      checks, invisible/far-sector skip via StarToCon/SectorVisible). Coordinate scaling is NOT ported -
      the marker is tuned to the standard 768x527 map and declares Conflict=XenoBigGalaxy, which resizes
      the galaxy and defines its own scaling constants.

```

---

## 📁 Mod files

* [latest release (archive)](https://github.com/space-rangers-mods-workshop/AMod_MapMarker/releases/latest) — the mod packaged for download
* [`mod/`](mod/) — the assembled, ready-to-deploy mod folder (/Mods/Miscellaneous/AMod_MapMarker)
* [`src/`](src/) — the readable sources



---

## ⚖️ License

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

**Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).**

You are free to share and adapt it, provided you give credit to the authors, do not use it commercially, and release your derivative under the same license. For a mod derived from museum exhibits, that credit includes the original exhibit authors and a link back to the preserved originals. See [LICENSE](LICENSE) for the full license text.

---

## 🔍 How the sources were used

An ordered chain of repeatable steps - how the source data was processed, modified and transformed into a usable form: [AMod_MapMarker.yaml](./AMod_MapMarker.yaml)