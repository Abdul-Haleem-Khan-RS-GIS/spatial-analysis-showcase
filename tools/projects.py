# Single source of truth for the showcase repo READMEs and the portfolio website.
# Facts come only from Upwork contracts / portfolio items / project catalog as read on 2026-11-23.
# 'old' = path of an existing image in spatial-analysis-showcase (moved into the new folder).
# 'files' = deliverables to copy in from the user's Downloads once available.

CATS = {
    "remote-sensing": ("01-Remote-Sensing", "Remote Sensing & Earth Observation"),
    "cartography":    ("02-Cartography", "Cartography & Thematic Mapping"),
    "urban":          ("03-Urban-GIS-and-Suitability", "Urban GIS & Site Suitability"),
    "network":        ("04-Network-Analysis", "Network Analysis & Routing"),
    "data":           ("05-GIS-Data-Engineering-and-CAD", "GIS Data Engineering & CAD"),
    "planning":       ("06-Master-Planning-and-Municipal-GIS", "Master Plans & Municipal GIS"),
}

P = []
def add(**k): P.append(k)

# ---------------- 01 Remote sensing ----------------
add(slug="burn-severity-sentinel2", cat="remote-sensing", featured=True,
    title="Burn Severity Analysis (NBR / dNBR)", year="2024", client="Upwork client (geomatics firm)",
    where="Wildfire-affected landscape", tools=["Sentinel-2", "Google Earth Engine", "ArcGIS Pro"],
    summary="Mapped wildfire damage from pre- and post-fire Sentinel-2 imagery using false-colour composites, the Normalized Burn Ratio (NBR) and delta NBR (dNBR).",
    result="Showed significant burn damage in November 2019 and vegetation recovery by January 2020, supporting ecological monitoring and rehabilitation planning.",
    method=["Pre- and post-fire Sentinel-2 scenes", "False-colour composites for vegetation health", "NBR for each date, then dNBR", "Burn-severity classes and report"],
    old=["Category-A-Remote-Sensing/Burn-Severity-Analysis/burn_severity_map.png"],
    files=["Task 4 Remote Sensing Data Analysis Report.pdf"])
add(slug="gee-dixie-fire-lst-ndvi", cat="remote-sensing", featured=True,
    title="Dixie Fire 2021: Land Surface Temperature & NDVI in Google Earth Engine", year="2021 fire season",
    client="Independent Earth Engine analysis",
    where="Dixie Fire, Plumas County area, California, USA", tools=["Google Earth Engine (JavaScript)", "Landsat 8 C2 L2", "LST", "NDVI", "Time series"],
    summary="Google Earth Engine analysis of the 2021 Dixie Fire, California's largest single wildfire: cloud-masked Landsat 8 land surface temperature and NDVI, compared season to season against an unburned control ring, showing the burn scar ran about 8 °C hotter the next summer.",
    result="Earth Engine app with cloud-masked 2021 fire-season LST, summer 2022 vs 2020 LST and NDVI change maps, burn-scar vs control-ring statistics and charts, and 30 m GeoTIFF exports.",
    method=["Landsat 8 LST and NDVI in GEE"],
    files=["code/dixie_fire_lst_ndvi.js (full Earth Engine script)", "Maps: LST change, NDVI change, summer 2022 LST; summer comparison chart"],
    links=[("Open in the Earth Engine Code Editor", "https://code.earthengine.google.com/41b9b32b5c8690a4727865efe43eb71a"), ("View the script on GitHub", "https://github.com/Abdul-Haleem-Khan-RS-GIS/spatial-analysis-showcase/blob/main/01-Remote-Sensing/gee-dixie-fire-lst-ndvi/code/dixie_fire_lst_ndvi.js")])
add(slug="lulc-andijan-reservoir", cat="remote-sensing", featured=True,
    title="Land-Cover Classification: Supervised vs Unsupervised", year="2024", client="Upwork client (geomatics firm)",
    where="Andijan Reservoir, Uzbekistan / Kyrgyzstan", tools=["Sentinel-2", "Google Earth Engine", "Random Forest", "ArcGIS Pro"],
    summary="Classified land cover around the Andijan Reservoir from a Sentinel-2 scene of 13 April 2023, comparing unsupervised clustering with supervised Random Forest classification in Google Earth Engine.",
    result="Supervised Random Forest classification produced more detailed and accurate land-cover maps than unsupervised methods; separating mixed land-cover classes remains the main area to improve.",
    method=["Sentinel-2 scene, 13 Apr 2023", "ISO Cluster unsupervised classification (7 classes)", "Training samples + Random Forest in GEE", "Accuracy comparison and report"],
    old=["Category-A-Remote-Sensing/Land-Use-Classification/Supervised Classification.png",
         "Category-A-Remote-Sensing/Land-Use-Classification/Unsupervised Classification.png"],
    files=["Remote Sensing Image Classification Report.pdf"])
