# Detailed case-study content, merged over projects.py by slug.
# Every fact here comes from Abdul's delivered reports, Upwork contract messages or portfolio items.
# Fields: challenge (str), data (list of "dataset — source/notes"), method (list, replaces the short version),
# findings (list), captions (list, one per map in maps/ order), plus any overrides (where, tools, summary...).

D = {}

# ---------------- 01 Remote sensing ----------------
D["burn-severity-sentinel2"] = dict(
    where="Eastern Australia (Sentinel-2, UTM zone 56S)",
    tools=["Sentinel-2", "QGIS", "Google Earth Engine", "Copernicus EMS"],
    challenge="Map how badly a wildfire burned the landscape in late 2019 and check whether vegetation was recovering, using freely available satellite data alongside the official Copernicus Emergency Management Service (CEMS) burn-extent map.",
    data=["Sentinel-2 Level-2A scenes for January 2019, October 2019, November 2019 and January 2020 (WGS 84 / UTM zone 56S, EPSG:32756)",
          "Copernicus Emergency Management Service (CEMS) burn-extent map, supplied as an image",
          "Google Earth Engine Sentinel-2 collection for index calculation"],
    method=["Loaded the True Colour Images (B4-B3-B2) for all four dates and compared pre-fire, active-fire and post-fire conditions",
            "Georeferenced the CEMS map to the Sentinel-2 grid with 6 ground control points, a 2nd-order polynomial transformation and nearest-neighbour resampling (RMS error 0.82)",
            "Built NIR-Red-Green false-colour composites (B8-B4-B3) to separate healthy vegetation from burn scars and smoke",
            "Uploaded the georeferenced CEMS map to Google Earth Engine as an asset and displayed it with the same Sentinel-2 scenes",
            "Calculated the Normalized Burn Ratio, NBR = (B8 − B12) / (B8 + B12), for pre- and post-fire dates and derived dNBR",
            "Classified dNBR into five severity classes (unburned to high severity) and produced the map and report"],
    findings=["October 2019 imagery shows dense, intact vegetation; November 2019 shows extensive burn scars and smoke plumes",
              "dNBR highlights large contiguous patches of high burn severity in the November 2019 observation",
              "By January 2020 parts of the burned area show regrowth, with clear contrast between burnt and unburnt zones",
              "Recommended SWIR (B12) for hotspot and burn-scar detection and NIR (B8) for vegetation health during an active fire"],
    captions=["Delta Normalized Burn Ratio (dNBR) classified into five burn-severity classes"])

D["lulc-andijan-reservoir"] = dict(
    where="Andijan Reservoir, Uzbekistan",
    tools=["Sentinel-2", "ArcGIS Pro", "Google Earth Engine", "Random Forest", "SVM"],
    challenge="Produce a reliable land-cover map around the Andijan Reservoir and work out which classification approach, unsupervised clustering or supervised machine learning, gives the most accurate result.",
    data=["Sentinel-2 image of 13 April 2023 (10 m bands)",
          "Area of interest digitised around the reservoir from visual assessment",
          "Training polygons for six classes: water, urban, agricultural land, open soil/rock, shrubs/bushes and grassland"],
    method=["Ran ISO Cluster unsupervised classification in ArcGIS Pro with 5, 7 and 10 classes and matched each cluster to a real-world land-cover class",
            "Uploaded the AOI to Google Earth Engine, clipped the Sentinel-2 scene and drew training polygons for the six classes",
            "Used the visible and near-infrared bands and a random split of the samples into training data and a 30% test set",
            "Trained and compared Random Forest and Support Vector Machine classifiers, adding samples for difficult classes",
            "Assessed accuracy with a confusion matrix in GEE (errorMatrix) and with accuracy-assessment points in ArcGIS Pro"],
    findings=["Water bodies reached user's and producer's accuracy above 90%",
              "Urban, open soil, agriculture and bushes reached moderate accuracy (80–90%), with some confusion between them",
              "Random Forest was more reliable for large classes (water, urban); SVM separated shrubs and grassland slightly better",
              "Supervised Random Forest in GEE gave the more detailed and accurate map; mixed classes such as shrubland and grassland remain the main area to improve"],
    captions=["Supervised pixel-based classification in Google Earth Engine (Random Forest)",
              "ISO Cluster unsupervised classification with 7 classes in ArcGIS Pro"])

