// Dixie Fire 2021 - Land Surface Temperature and NDVI Analysis (v2)
// Google Earth Engine Code Editor script by Abdul Haleem Khan
// Open in the Code Editor: https://code.earthengine.google.com/41b9b32b5c8690a4727865efe43eb71a
//
// Import used by this script (set in the Code Editor "Imports" panel):
//   var table = ee.FeatureCollection('projects/ee-abdulhaleemk03/assets/DixieFire2021');  // Dixie Fire perimeter
//
// v2 changes:
//  * The cloud / cloud-shadow / snow / cirrus mask is now applied to every Landsat scene.
//  * Fire impact is measured season-to-season: summer 2022 (burn scar) minus summer 2020
//    (pre-fire), so normal seasonal cooling no longer hides the fire signal.
//  * A 5 km unburned ring around the perimeter is used as a control, so regional
//    year-to-year weather differences are separated from the fire effect.

// --- TITLE ---
var title = ui.Label('Dixie Fire 2021 - LST & NDVI Analysis', {
  stretch: 'horizontal',
  textAlign: 'center',
  fontWeight: 'bold',
  fontSize: '24px'
});
Map.add(title);

// --- FIRE AREA IMPORT ---
var dixieFireAsset = ee.FeatureCollection(table);
var dixieFireArea = dixieFireAsset.geometry();

// Unburned control ring: 5 km band outside the perimeter
var controlRing = dixieFireArea.buffer(5000, 500).difference(dixieFireArea, 500);

// --- MAP SETTINGS ---
Map.centerObject(dixieFireArea, 9);
Map.setOptions('SATELLITE');

// --- TIME PERIODS ---
// 2021 fire season
var startDatePreFire = '2021-06-01';
var fireStartDate = '2021-07-13';
var fireContainmentDate = '2021-10-25';
var endDatePostFire = '2021-11-30';
// Same-season comparison: summer before the fire vs the first summer after it
var summerBefore = ['2020-06-15', '2020-08-31'];
var summerAfter = ['2022-06-15', '2022-08-31'];

// --- CLOUD MASKING (QA_PIXEL bits: 1 dilated cloud, 2 cirrus, 3 cloud, 4 shadow, 5 snow) ---
function maskL8sr(image) {
  var qa = image.select('QA_PIXEL');
  var mask = qa.bitwiseAnd(1 << 1).eq(0)          // Dilated cloud
             .and(qa.bitwiseAnd(1 << 2).eq(0))    // Cirrus
             .and(qa.bitwiseAnd(1 << 3).eq(0))    // Cloud
             .and(qa.bitwiseAnd(1 << 4).eq(0))    // Cloud shadow
             .and(qa.bitwiseAnd(1 << 5).eq(0));   // Snow
  return image.updateMask(mask);
}

// --- CALCULATE LST ---
function calculateLST(image) {
  var thermal = image.select('ST_B10');
  var lst = thermal.multiply(0.00341802).add(149.0).subtract(273.15); // Collection 2 scale factors, to Celsius
  return image.addBands(lst.rename('LST'));
}

// --- CALCULATE NDVI ---
function addNDVI(image) {
  var ndvi = image.normalizedDifference(['SR_B5', 'SR_B4']).rename('NDVI');
  return image.addBands(ndvi);
}

// --- LOAD AND PROCESS LANDSAT 8 ---
function landsat(start, end) {
  return ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
    .filterBounds(dixieFireArea)
    .filterDate(start, end)
    .map(maskL8sr)            // v2: mask is now applied
    .map(calculateLST)
    .map(addNDVI);
}

var landsatProcessed = landsat(startDatePreFire, endDatePostFire);

// --- 2021 FIRE-SEASON COMPOSITES ---
var preFire = landsatProcessed.filterDate(startDatePreFire, fireStartDate);
var duringFire = landsatProcessed.filterDate(fireStartDate, fireContainmentDate);
var postFire = landsatProcessed.filterDate(fireContainmentDate, endDatePostFire);

var preFireLST = preFire.select('LST').median();
var duringFireLST = duringFire.select('LST').median();
var postFireLST = postFire.select('LST').median();
var postFireNDVI = postFire.select('NDVI').median();

// --- SAME-SEASON COMPARISON: SUMMER 2020 vs SUMMER 2022 ---
var summer2020 = landsat(summerBefore[0], summerBefore[1]);
var summer2022 = landsat(summerAfter[0], summerAfter[1]);