add(slug="landsat-band4-band10-analysis", cat="remote-sensing",
    title="Landsat Band 4 & Band 10 Surface Analysis", year="2024", client="Upwork client (geomatics firm)",
    where="Study area", tools=["Landsat", "ArcGIS Pro"],
    summary="Analysed Band 4 (red) and Band 10 (thermal) pixel values to tell apart clouds, water, snow and land-cover types including forest, mountains and slopes.",
    result="Report explaining temperature differences, cloud vs water separation and snow vs cloud discrimination, backed by pixel statistics.",
    method=["Landsat scene", "Pixel sampling on Band 4 and Band 10", "Class-by-class comparison", "Written report"],
    files=["Report on the Analysis of Band 4 & 10.pdf", "Report Evaluating Remote Sensing Data for Specific Use Cases.pdf"])
add(slug="aerial-image-manual-classification", cat="remote-sensing",
    title="Manual Land-Cover Classification of Aerial Imagery", year="2024", client="Upwork client (geomatics firm)",
    where="Aerial image tile", tools=["ArcGIS Pro", "Digitising"],
    summary="Produced a land-cover map of a high-resolution aerial image by manual interpretation and digitising, delivered as a map and shapefile.",
    result="Land-cover classification map plus attributed shapefile and method report.",
    method=["Visual interpretation of aerial image", "Polygon digitising by class", "Attribute coding", "Map layout + report"],
    files=["Landcover classification Map across the aerial image.jpg", "Manual Image Classification Report.pdf", "Manual_Classification SHP.rar"])
add(slug="los-angeles-urban-land-cover", cat="remote-sensing", study=True,
    title="Urban Land-Cover Classification of Los Angeles", year="2024", client="Practice study",
    where="Los Angeles, USA", tools=["ENVI", "Landsat", "Maximum Likelihood"],
    summary="Classified urban land cover across Los Angeles for 2022 and 2024 with Maximum Likelihood classification in ENVI, with accuracy assessment, presented as a report and slide deck.",
    result="Land-cover maps for 2022 and 2024, confusion-matrix accuracy assessment, written report and presentation.",
    method=["Satellite scene preparation", "Image classification in ENVI", "Accuracy review", "Report and slides"],
    files=["Classification of Urban Land Cover in Los Angeles Using Remote Sensing Techniques.pdf", "Classification of Urban Land Cover in Los Angeles.pptx"])
add(slug="ndvi-and-image-classification-studies", cat="remote-sensing", study=True,
    title="NDVI, Supervised & Unsupervised Classification Studies", year="2024", client="Practice studies",
    where="Various study areas", tools=["ENVI", "ArcGIS Pro", "Landsat"],
    summary="A set of short studies computing NDVI and running unsupervised and supervised image classification, each documented step by step.",
    result="Three illustrated reports covering NDVI, unsupervised and supervised classification workflows.",
    method=["NDVI from red/NIR bands", "Unsupervised clustering", "Supervised classification with training samples", "Reports"],
    files=["NDVI and Unsupervised Classification - Week 3 Lab-2.pdf", "Lab 4 Report.pdf"])
add(slug="landsat-thermal-and-image-analysis", cat="remote-sensing", study=True,
    title="Landsat 9 Thermal & Image Analysis", year="2024", client="Practice study",
    where="Southern California (Landsat 9 scene, June 2022)", tools=["Landsat 9", "ArcGIS Pro"],
    summary="Analysed a Landsat 9 Collection 2 scene (15 June 2022): band composites, thermal band interpretation and surface analysis.",
    result="Two illustrated reports on Landsat image analysis and thermal interpretation.",
    method=["Landsat 9 C2 L2 scene", "Band composites", "Thermal band analysis", "Reports"],
    files=["Landsat 2024 Image Analysis Assignment.pdf", "Thermal Lab- Week 2-1.pdf"])
add(slug="ndvi-summary-arcgis-pro", cat="remote-sensing",
    title="NDVI Map of Los Angeles County (Landsat 8)", year="2025", client="Upwork client",
    where="Los Angeles County, USA", tools=["Landsat 8", "ArcGIS Pro", "NDVI"],
    summary="Quick-turnaround NDVI computation from Landsat 8 for Los Angeles County, with a summary layout in ArcGIS Pro.",
    result="NDVI summary map and short report.",
    method=["Imagery input", "NDVI raster", "Classification and layout"],
    files=["Summary of Normalized Difference Vegetation Index (NDVI).pdf"])

