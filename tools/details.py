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
    links=[("See the AHP extension of this study", "umluj-flood-susceptibility-ahp.html")],
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
    method=["Overlaid parcels with the hazard zones", "Summarised parcels by zone",
            "Calculated, for every Riverside neighbourhood, the share of its area inside classified fire hazard zones, and mapped it in four classes (0–11%, 12–41%, 42–63%, 64–100%)",
            "Neighbourhood case study of Alessandro Heights"],
    findings=["Very-high hazard zones run along the city's western and southern edges next to open land",
              "Alessandro Heights has the highest exposure: 88.2% of its area lies in classified fire hazard zones",
              "La Sierra Hills and Sycamore Canyon Park are also in the highest class (64–100%), and University, Canyon Crest and Sycamore Canyon/Canyon Springs fall in the 42–63% class; the central neighbourhoods are mostly below 11%"],
    captions=["Residential parcels by fire hazard zone in Riverside, California",
              "Riverside neighbourhoods by share of area within classified fire hazard zones; Alessandro Heights 88.20%"])

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
    challenge="Measure how a very large wildfire changed the land surface, from heat to vegetation, using only free satellite data processed in the cloud over the 3,894 km² burn perimeter. The first version compared June (before the fire) with July–October (during it). Because of the seasonal cooling and smoke, it wrongly suggested the burned area had cooled, so the method had to be fixed.",
    data=["Landsat 8 Collection 2 Level-2 surface reflectance and surface temperature (LANDSAT/LC08/C02/T1_L2), 2019–2022",
          "Dixie Fire perimeter uploaded as an Earth Engine asset (3,894 km²)",
          "Unburned control ring: a 5 km band around the perimeter",
          "2021 fire season: ignition 13 July, containment 25 October; impact comparison: summer (Jun 15 – Aug 31) 2020 vs 2022"],
    method=["Applied a QA_PIXEL mask to every Landsat scene to remove cloud, dilated cloud, cirrus, cloud shadow and snow",
            "Converted thermal Band 10 to land surface temperature in °C with the Collection 2 scale factors, and calculated NDVI from Bands 5 and 4",
            "Kept the 2021 fire-season layers (pre-, during- and post-fire median LST, post-fire NDVI)",
            "Measured fire impact season to season: median summer 2022 minus median summer 2020, for both LST and NDVI, so normal seasonal cooling no longer hides the signal",
            "Used a 5 km unburned ring around the perimeter as a control, to separate the fire effect from year-to-year weather",
            "Printed burn-scar vs control-ring statistics, charted both regions from June 2020 to September 2022, and set up 30 m GeoTIFF exports for all change layers"],
    findings=["Summer land surface temperature inside the perimeter rose from 34.2 °C (2020) to 43.9 °C (2022), +9.7 °C, while the unburned ring rose only 1.7 °C",
              "Before the fire, the forest was 1.4–2.1 °C cooler than its surroundings (2019 and 2020). After the fire, it was 5.8 °C hotter: a swing of about 8 °C caused by the burn",
              "Summer NDVI inside the perimeter fell from 0.24 to 0.13 (about −46%), while the control ring stayed at 0.21: vegetation loss limited to the burn scar",
              "Lesson learned: comparing different seasons, without cloud masking, gave a false cooling signal. Season-to-season comparison with a control area gave a clear, defensible result"],
    captions=["Land surface temperature change in the same season, summer 2022 minus summer 2020 (cloud-masked)",
              "Summer means inside the burn perimeter vs the unburned 5 km ring, 2019, 2020 and 2022",
              "Vegetation change (NDVI), summer 2022 minus summer 2020",
              "Land surface temperature in the first summer after the fire (2022)"])

