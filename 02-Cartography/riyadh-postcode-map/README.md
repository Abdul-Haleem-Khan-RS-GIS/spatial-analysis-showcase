# Riyadh Postal Code Boundaries (GeoJSON)

**Category:** Cartography & Thematic Mapping &nbsp;·&nbsp; **Location:** Riyadh, Saudi Arabia &nbsp;·&nbsp; **Year:** 2025  
**Client:** Upwork client, Saudi Arabia  
**Tools & data:** QGIS, ArcGIS Pro, GeoJSON

![Postal-code boundaries of Riyadh over satellite imagery](maps/riyadh-postcode-map-1.png)
*Figure 1. Postal-code boundaries of Riyadh over satellite imagery*

## Overview
Delineated Riyadh postal code boundaries and delivered them as GeoJSON ready for GIS platforms and web maps.

## Challenge
The client needed Riyadh's postal-code boundaries as a clean dataset that works in GIS software and web maps.

## Data
- Postal-code reference boundaries for Riyadh
- District names for every zone
- Satellite basemap for checking

## Approach
1. Delineated the postal-code zones in QGIS and ArcGIS Pro, in WGS 84 / UTM zone 38N (EPSG:32638)
2. Attached the district name (Dist_Name) and postal code (Zip_Code) to every polygon
3. Checked attributes and topology so neighbouring zones share edges, with no gaps or overlaps
4. Exported to GeoJSON and shapefile for web and GIS use

## Results
- 996 postal-code polygons carrying 988 distinct postal codes across 177 named districts
- The layer covers about 3,760 km² of Riyadh, from roughly 46.3°E to 47.1°E and 24.3°N to 25.2°N
- Delivered as GeoJSON and shapefile, ready for web maps and GIS platforms

## Deliverables

- Riyadh_ZIP.zip

---
[← All projects](../../README.md) · [Portfolio website](https://abdul-haleem-khan-rs-gis.github.io/Geospatial_Portfolio/projects/riyadh-postcode-map.html)
