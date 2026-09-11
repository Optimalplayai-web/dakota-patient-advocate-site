/* Dakota Patient Advocate Solutions — site scripts */
(function () {
  'use strict';

  /* ---------- Mobile navigation ---------- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.querySelector('.nav-toggle__label').textContent = open ? 'Close' : 'Menu';
    });

    // Close the menu when a link is chosen
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a') && nav.classList.contains('is-open')) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.querySelector('.nav-toggle__label').textContent = 'Menu';
      }
    });

    // Close on Escape
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.querySelector('.nav-toggle__label').textContent = 'Menu';
        toggle.focus();
      }
    });
  }

  /* ---------- Sticky header shadow ---------- */
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-scrolled', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---------- Reveal on scroll ---------- */
  var revealables = document.querySelectorAll('.reveal');
  if (revealables.length) {
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            io.unobserve(entry.target);
          }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
      revealables.forEach(function (el) { io.observe(el); });
    } else {
      revealables.forEach(function (el) { el.classList.add('is-visible'); });
    }
  }

  /* ---------- Current year in footer ---------- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* ---------- Image fallbacks ----------
     If an image can't load (e.g. it was moved), hide it gracefully instead of
     showing a broken-image icon. Photo areas fall back to a soft panel.
  --------------------------------------- */
  document.querySelectorAll('img[data-fallback-hide]').forEach(function (img) {
    img.addEventListener('error', function () { img.style.display = 'none'; });
  });

  document.querySelectorAll('.hero__media img, .split__media img, .creds img').forEach(function (img) {
    img.addEventListener('error', function () {
      img.style.display = 'none';
      if (img.parentElement) img.parentElement.classList.add('media-fallback');
    });
  });

  /* ---------- Contact form ----------
     Works with no server: composes a pre-filled email in the visitor's mail app.
     To collect submissions automatically instead, see README.md (Formspree /
     Netlify Forms are both one-line swaps).
  ------------------------------------- */
  var form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      if (form.getAttribute('data-mode') !== 'mailto') return; // a real endpoint is configured
      e.preventDefault();

      if (form.querySelector('.hp input').value) return; // honeypot: silently drop bots

      var get = function (name) {
        var el = form.elements[name];
        return el ? el.value.trim() : '';
      };

      var lines = [
        'Name: ' + get('name'),
        'Phone: ' + get('phone'),
        'Email: ' + get('email'),
        'How I can help: ' + get('topic'),
        'Preferred contact: ' + get('preferred'),
        '',
        get('message')
      ];

      var subject = 'Website inquiry — ' + (get('name') || 'New contact');
      var href = 'mailto:dpas.nd@outlook.com'
        + '?subject=' + encodeURIComponent(subject)
        + '&body=' + encodeURIComponent(lines.join('\n'));

      window.location.href = href;

      var status = document.getElementById('form-status');
      if (status) {
        status.textContent = 'Your email app should now be open with your message ready to send. '
          + 'If nothing happened, please email dpas.nd@outlook.com or call (701) 319-1700.';
        status.style.color = '#0E4E58';
      }
    });
  }
})();
