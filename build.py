"""Generates the static site. Edit SPECS / DOCS below, then run: python3 build.py"""
SPECS = [
 ("cardiology","Cardiology","❤️","Heart & vascular care"),
 ("neurology","Neurology","🧠","Brain & nervous system"),
 ("neurosurgery","Neurosurgery","🧠","Brain & spinal surgery"),
 ("orthopedics","Orthopedics","🦴","Bones & joints"),
 ("pediatrics","Pediatrics","👶","Care for children & teens"),
 ("dermatology","Dermatology","🧴","Skin, hair & nails"),
 ("gynecology","Gynecology","🌸","Women's health"),
 ("ent","ENT","👂","Ear, nose & throat"),
 ("ophthalmology","Ophthalmology","👁️","Eye care & vision"),
 ("urology","Urology","💧","Kidney & urinary health"),
 ("gastroenterology","Gastroenterology","🩺","Digestive system"),
 ("psychiatry","Psychiatry","💬","Mental health care"),
 ("oncology","Oncology","🎗️","Cancer care"),
 ("pulmonology","Pulmonology","🫁","Lungs & breathing"),
]
# (specialty id, name, qualifications, years experience, days, hours)
DOCS = [
 ("cardiology","Dr. Arjun Mehta","MD, DM (Cardiology)",18,"Mon · Wed · Fri","9:00 AM – 1:00 PM"),
 ("cardiology","Dr. Nadia Rahman","MD, FACC",12,"Tue · Thu","2:00 PM – 6:00 PM"),
 ("neurology","Dr. Samuel Ortiz","MD, DM (Neurology)",15,"Mon · Thu","10:00 AM – 2:00 PM"),
 ("neurosurgery","Dr. Priya Nair","MS, MCh (Neurosurgery)",20,"Tue · Fri","9:00 AM – 12:00 PM"),
 ("orthopedics","Dr. Daniel Hughes","MS (Orthopedics)",14,"Mon · Wed · Sat","11:00 AM – 3:00 PM"),
 ("pediatrics","Dr. Amira Khalid","MD (Pediatrics)",10,"Mon – Fri","9:00 AM – 1:00 PM"),
 ("dermatology","Dr. Helen Park","MD (Dermatology)",9,"Wed · Fri","1:00 PM – 5:00 PM"),
 ("gynecology","Dr. Sofia Marlowe","MD, DGO",16,"Mon · Tue · Thu","10:00 AM – 2:00 PM"),
 ("ent","Dr. Rohan Verma","MS (ENT)",11,"Tue · Sat","9:00 AM – 1:00 PM"),
 ("ophthalmology","Dr. Lena Fischer","MD (Ophthalmology)",13,"Mon · Thu","2:00 PM – 6:00 PM"),
 ("urology","Dr. Kareem Aziz","MS, MCh (Urology)",17,"Wed · Fri","10:00 AM – 2:00 PM"),
 ("gastroenterology","Dr. Meera Iyer","MD, DM (Gastroenterology)",12,"Tue · Thu","9:00 AM – 1:00 PM"),
 ("psychiatry","Dr. Jonas Weber","MD (Psychiatry)",8,"Mon · Wed","3:00 PM – 7:00 PM"),
 ("oncology","Dr. Grace Adeyemi","MD, DM (Oncology)",19,"Tue · Fri","10:00 AM – 3:00 PM"),
 ("pulmonology","Dr. Tomas Silva","MD (Pulmonology)",14,"Mon · Thu","9:00 AM – 12:00 PM"),
]
S = {s[0]: s for s in SPECS}
NAV = [("index.html","Home"),("doctors.html","Doctors"),("specialties.html","Specialties"),("about.html","About"),("contact.html","Contact")]
FONTS = "https://fonts.googleapis.com/css2?family=Fraunces:wght@600;700&family=Source+Sans+3:wght@400;600&display=swap"
PHONE = "+1 (555) 014-2911"

def page(fname, title, body, extra=""):
    nav = "".join(f'<a href="{h}"{" class=on" if h==fname else ""}>{t}</a>' for h,t in NAV)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · Meridian General</title><link rel="stylesheet" href="{FONTS}"><link rel="stylesheet" href="style.css"></head><body>