D["landsat-band4-band10-analysis"] = dict(
    challenge="Show how visible red (Band 4) and thermal infrared (Band 10) values can be used to tell clouds, water, snow, forest, mountains and slopes apart.",
    data=["Landsat 8/9 scene with Band 4 (red) and Band 10 (thermal infrared)",
          "Sample points for cloud, forest, lake, mountain and slope classes"],
    method=["Sampled pixel values for each class in Band 4 and Band 10",
            "Charted value ranges by class to compare reflectance and thermal emission",
            "Interpreted the differences physically: reflectivity, heat retention, altitude and sun exposure",
            "Wrote a companion report recommending the right sensor for five use cases (Sentinel-2, Sentinel-1, MODIS, WorldView-3, Meteosat)"],
    findings=["Clouds: highest Band 4 values (33,254–35,173) but only moderate Band 10 values (16,972–17,897)",
              "Lakes: low Band 4 (5,519–8,322) but the highest Band 10 values (17,065–19,795), because water retains heat",
              "South-facing slopes are warmer and brighter than north-facing ones; forests sit in a narrow thermal range (17,730–18,189)",
              "Snow and cloud look alike in Band 4 but can be separated in Band 10, where snow is much colder"])

D["aerial-image-manual-classification"] = dict(
    tools=["ArcGIS 10.8", "Visual interpretation", "Digitising"],
    challenge="Classify land cover on a non-georeferenced aerial photo by eye, consistently and in a way someone else could repeat.",
    data=["Aerial image supplied by the client (not georeferenced)"],
    method=["Built an interpretation key for six classes (meadow, agriculture, buildings, roads, parking lots, forest/trees) using colour, texture, structure, size, shape and context",
            "Created a polygon feature class with a Class field and digitised every feature with snapping on to avoid gaps and overlaps",
            "Used a minimum mapping unit of about 10 m² to keep the map readable",
            "Logged ambiguous polygons (for example road vs parking lot) in a separate table with the reasoning for each decision"],
    findings=["Complete land-cover map with attributed polygons delivered as a shapefile",
              "Interpretation key and ambiguity table make the classification reproducible",
              "Recommended georeferencing the image first and a second-reviewer check for ambiguous areas"],
    captions=["Manually digitised land-cover classification of the aerial image"])

D["los-angeles-urban-land-cover"] = dict(
    year="2024", tools=["Landsat 8 OLI", "ENVI", "Maximum Likelihood", "Correlation analysis"],
    summary="Classified urban land cover across the Los Angeles metropolitan area for 2019, 2022 and 2024 with Maximum Likelihood Classification of Landsat 8 imagery, to measure urban densification and changes in green space.",
    challenge="Measure how Los Angeles land cover changed between 2019 and 2024: where the city densified, and what happened to vegetation, water and bare soil.",
    data=["Landsat 8 OLI scenes for 2019, 2022 and 2024 (USGS EarthExplorer), bands 2–7",
          "Regions of interest for six classes: water, high-density urban, low-density urban, irrigated lawns, natural vegetation, bare soil"],
    method=["Radiometric calibration, atmospheric correction and subsetting to the metropolitan area",
            "Selected ROIs for the six classes and checked their spectral signatures",
            "Ran a Pearson correlation analysis between bands and excluded bands correlated above 0.85; bands 5, 1 and 7 were the least correlated",
            "Classified each year with Maximum Likelihood and assessed accuracy with confusion matrices and Kappa",
            "Compared class areas across the three years"],
    findings=["High-density urban grew from 76.71 km² (2019) to 78.56 km² (2024) while low-density urban fell from 195.75 to 186.51 km², a sign of densification",
              "Bare soil declined from 22.00 to 18.37 km² as development reached undeveloped land",
              "Irrigated lawns rose from 38.16 to 41.71 km²; natural vegetation dipped to 57.39 km² in 2022 and recovered to 63.15 km² in 2024",
              "Water rose from 35.83 km² (2019) to 42.92 km² (2022), then 41.50 km² (2024)"],
    captions=["Maximum Likelihood land-cover classification of Los Angeles (six classes)", "Maximum Likelihood land-cover classification for a second year, used for change comparison", "Study area: Los Angeles metropolitan region on Landsat 8"])

D["ndvi-and-image-classification-studies"] = dict(
    where="Los Angeles, USA", tools=["ENVI", "Landsat 8", "Landsat 9", "ISODATA", "Maximum Likelihood"],
    summary="Two step-by-step studies on Landsat imagery of Los Angeles: NDVI with ISODATA unsupervised classification, and supervised Maximum Likelihood classification with ROI statistics and band-correlation analysis.",
    challenge="Document, with interpretation at each step, how NDVI and unsupervised and supervised classification behave on an urban Landsat scene.",
    data=["Landsat 8 scene of Los Angeles (multispectral stack from the MTL file)", "Landsat 9 scene of Los Angeles", "NLCD land-cover subset as reference"],
    method=["Spatial and spectral subset of west Los Angeles (Santa Monica Mountains, urban area and ocean), bands 5-4-3-2",
            "True-colour (4-3-2) and false-colour (5-4-3) comparison; NDVI calculated and interpreted",
            "ISODATA unsupervised classification and identification of the resulting classes",
            "Supervised study: six classes, at least five ROIs and 1,000 pixels per class, ROI statistics, correlation matrix to choose the least correlated bands, then Maximum Likelihood classification and class summary"],
    findings=["NDVI cleanly separates vegetated hills and parks from the urban core and water",
              "Unsupervised classes needed manual labelling and merged some urban and soil areas",
              "Choosing the least correlated bands improved separation of the six supervised classes"],
    captions=["ISODATA unsupervised classification of west Los Angeles (Landsat 8)", "Maximum Likelihood supervised classification with six classes (Landsat 9)"])

