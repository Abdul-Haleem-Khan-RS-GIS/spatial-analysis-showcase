// Dixie Fire 2021 - Land Surface Temperature and NDVI Analysis
// Google Earth Engine Code Editor script by Abdul Haleem Khan
// Open in the Code Editor: https://code.earthengine.google.com/5fbd35d270e92e2c852970e16b9c2db1
//
// Import used by this script (set in the Code Editor "Imports" panel):
//   var table = ee.FeatureCollection('projects/ee-abdulhaleemk03/assets/DixieFire2021');  // Dixie Fire perimeter

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

// --- MAP SETTINGS ---
Map.centerObject(dixieFireArea, 9);
Map.setOptions('SATELLITE');

// --- TIME PERIODS ---
var startDatePreFire = '2021-06-01';
var fireStartDate = '2021-07-13';
var fireContainmentDate = '2021-10-25';
var endDatePostFire = '2021-11-30';

// --- CLOUD MASKING ---
function maskL8sr(image) {
  var qa = image.select('QA_PIXEL');
  var mask = qa.bitwiseAnd(1 << 3).eq(0) // Cloud shadow
             .and(qa.bitwiseAnd(1 << 4).eq(0)) // Snow
             .and(qa.bitwiseAnd(1 << 5).eq(0)) // Cloud
             .and(qa.bitwiseAnd(1 << 6).eq(0)); // Cirrus
  return image.updateMask(mask);
}


// --- LOAD LANDSAT 8 COLLECTION ---
var landsat8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
  .filterBounds(dixieFireArea)
  .filterDate(startDatePreFire, endDatePostFire);

// --- CALCULATE LST ---
function calculateLST(image) {
  var thermal = image.select('ST_B10');
  var lst = thermal.multiply(0.00341802).add(149.0).subtract(273.15); // Convert to Celsius
  return image.addBands(lst.rename('LST'));
}

// --- CALCULATE NDVI ---
function addNDVI(image) {
  var ndvi = image.normalizedDifference(['SR_B5', 'SR_B4']).rename('NDVI');
  return image.addBands(ndvi);
}

// --- APPLY FUNCTIONS ---
var landsatProcessed = landsat8.map(calculateLST).map(addNDVI);

// --- SPLIT COLLECTIONS ---
var preFire = landsatProcessed.filterDate(startDatePreFire, fireStartDate);
var duringFire = landsatProcessed.filterDate(fireStartDate, fireContainmentDate);
var postFire = landsatProcessed.filterDate(fireContainmentDate, endDatePostFire);

// --- MEDIAN IMAGES ---
var preFireLST = preFire.select('LST').median();
var duringFireLST = duringFire.select('LST').median();
var postFireLST = postFire.select('LST').median();
var postFireNDVI = postFire.select('NDVI').median();

// --- TEMP DIFFERENCE ---
var tempDifference = duringFireLST.subtract(preFireLST).rename('temp_diff');

// --- VISUALIZATION PARAMETERS ---
var lstPalette = ['#000080', '#0000D9', '#4000FF', '#8000FF', '#0080FF', '#00FFFF',
                  '#00FF80', '#80FF00', '#DAFF00', '#FFFF00', '#FFF500', '#FFDA00',
                  '#FFB000', '#FF7400', '#FF0000', '#A90000'];

var lstVis = {
  min: 0,
  max: 45,
  palette: lstPalette
};

var tempDiffVis = {
  min: -10,
  max: 30,
  palette: ['#2c7bb6', '#abd9e9', '#ffffbf', '#fdae61', '#d7191c']
};

var ndviVis = {
  min: -0.2,
  max: 0.8,
  palette: ['#d73027', '#f46d43', '#fdae61', '#fee08b',
            '#d9ef8b', '#a6d96a', '#66bd63', '#1a9850']
};

// --- ADD LAYERS ---
Map.addLayer(preFireLST.clip(dixieFireArea), lstVis, 'Pre-Fire LST (°C)');
Map.addLayer(duringFireLST.clip(dixieFireArea), lstVis, 'During-Fire LST (°C)', false);
Map.addLayer(postFireLST.clip(dixieFireArea), lstVis, 'Post-Fire LST (°C)', false);
Map.addLayer(tempDifference.clip(dixieFireArea), tempDiffVis, 'Temp Difference (°C)');
Map.addLayer(postFireNDVI.clip(dixieFireArea), ndviVis, 'Post-Fire NDVI');

