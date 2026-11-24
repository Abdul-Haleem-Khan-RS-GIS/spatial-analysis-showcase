// Flood Susceptibility Mapping with AHP - Umluj, Saudi Arabia (Red Sea coast)
// Google Earth Engine Code Editor script by Abdul Haleem Khan
// Open in the Code Editor: https://code.earthengine.google.com/a798305d9e3ebf798b8601c8bb0d61c3
//
// An AHP (Analytic Hierarchy Process) extension of my multi-criteria flood risk work for Umluj.
// Built entirely from open global data, so anyone with an Earth Engine account can run it.
//
// Study area : the five HydroSHEDS level-8 basins that drain to the coast at and around Umluj
//              (Umluj coastal catchments, ~2,000 km2)
// Factors    : HAND, distance to drainage, slope, elevation, land cover
// Weights    : AHP pairwise comparison (Saaty 1-9 scale), consistency ratio checked (< 0.10)

// ---------------------------------------------------------------------------
// 1. STUDY AREA
// ---------------------------------------------------------------------------
var basinIds = [2080083890, 2080083850, 2080083930, 2080083880, 2080083920];
var basins = ee.FeatureCollection('WWF/HydroSHEDS/v1/Basins/hybas_8')
  .filter(ee.Filter.inList('HYBAS_ID', basinIds));
var aoi = basins.geometry();

Map.centerObject(aoi, 10);
Map.setOptions('SATELLITE');

// ---------------------------------------------------------------------------
// 2. FACTOR DATA
// ---------------------------------------------------------------------------
// Copernicus GLO-30 DEM (30 m)
var dem = ee.ImageCollection('COPERNICUS/DEM/GLO30').filterBounds(aoi)
  .select('DEM').mosaic().setDefaultProjection('EPSG:4326', null, 30).rename('elevation');
var slope = ee.Terrain.slope(dem).rename('slope');

// MERIT Hydro (90 m): HAND and upstream drainage area
var merit = ee.Image('MERIT/Hydro/v1_0_1');
var hand = merit.select('hnd').rename('hand');                 // height above nearest drainage (m)
var streams = merit.select('upa').gte(5).selfMask();           // channels draining >= 5 km2
var distance = streams.fastDistanceTransform(256).sqrt()
  .multiply(ee.Image.pixelArea().sqrt()).rename('distance');   // distance to drainage (m)

// ESA WorldCover 2021 (10 m)
var landcover = ee.ImageCollection('ESA/WorldCover/v200').first().rename('landcover');

// ---------------------------------------------------------------------------
// 3. RECLASSIFY EACH FACTOR TO A 1-5 SUSCEPTIBILITY SCORE (5 = most susceptible)
// ---------------------------------------------------------------------------
// Breaks are set from the factor distributions inside the study area.
function scoreLowIsHigh(img, b1, b2, b3, b4) {   // lower value = higher susceptibility
  return ee.Image(1)
    .where(img.lt(b4), 2)
    .where(img.lt(b3), 3)
    .where(img.lt(b2), 4)
    .where(img.lt(b1), 5)
    .updateMask(img.mask());
}

var sHand = scoreLowIsHigh(hand, 3, 8, 15, 35).rename('s_hand');            // m
var sDist = scoreLowIsHigh(distance, 150, 400, 800, 1300).rename('s_dist'); // m
var sSlope = scoreLowIsHigh(slope, 1.5, 3.5, 8, 15).rename('s_slope');      // degrees
var sElev = scoreLowIsHigh(dem, 20, 50, 150, 400).rename('s_elev');         // m

// Land cover: built-up and water 5, bare / sparse 4, cropland 3, grass & shrub 2, trees 1
var sLand = landcover.remap(
  [10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 100],
  [1,  2,  2,  3,  5,  4,  4,  5,  5,  5,  2]).rename('s_land');

// ---------------------------------------------------------------------------
// 4. AHP WEIGHTS
// ---------------------------------------------------------------------------
// Order: HAND, distance to drainage, slope, elevation, land cover
// Saaty scale: 1 equal, 3 moderate, 5 strong, 7 very strong, 9 extreme importance
var factorNames = ['HAND', 'Distance to drainage', 'Slope', 'Elevation', 'Land cover'];
var A = [
  [1,     2,     3,     5,   7],
  [1/2,   1,     2,     4,   5],
  [1/3,   1/2,   1,     3,   4],
  [1/5,   1/4,   1/3,   1,   2],
  [1/7,   1/5,   1/4,   1/2, 1]
];

// Priority vector: normalised geometric mean of each row
var n = A.length;
var gm = A.map(function (row) {
  return Math.pow(row.reduce(function (p, v) { return p * v; }, 1), 1 / n);
});
var gmSum = gm.reduce(function (s, v) { return s + v; }, 0);
var w = gm.map(function (v) { return v / gmSum; });

