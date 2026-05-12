<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,60:0a3d2e,100:00e5a0&height=160&section=header&text=Land%20Use%20Classification&fontSize=32&fontColor=ffffff&fontAlignY=45&desc=Supervised%20vs%20Unsupervised%20%E2%80%94%20GEE%20vs%20ArcGIS&descAlignY=65&descSize=14&descColor=a0f0d0" width="100%"/>

[![Category](https://img.shields.io/badge/Category-A%20Remote%20Sensing-00e5a0?style=for-the-badge&labelColor=0d1117)](../)
[![GEE](https://img.shields.io/badge/Platform-Google%20Earth%20Engine-4285F4?style=for-the-badge&logo=google&logoColor=white&labelColor=0d1117)]()
[![ArcGIS](https://img.shields.io/badge/Platform-ArcGIS%20Pro-2C7BB6?style=for-the-badge&logo=esri&logoColor=white&labelColor=0d1117)]()
[![Method](https://img.shields.io/badge/Method-Comparative%20Study-8affd1?style=for-the-badge&labelColor=0d1117)]()

</div>

---

## 📌 Project Overview

A **comparative classification study** evaluating two industry-standard land use / land cover (LULC) classification approaches on the same study area:

- **Supervised Classification** via Google Earth Engine (Maximum Likelihood / Random Forest)
- **Unsupervised Classification** via ArcGIS Pro (ISODATA clustering)

The project evaluates accuracy, workflow efficiency, and output quality — providing a practical framework for selecting the right method per project context.

---

## 🎯 Objectives

- Classify land cover into standard LULC categories (urban, vegetation, water, bare soil, etc.)
- Compare Supervised vs Unsupervised accuracy using confusion matrices
- Document workflow differences between GEE cloud processing and ArcGIS desktop
- Produce side-by-side output maps for visual comparison

---

## 🛰️ Data Sources

| Dataset | Source | Resolution | Purpose |
|---------|--------|-----------|---------|
| Sentinel-2 L2A | ESA Copernicus / GEE | 10m | Multi-band classification input |
| Training samples | Manual digitization | — | Supervised method only |
| Validation points | Stratified random sampling | — | Accuracy assessment |

---

## ⚙️ Methodology

### Method 1 — Supervised (Google Earth Engine)

```
1. Load Sentinel-2 collection → filter by date, cloud, AOI
2. Create composite image (median reducer)
3. Digitize training ROIs per LULC class in GEE
4. Train classifier: Random Forest (100 trees) or SVM
5. Apply classifier to composite → classified image
6. Accuracy assessment → confusion matrix → Overall Accuracy & Kappa
```

### Method 2 — Unsupervised (ArcGIS Pro)

```
1. Import Sentinel-2 bands into ArcGIS Pro mosaic dataset
2. Run ISO Cluster tool → define N clusters (e.g. 15)
3. Inspect cluster spectral signatures
4. Assign LULC class labels to each cluster (Maximum Likelihood)
5. Reclassify to final LULC categories
6. Accuracy assessment using same validation points
```

---

## 🗂️ File Structure

```
Land-Use-Classification/
├── README.md
├── supervised/
│   ├── GEE_classification_script.js   ← Full GEE code
│   ├── training_samples.geojson       ← ROI polygons
│   └── outputs/
│       ├── supervised_LULC_map.pdf
│       └── confusion_matrix_supervised.xlsx
├── unsupervised/
│   ├── ArcGIS_workflow_notes.md       ← Step-by-step ArcGIS guide
│   └── outputs/
│       ├── unsupervised_LULC_map.pdf
│       └── confusion_matrix_unsupervised.xlsx
└── comparison/
    ├── method_comparison.pdf          ← Side-by-side output maps
    └── accuracy_summary.xlsx          ← Both methods compared
```

---

## 📊 Accuracy Comparison

| Metric | Supervised (GEE) | Unsupervised (ArcGIS) |
|--------|-----------------|----------------------|
| Overall Accuracy | —% | —% |
| Kappa Coefficient | — | — |
| Urban Class Accuracy | —% | —% |
| Vegetation Class Accuracy | —% | —% |

> 📝 *Fill in from your confusion matrix outputs.*

---

## 🏷️ LULC Classes

| Class | Color Code | Description |
|-------|-----------|-------------|
| Urban / Built-up | `#e84040` | Impervious surfaces, buildings |
| Vegetation | `#3a9c3a` | Trees, shrubs, grassland |
| Cropland | `#c8e850` | Agricultural fields |
| Water | `#1e78c8` | Rivers, lakes, reservoirs |
| Bare Soil / Sand | `#d4b483` | Exposed soil, desert |
| Clouds / Shadow | `#b0b0b0` | Masked pixels |

---

## 🛠️ Tools & Software

![Google Earth Engine](https://img.shields.io/badge/Google_Earth_Engine-4285F4?style=flat-square&logo=google&logoColor=white)
![ArcGIS Pro](https://img.shields.io/badge/ArcGIS_Pro-2C7BB6?style=flat-square&logo=esri&logoColor=white)
![Sentinel-2](https://img.shields.io/badge/Sentinel--2_L2A-003247?style=flat-square&logoColor=white)
![JavaScript](https://img.shields.io/badge/GEE_JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

---

## 🔗 Navigation

[← Back to Portfolio](../README.md) &nbsp;|&nbsp; [Previous: Burn Severity Analysis](../Burn-Severity-Analysis) &nbsp;|&nbsp; [Category B: Cartography →](../../Category-B-Cartography)

---
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00e5a0,60:0a3d2e,100:0d1117&height=80&section=footer" width="100%"/>
</div>