var lst2020 = summer2020.select('LST').median();
var lst2022 = summer2022.select('LST').median();
var ndvi2020 = summer2020.select('NDVI').median();
var ndvi2022 = summer2022.select('NDVI').median();

// Temperature and vegetation change in the same season (2022 minus 2020)
var tempDifference = lst2022.subtract(lst2020).rename('temp_diff');
var ndviDifference = ndvi2022.subtract(ndvi2020).rename('ndvi_diff');

// --- VISUALIZATION PARAMETERS ---
var lstPalette = ['#000080', '#0000D9', '#4000FF', '#8000FF', '#0080FF', '#00FFFF',
                  '#00FF80', '#80FF00', '#DAFF00', '#FFFF00', '#FFF500', '#FFDA00',
                  '#FFB000', '#FF7400', '#FF0000', '#A90000'];

var lstVis = {min: 0, max: 50, palette: lstPalette};

var diffColors = ['#2c7bb6', '#abd9e9', '#ffffbf', '#fdae61', '#d7191c'];
var tempDiffVis = {min: -5, max: 20, palette: diffColors};

var ndviPalette = ['#d73027', '#f46d43', '#fdae61', '#fee08b',
                   '#d9ef8b', '#a6d96a', '#66bd63', '#1a9850'];
var ndviVis = {min: -0.2, max: 0.8, palette: ndviPalette};
var ndviDiffVis = {min: -0.4, max: 0.1, palette: ['#8c510a', '#d8b365', '#f6e8c3', '#c7eae5', '#5ab4ac']};

// --- ADD LAYERS ---
Map.addLayer(preFireLST.clip(dixieFireArea), lstVis, 'Pre-Fire LST 2021 (°C)', false);
Map.addLayer(duringFireLST.clip(dixieFireArea), lstVis, 'During-Fire LST 2021 (°C)', false);
Map.addLayer(postFireLST.clip(dixieFireArea), lstVis, 'Post-Fire LST 2021 (°C)', false);
Map.addLayer(postFireNDVI.clip(dixieFireArea), ndviVis, 'Post-Fire NDVI 2021', false);
Map.addLayer(lst2022.clip(dixieFireArea), lstVis, 'Summer 2022 LST (°C)', false);
Map.addLayer(ndviDifference.clip(dixieFireArea), ndviDiffVis, 'NDVI Change, Summer 2022 - 2020', false);
Map.addLayer(tempDifference.clip(dixieFireArea), tempDiffVis, 'LST Change, Summer 2022 - 2020 (°C)');

// --- FIRE BOUNDARY AND CONTROL RING ---
Map.addLayer(ee.Image().byte().paint(dixieFireAsset, 1, 2), {palette: ['red']}, 'Dixie Fire Boundary');
Map.addLayer(ee.Image().byte().paint(ee.FeatureCollection([ee.Feature(controlRing)]), 1, 1),
             {palette: ['white']}, 'Unburned control ring (5 km)', false);

// --- LEGEND HELPER ---
function makeRow(color, name) {
  return ui.Panel({
    widgets: [
      ui.Label('', {backgroundColor: color, padding: '8px', margin: '0 0 4px 0'}),
      ui.Label(name, {margin: '0 0 4px 6px'})
    ],
    layout: ui.Panel.Layout.Flow('horizontal')
  });
}

