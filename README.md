# Dakota Patient Advocate Solutions — Website

A complete, ready-to-host static website. No build step, no database, no dependencies.
Upload the folder and it works.

---

## What's in the box

| File | Page |
|---|---|
| `index.html` | Home |
| `what-is-an-advocate.html` | What Is a Patient Advocate |
| `services.html` | Services (6 detailed service areas) |
| `pricing.html` | Pricing & packages |
| `about.html` | About Laurie Boeshans |
| `videos.html` | Video library (YouTube channel embed) |
| `contact.html` | Contact + inquiry form + FAQ |
| `404.html` | Friendly "page not found" |
| `assets/css/style.css` | All styling |
| `assets/js/main.js` | Mobile menu, animations, contact form |
| `sitemap.xml`, `robots.txt` | For Google |
| `build.py` | Optional page generator (see "Editing" below) |

---

## Publishing it

Any of these work. **Netlify Drop is the fastest** — about 60 seconds, free.

**Option 1 — Netlify (free, recommended)**

1. Go to <https://app.netlify.com/drop>
2. Drag this whole folder onto the page.
3. It goes live instantly at a temporary address.
4. In Site settings → Domain management, add `dakotapatientadvocatesolutions.com`
   and follow the DNS instructions.

**Option 2 — Traditional web host (GoDaddy, Bluehost, HostGator, etc.)**

Upload everything in this folder — keeping the `assets/` folder intact — into your
hosting account's `public_html` (or `www`) directory using the file manager or FTP.

**Option 3 — GitHub Pages / Cloudflare Pages / Vercel**

Push the folder to a repo and point the service at it. No build command needed;
the publish directory is the root.

> Keep the folder structure exactly as it is. The pages look for
> `assets/css/style.css` and `assets/js/main.js` relative to themselves.

---

## Two things to do after it's live

### 1. Hook up the contact form

Right now the form on `contact.html` opens the visitor's email app with their
message pre-filled and addressed to `dpas.nd@outlook.com`. That works everywhere,
but some people abandon it.

To collect submissions properly instead, use **Formspree** (free tier is plenty):

1. Sign up at <https://formspree.io> and create a form; you'll get an endpoint URL.
2. In `contact.html`, find this line:

   ```html
   <form id="contact-form" data-mode="mailto" novalidate>
   ```

   and replace it with:

   ```html
   <form id="contact-form" action="https://formspree.io/f/YOURCODE" method="POST">
   ```

That's the only change needed — the honeypot spam trap already in the form keeps
working. (If you host on Netlify, you can instead just add `netlify` to that same
tag and submissions appear in your Netlify dashboard.)

### 2. Move the images onto your own host (optional but wise)

The photos and logo currently load from your Squarespace image URLs, so the site
looks identical to what you have today. **If you ever cancel Squarespace, those
images will stop loading.**

To make the site fully self-contained:

1. Save the images from your current site into `assets/img/`.
2. In `build.py`, change the five `IMG_` variables near the top to local paths,
   e.g. `IMG_HERO = "assets/img/hero.jpg"`.
3. Run `python3 build.py` to regenerate the pages.

Or just find-and-replace the `https://images.squarespace-cdn.com/...` URLs in the
HTML files directly. The pages already degrade gracefully — if an image can't
load, a soft colored panel appears instead of a broken-image icon.

---

## Editing the site

**For small text changes,** open the `.html` file in any text editor and edit
directly. Each page is standalone and readable.

**For anything that repeats across pages** (the navigation, footer, phone number,
social links, disclaimer), edit `build.py` instead and run:

```bash
python3 build.py
```

That regenerates all eight HTML pages with your changes applied consistently.
Everything is defined near the top of that file — phone number, email, hours,
social URLs, image URLs, and the nav menu.

Colors and fonts all live in the `:root` block at the top of
`assets/css/style.css`.

---

## What's already handled

- **Responsive** — tested at desktop, tablet, and phone widths
- **Accessible** — skip link, keyboard navigation, visible focus rings, ARIA
  labels on the menu and social icons, real semantic headings
- **SEO** — unique title and description per page, Open Graph tags for link
  previews, canonical URLs, `sitemap.xml`, `robots.txt`
- **Local business schema** (JSON-LD) — helps Google show your hours, phone,
  service area, and credentials in search results
- **Social links** — Facebook, Instagram, and YouTube in the footer of every page,
  plus on the home, videos, and contact pages
- **Video page** — embeds your YouTube channel's uploads playlist, so new videos
  appear automatically without touching the site
- **Legal disclaimer** in the footer covering scope of practice, no guaranteed
  outcomes, and the private-pay nature of advocacy

---

## A note on the copy

The text was written from the content on your current site, your Greater National
Advocates profile, and your Chamber listing. Please read it through before going
live — particularly:

- The **"Response times"** and **"How quickly can you start?"** claims (one business
  day) — change these if that's not a promise you want to make.
- The **billing details** on `pricing.html` (quarter-hour increments, travel not
  billed within Bismarck–Mandan, unused package hours refundable). These are
  reasonable industry norms, but they should match how you actually work.
- **Office hours** are set to Monday–Friday, 8:00 am – 5:00 pm CT, from your
  Chamber listing.

Anything that isn't right is a quick text edit — or tell me and I'll change it.
