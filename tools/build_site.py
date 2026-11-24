import os, sys, json, html, shutil, urllib.parse
from PIL import Image

BUILD = os.path.dirname(os.path.abspath(__file__))
SHOW = sys.argv[1]          # built showcase repo
SITE = sys.argv[2]          # site repo checkout
P = json.load(open(os.path.join(BUILD, "projects_built.json")))
sys.path.insert(0, BUILD)
from projects import CATS

GH = "https://github.com/Abdul-Haleem-Khan-RS-GIS/spatial-analysis-showcase/tree/main/"
E = html.escape
EMAIL = "abdulhaleemk03@gmail.com"
UPWORK = "https://www.upwork.com/freelancers/abdulhaleemrsgis"
LINKEDIN = "https://www.linkedin.com/in/abdul-haleem-khan-rs-gis-specialist"
GITHUB = "https://github.com/Abdul-Haleem-Khan-RS-GIS"
URL = "https://abdul-haleem-khan-rs-gis.github.io/Geospatial_Portfolio/"

# ---------- images ----------
for d in ["projects", "assets/maps"]:
    shutil.rmtree(os.path.join(SITE, d), ignore_errors=True)
    os.makedirs(os.path.join(SITE, d))

for p in P:
    p["img"] = []
    for i, m in enumerate(p["maps"], 1):
        im = Image.open(os.path.join(SHOW, m)).convert("RGB")
        big = im.copy(); big.thumbnail((2000, 2000))
        b = f"assets/maps/{p['slug']}-{i}.jpg"
        big.save(os.path.join(SITE, b), quality=84, optimize=True, progressive=True)
        th = im.copy(); th.thumbnail((900, 900))
        t = f"assets/maps/{p['slug']}-{i}-thumb.jpg"
        th.save(os.path.join(SITE, t), quality=80, optimize=True, progressive=True)
        p["img"].append((b, t, big.size))

pro = [p for p in P if p.get("pro")]
shown = [p for p in P if p["img"] and not p.get("pro")]
more = [p for p in P if not p["img"] and not p.get("pro")]

