<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,60:2a1a00,100:e67e22&height=160&section=header&text=Employment%20Density%20Analysis&fontSize=30&fontColor=ffffff&fontAlignY=45&desc=Job%20Cluster%20Mapping%20with%20Kernel%20Density%20Estimation&descAlignY=65&descSize=14&descColor=f0c08a" width="100%"/>

[![Category](https://img.shields.io/badge/Category-C%20Urban%20GIS-e67e22?style=for-the-badge&labelColor=0d1117)](../)
[![Method](https://img.shields.io/badge/Method-Kernel%20Density%20Estimation-ff9800?style=for-the-badge&labelColor=0d1117)]()
[![Platform](https://img.shields.io/badge/Platform-ArcGIS%20Pro-2C7BB6?style=for-the-badge&logo=esri&logoColor=white&labelColor=0d1117)]()
[![Output](https://img.shields.io/badge/Output-Heatmap%20Raster-f0c08a?style=for-the-badge&labelColor=0d1117)]()

</div>

---

## 📌 Project Overview

This project applies **Kernel Density Estimation (KDE)** to map the spatial concentration of employment across an urban area — revealing job hotspots, employment corridors, and underserved zones. The output is a continuous density surface that goes beyond simple point mapping to show the true geographic distribution of economic activity.

Employment density maps are essential tools for transit planning, zoning decisions, economic development strategy, and real estate investment analysis.

---

## 🎯 Objectives

- Aggregate employment data to geocoded business/workplace locations
- Apply KDE to produce a smooth employment density surface
- Identify primary and secondary employment clusters
- Compare employment density against population density (optional overlay)
- Deliver a professional heatmap layout for planning use

---

## ⚙️ Methodology

```
1. DATA PREPARATION
   └── Business register / employment dataset (point locations)
   └── Attribute: number of employees per location
   └── Geocode any address-only records
   └── Clean and validate: remove duplicates, outliers

2. KERNEL DENSITY ESTIMATION
   └── Tool: ArcGIS Spatial Analyst → Kernel Density
   └── Input: employment point layer
   └── Population field: employee_count (weighted KDE)
   └── Search radius (bandwidth): tested 500m / 1km / 2km
   └── Output cell size: 50m raster
   └── Area units: square kilometers

3. CLASSIFICATION & SYMBOLOGY
   └── Classify output raster (Natural Breaks, 7 classes)
   └── Apply diverging or sequential color ramp
   └── Transparency blending over basemap

4. CLUSTER IDENTIFICATION
   └── Identify top 3–5 employment hotspots by density value
   └── Delineate clusters using Focal Statistics smoothing
   └── Label major employment zones

5. OUTPUT
   └── Density raster (GeoTIFF)
   └── Map layout with scale, legend, north arrow
   └── Summary statistics table
```

---

## 🗂️ File Structure

```
Employment-Density-Analysis/
├── README.md
├── data/
│   ├── employment_points.shp          ← Geocoded workplaces + employee counts
│   └── study_area_boundary.shp        ← Analysis extent
├── analysis/
│   ├── KDE_output_500m.tif            ← Bandwidth test 1
│   ├── KDE_output_1000m.tif           ← Bandwidth test 2 (selected)
│   └── bandwidth_comparison.xlsx      ← Sensitivity analysis
├── outputs/
│   ├── employment_density_map.pdf     ← Final print layout
│   └── employment_density_map.png     ← Web export
└── docs/
    └── bandwidth_selection.md         ← KDE parameter decisions
```

---

## 📊 Key Findings

| Employment Zone | Location | Peak Density (jobs/km²) |
|-----------------|----------|------------------------|
| Primary CBD cluster | — | — |
| Secondary cluster | — | — |
| Industrial zone | — | — |
| Emerging cluster | — | — |

> 📝 *Fill in from your KDE output statistics.*

---

## 🔬 KDE Parameter Decisions

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Bandwidth | 1,000m | Captures neighborhood-scale clustering |
| Cell size | 50m | Sufficient detail, manageable file size |
| Population field | `employee_count` | Weighted by jobs, not just presence |
| Kernel type | Quartic (default) | Smooth, bell-shaped influence |

---

## 🛠️ Tools & Software

![ArcGIS Pro](https://img.shields.io/badge/ArcGIS_Pro-2C7BB6?style=flat-square&logo=esri&logoColor=white)
![Spatial Analyst](https://img.shields.io/badge/Spatial_Analyst_Extension-2C7BB6?style=flat-square&logo=esri&logoColor=white)
![Python](https://img.shields.io/badge/Python_ArcPy-3776AB?style=flat-square&logo=python&logoColor=white)

---

## 🔗 Navigation

[← Back to Portfolio](../README.md) &nbsp;|&nbsp; [Previous: Business Logistics](../Business-Logistics-Optimization) &nbsp;|&nbsp; [Next: Daycare Accessibility →](../Daycare-Accessibility)

---
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:e67e22,60:2a1a00,100:0d1117&height=80&section=footer" width="100%"/>
</div>