D["landsat-thermal-and-image-analysis"] = dict(
    title="Landsat 9 & Thermal Image Analysis", year="2024",
    where="Los Angeles, Rome and Ann Arbor", tools=["Landsat 9", "Landsat TM", "Airborne thermal scanner", "ENVI"],
    summary="Image analysis of a Landsat 9 scene of Los Angeles (12 January 2024) and thermal interpretation of Landsat TM Band 6 over Rome and airborne thermal imagery of Ann Arbor.",
    challenge="Interpret multispectral and thermal imagery correctly: what different band combinations and thermal values reveal about urban surfaces.",
    data=["Landsat 9 scene of Los Angeles, 12 January 2024 (7,751 columns × 7,881 rows, 11 bands)",
          "Landsat TM Band 6 (thermal) image of Rome",
          "Airborne thermal infrared scan of Ann Arbor, 9 May 1981 (8–14 µm, 3,600 m altitude)"],
    method=["True-colour (4-3-2) and false-colour SWIR composite (7-6-4) to highlight urban areas",
            "Image dimension and band review, and subsetting to the area of interest",
            "Interpretation of thermal digital numbers for roads, rivers, vegetation and buildings"],
    findings=["The 7-6-4 composite shows urban areas in pink and magenta, clearly separated from natural land",
              "In early-morning thermal imagery, roads and rivers appear warmer than vegetation"],
    captions=["Landsat 9 scene over Los Angeles, 12 January 2024"])

D["ndvi-summary-arcgis-pro"] = dict(
    challenge="Produce a clear NDVI map of Los Angeles County within a strict 20-minute time limit.",
    data=["Landsat 8 surface reflectance (pre-processed)", "Los Angeles County AOI", "Esri basemap"],
    method=["Selected pre-processed Landsat 8 surface reflectance to save time",
            "Calculated NDVI = (NIR − Red) / (NIR + Red) and clipped it to the county",
            "Applied a green-to-orange ramp and a pre-built layout template"],
    findings=["NDVI ranged from −0.29 to 0.60 across the county",
              "Healthy vegetation in the mountains and parks stands out from the urban basin and barren areas"],
    captions=["NDVI map of Los Angeles County from Landsat 8"])

# ---------------- 02 Cartography ----------------
D["nps-map-redesign"] = dict(
    challenge="Replicate a National Park Service map of Rocky Mountain National Park and improve its clarity for visitors without losing its familiar look.",
    data=["NPS open data (public-nps.opendata.arcgis.com) and the NPS ArcGIS Online group supplied by the client", "Terrain for elevation shading"],
    method=["Rebuilt the park map in ArcGIS Pro from NPS open data",
            "Colour: a more vibrant but balanced palette (rich greens for forest, lighter tones for meadows and water) and clearer elevation shading",
            "Symbols: simplified, recognisable icons for trailheads and points of interest with a subtle shadow; solid, dashed and dotted lines for paved roads, trails and minor paths",
            "Labels: larger sans-serif type for major features, italics for trails and elevations, contour labels following terrain, no overlaps"],
    findings=["Finished map plus a written report on cartographic improvements for future NPS maps"],
    captions=["Redesigned map of Rocky Mountain National Park, Colorado"])

D["georgia-choropleth-classification"] = dict(
    tools=["ArcGIS 10.8", "2020 U.S. Census", "TIGER/Line"],
    challenge="Show how the choice of classification method changes what a choropleth map says about the same data.",
    data=["2020 U.S. Census population for Georgia's 159 counties", "TIGER/Line county boundaries", "NAD 1983 StatePlane Georgia West (feet)"],
    method=["Cleaned the attributes, removed nulls and projected to StatePlane Georgia West",
            "Mapped population with Equal Interval, Natural Breaks (Jenks), Quantile and Standard Deviation, using matching layouts",
            "Compared the advantages and drawbacks of each method in a one-page analysis"],
    findings=["Equal Interval hides most variation: almost every county falls in the lowest class (1,626–154,942)",
              "Quantile forces equal groups and exaggerates differences among rural counties",
              "Natural Breaks (Jenks) gives the most meaningful picture, showing the Atlanta concentration while still separating rural counties",
              "Standard Deviation highlights the extreme metro counties but is hard for non-specialists to read"],
    captions=["Equal Interval classification", "Natural Breaks (Jenks) classification", "Quantile classification", "Standard Deviation classification"])

