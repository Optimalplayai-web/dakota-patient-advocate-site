#!/usr/bin/env python3
"""
Static-site builder for Dakota Patient Advocate Solutions.

Run:  python3 build.py
Output: plain .html files in this folder, ready to upload to any host.
Edit the CONTENT sections below and re-run to regenerate.
"""

import os

OUT = os.path.dirname(os.path.abspath(__file__))

SITE = "https://www.dakotapatientadvocatesolutions.com"
BIZ = "Dakota Patient Advocate Solutions"
PHONE_DISPLAY = "(701) 319-1700"
PHONE_LINK = "+17013191700"
EMAIL = "dpas.nd@outlook.com"
CITY = "Mandan, ND 58554"
HOURS = "Monday – Friday, 8:00 am – 5:00 pm CT"

FACEBOOK = "https://www.facebook.com/profile.php?id=61579310060357"
INSTAGRAM = "https://www.instagram.com/dakotapatientadvocatesolutions/"
YOUTUBE = "https://www.youtube.com/@laurieboeshans275"
YT_UPLOADS = "UUkweh4HV-2vvSmd1lhYQfVw"  # uploads playlist for the channel

# --- Imagery pulled from the existing site (Squarespace CDN) --------------
CDN = "https://images.squarespace-cdn.com/content/v1/68792d6cbc7fb216ff14076a"
IMG_LOGO = f"{CDN}/899a9f0d-a95a-4214-9241-6dd5c9e0d573/Logo.png?format=750w"
IMG_HERO = f"{CDN}/48b85087-315c-4797-bf61-b7715363497d/Untitled+design.png?format=1500w"
IMG_FEATURE = f"{CDN}/1457f358-4f97-40c6-ba42-3a6a6b5df569/Untitled+design.png?format=1500w"
IMG_PACB = f"{CDN}/0357ea59-38d6-4076-91dd-3443fc6853bc/PACB-LOGO_RGB-300dpi.png?format=750w"
IMG_GNA = "https://gnanow.org/templates/gnanownew/images/gna_member_badge_2023.png"

NAV = [
    ("what-is-an-advocate.html", "What Is an Advocate"),
    ("services.html", "Services"),
    ("pricing.html", "Pricing"),
    ("about.html", "About Laurie"),
    ("videos.html", "Videos"),
    ("contact.html", "Contact"),
]

# --------------------------------------------------------------------------
# Inline SVG icon set
# --------------------------------------------------------------------------
def icon(name):
    p = {
        "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>',
        "receipt": '<path d="M4 2v20l2.5-1.5L9 22l2.5-1.5L14 22l2.5-1.5L19 22V2l-2.5 1.5L14 2l-2.5 1.5L9 2 6.5 3.5z"/><line x1="8" y1="8" x2="15" y2="8"/><line x1="8" y1="12" x2="15" y2="12"/>',
        "home": '<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/><path d="M9.5 21v-6h5v6"/>',
        "compass": '<circle cx="12" cy="12" r="9"/><polygon points="16 8 13.5 13.5 8 16 10.5 10.5 16 8"/>',
        "shield": '<path d="M12 2.5 20 6v6c0 5-3.4 8.4-8 9.5C7.4 20.4 4 17 4 12V6z"/><polyline points="9 12 11.2 14.2 15.5 9.8"/>',
        "file": '<path d="M14 2H7a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7z"/><polyline points="14 2 14 7 19 7"/><line x1="9" y1="13" x2="15" y2="13"/><line x1="9" y1="17" x2="13" y2="17"/>',
        "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
        "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><polyline points="2.5 6.5 12 13 21.5 6.5"/>',
        "pin": '<path d="M20 10.5c0 6-8 12-8 12s-8-6-8-12a8 8 0 1 1 16 0z"/><circle cx="12" cy="10.5" r="3"/>',
        "clock": '<circle cx="12" cy="12" r="9"/><polyline points="12 6.8 12 12 15.6 14"/>',
        "heart": '<path d="M20.4 5.6a5.2 5.2 0 0 0-7.4 0L12 6.6l-1-1a5.2 5.2 0 0 0-7.4 7.4l1 1 7.4 7.4 7.4-7.4 1-1a5.2 5.2 0 0 0 0-7.4z"/>',
        "users": '<path d="M16 20v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 20v-2a4 4 0 0 0-3-3.9"/><path d="M16 3.1a4 4 0 0 1 0 7.8"/>',
        "check-badge": '<circle cx="12" cy="12" r="9"/><polyline points="8.5 12.2 11 14.7 15.7 9.7"/>',
        "search": '<circle cx="11" cy="11" r="7"/><line x1="16.2" y1="16.2" x2="21" y2="21"/>',
        "star": '<polygon points="12 3 14.7 9 21 9.8 16.4 14.1 17.6 20.4 12 17.4 6.4 20.4 7.6 14.1 3 9.8 9.3 9"/>',
        "play": '<circle cx="12" cy="12" r="9"/><polygon points="10 8.5 16 12 10 15.5"/>',
    }[name]
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>')


SOCIAL_SVG = {
    "facebook": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22 12.06C22 6.5 17.52 2 12 2S2 6.5 2 12.06c0 5.02 3.66 9.18 8.44 9.94v-7.03H7.9v-2.9h2.54V9.85c0-2.52 1.5-3.91 3.77-3.91 1.09 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.78-1.63 1.57v1.89h2.78l-.45 2.9h-2.33V22c4.78-.76 8.44-4.92 8.44-9.94z"/></svg>',
    "instagram": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2.16c3.2 0 3.58.01 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.27.06-1.65.07-4.85.07s-3.58-.01-4.85-.07c-1.17-.05-1.8-.25-2.23-.41-.56-.22-.96-.48-1.38-.9a3.7 3.7 0 0 1-.9-1.38c-.16-.42-.36-1.06-.41-2.23C2.17 15.58 2.16 15.2 2.16 12s.01-3.58.07-4.85c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41C8.42 2.17 8.8 2.16 12 2.16zm0 1.98c-3.15 0-3.5.01-4.74.07-1.14.05-1.76.24-2.18.4-.55.21-.94.47-1.35.88-.41.41-.67.8-.88 1.35-.16.42-.35 1.04-.4 2.18-.06 1.24-.07 1.59-.07 4.74s.01 3.5.07 4.74c.05 1.14.24 1.76.4 2.18.21.55.47.94.88 1.35.41.41.8.67 1.35.88.42.16 1.04.35 2.18.4 1.24.06 1.59.07 4.74.07s3.5-.01 4.74-.07c1.14-.05 1.76-.24 2.18-.4.55-.21.94-.47 1.35-.88.41-.41.67-.8.88-1.35.16-.42.35-1.04.4-2.18.06-1.24.07-1.59.07-4.74s-.01-3.5-.07-4.74c-.05-1.14-.24-1.76-.4-2.18a3.6 3.6 0 0 0-.88-1.35 3.6 3.6 0 0 0-1.35-.88c-.42-.16-1.04-.35-2.18-.4-1.24-.06-1.59-.07-4.74-.07zm0 3.37a5.49 5.49 0 1 1 0 10.98 5.49 5.49 0 0 1 0-10.98zm0 9.05a3.56 3.56 0 1 0 0-7.12 3.56 3.56 0 0 0 0 7.12zm6.99-9.27a1.28 1.28 0 1 1-2.56 0 1.28 1.28 0 0 1 2.56 0z"/></svg>',
    "youtube": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23.5 6.9a3 3 0 0 0-2.12-2.13C19.5 4.25 12 4.25 12 4.25s-7.5 0-9.38.52A3 3 0 0 0 .5 6.9C0 8.79 0 12 0 12s0 3.21.5 5.1a3 3 0 0 0 2.12 2.13c1.88.52 9.38.52 9.38.52s7.5 0 9.38-.52a3 3 0 0 0 2.12-2.13C24 15.21 24 12 24 12s0-3.21-.5-5.1zM9.6 15.6V8.4l6.25 3.6-6.25 3.6z"/></svg>',
}


