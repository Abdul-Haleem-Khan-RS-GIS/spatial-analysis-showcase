# Flood Susceptibility with AHP: Umluj Coastal Catchments (Google Earth Engine)

**Category:** Urban GIS & Site Suitability &nbsp;·&nbsp; **Location:** Umluj city and surroundings, Saudi Arabia &nbsp;·&nbsp; **Year:** 2025 project · AHP extension 2026  
**Client:** Based on my project for Sadeem International Company, Saudi Arabia (5.0★ review)  
**Tools & data:** Google Earth Engine (JavaScript), AHP, MCDA, MERIT Hydro HAND, Copernicus DEM, ESA WorldCover

![Flood susceptibility of the Umluj coastal catchments from the AHP weighted overlay](maps/umluj-flood-susceptibility-ahp-1.jpg)
*Figure 1. Flood susceptibility of the Umluj coastal catchments from the AHP weighted overlay*

![The five flood factors with their AHP weights, and the 1–5 reclassification rules](maps/umluj-flood-susceptibility-ahp-2.jpg)
*Figure 2. The five flood factors with their AHP weights, and the 1–5 reclassification rules*

![AHP pairwise comparison matrix with consistency check, and area by susceptibility class (AHP vs equal weights)](maps/umluj-flood-susceptibility-ahp-3.jpg)
*Figure 3. AHP pairwise comparison matrix with consistency check, and area by susceptibility class (AHP vs equal weights)*

![Sensitivity test: AHP weights vs equal weights](maps/umluj-flood-susceptibility-ahp-4.jpg)
*Figure 4. Sensitivity test: AHP weights vs equal weights*

## Overview
Flood susceptibility map of the Umluj coastal catchments built with the Analytic Hierarchy Process (AHP): five factors weighted by pairwise comparison (CR = 0.018), combined in Google Earth Engine from open global data, with a sensitivity test against equal weights.

## Challenge
Purpose of the original 2025 project for Sadeem International Company: an environmental assessment to decide where to install flood sensors around Umluj. That map combined flood factors in a weighted overlay. Weights chosen by judgement are hard to defend, so I rebuilt the analysis with the Analytic Hierarchy Process (AHP). It gives every weight a documented pairwise comparison and a consistency check, and the whole model runs from open global data that anyone can reproduce.

## Data
- Study area: the five HydroSHEDS level-8 basins draining to the coast at and around Umluj (1,999 km²); the original client AOI file was not delivered, so a watershed boundary is used
- Copernicus GLO-30 DEM (30 m): elevation and slope
- MERIT Hydro (90 m): HAND (height above nearest drainage) and upstream area; channels draining at least 5 km²
- ESA WorldCover 2021 (10 m): land cover
- Sentinel-2 2023 composite as the map background

## Approach
1. Delineated the study area from HydroSHEDS level-8 basins, so it follows real catchments rather than an arbitrary box
2. Derived five flood factors: HAND, distance to drainage, slope, elevation and land cover
3. Reclassified each factor to a 1–5 susceptibility score with breaks set from its distribution in the study area (for example HAND under 3 m = 5, over 35 m = 1)
4. Built the AHP pairwise comparison matrix on Saaty's 1–9 scale and derived the weights: HAND 43.4%, distance to drainage 27.1%, slope 17.1%, elevation 7.5%, land cover 4.8%
5. Checked consistency: λmax 5.079, CI 0.020, CR 0.018, well below the 0.10 limit
6. Combined the factors in a weighted overlay and classified the index into five classes, from very low to very high
7. Ran a sensitivity test with equal weights, measured built-up exposure with WorldCover, and set up 30 m GeoTIFF and shapefile exports

## Results
- Very high susceptibility covers 238 km² (12%) and high 436 km² (22%), concentrated along the wadi network and the low coastal plain around Umluj
- 68% of built-up land in the catchments (10.9 of 16.1 km²) falls in the high or very high classes
- Sensitivity: AHP and equal weights give the same class for 71% of the area, but AHP identifies about 3× more very-high land (238 vs 75 km²) along the drainage lines, where flash floods actually run
- Consistent with the original client map: wadi channels and the coastal plain are the highest-risk zones, and the elevated eastern ground is lowest

## Links

- [Open in the Earth Engine Code Editor](https://code.earthengine.google.com/d24d6fb92d7d0dfc0040e81da7baff01)
- [View the script on GitHub](https://github.com/Abdul-Haleem-Khan-RS-GIS/spatial-analysis-showcase/blob/main/03-Urban-GIS-and-Suitability/umluj-flood-susceptibility-ahp/code/umluj_flood_susceptibility_ahp.js)
- [See the original client project](https://abdul-haleem-khan-rs-gis.github.io/Geospatial_Portfolio/projects/umluj-flood-risk-mcda.html)

## Deliverables

- code/umluj_flood_susceptibility_ahp.js (full Earth Engine script)
- Maps: susceptibility, factor panel, AHP matrix and class areas, sensitivity test

---
[← All projects](../../README.md) · [Portfolio website](https://abdul-haleem-khan-rs-gis.github.io/Geospatial_Portfolio/projects/umluj-flood-susceptibility-ahp.html)