D["reference-mapping-text-icons"] = dict(
    where="United States (national, Arizona and Colorado map panels)",
    challenge="Find the clearest way to label and symbolise cities, rivers, lakes, political and physical areas, and roads on reference maps.",
    data=["U.S. cities, states, rivers, lakes, mountain ranges and road networks"],
    method=["Built four map panels, each with three or four frames that progressively improve labelling",
            "Cities: from identical symbols to a four-tier hierarchy by population and capital status",
            "Water: curved labels that follow rivers and better lake label placement",
            "Political and physical areas: label colours matched to features, letter spacing, uppercase mountain ranges and spot elevations",
            "Roads: road hierarchy, highway shields instead of text, and controlled label density"],
    findings=["The four-tier city hierarchy balances detail and readability best",
              "Curved river labels and highway shields gave the clearest maps",
              "Two illustrated reports explain the best frame in each panel"],
    captions=["Urban hierarchy of U.S. cities: four labelling frames", "U.S. political and physical features: multi-frame labelling",
              "Labelling and symbolising cities (point features)", "Labelling and symbolising roads (line features)"])

D["riyadh-postcode-map"] = dict(
    challenge="The client needed Riyadh's postal-code boundaries as a clean dataset that works in GIS software and web maps.",
    data=["Postal-code reference boundaries for Riyadh", "Satellite basemap for checking"],
    method=["Delineated the postal-code zones in QGIS and ArcGIS Pro",
            "Checked attributes and topology so neighbouring zones share edges",
            "Exported to GeoJSON (and shapefile) for web and GIS use"],
    findings=["Postal-code polygon layer for the whole city, delivered as GeoJSON and shapefile"],
    captions=["Postal-code boundaries of Riyadh over satellite imagery"])

D["zurich-population-density"] = dict(
    challenge="Show where residents aged 25 to 45 are concentrated across Zurich for a client's location analysis.",
    data=["Population counts for ages 25–45 on a 100 m × 100 m grid", "Zurich city boundary"],
    method=["Clipped the 100 m grid to the city boundary", "Classified density into three classes", "Designed a clean thematic layout"],
    findings=["Density peaks in a band running through the centre and north of the city"],
    captions=["Population density of residents aged 25–45 on a 100 m grid"])

D["racehorse-facility-location-map"] = dict(
    where="Texas and the U.S. Gulf states",
    challenge="Create a marketing graphic that shows at a glance how close a racehorse training property is to the region's top race tracks.",
    data=["Property location and race-track locations supplied by the client", "U.S. state boundaries"],
    method=["Plotted the property and tracks with distinct symbols", "Added leader lines and labels to each track", "Exported high-resolution PNG, JPG and PDF"],
    findings=["High-resolution location graphic (20 MB PNG and 16 MB PDF) ready for marketing"],
    captions=["Strategic location of the training facility relative to the top race tracks"])

D["indonesia-landuse-school-locator"] = dict(
    challenge="Show natural land use and school locations for Wonosobo, Central Java, together with where the district sits within Indonesia.",
    data=["Natural land-use polygons (beach, forest, grassland, water and others)", "School locations", "Road network and administrative boundaries"],
    method=["Built a national locator map of Indonesia", "Mapped land-use classes and schools for the district", "Combined both in one layout with a world inset"],
    findings=["Two-map layout: national locator, plus land use and schools"],
    captions=["Natural land use and school locator map", "Location map of Indonesia"])

D["new-mexico-snow-load-kmz"] = dict(
    challenge="Turn a printed table of ground snow loads for New Mexico localities into a Google Earth file the client could explore.",
    data=["Ground snow-load table for New Mexico localities (table pages 4–8)", "Locality locations and elevations"],
    method=["Extracted the snow-load table", "Located each locality and attached snow load, elevation and county", "Exported a styled KMZ with pop-up attributes for Google Earth"],
    findings=["191 localities across 34 counties, with ground snow loads from 0 to 75.2 psf",
              "The highest loads are in the northern mountains (for example Red River, Lake Maloya, Dulce)"],
    captions=["Ground snow load at 191 New Mexico localities (preview rendered from the delivered KMZ)"])

