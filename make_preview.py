#!/usr/bin/env python3
"""
Bundles all pages into ONE self-contained preview.html so the whole site can be
clicked through in a single file (handy for review / sharing before hosting).
The real deliverable is still the separate .html files.
"""
import os, re
import build as b

OUT = os.path.dirname(os.path.abspath(__file__))
css = open(os.path.join(OUT, "assets/css/style.css"), encoding="utf-8").read()
js = open(os.path.join(OUT, "assets/js/main.js"), encoding="utf-8").read()

def rewrite(html):
    """Turn inter-page links into in-page section switches."""
    for page, _, _, _ in b.PAGES:
        pid = "p-" + page.replace(".html", "")
        html = html.replace(f'href="{page}#', f'href="#{pid}--')
        html = html.replace(f'href="{page}"', f'href="#{pid}"')
    return html

nav_items = "".join(
    f'            <li><a class="site-nav__link" href="#p-{h.replace(".html","")}" data-page="p-{h.replace(".html","")}">{l}</a></li>\n'
    for h, l in b.NAV)

sections = ""
for page, title, desc, body in b.PAGES:
    pid = "p-" + page.replace(".html", "")
    sections += f'<div class="pv-page" id="{pid}" data-title="{title}">\n{rewrite(body)}\n</div>\n'

header = rewrite(b.head("preview", "preview", "index.html"))
header = header.split("<body>", 1)[1].split('<main id="main">')[0]
# swap nav list for data-page version
header = re.sub(r'<ul class="site-nav__list">.*?</ul>',
                '<ul class="site-nav__list">\n' + nav_items + '      </ul>',
                header, flags=re.S)

footer = rewrite(b.footer()).replace("</main>\n", "").replace('<script src="assets/js/main.js"></script>', "").replace("</body>\n</html>\n", "")

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Preview — {b.BIZ}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&display=swap" rel="stylesheet">
<style>
{css}

/* --- preview shell only (not part of the real site) --- */
.pv-page {{ display: none; }}
.pv-page.is-active {{ display: block; }}
.pv-note {{
  background: #0F3239; color: #B8CDD1; font-family: var(--font-body);
  font-size: .8rem; text-align: center; padding: .55rem 1rem; line-height: 1.5;
}}
.pv-note strong {{ color: #fff; }}
</style>
</head>
<body>
<div class="pv-note"><strong>Preview mode</strong> &mdash; all 8 pages bundled into one file. Click the menu to move between them. The live site is 8 separate pages.</div>
{header}
<main id="main">
{sections}</main>
{footer}
<script>
{js}
</script>
<script>
(function () {{
  var pages = [].slice.call(document.querySelectorAll('.pv-page'));
  function show(id) {{
    var target = document.getElementById(id) || pages[0];
    pages.forEach(function (p) {{ p.classList.toggle('is-active', p === target); }});
    document.querySelectorAll('.site-nav__link').forEach(function (a) {{
      if (a.getAttribute('href') === '#' + target.id) a.setAttribute('aria-current', 'page');
      else a.removeAttribute('aria-current');
    }});
    document.title = target.getAttribute('data-title');
    target.querySelectorAll('.reveal').forEach(function (e) {{ e.classList.add('is-visible'); }});
    window.scrollTo({{ top: 0, behavior: 'instant' }});
  }}
  document.addEventListener('click', function (e) {{
    var a = e.target.closest('a[href^="#p-"]');
    if (!a) return;
    e.preventDefault();
    show(a.getAttribute('href').slice(1).split('--')[0]);
  }});
  show('p-index');
}})();
</script>
</body>
</html>
'''

with open(os.path.join(OUT, "preview.html"), "w", encoding="utf-8") as f:
    f.write(html)
print(f"wrote preview.html ({len(html):,} bytes)")