CSS = r"""
:root{--paper:#f6f5f1;--card:#fff;--ink:#16181a;--muted:#5c6066;--line:#dedbd3;--accent:#0f5257;--accent2:#c8642b;
--serif:'Fraunces',Georgia,serif;--sans:'Inter',system-ui,sans-serif;--mono:'JetBrains Mono',ui-monospace,monospace}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.6 var(--sans);-webkit-font-smoothing:antialiased}
a{color:inherit}img{max-width:100%;display:block}
.wrap{max-width:1200px;margin:0 auto;padding:0 24px}
.mono{font-family:var(--mono);font-size:12px;letter-spacing:.04em;text-transform:uppercase;color:var(--muted)}
header.nav{position:sticky;top:0;z-index:20;background:rgba(246,245,241,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
header.nav .wrap{display:flex;align-items:center;justify-content:space-between;height:64px}
.logo{font-family:var(--serif);font-weight:600;font-size:20px;text-decoration:none}
.logo span{color:var(--accent)}
nav a{text-decoration:none;font-size:14px;margin-left:24px;color:var(--muted)}nav a:hover{color:var(--ink)}
nav a.btn{color:#fff}
.btn{display:inline-block;padding:11px 20px;border-radius:4px;background:var(--ink);color:#fff;text-decoration:none;font-size:14px;font-weight:500;border:1px solid var(--ink)}
.btn.ghost{background:transparent;color:var(--ink)}.btn:hover{background:var(--accent);border-color:var(--accent);color:#fff}
.hero{padding:72px 0 56px;border-bottom:1px solid var(--line);background-image:linear-gradient(rgba(22,24,26,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(22,24,26,.05) 1px,transparent 1px);background-size:64px 64px;background-position:-1px -1px}
.hero .grid{display:grid;grid-template-columns:1.05fr 1fr;gap:56px;align-items:center}
h1{font-family:var(--serif);font-weight:600;font-size:clamp(40px,5.4vw,64px);line-height:1.02;margin:12px 0 16px;letter-spacing:-.02em}
.lead{font-size:18px;color:var(--muted);max-width:34em;margin:0 0 28px}
.ctas{display:flex;gap:12px;flex-wrap:wrap}
.stats{display:flex;gap:36px;margin-top:40px;padding-top:24px;border-top:1px solid var(--line)}
.stats b{display:block;font-family:var(--serif);font-size:30px;font-weight:600;line-height:1.1}
.stats span{font-size:13px;color:var(--muted)}
.sheet{background:#fff;border:1px solid var(--ink);padding:14px;box-shadow:10px 10px 0 var(--ink)}
.sheet img{width:100%;aspect-ratio:4/3;object-fit:cover;object-position:center}
.sheet.portrait{max-width:380px;margin-left:auto}.sheet.portrait img{aspect-ratio:400/512;object-position:top}
.sheet figcaption{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-top:10px}
section{padding:80px 0;border-bottom:1px solid var(--line)}
h2{font-family:var(--serif);font-weight:600;font-size:38px;margin:6px 0 12px;letter-spacing:-.01em}
.sub{color:var(--muted);max-width:42em;margin:0 0 32px}
.filters{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:32px}
.filters button{font:500 13px var(--sans);padding:8px 14px;border:1px solid var(--line);background:#fff;border-radius:999px;cursor:pointer;color:var(--muted)}
.filters button[aria-pressed=true]{background:var(--ink);border-color:var(--ink);color:#fff}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.card{background:var(--card);border:1px solid var(--line);display:flex;flex-direction:column;text-decoration:none;transition:border-color .2s,transform .2s}
.card:hover{border-color:var(--ink);transform:translateY(-3px)}
.card .ph{aspect-ratio:4/3;overflow:hidden;background:#eceae4;border-bottom:1px solid var(--line)}
.card .ph img{width:100%;height:100%;object-fit:cover}.card.text{background:#fff;border-top:4px solid var(--accent)}
.card .bd{padding:18px 18px 20px;display:flex;flex-direction:column;gap:8px;flex:1}
.card h3{font-family:var(--serif);font-weight:600;font-size:20px;line-height:1.2;margin:0}
.card p{margin:0;font-size:14px;color:var(--muted)}
.tags{display:flex;flex-wrap:wrap;gap:6px;margin-top:auto;padding-top:8px}
.tags span{font:11px var(--mono);border:1px solid var(--line);padding:3px 7px;border-radius:3px;color:var(--muted)}
.morelist{margin-top:56px;overflow-x:auto}
.morelist table{width:100%;border-collapse:collapse;background:#fff;border:1px solid var(--line);font-size:14px}
.morelist th,.morelist td{text-align:left;padding:10px 14px;border-bottom:1px solid var(--line)}
.morelist th{font:500 11px var(--mono);text-transform:uppercase;letter-spacing:.05em;color:var(--muted)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:48px}
.tl{list-style:none;margin:0;padding:0;border-left:2px solid var(--ink)}
.tl li{position:relative;padding:0 0 28px 24px}
.tl li:before{content:"";position:absolute;left:-7px;top:6px;width:12px;height:12px;background:var(--paper);border:2px solid var(--ink);border-radius:50%}
.tl h3{margin:0;font-size:18px;font-family:var(--serif);font-weight:600}
.tl .org{font-weight:500}.tl p{margin:6px 0 0;color:var(--muted);font-size:15px}
.skills{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.skills div{background:#fff;border:1px solid var(--line);padding:20px}
.skills h3{margin:0 0 10px;font-family:var(--serif);font-weight:600;font-size:18px}
.skills p{margin:0;color:var(--muted);font-size:15px}
.reviews{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:40px}
.esri{margin-top:8px;font-size:14px}.esri summary{cursor:pointer;color:var(--ink,#1a1a1a)}.esri .esri-list{list-style:none;margin:8px 0 4px 16px;padding:0}.tl .esri .esri-list li{position:relative;padding:3px 0 3px 16px;color:var(--muted);line-height:1.45;border:0;margin:0}.tl .esri .esri-list li::before{content:'·';position:absolute;left:2px;top:1px;width:auto;height:auto;border:0;border-radius:0;background:none;font-weight:700;color:var(--ink,#1a1a1a)}.esri .esri-list li::after{display:none}
blockquote{margin:0;background:#fff;border:1px solid var(--line);padding:20px;font-family:var(--serif);font-size:18px;line-height:1.4}
blockquote cite{display:block;margin-top:12px;font:13px var(--sans);color:var(--muted);font-style:normal}
.contact{display:grid;grid-template-columns:1fr 1.2fr;gap:48px}
.contact dl{margin:0}.contact dt{font:500 11px var(--mono);text-transform:uppercase;color:var(--muted);margin-top:18px}
.contact dd{margin:2px 0 0;font-size:17px}.contact dd a{text-decoration:none;border-bottom:1px solid var(--line)}
form label{display:block;font-size:13px;font-weight:500;margin:14px 0 6px}
form input,form textarea{width:100%;padding:12px;border:1px solid var(--ink);background:#fff;font:15px var(--sans);border-radius:3px}
footer{padding:40px 0;color:var(--muted);font-size:14px}
footer .wrap{display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px}
/* project page */
.crumb{padding:28px 0 0;font-size:14px}.crumb a{color:var(--muted);text-decoration:none}
.phero{padding:20px 0 40px}
.facts{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border:1px solid var(--line);background:#fff;margin:24px 0 32px}
.facts div{padding:14px 16px;border-right:1px solid var(--line)}.facts div:last-child{border-right:0}
.facts dd{margin:4px 0 0;font-size:15px}
.mapfull{background:#fff;border:1px solid var(--line);padding:12px;margin-bottom:20px}
.mapfull a{cursor:zoom-in}.mapfull img{max-height:82vh;width:auto;margin:0 auto}
.pbody{display:grid;grid-template-columns:1.6fr 1fr;gap:48px;padding:24px 0 72px}
.pbody h2{font-size:26px;margin-top:0}.pbody ol{padding-left:20px;color:var(--muted)}
.side{background:#fff;border:1px solid var(--line);padding:20px;align-self:start}
.mapfull figcaption{font-size:14px;color:var(--muted);padding-top:10px;text-align:center}.mapfull figcaption .mono{margin-right:6px}
.find{padding-left:0;list-style:none}.find li{border-left:3px solid var(--accent);padding:6px 0 6px 14px;margin:0 0 10px;background:#fff}
.side hr{border:0;border-top:1px solid var(--line);margin:18px 0}.side .dl{margin-bottom:0}.side .muted{color:var(--muted)}
.globe-sec{background:#0e1517;color:#e9ecea;padding:88px 0}.globe-sec h2{color:#fff}.globe-sec .lead{color:#b9c2c0}.globe-sec .mono{color:#9fb3b0}
.tours{display:flex;flex-wrap:wrap;gap:8px;margin:22px 0 18px}.tours button{font:500 14px Inter,sans-serif;background:transparent;color:#e9ecea;border:1px solid #3b4a4c;padding:9px 14px;cursor:pointer}
.tours button:hover,.tours button[aria-pressed=true]{background:#f5b700;color:#16181a;border-color:#f5b700}
.globe{position:relative;height:min(72vh,640px);border:1px solid #2a3739;background:radial-gradient(circle at 50% 45%,#16302f,#0b1112 70%)}#globe-map{position:absolute;inset:0}
.globe-msg{display:none;position:absolute;inset:0;margin:0;align-items:center;justify-content:center;text-align:center;padding:24px}.globe-off .globe-msg{display:flex}.globe-msg a{color:#f5b700}
.globe-foot{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-top:12px}.globe-foot a{color:#f5b700}
.gpop{font:14px/1.45 Inter,sans-serif;color:#16181a}.gpop .mono{color:#5b6668;font-size:11px}.gpop ul{margin:6px 0 0;padding-left:16px}.gpop a{color:#0f5257}
.maplibregl-popup-content{border-radius:0;padding:12px 14px}
.form-status{margin:14px 0 0;padding:12px 14px;font-size:15px;line-height:1.5;border-left:3px solid var(--accent);background:#fff}.form-status.ok{border-color:#1a9641}.form-status.warn{border-color:#e08a00}.form-status a{color:var(--accent)}.form-status a.btn{color:#fff;text-decoration:none}
.side ul{padding-left:18px;margin:8px 0 0;font-size:14px;color:var(--muted)}
.next{display:flex;justify-content:space-between;border-top:1px solid var(--line);padding:24px 0 64px}
.next a{text-decoration:none}
@media(max-width:900px){.hero .grid,.two,.contact,.pbody{grid-template-columns:1fr}.cards,.skills,.reviews{grid-template-columns:1fr 1fr}.facts{grid-template-columns:1fr 1fr}nav a:not(.btn){display:none}}
@media(max-width:600px){.morelist th:nth-child(2),.morelist td:nth-child(2),.morelist th:nth-child(3),.morelist td:nth-child(3){display:none}.ctas .btn{flex:1;text-align:center}.facts{grid-template-columns:1fr}.facts div{border-right:0;border-bottom:1px solid var(--line)}.cards,.skills,.reviews{grid-template-columns:1fr}.stats{gap:20px}h2{font-size:30px}}
"""