D["zip-code-territory-map"] = dict(
    challenge="Define a service territory around four ZIP codes and find the schools within reach.",
    data=["Census ZCTA boundaries for 44115, 44122, 44130 and 44145", "County, municipal and school-district boundaries", "School locations from OpenStreetMap"],
    method=["Selected the four ZCTAs", "Built 10-mile buffers around them", "Selected schools within the territory", "Packaged all layers and a map"],
    findings=["371 schools selected within the 10-mile territory across the Cleveland area"],
    captions=["Four ZIP code areas with a 10-mile reach and selected schools (preview rendered from the delivered data)"])

# ---------------- 03 Urban GIS & suitability ----------------
D["atlanta-green-space-suitability"] = dict(
    tools=["ArcGIS 10.8", "2020 U.S. Census", "Buffer & overlay analysis"],
    challenge="Southern and western Atlanta have limited access to public parks. The study set out to find which neighbourhoods are underserved and which vacant parcels could become new green space.",
    data=["Parks: Atlanta GIS Hub", "2020 Census tracts and population: U.S. Census Bureau", "Vacant parcels: Atlanta Open Data Portal (City Assessor)",
          "Roads: TIGER/Line (RTTYP functional class)", "City boundary: City of Atlanta (about 352 km²)", "Projection: NAD 1983 StatePlane Georgia West FIPS 1002 (feet)"],
    method=["Re-projected all layers and clipped them to the city limit",
            "Created 500 m walking buffers around existing parks",
            "Calculated population density per tract and flagged tracts above 5,000 people/km²",
            "Erased the park buffers from the city to find areas more than 500 m from a park",
            "Intersected the underserved areas with high-density tracts to get priority zones",
            "Selected vacant parcels in the priority zones larger than 1,000 m²",
            "Removed parcels within 100 m of major roads (interstate, U.S. and state routes)",
            "Ranked the remaining parcels as high, medium or low priority"],
    findings=["Several neighbourhoods, especially in Southeast Atlanta, have no green space within 500 m",
              "Many underserved areas are tracts above 5,000 people/km², confirming spatial inequity",
              "Of 6,000+ vacant parcels screened, 37 met every criterion (location, size, accessibility)",
              "Recommended ground-truthing the top parcels, stakeholder consultation and a full MCDM model in future"],
    captions=["Existing parks and 500 m service areas", "Population density by census tract (2020 Census)",
              "Underserved high-density areas without green-space access", "Suitable parcels for new green space by priority"])

D["umluj-flood-risk-mcda"] = dict(
    challenge="Sadeem International needed to know where flooding is most likely around Umluj, on Saudi Arabia's Red Sea coast, to decide where to install flood sensors.",
    data=["Elevation and terrain derivatives for the Umluj area", "Drainage network", "Study-area (AOI) boundary agreed with the client"],
    method=["Defined and compared study-area boundaries with the client",
            "Prepared flood factors from terrain and drainage",
            "Combined the factors in a weighted multi-criteria overlay",
            "Classified risk into five categories, from very low to very high"],
    findings=["Very-high-risk zones follow the wadi channels and the low-lying coastal plain in the west and south",
              "Elevated ground in the north-east is lowest risk",
              "The map gave the client a basis for siting flood sensors"],
    captions=["Multi-criteria flood risk map of Umluj city and surroundings"])

D["dubendorf-employment-density"] = dict(
    challenge="Show where jobs are concentrated in Dübendorf for planners and businesses.",
    data=["Employment counts on the Swiss 100 m × 100 m grid", "Dübendorf city boundary"],
    method=["Clipped the employment grid to the city", "Classified employees per cell into three classes", "Designed the thematic layout"],
    findings=["Most cells hold 1–175 employees; a few hotspots reach 843–2,468 employees per cell",
              "Employment clusters in the north and centre of the city, with a secondary cluster in the south-west"],
    captions=["Employees per 100 m grid cell in Dübendorf"])

D["zurich-daycare-centres"] = dict(
    challenge="Give the client a single, clear map of every daycare centre (Kita) in the city of Zurich.",
    data=["Daycare (Kita) locations", "Buildings, roads and water bodies", "Zurich city boundary"],
    method=["Geocoded and mapped every daycare centre", "Added buildings, roads and water as context", "Designed a print-ready city map"],
    findings=["City-wide daycare map delivered as a print-ready PDF"],
    captions=["Daycare centres (Kita) across the city of Zurich"])

D["swiss-client-employee-strategy-maps"] = dict(
    challenge="A Swiss cleaning company wanted to see where its clients and staff are, so it could plan service areas and recruitment.",
    data=["Client and employee address lists (Excel)", "Swiss postal-code boundaries and population"],
    method=["Geocoded clients and employees and aggregated them by postal code",
            "Showed clients in red and employees in green, with symbol size by count, over population and water bodies"],
    findings=["Clients and staff concentrate around Zurich, with smaller clusters elsewhere in Switzerland",
              "The map showed where service areas and recruitment could be optimised"],
    captions=["Clients and employees strategic locator map, by postal code"])

