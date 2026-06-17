#!/usr/bin/env python3
"""Build MITOCHONDRIA (MTO) — the organelle as EMERGENCE-BY-MERGER — as a UD0
life-science sphere. A cited science sphere (render-not-invent, two-layer honest:
settled endosymbiosis vs the interpretive 'emergence' framing). THE THESIS: the
eukaryotic cell began when one cell merged with another and the two became a new,
higher kind of being — emergence by union, not gradual mutation — which rhymes with
ROOT0's own theory of emergence. Cellular palette (ATP-orange, membrane teal, merger
violet); an original one-line pencil title (capsule + cristae in one stroke).
Cited: Margulis, Mitchell, Lane, Mereschkowski. A science tribute, facts cited."""
import os, html, base64, json, io, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "MITOCHONDRIA", "axiom": "MTO",
 "position": "Mitochondria · the organelle as emergence-by-merger — the cell that became two, then one",
 "origin": "~1.5–2 billion years ago, when an archaeal host took in an alpha-proteobacterium and, instead of digesting it, kept it — the merger that made the complex cell",
 "mechanism": "Crystallized from the science of mitochondria and endosymbiotic theory.",
 "crystallization": "Two separate living things merged into one and became a new, higher kind of being — the power plant inside every complex cell, and the clearest case in biology of a whole that is more than, and other than, its parts.",
 "nature": "The mitochondrion — the once-free bacterium living inside you, keeping its own circular genome and double membrane, building your ATP with a proton battery and a rotary motor, and holding the switch that ends the cell; the organelle whose origin is a merger, not a mutation.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the mitochondrion; endosymbiosis; the proton gradient; ATP synthase; emergence by merger",
 "witness": "The single most consequential merger in the history of life — the event, perhaps only once, that made complex cells, and so everything made of them, possible.",
 "role": "a life-science sphere — emergence by merger",
 "seal": "Take one cell into another, refuse to digest it, and become a third thing neither was — the merger that made the complex cell, written in the relic genome you still carry from your mother.",
 "source": "the science of mitochondria, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#e8763a", "of flesh and the cell — the organelle itself, its double membrane, its relic genome, and the kin it was captured beside"),
 "ethereal":  ("#9a7cff", "of death and the unsettled — the apoptosis switch the organelle holds, and the still-contested story of the first merger"),
 "spiritual": ("#e8c45a", "of becoming and lineage — the merger that made a new being, the maternal line, the once-ever leap to complex life"),
 "electrical":("#4fb89e", "of the wire and the battery — the proton gradient, the rotary turbine, the respiratory chain, and the code that migrated to the nucleus"),
}