# ---------------- 02 Cartography ----------------
add(slug="nps-map-redesign", cat="cartography", featured=True,
    title="U.S. National Park Service Map Redesign", year="2025", client="Upwork client",
    where="Rocky Mountain National Park, USA", tools=["ArcGIS Pro", "NPS open data"],
    summary="Replicated and improved an NPS park map, refining the colour scheme, symbology and labelling for a clearer, more usable map.",
    result="Redesigned map plus a report on cartographic improvements for the next generation of NPS maps.",
    method=["NPS open data", "Rebuild base map in ArcGIS Pro", "Colour, symbol and label redesign", "Report"],
    old=["Category-B-Cartography/National-Park-Style-Map/Rocky Mountain NPS Maps.jpg"],
    files=["Cartographic Improvements for the Next Generation of NPS Maps Report.pdf"])
add(slug="georgia-choropleth-classification", cat="cartography", featured=True,
    title="Choropleth Classification Comparison: Georgia", year="2025", client="Upwork client",
    where="Georgia, USA (159 counties)", tools=["ArcGIS 10.8", "U.S. Census data"],
    summary="Mapped U.S. Census population for Georgia's 159 counties four ways (Equal Interval, Quantile, Natural Breaks, Standard Deviation) with matching layouts.",
    result="Four-map series and a one-page analysis of how classification choice changes the story a map tells.",
    method=["Census population data", "Join to county boundaries", "Four classification methods", "Consistent layouts + report"],
    files=["Comparison of Population Distribution in Georgia Using Different Classification Methods.pdf"])
add(slug="reference-mapping-text-icons", cat="cartography",
    title="Reference Mapping with Text, Icons & Labels", year="2025", client="Upwork client",
    where="Reference map series", tools=["ArcGIS Pro"],
    summary="Two cartography projects on label placement, symbol design and icon use for reference maps.",
    result="Illustrated reports on effective reference mapping and on labelling and symbolising.",
    method=["Base data preparation", "Label classes and placement rules", "Icon/point symbology", "Reports"],
    files=["Report on Effective Reference Mapping Using Text and Icons_merged.pdf", "Labeling and Symbolizing Project.pdf"])
add(slug="riyadh-postcode-map", cat="cartography", featured=True,
    title="Riyadh Postal Code Boundaries (GeoJSON)", year="2025", client="Upwork client, Saudi Arabia",
    where="Riyadh, Saudi Arabia", tools=["QGIS", "ArcGIS Pro", "GeoJSON"],
    summary="Delineated Riyadh postal code boundaries and delivered them as GeoJSON ready for GIS platforms and web maps.",
    result="Postal-code polygon dataset (GeoJSON) and map.",
    method=["Reference boundary sources", "Delineate postcode polygons", "Attribute + topology check", "GeoJSON export"],
    old=["Category-B-Cartography/Riyadh-Postcode-Mapping/riyadh_postcode_map.png"],
    files=["Riyadh_ZIP.zip"])
add(slug="zurich-population-density", cat="cartography",
    title="Zurich Population Density, Ages 25–45", year="2023", client="Upwork client, Switzerland",
    where="Zurich, Switzerland", tools=["ArcGIS"],
    summary="Commissioned demographic map of Zurich showing the density of residents aged 25 to 45 on a 100 m grid.",
    result="Print-ready population density map.",
    method=["Demographic data by district", "Density calculation", "Thematic classification", "Layout"],
    old=["Category-B-Cartography/Zurich-Demographics/zurich_pop_density_map.png"])
add(slug="racehorse-facility-location-map", cat="cartography", featured=True,
    title="Racehorse Training Facility Location Map", year="2024", client="Upwork client, USA",
    where="USA", tools=["ArcGIS Pro"],
    summary="Strategic location graphic showing a racehorse training facility relative to the top race tracks.",
    result="High-resolution map in PNG, JPG and PDF for marketing use.",
    method=["Facility and race-track locations", "Base map and distances", "Graphic design and export"],
    files=["Strategic Location of Racehorse Training Facility Near Top Race Tracks.jpg", "Strategic Location of Racehorse Training Facility Near Top Race PNG.png"])
add(slug="indonesia-landuse-school-locator", cat="cartography",
    title="Land Use & School Locator Map: Wonosobo, Indonesia", year="2025", client="Upwork client",
    where="Wonosobo, Indonesia", tools=["ArcGIS Pro"],
    summary="Natural land-use map with school locations for Wonosobo, set within a national locator map of Indonesia.",
    result="Two-map layout (national locator + district land use and schools).",
    method=["Land-use and school data", "District and national extents", "Layout with locator"],
    files=["Natural Landuse & School Locator Map of Indonesia & Wonosobo.pdf", "indonesia.pdf"])