D["riverside-fire-hazard-parcels"] = dict(
    challenge="Identify residential parcels in Riverside that fall within classified fire hazard severity zones.",
    data=["Riverside residential parcels", "Fire hazard severity zones (moderate, high, very high)"],
    method=["Overlaid parcels with the hazard zones", "Summarised parcels by zone", "Neighbourhood case study of Alessandro Heights"],
    findings=["Very-high hazard zones run along the city's western and southern edges next to open land"],
    captions=["Residential parcels by fire hazard zone in Riverside, California"])

D["summer-campground-suitability"] = dict(
    challenge="Find suitable sites for a summer campground that are close to water and roads but not too far from emergency services.",
    data=["Relief/DEM", "Rivers and lakes", "Major roads", "Emergency services", "Study-area boundary"],
    method=["Derived slope and relief", "Reclassified each criterion", "Weighted overlay to find suitable cells", "Mapped the suitable locations"],
    findings=["A small set of suitable locations near rivers and roads, mapped with emergency-service coverage"],
    captions=["Suitable locations for a summer campground"])

# ---------------- 04 Network ----------------
D["bike-route-network-analysis"] = dict(
    challenge="Existing bike-routing services gave poor routes in mountainous terrain. The client wanted alternatives tested against a real ride.",
    data=["OpenStreetMap road and path network", "Hillshade/DEM", "Reference GPS track from a test ride"],
    method=["Built a network dataset from OpenStreetMap in ArcGIS Pro", "Solved alternative routes between the same start and end points",
            "Compared each route's length and travel time with the test-ride reference", "Wrote up conclusions for improving bike routing"],
    findings=["Four alternative routes (A–D) compared by length and time on a hillshade base",
              "Showed where routing services fail in steep terrain and how routes can be improved"],
    captions=["Alternative bike routes compared on a hillshade base"])

# ---------------- 05 Data engineering ----------------
D["solar-plant-gis-dataset"] = dict(
    challenge="An engineering firm needed a complete GIS asset dataset for a solar power plant, built from engineering drawings and approved milestone by milestone.",
    data=["Engineering layout drawings supplied by the client"],
    method=["Milestone 1 (approved): project boundary, block boundaries with IDs, substation and MV power station components (UPS, inverter, transformer, RMU)",
            "Pile points (about 8.5 MB of points) and LV/DC and PV trench layers, by trench width and depth",
            "Milestone 2 (approved): MV cable layer",
            "Milestone 3 (approved): all comments closed"],
    findings=["Full set of attributed shapefiles delivered across three approved milestones ($1,000 contract)",
              "Client review: “He did very well Job delivered his project on time.”"],
    captions=["Project boundary, PV blocks, trenches, MV cables, power stations and substation (preview rendered from the delivered shapefiles)"])

D["nc-contours-to-cad"] = dict(
    challenge="A fixed-scope, pass/fail task: clip North Carolina 1-ft contours to a one-mile area and deliver working DWG and shapefile versions, or no payment.",
    data=["NC OneMap 1-ft raster contours (from 3-ft DEMs), file geodatabase", "One-mile area of interest in Cherokee County, NC, reaching the Tennessee state line"],
    method=["Downloaded the contour FGDB and clipped it to the AOI (adjusted to the client's marked area)",
            "Exported to shapefile and to DWG with ArcGIS Export to CAD",
            "Documented the coordinate system and software in a text note and checked that both files open"],
    findings=["Delivered SHP + DWG + projection note; accepted and paid",
              "Noted that the dataset covers North Carolina only, so the part of the AOI in Tennessee has no contours",
              "Client review: “Abdul delivered exactly what we needed with a complex GIS to CAD conversion.”"])

D["minnesota-county-data-merge"] = dict(
    challenge="Combine several county datasets into one consistent parcel table per county, with coordinates and assessed values.",
    data=["Scott County and Dakota County parcel, address and assessment data"],
    method=["Matched schemas between sources", "Merged and cleaned records", "Added latitude and longitude for each parcel", "Exported one table per county"],
    findings=["More than 205,000 parcels across Scott and Dakota counties mapped with assessed values",
              "Tables kept private because they include owners' names and addresses"],
    captions=["Assessed parcel values in Scott and Dakota counties (preview rendered from the delivered data)"])

D["global-mapper-csv-export-script"] = dict(
    challenge="The client needed to export several shapefile layers to separate CSV files in one go instead of by hand.",
    data=["Four shapefile layers"],
    method=["Wrote a Global Mapper script: SET_DIR, then IMPORT → EXPORT_VECTOR TYPE=CSV → UNLOAD_ALL for each layer",
            "Tested the export and delivered sample CSVs",
            "Wrote a step-by-step guide explaining every command"],
    findings=["Working script, four sample CSV outputs and documentation"])