D["umluj-flood-susceptibility-ahp"] = dict(
    challenge="In 2025, Sadeem International Company asked me for an environmental assessment of Umluj city and its surroundings, to decide where to install flood sensors. That meant answering one question: where is flooding most likely? I delivered a multi-criteria flood risk map, rated 5.0★. In any weighted overlay, the weights drive the result, and sensor placement depends on them, so they need to be explained and defended. This extension rebuilds the analysis with the Analytic Hierarchy Process (AHP), so every weight comes from a documented pairwise comparison with a consistency check. The whole model runs in Google Earth Engine from open global data that anyone can reproduce.",
    data=["Study area: the five HydroSHEDS level-8 basins draining to the coast at and around Umluj (1,999 km²); the original client AOI file was not delivered, so a watershed boundary is used",
          "Copernicus GLO-30 DEM (30 m): elevation and slope",
          "MERIT Hydro (90 m): HAND (height above nearest drainage) and upstream area; channels draining at least 5 km²",
          "ESA WorldCover 2021 (10 m): land cover",
          "Sentinel-2 2023 composite as the map background"],
    method=["Delineated the study area from HydroSHEDS level-8 basins, so it follows real catchments rather than an arbitrary box",
            "Derived five flood factors: HAND, distance to drainage, slope, elevation and land cover",
            "Reclassified each factor to a 1–5 susceptibility score with breaks set from its distribution in the study area (for example HAND under 3 m = 5, over 35 m = 1)",
            "Built the AHP pairwise comparison matrix on Saaty's 1–9 scale and derived the weights: HAND 43.4%, distance to drainage 27.1%, slope 17.1%, elevation 7.5%, land cover 4.8%",
            "Checked consistency: λmax 5.079, CI 0.020, CR 0.018, well below the 0.10 limit",
            "Combined the factors in a weighted overlay and classified the index into five classes, from very low to very high",
            "Ran a sensitivity test with equal weights and measured built-up exposure with WorldCover",
            "Sited flood sensors: candidate cells on the main wadis in the high or very high class; one town gauge per wadi system where it meets built-up land, ranked by drainage area",
            "Added upstream early-warning gauges on the three largest wadis, checked by tracing each candidate's flow path cell by cell on the MERIT Hydro flow-direction grid to make sure it drains to that wadi's town gauge",
            "Exported the susceptibility rasters and the sensor sites (shapefile, GeoJSON, CSV)"],
    findings=["Very high susceptibility covers 238 km² (12%) and high 436 km² (22%), concentrated along the wadi network and the low coastal plain around Umluj",
              "68% of built-up land in the catchments (10.9 of 16.1 km²) falls in the high or very high classes",
              "Sensitivity: AHP and equal weights give the same class for 71% of the area, but AHP identifies about 3× more very-high land (238 vs 75 km²) along the drainage lines, where flash floods actually run",
              "Recommended network: 10 sensors. 7 town gauges (T1–T7) where wadis draining 127–871 km² reach built-up land, plus 3 early-warning gauges (E1–E3) 15.5–33.5 km upstream along the channel on the three largest wadis",
              "Consistent with the original client map: wadi channels and the coastal plain are the highest-risk zones, and the elevated eastern ground is lowest"],
    captions=["Flood susceptibility of the Umluj coastal catchments from the AHP weighted overlay",
              "The five flood factors with their AHP weights, and the 1–5 reclassification rules",
              "AHP pairwise comparison matrix with consistency check, and area by susceptibility class (AHP vs equal weights)",
              "Sensitivity test: AHP weights vs equal weights",
              "Recommended flood-sensor network: 7 town gauges and 3 upstream early-warning gauges on the AHP map",
              "Sensor sites with coordinates, drainage area, distance to built-up land and channel distance"])

