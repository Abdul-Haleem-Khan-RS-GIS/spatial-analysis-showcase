// 3D project globe: MapLibre GL (globe projection) + Sentinel-2 cloudless imagery + terrain.
(function () {
  var box = document.getElementById('globe');
  if (!box) return;
  var data = JSON.parse(document.getElementById('globe-data').textContent);

  function hasWebGL() {
    try { var c = document.createElement('canvas'); return !!(window.WebGLRenderingContext && (c.getContext('webgl2') || c.getContext('webgl'))); }
    catch (e) { return false; }
  }
  function fallback() { box.classList.add('globe-off'); }
  if (!hasWebGL()) return fallback();

  var started = false;
  function load() {
    if (started) return; started = true;
    var css = document.createElement('link'); css.rel = 'stylesheet';
    css.href = 'https://unpkg.com/maplibre-gl@5.6.0/dist/maplibre-gl.css'; document.head.appendChild(css);
    var s = document.createElement('script'); s.src = 'https://unpkg.com/maplibre-gl@5.6.0/dist/maplibre-gl.js';
    s.onload = init; s.onerror = fallback; document.head.appendChild(s);
  }
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) { if (es.some(function (e) { return e.isIntersecting; })) { io.disconnect(); load(); } }, { rootMargin: '300px' });
    io.observe(box);
  } else load();

  function esc(t) { return String(t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  function init() {
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var map = new maplibregl.Map({
      container: 'globe-map',
      style: {
        version: 8,
        projection: { type: 'globe' },
        sources: {
          s2: { type: 'raster', tileSize: 256, maxzoom: 15,
                tiles: ['https://tiles.maps.eox.at/wmts/1.0.0/s2cloudless_3857/default/g/{z}/{y}/{x}.jpg'],
                attribution: '<a href="https://s2maps.eu">Sentinel-2 cloudless 2016</a> by EOX IT Services GmbH (contains modified Copernicus Sentinel data 2016)' },
          dem: { type: 'raster-dem', encoding: 'terrarium', tileSize: 256, maxzoom: 14,
                 tiles: ['https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png'],
                 attribution: 'Terrain: Mapzen / AWS Terrain Tiles' },
          pins: { type: 'geojson', data: data.pins }
        },
        sky: { 'atmosphere-blend': ['interpolate', ['linear'], ['zoom'], 0, 1, 5, 1, 7, 0] },
        layers: [
          { id: 's2', type: 'raster', source: 's2' },
          { id: 'hill', type: 'hillshade', source: 'dem', paint: { 'hillshade-exaggeration': 0.25, 'hillshade-shadow-color': '#0b1a1c' } },
          { id: 'pin-halo', type: 'circle', source: 'pins', paint: { 'circle-radius': ['+', 9, ['*', 2, ['get', 'n']]], 'circle-color': '#f5b700', 'circle-opacity': 0.25 } },
          { id: 'pin', type: 'circle', source: 'pins', paint: { 'circle-radius': ['+', 5, ['get', 'n']], 'circle-color': '#f5b700', 'circle-stroke-color': '#16181a', 'circle-stroke-width': 1.5 } }
        ]
      },
      center: [45, 25], zoom: 1.6, attributionControl: { compact: true }, maxPitch: 80
    });
    map.addControl(new maplibregl.NavigationControl({ visualizePitch: true }), 'top-right');
    map.scrollZoom.disable();
    box.addEventListener('click', function () { map.scrollZoom.enable(); }, { once: true });

    map.on('load', function () {
      var a = box.querySelector('.maplibregl-ctrl-attrib'); if (a) a.classList.remove('maplibregl-compact-show');
      map.setTerrain({ source: 'dem', exaggeration: 1.4 });
      box.classList.add('globe-ready');
    });

    // gentle spin until the visitor interacts
    var spinning = !reduce;
    function spin() {
      if (!spinning || map.getZoom() > 3) return;
      var c = map.getCenter(); c.lng -= 6;
      map.easeTo({ center: c, duration: 1000, easing: function (t) { return t; } });
    }
    ['mousedown', 'touchstart', 'wheel'].forEach(function (ev) { map.on(ev, function () { spinning = false; }); });
    map.on('moveend', spin); map.on('load', spin);

    map.on('mouseenter', 'pin', function () { map.getCanvas().style.cursor = 'pointer'; });
    map.on('mouseleave', 'pin', function () { map.getCanvas().style.cursor = ''; });
    map.on('click', 'pin', function (e) {
      spinning = false;
      var p = e.features[0].properties, items = JSON.parse(p.items);
      var html = '<div class="gpop"><span class="mono">' + esc(p.place) + '</span><ul>' + items.map(function (i) {
        return '<li>' + (i.url ? '<a href="' + esc(i.url) + '">' + esc(i.t) + '</a>' : esc(i.t)) + '</li>';
      }).join('') + '</ul></div>';
      new maplibregl.Popup({ maxWidth: '300px' }).setLngLat(e.features[0].geometry.coordinates).setHTML(html).addTo(map);
    });

    document.querySelectorAll('[data-tour]').forEach(function (b) {
      b.addEventListener('click', function () {
        spinning = false;
        var t = data.tours[+b.dataset.tour];
        document.querySelectorAll('[data-tour]').forEach(function (x) { x.setAttribute('aria-pressed', x === b); });
        map.flyTo({ center: t.c, zoom: t.z, pitch: t.p, bearing: t.b, duration: reduce ? 0 : 6000, essential: true });
        var link = document.getElementById('globe-link');
        link.href = t.url; link.textContent = 'Open the case study: ' + t.title + ' →'; link.hidden = !t.url;
      });
    });
    var home = document.getElementById('globe-home');
    if (home) home.addEventListener('click', function () {
      document.querySelectorAll('[data-tour]').forEach(function (x) { x.setAttribute('aria-pressed', false); });
      document.getElementById('globe-link').hidden = true;
      map.flyTo({ center: [45, 25], zoom: 1.6, pitch: 0, bearing: 0, duration: reduce ? 0 : 3000 });
    });
  }
})();