def social_links(cls="social", onlight=False):
    if onlight:
        cls += " social--onlight"
    return f'''<div class="{cls}">
          <a href="{FACEBOOK}" target="_blank" rel="noopener noreferrer" aria-label="{BIZ} on Facebook" title="Facebook">{SOCIAL_SVG['facebook']}</a>
          <a href="{INSTAGRAM}" target="_blank" rel="noopener noreferrer" aria-label="{BIZ} on Instagram" title="Instagram">{SOCIAL_SVG['instagram']}</a>
          <a href="{YOUTUBE}" target="_blank" rel="noopener noreferrer" aria-label="{BIZ} on YouTube" title="YouTube">{SOCIAL_SVG['youtube']}</a>
        </div>'''


# --------------------------------------------------------------------------
# Structured data
# --------------------------------------------------------------------------
SCHEMA = f'''{{
  "@context": "https://schema.org",
  "@type": ["ProfessionalService", "LocalBusiness"],
  "name": "{BIZ}",
  "description": "Independent nurse patient advocate in Mandan, North Dakota. Board-Certified Patient Advocate helping patients and families navigate appointments, insurance, hospital stays and transitions of care.",
  "url": "{SITE}",
  "telephone": "{PHONE_DISPLAY}",
  "email": "{EMAIL}",
  "image": "{IMG_LOGO}",
  "priceRange": "$150",
  "address": {{
    "@type": "PostalAddress",
    "addressLocality": "Mandan",
    "addressRegion": "ND",
    "postalCode": "58554",
    "addressCountry": "US"
  }},
  "areaServed": [
    {{"@type": "State", "name": "North Dakota"}},
    {{"@type": "City", "name": "Bismarck"}},
    {{"@type": "City", "name": "Mandan"}}
  ],
  "openingHoursSpecification": {{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "08:00",
    "closes": "17:00"
  }},
  "founder": {{
    "@type": "Person",
    "name": "Laurie Boeshans",
    "jobTitle": "Board-Certified Patient Advocate, LPN",
    "hasCredential": ["Board-Certified Patient Advocate (BCPA)", "Licensed Practical Nurse"]
  }},
  "sameAs": ["{FACEBOOK}", "{INSTAGRAM}", "{YOUTUBE}"]
}}'''


# --------------------------------------------------------------------------
# Shell
# --------------------------------------------------------------------------
def head(title, desc, page):
    nav_html = ""
    for href, label in NAV:
        cur = ' aria-current="page"' if href == page else ""
        nav_html += f'            <li><a class="site-nav__link" href="{href}"{cur}>{label}</a></li>\n'

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Laurie Boeshans, BCPA, LPN">
<link rel="canonical" href="{SITE}/{'' if page == 'index.html' else page}">

<meta property="og:type" content="website">
<meta property="og:site_name" content="{BIZ}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/{'' if page == 'index.html' else page}">
<meta property="og:image" content="{IMG_HERO}">
<meta name="twitter:card" content="summary_large_image">

<link rel="icon" href="{IMG_LOGO}">
<link rel="apple-touch-icon" href="{IMG_LOGO}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">

<script type="application/ld+json">{SCHEMA}</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>

<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="index.html" aria-label="{BIZ} — home">
      <img class="brand__mark" src="{IMG_LOGO}" alt="" data-fallback-hide>
      <span class="brand__text">
        <span class="brand__name">Dakota Patient Advocate Solutions</span>
        <span class="brand__tag">Mandan, North Dakota</span>
      </span>
    </a>

    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">
      <span class="nav-toggle__bars" aria-hidden="true"><span></span><span></span><span></span></span>
      <span class="nav-toggle__label">Menu</span>
    </button>

    <nav class="site-nav" id="site-nav" aria-label="Main">
      <ul class="site-nav__list">
{nav_html}      </ul>
      <a class="btn btn--primary btn--sm" href="contact.html">Free 15-Minute Call</a>
    </nav>
  </div>
</header>

<main id="main">
'''


def footer():
    return f'''</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        <div class="footer-brand__name">Dakota Patient Advocate Solutions</div>
        <p>Independent nurse patient advocacy for North Dakota families. Board-Certified. Never paid by a hospital, clinic, or insurance company &mdash; only by you.</p>
        {social_links()}
      </div>

      <div>
        <h4>Explore</h4>
        <ul class="footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="what-is-an-advocate.html">What Is an Advocate</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="pricing.html">Pricing</a></li>
        </ul>
      </div>

      <div>
        <h4>More</h4>
        <ul class="footer-links">
          <li><a href="about.html">About Laurie</a></li>
          <li><a href="videos.html">Videos</a></li>
          <li><a href="contact.html">Contact</a></li>
          <li><a href="contact.html#faq">Questions</a></li>
        </ul>
      </div>

      <div>
        <h4>Get in touch</h4>
        <ul class="footer-links">
          <li><a href="tel:{PHONE_LINK}">{PHONE_DISPLAY}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{CITY}</li>
          <li>{HOURS}</li>
        </ul>
      </div>
    </div>

    <p class="footer-disclaimer">
      <strong>Please note:</strong> {BIZ} provides independent patient advocacy and healthcare navigation support.
      Laurie Boeshans is a Licensed Practical Nurse, and advocacy services are not medical care, legal advice, or a
      substitute for the advice of your physician or attorney. No advocate can guarantee a particular medical,
      insurance, or billing outcome. Independent advocacy services are generally not covered by Medicare or private
      health insurance and are paid privately by the client.
    </p>

    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> {BIZ}. All rights reserved.</span>
      <span>Mandan, ND &middot; Serving all of North Dakota, in person and virtually</span>
    </div>
  </div>
</footer>

<script src="assets/js/main.js"></script>
</body>
</html>
'''


def write(page, title, desc, body):
    html = head(title, desc, page) + body + footer()
    with open(os.path.join(OUT, page), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  wrote {page}  ({len(html):,} bytes)")


# --------------------------------------------------------------------------
# Shared partials
# --------------------------------------------------------------------------
TRUSTBAR = f'''<section class="trustbar">
  <div class="wrap">
    <ul class="trustbar__list">
      <li>{icon('check-badge')} Board-Certified Patient Advocate (BCPA)</li>
      <li>{icon('heart')} Licensed Practical Nurse since 2001</li>
      <li>{icon('shield')} Independent &mdash; paid only by you</li>
      <li>{icon('pin')} All of North Dakota &middot; in person or virtual</li>
    </ul>
  </div>
</section>
'''


def cta_band(title="Let's start with a conversation.",
             text="A free 15&ndash;30 minute call costs nothing and there's no obligation. Tell me what's going on, and I'll tell you honestly whether I can help."):
    return f'''<section class="cta-band">
  <div class="wrap">
    <h2>{title}</h2>
    <p>{text}</p>
    <div class="btn-row">
      <a class="btn btn--light" href="contact.html">Request your free call</a>
      <a class="btn btn--outline-light" href="tel:{PHONE_LINK}">Call {PHONE_DISPLAY}</a>
    </div>
  </div>
</section>
'''


def page_hero(eyebrow, title, lede, crumb):
    return f'''<section class="page-hero">
  <div class="wrap">
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">Home</a> &nbsp;/&nbsp; {crumb}</nav>
    <p class="eyebrow">{eyebrow}</p>
    <h1>{title}</h1>
    <p class="lede">{lede}</p>
  </div>