D["uyun-al-jawa-municipal-gis"] = dict(
    challenge="Uyun Al Jawa Governorate in Al-Qassim is growing around several settlements, including Uyun Al Jawa city, Al-Jawa, Rawd Al-Jawa and Ghaf Al-Jawa. The municipality needed one reliable, approved picture of its land: what each area is zoned for, which land belongs to the municipality and is reserved for investment, where the urban boundary runs, and how new subdivisions fit in. Most plans existed only as AutoCAD drawings, so they had to be brought accurately into GIS before they could be mapped together. These are the maps planners, the Amanah and the Ministry sign off on.",
    data=["Municipal parcel and subdivision plans (approved plan numbers, e.g. 3045/ق)",
          "Land-use survey and municipal land records (allocated and reserved investment lands)",
          "Urban boundary, development-limit and municipal-services boundaries",
          "Road network by class (30 m secondary and main, 40 m arterial, 100 m ring road)",
          "High-resolution satellite imagery as the map base"],
    method=["Drew municipal subdivision plans in AutoCAD to Ministry drafting standards: plot boundaries, regulation lines, roads with their widths, services and land-use tables (e.g. Government Residential Plans 2505 and 3045)",
            "Transferred each AutoCAD plan into GIS accurately: cleaned the drawing (closed plot polygons, removed duplicates and gaps), set the correct coordinate system (UTM) and placed it on its true location",
            "Checked the positional accuracy of each transferred plan against high-resolution satellite imagery, survey points and neighbouring approved plans, adjusting it until plot and road edges matched",
            "Converted the CAD layers into GIS feature classes (plots, blocks, roads, services, boundaries) and attached attributes: plan number, plot number, land use, area and ownership status",
            "Merged all transferred plans into the municipal geodatabase, keeping topology clean so neighbouring plans meet without overlaps or gaps",
            "Built the Municipal Lands Plans Document from this database (ArcMap 10.9, 2025): land use in 11 classes, municipal lands allocated or reserved for investment, urban and development boundaries and the road hierarchy, with definitions, general rules and the approval block for the municipality, the Al-Qassim Region Municipality and the Ministry of Municipalities and Housing",
            "Mapped the areas reserved for municipal investments (2026) from the same database, classifying each site as new or existing and overlaying the new subdivision plans and the development boundary",
            "Coordinated GPS field collection, shared GIS data across departments and delivered GIS training to Uyun Al Jawa staff"],
    findings=["A complete CAD-to-GIS workflow: every plan is drawn in AutoCAD, transferred into GIS at its true location, and becomes part of one municipal database",
              "One approved reference map of land use and municipal land for the whole governorate, built from the transferred plans and signed off up to the Amanah and the Ministry",
              "A clear inventory of the municipality's investment land, separating new reservations from existing ones",
              "Plans linked to the GIS by plan and plot number, so planners can move between the AutoCAD drawing and the map for any parcel"],
    captions=["Municipal Lands Plans Document, Uyun Al Jawa Governorate: land use, municipal investment lands, urban boundaries and roads (ArcMap, 2025)",
              "Areas reserved for municipal investments, classified as new or existing, with new subdivision plans and the development boundary (ArcMap, 2026)",
              "Government Residential Plan 2505/ق (amended), Uyun Al Jawa, 1:5000: final AutoCAD drawing with plot tables, road cross-sections, notes and title block",
              "Plan 2505 detail: central mosque square, schools, health centre, parks and walkways, parking and numbered plots",
              "Government Residential Plan 3045/ق, east of Uyun Al Jawa, 1:1500: 72 plots, 2 mosques, a boys' school, road cross-sections, plot tables and building regulations (final AutoCAD drawing)",
              "Structural plan of Al-Jawa city from the national informal-settlements study (Ministry of Municipal and Rural Affairs; Talal Adham & Partners), used as a planning reference"])

# ---- 2026-11 audit: details expanded from the delivered data, maps and reports ----
D["riyadh-postcode-map"].update(
    data=["Postal-code reference boundaries for Riyadh", "District names for every zone", "Satellite basemap for checking"],
    method=["Delineated the postal-code zones in QGIS and ArcGIS Pro, in WGS 84 / UTM zone 38N (EPSG:32638)",
            "Attached the district name (Dist_Name) and postal code (Zip_Code) to every polygon",
            "Checked attributes and topology so neighbouring zones share edges, with no gaps or overlaps",
            "Exported to GeoJSON and shapefile for web and GIS use"],
    findings=["996 postal-code polygons carrying 988 distinct postal codes across 177 named districts",
              "The layer covers about 3,760 km² of Riyadh, from roughly 46.3°E to 47.1°E and 24.3°N to 25.2°N",
              "Delivered as GeoJSON and shapefile, ready for web maps and GIS platforms"],
    result="Postal-code polygon dataset for the whole city (996 zones, 988 postal codes, 177 districts) in GeoJSON and shapefile, plus a map.")

D["zip-code-territory-map"].update(
    summary="Built a territory around four ZIP code areas in the Cleveland area (44115, 44122, 44130, 44145) with a 10-mile reach, added county, municipal and school-district boundaries, and selected the schools and public facilities inside it from OpenStreetMap.",
    data=["Census 2020 ZCTA boundaries for 44115, 44122, 44130 and 44145",
          "Boundaries of seven counties (Cuyahoga, Lorain, Medina, Summit, Portage, Geauga, Lake), 59 Cuyahoga municipalities and 31 school districts",
          "53,130 OpenStreetMap points of 187 types for the area"],
    method=["Selected the four ZCTAs and created a centroid point for each",
            "Built a 10-mile buffer around them and dissolved it into one territory (about 2,900 km²)",
            "Added county, municipal and school-district boundaries for context",
            "Filtered the 53,130 OpenStreetMap points down to schools and public facilities inside the territory",
            "Packaged all layers with the map"],
    findings=["371 facilities selected inside the territory: 236 schools, 48 post offices, 44 social facilities, 30 police stations, 11 hospitals, 1 university and 1 public building",
              "The territory spans parts of seven counties around Cleveland, not just Cuyahoga",
              "Every layer was delivered as a shapefile so the client can redraw or extend the territory"])