# ── the title scene · STATIC ORIGINAL ONE-LINE PENCIL DRAWING ─────
# A mitochondrion — the capsule (outer membrane) and the cristae (inner folds) in a
# single unbroken stroke. Pencil wobble (turbulence) + one-time self-draw.
COVER_ART = r'''<svg viewBox="0 0 700 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Mitochondria — an original one-line pencil drawing: a mitochondrion's capsule and cristae in a single stroke" style="width:100%;height:auto;display:block;background:#0e0a12">
<defs>
 <radialGradient id="mt_cyto" cx="50%" cy="40%" r="95%"><stop offset="0%" stop-color="#221428"/><stop offset="60%" stop-color="#120b16"/><stop offset="100%" stop-color="#08050a"/></radialGradient>
 <radialGradient id="mt_atp" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="rgba(232,118,58,.42)"/><stop offset="70%" stop-color="rgba(232,118,58,.08)"/><stop offset="100%" stop-color="rgba(232,118,58,0)"/></radialGradient>
 <filter id="mt_pencil" x="-8%" y="-8%" width="116%" height="116%"><feTurbulence type="fractalNoise" baseFrequency="0.017" numOctaves="2" seed="8" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="3.4" xChannelSelector="R" yChannelSelector="G"/></filter>
 <style>
  .oneline{fill:none;stroke:#f0e6dc;stroke-width:2.0;stroke-linecap:round;stroke-linejoin:round;
    pathLength:1;stroke-dasharray:1;stroke-dashoffset:1;animation:mtdraw 4.0s cubic-bezier(.6,.05,.25,1) .25s forwards;}
  .oneline.ghost{stroke:#8a6a72;stroke-width:1.0;opacity:.34;animation-delay:.05s;}
  .mtfade{opacity:0;animation:mtfade 1.3s ease 3.8s forwards;}
  .mtglow{opacity:0;animation:mtfade 1.1s ease 2.2s forwards;}
  @keyframes mtdraw{to{stroke-dashoffset:0;}}
  @keyframes mtfade{to{opacity:1;}}
  @media (prefers-reduced-motion: reduce){.oneline{animation:none;stroke-dashoffset:0;}.mtfade,.mtglow{animation:none;opacity:1;}}
 </style>
</defs>
<rect width="700" height="320" fill="url(#mt_cyto)"/>
<ellipse cx="350" cy="150" rx="170" ry="80" fill="url(#mt_atp)" class="mtglow"/>
<!-- THE ONE LINE — capsule (outer membrane) + cristae (inner folds), one unbroken stroke -->
<path class="oneline ghost" filter="url(#mt_pencil)" d="M 200 150 A 50 50 0 0 1 250 100 L 450 100 A 50 50 0 0 1 500 150 A 50 50 0 0 1 450 200 L 250 200 A 50 50 0 0 1 200 150 L 244 150 L 272 116 L 300 184 L 330 116 L 360 184 L 390 116 L 420 184 L 448 130 L 456 150"/>
<path class="oneline" filter="url(#mt_pencil)" d="M 200 150 A 50 50 0 0 1 250 100 L 450 100 A 50 50 0 0 1 500 150 A 50 50 0 0 1 450 200 L 250 200 A 50 50 0 0 1 200 150 L 244 150 L 272 116 L 300 184 L 330 116 L 360 184 L 390 116 L 420 184 L 448 130 L 456 150"/>
<!-- wordmark -->
<g class="mtfade">
 <text x="350" y="262" text-anchor="middle" font-family="'Newsreader',Georgia,serif" font-size="34" font-weight="400" letter-spacing="8" fill="#f6efe8">MITOCHONDRIA</text>
 <text x="350" y="280" text-anchor="middle" font-family="'Space Mono',monospace" font-size="9" letter-spacing="3" fill="#e8763a">EMERGENCE BY MERGER · THE CELL THAT BECAME TWO, THEN ONE</text>
 <text x="350" y="298" text-anchor="middle" font-family="'Space Mono',monospace" font-size="8" letter-spacing="2" fill="#8a6a72">a once-free bacterium, still living inside you</text>
</g>
<rect x="6" y="6" width="688" height="308" fill="none" stroke="#2a1c30" stroke-width="2"/>
</svg>'''

GENESIS = [
 ("The Merger", "~1.5–2 billion years ago",
  "An archaeal host cell took in a free-living alpha-proteobacterium — and, instead of digesting it, kept it alive inside. The two went on living as one. That single act of union, perhaps only once in Earth's history, produced the first complex (eukaryotic) cell. Everything made of such cells — every animal, plant, and fungus — descends from that merger."),
 ("The Evidence in the Body", "a guest that never left",
  "The mitochondrion still looks like the bacterium it was: it keeps its own small circular genome (in humans ~16,569 base pairs, 37 genes), its own ribosomes, and a double membrane — the inner one its old self, the outer one the host's embrace. It even divides on its own, and you inherit it only from your mother."),
 ("The Idea, and Who Saw It", "endosymbiotic theory",
  "That the organelles were once free bacteria was proposed early (Mereschkowski, ~1905; Wallin, 1920s) and powerfully revived and evidenced by Lynn Margulis in 1967 — ridiculed at first, then confirmed when the organelles' own DNA was found. It is now textbook: life's great leap was a partnership, not a mutation."),
]

