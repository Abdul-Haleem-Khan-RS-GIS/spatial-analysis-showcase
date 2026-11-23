import os, sys, shutil, subprocess, urllib.parse
sys.path.insert(0, os.path.dirname(__file__))
from projects import P, CATS

REPO = sys.argv[1]
SITE = "https://abdul-haleem-khan-rs-gis.github.io/Geospatial_Portfolio/"
GH = "https://github.com/Abdul-Haleem-Khan-RS-GIS/spatial-analysis-showcase"
q = lambda s: urllib.parse.quote(s)

def git(*a): subprocess.run(["git", "-C", REPO, *a], check=True)

for p in P:
    catdir, _ = CATS[p["cat"]]
    d = os.path.join(REPO, catdir, p["slug"])
    os.makedirs(os.path.join(d, "maps"), exist_ok=True)
    p["dir"] = f"{catdir}/{p['slug']}"
    p["maps"] = []
    for i, old in enumerate(p.get("old", []), 1):
        ext = os.path.splitext(old)[1].lower()
        new = f"{p['dir']}/maps/{p['slug']}-{i}{ext}"
        if os.path.exists(os.path.join(REPO, old)):
            git("mv", old, new)
        p["maps"].append(new)
    for j, cid in enumerate(p.get("catalog", []), len(p["maps"]) + 1):
        src = os.path.join(os.path.dirname(__file__), "catalog", cid + ".jpg")
        new = f"{p['dir']}/maps/{p['slug']}-{j}.jpg"
        if os.path.exists(src) and not os.path.exists(os.path.join(REPO, new)):
            shutil.copy(src, os.path.join(REPO, new))
        p["maps"].append(new)
    # pick up any images already placed in maps/ (later runs)
    for f in sorted(os.listdir(os.path.join(d, "maps"))):
        rel = f"{p['dir']}/maps/{f}"
        if rel not in p["maps"] and f.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            p["maps"].append(rel)

# remove old category folders (only READMEs remain there)
for old in ["Category-A-Remote-Sensing", "Category-B-Cartography", "Category-C-Urban-GIS", "Category-D-Network-GIS"]:
    if os.path.exists(os.path.join(REPO, old)):
        git("rm", "-r", "-q", old)

def readme(p):
    cat = CATS[p["cat"]][1]
    L = [f"# {p['title']}", ""]
    L.append(f"**Category:** {cat} &nbsp;·&nbsp; **Location:** {p['where']} &nbsp;·&nbsp; **Year:** {p['year']}  ")
    L.append(f"**Client:** {p['client']}  ")
    L.append(f"**Tools & data:** {', '.join(p['tools'])}")
    L.append("")
    if p.get("study"):
        L += ["> Practice study. Course and client details are omitted.", ""]
    caps = p.get("captions", [])
    for k, m in enumerate(p["maps"]):
        cap = caps[k] if k < len(caps) else p["title"]
        L += [f"![{cap}](maps/{q(os.path.basename(m))})", f"*Figure {k+1}. {cap}*", ""]
    if not p["maps"]:
        L += ["*No public map for this project: the deliverable was data or code (see Deliverables).*", ""]
    L += ["## Overview", p["summary"], ""]
    if p.get("challenge"):
        L += ["## Challenge", p["challenge"], ""]
    if p.get("data"):
        L += ["## Data"] + [f"- {x}" for x in p["data"]] + [""]
    L += ["## Approach"]
    L += [f"{i}. {s}" for i, s in enumerate(p["method"], 1)]
    L += ["", "## Results"]
    if p.get("findings"):
        L += [f"- {x}" for x in p["findings"]] + [""]
    if not p.get("findings"):
        L += [p["result"], ""]
    if p.get("links"):
        L += ["## Links", ""] + [f"- [{a}]({u})" for a,u in p["links"]] + [""]
    if p.get("files"):
        L += ["## Deliverables", ""]
        L += [f"- {f}" for f in p["files"]]
        L.append("")
    if p.get("note"):
        L += [f"*{p['note']}*", ""]
    L += ["---", f"[← All projects](../../README.md) · [Portfolio website]({SITE}projects/{p['slug']}.html)", ""]
    return "\n".join(L)

for p in P:
    open(os.path.join(REPO, p["dir"], "README.md"), "w").write(readme(p))
    os.makedirs(os.path.join(REPO, p["dir"], "data"), exist_ok=True)
    keep = os.path.join(REPO, p["dir"], "data", ".gitkeep")
    if not os.listdir(os.path.join(REPO, p["dir"], "data")): open(keep, "w").close()
    if not os.listdir(os.path.join(REPO, p["dir"], "maps")): open(os.path.join(REPO, p["dir"], "maps", ".gitkeep"), "w").close()

# root README
R = ["# GIS & Remote Sensing Project Showcase", "",
     "**Abdul Haleem Khan**, GIS Engineer & Remote Sensing Specialist  ",
     f"[Portfolio website]({SITE}) · [Upwork](https://www.upwork.com/freelancers/abdulhaleemrsgis) · [LinkedIn](https://www.linkedin.com/in/abdul-haleem-khan-rs-gis-specialist) · [Email](mailto:abdulhaleemk03@gmail.com)", "",
     "Final maps, reports and data from planning consultancy work in Pakistan and freelance GIS projects for clients in the USA, Saudi Arabia, Switzerland and beyond, organised by discipline. Each folder has the maps, a short write-up and the delivered files.", ""]
for key, (catdir, name) in CATS.items():
    ps = [p for p in P if p["cat"] == key]
    R += [f"## {name}", "", "| Project | Where | Year | Tools |", "|---|---|---|---|"]
    for p in ps:
        R.append(f"| [{p['title']}]({catdir}/{p['slug']}/) | {p['where']} | {p['year']} | {', '.join(p['tools'][:3])} |")
    R.append("")
R += ["---", "Practice studies are anonymised: course and client details are omitted.", ""]
open(os.path.join(REPO, "README.md"), "w").write("\n".join(R))

import json
json.dump([{k: v for k, v in p.items()} for p in P], open(os.path.join(os.path.dirname(__file__), "projects_built.json"), "w"), indent=1)
print(len(P), "projects;", sum(1 for p in P if p["maps"]), "with maps")