add(slug="new-mexico-snow-load-kmz", cat="cartography",
    title="New Mexico Cities Snow-Load & Elevation KMZ", year="2026", client="Upwork client, USA",
    where="New Mexico, USA", tools=["QGIS", "Google Earth", "KML/KMZ"],
    summary="Built a Google Earth KMZ of 191 New Mexico localities across 34 counties, carrying ground snow-load and elevation attributes from a published snow-load table.",
    result="KMZ with attributed locality features (snow load 0–75 psf), ready to open in Google Earth.",
    method=["Snow-load table extraction", "Geocode cities", "Attach snow load + elevation", "KMZ export"],
    files=["Final_City_with_Snow_and_Elevation.kmz", "New Mexico Snowload Extract[4-8].pdf"], note="Map preview rendered from the delivered KMZ.")
add(slug="zip-code-territory-map", cat="cartography",
    title="Sales Territory Map from ZIP Codes", year="2024", client="Upwork client, USA",
    where="Cuyahoga County (Cleveland area), Ohio, USA", tools=["ArcGIS Pro", "Census ZCTA", "OpenStreetMap"],
    summary="Built a territory around four ZIP code areas (44115, 44122, 44130, 44145) with 10-mile buffers, county, municipal and school-district boundaries, and selected the schools inside the territory from OpenStreetMap.",
    result="Territory map and GIS data package (ZCTA boundaries, buffers, administrative layers, selected school points).",
    method=["Census ZCTA polygons for four ZIP codes", "10-mile buffers", "County, municipal and school-district layers", "Select schools within the territory"],
    files=["Todd Project Data.rar"], note="Map preview rendered from the delivered shapefiles.")

# ---------------- 03 Urban GIS & suitability ----------------
add(slug="atlanta-green-space-suitability", cat="urban", featured=True,
    title="Site Suitability for Urban Green Space: Atlanta", year="2025", client="Upwork client, USA (5.0★)",
    where="Atlanta, Georgia, USA", tools=["ArcGIS Pro", "2020 U.S. Census", "Buffer analysis"],
    summary="GIS site-suitability study for new urban green space in Atlanta, combining park access, population density and available parcels.",
    result="Several neighbourhoods, especially in Southeast Atlanta, had no green space within 500 m, and many of them were tracts above 5,000 people/km². Of 6,000+ vacant parcels screened, 37 met every criterion (location, size, accessibility) and were ranked high, medium or low priority. Delivered as four large-format maps and a full report.",
    method=["Existing parks + 500 m service buffers", "2020 Census population density by tract", "Underserved-area overlay", "Suitable parcel selection + report"],
    files=["Distribution of Existing Parks and 500-Meter.pdf", "Population Density by Census Tract in Atlanta, Georgia (2020 Census Data).pdf",
           "Underserved Urban Areas Lacking Green Space.pdf", "Suitable Land Parcels for New Green Space.pdf",
           "A GIS-Based Site Suitability Analysis for Urban Green Spaces in Atlanta, Georgia.pdf"])
add(slug="umluj-flood-risk-mcda", cat="urban", featured=True,
    title="Multi-Criteria Flood Risk Map: Umluj", year="2025", client="Sadeem International Company, Saudi Arabia (5.0★)",
    where="Umluj, Saudi Arabia", tools=["ArcGIS Pro", "MCDA", "DEM"],
    summary="Environmental assessment to choose sites for flood sensors: a multi-criteria flood risk map of Umluj city and surroundings.",
    result="Flood risk map, study-area boundary comparison maps and project outline.",
    method=["Study-area definition", "Flood factors (terrain, drainage, land use)", "Weighted overlay (MCDA)", "Risk map + sensor siting"],
    files=["Multi-Criteria Flood Risk Map – Umluj City and Surroundings.pdf", "Compersion Map of Study Area Boundary and Without Boundary.pdf", "Project Outline.pdf"])
