# Burn Severity Analysis (NBR / dNBR)

**Category:** Remote Sensing & Earth Observation &nbsp;·&nbsp; **Location:** Eastern Australia (Sentinel-2, UTM zone 56S) &nbsp;·&nbsp; **Year:** 2024  
**Client:** Upwork client (geomatics firm)  
**Tools & data:** Sentinel-2, QGIS, Google Earth Engine, Copernicus EMS

![Delta Normalized Burn Ratio (dNBR) classified into five burn-severity classes](maps/burn-severity-sentinel2-1.png)
*Figure 1. Delta Normalized Burn Ratio (dNBR) classified into five burn-severity classes*

## Overview
Mapped wildfire damage from pre- and post-fire Sentinel-2 imagery using false-colour composites, the Normalized Burn Ratio (NBR) and delta NBR (dNBR).

## Challenge
Map how badly a wildfire burned the landscape in late 2019 and check whether vegetation was recovering, using freely available satellite data alongside the official Copernicus Emergency Management Service (CEMS) burn-extent map.

## Data
- Sentinel-2 Level-2A scenes for January 2019, October 2019, November 2019 and January 2020 (WGS 84 / UTM zone 56S, EPSG:32756)
- Copernicus Emergency Management Service (CEMS) burn-extent map, supplied as an image
- Google Earth Engine Sentinel-2 collection for index calculation

## Approach
1. Loaded the True Colour Images (B4-B3-B2) for all four dates and compared pre-fire, active-fire and post-fire conditions
2. Georeferenced the CEMS map to the Sentinel-2 grid with 6 ground control points, a 2nd-order polynomial transformation and nearest-neighbour resampling (RMS error 0.82)
3. Built NIR-Red-Green false-colour composites (B8-B4-B3) to separate healthy vegetation from burn scars and smoke
4. Uploaded the georeferenced CEMS map to Google Earth Engine as an asset and displayed it with the same Sentinel-2 scenes
5. Calculated the Normalized Burn Ratio, NBR = (B8 − B12) / (B8 + B12), for pre- and post-fire dates and derived dNBR
6. Classified dNBR into five severity classes (unburned to high severity) and produced the map and report

## Results
- October 2019 imagery shows dense, intact vegetation; November 2019 shows extensive burn scars and smoke plumes
- dNBR highlights large contiguous patches of high burn severity in the November 2019 observation
- By January 2020 parts of the burned area show regrowth, with clear contrast between burnt and unburnt zones
- Recommended SWIR (B12) for hotspot and burn-scar detection and NIR (B8) for vegetation health during an active fire

## Deliverables

- Task 4 Remote Sensing Data Analysis Report.pdf

---
[← All projects](../../README.md) · [Portfolio website](https://abdul-haleem-khan-rs-gis.github.io/Geospatial_Portfolio/projects/burn-severity-sentinel2.html)