// Consistency: lambda_max, CI, CR (random index RI = 1.12 for n = 5)
var Aw = A.map(function (row) {
  return row.reduce(function (s, v, j) { return s + v * w[j]; }, 0);
});
var lambdaMax = Aw.reduce(function (s, v, i) { return s + v / w[i]; }, 0) / n;
var CI = (lambdaMax - n) / (n - 1);
var CR = CI / 1.12;

print('AHP weights', ee.Dictionary.fromLists(factorNames, w));
print('lambda_max', lambdaMax, 'CI', CI, 'CR (must be < 0.10)', CR);

// ---------------------------------------------------------------------------
// 5. WEIGHTED OVERLAY AND SUSCEPTIBILITY CLASSES
// ---------------------------------------------------------------------------
var fsi = sHand.multiply(w[0])
  .add(sDist.multiply(w[1]))
  .add(sSlope.multiply(w[2]))
  .add(sElev.multiply(w[3]))
  .add(sLand.multiply(w[4]))
  .rename('FSI')
  .clip(aoi);

// Five classes on the 1-5 index: very low ... very high
var fsiClass = ee.Image(1)
  .where(fsi.gte(1.8), 2)
  .where(fsi.gte(2.6), 3)
  .where(fsi.gte(3.4), 4)
  .where(fsi.gte(4.2), 5)
  .updateMask(fsi.mask())
  .rename('class')
  .clip(aoi);

// Equal-weights version, for a sensitivity comparison
var fsiEqual = sHand.add(sDist).add(sSlope).add(sElev).add(sLand).divide(5).clip(aoi);
var equalClass = ee.Image(1)
  .where(fsiEqual.gte(1.8), 2).where(fsiEqual.gte(2.6), 3)
  .where(fsiEqual.gte(3.4), 4).where(fsiEqual.gte(4.2), 5)
  .updateMask(fsiEqual.mask()).clip(aoi);

// ---------------------------------------------------------------------------
// 6. MAP LAYERS
// ---------------------------------------------------------------------------
var classPalette = ['#1a9641', '#a6d96a', '#ffffbf', '#fdae61', '#d7191c'];
Map.addLayer(hand.clip(aoi), {min: 0, max: 60, palette: ['#08306b', '#6baed6', '#f7fbff']}, 'HAND (m)', false);
Map.addLayer(distance.clip(aoi), {min: 0, max: 1500, palette: ['#08306b', '#6baed6', '#f7fbff']}, 'Distance to drainage (m)', false);
Map.addLayer(slope.clip(aoi), {min: 0, max: 25, palette: ['#ffffcc', '#fd8d3c', '#800026']}, 'Slope (deg)', false);
Map.addLayer(dem.clip(aoi), {min: 0, max: 1200, palette: ['#006837', '#ffffbf', '#a50026']}, 'Elevation (m)', false);
Map.addLayer(fsiClass, {min: 1, max: 5, palette: classPalette}, 'Flood susceptibility (AHP)');
Map.addLayer(streams.clip(aoi), {palette: ['#00e5ff']}, 'Drainage (>= 5 km2)', false);
Map.addLayer(ee.Image().byte().paint(basins, 1, 2), {palette: ['white']}, 'Study area (coastal catchments)');

// ---------------------------------------------------------------------------
// 7. LEGEND AND TITLE
// ---------------------------------------------------------------------------
Map.add(ui.Label('Umluj Flood Susceptibility - AHP', {
  stretch: 'horizontal', textAlign: 'center', fontWeight: 'bold', fontSize: '22px'
}));
var legend = ui.Panel({style: {position: 'bottom-left', padding: '8px 15px'}});
legend.add(ui.Label('Flood susceptibility', {fontWeight: 'bold', fontSize: '16px'}));
['Very low', 'Low', 'Moderate', 'High', 'Very high'].forEach(function (name, i) {
  legend.add(ui.Panel({
    widgets: [ui.Label('', {backgroundColor: classPalette[i], padding: '8px', margin: '0 0 4px 0'}),
              ui.Label(name, {margin: '0 0 4px 6px'})],
    layout: ui.Panel.Layout.Flow('horizontal')
  }));
});
Map.add(legend);

// ---------------------------------------------------------------------------
// 8. STATISTICS
// ---------------------------------------------------------------------------
function classAreas(classImg) {
  var areas = ee.Image.pixelArea().divide(1e6).addBands(classImg).reduceRegion({
    reducer: ee.Reducer.sum().group({groupField: 1, groupName: 'class'}),
    geometry: aoi, scale: 30, maxPixels: 1e10, bestEffort: true
  });
  return areas.get('groups');
}
print('Area by class, AHP (km2)', classAreas(fsiClass));
print('Area by class, equal weights (km2)', classAreas(equalClass));

// Built-up land (WorldCover class 50) by susceptibility class
var builtUp = landcover.eq(50);
var builtAreas = ee.Image.pixelArea().divide(1e6).updateMask(builtUp).addBands(fsiClass).reduceRegion({
  reducer: ee.Reducer.sum().group({groupField: 1, groupName: 'class'}),
  geometry: aoi, scale: 10, maxPixels: 1e11, bestEffort: true
});
print('Built-up area by class (km2)', builtAreas.get('groups'));