D["solar-plant-gis-dataset"].update(
    where="Solar power plant site, Saudi Arabia",
    data=["Engineering layout drawings (CAD) supplied by the client",
          "All layers built in WGS 84 / UTM zone 38N (EPSG:32638)"],
    method=["Milestone 1 (approved): fenced project boundary, 240 PV block boundaries with Block IDs, 2 substations and 960 MV power-station components (240 each of RMU, transformer, inverter and UPS)",
            "Pile layer: 547,055 pile points with easting, northing and Block ID",
            "LV/DC trench layers split by trench width (350, 425, 550, 675, 1,300, 1,550 and 1,800 mm, all 900 mm deep), plus PV trenches and 12-in-1 and 16-in-1 DC combiner-box trenches",
            "Milestone 2 (approved): MV cable layer, 624 segments in 12 MV trench circuits",
            "Milestone 3 (approved): all review comments closed"],
    findings=["A plant of about 38 km² inside the fence, laid out in 240 blocks covering about 32.6 km²",
              "Cable network: about 295 km of MV cable routes and about 149 km of LV trenches, each attributed to its block",
              "Full set of attributed shapefiles delivered across three approved milestones ($1,000 contract)",
              "Client review: “He did very well Job delivered his project on time.”"])

D["global-mapper-csv-export-script"].update(
    data=["Four shapefile layers (Layer1 to Layer4) supplied by the client", "Point features in England, around 53.3°N, 1.0°W"],
    findings=["One script replaces four manual exports: each layer is imported, written to its own CSV and unloaded",
              "Each CSV holds 99 points with longitude and latitude in degrees-minutes-seconds and in decimal degrees (X, Y), plus elevation, name and label fields",
              "Delivered the script, four sample CSV outputs and a step-by-step guide to every command"])

D["aerial-image-manual-classification"].update(
    data=["Aerial image supplied by the client (not georeferenced)", "Interpretation key built for the job (colour, texture, structure, size, shape, context)"],
    findings=["80 digitised polygons: 65 buildings, 6 meadows, 5 parking lots, 2 agricultural fields, 1 forest/tree area and 1 road",
              "Complete land-cover map with attributed polygons delivered as a shapefile",
              "Interpretation key and ambiguity table make the classification reproducible",
              "Recommended georeferencing the image first and a second-reviewer check for ambiguous areas"])

D["nps-map-redesign"].update(
    findings=["Colour: a brighter but balanced palette separates dense forest, meadows and water, and clearer elevation shading makes terrain readable at a glance",
              "Symbols: simplified icons with a subtle shadow stay visible over forest and rugged terrain; solid, dashed and dotted lines separate paved roads, trails and minor paths",
              "Labels: hierarchy by type size and style, contour labels following the terrain, and no text over important features",
              "Finished map plus a written report recommending these changes for future NPS maps"])

D["zurich-population-density"].update(
    method=["Joined population counts for ages 25–45 to the 100 m × 100 m grid",
            "Clipped the grid to the Zurich city boundary",
            "Classified residents per cell into three classes (0–28.3, 28.4–48.9 and 49–100)",
            "Designed a clean thematic layout with legend, north arrow and scale"],
    findings=["Density peaks in a band running through the centre and north of the city",
              "Grid cells follow the built-up valleys; forested hills and the lake have no residents",
              "The highest class (49–100 residents aged 25–45 per hectare) clusters in the inner districts"],
    result="Print-ready map of residents aged 25–45 per 100 m cell, in three classes.")

D["racehorse-facility-location-map"].update(
    where="Texas and Louisiana, USA",
    data=["Property location supplied by the client",
          "Five race tracks: Sam Houston Race Park, Delta Downs, Louisiana Downs, Evangeline Downs and Fair Grounds Race Course",
          "U.S. state boundaries for the main map and a national inset"],
    method=["Plotted the property and the five tracks with distinct symbols",
            "Added leader lines, track icons and labels to each track",
            "Added a U.S. inset map highlighting the region, plus a scale bar in kilometres",
            "Exported high-resolution PNG, JPG and PDF"],
    findings=["One graphic shows the property's position relative to all five tracks across Texas and Louisiana",
              "High-resolution location graphic (20 MB PNG and 16 MB PDF) ready for marketing"])

