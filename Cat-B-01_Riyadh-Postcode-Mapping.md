<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,60:1a1a3d,100:6c63ff&height=160&section=header&text=Riyadh%20Postcode%20Mapping&fontSize=32&fontColor=ffffff&fontAlignY=45&desc=Geospatial%20Postal%20Boundaries%20in%20GeoJSON&descAlignY=65&descSize=14&descColor=c0b8ff" width="100%"/>

[![Category](https://img.shields.io/badge/Category-B%20Cartography-6c63ff?style=for-the-badge&labelColor=0d1117)](../)
[![Location](https://img.shields.io/badge/Area-Riyadh%2C%20Saudi%20Arabia-00b8d4?style=for-the-badge&labelColor=0d1117)]()
[![Format](https://img.shields.io/badge/Output-GeoJSON-000000?style=for-the-badge&logo=json&logoColor=white&labelColor=0d1117)]()
[![CRS](https://img.shields.io/badge/CRS-WGS84%20%2F%20UTM%2038N-8affd1?style=for-the-badge&labelColor=0d1117)]()

</div>

---

## 📌 Project Overview

This project creates accurate **geospatial postal code boundary data** for Riyadh, Saudi Arabia — delivered in GeoJSON format for direct web and GIS application use. The deliverable enables address validation systems, delivery logistics optimization, demographic analysis, and spatial business intelligence across the Saudi capital.

Saudi Arabia's postal system (Saudi Post / SPL) uses 5-digit postal codes. This project maps those boundaries as clean, topology-correct polygon geometries.

---

## 🎯 Objectives

- Digitize and attribute Riyadh postal code boundaries
- Ensure topological integrity (no overlaps, no gaps)
- Deliver in GeoJSON (WGS84) for immediate web use
- Include attribute table with postcode, district name, and region

---

## 🗺️ Study Area

| Attribute | Value |
|-----------|-------|
| City | Riyadh (الرياض) |
| Country | Saudi Arabia |
| CRS | WGS84 (EPSG:4326) |
| Projection (analysis) | UTM Zone 38N (EPSG:32638) |
| Approx. Coverage | Greater Riyadh Metropolitan Area |

---

## ⚙️ Methodology

```
1. REFERENCE DATA COLLECTION
   └── Saudi Post official postcode zones
   └── OSM administrative boundaries
   └── Google Maps / satellite imagery reference

2. DIGITIZATION
   └── Heads-up digitizing in QGIS / ArcGIS Pro
   └── Snap-to-feature for shared boundaries
   └── Topology check → fix overlaps and gaps

3. ATTRIBUTE TABLE
   └── postcode    (string, 5-digit)
   └── district    (Arabic + English name)
   └── region      (administrative zone)
   └── area_km2    (calculated geometry)

4. EXPORT
   └── GeoJSON (WGS84) → for web / APIs
   └── Shapefile         → for desktop GIS
   └── KML               → for Google Earth
```

---

## 🗂️ File Structure

```
Riyadh-Postcode-Mapping/
├── README.md
├── data/
│   ├── riyadh_postcodes.geojson      ← Main deliverable (WGS84)
│   ├── riyadh_postcodes.shp          ← Shapefile package
│   └── riyadh_postcodes.kml          ← Google Earth format
├── outputs/
│   ├── riyadh_postcode_map.pdf       ← Print-quality map
│   └── riyadh_postcode_map.png       ← Web export
└── docs/
    └── attribute_schema.md           ← Field descriptions
```

---

## 📋 GeoJSON Schema

```json
{
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [...]
  },
  "properties": {
    "postcode":   "11411",
    "district_en": "Al Olaya",
    "district_ar": "العليا",
    "region":     "Central",
    "area_km2":   12.4
  }
}
```

---

## 🛠️ Tools & Software

![QGIS](https://img.shields.io/badge/QGIS-589632?style=flat-square&logo=qgis&logoColor=white)
![ArcGIS Pro](https://img.shields.io/badge/ArcGIS_Pro-2C7BB6?style=flat-square&logo=esri&logoColor=white)
![GeoJSON](https://img.shields.io/badge/GeoJSON-000000?style=flat-square&logo=json&logoColor=white)
![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-7EBC6F?style=flat-square&logo=openstreetmap&logoColor=white)

---

## 🔗 Navigation

[← Back to Portfolio](../README.md) &nbsp;|&nbsp; [Category B: All Cartography Projects](../Category-B-Cartography) &nbsp;|&nbsp; [Next: National Park Style Map →](../National-Park-Style-Map)

---
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6c63ff,60:1a1a3d,100:0d1117&height=80&section=footer" width="100%"/>
</div>