<div class="top"><div class="wrap"><span>🚑 Emergency Line: <u>{PHONE}</u> — open 24/7</span><span>123 Harborview Ave, Meridian City</span></div></div>
<header><div class="wrap"><a class="logo" href="index.html"><b>M+</b>Meridian General</a><nav>{nav}</nav><a class="btn" href="doctors.html">Find a Doctor</a></div></header>
{body}
<footer><div class="wrap"><div class="cols"><div><a class="logo" href="index.html"><b>M+</b>Meridian General</a><p>A private multi-specialty hospital connecting patients with trusted consultants across {len(SPECS)} departments.</p></div>
<div><h4>Explore</h4><a href="doctors.html">Find a Doctor</a><a href="specialties.html">Specialties</a></div>
<div><h4>Hospital</h4><a href="about.html">About Us</a><a href="contact.html">Contact</a></div>
<div><h4>Contact</h4><p>123 Harborview Ave<br>+1 (555) 014-2900<br>care@meridiangeneral.example</p></div></div>
<div class="copy"><span>© 2026 Meridian General Hospital. All rights reserved.</span><span>Sample data for demonstration only.</span></div></div></footer>{extra}</body></html>"""

def spec_card(s):
    n = sum(d[0]==s[0] for d in DOCS)
    return f'<a class="card" href="specialty-{s[0]}.html"><div class="ico">{s[2]}</div><h3>{s[1]}</h3><p>{s[3]}</p><span class="count">{n} doctor{"s" if n!=1 else ""}</span></a>'

def doc_card(d):
    sp = S[d[0]]; ini = "".join(w[0] for w in d[1].replace("Dr. ","").split()[:2])
    key = f"{d[1]} {sp[1]} {sp[3]} {d[2]}".lower()
    return f'''<div class="card doc" data-s="{key}"><div class="av">{ini}</div><h3>{d[1]}</h3><a class="tag" href="specialty-{sp[0]}.html">{sp[1]}</a><small>{d[2]} · {d[3]} yrs experience</small><div class="sched"><b>Consultation hours</b>{d[4]}<br>{d[5]}</div></div>'''

def write(f, html): open(f, "w", encoding="utf-8").write(html)

write("index.html", page("index.html","Home", f"""<section class="hero"><div class="wrap"><div><span class="eyebrow">Meridian General Hospital</span><h1>Find the Right Doctor for Your Care</h1>
<p>Search {len(DOCS)} consultants across {len(SPECS)} specialties and check their consultation schedules.</p>
<form class="search" action="doctors.html"><label for="q">Search by doctor name or specialty</label><div><input id="q" name="q" placeholder="e.g. Cardiology, Dr. Rahman, knee pain…"><button class="btn">Find a Doctor</button></div></form>
<div class="cta"><a class="btn alt" href="doctors.html">Meet Our Doctors</a><a class="btn out" href="specialties.html">Browse Specialties</a></div></div>
<div class="panel"><div>🚑 Emergency Line: {PHONE} — staffed around the clock</div></div></div></section>
<section style="padding-top:0"><div class="wrap"><span class="eyebrow">Departments</span><h2>Browse by Specialty</h2><p class="lead">Every consultant is grouped by what they treat, so you can go straight to the right kind of care.</p>
<div class="grid">{"".join(spec_card(s) for s in SPECS)}</div></div></section>"""))

write("specialties.html", page("specialties.html","Specialties", f"""<section class="page"><div class="wrap"><span class="eyebrow">Departments</span><h2>Browse by Specialty</h2><p class="lead">Select a department to see its consultants and their schedules.</p><div class="grid">{"".join(spec_card(s) for s in SPECS)}</div></div></section>"""))

write("doctors.html", page("doctors.html","Doctors", f"""<section class="page"><div class="wrap"><span class="eyebrow">Our consultants</span><h2>Find a Doctor</h2>
<form class="search" onsubmit="return false"><label for="q">Search by doctor name or specialty</label><div><input id="q" placeholder="e.g. Cardiology, Dr. Rahman…" autocomplete="off"></div></form>
<div class="grid" id="list" style="margin-top:0">{"".join(doc_card(d) for d in DOCS)}</div><p class="none" id="none">No doctors match your search.</p></div></section>""",
"""<script>const q=document.getElementById('q'),cards=[...document.querySelectorAll('#list .card')];
function f(){const v=q.value.trim().toLowerCase();let n=0;cards.forEach(c=>{const m=c.dataset.s.includes(v);c.style.display=m?'':'none';n+=m});document.getElementById('none').style.display=n?'none':'block'}
q.value=new URLSearchParams(location.search).get('q')||'';q.oninput=f;f();</script>"""))

for s in SPECS:
    ds = [d for d in DOCS if d[0]==s[0]]
    write(f"specialty-{s[0]}.html", page("specialties.html", s[1], f"""<section class="page"><div class="wrap"><div class="crumb"><a href="specialties.html">Specialties</a> / {s[1]}</div>
<div class="ico" style="margin-top:18px">{s[2]}</div><h2>{s[1]}</h2><p class="lead">{s[3]}. Meet our {s[1].lower()} consultant{"s" if len(ds)!=1 else ""}.</p>
<div class="grid">{"".join(doc_card(d) for d in ds)}</div><p style="margin-top:36px"><a class="tag" href="specialties.html">← All specialties</a></p></div></section>"""))

write("about.html", page("about.html","About", f"""<section class="page"><div class="wrap"><span class="eyebrow">About us</span><h2>Meridian General Hospital</h2>
<p class="lead">Meridian General is a private multi-specialty hospital with {len(DOCS)} consultants across {len(SPECS)} departments. Our goal is simple: help patients reach the right specialist quickly, with clear information about who treats what and when they are available.</p>
<div class="grid"><div class="card"><h3>Expert consultants</h3><p>Experienced specialists across every department.</p></div><div class="card"><h3>Open 24/7</h3><p>Our emergency line is staffed around the clock.</p></div><div class="card"><h3>Clear schedules</h3><p>Every doctor's consultation hours are listed on their profile.</p></div></div></div></section>"""))

write("contact.html", page("contact.html","Contact", f"""<section class="page"><div class="wrap"><span class="eyebrow">Get in touch</span><h2>Contact Us</h2>
<div class="grid"><div class="card"><h3>Emergency</h3><p>{PHONE}<br>Open 24/7</p></div><div class="card"><h3>General enquiries</h3><p>+1 (555) 014-2900<br>care@meridiangeneral.example</p></div><div class="card"><h3>Visit us</h3><p>123 Harborview Ave<br>Meridian City</p></div></div></div></section>"""))
print("Built", len(SPECS)+5, "pages")