# ---------------- 06 Master plans & municipal ----------------
D["sahiwal-city-comprehensive-plan"] = dict(
    challenge="Prepare the GIS base and analysis for Sahiwal's land-use focused city comprehensive plan to guide growth to 2042.",
    data=["Land-use survey of MC Sahiwal", "Road network, railway and administrative boundaries", "Imagery"],
    captions=["Existing land-use map of MC Sahiwal", "Land-use suitability analysis for residential use",
              "Land-use suitability analysis for industry", "Site Development Zone, Scenario III (2022–2042)"])
D["sialkot-city-comprehensive-plan"] = dict(
    challenge="Map the existing land use of the Sialkot study area as the base for its land-use focused city comprehensive plan.",
    captions=["Existing land use of the Sialkot study area"])
D["batswat-terrain-assessment"] = dict(
    challenge="Understand the terrain constraints of the Batswat study area for a habitat planning study.",
    captions=["Location and land-use map of Batswat with inset maps", "Slope map (degrees)", "Contour map"])

D["rawd-al-jawa-investment-site-plan"] = dict(
    challenge="The municipality's only record of the site was an old scanned paper map. It needed an accurate, dimensioned plan drawn to the Al-Qassim Region Municipality's standard so the plot could go forward for preliminary approval as a municipal investment site.",
    data=["Old scanned municipal map of the site (the source drawing)",
          "Municipality survey (field survey prepared by the Municipality of Uyun Al Jawa)",
          "Google Earth imagery for the two location insets (site in relation to neighbours and to the city)",
          "Hydrological study results approved by decision of the head of Uyun Al Jawa Municipality (1446 AH)"],
    method=["Brought the scanned map into AutoCAD and redrew the plot boundary to scale",
            "Drafted the ownership line and the regulation line, and divided the site into the proposed investment plot (Th 1) and a garden area",
            "Dimensioned every boundary segment (for example 65.03 m, 79.73 m, 61.96 m, 47.15 m, 25.19 m) and the control diagonals, and calculated the area",
            "Added the surrounding context: the existing 20 m street, the 10 m walkway and the neighbouring existing property",
            "Added location insets from Google Earth imagery, the north arrow, a 1:500 scale bar, legend and site statistics table",
            "Completed the Amanah title block, land-use and phase fields, approval notes and the hydrological study recommendations"],
    findings=["Proposed municipal-investment site (Th 1): 5,000 m², commercial use, phase 1445 AH, with a garden area in the northern corner",
              "Bounded by an existing 20 m street to the west and south-west and a 10 m walkway to the north-east",
              "The hydrological study found no wadi channels or drainage courses through the site, so the whole area can be used",
              "Recommendations shown on the plan: grade the site following the natural north-to-south slope, drain surface water south to the existing road, link to the adjoining road slopes, and design curbs at least 20 cm high",
              "Issued as the preliminary-approval plan (مخطط الاعتماد الابتدائي) of the Planning and Government Land Allocation Department, Al-Qassim Region Municipality"],
    captions=["Preliminary-approval regulatory plan of the Rawd Al-Jawa investment site, drafted in AutoCAD from an old scanned map (1:500)"])

D["st-louis-parcel-criteria-map"] = dict(
    challenge="A real-estate investor needed to see at a glance which residential parcels in St. Louis fit their buying criteria: lots in specific size ranges, and in a second map only those lots that also have a 3,000–6,000 sq ft building. Parks had to stand out, while commercial, school and city-owned parcels had to be left blank. The client asked me to find all the data myself.",
    data=["Parcel polygons with zoning, property address, ZIP and lot area (sq ft)",
          "Building footprints / structure size for the lot-and-structure map",
          "Parks from OpenStreetMap (land-use class \"park\")",
          "OpenStreetMap basemap"],
    method=["Sourced the parcel, zoning and building data, then joined attributes and calculated lot area in square feet",
            "Filtered to residential parcels; commercial parcels, schools and city-owned land were kept but left without fill",
            "Classified lot size into the client's bands: under 13,000 sq ft no colour; 13,000–15,500 blue; 15,501–17,500 purple; 17,501–21,500 orange; 21,501–43,500 yellow; 43,501–200,000 red; over 200,000 no colour",
            "Added all parks in green as a separate layer",
            "For the second map, kept the lot-size colours only where the parcel's building is 3,000–6,000 sq ft; parcels with smaller or larger structures stay uncoloured",
            "Set up pop-ups showing zoning, owner, property address, ZIP and lot area, so the client can click any parcel",
            "Exported the QGIS project to an interactive Leaflet web map with qgis2web and hosted it for the client"],
    findings=["City-wide interactive map: zoom from the whole city down to individual lots on an OpenStreetMap base",
              "Colour classes make larger lots immediately visible, for example blocks of orange and yellow lots south of Delmar Boulevard",
              "Every parcel can be clicked for its zoning, address and exact lot area (for example a commercial parcel of 29,186 sq ft)",
              "Parks such as Forest Park and North Riverfront Park are shown in green for context"],
    captions=["Parcels colour-coded by lot size around Delmar Boulevard, with a parcel pop-up (address hidden here)",
              "City-wide view of the parcel layer with parks in green and a park pop-up from OpenStreetMap"])

