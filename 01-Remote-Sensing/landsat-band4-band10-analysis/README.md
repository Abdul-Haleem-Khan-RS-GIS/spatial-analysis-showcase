# Landsat Band 4 & Band 10 Surface Analysis

**Category:** Remote Sensing & Earth Observation &nbsp;·&nbsp; **Location:** Study area &nbsp;·&nbsp; **Year:** 2024  
**Client:** Upwork client (geomatics firm)  
**Tools & data:** Landsat, ArcGIS Pro

*No public map for this project: the deliverable was data or code (see Deliverables).*

## Overview
Analysed Band 4 (red) and Band 10 (thermal) pixel values to tell apart clouds, water, snow and land-cover types including forest, mountains and slopes.

## Challenge
Show how visible red (Band 4) and thermal infrared (Band 10) values can be used to tell clouds, water, snow, forest, mountains and slopes apart.

## Data
- Landsat 8/9 scene with Band 4 (red) and Band 10 (thermal infrared)
- Sample points for cloud, forest, lake, mountain and slope classes

## Approach
1. Sampled pixel values for each class in Band 4 and Band 10
2. Charted value ranges by class to compare reflectance and thermal emission
3. Interpreted the differences physically: reflectivity, heat retention, altitude and sun exposure
4. Wrote a companion report recommending the right sensor for five use cases (Sentinel-2, Sentinel-1, MODIS, WorldView-3, Meteosat)

## Results
- Clouds: highest Band 4 values (33,254–35,173) but only moderate Band 10 values (16,972–17,897)
- Lakes: low Band 4 (5,519–8,322) but the highest Band 10 values (17,065–19,795), because water retains heat
- South-facing slopes are warmer and brighter than north-facing ones; forests sit in a narrow thermal range (17,730–18,189)
- Snow and cloud look alike in Band 4 but can be separated in Band 10, where snow is much colder

## Deliverables

- Report on the Analysis of Band 4 & 10.pdf
- Report Evaluating Remote Sensing Data for Specific Use Cases.pdf

---
[← All projects](../../README.md) · [Portfolio website](https://abdul-haleem-khan-rs-gis.github.io/Geospatial_Portfolio/projects/landsat-band4-band10-analysis.html)