def head(title, desc, ogimg, depth=""):
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:image" content="{URL}{ogimg}"><meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{depth}assets/site.css?v=3"></head><body>
<header class="nav"><div class="wrap"><a class="logo" href="{depth}index.html">Abdul Haleem <span>Khan</span></a>
<nav><a href="{depth}index.html#map">Map</a><a href="{depth}index.html#planning">Master plans</a><a href="{depth}index.html#work">Work</a><a href="{depth}index.html#experience">Experience</a><a href="{depth}index.html#education">Education</a><a href="{depth}index.html#skills">Skills</a><a href="{depth}index.html#testimonials">Testimonials</a><a class="btn" href="{depth}index.html#contact">Contact</a></nav></div></header>"""

FOOT = f"""<footer><div class="wrap"><span>© 2026 Abdul Haleem Khan · GIS Engineer & Remote Sensing Specialist</span>
<span><a href="{LINKEDIN}">LinkedIn</a> · <a href="{GITHUB}">GitHub</a> · <a href="{UPWORK}">Upwork</a> · <a href="mailto:{EMAIL}">Email</a></span></div></footer>"""

def card(p, depth=""):
    b, t, _ = p["img"][0]
    return f"""<a class="card" href="{depth}projects/{p['slug']}.html" data-cat="{p['cat']}">