D["qgis-polygon-point-digitisation"] = dict(
    challenge="The client had only a picture of a refinery's site plan, showing the West, East and Bay plants, process units and numbered emergency muster points. They needed it turned urgently into real GIS layers in the correct location, so the units and muster points could be used on a map with other data.",
    data=["Site-plan image supplied by the client (West Plant, East Plant and Bay Plant)",
          "OpenStreetMap basemap as the reference for georeferencing (streets such as 5th Ave. S. and 14th Street)",
          "Output projection: WGS 84 / Pseudo-Mercator (EPSG:3857)"],
    method=["Georeferenced the site-plan image in QGIS against OpenStreetMap, matching road intersections and plant boundaries, and saved a world file",
            "Created a polygon layer of process units with a Unit name field",
            "Traced every unit building from the plan and entered its name (for example FCCU 1, ALKY 3, SRU, Coker A and B)",
            "Labelled units whose name could not be read as \"Not Readable\" and units with no label as \"Not Mention\", so no guesses entered the data",
            "Created a point layer for the muster points and recorded each muster-point number",
            "Checked the geometry and labels against the source, then delivered the QGIS project, a GeoPackage and shapefiles"],
    findings=["60 process-unit polygons digitised: 27 named, 25 marked Not Readable and 8 marked Not Mention",
              "15 muster points captured (MP 1–13, 17 and 18) across the West, East and Bay plants",
              "All layers sit in their real location over OpenStreetMap, ready for further GIS analysis",
              "Delivered on an urgent deadline; the client left a 5.0★ review"],
    captions=["Digitised process units (named and unreadable) and muster points over the georeferenced site plan",
              "The digitised layers over OpenStreetMap in QGIS",
              "Working view: digitised unit outlines with their labels on the georeferenced plan"])

D["gee-dixie-fire-lst-ndvi"] = dict(
    challenge="Measure how a very large wildfire changed the land surface, from heat to vegetation, using only free satellite data. The aim was to run everything in the cloud, over a 3,894 km² burn perimeter, without downloading a single scene.",
    data=["Landsat 8 Collection 2 Level-2 surface reflectance and surface temperature (LANDSAT/LC08/C02/T1_L2), June–November 2021",
          "Dixie Fire perimeter uploaded as an Earth Engine asset (3,894 km²)",
          "Periods: pre-fire Jun 1 – Jul 13 (7 scenes), during-fire Jul 13 – Oct 25 (16 scenes), post-fire Oct 25 – Nov 30, 2021 (6 scenes)"],
    method=["Filtered the Landsat 8 collection to the fire perimeter and the June–November 2021 window",
            "Converted thermal Band 10 (ST_B10) to land surface temperature in °C with the Collection 2 scale factors (× 0.00341802 + 149.0 − 273.15)",
            "Calculated NDVI from Band 5 (NIR) and Band 4 (red) for every scene",
            "Split the collection at the ignition date (13 July) and the containment date (25 October) and took median composites for each period",
            "Subtracted pre-fire from during-fire LST to map temperature change",
            "Built the app interface: title, layer list, LST and temperature-difference legends and an information panel",
            "Charted mean LST and NDVI over the perimeter for every scene, and set up 30 m GeoTIFF exports to Google Drive for each LST layer and the difference map"],
    findings=["Mean NDVI inside the perimeter fell from 0.24 before the fire to 0.09 after it, a drop of about 63%, showing extensive vegetation loss",
              "The time-series chart tracks how surface temperature over the burn area changed through the fire season",
              "Median LST over the perimeter: 35.1 °C before the fire and 33.6 °C during it. Smoke and cloud in the during-fire scenes lower the thermal signal, so much of the difference map shows cooling",
              "Next step: apply the cloud-mask function (already written in the script) to every scene, and add a smoke filter, to sharpen the temperature-change map"],
    captions=["Median land surface temperature inside the Dixie Fire perimeter during the fire (Landsat 8 Band 10)",
              "Temperature change: during-fire minus pre-fire median LST",
              "Post-fire NDVI inside the perimeter (Oct 25 – Nov 30, 2021)",
              "The Earth Engine app: layers, legends and the LST time-series chart in the Code Editor"])