// Agreement between AHP and equal-weights classes
var agree = fsiClass.eq(equalClass).reduceRegion({
  reducer: ee.Reducer.mean(), geometry: aoi, scale: 90, maxPixels: 1e10, bestEffort: true
});
print('Share of area with the same class (AHP vs equal weights)', agree);

// ---------------------------------------------------------------------------
// 9. EXPORTS
// ---------------------------------------------------------------------------
Export.image.toDrive({
  image: fsiClass.toByte(), description: 'Umluj_Flood_Susceptibility_AHP_class',
  region: aoi, scale: 30, maxPixels: 1e10
});
Export.image.toDrive({
  image: fsi.toFloat(), description: 'Umluj_Flood_Susceptibility_AHP_index',
  region: aoi, scale: 30, maxPixels: 1e10
});
Export.table.toDrive({
  collection: basins, description: 'Umluj_coastal_catchments', fileFormat: 'SHP'
});

// ---------------------------------------------------------------------------
// 10. FLOOD-SENSOR SITING (answers the original question: where should sensors go?)
// ---------------------------------------------------------------------------
// Step 1 (Earth Engine): candidate sensor cells = main wadi channels (MERIT upstream area
//   >= 10 km2 for town gauges, >= 40 km2 for early-warning gauges) in the HIGH or VERY HIGH
//   AHP class, with distance to the nearest built-up pixel (ESA WorldCover class 50).
var builtDistance = landcover.eq(50).selfMask().reproject('EPSG:4326', null, 30)
  .fastDistanceTransform(512).sqrt().multiply(30).unmask(99999).rename('dist_builtup_m');
var classMax = fsiClass.reduceNeighborhood({reducer: ee.Reducer.max(), kernel: ee.Kernel.square(1)});
var townCandidates = merit.select('upa').gte(10).and(classMax.gte(4)).and(builtDistance.lte(3000)).selfMask();
Map.addLayer(townCandidates.clip(aoi), {palette: ['#ffd400']}, 'Town-gauge candidate cells', false);
//
// Step 2 (selection, done on the exported candidates):
//   * Town gauges: in each wadi system, the candidate with the largest drainage area
//     (the point where the wadi reaches built-up land); sites closer than 1.5 km merged;
//     wadis draining >= 50 km2 kept -> 7 town gauges, ranked by drainage area.
//   * Early-warning gauges: on the 3 largest wadis, a candidate at least 2 km from built-up
//     land whose flow path (traced cell by cell on the MERIT Hydro D8 flow-direction grid)
//     reaches that wadi's town gauge, with drainage area closest to half of the town gauge's.
//     Wadi 1 collects most of its water outside the study basins, so its gauge sits where
//     the channel enters the study area.
//
// Result: recommended network (WGS 84). Drainage area from MERIT Hydro, km2.
var sensors = ee.FeatureCollection([
  ee.Feature(ee.Geometry.Point([37.2294, 25.2023]), {id: 'T1', role: 'town gauge', drainage_km2: 871}),
  ee.Feature(ee.Geometry.Point([37.2643, 25.1158]), {id: 'T2', role: 'town gauge', drainage_km2: 792}),
  ee.Feature(ee.Geometry.Point([37.2851, 24.9678]), {id: 'T3', role: 'town gauge', drainage_km2: 350}),
  ee.Feature(ee.Geometry.Point([37.3084, 25.1807]), {id: 'T4', role: 'town gauge', drainage_km2: 174}),
  ee.Feature(ee.Geometry.Point([37.2751, 24.9486]), {id: 'T5', role: 'town gauge', drainage_km2: 158}),
  ee.Feature(ee.Geometry.Point([37.2909, 24.9411]), {id: 'T6', role: 'town gauge', drainage_km2: 148}),
  ee.Feature(ee.Geometry.Point([37.2593, 25.0842]), {id: 'T7', role: 'town gauge', drainage_km2: 127}),
  ee.Feature(ee.Geometry.Point([37.2646, 25.2878]), {id: 'E1', role: 'early warning for T1', drainage_km2: 830, channel_km_to_town_gauge: 15.5}),
  ee.Feature(ee.Geometry.Point([37.4773, 25.1091]), {id: 'E2', role: 'early warning for T2', drainage_km2: 645, channel_km_to_town_gauge: 33.5}),
  ee.Feature(ee.Geometry.Point([37.4482, 24.9984]), {id: 'E3', role: 'early warning for T3', drainage_km2: 273, channel_km_to_town_gauge: 23.9})
]);
Map.addLayer(sensors.filter(ee.Filter.stringStartsWith('id', 'T')), {color: 'FFD400'}, 'Town gauges (T1-T7)');
Map.addLayer(sensors.filter(ee.Filter.stringStartsWith('id', 'E')), {color: '00E5FF'}, 'Early-warning gauges (E1-E3)');
print('Recommended flood-sensor sites', sensors);
Export.table.toDrive({collection: sensors, description: 'Umluj_flood_sensor_sites', fileFormat: 'SHP'});