<div class="ph"><img src="{depth}{t}" alt="{E(p['title'])} map" loading="lazy"></div>
<div class="bd"><span class="mono">{E(CATS[p['cat']][1])} · {E(p['year'])}</span><h3>{E(p['title'])}</h3><p>{E(p['where'])}</p>
<div class="tags">{''.join(f'<span>{E(x)}</span>' for x in p['tools'][:3])}</div></div></a>"""

def procard(p):
    if p["img"]:
        return card(p)
    return f"""<a class="card text" href="projects/{p['slug']}.html"><div class="bd"><span class="mono">{E(p['year'])}</span><h3>{E(p['title'])}</h3><p>{E(p['client'])}</p><p style="color:var(--ink)">{E(p['summary'])}</p>
<div class="tags">{''.join(f'<span>{E(x)}</span>' for x in p['tools'][:3])}</div></div></a>"""

# order: featured first
shown.sort(key=lambda p: (not p.get("featured"), list(CATS).index(p["cat"])))
hero = next(p for p in shown if p["slug"] == "burn-severity-sentinel2")
cats_present = [k for k in CATS if any(p["cat"] == k for p in shown)]

filters = '<button aria-pressed="true" data-f="all">All</button>' + "".join(
    f'<button aria-pressed="false" data-f="{k}">{E(CATS[k][1])}</button>' for k in cats_present)

more_rows = "".join(f"<tr><td><a href=\"{('projects/'+p['slug']+'.html') if p.get('challenge') else GH+p['dir']}\">{E(p['title'])}</a></td><td>{E(CATS[p['cat']][1])}</td><td>{E(p['where'])}</td><td>{E(p['year'])}</td></tr>" for p in more)

REVIEWS = [
 ("Abdul delivered exactly what we needed with a complex GIS to CAD conversion.", "MBH Inc., USA · Contours to CAD"),
 ("He did very well Job delivered his project on time.", "Engineering client · Solar plant GIS dataset ($1,000)"),
 ("Thanks for fast assistance on an urgent task related to Polygon and Point Digitization!", "Valorian · QGIS digitisation"),
]

from locations import LOC, TOURS
_pageset = {p["slug"] for p in pro + shown} | {p["slug"] for p in more if p.get("challenge")}
_title = {p["slug"]: p["title"] for p in P}
_groups = {}
for slug,(lat,lon,place) in LOC.items():
    if slug not in _title: continue
    g = _groups.setdefault((lat,lon), {"place": place, "items": []})
    g["items"].append({"t": _title[slug], "url": ("projects/"+slug+".html") if slug in _pageset else ""})
_feats = [{"type":"Feature","geometry":{"type":"Point","coordinates":[lon,lat]},
           "properties":{"place":g["place"],"n":min(len(g["items"]),4),"items":json.dumps(g["items"])}} for (lat,lon),g in _groups.items()]
_tours = [{"title":t,"c":list(c),"z":z,"p":pt,"b":b,"url":("projects/"+sl+".html") if sl in _pageset else ""} for (t,c,z,pt,b,sl) in TOURS]
GLOBE_DATA = json.dumps({"pins":{"type":"FeatureCollection","features":_feats},"tours":_tours}).replace("</","<\\/")
N_PLACES = len(_groups); N_COUNTRIES = len({g["place"].split(",")[-1].strip() for g in _groups.values()})
TOUR_BTNS = "".join(f'<button type="button" data-tour="{k}" aria-pressed="false">{E(t[0])}</button>' for k,t in enumerate(TOURS))

index = head("Abdul Haleem Khan | GIS Engineer & Remote Sensing Specialist",
             "GIS Engineer and Remote Sensing Specialist: satellite image analysis, cartography, site suitability and GIS data engineering. Portfolio of real client maps.",
             hero["img"][0][0]) + f"""