D["swiss-client-employee-strategy-maps"].update(
    summary="Strategy maps for a Swiss cleaning company: clients (red) and employees (green) by postal code, with circle size by count, over city population and water bodies, and a later postal-code map shaded by client count.",
    data=["Client and employee address lists (Excel)", "Swiss postal-code points, district, canton and country boundaries",
          "City population (10,019 to 421,878) and water bodies"],
    method=["Geocoded clients and employees and aggregated them by postal code",
            "Sized client symbols in five classes (1 to 32 clients per postal code) and employee symbols from 1 to 5",
            "Added city population circles, lakes and administrative boundaries for context"],
    findings=["Clients concentrate in and around Zurich, with smaller clusters around Lucerne and Bern",
              "Employees live mostly in the Zurich area, close to the main client cluster",
              "Large cities such as Geneva, Basel and Lausanne show few or no clients on the map"])

D["zurich-daycare-centres"].update(
    method=["Geocoded every daycare centre (Kita) address to a point",
            "Added buildings, roads, Lake Zurich and other water bodies as context",
            "Designed a print-ready city map with legend, north arrow and scale"],
    findings=["Kitas spread across all the built-up districts of the city",
              "No Kitas in the forested hills and the lake, which frame the city's coverage",
              "City-wide daycare map delivered as a print-ready PDF"])

D["summer-campground-suitability"].update(
    where="Eastern San Diego County, California, USA",
    data=["Relief/DEM", "Rivers and lakes", "Major roads (I-8, SR-78, SR-79 and local roads)", "Emergency services", "Study-area boundary"],
    findings=["The largest group of suitable sites lies in the south-east of the study area, along Sunrise Highway",
              "Smaller groups sit near SR-79 in the north, at San Felipe, and next to I-8 and Old Highway 80 in the south",
              "Most suitable sites lie close to a road and within a few miles of one of the six emergency-service points"],
    result="Suitability map of campground locations, with emergency services, roads and water, at a 12-mile scale.")

D["bike-route-network-analysis"].update(
    where="Gaisberg, Salzburg, Austria",
    data=["OpenStreetMap road and path network", "Hillshade/DEM", "Reference GPS track from a test ride",
          "Start and end points: the Natural Sciences Faculty and Gaisberg"],
    findings=["Route A is the shortest at 6.8 km but the slowest, at 7 h 39 min, because it climbs the steepest ground",
              "Route B: 12.5 km in 2 h 08 min; Route C: 14.5 km in 1 h 58 min; Route D: 15.2 km in 2 h 00 min",
              "Longer routes on gentler gradients were up to about four times faster than the shortest path",
              "This shows why distance-based routing fails in steep terrain and slope has to be in the cost"],
    result="Four alternative routes from the Natural Sciences Faculty to Gaisberg compared by length and travel time against a test ride.")

D["sahiwal-city-comprehensive-plan"].update(
    data=["Land-use survey of MC Sahiwal (17 land-use classes)", "Road hierarchy, GT Road, Sahiwal Bypass and railway",
          "MC (2013 and 2019), EBA boundaries, state land and approved housing societies",
          "Proposed water supply and sewerage system (NESPAK)", "Imagery"],
    method=["Mapped existing land use across 17 classes, from residential, commercial and industry to orchards, graveyards and vacant land",
            "Residential suitability analysis, classed as highly, marginally or not suitable",
            "Industrial suitability analysis with the same three classes",
            "Development scenarios to 2042; for Scenario III, laid out residential zones 1–4, commercial and infill mixed-use zones, proposed industry, reserved agriculture and a proposed ring road",
            "Overlaid the proposed water supply and sewerage network on the development zones"],
    findings=["The built-up core sits along GT Road and the railway, surrounded by agricultural land inside the MC boundary",
              "The most suitable land for new housing lies in the west and north, with marginal land in the north-east",
              "Highly suitable industrial land is limited, mainly in the west near Harappa Road",
              "Scenario III directs growth into four residential zones inside a proposed ring road, with industry in the east and south-west and agriculture reserved to the west"])

D["sialkot-city-comprehensive-plan"].update(
    data=["Land-use survey of the Sialkot study area (14 land-use classes)",
          "M11 motorway, railway, primary and secondary roads",
          "Upper Chenab Canal, Marala Ravi Link Canal and the city's nullahs",
          "MC, cantonment and study-area boundaries", "Esri/Maxar imagery basemap"],
    findings=["A dense residential and commercial core around the old city, with the cantonment occupying the north-east",
              "Industry is scattered along the main radial roads, notably towards Wazirabad and Daska",
              "Agriculture still surrounds the city inside the study-area boundary, the land the plan must manage for growth"])