</section>
'''


CREDS = f'''<section class="section section--tight section--sand">
  <div class="wrap center">
    <p class="eyebrow">Credentials &amp; memberships</p>
    <div class="creds reveal">
      <figure>
        <img src="{IMG_PACB}" alt="Patient Advocate Certification Board logo" loading="lazy">
        <figcaption>Board-Certified Patient Advocate (BCPA), certified 2025 by the Patient Advocate Certification Board</figcaption>
      </figure>
      <figure>
        <img src="{IMG_GNA}" alt="Greater National Advocates member badge" loading="lazy">
        <figcaption>Member, Greater National Advocates</figcaption>
      </figure>
      <figure>
        <div class="creds__mark">{icon('heart')}</div>
        <figcaption>Licensed Practical Nurse in good standing since 2001 &mdash; 24+ years of clinical practice</figcaption>
      </figure>
    </div>
  </div>
</section>
'''

# ==========================================================================
# PAGE 1 — HOME
# ==========================================================================
SERVICES_SHORT = [
    ("calendar", "Appointments &amp; Care Coordination",
     "I go with you to appointments, help you prepare the questions that matter, take notes, and make sure your concerns are actually heard &mdash; then keep every provider on the same page afterward."),
    ("receipt", "Billing &amp; Insurance Help",
     "Medication prior authorizations, confusing statements, and denied claims. I review the paperwork, find the error or the argument, and write the appeal."),
    ("home", "Transitions of Care",
     "Searching for assisted living, memory care, or a nursing home, then coordinating the move so nothing &mdash; medications, records, or dignity &mdash; gets lost along the way."),
    ("compass", "New Diagnosis Support",
     "A new diagnosis arrives with a wall of information and very little time. I translate it into plain language and help you think through the next step."),
    ("shield", "Hospital Advocacy &amp; Discharge Planning",
     "Someone at the bedside asking the right questions, and a discharge plan that's genuinely safe &mdash; not just a signature on a form."),
    ("file", "Medical Records &amp; Review",
     "Gathering, organizing, and reviewing scattered records so you and your providers finally have the whole picture in one place."),
]

home_cards = "\n".join(
    f'''      <article class="card card--link reveal">
        <div class="card__icon">{icon(ic)}</div>
        <h3>{t}</h3>
        <p>{d}</p>
      </article>''' for ic, t, d in SERVICES_SHORT)

HOME = f'''<section class="hero">
  <div class="wrap hero__grid">
    <div>
      <p class="eyebrow">Independent nurse patient advocate &middot; Mandan, ND</p>
      <h1 class="hero__title">Empower your <em>healthcare choices.</em></h1>
      <p class="lede">Navigating healthcare shouldn't feel overwhelming. I'm Laurie Boeshans &mdash; a nurse of 24 years and a Board-Certified Patient Advocate. I sit on your side of the table, help connect the puzzle pieces, and bring clarity to the process.</p>
      <div class="btn-row">
        <a class="btn btn--primary" href="contact.html">Book a free 15-minute call</a>
        <a class="btn btn--ghost" href="services.html">See how I can help</a>
      </div>
    </div>
    <div class="hero__media">
      <img src="{IMG_HERO}" alt="Laurie Boeshans, Board-Certified Patient Advocate and Licensed Practical Nurse, serving North Dakota families" fetchpriority="high" width="1200" height="900">
      <div class="hero__badge">
        <strong>24+</strong>
        <span>years of nursing experience behind every conversation</span>
      </div>
    </div>
  </div>
</section>

{TRUSTBAR}

<section class="section">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">Why this exists</p>
      <h2>You shouldn't have to fight the system while you're trying to get well.</h2>
      <p>Appointments run fifteen minutes. Specialists don't talk to each other. Insurance denies a medication with no explanation you can follow. A parent is being discharged tomorrow and no one has said where they're going.</p>
      <p>After more than two decades in cardiology, internal medicine, family practice, and behavioral health, I watched capable, intelligent people leave appointments more confused than when they walked in &mdash; not because they weren't paying attention, but because the system isn't built to be understood.</p>
      <p><strong>That's the gap I fill.</strong> I know how hospitals, clinics, and insurers actually work from the inside, and I use that knowledge entirely on your behalf.</p>
      <a class="textlink" href="about.html">Read more about my background</a>
    </div>
    <div class="split__media reveal">
      <img src="{IMG_FEATURE}" alt="Compassionate patient advocacy support for North Dakota patients and families" loading="lazy" width="1200" height="900">
    </div>
  </div>
</section>

<section class="section section--sand" id="services">
  <div class="wrap">
    <div class="section-head center">
      <p class="eyebrow">How I help</p>
      <h2>Practical support at the moments that matter most</h2>
      <p class="lede">Every engagement is built around what you actually need &mdash; a single appointment, one stubborn insurance denial, or steady support through a long illness.</p>
    </div>
    <div class="grid grid--3">
{home_cards}
    </div>
    <div class="btn-row" style="justify-content:center">
      <a class="btn btn--teal" href="services.html">Explore all services in detail</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center">
      <p class="eyebrow">Who I work with</p>
      <h2>If any of this sounds familiar, we should talk</h2>
    </div>
    <div class="grid grid--4">
      <article class="card reveal"><div class="card__icon">{icon('compass')}</div><h3>Newly diagnosed</h3><p>You've just been handed a diagnosis and a stack of pamphlets, and you don't know which question to ask first.</p></article>
      <article class="card reveal"><div class="card__icon">{icon('users')}</div><h3>Families far from home</h3><p>Your parent is in a Bismarck hospital and you're in another state. You need someone trustworthy in the room.</p></article>
      <article class="card reveal"><div class="card__icon">{icon('heart')}</div><h3>Caregivers running on empty</h3><p>You're managing appointments, medications, and paperwork for someone you love &mdash; on top of your own life.</p></article>
      <article class="card reveal"><div class="card__icon">{icon('receipt')}</div><h3>Anyone facing a denial</h3><p>A claim was rejected or a medication wasn't authorized, and the appeal letter feels written in another language.</p></article>
    </div>
  </div>
</section>

<section class="section section--teal">
  <div class="wrap split split--media-left">
    <div class="split__media reveal">
      <div class="quote">
        &ldquo;When you can't be with your loved one, we provide reliable, compassionate patient advocate support by their side. With years of experience, we help ease anxiety for families and patients alike.&rdquo;
        <cite>Laurie Boeshans, BCPA, LPN &mdash; Founder</cite>
      </div>
    </div>
    <div class="reveal">
      <p class="eyebrow">Independent by design</p>
      <h2>No hospital, clinic, or insurer pays me. You do.</h2>
      <p>That single fact changes everything about the advice you get. Case managers and discharge planners are good people working inside institutions that also employ them. My only obligation is to you.</p>
      <ul class="checklist">
        <li>No referral fees, kickbacks, or facility commissions &mdash; ever</li>
        <li>No pressure toward a particular provider, plan, or placement</li>
        <li>Straight answers, including when the answer is &ldquo;you don't need to hire me for this&rdquo;</li>
        <li>Your information stays confidential and shared only where you direct</li>
      </ul>
      <div class="btn-row"><a class="btn btn--teal" href="what-is-an-advocate.html">What exactly is a patient advocate?</a></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center">
      <p class="eyebrow">How it works</p>
      <h2>Four simple steps</h2>
    </div>
    <div class="steps">
      <div class="step reveal"><div class="step__num">1</div><h3>Free call</h3><p>A no-cost 15&ndash;30 minute conversation so I understand the situation and you can decide if this feels right.</p></div>
      <div class="step reveal"><div class="step__num">2</div><h3>Consultation</h3><p>A focused 60-minute session where we go deep on the details and map out what needs to happen.</p></div>
      <div class="step reveal"><div class="step__num">3</div><h3>A plan you keep</h3><p>You leave with a written plan &mdash; priorities, questions to ask, deadlines, and who is responsible for what.</p></div>
      <div class="step reveal"><div class="step__num">4</div><h3>Support that fits</h3><p>Hire me by the hour or by the package for as much or as little ongoing help as you need.</p></div>
    </div>
    <div class="btn-row" style="justify-content:center"><a class="btn btn--ghost" href="pricing.html">See rates and packages</a></div>
  </div>