<main>
<section class="hero"><div class="wrap grid">
<div><span class="mono">GIS Engineer · Remote Sensing Specialist · Lahore, Pakistan</span>
<h1>Abdul Haleem Khan</h1>
<p class="lead">I turn satellite imagery and spatial data into maps and analysis people can act on, from municipal GIS in Saudi Arabia and city master plans in Pakistan to freelance projects for clients in the USA, Europe and the Gulf.</p>
<div class="ctas"><a class="btn" href="#work">View work</a><a class="btn ghost" href="#contact">Get in touch</a><a class="btn ghost" href="{UPWORK}">Hire on Upwork</a></div>
<div class="stats"><div><b>4+ yrs</b><span>Professional GIS</span></div><div><b>33</b><span>Upwork jobs</span></div><div><b>4.8★</b><span>14 client reviews</span></div></div>
</div>
<figure class="sheet portrait"><img src="assets/portrait.jpg" alt="Abdul Haleem Khan, GIS Engineer and Remote Sensing Specialist" width="400" height="512"><figcaption><span class="mono">Abdul Haleem Khan</span><span class="mono">GIS Engineer · RS Specialist</span></figcaption></figure>
</div></section>

<section id="map" class="globe-sec"><div class="wrap">
<span class="mono">Interactive · 3D</span><h2>Where I've mapped</h2>
<p class="lead" style="max-width:760px">{N_PLACES} project locations in {N_COUNTRIES} countries on a 3D globe built with MapLibre GL, Sentinel-2 cloud-free imagery and real terrain elevation. Click a pin to open its case study, or fly into one of the landscapes below in 3D.</p>
<div class="tours">{TOUR_BTNS}<button type="button" id="globe-home">↺ Whole globe</button></div>
<div id="globe" class="globe"><div id="globe-map"></div><p class="globe-msg">The 3D globe needs WebGL. <a href="#work">Browse the projects instead →</a></p></div>
<p class="globe-foot"><a id="globe-link" class="mono" hidden href="#"></a><span class="mono">Drag to rotate · right-drag or Ctrl+drag to tilt · click the map, then scroll to zoom</span></p>
</div></section>
<script type="application/json" id="globe-data">{GLOBE_DATA}</script>
<section id="planning"><div class="wrap">
<span class="mono">Professional work</span><h2>Master plans & municipal GIS</h2>
<p class="sub">City comprehensive plans for the Government of Punjab (PICIIP) and the Aga Khan Agency for Habitat at Shehersaaz, master-plan and cadastral work across Punjab and KP, and two years running municipal GIS in Saudi Arabia.</p>
<div class="cards">{''.join(procard(p) for p in pro)}</div>
</div></section>

<section id="work"><div class="wrap">
<span class="mono">Freelance & client work</span><h2>Real maps from real projects</h2>
<p class="sub">These are maps I delivered to clients or produced in my professional work, plus a few practice studies (marked as such). Each case study links to its folder on GitHub with the maps, write-up and data.</p>
<div class="filters" role="group" aria-label="Filter projects">{filters}</div>
<div class="cards" id="cards">{''.join(card(p) for p in shown)}</div>
{"<div class='morelist'><span class='mono'>More projects on GitHub</span><h2 style='font-size:26px'>Other delivered work</h2><table><thead><tr><th>Project</th><th>Category</th><th>Where</th><th>Year</th></tr></thead><tbody>"+more_rows+"</tbody></table></div>" if more else ""}
<p style="margin-top:32px"><a class="btn ghost" href="{GITHUB}/spatial-analysis-showcase">All projects on GitHub →</a></p>
</div></section>

