# Global Mapper Script: Export Layers to CSV

**Category:** GIS Data Engineering & CAD &nbsp;·&nbsp; **Location:** United Kingdom &nbsp;·&nbsp; **Year:** 2024  
**Client:** Futurewise Aerial  
**Tools & data:** Global Mapper scripting

*No public map for this project: the deliverable was data or code (see Deliverables).*

## Overview
Global Mapper script that exports multiple layers to separate CSV files, with a how-to guide.

## Challenge
The client needed to export several shapefile layers to separate CSV files in one go instead of by hand.

## Data
- Four shapefile layers (Layer1 to Layer4) supplied by the client
- Point features in England, around 53.3°N, 1.0°W

## Approach
1. Wrote a Global Mapper script: SET_DIR, then IMPORT → EXPORT_VECTOR TYPE=CSV → UNLOAD_ALL for each layer
2. Tested the export and delivered sample CSVs
3. Wrote a step-by-step guide explaining every command

## Results
- One script replaces four manual exports: each layer is imported, written to its own CSV and unloaded
- Each CSV holds 99 points with longitude and latitude in degrees-minutes-seconds and in decimal degrees (X, Y), plus elevation, name and label fields
- Delivered the script, four sample CSV outputs and a step-by-step guide to every command

## Deliverables

- Global Mapper Script to export multiple layers as CSV files.pdf
- Export multiple layers in csv.docx
- 1.csv
- 2.csv
- 3.csv
- 4.csv

---
[← All projects](../../README.md) · [Portfolio website](https://abdul-haleem-khan-rs-gis.github.io/Geospatial_Portfolio/projects/global-mapper-csv-export-script.html)
