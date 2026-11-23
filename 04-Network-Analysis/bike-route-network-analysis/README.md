# Bike Route Network Analysis

**Category:** Network Analysis & Routing &nbsp;·&nbsp; **Location:** Mountainous region &nbsp;·&nbsp; **Year:** 2024  
**Client:** Upwork client (geomatics firm)  
**Tools & data:** ArcGIS Pro, Network Analyst, OpenStreetMap

![Alternative bike routes compared on a hillshade base](maps/bike-route-network-analysis-1.png)
*Figure 1. Alternative bike routes compared on a hillshade base*

## Overview
Used ArcGIS Pro and OpenStreetMap to calculate alternative routes for a bike tour where existing routing services fall short.

## Challenge
Existing bike-routing services gave poor routes in mountainous terrain. The client wanted alternatives tested against a real ride.

## Data
- OpenStreetMap road and path network
- Hillshade/DEM
- Reference GPS track from a test ride

## Approach
1. Built a network dataset from OpenStreetMap in ArcGIS Pro
2. Solved alternative routes between the same start and end points
3. Compared each route's length and travel time with the test-ride reference
4. Wrote up conclusions for improving bike routing

## Results
- Four alternative routes (A–D) compared by length and time on a hillshade base
- Showed where routing services fail in steep terrain and how routes can be improved

---
[← All projects](../../README.md) · [Portfolio website](https://abdul-haleem-khan-rs-gis.github.io/Geospatial_Portfolio/projects/bike-route-network-analysis.html)