</section>

{CREDS}

{cta_band()}

<section class="section section--tight">
  <div class="wrap center">
    <p class="eyebrow">Follow along</p>
    <h2 style="margin-bottom:.4rem">Healthcare, explained in plain language</h2>
    <p class="lede" style="margin-inline:auto">I share short videos and practical tips on navigating appointments, insurance, and hospital stays.</p>
    <div style="margin-top:1.5rem">{social_links("social social--center", onlight=True)}</div>
    <div class="btn-row" style="justify-content:center"><a class="btn btn--ghost" href="videos.html">Watch the video library</a></div>
  </div>
</section>
'''

# ==========================================================================
# PAGE 2 — WHAT IS AN ADVOCATE
# ==========================================================================
ADVOCATE = page_hero(
    "Understanding the role",
    "What is a patient advocate?",
    "A patient advocate is a trained professional you hire to stand beside you inside the healthcare system &mdash; explaining, organizing, questioning, and making sure decisions get made with you rather than around you.",
    "What Is an Advocate") + f'''
<section class="section">
  <div class="wrap wrap-narrow">
    <h2>The short version</h2>
    <p>Think of a patient advocate the way you'd think of an accountant at tax time or a realtor when you're buying a house. The system is navigable &mdash; but it has its own language, its own timelines, and its own rules that nobody hands you in writing. An advocate is someone who already knows those rules and works only for you.</p>
    <p>An <strong>independent</strong> advocate is not employed by a hospital, clinic, insurance company, or care facility. Many hospitals have a &ldquo;patient advocate&rdquo; or ombudsman on staff, and they can be genuinely helpful &mdash; but they are paid by the institution. When your interests and the institution's interests diverge, an independent advocate has no conflict to manage.</p>
    <div class="callout">
      <strong>The distinction that matters</strong>
      I am a <em>nurse</em> advocate. Twenty-four years of clinical practice means I can read the chart, understand the medication list, recognize when something in a care plan doesn't add up, and ask a physician a clinical question in the language they use with each other.
    </div>
  </div>
</section>

<section class="section section--sand">
  <div class="wrap">
    <div class="grid grid--2">
      <div class="card reveal">
        <div class="card__icon">{icon('check-badge')}</div>
        <h3>What a patient advocate does</h3>
        <ul class="checklist">
          <li>Attends appointments with you, in person or virtually, and takes detailed notes</li>
          <li>Prepares the questions you'd otherwise think of in the parking lot afterward</li>
          <li>Translates diagnoses, test results, and treatment options into plain language</li>
          <li>Gathers and organizes medical records scattered across systems</li>
          <li>Coordinates between specialists who aren't talking to each other</li>
          <li>Reviews bills and Explanation of Benefits statements for errors</li>
          <li>Writes and files insurance appeals for denied claims and authorizations</li>
          <li>Advocates at the bedside during a hospital stay and pushes for a safe discharge</li>
          <li>Researches and vets assisted living, memory care, and nursing home options</li>
          <li>Keeps distant family members informed and included</li>
        </ul>
      </div>
      <div class="card card--clay reveal">
        <div class="card__icon">{icon('search')}</div>
        <h3>What a patient advocate does <em>not</em> do</h3>
        <ul class="checklist checklist--cross">
          <li>Diagnose conditions or prescribe medication</li>
          <li>Provide hands-on nursing or personal care in your home</li>
          <li>Replace your physician, nurse practitioner, or care team</li>
          <li>Give legal advice or represent you in court</li>
          <li>Make medical decisions for you &mdash; the decisions stay yours</li>
          <li>Guarantee a specific medical, billing, or insurance outcome</li>
          <li>Accept payment, referral fees, or commissions from any provider or facility</li>
        </ul>
        <p style="margin-top:1.3rem;font-size:.93rem">Where something falls outside my scope, I'll say so plainly and, where I can, point you toward the right professional.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center">
      <p class="eyebrow">Timing</p>
      <h2>When it's worth calling an advocate</h2>
      <p class="lede">You don't need to be in a crisis. Most people call at one of these moments.</p>
    </div>
    <div class="grid grid--3">
      <article class="card reveal"><div class="card__icon">{icon('compass')}</div><h3>A serious new diagnosis</h3><p>Cancer, heart failure, dementia, an autoimmune condition &mdash; anything where the treatment path has real branches and the choices are yours to make.</p></article>
      <article class="card reveal"><div class="card__icon">{icon('shield')}</div><h3>An unplanned hospital stay</h3><p>Especially when discharge is being discussed and the plan sounds faster than it sounds safe.</p></article>
      <article class="card reveal"><div class="card__icon">{icon('receipt')}</div><h3>A denial or a bill that's wrong</h3><p>Prior authorizations, out-of-network surprises, duplicate charges, or an appeal with a deadline attached.</p></article>
      <article class="card reveal"><div class="card__icon">{icon('users')}</div><h3>Caring from a distance</h3><p>You live out of state and need eyes, ears, and a nurse's judgment in the room.</p></article>
      <article class="card reveal"><div class="card__icon">{icon('home')}</div><h3>A move to a care facility</h3><p>Assisted living, memory care, or skilled nursing &mdash; a decision most families make once, under time pressure.</p></article>
      <article class="card reveal"><div class="card__icon">{icon('star')}</div><h3>Nobody is coordinating</h3><p>Four specialists, three portals, two pharmacies, and no single person holding the whole picture.</p></article>
    </div>
  </div>
</section>

<section class="section section--teal">
  <div class="wrap wrap-narrow">
    <div class="section-head center">
      <p class="eyebrow">Common questions</p>
      <h2>Questions people ask first</h2>
    </div>
    <div class="faq">
      <details>
        <summary>Isn't this what the hospital's case manager is for?</summary>
        <div><p>Case managers and discharge planners do important work, and I collaborate with them respectfully. The difference is who employs them. Their role includes managing length of stay and institutional priorities alongside your care. I have one client in the room: you.</p></div>
      </details>
      <details>
        <summary>Will my doctor be offended if I bring an advocate?</summary>
        <div><p>In my experience, the opposite. Clinicians generally welcome a prepared patient with organized records and clear questions &mdash; it makes a fifteen-minute appointment far more productive. I'm there to support the relationship with your care team, not to fight it.</p></div>
      </details>
      <details>
        <summary>Does insurance or Medicare pay for a patient advocate?</summary>
        <div><p>Generally, no. Independent advocacy is a private-pay service. Some people use HSA or FSA funds &mdash; check with your plan administrator, as eligibility varies. Many families find the cost is offset by billing errors caught or denials overturned, but I never promise that as an outcome.</p></div>
      </details>
      <details>
        <summary>What does &ldquo;Board-Certified&rdquo; actually mean?</summary>
        <div><p>The BCPA credential is awarded by the Patient Advocate Certification Board, an independent body. It requires documented professional experience, a qualifying education background, passing a national examination, and adherence to a published code of ethics with ongoing continuing education. It is currently the only nationally recognized certification for the profession.</p></div>
      </details>
      <details>
        <summary>Do you have to be local to work with you?</summary>
        <div><p>No. I attend appointments and hospital visits in person throughout the Bismarck&ndash;Mandan area and travel elsewhere in North Dakota by arrangement. Records review, insurance appeals, research, and family coordination all work well virtually, so I support clients across the state and their families anywhere.</p></div>
      </details>
      <details>
        <summary>Is what I tell you confidential?</summary>
        <div><p>Yes. Your information is kept confidential and is shared only with the people and organizations you specifically authorize in writing. That authorization is part of the paperwork we complete before any work begins.</p></div>
      </details>
    </div>
  </div>