D["batswat-terrain-assessment"].update(
    where="Batswat, Ishkoman valley, Ghizer, Gilgit-Baltistan, Pakistan",
    data=["DEM of the study area", "Land-use survey (agriculture, cattle sheds, sloping barren and vegetated land, community buildings, school, Jamat Khana, wood factory and others)",
          "Ishkoman River, Ishkoman Road and Batswat Link Road", "Pakistan, Gilgit-Baltistan and Ghizer boundaries for the insets"],
    method=["Mapped land use in the study area, including a GLOF (glacial lake outburst flood) zone",
            "Processed the DEM and calculated slope in degrees, in 10 classes from under 3.2° to 45°",
            "Generated contours across the study area",
            "Built a location map with insets for Pakistan, Gilgit-Baltistan and Ghizer"],
    findings=["Flat land (under about 3°) is limited to the river terrace along the Ishkoman River in the north-west",
              "Slopes rise steeply to the south-east, up to about 45°, which limits where new homes can go",
              "A GLOF hazard area at the south-west end of the valley was mapped as a constraint for habitat planning"])

D["indonesia-landuse-school-locator"].update(
    data=["Natural land-use features: beach, cave, cliff, peak, spring and glacier", "School locations", "Primary roads, water bodies and the national boundary", "World boundaries for the inset"],
    method=["Built a national map of Indonesia with primary roads, water bodies and the country boundary",
            "Mapped natural land-use features in six classes and school locations as point symbols",
            "Added a world inset that highlights Indonesia, plus a separate location map at 0–2,000 km scale",
            "Produced a district-level version for Wonosobo, Central Java"],
    findings=["School points concentrate on Java, with further clusters in Sumatra, Bali and the Lesser Sunda islands",
              "Road density follows the same pattern: dense on Java and Sumatra, sparse in Kalimantan and Papua",
              "Two layouts delivered: a national land-use and school locator map and a location map of Indonesia"])


D["scanned-contours-to-kmz"] = dict(
    title="1-ft Contours to SHP, KMZ & CAD: Cherokee County, NC",
    where="Cherokee County, North Carolina, USA",
    tools=["ArcMap", "AutoCAD 2023", "Export to CAD", "Shapefile", "KMZ", "DWG"],
    summary="Clipped 1-ft contours to a client's area of interest in Cherokee County, North Carolina, and delivered them as an attributed shapefile, a KMZ for Google Earth and an AutoCAD file.",
    challenge="The client needed detailed 1-ft contours for a site near the Hiwassee River and Apalachia Lake, in formats they could use in GIS, in Google Earth and in AutoCAD. The full delivery came to more than 700 MB.",
    data=["1-ft contour data for Cherokee County, North Carolina (vector contours and a raster contour layer)",
          "Client's centre point, used to build a one-mile buffer and the area-of-interest box",
          "Esri World Street Map basemap for checking"],
    method=["Plotted the client's centre point and built a one-mile buffer and an area-of-interest box around it",
            "Clipped the contours to the AOI, keeping the elevation (Contour) and index-contour (Index) attributes",
            "Checked contour continuity and elevation labels at large scale",
            "Exported the clipped contours as a shapefile, as a KMZ for Google Earth and as an AutoCAD file with Export to CAD",
            "Checked the DWG in AutoCAD 2023: contours sit on an AOI Contours layer as polylines carrying their elevation (for example 1,278 ft)"],
    findings=["9,986 contour lines in the area of interest at a 1-ft interval, with every fifth foot flagged as an index contour",
              "Elevations run from about 1,277 ft near the lake shore to over 1,650 ft on the ridges",
              "Delivered as SHP, KMZ and CAD, more than 700 MB in total"],
    result="Attributed 1-ft contour shapefile, KMZ and AutoCAD file (9,986 lines) for the client's area of interest, more than 700 MB in total.",
    note="The delivered files are not published here because the package is more than 700 MB.",
    captions=["Area of interest (red box) over the Hiwassee River and Apalachia Lake, Cherokee County, NC",
              "Clipped 1-ft contours with elevation labels and the contour attribute table (9,986 features)",
              "Delivered DWG (AOI Contours.dwg) open in AutoCAD 2023, with each contour polyline carrying its elevation"])