<section id="experience"><div class="wrap two">
<div><span class="mono">Experience</span><h2>Where I've worked</h2>
<ul class="tl">
<li><span class="mono">Jun 2024 – Jun 2026 · Saudi Arabia</span><h3>GIS Engineer</h3><div class="org">Municipality of Uyun Al Jawa, Al-Qassim</div><p>Managed municipal spatial databases and urban-planning and infrastructure datasets, produced planning maps, coordinated GPS field data collection, and delivered GIS training to Uyun Al Jawa staff.</p></li>
<li><span class="mono">Apr – May 2024 · Lahore</span><h3>Junior GIS Expert</h3><div class="org">NESPAK</div><p>Collected, managed and processed imagery, survey and vector data for engineering and infrastructure projects.</p></li>
<li><span class="mono">May 2022 – Mar 2024 · Lahore</span><h3>GIS Analyst</h3><div class="org">Shehersaaz Urban Planning Consultancy</div><p>Spatial analysis and mapping for Land Use Focused City Comprehensive Plans (Sahiwal, Sialkot) and terrain studies for the Aga Khan Agency for Habitat.</p></li>
<li><span class="mono">2023 – present · Remote</span><h3>Freelance GIS & Remote Sensing</h3><div class="org">Upwork</div><p>33 jobs for clients in the USA, Saudi Arabia, Switzerland and elsewhere: remote sensing, cartography, suitability analysis and GIS-to-CAD data work.</p></li>
</ul></div>
<div id="education" style="scroll-margin-top:100px"><span class="mono">Education</span><h2>Degree and certifications</h2>
<ul class="tl">
<li><span class="mono">Master's</span><h3>Geographical Information System</h3><div class="org">University of the Punjab</div><p>Thesis: urban sprawl trend in Mardan City, Pakistan (image classification in ERDAS Imagine and ArcMap).</p></li>
</ul>
<span class="mono">Certifications</span>
<ul class="tl" style="margin-top:12px"><li><h3 style="font-size:16px">Teaming@BCG Job Simulation</h3><p>BCG via Forage · Apr 2026 · Effective teaming as a project leader, managing an unanticipated request</p></li>
<li><h3 style="font-size:16px">Data Analytics Job Simulation</h3><p>Deloitte via Forage · Feb 2026 · Data analysis, forensic technology</p></li>
<li><h3 style="font-size:16px">Esri Training: 24 web courses in 3 learning series</h3><p>Esri · 2024–2025 · ArcGIS Pro</p><details class="esri"><summary><b>Spatial Analysis</b> · 10 courses · Jul–Dec 2024</summary><ul class="esri-list"><li>Getting Started with Spatial Analysis</li><li>Getting Started with Geoprocessing</li><li>Building Geoprocessing Models Using ArcGIS Pro</li><li>Summarizing Data by Spatial Relationships</li><li>Calculating Density Using ArcGIS</li><li>Distance Analysis: Creating Cost Surfaces</li><li>Distance Analysis: Using Distance Accumulation and Distance Allocation</li><li>Distance Analysis: Creating Optimal Region Connections</li><li>Performing Line of Sight Analysis</li><li>Terrain Analysis Using ArcGIS Pro</li></ul></details><details class="esri"><summary><b>Advanced Spatial Analysis</b> · 8 courses · Jan 2025</summary><ul class="esri-list"><li>Mapping Clusters: Introduction to Statistical Cluster Analysis</li><li>Mapping Clusters: Hot Spot and Cluster and Outlier Analysis</li><li>Mapping Clusters: Optimized Hot Spot and Optimized Outlier Analysis</li><li>Introduction to Space-Time Analysis</li><li>Creating a Space-Time Cube</li><li>Space-Time Analysis: Finding Temporal Trends</li><li>Suitability Modeling: Introduction</li><li>Suitability Modeling: Creating a Weighted Suitability Model</li></ul></details><details class="esri"><summary><b>Visualization and Cartography</b> · 6 courses · Feb 2025</summary><ul class="esri-list"><li>Labeling Map Features</li><li>Creating a Map Series in ArcGIS Pro</li><li>Creating a Web Map in ArcGIS Pro</li><li>Creating Vector Tiles in ArcGIS Pro</li><li>Introduction to 3D Visualization</li><li>Creating and Sharing Animation in ArcGIS Pro</li></ul></details></li>
<li><h3 style="font-size:16px">GeoPandas Fundamentals</h3><p>Spatial Lab · Nov 2025</p></li>
<li><h3 style="font-size:16px">Advanced Diploma in Geographic Information Systems</h3><p>Alison · Feb 2025</p></li>
<li><h3 style="font-size:16px">Remote Sensing Technology and Data Processing Applications</h3><p>DQGAST & PIESAT · Feb 2022</p></li></ul>
</div></div></section>