</section>

{cta_band("Still not sure whether you need an advocate?",
          "That's exactly what the free call is for. If your situation doesn't call for paid help, I'll tell you that &mdash; and point you somewhere useful instead.")}
'''

# ==========================================================================
# PAGE 3 — SERVICES
# ==========================================================================
SERVICE_DETAIL = [
    ("Care navigation", "calendar", "Appointments &amp; Care Coordination",
     "The fifteen-minute appointment is where most healthcare actually happens &mdash; and it's where the most gets lost. I make sure it counts.",
     ["Pre-appointment preparation: we build the list of questions together, in priority order",
      "Attendance in person or by phone/video, with detailed notes you keep",
      "Real-time clarification &mdash; I ask the follow-up question when an answer isn't clear",
      "A written summary after each visit: what was decided, what changes, what happens next",
      "Coordination between primary care and specialists so nobody is working from stale information",
      "Medication list reconciliation across every prescriber and pharmacy",
      "Tracking referrals, orders, and test results that would otherwise fall through"]),
    ("Coverage &amp; cost", "receipt", "Billing &amp; Insurance Help",
     "Denials and billing errors are common, and they are frequently reversible &mdash; if someone knows what to look for and files inside the deadline.",
     ["Medication prior authorization requests and follow-through with the prescriber's office",
      "Line-by-line review of itemized bills and Explanation of Benefits statements",
      "Identifying duplicate charges, coding errors, and services never rendered",
      "Preparing and submitting written appeals for denied claims and denied authorizations",
      "Escalating to peer-to-peer review, external review, or the state insurance department where appropriate",
      "Explaining deductibles, coinsurance, out-of-pocket maximums, and network rules in plain numbers",
      "Locating manufacturer assistance programs, foundation grants, and charity care applications"]),
    ("Placement", "home", "Transitions of Care",
     "Moving a parent into assisted living, memory care, or a nursing home is a decision most families make exactly once &mdash; usually with a deadline attached.",
     ["Clarifying the actual level of care needed, clinically, before touring anything",
      "Researching and shortlisting facilities that match the need, budget, and location",
      "Reviewing state survey results, staffing data, and inspection history",
      "Preparing the questions to ask on a tour that admissions staff aren't expecting",
      "Coordinating the transfer of records, medications, and equipment on move day",
      "Following up in the first weeks to confirm the care plan is being followed",
      "Supporting the family conversation when siblings don't agree"]),
    ("Understanding", "compass", "New Diagnosis Support",
     "A new diagnosis arrives with a wall of information and almost no time to absorb it. My job is to slow it down and make it make sense.",
     ["Plain-language explanation of the diagnosis, staging or severity, and prognosis language",
      "Walking through treatment options, including the trade-offs nobody has time to describe",
      "Helping you decide whether a second opinion is worth pursuing, and arranging it if so",
      "Vetting the information you've found online &mdash; what's credible, what isn't",
      "Preparing you for the next specialist visit so you arrive informed rather than overwhelmed",
      "Connecting you with disease-specific support organizations and resources",
      "Helping you articulate your own goals of care, so treatment decisions reflect what you want"]),
    ("At the bedside", "shield", "Hospital Advocacy &amp; Discharge Planning",
     "Hospitals are fast, fragmented, and staffed in shifts. Someone needs to be tracking the whole story &mdash; and asking whether tomorrow's discharge is genuinely safe.",
     ["Bedside presence during rounds, with the right clinical questions asked in the moment",
      "Daily updates to family members who can't be there, including those out of state",
      "Monitoring for medication changes, new orders, and gaps between shifts",
      "Reviewing the proposed discharge plan against the reality of the home situation",
      "Confirming equipment, home health, therapy, and follow-up appointments are truly in place before discharge",
      "Support in appealing a discharge you believe is premature",
      "Post-discharge follow-up in the first days, when readmissions most often happen"]),
    ("Specialty", "file", "Medical Records &amp; Specialty Services",
     "Standalone projects for people who need one specific thing done thoroughly, rather than ongoing support.",
     ["Requesting, gathering, and organizing records from multiple health systems into one file",
      "Chronological medical summary &mdash; a single document your providers can actually read",
      "Focused medical records review with a written summary of findings and questions",
      "Insurance billing audit for a single episode of care or a full year",
      "Standalone appeal preparation for one denied claim or authorization",
      "Preparation support ahead of a scheduled surgery or procedure",
      "Second-opinion coordination, including assembling the packet the new physician needs"]),
]

svc_blocks = ""
for tag, ic, title, intro, bullets in SERVICE_DETAIL:
    lis = "\n".join(f"        <li>{b}</li>" for b in bullets)
    svc_blocks += f'''  <div class="service-block reveal">
    <div class="service-block__aside">
      <span class="service-block__tag">{tag}</span>
      <div class="card__icon">{icon(ic)}</div>
      <h3>{title}</h3>
    </div>
    <div>
      <p class="lede" style="font-size:1.05rem;color:var(--text)">{intro}</p>
      <ul class="checklist">
{lis}
      </ul>
    </div>
  </div>
'''

SERVICES = page_hero(
    "Services",
    "Support built around your situation",
    "Some clients need one hour to untangle a single insurance denial. Others need someone alongside them for months. Every engagement starts the same way &mdash; with a free call &mdash; and is shaped entirely by what's actually in front of you.",
    "Services") + f'''
<section class="section">
  <div class="wrap">
{svc_blocks}  </div>
</section>

<section class="section section--sand">
  <div class="wrap">
    <div class="grid grid--3">
      <div class="card reveal">
        <div class="card__icon">{icon('pin')}</div>
        <h3>Where I work</h3>
        <p>In-person advocacy throughout the Bismarck&ndash;Mandan area, including hospitals, clinics, and care facilities. Travel elsewhere in North Dakota by arrangement.</p>
      </div>
      <div class="card reveal">
        <div class="card__icon">{icon('play')}</div>
        <h3>Virtual support</h3>
        <p>Records review, appeals, research, telehealth attendance, and family coordination work just as well by phone or video &mdash; anywhere in the state, for families anywhere.</p>
      </div>
      <div class="card reveal">
        <div class="card__icon">{icon('clock')}</div>
        <h3>Response times</h3>
        <p>Inquiries answered within one business day. Hospital and urgent situations are prioritized &mdash; call directly at <a href="tel:{PHONE_LINK}">{PHONE_DISPLAY}</a> when time matters.</p>
      </div>
    </div>
    <div class="callout" style="margin-top:2rem">
      <strong>Not sure which of these you need?</strong>
      Most people aren't &mdash; that's normal. Describe the situation on a free call and I'll tell you which of these actually applies, roughly how much time it's likely to take, and whether it's something you could reasonably handle yourself.
    </div>
  </div>
</section>