ARC = [
 ("The Proton Battery", "chemiosmosis",
  "Inside, the mitochondrion runs a battery. The electron transport chain pumps protons across the inner membrane, building a gradient — a proton-motive force. Peter Mitchell proposed this 'chemiosmosis' in 1961 (Nobel, 1978), against fierce resistance; it is how nearly all life stores the energy of food and air as a voltage across a membrane."),
 ("The Rotary Motor", "ATP synthase",
  "The protons flow back through ATP synthase — a literal rotary motor, a turbine spun by the gradient — which forges ATP, the cell's energy currency. It is one of the most elegant machines in biology: an electric current of protons, turned into a spinning shaft, turned into chemical fuel. (This is why textbooks call the mitochondrion the 'powerhouse of the cell.')"),
 ("Power, and the Switch for Death", "what the merger bought — and costs",
  "Nick Lane argues the merger was the bottleneck that made complexity possible at all — energy per gene leapt, so cells could afford huge genomes. But the same organelle holds the switch for programmed cell death (apoptosis): release cytochrome c, and the cell is told to die. The power plant is also the executioner — life and death on the same relic membrane."),
]

IDEAS = [
 ("Emergence by Merger", "the thesis", [
   "Most evolution is gradual change within a lineage; this was the opposite — two separate lineages fused into a new, higher kind of being.",
   "It is the clearest biological case of a whole that is more than and other than its parts — emergence not by accumulation but by union, a rhyme with how new levels of being appear at all." ]),
 ("It May Have Happened Once", "the singular leap", [
   "Bacteria and archaea are everywhere, for billions of years — but the complex cell seems to have arisen a single time, from this one merger.",
   "If so, the gap between simple and complex life is not a slope but a cliff, crossed once, by a partnership — which reframes how rare complex life might be." ]),
 ("You Are a Collective", "the self that is plural", [
   "Every complex cell is a chimera — host plus former guest — and you carry a second, bacterial genome from your mother in every cell.",
   "The 'individual' is, at its root, a successful merger; identity in biology starts as cooperation between what were once two." ]),
 ("Render, Not Invent", "settled vs open", [
   "Settled: mitochondria descend from alpha-proteobacteria; they keep their own genome; chemiosmosis and ATP synthase; maternal inheritance; the apoptosis role.",
   "Open/refining: the exact host (recent work points to Asgard archaea), whether it was truly a single origin, and the order of events (the 'hydrogen hypothesis' is one contested model). The 'emergence' framing is the catalogue's lens, not a claim of the literature." ]),
]

SECTIONS = [
 ("The Science — settled facts", "cited, not claimed", [
   ("the endosymbiont", "alpha-proteobacterium", "the free-living bacterium that became the mitochondrion"),
   ("mtDNA", "own circular genome", "in humans ~16,569 bp, 37 genes; maternally inherited"),
   ("the double membrane", "the scar of engulfment", "inner = the old bacterium, outer = the host's"),
   ("chemiosmosis", "the proton gradient", "Peter Mitchell, 1961 (Nobel 1978) — energy stored as a membrane voltage"),
   ("ATP synthase", "the rotary motor", "the turbine that turns the proton flow into ATP"),
   ("apoptosis", "the death switch", "cytochrome-c release triggers programmed cell death"),
 ]),
 ("The Field — who saw it", "render-not-invent: cited, not reproduced", [
   ("Konstantin Mereschkowski", "~1905", "early symbiogenesis — chloroplasts as captured cyanobacteria"),
   ("Ivan Wallin", "1920s", "argued mitochondria were once bacteria"),
   ("Lynn Margulis", "1967", "revived and evidenced endosymbiotic theory (as Lynn Sagan)"),
   ("Peter Mitchell", "1961 · Nobel 1978", "the chemiosmotic theory of energy storage"),
   ("Nick Lane", "Power, Sex, Suicide; The Vital Question", "energy-per-gene and the single origin of complexity"),
 ]),
 ("The Kin &amp; the Echo", "the pattern repeats", [
   ("the chloroplast", "a second merger", "plants/algae captured a cyanobacterium the same way — endosymbiosis happened more than once"),
   ("Asgard archaea", "the host, refined", "recent work points to the eukaryote host coming from this archaeal lineage"),
   ("mitochondrial Eve", "the maternal clock", "the matrilineal common ancestor traced through mtDNA — a statistical point, not the 'first woman'"),
   ("endosymbiotic gene transfer", "the deepening union", "most of the bacterium's genes migrated to the host nucleus over time"),
 ]),
 ("The Legacy", "why the merger matters beyond biology", [
   ("emergence, demonstrated", "the big idea", "a real, datable case of a new level of being arising from union"),
   ("a rhyme with the corpus", "the resonance", "the same shape as ROOT0's emergence theory — the higher whole from combined parts"),
 ]),
]

