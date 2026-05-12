<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,60:1a3a3a,100:00b8d4&height=200&section=header&text=Daycare%20Accessibility%20Analysis&fontSize=30&fontColor=ffffff&fontAlignY=36&desc=Social%20Infrastructure%20Gap%20Mapping%20%E2%80%94%20Zurich&descAlignY=55&descSize=14&descColor=a0e8f0" width="100%"/>

[![Category](https://img.shields.io/badge/Category-C%20Urban%20GIS-00b8d4?style=for-the-badge&labelColor=0d1117)](../)
[![Location](https://img.shields.io/badge/Area-Zurich%2C%20Switzerland-e30613?style=for-the-badge&labelColor=0d1117)]()
[![Method](https://img.shields.io/badge/Method-Service%20Area%20Analysis-00e5a0?style=for-the-badge&labelColor=0d1117)]()
[![Platform](https://img.shields.io/badge/Platform-QGIS-589632?style=for-the-badge&logo=qgis&logoColor=white&labelColor=0d1117)]()

</div>

---

## 📌 Project Overview

This project maps **access to daycare services** across Zurich, identifying which residential areas fall within acceptable travel distance of a daycare facility and critically which areas are **underserved**. The analysis uses service area / catchment modeling on the pedestrian road network to define realistic walking access zones.

Results directly support urban social policy: planners can use this output to prioritize new facility locations, identify equity gaps, and report on childcare access by district.

---

## 🎯 Objectives

- Map all daycare facility locations across Zurich
- Define service areas (catchments) at 5, 10, and 15-minute walking distance
- Identify residential areas outside all catchment zones (service gaps)
- Overlay population density to quantify the number of underserved residents
- Deliver a policy-ready map and gap report

---

## 🗺️ Study Area

| Attribute | Value |
|-----------|-------|
| City | Zürich, Switzerland |
| Unit of analysis | Statistical quarters (Quartiere) |
| CRS | CH1903+ / LV95 (EPSG:2056) |
| Network type | Pedestrian / walking |
| Travel time thresholds | 5 min · 10 min · 15 min walk |

---

## ⚙️ Methodology

```
1. DATA COLLECTION
   └── Zurich Open Data: daycare facility locations (point layer)
   └── OSM pedestrian network (footpaths, sidewalks, crossings)
   └── Residential building / population layer
   └── District boundary polygons

2. NETWORK PREPARATION
   └── Import OSM pedestrian network to QGIS
   └── Build network topology (QNEAT3 or ORS Tools plugin)
   └── Set average walking speed: 5 km/h
   └── Convert time thresholds: 5min=417m, 10min=833m, 15min=1250m

3. SERVICE AREA ANALYSIS
   └── Generate isochrone polygons (5/10/15 min) from each daycare
   └── Dissolve overlapping catchments per time band
   └── Produce three nested service area polygons

4. GAP ANALYSIS
   └── Erase service areas from study area extent → gap polygons
   └── Intersect gaps with residential population layer
   └── Quantify: population in gap zones per district

5. OUTPUT
   └── Service area map with gap zones highlighted
   └── District-level accessibility score table
   └── Recommendations for new facility locations
```

---

## 🗂️ File Structure

```
Daycare-Accessibility/
├── README.md
├── data/
│   ├── daycare_locations.geojson      ← Facility points
│   ├── zurich_pedestrian_network.shp  ← OSM walking network
│   ├── zurich_population.shp          ← Residential population
│   └── zurich_districts.geojson       ← Administrative boundaries
├── analysis/
│   ├── service_area_5min.shp          ← 5-minute catchment
│   ├── service_area_10min.shp         ← 10-minute catchment
│   ├── service_area_15min.shp         ← 15-minute catchment
│   └── gap_zones.shp                  ← Underserved areas
├── outputs/
│   ├── daycare_accessibility_map.pdf  ← Final map layout
│   └── gap_analysis_report.xlsx       ← District gap statistics
└── docs/
    └── policy_recommendations.md      ← Suggested new locations
```

---

## 📊 Accessibility Results

| District | Daycares | Pop within 10 min walk | Gap Population | Coverage |
|----------|----------|----------------------|----------------|----------|
| District 1 | — | — | — | —% |
| District 2 | — | — | — | —% |
| District 3 | — | — | — | —% |
| *All districts* | — | — | — | —% |

> 📝 *Fill in from your service area intersection analysis.*

---

## 🛠️ Tools & Software

![QGIS](https://img.shields.io/badge/QGIS-589632?style=flat-square&logo=qgis&logoColor=white)
![QNEAT3](https://img.shields.io/badge/QNEAT3_Plugin-589632?style=flat-square&logo=qgis&logoColor=white)
![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-7EBC6F?style=flat-square&logo=openstreetmap&logoColor=white)
![ArcGIS Pro](https://img.shields.io/badge/ArcGIS_Pro-2C7BB6?style=flat-square&logo=esri&logoColor=white)

---
![Alt Map](https://github.com/Abdul-Haleem-Khan-RS-GIS/spatial-analysis-showcase/blob/6da8527e967e96cc006559a79c6ba58d6140cab8/Category-C-Urban-GIS/Daycare-Accessibility/daycare_accessibility_mapdaycare_accessibility_map.png)

## 🔗 Navigation

[← Back to Portfolio](../README.md) &nbsp;|&nbsp; [Previous: Employment Density](../Employment-Density-Analysis) &nbsp;|&nbsp; [Category D: Network GIS →](../../Category-D-Network-GIS)

---
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00b8d4,60:1a3a3a,100:0d1117&height=80&section=footer" width="100%"/>
</div>
