<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,60:2d1b4a,100:9b59b6&height=200&section=header&text=Business%20Logistics%20Optimization&fontSize=28&fontColor=ffffff&fontAlignY=36&desc=Employee%20%E2%80%93%20Client%20Spatial%20Strategy%20%E2%80%94%20Switzerland&descAlignY=55&descSize=14&descColor=d7b8f0" width="100%"/>

[![Category](https://img.shields.io/badge/Category-C%20Urban%20GIS-9b59b6?style=for-the-badge&labelColor=0d1117)](../)
[![Location](https://img.shields.io/badge/Area-Switzerland-e30613?style=for-the-badge&labelColor=0d1117)]()
[![Type](https://img.shields.io/badge/Analysis-Spatial%20Optimization-00b8d4?style=for-the-badge&labelColor=0d1117)]()
[![Platform](https://img.shields.io/badge/Platform-ArcGIS%20Pro-2C7BB6?style=for-the-badge&logo=esri&logoColor=white&labelColor=0d1117)]()

</div>

---

## 📌 Project Overview

A **private-sector spatial analysis project** for a Swiss business client — optimizing the geographic assignment between employees and clients to minimize total travel time and cost. This is a real-world operations problem solved entirely through GIS spatial analysis.

By mapping employee home locations and client site locations together, and applying proximity and network-based assignment logic, the project delivers an optimized allocation strategy that reduces unnecessary travel across the Swiss road network.

---

## 🎯 Objectives

- Map employee and client locations across Switzerland
- Calculate travel distances and times via road network
- Identify inefficient current assignments
- Propose an optimized employee–client allocation
- Visualize the before/after difference in a comparison map

---

## 🗺️ Study Area

| Attribute | Value |
|-----------|-------|
| Country | Switzerland |
| Transport network | Swiss road network (OSM) |
| CRS | CH1903+ / LV95 (EPSG:2056) |
| Analysis type | Origin–Destination travel optimization |

---

## ⚙️ Methodology

```
1. DATA PREPARATION
   └── Geocode employee home addresses → point layer
   └── Geocode client site addresses  → point layer
   └── Load Swiss road network (OSM) into Network Dataset

2. OD COST MATRIX
   └── ArcGIS Network Analyst: OD Cost Matrix tool
   └── Calculate travel time (mins) and distance (km)
   └── For every employee → every client combination
   └── Output: full OD matrix table

3. CURRENT STATE ANALYSIS
   └── Map existing assignments
   └── Calculate total travel burden (sum of times)
   └── Identify inefficient long-distance assignments

4. OPTIMIZATION
   └── Apply nearest-available assignment algorithm
   └── Balance workload per employee (max clients per person)
   └── Minimize total network travel time

5. OUTPUT
   └── Optimized assignment table
   └── Spider diagram: employee → assigned clients
   └── Before/after comparison map and statistics
```

---

## 🗂️ File Structure

```
Business-Logistics-Optimization/
├── README.md
├── data/
│   ├── employees_geocoded.shp         ← Employee locations
│   ├── clients_geocoded.shp           ← Client site locations
│   └── switzerland_roads_osm.shp      ← Road network
├── analysis/
│   ├── OD_matrix_current.xlsx         ← Current assignment costs
│   └── OD_matrix_optimized.xlsx       ← Optimized assignments
├── outputs/
│   ├── current_assignment_map.pdf     ← Before map
│   ├── optimized_assignment_map.pdf   ← After map
│   └── comparison_statistics.xlsx     ← Travel time savings
└── docs/
    └── methodology_notes.md           ← Analysis decisions
```

---

## 📊 Results Summary

| Metric | Before Optimization | After Optimization |
|--------|--------------------|--------------------|
| Total travel time (all routes) | — hrs | — hrs |
| Avg. travel time per visit | — mins | — mins |
| Longest single assignment | — km | — km |
| Estimated cost saving | — | —% |

> 📝 *Update with values from your OD matrix analysis.*

---

## 🛠️ Tools & Software

![ArcGIS Pro](https://img.shields.io/badge/ArcGIS_Pro-2C7BB6?style=flat-square&logo=esri&logoColor=white)
![Network Analyst](https://img.shields.io/badge/Network_Analyst-2C7BB6?style=flat-square&logo=esri&logoColor=white)
![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-7EBC6F?style=flat-square&logo=openstreetmap&logoColor=white)
![Python](https://img.shields.io/badge/Python_ArcPy-3776AB?style=flat-square&logo=python&logoColor=white)

---

![Alt Map](https://github.com/Abdul-Haleem-Khan-RS-GIS/spatial-analysis-showcase/blob/bb0d630d1521b877081e49634ba6647b731799a4/Category-C-Urban-GIS/Business-Logistics-Optimization/optimized_assignment_map.png)

## 🔗 Navigation

[← Back to Portfolio](../README.md) &nbsp;|&nbsp; [Category C: All Urban GIS Projects](../Category-C-Urban-GIS) &nbsp;|&nbsp; [Next: Employment Density →](../Employment-Density-Analysis)

---
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:9b59b6,60:2d1b4a,100:0d1117&height=80&section=footer" width="100%"/>
</div>
