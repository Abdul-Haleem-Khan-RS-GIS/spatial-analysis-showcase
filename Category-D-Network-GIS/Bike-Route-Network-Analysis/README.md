<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,60:2a1a00,100:e67e22&height=240&section=header&text=Bike%20Route%20Network%20Analysis&fontSize=32&fontColor=ffffff&fontAlignY=32&desc=Optical%20Urban%20Cycling%20Terrain%20Network%20Analysis&descAlignY=50&descSize=16&descColor=ffffff" width="100%"/>
<div align="center">


[![Category](https://img.shields.io/badge/Category-D%20Network%20GIS-27ae60?style=for-the-badge&labelColor=0d1117)](../)
[![Method](https://img.shields.io/badge/Method-Network%20Analyst-2C7BB6?style=for-the-badge&logo=esri&logoColor=white&labelColor=0d1117)]()
[![Data](https://img.shields.io/badge/Network-OpenStreetMap-7EBC6F?style=for-the-badge&logo=openstreetmap&logoColor=white&labelColor=0d1117)]()
[![Terrain](https://img.shields.io/badge/Elevation-DEM%20Integrated-a8f0c0?style=for-the-badge&labelColor=0d1117)]()

<div align="left">


## 📌 Project Overview

This project uses **ArcGIS Network Analyst** to calculate optimal cycling routes across an urban area incorporating not just distance, but also terrain difficulty elevation gain, gradient, and path surface quality. Standard shortest-path routing ignores hills; this analysis weights routes by both travel distance and cycling effort.

The result is a set of truly optimal bike routes that a cyclist would choose in practice — minimizing a composite cost of distance, elevation gain, and road type. This approach is directly applicable to urban cycling infrastructure planning, bike-share deployment, and active transport policy.

---

## 🎯 Objectives

- Build a cycling-specific network dataset from OSM data
- Incorporate elevation data (DEM) as a route impedance factor
- Calculate optimal routes between key origin–destination pairs
- Compare: shortest distance route vs lowest effort route
- Map results with elevation profile visualization

---

## 🗺️ Study Area

| Attribute | Value |
|-----------|-------|
| City | Urban area (hilly terrain) |
| Network type | Cycling (road + dedicated cycle paths) |
| CRS | Local UTM projection |
| Elevation source | SRTM 30m DEM / local LiDAR |
| Route cost | Composite: distance + elevation impedance |

---

## ⚙️ Methodology

```
1. NETWORK DATA PREPARATION
   └── Download OSM road network for study area (osmnx / QGIS QuickOSM)
   └── Filter: roads accessible to cyclists
   └── Classify: cycle path / shared road / highway (avoid) / forbidden
   └── Assign base impedance: distance (meters)

2. ELEVATION INTEGRATION
   └── Load DEM (SRTM 30m or higher resolution)
   └── Extract elevation values along each road segment:
       Elevation at start node / end node → slope %
   └── Calculate: grade-adjusted impedance per segment
       Formula: impedance = distance × (1 + k × max(0, slope))
       where k = effort coefficient for uphill penalty

3. NETWORK DATASET BUILD
   └── Build Network Dataset in ArcGIS Pro
   └── Define impedance attribute: cycling_cost
   └── Add restrictions: no-cycling roads, one-ways
   └── Validate connectivity

4. ROUTE ANALYSIS
   └── Define Origin-Destination pairs (residential → POI)
   └── Solve: Closest Facility / Route solver
   └── Solve 1: minimum distance (ignore elevation)
   └── Solve 2: minimum effort (grade-adjusted cost)
   └── Compare results: distance saved vs effort saved

5. OUTPUT
   └── Route comparison map (distance vs effort)
   └── Elevation profile chart per route
   └── Route statistics table
```

---

## 🗂️ File Structure

```
Bike-Route-Network-Analysis/
├── README.md
├── data/
│   ├── osm_cycling_network.shp        ← OSM road network (filtered)
│   ├── DEM_study_area.tif             ← Elevation raster
│   └── OD_pairs.csv                   ← Origin–destination pairs
├── network/
│   └── cycling_network.gdb/           ← ArcGIS Network Dataset
├── analysis/
│   ├── routes_shortest_distance.shp   ← Result: distance-only
│   ├── routes_lowest_effort.shp       ← Result: grade-adjusted
│   └── route_comparison.xlsx          ← Stats per OD pair
├── outputs/
│   ├── bike_route_map.pdf             ← Final route map
│   ├── elevation_profiles.pdf         ← Profile charts
│   └── route_comparison_map.png       ← Web export
└── docs/
    └── impedance_formula.md           ← Grade-adjustment methodology
```

---

## 📊 Route Comparison Results

| Route | Distance (Shortest) | Distance (Effort-Optimal) | Elevation Gain Saved |
|-------|--------------------|--------------------------|--------------------|
| Route 1 | — km | — km | — m |
| Route 2 | — km | — km | — m |
| Route 3 | — km | — km | — m |

> 📝 *Fill in from your Network Analyst route output.*

---

## 🔬 Impedance Formula

The grade-adjusted cycling impedance applied per network edge:

```
cycling_cost = segment_length_m × (1 + 0.03 × max(0, slope_%))

Where:
  slope_%  = rise/run × 100
  0.03     = empirical uphill effort coefficient
  Downhill = no penalty (coasting assumed)
```

---

## 🛠️ Tools & Software

![ArcGIS Pro](https://img.shields.io/badge/ArcGIS_Pro-2C7BB6?style=flat-square&logo=esri&logoColor=white)
![Network Analyst](https://img.shields.io/badge/Network_Analyst_Extension-2C7BB6?style=flat-square&logo=esri&logoColor=white)
![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-7EBC6F?style=flat-square&logo=openstreetmap&logoColor=white)
![SRTM DEM](https://img.shields.io/badge/SRTM_DEM_30m-8B4513?style=flat-square&logoColor=white)
![Python](https://img.shields.io/badge/Python_ArcPy-3776AB?style=flat-square&logo=python&logoColor=white)

---
![Alt Map](https://github.com/Abdul-Haleem-Khan-RS-GIS/spatial-analysis-showcase/blob/44c74f47368bb03850b291e4c0d7104d87ac36ec/Category-D-Network-GIS/Bike-Route-Network-Analysis/route_comparison_map.png)


## 🔗 Navigation

[← Back to Portfolio](../README.md) &nbsp;|&nbsp; [Category D: All Network GIS Projects](../Category-D-Network-GIS)

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:27ae60,60:0a2a1a,100:0d1117&amp;height=80&amp;section=footer" width="100%"/>
</div>