{cta_band("Tell me what's going on.",
          "The first call is free and there's no obligation. Fifteen minutes is usually enough for me to tell you whether I can help and what it would take.")}
'''

# ==========================================================================
# PAGE 4 — PRICING
# ==========================================================================
PRICING = page_hero(
    "Pricing",
    "Clear rates, no surprises",
    "Independent advocacy is a private-pay service, so you should know exactly what it costs before you commit to anything. Nothing here is billed without your approval first.",
    "Pricing") + f'''
<section class="section">
  <div class="wrap">
    <div class="price-grid">
      <div class="price-card reveal">
        <h3>Free Initial Call</h3>
        <div class="price-card__amount">$0</div>
        <p class="price-card__meta">15&ndash;30 minutes &middot; phone or video</p>
        <ul>
          <li>Describe what's happening in your own words</li>
          <li>My honest read on whether advocacy helps here</li>
          <li>A rough sense of the time it would take</li>
          <li>No obligation and no sales pressure</li>
        </ul>
        <a class="btn btn--ghost" href="contact.html">Request a call</a>
      </div>

      <div class="price-card price-card--featured reveal">
        <span class="price-card__flag">Most people start here</span>
        <h3>Initial Consultation</h3>
        <div class="price-card__amount">$150</div>
        <p class="price-card__meta">60 minutes &middot; in person, phone, or video</p>
        <ul>
          <li>A full review of the medical and insurance situation</li>
          <li>Records and documents you've collected, gone through together</li>
          <li>A written action plan with priorities and deadlines</li>
          <li>Questions prepared for your next appointment</li>
          <li>Clear recommendation on what, if anything, comes next</li>
        </ul>
        <a class="btn btn--primary" href="contact.html">Book a consultation</a>
      </div>

      <div class="price-card reveal">
        <h3>Ongoing Advocacy</h3>
        <div class="price-card__amount">$150<small> / hour</small></div>
        <p class="price-card__meta">Billed in quarter-hour increments</p>
        <ul>
          <li>Appointment and hospital attendance</li>
          <li>Insurance appeals and billing review</li>
          <li>Records gathering, research, and calls on your behalf</li>
          <li>Family updates and care coordination</li>
          <li>Discounted rates available through packages below</li>
        </ul>
        <a class="btn btn--teal" href="contact.html">Get started</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--sand">
  <div class="wrap wrap-narrow">
    <div class="section-head">
      <p class="eyebrow">Packages</p>
      <h2>Support packages for longer situations</h2>
      <p class="lede">When you know the road ahead is longer than an hour or two, a package keeps things simple. Hours are drawn down as they're used, across any of the services offered.</p>
    </div>
    <table class="rate-table">
      <caption class="sr-only">Support package pricing</caption>
      <thead>
        <tr><th scope="col">Package</th><th scope="col">Best for</th><th scope="col">Price</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>3-hour package</strong></td><td>A single appointment series, or one insurance appeal seen through end to end</td><td>$450</td></tr>
        <tr><td><strong>6-hour package</strong></td><td>A new diagnosis workup, or a hospital stay with discharge planning</td><td>$900</td></tr>
        <tr><td><strong>10-hour package</strong></td><td>A facility search and move, or sustained support through a long treatment course</td><td>$1,500</td></tr>
      </tbody>
    </table>
    <p style="margin-top:1.2rem;font-size:.92rem;color:var(--muted)">Package hours never expire during an active engagement, and unused time is refundable if the situation resolves sooner than expected.</p>
  </div>
</section>

<section class="section">
  <div class="wrap wrap-narrow">
    <div class="section-head">
      <p class="eyebrow">The details</p>
      <h2>How billing works</h2>
    </div>
    <div class="faq">
      <details open>
        <summary>Does insurance or Medicare cover this?</summary>
        <div><p>Independent patient advocacy is generally not covered by Medicare, Medicaid, or private health insurance &mdash; it's paid privately, like hiring an accountant or an attorney. Some clients are able to use HSA or FSA funds; eligibility varies by plan, so check with your administrator first. I provide an itemized receipt for any submission you'd like to attempt.</p></div>
      </details>
      <details>
        <summary>What exactly is billable time?</summary>
        <div><p>Time spent working on your behalf: appointments and hospital visits, phone calls with providers and insurers, records review, research, drafting appeals, and family updates. Travel within the Bismarck&ndash;Mandan area is not billed. Longer travel is discussed and agreed in advance. Time is tracked in quarter-hour increments and itemized on every invoice.</p></div>
      </details>
      <details>
        <summary>Will I get a bill I wasn't expecting?</summary>
        <div><p>No. We agree on scope and an estimated range before work begins, and I check in with you before exceeding it. If a situation changes and more time is needed, that's a conversation, not a surprise line item.</p></div>
      </details>
      <details>
        <summary>How and when do I pay?</summary>
        <div><p>Consultations and packages are paid at the time of service. Ongoing hourly work is invoiced on a regular schedule. Payment methods are confirmed when we begin; if cost is a genuine barrier for your situation, say so on the free call and we'll talk honestly about what's workable.</p></div>
      </details>
      <details>
        <summary>Is the cost worth it?</summary>
        <div><p>Sometimes an advocate catches a billing error or overturns a denial that more than covers the fee &mdash; but I won't promise that, because no one honestly can. What I will say is this: on the free call, if I don't think paid advocacy will meaningfully change your situation, I'll tell you so.</p></div>
      </details>
    </div>

    <div class="callout callout--warn" style="margin-top:2rem">
      <strong>A note on outcomes</strong>
      No patient advocate can guarantee a medical result, an approved claim, or a specific placement. What I can commit to is thorough preparation, persistent follow-through, and honest communication about where things stand.
    </div>
  </div>
</section>

{cta_band("Start with the free call &mdash; not the invoice.",
          "There's no cost to find out whether this makes sense for your situation.")}
'''

# ==========================================================================
# PAGE 5 — ABOUT
# ==========================================================================
ABOUT = page_hero(
    "About",
    "Meet Laurie Boeshans, BCPA, LPN",
    "Twenty-four years of nursing, and a conviction that no one should have to face the healthcare system alone.",
    "About Laurie") + f'''
<section class="section">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">My story</p>
      <h2>I kept watching the same thing happen.</h2>
      <p>I've been a Licensed Practical Nurse since 2001. Over more than two decades I've worked in cardiology, internal medicine, family practice, and behavioral health, in hospitals, clinics, and nursing homes, caring for patients from newborns to the very end of life.</p>
      <p>And in all of those settings, I kept seeing the same thing: capable, intelligent people leaving an appointment more confused than when they arrived. Families making enormous decisions with a fraction of the information they needed. Patients giving up on a medication because an insurance denial letter was too dense to fight.</p>
      <p>None of that was anyone's fault. It's what happens when a system built out of separate institutions asks a person in the middle of the worst week of their life to coordinate it.</p>
      <p>So I built <strong>Dakota Patient Advocate Solutions</strong> &mdash; an independent practice where the whole job is to be on the patient's side of the table. In 2025 I earned the Board-Certified Patient Advocate credential to hold that work to a national professional standard.</p>
      <p>I'm proud that it's a North Dakota practice, serving neighbors in the community where I've built my life.</p>
    </div>
    <div class="split__media reveal">
      <img src="{IMG_HERO}" alt="Laurie Boeshans, BCPA, LPN, founder of Dakota Patient Advocate Solutions" loading="lazy" width="1200" height="900">
    </div>
  </div>
</section>