add(slug="umluj-flood-susceptibility-ahp", cat="urban", featured=True,
    title="Flood Susceptibility with AHP: Umluj Coastal Catchments (Google Earth Engine)", year="2025 project · AHP extension 2026",
    client="Based on my project for Sadeem International Company, Saudi Arabia (5.0★ review)",
    where="Umluj city and surroundings, Saudi Arabia", tools=["Google Earth Engine (JavaScript)", "AHP", "MCDA", "MERIT Hydro HAND", "Copernicus DEM", "ESA WorldCover"],
    summary="Flood susceptibility map of the Umluj coastal catchments built with the Analytic Hierarchy Process (AHP): five factors weighted by pairwise comparison (CR = 0.018), combined in Google Earth Engine from open global data, then used to site a 10-gauge flood-sensor network, the original goal of the project.",
    result="Five-class flood susceptibility map with AHP weights (CR 0.018) and a recommended network of 10 flood sensors: 7 town gauges and 3 upstream early-warning gauges, all reproducible in Earth Engine.",
    method=["AHP-weighted flood susceptibility in GEE"],
    files=["code/umluj_flood_susceptibility_ahp.js (full Earth Engine script)", "data/umluj_flood_sensor_sites.geojson and .csv (10 recommended sensor sites)", "Maps: susceptibility, factors, AHP matrix, sensitivity test, sensor network, site table"],
    links=[("Open in the Earth Engine Code Editor", "https://code.earthengine.google.com/a798305d9e3ebf798b8601c8bb0d61c3"), ("View the script on GitHub", "https://github.com/Abdul-Haleem-Khan-RS-GIS/spatial-analysis-showcase/blob/main/03-Urban-GIS-and-Suitability/umluj-flood-susceptibility-ahp/code/umluj_flood_susceptibility_ahp.js"), ("See the original client project", "umluj-flood-risk-mcda.html")])
add(slug="dubendorf-employment-density", cat="urban",
    title="Employment Density on a 100 m Grid: Dübendorf", year="2024", client="Upwork client, Switzerland",
    where="Dübendorf, Switzerland", tools=["ArcGIS", "QGIS", "Swiss 100 m grid"],
    summary="Employment density map of Dübendorf, showing the number of employees in each 100 m × 100 m grid cell across the city.",
    result="Grid map in three classes (1–175, 175–843 and 843–2,468 employees per cell) that shows the main employment clusters in the north and centre of the city.",
    method=["Employment counts per 100 m grid cell", "Clip to the city boundary", "Classify into three density classes", "Layout"],
    files=["Employment Density Map Of Dübendorf City.pdf"])
add(slug="zurich-daycare-centres", cat="urban",
    title="Daycare Centres of Zurich", year="2023", client="Upwork client, Switzerland",
    where="Zurich, Switzerland", tools=["ArcGIS"],
    summary="Map of every daycare centre in the city of Zurich.",
    result="City-wide daycare location map (PDF).",
    method=["Daycare locations", "City base map", "Layout"],
    old=["Category-C-Urban-GIS/Daycare-Accessibility/daycare_accessibility_mapdaycare_accessibility_map.png"],
    files=["Daycare Center Map Of Zurich City_compressed.pdf"])
add(slug="swiss-client-employee-strategy-maps", cat="urban", featured=True,
    title="Client & Employee Strategy Maps: Switzerland", year="2023–2025", client="Swiss service company (repeat client)",
    where="Switzerland", tools=["ArcGIS", "QGIS"],
    summary="Strategy maps for a Swiss cleaning company: client and employee clusters by postal code (clients red, employees blue, circle size by count), and a later postal-code map shaded by client count.",
    result="Postcode-based strategic locator maps used to optimise service areas.",
    method=["Client and employee address lists", "Aggregate by postal code", "Proportional symbols / graduated hatch", "Layouts"],
    old=["Category-C-Urban-GIS/Business-Logistics-Optimization/optimized_assignment_map.png"],
    files=["4Postalcode base Strategic Locator Map.pdf"])
add(slug="riverside-fire-hazard-parcels", cat="urban", study=True,
    title="Residential Parcels by Fire Hazard Zone: Riverside", year="2024", client="Practice study",
    where="Riverside, California, USA", tools=["ArcGIS Pro"],
    summary="Overlay of residential parcels with fire hazard severity zones in Riverside, including a neighbourhood case study (Alessandro Heights).",
    result="Map and data package of residential parcels by fire hazard zone.",
    method=["Parcel and hazard-zone layers", "Spatial join / overlay", "Summary by zone", "Maps"],
    files=["Residential Parcels by Fire Hazard Zone in Riverside.rar", "Alessandro Heights - 88.20 %.rar"])
add(slug="summer-campground-suitability", cat="urban", study=True,
    title="Suitable Locations for a Summer Campground", year="2024", client="Practice study",
    where="Study area, USA", tools=["ArcGIS Pro", "DEM", "Weighted overlay"],
    summary="Raster suitability model combining relief and other criteria to find suitable campground sites.",
    result="Suitability map and relief data.",
    method=["Relief/slope from DEM", "Criteria reclassification", "Weighted overlay", "Suitable sites"],
    files=["Suitable Locations for Summer Campground.pdf", "Relief Details.rar"])
