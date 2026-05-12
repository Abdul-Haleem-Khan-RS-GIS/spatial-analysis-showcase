<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,60:3d1a00,100:ff6b00&height=200&section=header&text=Burn%20Severity%20Analysis&fontSize=32&fontColor=ffffff&fontAlignY=32&desc=Wildfire%20Damage%20Mapping%20with%20Sentinel-2&descAlignY=50&descSize=16&descColor=ffb380" width="100%"/>

<div align="center">


[![Category](https://img.shields.io/badge/Category-A%20Remote%20Sensing-ff6b00?style=for-the-badge&labelColor=0d1117)](../)
[![Satellite](https://img.shields.io/badge/Data-Sentinel--2-003247?style=for-the-badge&logo=esa&logoColor=white&labelColor=0d1117)]()
[![Platform](https://img.shields.io/badge/Platform-ArcGIS%20Pro-2C7BB6?style=for-the-badge&logo=esri&logoColor=white&labelColor=0d1117)]()
[![Index](https://img.shields.io/badge/Index-NBR%20%2F%20dNBR-ff4500?style=for-the-badge&labelColor=0d1117)]()

<div align="left">

---

## 📌 Project Overview

This project maps wildfire burn severity across an affected landscape using **pre- and post-fire Sentinel-2 satellite imagery**. By calculating the Normalized Burn Ratio (NBR) and its difference (dNBR), the analysis produces a classified burn severity map identifying unburned, low, moderate, high, and very-high severity zones.

Burn severity data is critical for post-fire rehabilitation planning, ecological impact assessments, and insurance or government damage reporting.

---

## 🎯 Objectives

- Acquire and pre-process pre-fire and post-fire Sentinel-2 imagery
- Calculate NBR for both acquisitions
- Derive dNBR (delta NBR) to quantify burn severity change
- Classify severity into standard USGS burn severity classes
- Produce a publication-ready burn severity map

---

## 🛰️ Data Sources

| Dataset | Source | Resolution | Bands Used |
|---------|--------|-----------|------------|
| Pre-fire Sentinel-2 | ESA Copernicus / GEE | 10–20m | B8 (NIR), B12 (SWIR) |
| Post-fire Sentinel-2 | ESA Copernicus / GEE | 10–20m | B8 (NIR), B12 (SWIR) |
| Study area boundary | Digitized / OSM | — | Polygon AOI |

---

## ⚙️ Methodology

```
1. DATA ACQUISITION
   └── Filter Sentinel-2 image collection by date, cloud cover < 10%, AOI

2. PRE-PROCESSING
   └── Cloud masking using SCL band
   └── Atmospheric correction (Surface Reflectance product)

3. INDEX CALCULATION
   └── NBR = (NIR - SWIR) / (NIR + SWIR)
   └── Pre-fire NBR  →  image_pre
   └── Post-fire NBR →  image_post

4. CHANGE DETECTION
   └── dNBR = Pre-fire NBR − Post-fire NBR

5. CLASSIFICATION
   └── Apply USGS dNBR severity thresholds:
       < -0.25   → Enhanced Regrowth
       -0.25–0.1 → Unburned
       0.1–0.27  → Low Severity
       0.27–0.66 → Moderate Severity
       > 0.66    → High Severity

6. OUTPUT
   └── Classified raster + area statistics per severity class
```

---

## 🗂️ File Structure

```
Burn-Severity-Analysis/
├── README.md
├── scripts/
│   └── burn_severity_GEE.js       ← Google Earth Engine script
├── data/
│   ├── AOI_boundary.geojson       ← Study area polygon
│   └── severity_classes.csv       ← dNBR threshold reference
├── outputs/
│   ├── burn_severity_map.pdf      ← Final map layout
│   ├── burn_severity_map.png      ← Export for web
│   └── area_statistics.xlsx       ← Burned area per class
└── report/
    └── Burn_Severity_Report.pdf   ← Full methodology report
```

---

## 📊 Key Results

| Severity Class | dNBR Range | Area (ha) | % of AOI |
|----------------|-----------|-----------|----------|
| Unburned | < 0.10 | — | — |
| Low Severity | 0.10 – 0.27 | — | — |
| Moderate Severity | 0.27 – 0.44 | — | — |
| High Severity | 0.44 – 0.66 | — | — |
| Very High Severity | > 0.66 | — | — |

> 📝 *Fill in area values from your output statistics table.*

---

## 🛠️ Tools & Software

![ArcGIS Pro](https://img.shields.io/badge/ArcGIS_Pro-2C7BB6?style=flat-square&logo=esri&logoColor=white)
![Google Earth Engine](https://img.shields.io/badge/Google_Earth_Engine-4285F4?style=flat-square&logo=google&logoColor=white)
![Sentinel-2](https://img.shields.io/badge/Sentinel--2_L2A-003247?style=flat-square&logoColor=white)

---
![Alt Title](https://github.com/Abdul-Haleem-Khan-RS-GIS/spatial-analysis-showcase/blob/5f2c4ba64b5ee9d1046ce4bf12558a51c5b7a430/Category-A-Remote-Sensing/Burn-Severity-Analysis/burn_severity_map.png)

## 🔗 Navigation

[← Back to Portfolio](../README.md) &nbsp;|&nbsp; [Category A: All Remote Sensing Projects](../Category-A-Remote-Sensing) &nbsp;|&nbsp; [Next Project: Land Use Classification →](../Land-Use-Classification)

---
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:ff6b00,60:3d1a00,100:0d1117&height=80&section=footer" width="100%"/>
</div>