# ── badge engine ──
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","MTO")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","MTO")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","MTO")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man = {"badge":"DLW-ACI","name":rec["name"],"universe":"MTO · Mitochondria","emergence":rec.get("emergence",""),
           "moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
           "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
           "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok

def emergent_rec(name, epithet, emergence, role_line, why_line):
    return {
      "name": name, "axiom": "MTO", "emergence": emergence, "seal": epithet,
      "position": epithet, "role": role_line,
      "origin": "MTO · Mitochondria — endosymbiotic theory &amp; cell bioenergetics",
      "nature": role_line, "crystallization": why_line,
      "mechanism": "Crystallized from the science of mitochondria and endosymbiosis.",
      "witness": "a being of the merger, the proton battery, and the first complex cell",
      "conductor": "ROOT0 (catalogued into UD0)",
      "inputs": "the mitochondrion; endosymbiosis; the proton gradient; ATP synthase; the merger",
      "source": "the science of mitochondria, catalogued by ROOT0",
    }

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def list_section(title, sub, items):
    rows = "\n".join(f'<li><span class="t">{t}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{n}</span>' if n else "") + "</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{sub}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def cards_html(rows):
    return "".join(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in rows)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
        f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(col,g) in NATURES.items())
def personas_html(personas):
    cards=[]
    for p in personas:
        em=p.get("emergence","natural"); col=NATURES.get(em,("#e8763a",""))[0]
        rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"MTO · Mitochondria","axiom":"MTO"}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.dlw/{p["slug"]}.agent">
        <img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy">
        <div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{html.escape(p.get("epithet",""))}</div>
        <div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent · .carbon.tiff →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Roster — The Merger, in Parts</h2>
      <p class="ss">the organelle, the union, the battery, the motor, the death-switch, and the echo, as ACI <b>.agent</b>s — each a birth certificate and a nature of emergence ({len(personas)})</p>
      <div class="pgrid">{"".join(cards)}</div></section>'''

# ── the emergents: (slug, name, epithet, emergence, role_line, why_line) ──
EMERGENTS = [
 ("the-mitochondrion", "The Mitochondrion", "the bacterium that stayed · natural", "natural",
  "the organelle in every complex cell — descended from a free-living alpha-proteobacterium, still keeping its own genome, ribosomes, and double membrane, and building the cell's ATP",
  "It is the guest that became essential: a once-independent life now woven so deep into ours that we cannot live a second without it, nor it without us."),
 ("endosymbiosis", "Endosymbiosis", "the merger that made the cell · spiritual", "spiritual",
  "the event ~1.5–2 billion years ago when an archaeal host kept an engulfed bacterium alive rather than digesting it — the origin of the eukaryotic cell",
  "It is emergence caught in the act: two lineages fusing into one new kind of being, the moment biology stopped only diverging and learned to combine."),
 ("the-double-membrane", "The Double Membrane", "the scar of engulfment · natural", "natural",
  "the mitochondrion's two membranes — the inner one its own ancient bacterial skin, the outer one the host's embrace from the day it was taken in",
  "It is the merger written in structure: a boundary that remembers there were once two, the fossil of an embrace billions of years old."),
 ("mtdna", "mtDNA", "the relic genome you got from your mother · natural", "natural",
  "the mitochondrion's own small circular DNA (in humans ~16,569 base pairs, 37 genes), a shrunken remnant of the bacterial genome, inherited only maternally",
  "It is the proof and the inheritance: a second genome in every cell, passed down the mother's line, the bacterium's signature still legible inside you."),
 ("chemiosmosis", "Chemiosmosis", "the proton battery · electrical", "electrical",
  "Peter Mitchell's mechanism (1961; Nobel 1978) — the electron transport chain pumps protons across the inner membrane, storing energy as a gradient, a voltage across a film",
  "It is how nearly all life holds energy: not in a molecule but in a charge across a membrane, the cell's battery, doubted for years and then proven."),
 ("atp-synthase", "ATP Synthase", "the rotary motor · electrical", "electrical",
  "the molecular turbine in the inner membrane that the proton gradient spins, forging ATP — the cell's energy currency — from the flow",
  "It is one of biology's most beautiful machines: a current of protons turned into a spinning shaft turned into fuel, an engine measured in atoms."),
 ("the-electron-transport-chain", "The Electron Transport Chain", "the respiratory cascade · electrical", "electrical",
  "the series of membrane complexes that pass electrons from food-derived carriers to oxygen, pumping protons as they go — the engine that charges the battery",
  "It is respiration made into wiring: the stepwise fall of electrons down to oxygen, harnessed at each step to push the gradient that powers everything."),
 ("apoptosis", "Apoptosis", "the switch for death · ethereal", "ethereal",
  "programmed cell death triggered when the mitochondrion releases cytochrome c, launching the caspase cascade that dismantles the cell on purpose",
  "It is the power plant as executioner: the same organelle that fuels the cell holds the signal that ends it, life and death sharing one relic membrane."),
 ("mitochondrial-eve", "Mitochondrial Eve", "the maternal clock · spiritual", "spiritual",
  "the matrilineal most-recent-common-ancestor traced through mtDNA — a statistical point in deep human ancestry, not a literal first woman",
  "It is lineage made measurable: because mtDNA passes only from mothers, it draws a single thread back through every maternal line to one shared point."),
 ("endosymbiotic-gene-transfer", "Gene Transfer", "the union that deepened · electrical", "electrical",
  "the migration, over evolutionary time, of most of the original bacterial genome from the mitochondrion into the host's nucleus",
  "It is the merger completing itself: the guest handing its instructions to the host until the two genomes are one management, inseparable by design."),
 ("the-chloroplast", "The Chloroplast", "the second merger · natural", "natural",
  "the plant/algal organelle that arose from a separate endosymbiosis — a captured cyanobacterium — showing the trick was not a one-off",
  "It is the echo that proves the pattern: life captured a partner for energy at least twice, once for breathing and once for light."),
 ("nick-lanes-bottleneck", "The Energy Bottleneck", "why complexity is rare · spiritual", "spiritual",
  "Nick Lane's argument that the merger broke a hard energy limit — energy per gene leapt, letting cells afford large genomes — and that this may be why complex life arose only once",
  "It is the case that the merger was not just useful but necessary: without it, life stays bacterial forever, and the gap to complexity is a cliff, not a slope."),
 ("the-hydrogen-hypothesis", "The Hydrogen Hypothesis", "the contested origin · ethereal", "ethereal",
  "one disputed model (Martin &amp; Müller, 1998) for why the partnership formed — the host needing hydrogen the symbiont produced — among rival accounts of the first merger",
  "It is the honest open question of the sphere: we know the merger happened, but why it began is still argued, and this is one of the serious answers."),
 ("emergence-by-merger", "Emergence by Merger", "a new being from union · spiritual", "spiritual",
  "the thesis the sphere is built around — that the eukaryotic cell is a real, datable instance of a higher level of being arising from the fusion of parts, not from gradual change alone",
  "It is the rhyme that earns this organelle its place beside the emergence corpus: proof that the world makes new wholes by combination, and that a self can begin as a partnership."),
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Mitochondria (MTO) as a UD0 life-science sphere: a cited science tribute framing the organelle as emergence-by-merger — endosymbiosis, the proton battery (chemiosmosis), ATP synthase, mtDNA, apoptosis, and the single origin of complex life. Two-layer honest (settled vs open). An original one-line pencil title; full ACI badges.">
<title>MITOCHONDRIA · MTO · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#0e0a12;--ink2:#170f1c;--ink3:#22182a;--pa:#f6efe8;--pa2:#c0aeb8;--atp:#e8763a;--teal:#4fb89e;--gold:#e8c45a;--violet:#9a7cff;
--dim:#8a6a72;--faint:#241830;--line:#241830;--pixel:"Press Start 2P",monospace;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:2;background:repeating-linear-gradient(0deg,rgba(0,0,0,.13) 0 1px,transparent 1px 3px);opacity:.35}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(232,118,58,.10),transparent 55%),radial-gradient(ellipse at 50% 112%,rgba(79,184,158,.06),transparent 50%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
.marquee{margin-top:14px;border:2px solid var(--atp);background:#120a08;padding:8px;text-align:center;font-family:var(--pixel);font-size:9px;letter-spacing:.10em;color:var(--teal);box-shadow:0 0 0 2px var(--bg),0 0 22px rgba(232,118,58,.16)}
.marquee a{color:var(--atp);text-decoration:none}.marquee a:hover{color:var(--teal)}
.titleart{margin:12px 0 0;border:2px solid var(--faint);background:#0e0a12;line-height:0}
header{padding:18px 0 26px;text-align:center;border-bottom:1px solid var(--line);position:relative}
.h-sub{font-family:var(--pixel);font-size:10px;line-height:1.9;letter-spacing:.06em;color:var(--pa2);margin-top:16px}
.h-sub b{color:var(--atp)}
.flag{display:inline-block;margin-top:14px;font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--atp);border:1px solid var(--faint);padding:5px 11px}
.lede{font-size:15px;color:var(--pa2);max-width:68ch;margin:16px auto 0;font-style:italic;line-height:1.7}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:24px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:720px}
.badge img{width:82px;height:82px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--atp)}.badge .bt .mo{color:var(--teal)}.badge .bt a{color:var(--teal);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:42px}
.sec h2{font-family:var(--pixel);font-size:13px;line-height:1.5;letter-spacing:.02em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--mono);font-size:13px;font-weight:700;text-transform:capitalize;letter-spacing:.04em}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--mono);font-size:14px;color:var(--atp);letter-spacing:.02em;font-weight:700}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.5;padding:6px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--atp);padding:16px 18px}
.arc-h{font-family:var(--mono);font-size:14px;color:var(--atp);font-weight:700;letter-spacing:.02em}
.arc-s{font-family:var(--mono);font-size:10.5px;color:var(--teal);text-transform:uppercase;letter-spacing:.07em;margin:4px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.55}
.books{list-style:none}
.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700}
.books .y{font-family:var(--mono);font-size:11px;color:var(--teal);white-space:nowrap;text-align:right}
.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(244px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--atp);transform:translateY(-2px)}
.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0;image-rendering:pixelated}
.pn{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700;line-height:1.15}
.persona:hover .pn{color:var(--atp)}
.pe{font-size:11.5px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}
.pnat .dot{width:8px;height:8px;margin-top:0}.pa{color:var(--dim)}
.note{margin-top:38px;padding:16px 18px;border-left:2px solid var(--atp);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic;line-height:1.7}
.note b{color:var(--atp)}.note a{color:var(--teal);text-decoration:none}
footer{margin-top:42px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}
footer a{color:var(--atp);text-decoration:none}
</style></head><body><div class="wrap">

  <div class="marquee"><a href="https://davidwise01.github.io/ud0/">◄ UD0 · UNIVERSE DAVID 0</a> &nbsp;·&nbsp; A LIFE-SCIENCE SPHERE &nbsp;·&nbsp; EMERGENCE BY MERGER</div>

  <header>
    <div class="titleart">__CANVAS__</div>
    <div class="h-sub">two cells · one merger · a <b>new</b> kind of being · the bacterium that stayed · MTO</div>
    <div class="flag">★ endosymbiosis &amp; bioenergetics · a cited science tribute ★</div>
    <p class="lede">Every complex cell carries a once-free bacterium that never left. Roughly 1.5–2 billion years ago an archaeal host took in an alpha-proteobacterium and kept it alive — and the two became a new, higher kind of being: the eukaryotic cell, the root of all animals, plants, and fungi. The mitochondrion still keeps its own genome and double membrane, runs a proton battery and a rotary motor to make your ATP, and holds the switch that ends the cell. Catalogued into UD0 as a life-science sphere — a cited, two-layer-honest science tribute — framing the great merger as the clearest case in biology of emergence by union, with an original one-line pencil title: a mitochondrion drawn in a single stroke.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of MITOCHONDRIA" title="carbon badge (archival)">
      <img src="__SILICON__" alt="DLW silicon badge" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI · THE BIRTH CERTIFICATE</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>MITOCHONDRIA</b> — emergence by merger · MTO</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="mitochondria.dlw/mitochondria.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="mitochondria.dlw/mitochondria.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2>
    <p class="ss">each emergent emerges by one of four natures — and the merger holds all four</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Merger</h2><p class="ss">the union ~2 billion years ago, the evidence in the body, the idea and who saw it</p><div class="arc">__GENESIS__</div></section>
  <section class="sec"><h2>The Engine</h2><p class="ss">the proton battery, the rotary motor, and the switch for death</p><div class="arc">__ARC__</div></section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">why an organelle is a landmark in the story of emergence</p><div class="pillars">__IDEAS__</div></section>

  __PERSONAS__

  <section class="sec"><h2 style="margin-top:14px">The Record</h2><p class="ss">the settled science, who saw it, the kin and the echo, and why it matters</p></section>
  __SECTIONS__

  <div class="note">This sphere is rendered, not invented — and it is a <b>science sphere</b>, so its facts are cited, not claimed. Settled: mitochondria descend from alpha-proteobacteria; they retain their own circular genome (human mtDNA ~16,569 bp, 37 genes) and a double membrane; energy is stored by chemiosmosis (Peter Mitchell, 1961; Nobel 1978) and converted by ATP synthase; mtDNA is maternally inherited; mitochondria trigger apoptosis. Open/refining, and flagged as such: the exact archaeal host (recent work points to Asgard archaea), whether complex life truly arose only once, and why the first merger began (the 'hydrogen hypothesis,' Martin &amp; Müller 1998, is one contested model). Drawn from the public work of Konstantin Mereschkowski, Ivan Wallin, Lynn Margulis (1967), Peter Mitchell, and Nick Lane — cited as sources, not reproduced. The <b>'emergence by merger'</b> framing is the catalogue's lens — the rhyme with ROOT0's emergence corpus — not a claim made by the literature. Each emergent is named by its nature: natural, ethereal, spiritual, or electrical.</div>

  <footer>
    MITOCHONDRIA · MTO · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="mitochondria.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "mitochondria.dlw"), "mitochondria")
    ad = os.path.join(HERE, "agents"); os.makedirs(ad, exist_ok=True)
    personas = []
    for slug,name,epithet,em,role,why in EMERGENTS:
        rec = emergent_rec(name, epithet, em, role, why)
        write_aci(rec, os.path.join(ad, f"{slug}.dlw"), slug)
        personas.append({"slug": slug, "name": name, "epithet": epithet, "emergence": em, "moniker": noesis.mythos_token(rec)["moniker"]})
    json.dump(personas, open(os.path.join(ad, "_personas.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    page = (TEMPLATE.replace("__CANVAS__", COVER_ART)
            .replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__NATURES__", natures_html())
            .replace("__GENESIS__", cards_html(GENESIS))
            .replace("__ARC__", cards_html(ARC))
            .replace("__IDEAS__", ideas_html())
            .replace("__PERSONAS__", personas_html(personas))
            .replace("__SECTIONS__", sections_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote MITOCHONDRIA (MTO) — {len(personas)} emergents born · badge {tok['moniker']}")