<section id="skills"><div class="wrap"><span class="mono">Skills</span><h2>Tools and methods</h2>
<div class="skills">
<div><h3>GIS software</h3><p>ArcGIS Pro, ArcMap, ArcGIS Online, QGIS, Global Mapper, AutoCAD (GIS–CAD exchange), Google Earth / KMZ</p></div>
<div><h3>Remote sensing</h3><p>Google Earth Engine, ENVI, ERDAS Imagine, SNAP; Sentinel-2, Landsat 8/9; NDVI, NBR/dNBR, supervised and unsupervised classification, change detection</p></div>
<div><h3>Analysis</h3><p>Multi-criteria suitability (MCDA, AHP weighting), flood risk and susceptibility, kernel density, buffers and service areas, network routing, choropleth classification</p></div>
<div><h3>Data engineering</h3><p>Geodatabases, digitising, georeferencing, topology QA, geocoding, GeoJSON / SHP / DWG / KMZ conversion, PostGIS</p></div>
<div><h3>Programming</h3><p>Python (ArcPy, GeoPandas, Rasterio, GDAL), GEE JavaScript, Global Mapper scripting</p></div>
<div><h3>Cartography</h3><p>Print and web map layout, symbology and labelling, terrain and hillshade, thematic and reference maps</p></div>
</div>
<span id="testimonials" class="mono" style="display:block;margin-top:64px;scroll-margin-top:100px">Testimonials</span><h2>What clients say</h2>
<div class="reviews" style="margin-top:24px">{''.join(f'<blockquote>“{E(q)}”<cite>{E(c)}</cite></blockquote>' for q, c in REVIEWS)}</div>
</div></section>

<section id="contact"><div class="wrap contact">
<div><span class="mono">Contact</span><h2>Let's work on your map</h2><p class="sub">Tell me about the area, the data you have and what decision the map should support. I usually reply within a few hours.</p>
<dl><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd><dt>Upwork</dt><dd><a href="{UPWORK}">abdulhaleemrsgis</a></dd><dt>LinkedIn</dt><dd><a href="{LINKEDIN}">abdul-haleem-khan-rs-gis-specialist</a></dd><dt>Based in</dt><dd>Lahore, Pakistan (GMT+5) · working remotely</dd></dl></div>
<form id="contact-form" data-email="{EMAIL}" action="https://formsubmit.co/{EMAIL}" method="POST">
<input type="hidden" name="_subject" value="New portfolio enquiry"><input type="hidden" name="_captcha" value="true"><input type="hidden" name="_template" value="table"><input type="hidden" name="_next" value="{URL}thanks.html"><input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
<label for="n">Name</label><input id="n" name="name" required>
<label for="e">Email</label><input id="e" name="email" type="email" required autocomplete="email">
<label for="s">Project / organisation</label><input id="s" name="project">
<label for="m">Message</label><textarea id="m" name="message" rows="5" required></textarea>
<p style="margin-top:16px"><button class="btn" type="submit">Send message</button></p><p id="form-status" class="form-status" role="status" aria-live="polite" hidden></p></form>
</div></section>
</main>{FOOT}
<script>
const bs=document.querySelectorAll('.filters button'),cs=document.querySelectorAll('#cards .card');
bs.forEach(b=>b.addEventListener('click',()=>{{bs.forEach(x=>x.setAttribute('aria-pressed',x===b));const f=b.dataset.f;cs.forEach(c=>c.style.display=(f==='all'||c.dataset.cat===f)?'':'none')}}));
</script>
<script src="assets/globe.js?v=3" defer></script>
<script src="assets/contact.js?v=3" defer></script>
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"Person","name":"Abdul Haleem Khan","jobTitle":"GIS Engineer & Remote Sensing Specialist","url":URL,"email":"mailto:"+EMAIL,"address":{"@type":"PostalAddress","addressLocality":"Lahore","addressCountry":"PK"},"sameAs":[LINKEDIN,GITHUB,UPWORK]})}</script>
</body></html>"""

open(os.path.join(SITE, "index.html"), "w").write(index)
os.makedirs(os.path.join(SITE, "assets"), exist_ok=True)
open(os.path.join(SITE, "assets/site.css"), "w").write(CSS)
shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), "contact.js"), os.path.join(SITE, "assets/contact.js"))
shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), "globe.js"), os.path.join(SITE, "assets/globe.js"))
shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), "portrait.jpg"), os.path.join(SITE, "assets/portrait.jpg"))

def cap(p, k):
    c = p.get('captions') or []
    return c[k-1] if k-1 < len(c) else p['title']

pages = pro + shown + [p for p in more if p.get('challenge')]
for i, p in enumerate(pages):
    nxt = pages[(i + 1) % len(pages)]
    imgs = "".join(f'<figure class="mapfull"><a href="../{b}"><img src="../{b}" alt="{E(cap(p,k))}" width="{w}" height="{h}"></a><figcaption><span class="mono">Fig. {k}</span> {E(cap(p,k))}</figcaption></figure>'
                   for k, (b, t, (w, h)) in enumerate(p["img"], 1))
    from projects import split_files
    _pub, _unpub = split_files(p, SHOW)
    files = "".join(f"<li>{E(f)}</li>" for f in _pub)
    unfiles = ('<span class="mono" style="display:block;margin-top:16px">Also delivered to the client</span><ul class="dl muted">' + "".join(f"<li>{E(f)}</li>" for f in _unpub) + '</ul>') if _unpub else ""
    og = p["img"][0][0] if p["img"] else hero["img"][0][0]
    pg = head(f"{p['title']} | Abdul Haleem Khan", p["summary"], og, "../") + f"""
