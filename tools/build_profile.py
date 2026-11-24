import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from projects import CATS
P = json.load(open(os.path.join(os.path.dirname(__file__), "projects_built.json")))
OUT = sys.argv[1]
SITE = "https://abdul-haleem-khan-rs-gis.github.io/Geospatial_Portfolio/"
GH = "https://github.com/Abdul-Haleem-Khan-RS-GIS/spatial-analysis-showcase/tree/main/"
RAW = "https://raw.githubusercontent.com/Abdul-Haleem-Khan-RS-GIS/spatial-analysis-showcase/main/"

feat = [p for p in P if p.get("featured") and p["maps"]][:6]
cells = []
for p in feat:
    img = RAW + p["maps"][0].replace(" ", "%20")
    cells.append(f'<td width="33%" valign="top"><a href="{SITE}projects/{p["slug"]}.html"><img src="{img}" alt="{p["title"]}"></a><br><b>{p["title"]}</b><br><sub>{p["where"]} · {p["year"]}</sub></td>')
rows = "".join("<tr>" + "".join(cells[i:i+3]) + "</tr>" for i in range(0, len(cells), 3))

others = [p for p in P if p.get("featured") and not p["maps"]]
md = f"""# Abdul Haleem Khan

**GIS Engineer & Remote Sensing Specialist** · Lahore, Pakistan

[Portfolio]({SITE}) · [Upwork](https://www.upwork.com/freelancers/abdulhaleemrsgis) · [LinkedIn](https://www.linkedin.com/in/abdul-haleem-khan-rs-gis-specialist) · [Email](mailto:abdulhaleemk03@gmail.com)

I turn satellite imagery and spatial data into maps and analysis people can act on. I have 4+ years in GIS: municipal GIS engineer in Al-Qassim, Saudi Arabia; GIS analyst for city comprehensive plans at Shehersaaz; NESPAK; and 33 freelance jobs on Upwork (4.8★ from 14 reviews).

**Work I do:** satellite image analysis (Sentinel-2, Landsat; NDVI, NBR/dNBR, land-cover classification) · site suitability and flood-risk MCDA · cartography and thematic mapping · GIS data engineering (digitising, geocoding, GIS↔CAD, KMZ/GeoJSON)

**Tools:** ArcGIS Pro · QGIS · Google Earth Engine · ENVI · ERDAS Imagine · Global Mapper · AutoCAD · Python (ArcPy, GeoPandas, Rasterio, GDAL) · PostGIS

## Selected maps

<table>{rows}</table>

{("Also: " + " · ".join(f"[{p['title']}]({GH}{p['dir']})" for p in others)) if others else ""}

**All {len(P)} projects by category:** [spatial-analysis-showcase](https://github.com/Abdul-Haleem-Khan-RS-GIS/spatial-analysis-showcase)

## Repositories

| Repo | What it is |
|---|---|
| [spatial-analysis-showcase](https://github.com/Abdul-Haleem-Khan-RS-GIS/spatial-analysis-showcase) | Final maps, write-ups and data for every project, by category |
| [Geospatial_Portfolio]({SITE}) | Source of my portfolio website |
"""
open(OUT, "w").write(md)
print("profile README:", len(feat), "featured with maps,", len(others), "text-only")