// --- LST LEGEND ---
var legend = ui.Panel({style: {position: 'bottom-left', padding: '8px 15px'}});
legend.add(ui.Label('Land Surface Temp (°C)', {fontWeight: 'bold', fontSize: '18px'}));
var temps = ['0', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50+'];
var legendIdx = [0, 1, 2, 3, 4, 5, 6, 7, 9, 12, 15];
for (var i = 0; i < temps.length; i++) {
  legend.add(makeRow(lstPalette[legendIdx[i]], temps[i]));
}
Map.add(legend);

// --- TEMP CHANGE LEGEND ---
var diffLegend = ui.Panel({style: {position: 'bottom-right', padding: '8px 15px'}});
diffLegend.add(ui.Label('LST Change 2022 - 2020 (°C)', {fontWeight: 'bold', fontSize: '18px'}));
var diffValues = ['-5 or less', '0', '+5', '+12', '+20 or more'];
for (var j = 0; j < 5; j++) {
  diffLegend.add(makeRow(diffColors[j], diffValues[j]));
}
Map.add(diffLegend);

// --- INFO PANEL ---
var infoPanel = ui.Panel({
  widgets: [
    ui.Label('Landsat 8 Collection 2 L2 (cloud-masked)'),
    ui.Label('Dixie Fire (Plumas County, CA)'),
    ui.Label('Start: July 13, 2021'),
    ui.Label('Contained: Oct 25, 2021'),
    ui.Label('Impact: summer 2022 vs summer 2020'),
    ui.Label('Control: 5 km unburned ring'),
    ui.Label('LST: Band 10 (ST_B10) · NDVI: B5 - B4')
  ],
  style: {position: 'top-left', padding: '8px', backgroundColor: 'rgba(255, 255, 255, 0.8)'}
});
Map.add(infoPanel);

// --- SUMMARY STATISTICS: BURN SCAR vs CONTROL RING ---
function meanIn(image, band, region) {
  return image.reduceRegion({
    reducer: ee.Reducer.mean(), geometry: region, scale: 500, maxPixels: 1e10, bestEffort: true
  }).get(band);
}
var stats = ee.Dictionary({
  'Burn scar LST, summer 2020 (°C)': meanIn(lst2020, 'LST', dixieFireArea),
  'Burn scar LST, summer 2022 (°C)': meanIn(lst2022, 'LST', dixieFireArea),
  'Control ring LST, summer 2020 (°C)': meanIn(lst2020, 'LST', controlRing),
  'Control ring LST, summer 2022 (°C)': meanIn(lst2022, 'LST', controlRing),
  'Burn scar NDVI, summer 2020': meanIn(ndvi2020, 'NDVI', dixieFireArea),
  'Burn scar NDVI, summer 2022': meanIn(ndvi2022, 'NDVI', dixieFireArea),
  'Control ring NDVI, summer 2020': meanIn(ndvi2020, 'NDVI', controlRing),
  'Control ring NDVI, summer 2022': meanIn(ndvi2022, 'NDVI', controlRing)
});
print('Burn scar vs unburned control ring', stats);

// --- TIME SERIES CHARTS (June 2020 - September 2022, cloud-masked) ---
var longSeries = landsat('2020-06-01', '2022-09-30');
var regions = ee.FeatureCollection([
  ee.Feature(dixieFireArea, {label: 'Burn scar'}),
  ee.Feature(controlRing, {label: 'Unburned ring'})
]);

var tempChart = ui.Chart.image.seriesByRegion({
  imageCollection: longSeries.select('LST'),
  regions: regions,
  reducer: ee.Reducer.mean(),
  band: 'LST',
  scale: 1000,
  seriesProperty: 'label'
}).setOptions({
  title: 'Land Surface Temperature: burn scar vs unburned ring',
  vAxis: {title: 'Temp (°C)'},
  hAxis: {title: 'Date', format: 'MM-yyyy'},
  lineWidth: 1,
  pointSize: 3,
  colors: ['#d7191c', '#2c7bb6']
});
print(tempChart);

var ndviChart = ui.Chart.image.seriesByRegion({
  imageCollection: longSeries.select('NDVI'),
  regions: regions,
  reducer: ee.Reducer.mean(),
  band: 'NDVI',
  scale: 1000,
  seriesProperty: 'label'
}).setOptions({
  title: 'NDVI: burn scar vs unburned ring',
  vAxis: {title: 'NDVI'},
  hAxis: {title: 'Date', format: 'MM-yyyy'},
  lineWidth: 1,
  pointSize: 3,
  colors: ['#d7191c', '#1a9850']
});
print(ndviChart);

// --- EXPORTS ---
function exportImage(image, name) {
  Export.image.toDrive({
    image: image.clip(dixieFireArea),
    description: name,
    scale: 30,
    region: dixieFireArea,
    maxPixels: 1e10
  });
}
exportImage(preFireLST, 'DixieFire_PreFire_LST_2021');
exportImage(duringFireLST, 'DixieFire_DuringFire_LST_2021');
exportImage(postFireLST, 'DixieFire_PostFire_LST_2021');
exportImage(tempDifference, 'DixieFire_LST_Change_Summer2022_vs_2020');
exportImage(ndviDifference, 'DixieFire_NDVI_Change_Summer2022_vs_2020');