add(slug="st-louis-parcel-criteria-map", cat="urban", featured=True,
    title="Real-Estate Parcel Screening: St. Louis (Interactive Web Map)", year="2025", client="Upwork client, USA (real-estate investor)",
    where="St. Louis, Missouri, USA", tools=["QGIS", "qgis2web", "Leaflet", "OpenStreetMap", "Parcel & zoning data"],
    summary="Interactive web maps that screen St. Louis residential parcels by lot size and building size, colour-coding the parcels that fit a real-estate investor's buying criteria.",
    result="Interactive Leaflet web map (QGIS + qgis2web) with colour-coded lot-size classes, parks in green, commercial and public parcels left blank, and a pop-up for every parcel.",
    method=["Parcel data", "Lot-size classes", "Web map"],
    files=["Interactive web map (shared privately with the client)"],
    note="The live map link is confidential and is not published here.")

# ---------------- 04 Network ----------------
add(slug="bike-route-network-analysis", cat="network", featured=True,
    title="Bike Route Network Analysis", year="2024", client="Upwork client (geomatics firm)",
    where="Mountainous region", tools=["ArcGIS Pro", "Network Analyst", "OpenStreetMap"],
    summary="Used ArcGIS Pro and OpenStreetMap to calculate alternative routes for a bike tour where existing routing services fall short.",
    result="Calculated routes compared against reference data from a test ride, with conclusions for improving bike routing in mountainous terrain.",
    method=["OSM network dataset", "Route solving in Network Analyst", "Comparison with test-ride track", "Findings"],
    old=["Category-D-Network-GIS/Bike-Route-Network-Analysis/route_comparison_map.png"])

# ---------------- 05 Data engineering & CAD ----------------
add(slug="solar-plant-gis-dataset", cat="data", featured=True,
    title="Solar Power Plant GIS Dataset", year="2026", client="Engineering firm (5.0★, $1,000)",
    where="Solar power plant site", tools=["ArcGIS Pro", "AutoCAD", "Shapefile"],
    summary="Built the GIS dataset for a solar power plant from engineering drawings, in three approved milestones.",
    result="Shapefiles for project boundary, blocks (with IDs), substation, MVP components (UPS, inverter, transformer, RMU), piles, trenches and MV cables. Client review: “He did very well Job delivered his project on time.”",
    method=["Engineering drawings", "Digitise and attribute assets", "Piles, trenches, MV cables", "QA and milestone delivery"],
    files=["FINAL SHAPEFILES.zip", "Piles_Points.zip", "Trenches SHP.rar", "MV_Details.rar"], note="Map preview rendered from the delivered shapefiles.")
add(slug="nc-contours-to-cad", cat="data", featured=True,
    title="1-ft Contours to CAD (DWG + SHP)", year="2026", client="MBH Inc., USA (5.0★)",
    where="Cherokee County, North Carolina, USA", tools=["ArcGIS Pro", "Export to CAD", "NC OneMap"],
    summary="Clipped NC OneMap 1-ft contours to a one-mile area of interest and exported them to both shapefile and AutoCAD DWG.",
    result="Validated SHP + DWG package with documented coordinate system. Client review: “Abdul delivered exactly what we needed with a complex GIS to CAD conversion.”",
    method=["NC OneMap 1-ft contour FGDB", "Clip to AOI", "Export to CAD", "Verify in AutoCAD"],
    files=[], note="Large files delivered via Google Drive.")
add(slug="scanned-contours-to-kmz", cat="data",
    title="Vectorised Contours from Scanned Maps (KMZ)", year="2026", client="Upwork client (5.0★)",
    where="USA", tools=["ArcGIS Pro", "Georeferencing", "KMZ"],
    summary="Georeferenced scanned maps, vectorised the contours and delivered attributed KMZ polygons.",
    result="Attributed contour polygons in KMZ.",
    method=["Georeference scans", "Vectorise contours", "Build polygons + attributes", "KMZ export"], files=[])
add(slug="minnesota-county-data-merge", cat="data",
    title="County Dataset Integration: Scott & Dakota, MN", year="2024", client="Upwork client, USA",
    where="Scott and Dakota Counties, Minnesota, USA", tools=["ArcGIS Pro"],
    summary="Combined county parcel, address and assessment datasets into one clean, consistent table for each of two Minnesota counties, with coordinates for every parcel.",
    result="Integrated parcel tables for Scott County (60,713 parcels) and Dakota County (146,596 parcels) with assessed values and coordinates. The tables are not published because they include owners' names and addresses.",
    method=["Source datasets", "Schema matching", "Merge and clean", "Package per county"],
    files=[], note="Map preview rendered from the delivered data.")