// --- FIRE BOUNDARY ---
Map.addLayer(dixieFireArea, {color: 'red'}, 'Dixie Fire Boundary');

// --- LST LEGEND ---
var legend = ui.Panel({style: {position: 'bottom-left', padding: '8px 15px'}});
legend.add(ui.Label('Land Surface Temp (°C)', {fontWeight: 'bold', fontSize: '18px'}));

function makeRow(color, name) {
  return ui.Panel({
    widgets: [
      ui.Label('', {backgroundColor: color, padding: '8px', margin: '0 0 4px 0'}),
      ui.Label(name, {margin: '0 0 4px 6px'})
    ],
    layout: ui.Panel.Layout.Flow('horizontal')
  });
}

var temps = ['0', '5', '10', '15', '20', '25', '30', '35', '40', '45+'];
for (var i = 0; i < 10; i++) {
  legend.add(makeRow(lstPalette[i], temps[i]));
}
Map.add(legend);

// --- TEMP DIFFERENCE LEGEND ---
var diffLegend = ui.Panel({style: {position: 'bottom-right', padding: '8px 15px'}});
diffLegend.add(ui.Label('Temp Difference (°C)', {fontWeight: 'bold', fontSize: '18px'}));

var diffColors = ['#2c7bb6', '#abd9e9', '#ffffbf', '#fdae61', '#d7191c'];
var diffValues = ['-10 or less', '-5', '0', '15', '30+'];
for (var i = 0; i < 5; i++) {
  diffLegend.add(makeRow(diffColors[i], diffValues[i]));
}
Map.add(diffLegend);

// --- INFO PANEL ---
var infoPanel = ui.Panel({
  widgets: [
    ui.Label('Landsat 8 Collection 2 L2'),
    ui.Label('Dixie Fire (Plumas County, CA)'),
    ui.Label('Start: July 13, 2021'),
    ui.Label('Contained: Oct 25, 2021'),
    ui.Label('Period: June - Nov 2021'),
    ui.Label('LST: Band 10 (ST_B10)'),
    ui.Label('NDVI: B5 - B4')
  ],
  style: {position: 'top-left', padding: '8px', backgroundColor: 'rgba(255, 255, 255, 0.8)'}
});
Map.add(infoPanel);

// --- TIME SERIES CHART ---
var tempChart = ui.Chart.image.series({
  imageCollection: landsatProcessed.select('LST'),
  region: dixieFireArea,
  reducer: ee.Reducer.mean(),
  scale: 1000
}).setOptions({
  title: 'Land Surface Temperature Over Time',
  vAxis: {title: 'Temp (°C)'},
  hAxis: {title: 'Date', format: 'MM-yyyy'},
  lineWidth: 2,
  pointSize: 4
});
print(tempChart);

// --- NDVI TIME SERIES ---
var ndviChart = ui.Chart.image.series({
  imageCollection: landsatProcessed.select('NDVI'),
  region: dixieFireArea,
  reducer: ee.Reducer.mean(),
  scale: 1000
}).setOptions({
  title: 'NDVI Over Time',
  vAxis: {title: 'NDVI'},
  hAxis: {title: 'Date', format: 'MM-yyyy'},
  lineWidth: 2,
  pointSize: 4,
  colors: ['green']
});
print(ndviChart);

// --- EXPORTS ---
Export.image.toDrive({
  image: preFireLST.clip(dixieFireArea),
  description: 'DixieFire_PreFire_LST',
  scale: 30,
  region: dixieFireArea,
  maxPixels: 1e10
});

Export.image.toDrive({
  image: duringFireLST.clip(dixieFireArea),
  description: 'DixieFire_DuringFire_LST',
  scale: 30,
  region: dixieFireArea,
  maxPixels: 1e10
});

Export.image.toDrive({
  image: postFireLST.clip(dixieFireArea),
  description: 'DixieFire_PostFire_LST',
  scale: 30,
  region: dixieFireArea,
  maxPixels: 1e10
});

Export.image.toDrive({
  image: tempDifference.clip(dixieFireArea),
  description: 'DixieFire_TempDifference',
  scale: 30,
  region: dixieFireArea,
  maxPixels: 1e10
});
