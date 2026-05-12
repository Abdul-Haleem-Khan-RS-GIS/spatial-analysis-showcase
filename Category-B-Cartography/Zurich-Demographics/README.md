<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,60:1a2a4a,100:4488cc&height=160&section=header&text=Zurich%20Demographics&fontSize=32&fontColor=ffffff&fontAlignY=45&desc=Thematic%20Mapping%20of%20Population%20Density&descAlignY=65&descSize=14&descColor=a0c8f0" width="100%"/>

[![Category](https://img.shields.io/badge/Category-B%20Cartography-4488cc?style=for-the-badge&labelColor=0d1117)](../)
[![Location](https://img.shields.io/badge/Area-Zurich%2C%20Switzerland-e30613?style=for-the-badge&labelColor=0d1117)]()
[![Type](https://img.shields.io/badge/Map%20Type-Choropleth-00b8d4?style=for-the-badge&labelColor=0d1117)]()
[![Platform](https://img.shields.io/badge/Platform-QGIS-589632?style=for-the-badge&logo=qgis&logoColor=white&labelColor=0d1117)]()

</div>

---

## 📌 Project Overview

A **thematic demographic mapping project** for the city of Zurich, Switzerland, visualizing population density across statistical districts using choropleth cartography. The project translates raw census attribute data into a clear, professional thematic map applying best-practice data classification and color theory.

This type of map is widely used in urban planning, real estate analysis, public health, and policy reporting.

---

## 🎯 Objectives

- Join Zurich population census data to administrative district boundaries
- Select optimal data classification method for the distribution
- Apply a sequential color ramp following cartographic best practices
- Design a professional map layout with legend, scale, and north arrow
- Export for both print and web delivery

---

## 🗺️ Study Area

| Attribute | Value |
|-----------|-------|
| City | Zürich (Zurich) |
| Country | Switzerland |
| Administrative unit | Statistical districts (Stadtkreise / Quartiere) |
| CRS | CH1903+ / LV95 (EPSG:2056) |
| Population | ~440,000 (city proper) |

---

## ⚙️ Methodology

```
1. DATA COLLECTION
   └── Zurich Open Data: district boundaries (.shp / GeoJSON)
   └── Census data: population per district (CSV)
   └── Reference layers: streets, water bodies (OSM)

2. DATA JOIN
   └── Join population CSV to district polygon layer by district ID
   └── Calculate population density: pop / area_km2

3. CLASSIFICATION METHOD SELECTION
   └── Examine data distribution (histogram, outliers)
   └── Select: Jenks Natural Breaks (optimal for skewed data)
   └── Alternative tested: Quantile / Equal Interval

4. SYMBOLOGY
   └── Sequential color ramp: light → dark (single hue)
   └── ColorBrewer palette: YlOrRd or Blues (5 classes)
   └── Ensure colorblind-safe palette

5. LAYOUT DESIGN
   └── Map frame, legend with class labels
   └── Scale bar, north arrow, source credits
   └── Inset map showing Zurich location in Switzerland

6. EXPORT
   └── PDF 300 DPI (A3 print layout)
   └── PNG 150 DPI (web/presentation)
```

---

## 🗂️ File Structure

```
Zurich-Demographics/
├── README.md
├── data/
│   ├── zurich_districts.geojson       ← District boundaries
│   ├── zurich_population.csv          ← Census data table
│   └── zurich_streets_osm.shp         ← Reference road layer
├── outputs/
│   ├── zurich_pop_density_map.pdf     ← Print layout (A3, 300 DPI)
│   └── zurich_pop_density_map.png     ← Web export
└── docs/
    └── classification_analysis.md     ← Jenks vs Quantile comparison
```

---

## 🎨 Cartographic Design Choices

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Classification | Jenks Natural Breaks | Best reflects natural groupings in skewed data |
| Color ramp | Sequential single-hue | Encodes magnitude (low → high density) |
| Classes | 5 | Balances detail and readability |
| Background | Neutral gray OSM basemap | Reduces visual competition with thematic layer |
| Projection | CH1903+ LV95 | Swiss national standard, minimal distortion |

---

## 🛠️ Tools & Software

![QGIS](https://img.shields.io/badge/QGIS-589632?style=flat-square&logo=qgis&logoColor=white)
![ArcGIS Pro](https://img.shields.io/badge/ArcGIS_Pro-2C7BB6?style=flat-square&logo=esri&logoColor=white)
![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-7EBC6F?style=flat-square&logo=openstreetmap&logoColor=white)

---

<h2>🖼️ Visual Preview</h2>

![Map Title](https://raw.githubusercontent.com/Abdul-Haleem-Khan-RS-GIS/spatial-analysis-showcase/main/Category-B-Cartography/Zurich-Demographics/zurich_pop_density_map.png)

---
## 🔗 Navigation

[← Back to Portfolio](../README.md) &nbsp;|&nbsp; [Previous: National Park Style Map](../National-Park-Style-Map) &nbsp;|&nbsp; [Category C: Urban GIS →](../../Category-C-Urban-GIS)

---
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:4488cc,60:1a2a4a,100:0d1117&height=80&section=footer" width="100%"/>
</div>