add(slug="ny-address-geocoding", cat="data",
    title="Address Geocoding: New York & Long Island", year="2025", client="Upwork client, USA",
    where="New York, USA", tools=["Geocoding", "Excel", "Google Maps"],
    summary="Geocoded client address lists for New York and Long Island to coordinates.",
    result="Geocoded address tables (about 2,270 addresses). The address data is kept private because it lists individuals' addresses.",
    method=["Address cleaning", "Geocoding", "Match review", "Output tables"],
    files=[])
add(slug="qgis-polygon-point-digitisation", cat="data", featured=True,
    title="Refinery Site Plan Digitisation: Process Units & Muster Points (QGIS)", year="2025", client="Valorian (5.0★)",
    where="Texas City, Texas, USA", tools=["QGIS", "Georeferencer", "GeoPackage", "Shapefile", "EPSG:3857"],
    summary="Urgent QGIS job: georeferenced a refinery site-plan image over OpenStreetMap and digitised 60 process-unit polygons and 15 emergency muster points with attributes.",
    result="Georeferenced site plan plus process-unit and muster-point layers (GeoPackage and shapefile) in a ready-to-open QGIS project.",
    method=["Georeferencing", "Digitising", "QA and delivery"],
    files=["Refinery_Digitisation_QGIS.zip (QGIS project, Units and MusterPoints shapefiles, gbr.gpkg, georeferenced site-plan image)"])
add(slug="global-mapper-csv-export-script", cat="data",
    title="Global Mapper Script: Export Layers to CSV", year="2024", client="Futurewise Aerial",
    where="United Kingdom", tools=["Global Mapper scripting"],
    summary="Global Mapper script that exports multiple layers to separate CSV files, with a how-to guide.",
    result="Working script, sample CSV outputs and documentation.",
    method=["Layer loop in Global Mapper script", "CSV export per layer", "Test + guide"],
    files=["Global Mapper Script to export multiple layers as CSV files.pdf", "Export multiple layers in csv.docx", "1.csv", "2.csv", "3.csv", "4.csv"])

# ---------------- 06 Master plans & municipal GIS ----------------
add(slug="uyun-al-jawa-municipal-gis", cat="planning", featured=True, pro=True,
    title="Municipal GIS: Uyun Al Jawa, Saudi Arabia", year="Jun 2024 – Jun 2026", client="Municipality of Uyun Al Jawa, Al-Qassim (GIS Engineer)",
    where="Uyun Al Jawa Governorate, Al-Qassim, Saudi Arabia", tools=["ArcMap 10.9", "ArcGIS Pro", "AutoCAD", "Geodatabases", "GPS field survey"],
    summary="Two years as the municipality's GIS Engineer: the official Municipal Lands Plans Document for the governorate, the map of areas reserved for municipal investments, final AutoCAD drawings of government residential plans 2505 and 3045, and the spatial databases behind municipal planning decisions.",
    result="Approved municipal maps (land use, municipal investment lands, urban boundaries, road network), an inventory map of reserved investment areas, final AutoCAD drawings of government residential plans 2505 (amended, 1:5000) and 3045 (72 plots, 1:1500), and maintained municipal geodatabases; GIS training delivered to World Bank officials.",
    method=["Maintain municipal geodatabases (planning, parcels, infrastructure)", "Coordinate GPS field data collection", "Spatial analysis and map production for planning and services", "Integrate GIS data across departments; staff and World Bank training"],
    files=["Uyun Al Jawa - Municipal Lands Plans Document.pdf", "Uyun Al Jawa - Areas Reserved for Municipal Investments (58).pdf", "Plan 2505 - Government residential plan, amended.pdf + AutoCAD .dwg", "Plan 3045 - Government residential plan.pdf + AutoCAD .dwg"],
    note="See also the Rawd Al-Jawa investment site plan, drafted in AutoCAD for the municipality.")
add(slug="rawd-al-jawa-investment-site-plan", cat="planning", featured=True, pro=True,
    title="Rawd Al-Jawa Municipal Investment Site: AutoCAD Regulatory Plan", year="2024–2026",
    client="Municipality of Uyun Al Jawa · Al-Qassim Region Municipality (Amanah)",
    where="Rawd Al-Jawa, Uyun Al Jawa, Al-Qassim, Saudi Arabia", tools=["AutoCAD 2023", "Scanned-map digitising", "Google Earth", "Cadastral drafting"],
    summary="Redrew an old scanned municipal map as an accurate AutoCAD regulatory plan for a 5,000 m² commercial investment site in Rawd Al-Jawa, prepared for preliminary approval by the Al-Qassim Region Municipality.",
    result="Preliminary-approval regulatory plan (1:500) for a 5,000 m² commercial municipal-investment site with a garden area, dimensioned boundaries, location insets and hydrological recommendations.",
    method=["Digitised the plot from the old scanned map in AutoCAD"],
    files=["Rawd Al-Jawa investment site plan (AutoCAD plot).pdf"])
