<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,60:1a3320,100:4a7c59&height=160&section=header&text=National%20Park%20Style%20Map&fontSize=32&fontColor=ffffff&fontAlignY=45&desc=Replicating%20the%20Iconic%20US%20NPS%20Cartographic%20Style&descAlignY=65&descSize=14&descColor=a8d5b5" width="100%"/>

[![Category](https://img.shields.io/badge/Category-B%20Cartography-4a7c59?style=for-the-badge&labelColor=0d1117)](../)
[![Style](https://img.shields.io/badge/Style-US%20NPS%20Standard-1a3320?style=for-the-badge&labelColor=0d1117)]()
[![Platform](https://img.shields.io/badge/Platform-ArcGIS%20Pro-2C7BB6?style=for-the-badge&logo=esri&logoColor=white&labelColor=0d1117)]()
[![Type](https://img.shields.io/badge/Type-Cartographic%20Recreation-a8d5b5?style=for-the-badge&labelColor=0d1117)]()

</div>

---

## 📌 Project Overview

This project replicates the **iconic cartographic style of the US National Park Service (NPS)** — one of the most recognizable and respected map design systems in the world, developed by cartographer Tom Patterson at the NPS.

The NPS style is renowned for its hand-crafted aesthetics: soft hillshading, muted natural color palettes, clean label hierarchy, and a warm, inviting tone that makes complex terrain feel approachable. Replicating this style in ArcGIS Pro demonstrates advanced cartographic design skills.

---

## 🎯 Objectives

- Study and deconstruct the NPS cartographic style guide
- Recreate terrain rendering using custom hillshading and hypsometric tinting
- Apply NPS-compliant color palette, typography, and symbology
- Produce a final map indistinguishable in style from official NPS outputs

---

## 🎨 NPS Style Elements Recreated

| Element | Specification |
|---------|--------------|
| **Hillshading** | Multi-directional blended hillshade (315° + 45°) |
| **Hypsometric Tint** | Muted green-to-brown elevation ramp |
| **Water Bodies** | Soft desaturated blue `#a8c8d8` fill |
| **Vegetation** | Stippled / classified green zones |
| **Typography** | Frutiger / Myriad Pro (NPS standard fonts) |
| **Roads** | Hierarchical symbology — highway to trail |
| **Labels** | Mixed upper/lower case with halo masking |
| **Border** | Neat line with coordinate tick marks |
| **Scale** | Bar scale + representative fraction |
| **North Arrow** | NPS-style compass rose |

---

## ⚙️ Methodology

```
1. DATA PREPARATION
   └── DEM (30m SRTM or 10m NED) for hillshading
   └── OSM / NPS vector data for roads, trails, POIs
   └── Hydrology layer for streams and lakes
   └── Vegetation / land cover classification

2. TERRAIN RENDERING
   └── Generate hillshade at 315° azimuth, 45° altitude
   └── Generate secondary hillshade at 45° azimuth
   └── Blend both using Transparency rendering
   └── Apply hypsometric tint as color ramp symbology

3. VECTOR STYLING
   └── Apply NPS road hierarchy symbology
   └── Style water features with NPS blue palette
   └── Add vegetation polygons with NPS green fills

4. LABELING
   └── Set label classes per feature type
   └── Apply NPS-standard fonts and sizes
   └── Configure halo masking for readability

5. LAYOUT & EXPORT
   └── ArcGIS Pro layout view — A2 or A1 size
   └── Export PDF (300 DPI) + PNG (150 DPI web)
```

---

## 🗂️ File Structure

```
National-Park-Style-Map/
├── README.md
├── data/
│   ├── DEM_study_area.tif             ← Elevation raster
│   ├── roads_trails.shp               ← OSM road network
│   ├── hydrology.shp                  ← Streams and lakes
│   └── vegetation.shp                 ← Land cover polygons
├── styles/
│   └── NPS_symbology.stylx            ← ArcGIS Pro style file
├── outputs/
│   ├── NPS_style_map_A2.pdf           ← Print layout (300 DPI)
│   └── NPS_style_map_web.png          ← Web version
└── docs/
    └── NPS_style_reference.md         ← Color codes and font specs
```

---

## 🎨 Color Reference

| Feature | Hex Code | Usage |
|---------|---------|-------|
| Water fill | `#a8c8d8` | Lakes, rivers |
| Vegetation | `#b5cca0` | Forest/shrub zones |
| Developed | `#e8dcc8` | Buildings, roads |
| Elevation low | `#c8d8a0` | Low hypsometric |
| Elevation high | `#a07858` | High hypsometric |
| Background | `#f0ead8` | Paper / base tone |

---

## 🛠️ Tools & Software

![ArcGIS Pro](https://img.shields.io/badge/ArcGIS_Pro-2C7BB6?style=flat-square&logo=esri&logoColor=white)
![QGIS](https://img.shields.io/badge/QGIS-589632?style=flat-square&logo=qgis&logoColor=white)
![SRTM DEM](https://img.shields.io/badge/SRTM_DEM-30m-8B4513?style=flat-square&logoColor=white)

---

<h2>🖼️ Visual Preview</h2>
<img src="Rocky Mountain NPS Maps.jpg" alt="Rocky Mountain NPS Map" width="600">

---

## 🔗 Navigation

[← Back to Portfolio](../README.md) &nbsp;|&nbsp; [Previous: Riyadh Postcode Mapping](../Riyadh-Postcode-Mapping) &nbsp;|&nbsp; [Next: Zurich Demographics →](../Zurich-Demographics)

---
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:4a7c59,60:1a3320,100:0d1117&height=80&section=footer" width="100%"/>
</div>