<section class="section section--sand">
  <div class="wrap">
    <div class="grid grid--3">
      <div class="card reveal">
        <div class="card__icon">{icon('check-badge')}</div>
        <h3>Credentials</h3>
        <ul class="checklist">
          <li>Board-Certified Patient Advocate (BCPA), 2025</li>
          <li>Licensed Practical Nurse, licensed since 2001</li>
          <li>Member, Greater National Advocates</li>
          <li>Ongoing continuing education in healthcare policy and advocacy practice</li>
        </ul>
      </div>
      <div class="card reveal">
        <div class="card__icon">{icon('file')}</div>
        <h3>Education</h3>
        <ul class="checklist">
          <li>Saint Paul College &mdash; Practical Nursing program, 2001</li>
          <li>Bismarck State College &mdash; A.S., Pre-Nursing, 1996</li>
          <li>Regular participation in national advocacy webinars and workshops</li>
        </ul>
      </div>
      <div class="card reveal">
        <div class="card__icon">{icon('heart')}</div>
        <h3>Clinical background</h3>
        <ul class="checklist">
          <li>Cardiology and internal medicine</li>
          <li>Family practice</li>
          <li>Behavioral health</li>
          <li>Hospital, clinic, and long-term care settings</li>
          <li>Patients from newborn through geriatric care</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap wrap-narrow">
    <div class="section-head">
      <p class="eyebrow">How I work</p>
      <h2>What you can expect from me</h2>
    </div>
    <div class="grid grid--2">
      <div class="card reveal"><h3>Plain language, always</h3><p>If I use a clinical term, I'll explain it. If I don't know something, I'll say so and find out rather than guess.</p></div>
      <div class="card reveal"><h3>You make the decisions</h3><p>My role is to make sure you're deciding with complete information &mdash; not to decide for you, and not to steer you toward what I'd choose.</p></div>
      <div class="card reveal"><h3>Prepared, every time</h3><p>I read the records before the appointment. I know the medication list. I arrive with the questions written down.</p></div>
      <div class="card reveal"><h3>Respectful of your care team</h3><p>I work alongside your providers, not against them. Good advocacy usually makes their job easier, too.</p></div>
    </div>

    <div class="quote reveal" style="margin-top:2.5rem">
      &ldquo;Navigating healthcare shouldn't feel overwhelming. I help connect the puzzle pieces and bring clarity to the process.&rdquo;
      <cite>Laurie Boeshans, BCPA, LPN</cite>
    </div>
  </div>
</section>

{CREDS}

{cta_band("I'd like to hear what you're facing.",
          "Start with a free 15-minute call. No cost, no obligation &mdash; just a conversation with a nurse who knows the system.")}
'''

# ==========================================================================
# PAGE 6 — VIDEOS
# ==========================================================================
VIDEOS = page_hero(
    "Video library",
    "Patient advocacy, in my own words",
    "Short, practical videos on navigating appointments, insurance, hospital stays, and the decisions that come with a new diagnosis. Helping people navigate their healthcare journey &mdash; sharing in my own words.",
    "Videos") + f'''
<section class="section">
  <div class="wrap">
    <div class="video-frame reveal">
      <iframe
        src="https://www.youtube-nocookie.com/embed/videoseries?list={YT_UPLOADS}&amp;rel=0"
        title="Dakota Patient Advocate Solutions video library"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerpolicy="strict-origin-when-cross-origin"
        allowfullscreen
        loading="lazy"></iframe>
    </div>
    <div class="btn-row" style="justify-content:center">
      <a class="btn btn--primary" href="{YOUTUBE}" target="_blank" rel="noopener noreferrer">Watch on YouTube</a>
      <a class="btn btn--ghost" href="{YOUTUBE}?sub_confirmation=1" target="_blank" rel="noopener noreferrer">Subscribe to the channel</a>
    </div>
    <p class="form-note center" style="margin-top:1rem">Videos play newest first. Use the playlist icon in the top corner of the player to browse everything.</p>
  </div>
</section>

<section class="section section--sand">
  <div class="wrap">
    <div class="section-head center">
      <p class="eyebrow">What I cover</p>
      <h2>Topics you'll find on the channel</h2>
    </div>
    <div class="grid grid--3">
      <article class="card reveal"><div class="card__icon">{icon('calendar')}</div><h3>Getting more from an appointment</h3><p>How to prepare, what to bring, and the questions that change the conversation with your doctor.</p></article>
      <article class="card reveal"><div class="card__icon">{icon('receipt')}</div><h3>Insurance, decoded</h3><p>Prior authorizations, denials, appeals, and how to read an Explanation of Benefits without a headache.</p></article>
      <article class="card reveal"><div class="card__icon">{icon('shield')}</div><h3>Hospital stays</h3><p>What to watch for, who to ask, and how to know whether a discharge plan is actually safe.</p></article>
      <article class="card reveal"><div class="card__icon">{icon('compass')}</div><h3>After a new diagnosis</h3><p>Slowing down the first few weeks, and deciding whether a second opinion is worth pursuing.</p></article>
      <article class="card reveal"><div class="card__icon">{icon('users')}</div><h3>Caregiving from a distance</h3><p>Staying informed and useful when you can't be in the room.</p></article>
      <article class="card reveal"><div class="card__icon">{icon('home')}</div><h3>Care transitions</h3><p>Assisted living, memory care, and nursing homes &mdash; what to ask before you choose.</p></article>
    </div>
  </div>
</section>

<section class="section section--tight center">
  <div class="wrap">
    <p class="eyebrow">Follow along</p>
    <h2 style="margin-bottom:1.2rem">New videos and tips, shared regularly</h2>
    {social_links("social social--center", onlight=True)}
  </div>
</section>

{cta_band("Have a question the videos don't answer?",
          "Ask it directly. The first call is free and there's no obligation.")}
'''

# ==========================================================================
# PAGE 7 — CONTACT
# ==========================================================================
CONTACT = page_hero(
    "Contact",
    "Let's talk about what you're facing",
    "The first conversation is free, lasts 15&ndash;30 minutes, and carries no obligation. Call, email, or send the form below &mdash; I answer every inquiry within one business day.",
    "Contact") + f'''