add(slug="sahiwal-city-comprehensive-plan", cat="planning", featured=True, pro=True,
    title="Sahiwal Land-Use City Comprehensive Plan (2022–2042)", year="2022–2024", client="PICIIP, Government of Punjab · via Shehersaaz (UMDS Consultant)",
    where="Municipal Committee Sahiwal, Punjab, Pakistan", tools=["ArcGIS", "Land-use survey", "Suitability analysis"],
    summary="GIS mapping and analysis for Output A-1 of the Land-Use Focused City Comprehensive Plan for Sahiwal under the Punjab Intermediate Cities Improvement Investment Program (PICIIP).",
    result="Existing land-use map of MC Sahiwal, land-use suitability analyses for residential and industrial development, and the Site Development Zone (Scenario III) for the 2022–2042 plan period.",
    method=["Existing land-use mapping from survey data and imagery", "Suitability analysis for residential land use", "Suitability analysis for industrial land use", "Development scenarios and site development zones to 2042"],
    catalog=["vhm0wahkouzlkfw08z58", "uwzuuikepve2sazgaeqg", "lgkomtrlgjiukkajzpnm", "dv9fdkelwvcnszchvt8h"])
add(slug="sialkot-city-comprehensive-plan", cat="planning", featured=True, pro=True,
    title="Sialkot Land-Use City Comprehensive Plan", year="2022–2024", client="PICIIP, Government of Punjab · via Shehersaaz (UMDS Consultant)",
    where="Sialkot, Punjab, Pakistan", tools=["ArcGIS", "Land-use survey"],
    summary="Existing land-use mapping of the Sialkot study area for Output A-1 of the PICIIP Land-Use Focused City Comprehensive Plan.",
    result="Existing land-use map of the study area showing residential, commercial, industrial, agricultural, education and religious uses with the M11 motorway, railway, road hierarchy, MC and cantonment boundaries.",
    method=["Land-use survey data", "Classify and digitise parcels by use", "Transport network and administrative boundaries", "Plan-standard map layout"],
    catalog=["umgrmwpgh8nfeaatxwhj"])
add(slug="batswat-terrain-assessment", cat="planning", pro=True,
    title="Batswat Habitat Planning: Terrain Assessment", year="2022–2024", client="Aga Khan Agency for Habitat · via Shehersaaz",
    where="Batswat, Pakistan", tools=["ArcGIS", "DEM", "Slope & contour analysis"],
    summary="Base maps for a habitat planning study: a location and land-use map, a slope map and a contour map of the Batswat study area.",
    result="Location, slope (in degrees) and contour maps used to read terrain constraints and the river corridor for habitat planning.",
    method=["DEM processing", "Slope in degrees, classified", "Contour generation", "Location and land-use map with inset maps"],
    catalog=["ish32lzdwtxa4dtobvel", "shbpxha7ujqe2uom5utt", "ovy3p2rvbze6fstpe7xi"])
add(slug="punjab-kp-master-plans-and-cadastre", cat="planning", pro=True,
    title="City Master Plans & Cadastral Mapping: Punjab and KP", year="2022–2024", client="Shehersaaz · supervised by PICIIP, UPU and PULSE",
    where="Cities in Punjab and Khyber Pakhtunkhwa, Pakistan", tools=["ArcGIS Pro", "QGIS", "ERDAS Imagine", "Python"],
    summary="Spatial analysis, mapping and geodatabase management for city master-plan programmes in Punjab (PICIIP) and Khyber Pakhtunkhwa (Urban Policy Unit), and cadastral mapping across several Punjab cities for PULSE (May 2023 – Apr 2024).",
    result="Planning geodatabases and map sets for master-plan reports, cadastral maps for PULSE, and automated processing workflows in ArcGIS Pro, QGIS, ERDAS Imagine and Python.",
    method=["Base data and imagery processing", "Geodatabase design and management", "Planning and cadastral mapping", "Workflow automation with Python"],
    files=[])

# ---- merge detailed case-study content ----
try:
    from details import D as _D
except ImportError:
    _D = {}
for _p in P:
    _p.update(_D.get(_p["slug"], {}))