<main class="wrap">
<div class="crumb"><a href="../index.html#work">← All work</a></div>
<div class="phero"><span class="mono">{E(CATS[p['cat']][1])}</span><h1 style="font-size:clamp(32px,4.5vw,52px)">{E(p['title'])}</h1>
<p class="lead">{E(p['summary'])}</p>
<dl class="facts"><div><dt class="mono">Location</dt><dd>{E(p['where'])}</dd></div><div><dt class="mono">Year</dt><dd>{E(p['year'])}</dd></div><div><dt class="mono">Client</dt><dd>{E(p['client'])}</dd></div><div><dt class="mono">Tools</dt><dd>{E(', '.join(p['tools']))}</dd></div></dl>
{imgs}{('<p class="mono">'+E(p['note'])+'</p>') if p.get('note') else ''}</div>
<div class="pbody"><div>{('<h2>Challenge</h2><p>'+E(p['challenge'])+'</p>') if p.get('challenge') else ''}
<h2>Approach</h2><ol>{''.join(f'<li>{E(s)}</li>' for s in p['method'])}</ol>
<h2>Results</h2>{('<ul class="find">'+''.join(f'<li>{E(x)}</li>' for x in p['findings'])+'</ul>') if p.get('findings') else '<p>'+E(p['result'])+'</p>'}{'<p class="mono">Practice study: course and client details omitted.</p>' if p.get('study') else ''}</div>
<aside class="side">{''.join(f'<p style="margin:0 0 10px"><a class="btn" href="{E(u)}">{E(a)}</a></p>' for a,u in p.get('links',[]))}{('<hr>' if p.get('links') else '')}{('<span class="mono">Data used</span><ul class="dl">'+''.join(f'<li>{E(x)}</li>' for x in p['data'])+'</ul><hr>') if p.get('data') else ''}<span class="mono">Files & data</span><p style="margin:8px 0 0"><a class="btn" href="{GH}{p['dir']}">Open on GitHub</a></p>{('<ul>'+files+'</ul>') if files else ''}{unfiles}</aside></div>
<div class="next"><a href="../index.html#work">← All work</a><a href="{nxt['slug']}.html">Next: {E(nxt['title'])} →</a></div>
</main>{FOOT}</body></html>"""
    open(os.path.join(SITE, "projects", p["slug"] + ".html"), "w").write(pg)

open(os.path.join(SITE, "thanks.html"), "w").write(head("Message sent | Abdul Haleem Khan", "Thank you for your message.", hero["img"][0][0]) + f"""
<main class="wrap" style="padding:120px 0 140px;max-width:720px"><span class="mono">Message sent</span><h1 style="font-size:clamp(34px,5vw,56px)">Thank you, your message is on its way.</h1>
<p class="lead">I usually reply within a few hours. If it is urgent, email me directly at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<p style="margin-top:28px"><a class="btn" href="index.html#work">Back to my work</a></p></main>{FOOT}</body></html>""")
open(os.path.join(SITE, "README.md"), "w").write(f"""# Geospatial Portfolio: Abdul Haleem Khan

Live site: {URL}

Static portfolio site (HTML/CSS, no build step) deployed with GitHub Pages. Map images live in `assets/maps/`; each case study page links to its folder in [spatial-analysis-showcase]({GITHUB}/spatial-analysis-showcase), which holds the full maps, write-up and data.
""")
print("site:", len(pro), "professional,", len(shown), "case studies,", len(more), "listed")

# ---- redirects for renamed/merged project pages ----
REDIRECTS = {"scanned-contours-to-kmz": "nc-contours-to-cad"}
for old, new in REDIRECTS.items():
    open(os.path.join(SITE, "projects", old + ".html"), "w").write(
        f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Moved</title>'
        f'<meta http-equiv="refresh" content="0; url={new}.html"><link rel="canonical" href="{URL}projects/{new}.html">'
        f'<meta name="robots" content="noindex"></head><body><p>This project has moved: <a href="{new}.html">open it here</a>.</p>'
        f'<script>location.replace("{new}.html")</script></body></html>')