<section class="section">
  <div class="wrap contact-grid">
    <div class="reveal">
      <h2>Reach me directly</h2>
      <ul class="contact-list" style="margin-top:1.6rem">
        <li>
          <span class="contact-list__icon">{icon('phone')}</span>
          <div><dl style="margin:0"><dt>Phone</dt><dd><a href="tel:{PHONE_LINK}">{PHONE_DISPLAY}</a><small>Best for urgent hospital or discharge situations</small></dd></dl></div>
        </li>
        <li>
          <span class="contact-list__icon">{icon('mail')}</span>
          <div><dl style="margin:0"><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a><small>Answered within one business day</small></dd></dl></div>
        </li>
        <li>
          <span class="contact-list__icon">{icon('pin')}</span>
          <div><dl style="margin:0"><dt>Based in</dt><dd>{CITY}<small>Serving Bismarck&ndash;Mandan in person and all of North Dakota virtually</small></dd></dl></div>
        </li>
        <li>
          <span class="contact-list__icon">{icon('clock')}</span>
          <div><dl style="margin:0"><dt>Office hours</dt><dd>{HOURS}<small>Hospital situations accommodated outside these hours by arrangement</small></dd></dl></div>
        </li>
      </ul>

      <div style="margin-top:2rem">
        <h3 style="font-size:1.05rem">Follow along</h3>
        {social_links(onlight=True)}
      </div>

      <div class="callout" style="margin-top:2rem">
        <strong>If this is a medical emergency</strong>
        Call 911 or go to your nearest emergency department. Patient advocacy is not emergency care, and this form is not monitored around the clock.
      </div>
    </div>

    <div class="form-card reveal">
      <h2 style="font-size:1.5rem">Request your free call</h2>
      <p style="color:var(--muted);font-size:.95rem">Tell me a little about the situation and I'll get back to you within one business day.</p>

      <form id="contact-form" data-mode="mailto" novalidate>
        <div class="hp" aria-hidden="true"><label>Leave this field empty<input type="text" name="company" tabindex="-1" autocomplete="off"></label></div>

        <div class="field-row">
          <div class="field">
            <label for="name">Your name <span class="req" aria-hidden="true">*</span></label>
            <input type="text" id="name" name="name" required autocomplete="name">
          </div>
          <div class="field">
            <label for="phone">Phone <span class="req" aria-hidden="true">*</span></label>
            <input type="tel" id="phone" name="phone" required autocomplete="tel">
          </div>
        </div>

        <div class="field">
          <label for="email">Email</label>
          <input type="email" id="email" name="email" autocomplete="email">
        </div>

        <div class="field">
          <label for="topic">What do you need help with?</label>
          <select id="topic" name="topic">
            <option value="">Select one &mdash; or leave blank</option>
            <option>Appointments &amp; care coordination</option>
            <option>Billing or insurance denial</option>
            <option>A hospital stay or discharge</option>
            <option>A new diagnosis</option>
            <option>Assisted living / nursing home search</option>
            <option>Medical records review</option>
            <option>Something else / not sure yet</option>
          </select>
        </div>

        <div class="field">
          <label for="preferred">Preferred way to be contacted</label>
          <select id="preferred" name="preferred">
            <option>Phone call</option>
            <option>Text message</option>
            <option>Email</option>
          </select>
        </div>

        <div class="field">
          <label for="message">Tell me what's going on <span class="req" aria-hidden="true">*</span></label>
          <textarea id="message" name="message" required placeholder="A few sentences is plenty. Please don't include sensitive medical details in this form &mdash; we'll cover those securely on the call."></textarea>
        </div>

        <button class="btn btn--primary" type="submit" style="width:100%">Send my request</button>
        <p class="form-note" id="form-status" role="status" aria-live="polite">Your message goes straight to Laurie. Prefer to talk now? Call <a href="tel:{PHONE_LINK}">{PHONE_DISPLAY}</a>.</p>
      </form>
    </div>
  </div>
</section>

<section class="section section--tight section--sand">
  <div class="wrap">
    <iframe class="map-embed"
      src="https://www.google.com/maps?q=Mandan,%20ND%2058554&amp;output=embed"
      title="Map showing Mandan, North Dakota &mdash; the service area of Dakota Patient Advocate Solutions"
      loading="lazy"
      referrerpolicy="no-referrer-when-downgrade"></iframe>
  </div>
</section>

<section class="section" id="faq">
  <div class="wrap wrap-narrow">
    <div class="section-head center">
      <p class="eyebrow">Before you call</p>
      <h2>Questions people ask most</h2>
    </div>
    <div class="faq">
      <details><summary>What happens on the free call?</summary><div><p>You describe the situation in your own words. I ask a few clarifying questions, then tell you honestly whether patient advocacy would help, roughly what it would involve, and what it would cost. If it isn't a fit, I'll say so and point you somewhere more useful. There's no pressure and no follow-up sales sequence.</p></div></details>
      <details><summary>How quickly can you start?</summary><div><p>Usually within a few days for planned work. Hospital and discharge situations are prioritized &mdash; if something is happening now, call {PHONE_DISPLAY} rather than using the form.</p></div></details>
      <details><summary>Can you help if my family member lives here and I don't?</summary><div><p>Yes, and this is one of the most common reasons people call. I attend appointments and hospital visits in person and keep you fully informed wherever you are, with your family member's written authorization.</p></div></details>
      <details><summary>Do you work with people outside Bismarck&ndash;Mandan?</summary><div><p>Yes. Records review, appeals, research, telehealth attendance, and coordination all work virtually anywhere in North Dakota. In-person travel elsewhere in the state is arranged case by case.</p></div></details>
      <details><summary>Is my information kept private?</summary><div><p>Yes. Everything you share is confidential and disclosed only to people and organizations you authorize in writing. Please keep detailed medical information out of the web form &mdash; we'll handle those details securely once we're in touch.</p></div></details>
    </div>
  </div>
</section>
'''

# ==========================================================================
# Build
# ==========================================================================
PAGES = [
    ("index.html",
     f"{BIZ} | North Dakota Patient Advocacy | Empower Your Healthcare Choices",
     "Independent, Board-Certified nurse patient advocate in Mandan, ND. Laurie Boeshans, BCPA, LPN helps North Dakota patients and families navigate appointments, insurance denials, hospital stays, and transitions of care. Free 15-minute consultation.",
     HOME),
    ("what-is-an-advocate.html",
     f"What Is a Patient Advocate? | {BIZ}",
     "What an independent patient advocate does, what they don't do, and when it's worth hiring one. Answers from a Board-Certified nurse advocate serving North Dakota.",
     ADVOCATE),
    ("services.html",
     f"Patient Advocacy Services | {BIZ} | Mandan, ND",
     "Appointment and care coordination, insurance appeals and billing review, hospital advocacy and discharge planning, transitions of care, new diagnosis support, and medical records review across North Dakota.",
     SERVICES),
    ("pricing.html",
     f"Pricing &amp; Packages | {BIZ}",
     "Transparent patient advocacy rates: free 15-minute call, $150 initial consultation, $150 per hour, and 3-, 6-, and 10-hour support packages. No surprise billing.",
     PRICING),
    ("about.html",
     f"About Laurie Boeshans, BCPA, LPN | {BIZ}",
     "Meet Laurie Boeshans, Board-Certified Patient Advocate and Licensed Practical Nurse since 2001, with 24+ years in cardiology, internal medicine, family practice, and behavioral health in North Dakota.",
     ABOUT),
    ("videos.html",
     f"Videos | {BIZ}",
     "Short, practical videos on navigating appointments, insurance, hospital stays, and new diagnoses &mdash; from Board-Certified Patient Advocate Laurie Boeshans.",
     VIDEOS),
    ("contact.html",
     f"Contact | Free Consultation | {BIZ}",
     "Contact Dakota Patient Advocate Solutions in Mandan, ND. Call (701) 319-1700 or request a free 15-minute patient advocacy consultation. Serving all of North Dakota.",
     CONTACT),
]

if __name__ == "__main__":
    print("Building Dakota Patient Advocate Solutions...")
    for page, title, desc, body in PAGES:
        write(page, title, desc, body)

    # sitemap.xml
    urls = "\n".join(
        f"  <url><loc>{SITE}/{'' if p == 'index.html' else p}</loc>"
        f"<changefreq>monthly</changefreq>"
        f"<priority>{'1.0' if p == 'index.html' else '0.8'}</priority></url>"
        for p, _, _, _ in PAGES)
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n'
                f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    print("  wrote sitemap.xml")

    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    print("  wrote robots.txt")

    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
        body = '''<section class="section center">
  <div class="wrap wrap-narrow">
    <p class="eyebrow">Page not found</p>
    <h1>That page seems to have moved.</h1>
    <p class="lede">Let's get you back on track &mdash; or just call and I'll point you the right way.</p>
    <div class="btn-row"><a class="btn btn--primary" href="index.html">Back to home</a><a class="btn btn--ghost" href="contact.html">Contact Laurie</a></div>
  </div>
</section>
'''
        f.write(head("Page Not Found | " + BIZ, "The page you were looking for could not be found.", "404.html") + body + footer())
    print("  wrote 404.html")
    print("Done.")
