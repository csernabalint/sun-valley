import os
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ROOT_INDEX = REPO_ROOT / "index.html"

def generate_html():
    return """<!DOCTYPE html>
<html lang="hu" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sun Valley Zrt. – Ipari Sütésálló Gyümölcstöltelékek & Élelmiszer-technológia</title>
  <meta name="description" content="A Sun Valley Zrt. nagyüzemi sütésálló gyümölcstöltelékek, kenhető készítmények és egyedi receptúrák gyártója ipari pékségek és nagykereskedők számára. Móri üzem, AA+ bonitás.">

  <!-- Open Graph / Social Sharing -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://csernabalint.github.io/sun-valley/">
  <meta property="og:title" content="Sun Valley Zrt. – Ipari Sütésálló Gyümölcstöltelékek & Élelmiszer-technológia">
  <meta property="og:description" content="Nagyüzemi sütésálló gyümölcstöltelékek, kenhető készítmények és egyedi receptúrák közvetlenül a gyártótól. 200 °C felett sem forr ki.">
  <meta property="og:image" content="https://csernabalint.github.io/sun-valley/assets/sun-valley-logo.webp">
  <meta property="og:locale" content="hu_HU">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="https://csernabalint.github.io/sun-valley/">
  <meta name="twitter:title" content="Sun Valley Zrt. – Ipari Sütésálló Gyümölcstöltelékek">
  <meta name="twitter:description" content="Nagyüzemi sütésálló gyümölcstöltelékek és egyedi receptúrák ipari pékségek számára. Móri üzem, AA+ bonitás.">
  <meta name="twitter:image" content="https://csernabalint.github.io/sun-valley/assets/sun-valley-logo.webp">

  <!-- Tailwind CSS via CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            stone: {
              900: 'rgb(50, 45, 36)',
            }
          }
        }
      }
    };
  </script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- StPageFlip Flipbook Engine (Pantastico / Heyzine inspired physics) -->
  <script defer src="assets/vendor/page-flip.browser.js"></script>

  <!-- Google Fonts: Inter & Montserrat -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&display=swap" rel="stylesheet">

  <style>
    :root {
      /* Sun Valley Official Palette (Frissítve: 2026-09) */
      --sv-burgundy: #a3392e;         /* Meleg Gyümölcspiros: Főcímek, gombok, logó */
      --sv-burgundy-hover: #872c24;   /* Gombok hover állapota */
      --sv-burgundy-dark: #451C1B;    /* Sötétbordó: Icon backgrounds, divider strips */
      --sv-orange: #91372d;           /* Terrakotta gyümölcstónus (korábbi narancs helyett): kiemelések, CTA */
      --sv-orange-hover: #7b2a22;     /* Másodlagos gombok hover állapota */
      --sv-gold: #D48054;             /* Arany Napsugár: Secondary highlights, sun rays */
      --sv-gold-light: #FBBB9C;       /* Világos Arany: Halo, glow, badge accents */
      --sv-green-dark: #2D3628;       /* Dombok Mélyzöldje: Landscape layers, dark surfaces */
      --sv-green-light: #5F6E4D;      /* Dombok Világoszöldje: Subtle green accents */
      --sv-apple-red: #923833;        /* Érett Almapiros: Fruit badges, alert accents */
      --sv-soil-brown: #63412C;       /* Termőföld: Earthy structural accents */
      --sv-paper-cream: #F5F2EE;      /* Papíralap Krémfehér: Light mode background */
      --sv-sand-watermark: #D0AE9F;   /* Homokbézs Vízjel: Decorative borders, subtle watermarks */
      --sv-selection: #f1c7a6;        /* Barackkrém szövegkijelölés */
      --sv-surface: #FFFFFF;
      --sv-text-main: rgb(50, 45, 36); /* #322d24: Lágy meleg koromfekete az rgb(28, 25, 23) helyett */
      --sv-text-muted: #57524E;
      --sv-border: rgba(163, 57, 46, 0.16);
      --sv-border-light: rgba(163, 57, 46, 0.08);
    }

    /* Primary dark text color override: rgb(50, 45, 36) replaces rgb(28, 25, 23) */
    .text-stone-900 {
      color: rgb(50, 45, 36) !important;
    }
    .hover\\:text-stone-900:hover {
      color: rgb(50, 45, 36) !important;
    }
    .border-stone-900 {
      border-color: rgb(50, 45, 36) !important;
    }
    .bg-stone-900 {
      background-color: rgb(50, 45, 36) !important;
    }

    ::selection {
      background-color: #f1c7a6;
      color: #451C1B;
    }

    ::-moz-selection {
      background-color: #f1c7a6;
      color: #451C1B;
    }

    html {
      scroll-padding-top: 100px;
    }

    *, *::before, *::after {
      box-sizing: border-box;
    }

    html, body {
      overflow-x: clip;
      max-width: 100vw;
    }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--sv-paper-cream);
      color: var(--sv-text-main);
    }

    .font-syne, .font-montserrat {
      font-family: Montserrat, "Montserrat Placeholder", sans-serif;
      letter-spacing: -0.01em;
    }

    .font-mono-spec {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      font-variant-numeric: tabular-nums;
      font-feature-settings: "cv02", "cv03", "cv04", "cv11", "tnum" 1;
      letter-spacing: 0.02em;
    }

    /* Subtle industrial graph grid pattern */
    .bg-tech-grid {
      background-size: 40px 40px;
      background-image: 
        linear-gradient(to right, rgba(163, 57, 46, 0.035) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(163, 57, 46, 0.035) 1px, transparent 1px);
    }

    /* Custom scrollbar */
    ::-webkit-scrollbar {
      width: 8px;
    }
    ::-webkit-scrollbar-track {
      background: var(--sv-paper-cream);
    }
    ::-webkit-scrollbar-thumb {
      background: var(--sv-burgundy);
      border-radius: 4px;
    }

    .catalog-tab.active {
      background-color: var(--sv-burgundy);
      color: #ffffff;
      border-color: var(--sv-burgundy);
    }

    /* ------------------------------------------------------------------------- */
    /* StPageFlip Interactive Physical Book Styles (Pantastico / Heyzine engine) */
    /* ------------------------------------------------------------------------- */
    #sv-book-slot {
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      overflow: visible;
      padding: 1.5rem 0 2.25rem 0;
    }
    #sv-book {
      margin: 0 auto;
      background: #FFFFFF;
      border-radius: 18px;
      box-shadow: 
        0 14px 30px -4px rgba(70, 28, 27, 0.08),
        0 6px 14px -2px rgba(0, 0, 0, 0.06),
        0 0 0 1px rgba(70, 28, 27, 0.06);
      position: relative;
    }
    /* Strictly clip flipbook wrappers so curling pages, canvases, and internal shadows never poke out of the 18px rounded book bounds */
    .stf__wrapper,
    .stf__block {
      border-radius: 18px !important;
      overflow: hidden !important;
      -webkit-mask-image: -webkit-radial-gradient(white, black); /* WebKit/Safari 3D clipping fix */
    }
    .stf__parent canvas {
      border-radius: 18px;
    }
    .sv-page {
      background: #FFFFFF;
      box-sizing: border-box;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      height: 100%;
      position: relative;
      border-radius: 18px;
    }
    .sv-page-left {
      border-top-left-radius: 18px;
      border-bottom-left-radius: 18px;
      border-top-right-radius: 0;
      border-bottom-right-radius: 0;
    }
    .sv-page-right {
      border-top-right-radius: 18px;
      border-bottom-right-radius: 18px;
      border-top-left-radius: 0;
      border-bottom-left-radius: 0;
    }
    .sv-spine-left {
      position: absolute;
      top: 0;
      right: 0;
      bottom: 0;
      width: 32px;
      background: linear-gradient(to left, rgba(0, 0, 0, 0.08) 0%, rgba(0, 0, 0, 0.02) 40%, transparent 100%);
      pointer-events: none;
      z-index: 25;
    }
    .sv-spine-right {
      position: absolute;
      top: 0;
      left: 0;
      bottom: 0;
      width: 32px;
      background: linear-gradient(to right, rgba(0, 0, 0, 0.08) 0%, rgba(0, 0, 0, 0.02) 40%, transparent 100%);
      pointer-events: none;
      z-index: 25;
    }

    /* Mobile 3D Flip Card Transitions (< 1024px) */
    .mobile-catalog-card {
      perspective: 1200px;
      touch-action: pan-y;
    }
    .mobile-card-inner {
      transition: transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.3s ease;
      will-change: transform, opacity;
    }
    .mobile-card-flip-out-next {
      transform: translateX(-40px) scale(0.96) rotateY(-8deg);
      opacity: 0;
    }
    .mobile-card-flip-in-next {
      transform: translateX(40px) scale(0.96) rotateY(8deg);
      opacity: 0;
    }
    .mobile-card-flip-out-prev {
      transform: translateX(40px) scale(0.96) rotateY(8deg);
      opacity: 0;
    }
    .mobile-card-flip-in-prev {
      transform: translateX(-40px) scale(0.96) rotateY(-8deg);
      opacity: 0;
    }

    /* Standardized button micro-interactions: smooth 180ms color transitions without disruptive layout scale jumps */
    a, button {
      transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, box-shadow, transform;
      transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
      transition-duration: 180ms;
    }

    /* Subtle icon nudge on button hover instead of whole button scale */
    a:hover > [data-lucide], button:hover > [data-lucide] {
      transform: translateX(2px);
      transition: transform 180ms ease-out;
    }

    /* Button hovers: #872c24 exclusively on buttons as requested */
    button[style*="background-color: var(--sv-burgundy)"]:hover,
    button[style*="background-color:var(--sv-burgundy)"]:hover,
    a[style*="background-color: var(--sv-burgundy)"]:hover,
    a[style*="background-color:var(--sv-burgundy)"]:hover {
      background-color: var(--sv-burgundy-hover) !important;
    }

    button[style*="background-color: var(--sv-orange)"]:hover,
    button[style*="background-color:var(--sv-orange)"]:hover,
    a[style*="background-color: var(--sv-orange)"]:hover,
    a[style*="background-color:var(--sv-orange)"]:hover {
      background-color: var(--sv-orange-hover) !important;
    }

    /* Smooth mobile drawer transition */
    #mobile-menu {
      transition: max-height 0.28s ease, opacity 0.24s ease;
    }

    /* Active navigation indicator */
    .nav-item-active {
      color: var(--sv-burgundy) !important;
      font-weight: 700 !important;
    }
    .nav-item-active > span {
      width: 100% !important;
    }

    /* Comprehensive prefers-reduced-motion overrides */
    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }
      .mobile-card-inner {
        transition: none !important;
        transform: none !important;
      }
      #mobile-menu {
        transition: none !important;
      }
      #site-header {
        transition: none !important;
      }
      a:hover > [data-lucide], button:hover > [data-lucide] {
        transform: none !important;
      }
    }

  </style>
</head>
<body id="top" class="min-h-screen flex flex-col antialiased selection:bg-[#f1c7a6] selection:text-[#451C1B]" style="background-color: var(--sv-paper-cream);">

  <!-- ========================================================================= -->
  <!-- DYNAMIC SMART HEADER (Reveal on Scroll Up / Hide on Scroll Down)         -->
  <!-- ========================================================================= -->
  <header id="site-header" class="fixed top-0 inset-x-0 z-50 transition-transform duration-300 ease-out will-change-transform">
<!-- MAIN NAVIGATION BAR -->
    <div id="main-nav" class="backdrop-blur-md border-b transition-all duration-300 shadow-sm"
         style="background-color: rgba(255, 255, 255, 0.98); border-color: rgba(163, 57, 46, 0.15); box-shadow: 0 2px 12px rgba(70, 28, 27, 0.06);">
      <div class="max-w-7xl mx-auto px-3.5 sm:px-8 py-3 sm:py-3.5 flex items-center justify-between gap-2 sm:gap-4">
        
        <!-- Brand Crest & Identity (Authentic Sun Valley Logo) -->
        <a href="#top" class="flex items-center gap-2 sm:gap-3 group shrink-0">
          <img src="assets/sun-valley-logo.webp" alt="Sun Valley Logo" width="160" height="44" class="h-8 sm:h-11 w-auto object-contain">
          <div>
            <div class="font-montserrat font-extrabold text-sm sm:text-base md:text-lg tracking-tight leading-none" style="color: var(--sv-burgundy);">
              Sun Valley
            </div>
            <p class="text-[10px] font-mono-spec tracking-wider uppercase hidden md:block mt-0.5" style="color: var(--sv-text-muted);" data-i18n="tagline">
              Ipari Gyümölcstechnológia • Mór
            </p>
          </div>
        </a>

        <!-- Desktop Nav Links (Streamlined Essential Links, Single Line, No Wrap) -->
        <nav class="hidden lg:flex items-center gap-5 xl:gap-8 text-xs xl:text-sm font-semibold whitespace-nowrap text-stone-700">
          <a href="#termekek" class="hover:text-[#91372d] transition-colors py-1 relative group whitespace-nowrap" data-i18n="nav_products">
            Termékek & Katalógus
            <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#91372d] transition-all group-hover:w-full"></span>
          </a>
          <a href="#technologia" class="hover:text-[#91372d] transition-colors py-1 relative group whitespace-nowrap" data-i18n="nav_tech">
            Technológia
            <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#91372d] transition-all group-hover:w-full"></span>
          </a>
          <a href="#cegunkrol" class="hover:text-[#91372d] transition-colors py-1 relative group whitespace-nowrap" data-i18n="nav_about">
            Cégünkről
            <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#91372d] transition-all group-hover:w-full"></span>
          </a>
          <a href="#egyedi-fejlesztes" class="hover:text-[#91372d] transition-colors py-1 relative group whitespace-nowrap" data-i18n="nav_rd">
            Egyedi receptúra
            <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#91372d] transition-all group-hover:w-full"></span>
          </a>
          <a href="#kapcsolat" class="hover:text-[#91372d] transition-colors py-1 relative group whitespace-nowrap" data-i18n="nav_contact">
            Kapcsolat
            <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#91372d] transition-all group-hover:w-full"></span>
          </a>
        </nav>

        <!-- Right Controls: Language Switcher & Direct Call CTA -->
        <div class="flex items-center gap-1.5 sm:gap-3 shrink-0">
          
          <!-- BILINGUAL SWITCHER (HU / EN) -->
          <div class="h-9 flex items-center p-0.5 sm:p-1 rounded-lg border font-mono-spec shrink-0 box-border"
               style="background-color: var(--sv-surface); border-color: var(--sv-border);">
            <button onclick="setLanguage('hu')" id="lang-hu" class="h-full px-2 sm:px-2.5 flex items-center justify-center rounded font-bold transition-all bg-[#a3392e] text-white shadow-sm text-[11px] sm:text-xs">
              HU
            </button>
            <button onclick="setLanguage('en')" id="lang-en" class="h-full px-2 sm:px-2.5 flex items-center justify-center rounded font-medium text-stone-600 hover:text-[#91372d] transition-all text-[11px] sm:text-xs">
              EN
            </button>
          </div>

          <!-- Direct Contact Button -->
          <a href="#kapcsolat" 
             class="h-9 hidden sm:inline-flex items-center justify-center gap-2 px-3.5 xl:px-4 rounded-lg font-semibold text-xs transition-all transform active:scale-95 shadow-sm shrink-0 box-border"
             style="background-color: var(--sv-burgundy); color: white;">
            <i data-lucide="mail" class="w-3.5 h-3.5"></i>
            <span data-i18n="nav_contact">Kapcsolat</span>
          </a>

          <!-- Mobile Menu Toggle -->
          <button onclick="toggleMobileMenu()" class="h-9 w-9 flex items-center justify-center lg:hidden rounded-lg border shrink-0 box-border" style="border-color: var(--sv-border);" aria-label="Navigációs menü">
            <i data-lucide="menu" class="w-5 h-5 text-stone-800"></i>
          </button>
        </div>

      </div>

      <!-- Mobile Drawer -->
      <div id="mobile-menu" class="hidden lg:hidden border-t px-6 py-5 space-y-4 max-h-[calc(100vh-90px)] overflow-y-auto shadow-xl" style="background-color: #FFFFFF; border-color: var(--sv-border);">
        <div class="flex flex-col space-y-3 font-semibold text-sm">
          <a href="#termekek" onclick="toggleMobileMenu()" class="py-1 text-stone-800 hover:text-[#91372d]" data-i18n="nav_products">Termékek & Katalógus</a>
          <a href="#technologia" onclick="toggleMobileMenu()" class="py-1 text-stone-800 hover:text-[#91372d]" data-i18n="nav_tech">Technológia</a>
          <a href="#cegunkrol" onclick="toggleMobileMenu()" class="py-1 text-stone-800 hover:text-[#91372d]" data-i18n="nav_about">Cégünkről</a>
          <a href="#egyedi-fejlesztes" onclick="toggleMobileMenu()" class="py-1 text-stone-800 hover:text-[#91372d]" data-i18n="nav_rd">Egyedi receptúra</a>
          <a href="#prospektus" onclick="toggleMobileMenu()" class="py-1 text-stone-800 hover:text-[#91372d]" data-i18n="nav_prospectus">Prospektus</a>
          <a href="#kapcsolat" onclick="toggleMobileMenu()" class="py-1 text-stone-800 hover:text-[#91372d]" data-i18n="nav_contact">Kapcsolat</a>
        </div>
        <div class="pt-3 border-t flex flex-col gap-2" style="border-color: var(--sv-border);">
          <a href="#kapcsolat" onclick="toggleMobileMenu()" class="flex items-center justify-center gap-2 py-2.5 rounded-lg text-white font-semibold text-sm" style="background-color: var(--sv-burgundy);">
            <i data-lucide="mail" class="w-4 h-4"></i>
            <span data-i18n="nav_contact">Kapcsolat</span>
          </a>
        </div>
      </div>
    </div>
  </header>

  <!-- Flow Spacer (prevents hero section jump) -->
  <div id="header-spacer" class="w-full shrink-0" aria-hidden="true"></div>

  <!-- ========================================================================= -->
  <!-- HERO SECTION – INDUSTRIAL CONVICTION WITH PHOTOGRAPHIC PROOF             -->
  <!-- ========================================================================= -->
  <section id="hero" class="relative overflow-hidden pt-10 pb-16 md:pt-16 md:pb-20 border-b" style="border-color: var(--sv-border);">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      
      <!-- Asymmetric Two-Column Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-8 xl:gap-12 items-center">
        
        <!-- Left Column: High-Conviction Value Proposition (Span 7) -->
        <div class="lg:col-span-7 flex flex-col gap-6">

          <!-- Target Audience Category Badge -->
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-lg text-xs font-mono-spec uppercase tracking-wider font-semibold border self-start shadow-sm"
               style="background-color: rgba(163, 57, 46, 0.08); color: var(--sv-burgundy); border-color: rgba(163, 57, 46, 0.2);">
            <i data-lucide="factory" class="w-3.5 h-3.5 text-[#a3392e]"></i>
            <span data-i18n="hero_target_badge">Nagyüzemi sütő- és cukrászipari alapanyagok</span>
          </div>

          <!-- Headline -->
          <h1 class="font-montserrat font-extrabold text-3xl sm:text-4xl lg:text-5xl xl:text-[3.25rem] tracking-tight leading-[1.12]"
              style="color: var(--sv-burgundy);">
            <span data-i18n="hero_h1">Kiforrásbiztos, formamegtartó gyümölcstöltelékek</span>
          </h1>

          <p class="text-stone-700 text-base sm:text-lg leading-relaxed max-w-xl font-sans" data-i18n="hero_sub_p">
            Kiforrásbiztos, 180–220 °C-ig hőtűrő és hidegen kenhető gyümölcskészítmények közvetlen a gyártóüzemünkből. Stabil viszkozitás automata adagoló- és injektálósorokra, 5 kg-tól 200 kg-os kiszerelésig.
          </p>

          <!-- Industrial Proof Micro-Badges -->
          <div class="grid grid-cols-3 gap-2.5 sm:gap-4 max-w-xl py-1">
            <div class="p-2.5 sm:p-3 rounded-xl border bg-white/70 backdrop-blur-sm shadow-xs flex flex-col gap-0.5" style="border-color: var(--sv-border);">
              <span class="text-[10px] font-mono-spec uppercase tracking-wider text-stone-500 font-semibold" data-i18n="hero_pill_heat">Hőtűrés</span>
              <span class="font-montserrat font-bold text-sm sm:text-base text-stone-900 tracking-tight">180–220 °C</span>
            </div>
            <div class="p-2.5 sm:p-3 rounded-xl border bg-white/70 backdrop-blur-sm shadow-xs flex flex-col gap-0.5" style="border-color: var(--sv-border);">
              <span class="text-[10px] font-mono-spec uppercase tracking-wider text-stone-500 font-semibold" data-i18n="hero_pill_scale">Kiszerelés</span>
              <span class="font-montserrat font-bold text-sm sm:text-base text-stone-900 tracking-tight">5 – 200 kg</span>
            </div>
            <div class="p-2.5 sm:p-3 rounded-xl border bg-white/70 backdrop-blur-sm shadow-xs flex flex-col gap-0.5" style="border-color: var(--sv-border);">
              <span class="text-[10px] font-mono-spec uppercase tracking-wider text-stone-500 font-semibold" data-i18n="hero_pill_origin">Gyártás</span>
              <span class="font-montserrat font-bold text-sm sm:text-base text-stone-900 tracking-tight">Móri Üzem</span>
            </div>
          </div>

          <!-- Action Buttons: Dominant vs Secondary Hierarchy -->
          <div class="pt-2 flex flex-col sm:flex-row items-stretch sm:items-center gap-4">
            <!-- Primary Dominant: Inquire / Quote -->
            <a href="#kapcsolat" 
               class="inline-flex items-center justify-center gap-2.5 px-7 py-3.5 rounded-xl font-bold text-sm transition-all transform active:scale-95 shadow-md hover:shadow-lg text-white text-center"
               style="background-color: var(--sv-burgundy);"
               onmouseover="this.style.backgroundColor='var(--sv-burgundy-hover)'"
               onmouseout="this.style.backgroundColor='var(--sv-burgundy)'">
              <i data-lucide="mail" class="w-4 h-4"></i>
              <span data-i18n="hero_cta_inquire">Közvetlen gyári árajánlatkérés</span>
            </a>

            <!-- Secondary Outline: Browse Categories -->
            <a href="#termekek" 
               class="inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-xl font-semibold text-sm transition-all border hover:bg-stone-50 text-stone-800 text-center shadow-xs"
               style="border-color: var(--sv-border); background-color: #FFFFFF;">
              <i data-lucide="book-open" class="w-4 h-4 text-stone-600"></i>
              <span data-i18n="hero_cta_browse">Termékkategóriák megtekintése</span>
            </a>
          </div>

        </div>

        <!-- Right Column: Clean Visual Hero (Span 5) -->
        <div class="lg:col-span-5 flex items-center justify-center">
          <div class="w-full rounded-2xl border overflow-hidden bg-stone-100 group relative shadow-md hover:shadow-lg transition-shadow"
               style="border-color: var(--sv-border);">
            <picture>
              <source srcset="assets/hero-page-jam.webp" type="image/webp">
              <img src="assets/hero-page-jam.jpg" alt="Sun Valley gyümölcstöltelék" width="600" height="480" fetchpriority="high" decoding="async" class="w-full h-80 sm:h-96 lg:h-[460px] object-cover object-center">
            </picture>

            <!-- Authentic Quality Tag Overlay -->
            <div class="absolute bottom-4 left-4 right-4 sm:left-auto sm:right-4 z-20 flex items-center gap-2 px-3.5 py-2 rounded-xl backdrop-blur-md bg-stone-900/80 border border-white/20 text-white shadow-lg">
              <i data-lucide="shield-check" class="w-4 h-4 text-[#FBBB9C] shrink-0"></i>
              <div class="text-[11px] font-mono-spec font-medium leading-tight">
                <span class="block font-bold text-white" data-i18n="hero_img_badge_title">Ipari Minőség • Formamegtartó</span>
                <span class="text-white/75 text-[10px]" data-i18n="hero_img_badge_sub">200 °C felett sem forr ki</span>
              </div>
            </div>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- HERO SPECIFICATIONS RIBBON – RED / BURGUNDY BANNER                          -->
  <!-- ========================================================================= -->
  <section class="py-6 border-b text-white" style="background-color: var(--sv-burgundy); border-color: rgba(0,0,0,0.15);">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 sm:gap-8 items-center">
        <!-- Telemetry 1: Hőtűrési küszöb -->
        <div class="flex items-center gap-4">
          <div class="w-12 h-12 rounded-xl flex items-center justify-center shrink-0 bg-white/10 border border-white/20 text-[#FBBB9C]">
            <i data-lucide="flame" class="w-6 h-6"></i>
          </div>
          <div>
            <div class="text-[11px] font-mono-spec uppercase tracking-wider text-white/70" data-i18n="telemetry_heat_label">Hőtűrési küszöb</div>
            <div class="font-montserrat font-extrabold text-xl sm:text-2xl text-white tracking-tight mt-0.5" data-i18n="telemetry_heat_val">180 °C és 220 °C</div>
            <div class="text-xs text-white/80 font-mono-spec mt-0.5" data-i18n="telemetry_heat_sub">Két hőtűrési kategória leveles és kelt tésztákhoz</div>
          </div>
        </div>
        <!-- Telemetry 2: Ipari Kiszerelés -->
        <div class="flex items-center gap-4 sm:border-l sm:pl-8" style="border-color: rgba(255,255,255,0.2);">
          <div class="w-12 h-12 rounded-xl flex items-center justify-center shrink-0 bg-white/10 border border-white/20 text-[#FBBB9C]">
            <i data-lucide="package" class="w-6 h-6"></i>
          </div>
          <div>
            <div class="text-[11px] font-mono-spec uppercase tracking-wider text-white/70" data-i18n="telemetry_pack_label">Ipari Kiszerelés</div>
            <div class="font-montserrat font-extrabold text-xl sm:text-2xl text-white tracking-tight mt-0.5" data-i18n="telemetry_pack_val">5–20 kg és 200 kg</div>
            <div class="text-xs text-white/80 font-mono-spec mt-0.5" data-i18n="telemetry_pack_sub">Vödör, tömb és aszeptikus hordó (480 kg raklapos egységek)</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- TERMÉKPORTFÓLIÓ & LAPOZHATÓ TERMÉKKATALÓGUS                                -->
  <!-- ========================================================================= -->
  <section id="termekek" class="py-16 md:py-24 border-b" style="border-color: var(--sv-border); background-color: var(--sv-paper-cream);">
    <div class="max-w-7xl mx-auto px-4 sm:px-8 space-y-8 sm:space-y-10">
      
      <!-- Section Header -->
      <div class="max-w-3xl">
        <div class="font-mono-spec text-xs uppercase tracking-widest text-[#91372d] font-semibold mb-2" data-i18n="cat_section_tag">
          Termékportfólió & Minőségi Specifikációk
        </div>
        <h2 class="font-montserrat font-bold text-3xl sm:text-4xl text-stone-900 leading-snug pb-1" data-i18n="cat_section_title">
          Lekvárok felhasználás szerint
        </h2>
      </div>

      <!-- ========================================================================= -->
      <!-- DESKTOP FLIPPABLE BOOK (Screens >= 1024px)                                -->
      <!-- ========================================================================= -->
      <div class="hidden lg:block relative catalog-viewport max-w-6xl mx-auto px-4 md:px-8" id="desktop-catalog-container">
        
        <!-- Left Side Flanking Navigation Arrow -->
        <button onclick="svFlipPrev()" id="cat-side-prev" aria-label="Előző oldal" title="Előző oldal"
                class="flex absolute -left-5 top-1/2 -translate-y-1/2 z-30 w-12 h-12 md:w-13 md:h-13 rounded-full bg-white/95 backdrop-blur-md border border-stone-200 hover:border-[#a3392e] shadow-lg hover:shadow-xl items-center justify-center text-stone-800 hover:text-white hover:bg-[#a3392e] hover:scale-105 active:scale-95 transition-all focus:outline-none focus:ring-2 focus:ring-[#a3392e]/40 cursor-pointer disabled:opacity-30 disabled:pointer-events-none disabled:hover:scale-100">
          <i data-lucide="chevron-left" class="w-5 h-5 sm:w-6 sm:h-6 stroke-[2.5]"></i>
        </button>

        <!-- Right Side Flanking Navigation Arrow -->
        <button onclick="svFlipNext()" id="cat-side-next" aria-label="Következő oldal" title="Következő oldal"
                class="flex absolute -right-5 top-1/2 -translate-y-1/2 z-30 w-12 h-12 md:w-13 md:h-13 rounded-full bg-white/95 backdrop-blur-md border border-stone-200 hover:border-[#a3392e] shadow-lg hover:shadow-xl items-center justify-center text-stone-800 hover:text-white hover:bg-[#a3392e] hover:scale-105 active:scale-95 transition-all focus:outline-none focus:ring-2 focus:ring-[#a3392e]/40 cursor-pointer disabled:opacity-30 disabled:pointer-events-none disabled:hover:scale-100">
          <i data-lucide="chevron-right" class="w-5 h-5 sm:w-6 sm:h-6 stroke-[2.5]"></i>
        </button>

        <!-- Book Stage & StPageFlip Canvas Wrapper -->
        <div id="sv-book-slot" class="w-full flex justify-center items-center py-6 sm:py-8" style="min-height: 580px;">
          <div id="sv-book" class="mx-auto rounded-2xl">
            
            <!-- ================= PAGE 0 (SPREAD 1 LEFT: KENHETŐ IMAGE) ================= -->
            <section class="sv-page sv-page-left relative overflow-hidden" id="page-0">
              <picture class="w-full h-full block">
                <source srcset="assets/catalog-jam1.webp" type="image/webp">
                <img src="assets/catalog-jam1.jpg" alt="Kenhető lekvárok bemutató" width="640" height="520" loading="lazy" decoding="async" class="w-full h-full object-cover object-center">
              </picture>
              <div class="absolute bottom-5 left-6 z-30 font-mono-spec font-bold text-xs text-white bg-black/60 backdrop-blur-sm px-2.5 py-1 rounded">
                1
              </div>
              <div class="sv-spine-left"></div>
            </section>

            <!-- ================= PAGE 1 (SPREAD 1 RIGHT: KENHETŐ SPECS) ================= -->
            <section class="sv-page sv-page-right p-6 sm:p-8 flex flex-col justify-between" id="page-1">
              <div class="space-y-4">
                <div>
                  <h3 data-i18n="prod_cat1_title" class="font-montserrat font-bold text-2xl sm:text-3xl text-stone-900 leading-tight">
                    Kenhető lekvárok
                  </h3>
                  <p data-i18n="prod_cat1_subtitle" class="text-xs sm:text-sm text-[#91372d] font-semibold font-mono-spec mt-1">
                    Selymes, homogén állag linzerekhez, piskótákhoz és tortalapokhoz
                  </p>
                </div>

                <p data-i18n="prod_cat1_desc" class="text-stone-600 text-xs sm:text-sm leading-relaxed">
                  Egyenletesen és könnyedén kenhető, homogén gyümölcskészítmények. Tiszta gyümölcsíz, csomómentes textúra és stabil hidegterülés.
                </p>

                <!-- Available Flavors -->
                <div>
                  <div data-i18n="prod_flavors_label" class="text-[11px] font-mono-spec uppercase tracking-wider text-stone-500 font-semibold mb-2">
                    Elérhető Ízek (Azonos Technológiai Paraméterekkel):
                  </div>
                  <div class="flex flex-wrap gap-1.5">
                    <span data-i18n="flavor_apricot" class="px-2 py-0.5 rounded text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">Sárgabarack</span>
                    <span data-i18n="flavor_raspberry" class="px-2 py-0.5 rounded text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">Málna</span>
                    <span data-i18n="flavor_sour_cherry" class="px-2 py-0.5 rounded text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">Meggy</span>
                    <span data-i18n="flavor_blueberry" class="px-2 py-0.5 rounded text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">Áfonya</span>
                    <span data-i18n="flavor_forest_berry" class="px-2 py-0.5 rounded text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">Erdei gyümölcs</span>
                  </div>
                </div>

                <!-- Applications -->
                <div>
                  <div data-i18n="cat_apps_label_pastry" class="text-[11px] font-mono-spec uppercase tracking-wider text-stone-500 font-semibold mb-1.5">
                    Ajánlott Cukrászati Felhasználás:
                  </div>
                  <div class="flex flex-wrap gap-1.5 text-xs text-stone-600 font-mono-spec">
                    <span data-i18n="app_linzer" class="bg-emerald-50/80 border border-emerald-200/80 px-2 py-0.5 rounded">Linzerkarika</span>
                    <span data-i18n="app_roll" class="bg-emerald-50/80 border border-emerald-200/80 px-2 py-0.5 rounded">Piskótatekercs</span>
                    <span data-i18n="app_layers" class="bg-emerald-50/80 border border-emerald-200/80 px-2 py-0.5 rounded">Tortalapok kenése</span>
                    <span data-i18n="app_inserts" class="bg-emerald-50/80 border border-emerald-200/80 px-2 py-0.5 rounded">Desszertbetétek</span>
                    <span data-i18n="app_donuts" class="bg-emerald-50/80 border border-emerald-200/80 px-2 py-0.5 rounded">Fánk</span>
                  </div>
                </div>
              </div>

              <!-- Bottom CTA & Packaging -->
              <div class="pt-5 border-t mt-auto flex flex-col items-start gap-1.5" style="border-color: var(--sv-border-light);">
                <a href="#kapcsolat" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl font-semibold text-xs font-mono-spec transition-all shadow-sm text-white" style="background-color: var(--sv-orange);">
                  <i data-lucide="mail-check" class="w-4 h-4"></i>
                  <span data-i18n="btn_inquire_jam">Érdeklődés & Ajánlatkérés</span>
                </a>
                <span data-i18n="pack_spread_spec" class="text-[11px] font-mono-spec text-stone-400">Kiszerelés: 5 / 10 / 20 kg</span>
              </div>

              <!-- Page Number pinned to bottom right -->
              <div class="absolute bottom-5 right-6 z-30 font-mono-spec font-bold text-xs text-stone-500">
                2
              </div>
              <div class="sv-spine-right"></div>
            </section>

            <!-- ================= PAGE 2 (SPREAD 2 LEFT: SÜTÉSÁLLÓ IMAGE) ================= -->
            <section class="sv-page sv-page-left relative overflow-hidden" id="page-2">
              <picture class="w-full h-full block">
                <source srcset="assets/catalog-jam2.webp" type="image/webp">
                <img src="assets/catalog-jam2.jpg" alt="Sütésálló gyümölcstöltelékek ipari finompékárukban" width="640" height="520" loading="lazy" decoding="async" class="w-full h-full object-cover object-center">
              </picture>
              <div class="absolute bottom-5 left-6 z-30 font-mono-spec font-bold text-xs text-white bg-black/60 backdrop-blur-sm px-2.5 py-1 rounded">
                3
              </div>
              <div class="sv-spine-left"></div>
            </section>

            <!-- ================= PAGE 3 (SPREAD 2 RIGHT: SÜTÉSÁLLÓ SPECS) ================= -->
            <section class="sv-page sv-page-right p-6 sm:p-8 flex flex-col justify-between" id="page-3">
              <div class="space-y-4">
                <div>
                  <h3 data-i18n="prod_cat2_title" class="font-montserrat font-bold text-2xl sm:text-3xl text-stone-900 leading-tight">
                    Sütésálló lekvárok
                  </h3>
                  <p data-i18n="prod_cat2_subtitle" class="text-xs sm:text-sm text-[#91372d] font-semibold font-mono-spec mt-1">
                    Formamegtartó, sütés közben sem kiforró tésztabetétek
                  </p>
                </div>

                <p data-i18n="prod_cat2_desc" class="text-stone-600 text-xs sm:text-sm leading-relaxed">
                  Összetételüknek köszönhetően magas hőfokon sem forrnak ki, és nem áztatják el a tésztát. Kihűlés után is szépen megtartják a formájukat, a töltőgépeken pedig tisztán, csepegés nélkül adagolhatók.
                </p>

                <!-- Available Flavors -->
                <div>
                  <div data-i18n="prod_flavors_label" class="text-[11px] font-mono-spec uppercase tracking-wider text-stone-500 font-semibold mb-2">
                    Elérhető Ízek (Azonos Technológiai Paraméterekkel):
                  </div>
                  <div class="flex flex-wrap gap-1.5">
                    <span data-i18n="flavor_apricot" class="px-2 py-0.5 rounded text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">Kajszibarack</span>
                    <span data-i18n="flavor_plum" class="px-2 py-0.5 rounded text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">Szilva</span>
                    <span data-i18n="flavor_sour_cherry" class="px-2 py-0.5 rounded text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">Meggy</span>
                    <span data-i18n="flavor_forest_berry" class="px-2 py-0.5 rounded text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">Erdei gyümölcs</span>
                    <span data-i18n="flavor_apple" class="px-2 py-0.5 rounded text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">Alma</span>
                    <span data-i18n="flavor_strawberry" class="px-2 py-0.5 rounded text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">Eper</span>
                  </div>
                </div>

                <!-- Applications -->
                <div>
                  <div data-i18n="cat_apps_label_bakery" class="text-[11px] font-mono-spec uppercase tracking-wider text-stone-500 font-semibold mb-1.5">
                    Jellemző Pékipari Felhasználás:
                  </div>
                  <div class="flex flex-wrap gap-1.5 text-xs text-stone-600 font-mono-spec">
                    <span data-i18n="app_croissant" class="bg-red-50/80 border border-red-200/80 px-2 py-0.5 rounded">Croissantok & búrkiflik</span>
                    <span data-i18n="app_buns" class="bg-red-50/80 border border-red-200/80 px-2 py-0.5 rounded">Bukták & batyuk</span>
                    <span data-i18n="app_puff" class="bg-red-50/80 border border-red-200/80 px-2 py-0.5 rounded">Leveles tészták</span>
                    <span data-i18n="app_pouches" class="bg-red-50/80 border border-red-200/80 px-2 py-0.5 rounded">Párnácskák</span>
                    <span data-i18n="app_frozen" class="bg-red-50/80 border border-red-200/80 px-2 py-0.5 rounded">Fagyasztott félkészáru</span>
                  </div>
                </div>
              </div>

              <!-- Bottom CTA & Packaging -->
              <div class="pt-5 border-t mt-auto flex flex-col items-start gap-1.5" style="border-color: var(--sv-border-light);">
                <a href="#kapcsolat" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl font-semibold text-xs font-mono-spec transition-all shadow-sm text-white" style="background-color: var(--sv-orange);">
                  <i data-lucide="mail-check" class="w-4 h-4"></i>
                  <span data-i18n="btn_inquire_jam">Érdeklődés & Ajánlatkérés</span>
                </a>
                <span data-i18n="pack_bake_spec" class="text-[11px] font-mono-spec text-stone-400">Kiszerelés: 10 / 20 kg tömb & vödör</span>
              </div>

              <!-- Page Number pinned to bottom right -->
              <div class="absolute bottom-5 right-6 z-30 font-mono-spec font-bold text-xs text-stone-500">
                4
              </div>
              <div class="sv-spine-right"></div>
            </section>

            <!-- ================= PAGE 4 (SPREAD 3 LEFT: EXTRA DZSEM IMAGE) ================= -->
            <section class="sv-page sv-page-left relative overflow-hidden" id="page-4">
              <picture class="w-full h-full block">
                <source srcset="assets/catalog-jam-3.webp" type="image/webp">
                <img src="assets/catalog-jam-3.jpg" alt="Prémium gyümölcsdarabos extra dzsemek" width="640" height="520" loading="lazy" decoding="async" class="w-full h-full object-cover object-center">
              </picture>
              <div class="absolute bottom-5 left-6 z-30 font-mono-spec font-bold text-xs text-white bg-black/60 backdrop-blur-sm px-2.5 py-1 rounded">
                5
              </div>
              <div class="sv-spine-left"></div>
            </section>

            <!-- ================= PAGE 5 (SPREAD 3 RIGHT: EXTRA DZSEM SPECS) ================= -->
            <section class="sv-page sv-page-right p-6 sm:p-8 flex flex-col justify-between" id="page-5">
              <div class="space-y-4">
                <div>
                  <h3 data-i18n="prod_cat3_title" class="font-montserrat font-bold text-2xl sm:text-3xl text-stone-900 leading-tight">
                    Extra dzsemek
                  </h3>
                  <p data-i18n="prod_cat3_subtitle" class="text-xs sm:text-sm text-[#91372d] font-semibold font-mono-spec mt-1">
                    Válogatott gyümölcsök, intenzív gyümölcsdarabos textúra és természetes ízek
                  </p>
                </div>

                <p data-i18n="prod_cat3_desc" class="text-stone-600 text-xs sm:text-sm leading-relaxed">
                  Magas gyümölcstartalmú, kíméletes főzéssel készült prémium dzsemek egész és vágott gyümölcsdarabokkal. Kifejezetten prémium cukrászati finompékárukhoz, látványpékségi süteményekhez és desszertbetétekhez.
                </p>

                <!-- Available Flavors -->
                <div>
                  <div data-i18n="prod_flavors_label" class="text-[11px] font-mono-spec uppercase tracking-wider text-stone-500 font-semibold mb-2">
                    Elérhető Ízek (Azonos Technológiai Paraméterekkel):
                  </div>
                  <div class="flex flex-wrap gap-1.5">
                    <span data-i18n="flavor_lingonberry" class="px-2 py-0.5 rounded text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">Erdei vörösáfonya</span>
                    <span data-i18n="flavor_apricot_pieces" class="px-2 py-0.5 rounded text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">Sárgabarack darabos</span>
                    <span data-i18n="flavor_blackberry" class="px-2 py-0.5 rounded text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">Feketeszeder</span>
                    <span data-i18n="flavor_raspberry_seeds" class="px-2 py-0.5 rounded text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">Málna magvas</span>
                    <span data-i18n="flavor_wild_strawberry" class="px-2 py-0.5 rounded text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">Szamóca</span>
                    <span data-i18n="flavor_orange_peel" class="px-2 py-0.5 rounded text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">Narancs héjjal</span>
                  </div>
                </div>

                <!-- Applications -->
                <div>
                  <div data-i18n="cat_apps_label_extra" class="text-[11px] font-mono-spec uppercase tracking-wider text-stone-500 font-semibold mb-1.5">
                    Jellemző Prémium Felhasználás:
                  </div>
                  <div class="flex flex-wrap gap-1.5 text-xs text-stone-600 font-mono-spec">
                    <span data-i18n="app_hotel" class="bg-amber-50/80 border border-amber-200/80 px-2 py-0.5 rounded">Szállodai reggeliztetés</span>
                    <span data-i18n="app_plated" class="bg-amber-50/80 border border-amber-200/80 px-2 py-0.5 rounded">Tányérdesszertek</span>
                    <span data-i18n="app_artisan" class="bg-amber-50/80 border border-amber-200/80 px-2 py-0.5 rounded">Látványpéksütemények</span>
                    <span data-i18n="app_macaron" class="bg-amber-50/80 border border-amber-200/80 px-2 py-0.5 rounded">Macaron betétek</span>
                    <span data-i18n="app_tartlet" class="bg-amber-50/80 border border-amber-200/80 px-2 py-0.5 rounded">Tartlet tortácskák</span>
                  </div>
                </div>
              </div>

              <!-- Bottom CTA & Packaging -->
              <div class="pt-5 border-t mt-auto flex flex-col items-start gap-1.5" style="border-color: var(--sv-border-light);">
                <a href="#kapcsolat" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl font-semibold text-xs font-mono-spec transition-all shadow-sm text-white" style="background-color: var(--sv-orange);">
                  <i data-lucide="mail-check" class="w-4 h-4"></i>
                  <span data-i18n="btn_inquire_jam">Érdeklődés & Ajánlatkérés</span>
                </a>
                <span data-i18n="pack_extra_spec" class="text-[11px] font-mono-spec text-stone-400">Kiszerelés: 5 / 10 kg vödör</span>
              </div>

              <!-- Page Number pinned to bottom right -->
              <div class="absolute bottom-5 right-6 z-30 font-mono-spec font-bold text-xs text-stone-500">
                6
              </div>
              <div class="sv-spine-right"></div>
            </section>

          </div>
        </div>

        <!-- Bottom Category Counter and Dots -->
        <div class="mt-8 flex flex-col sm:flex-row items-center justify-between gap-4 px-2">
          
          <!-- Category Indicator Capsule -->
          <div class="inline-flex items-center gap-2.5 px-4 py-1.5 rounded-full bg-white border border-stone-200 text-stone-600 text-xs font-mono-spec">
            <span class="text-[10px] uppercase font-bold tracking-widest text-[#91372d]" data-i18n="cat_category_label">Kategória</span>
            <span id="cat-current-num" class="font-extrabold text-stone-900 text-sm">01</span>
            <span class="text-stone-300 font-normal">/</span>
            <span class="font-bold text-stone-500">03</span>
          </div>

          <!-- Bottom Navigation Pills / Dots -->
          <div class="flex items-center justify-center gap-2.5">
            <button onclick="svFlipGoToCategory(0)" id="cat-dot-0" aria-label="1. Kenhető lekvárok" class="h-2.5 rounded-full transition-all duration-300 w-9 bg-[#a3392e]"></button>
            <button onclick="svFlipGoToCategory(1)" id="cat-dot-1" aria-label="2. Sütésálló lekvárok" class="h-2.5 rounded-full transition-all duration-300 w-3 bg-stone-300 hover:bg-stone-400"></button>
            <button onclick="svFlipGoToCategory(2)" id="cat-dot-2" aria-label="3. Extra dzsemek" class="h-2.5 rounded-full transition-all duration-300 w-3 bg-stone-300 hover:bg-stone-400"></button>
          </div>

          <!-- Hint -->
          <div class="text-[11px] font-mono-spec text-stone-400 flex items-center gap-1.5">
            <i data-lucide="compass" class="w-3.5 h-3.5 text-stone-400"></i>
            <span data-i18n="cat_flip_hint">Lapozzon a nyilakkal, vagy húzza az oldal sarkát</span>
          </div>

        </div>

      </div>

      <!-- ========================================================================= -->
      <!-- MOBILE & TABLET RESPONSIVE CATALOG SHOWCASE (< 1024px)                     -->
      <!-- ========================================================================= -->
      <div class="block lg:hidden mobile-catalog-card w-full max-w-lg mx-auto" id="mobile-catalog-container">
        <div id="mobile-card-shell" class="mobile-card-inner rounded-3xl border bg-white overflow-hidden" style="border-color: var(--sv-border);">
          
          <!-- Mobile Image Top Section (16:9 / 4:3) -->
          <div class="relative w-full h-56 sm:h-72 overflow-hidden bg-stone-100 border-b" style="border-color: var(--sv-border-light);">
            <picture class="w-full h-full block">
              <source id="mob-img-source" srcset="assets/catalog-jam1.webp" type="image/webp">
              <img id="mob-img" src="assets/catalog-jam1.jpg" alt="Termékfotó" width="600" height="400" loading="lazy" decoding="async" class="w-full h-full object-cover object-center">
            </picture>
            <span id="mob-page-indicator" class="absolute bottom-3 left-3 z-10 px-2.5 py-1 rounded-md text-xs font-mono-spec font-bold text-white bg-black/60 backdrop-blur-sm">
              1
            </span>
          </div>

          <!-- Mobile Specs Body Section -->
          <div class="p-5 sm:p-7 space-y-4">
            <div>
              <h3 id="mob-title" class="font-montserrat font-bold text-2xl text-stone-900 leading-tight">
                Kenhető lekvárok
              </h3>
              <p id="mob-subtitle" class="text-xs sm:text-sm text-[#91372d] font-semibold font-mono-spec mt-1">
                Selymes, homogén állag linzerekhez, piskótákhoz és tortalapokhoz
              </p>
            </div>

            <p id="mob-desc" class="text-stone-600 text-xs sm:text-sm leading-relaxed">
              Egyenletesen és könnyedén kenhető, homogén gyümölcskészítmények. Tiszta gyümölcsíz, csomómentes textúra és stabil hidegterülés.
            </p>

            <!-- Flavors -->
            <div>
              <div id="mob-flavors-label" class="text-[11px] font-mono-spec uppercase tracking-wider text-stone-500 font-semibold mb-1.5">
                Elérhető Ízek (Azonos Technológiai Paraméterekkel):
              </div>
              <div id="mob-flavors" class="flex flex-wrap gap-1.5">
                <!-- Dynamically populated -->
              </div>
            </div>

            <!-- Applications -->
            <div>
              <div id="mob-apps-label" class="text-[11px] font-mono-spec uppercase tracking-wider text-stone-500 font-semibold mb-1.5">
                Ajánlott Cukrászati Felhasználás:
              </div>
              <div id="mob-apps" class="flex flex-wrap gap-1.5 text-xs font-mono-spec">
                <!-- Dynamically populated -->
              </div>
            </div>

            <!-- Footer Action -->
            <div class="pt-5 border-t flex flex-col items-start gap-2 mt-6" style="border-color: var(--sv-border-light);">
              <a href="#kapcsolat" class="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-5 py-3 rounded-xl font-semibold text-xs font-mono-spec text-white shadow-sm transition-all transform active:scale-95" style="background-color: var(--sv-orange);">
                <i data-lucide="mail-check" class="w-4 h-4"></i>
                <span data-i18n="btn_inquire_jam">Érdeklődés & Ajánlatkérés</span>
              </a>
              <span id="mob-pack" class="text-[11px] font-mono-spec text-stone-400 text-left">
                Kiszerelés: 5 / 10 / 20 kg
              </span>
            </div>
          </div>

        </div>

        <!-- Mobile Navigation Bar Below Card (No overlap on content!) -->
        <div class="mt-5 flex items-center justify-between gap-3 px-1">
          <button onclick="mobNavPrev()" id="mob-btn-prev" aria-label="Előző kategória" title="Előző kategória"
                  class="w-11 h-11 rounded-full bg-white border border-stone-200 shadow-md flex items-center justify-center text-stone-800 hover:text-white hover:bg-[#a3392e] active:scale-95 transition-all focus:outline-none focus:ring-2 focus:ring-[#a3392e]/40 cursor-pointer disabled:opacity-30 disabled:pointer-events-none">
            <i data-lucide="chevron-left" class="w-5 h-5 stroke-[2.5]"></i>
          </button>

          <div class="flex items-center gap-2">
            <button onclick="mobGoTo(0)" id="mob-dot-0" aria-label="1. Kenhető lekvárok" class="h-2 rounded-full transition-all duration-300 w-8 bg-[#a3392e]"></button>
            <button onclick="mobGoTo(1)" id="mob-dot-1" aria-label="2. Sütésálló lekvárok" class="h-2 rounded-full transition-all duration-300 w-2.5 bg-stone-300 hover:bg-stone-400"></button>
            <button onclick="mobGoTo(2)" id="mob-dot-2" aria-label="3. Extra dzsemek" class="h-2 rounded-full transition-all duration-300 w-2.5 bg-stone-300 hover:bg-stone-400"></button>
          </div>

          <button onclick="mobNavNext()" id="mob-btn-next" aria-label="Következő kategória" title="Következő kategória"
                  class="w-11 h-11 rounded-full bg-white border border-stone-200 shadow-md flex items-center justify-center text-stone-800 hover:text-white hover:bg-[#a3392e] active:scale-95 transition-all focus:outline-none focus:ring-2 focus:ring-[#a3392e]/40 cursor-pointer disabled:opacity-30 disabled:pointer-events-none">
            <i data-lucide="chevron-right" class="w-5 h-5 stroke-[2.5]"></i>
          </button>
        </div>
        
        <div class="text-center mt-2.5 text-[11px] font-mono-spec text-stone-400" data-i18n="cat_flip_hint_mob">
          Lapozzon a nyilakkal, vagy húzza el a kártyát
        </div>
      </div>

      <!-- Standard Domestic Flavor Availability Strip (Embedded into Product Catalog) -->
      <div class="pt-8 border-t mt-10" style="border-color: var(--sv-border-light);">
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-5">
          <div>
            <div class="font-mono-spec text-xs uppercase tracking-widest text-[#91372d] font-semibold" data-i18n="flavors_tag">
              Hagyományos Ízvilág • Korszerű Technológia
            </div>
            <h3 class="font-montserrat font-bold text-xl sm:text-2xl text-stone-900 mt-1" data-i18n="flavors_title">
              Ismerős Ízek. Megbízható Ipari Minőség.
            </h3>
          </div>
          <p class="text-xs sm:text-sm text-stone-600 max-w-xl font-sans" data-i18n="flavors_desc">
            A magyar pékipar és cukrászat legkedveltebb hagyományos gyümölcseit dolgozzuk fel kíméletes eljárással, modern technológiával. A termékeket a partner technológiájához igazítva állítjuk be mind sütésálló, mind hidegen kenhető formában.
          </p>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-7 gap-2.5 font-mono-spec text-xs">
          <div class="p-3 rounded-xl border bg-white flex items-center gap-2 shadow-xs" style="border-color: var(--sv-border-light);">
            <span class="w-2.5 h-2.5 rounded-full bg-orange-400 shrink-0"></span>
            <span class="font-bold text-stone-800" data-i18n="flavor_apricot">Sárgabarack</span>
          </div>
          <div class="p-3 rounded-xl border bg-white flex items-center gap-2 shadow-xs" style="border-color: var(--sv-border-light);">
            <span class="w-2.5 h-2.5 rounded-full bg-purple-950 shrink-0"></span>
            <span class="font-bold text-stone-800" data-i18n="flavor_plum">Szilva</span>
          </div>
          <div class="p-3 rounded-xl border bg-white flex items-center gap-2 shadow-xs" style="border-color: var(--sv-border-light);">
            <span class="w-2.5 h-2.5 rounded-full bg-green-600 shrink-0"></span>
            <span class="font-bold text-stone-800" data-i18n="flavor_apple">Alma</span>
          </div>
          <div class="p-3 rounded-xl border bg-white flex items-center gap-2 shadow-xs" style="border-color: var(--sv-border-light);">
            <span class="w-2.5 h-2.5 rounded-full bg-rose-900 shrink-0"></span>
            <span class="font-bold text-stone-800" data-i18n="flavor_sour_cherry">Meggy</span>
          </div>
          <div class="p-3 rounded-xl border bg-white flex items-center gap-2 shadow-xs" style="border-color: var(--sv-border-light);">
            <span class="w-2.5 h-2.5 rounded-full bg-pink-600 shrink-0"></span>
            <span class="font-bold text-stone-800" data-i18n="flavor_raspberry">Málna</span>
          </div>
          <div class="p-3 rounded-xl border bg-white flex items-center gap-2 shadow-xs" style="border-color: var(--sv-border-light);">
            <span class="w-2.5 h-2.5 rounded-full bg-blue-900 shrink-0"></span>
            <span class="font-bold text-stone-800" data-i18n="flavor_blueberry">Áfonya</span>
          </div>
          <div class="p-3 rounded-xl border bg-white flex items-center gap-2 col-span-2 sm:col-span-2 lg:col-span-1 shadow-xs" style="border-color: var(--sv-border-light);">
            <span class="w-2.5 h-2.5 rounded-full bg-red-700 shrink-0"></span>
            <span class="font-bold text-stone-800" data-i18n="flavor_classic_mixed">Klasszikus Vegyes Gyümölcs</span>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- FOOD-TECH ENGINEERING ADVANTAGES & APPLICATION PHOTOGRAPHY                -->
  <!-- ========================================================================= -->
  <section id="technologia" class="py-16 md:py-24 border-b bg-tech-grid" style="background-color: var(--sv-paper-cream); border-color: var(--sv-border);">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      
      <!-- Section Title -->
      <div class="max-w-3xl mb-12">
        <div class="font-mono-spec text-xs uppercase tracking-widest text-[#91372d] font-semibold mb-2" data-i18n="tech_section_tag">
          Élelmiszer-technológiai Garanciák
        </div>
        <h2 class="font-montserrat font-bold text-3xl sm:text-4xl text-stone-900 leading-snug pb-1" data-i18n="tech_section_title">
          Nem Csak Az Íz Számít. Technológia & Megbízhatóság.
        </h2>
        <p class="text-stone-600 mt-3 text-sm sm:text-base leading-relaxed max-w-2xl" data-i18n="tech_section_desc">
          A finompékáru-gyártásban a selejtképződés legfőbb oka a töltelék kiforrása, a tészta elázása vagy a gépi adagolófejek eldugulása. 
          A Sun Valley Zrt. hidrokolloid- és pektinmátrixa négy technológiai alappillérre épül:
        </p>
      </div>

      <!-- Architectural Matrix Layout (No cards - Clean vertical and horizontal divider lines) -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 lg:gap-0 border-t-2 border-b-2 py-2 lg:py-0" style="border-color: var(--sv-border);">
        
        <!-- Pillar 1: Baking Stability -->
        <article class="pt-6 pb-6 lg:p-6 lg:border-r border-b lg:border-b-0 flex flex-col justify-between" style="border-color: var(--sv-border);">
          <div class="space-y-3.5">
            <div class="flex items-center justify-between">
              <span class="font-mono-spec text-sm font-bold text-[#a3392e]">01</span>
              <span class="text-xs font-mono-spec font-bold px-2.5 py-0.5 rounded text-white bg-[#a3392e]" data-i18n="tech_pillar1_badge">180 °C és 220 °C</span>
            </div>
            <div>
              <span class="text-xs font-mono-spec font-bold uppercase tracking-wider text-[#91372d]" data-i18n="tech_hero_tag">
                Kiemelt Garancia
              </span>
              <h3 class="font-montserrat font-bold text-xl text-stone-900 leading-snug mt-1" data-i18n="tech_card1_title">
                Garantált Sütésállóság
              </h3>
            </div>
            <p class="text-sm sm:text-[0.9375rem] text-stone-700 leading-relaxed" data-i18n="tech_card1_desc">
              Kétféle hőtűrési kategóriában (180 °C-ig és 220 °C-ig). Magas hőfokon sem forr ki a süteményből, nem ég le a tepsire, és megőrzi térfogatát a tésztában szinerézis nélkül.
            </p>

            <ul class="space-y-2 pt-2 font-mono-spec text-xs sm:text-[0.8125rem] text-stone-800">
              <li class="flex items-start gap-1.5">
                <i data-lucide="check" class="w-4 h-4 text-[#a3392e] shrink-0 mt-0.5"></i>
                <span data-i18n="tech_hero_check1">Alaktartó gélmátrix: sütés után sem lapul el.</span>
              </li>
              <li class="flex items-start gap-1.5">
                <i data-lucide="check" class="w-4 h-4 text-[#a3392e] shrink-0 mt-0.5"></i>
                <span data-i18n="tech_hero_check2">Zéró tésztaelázás: nem enged szabad vizet.</span>
              </li>
              <li class="flex items-start gap-1.5">
                <i data-lucide="check" class="w-4 h-4 text-[#a3392e] shrink-0 mt-0.5"></i>
                <span data-i18n="tech_hero_check3">Tiszta tepsik & gépsorok: minimális selejt.</span>
              </li>
            </ul>
          </div>
          <div class="pt-4 mt-4 border-t font-mono-spec text-xs text-[#91372d] font-semibold" style="border-color: var(--sv-border-light);">
            Leveles & kelt tésztákhoz
          </div>
        </article>

        <!-- Pillar 2: Freezing Stability -->
        <article class="pt-6 pb-6 lg:p-6 lg:border-r border-b lg:border-b-0 flex flex-col justify-between" style="border-color: var(--sv-border);">
          <div class="space-y-3.5">
            <div class="flex items-center justify-between">
              <span class="font-mono-spec text-sm font-bold text-[#2D3628]">02</span>
              <span class="text-xs font-mono-spec font-bold px-2.5 py-0.5 rounded text-white bg-[#2D3628]" data-i18n="tech_badge_freeze">
                FAGYASZTÁSÁLLÓ
              </span>
            </div>
            <div>
              <span class="text-xs font-mono-spec font-bold uppercase tracking-wider text-stone-600" data-i18n="tech_pillar2_tag">
                Fagyasztási ciklusstabilitás (Freeze-thaw)
              </span>
              <h3 class="font-montserrat font-bold text-xl text-stone-900 leading-snug mt-1" data-i18n="tech_card2_title">
                Fagyasztásállóság
              </h3>
            </div>
            <p class="text-sm sm:text-[0.9375rem] text-stone-700 leading-relaxed" data-i18n="tech_card2_desc">
              Fagyasztott félkész és fagyasztva tárolt késztermékekhez kifejlesztve. Felengedéskor nem enged levet, nem áztatja el a nyers vagy elősütött tésztát.
            </p>
          </div>
          <div class="pt-4 mt-4 border-t font-mono-spec text-xs text-[#5F6E4D] font-semibold" style="border-color: var(--sv-border-light);">
            Félkész és fagyasztott vonal
          </div>
        </article>

        <!-- Pillar 3: Pumpability & Dosing -->
        <article class="pt-6 pb-6 lg:p-6 lg:border-r border-b lg:border-b-0 flex flex-col justify-between" style="border-color: var(--sv-border);">
          <div class="space-y-3.5">
            <div class="flex items-center justify-between">
              <span class="font-mono-spec text-sm font-bold text-[#91372d]">03</span>
              <span class="text-xs font-mono-spec font-bold px-2.5 py-0.5 rounded text-white bg-[#91372d]" data-i18n="tech_badge_dosing">
                AUTOMATA ADAGOLÁS
              </span>
            </div>
            <div>
              <span class="text-xs font-mono-spec font-bold uppercase tracking-wider text-[#91372d]">
                Viszkozitási Stabilitás
              </span>
              <h3 class="font-montserrat font-bold text-xl text-stone-900 leading-snug mt-1" data-i18n="tech_card3_title">
                Gépi Tölthetőség & Pumpálás
              </h3>
            </div>
            <p class="text-sm sm:text-[0.9375rem] text-stone-700 leading-relaxed" data-i18n="tech_card3_desc">
              A kézi kenéstől a nagyteljesítményű automata tüskés injektálósorokig nyírásstabil viszkozitást garantálunk: a töltelék nem csöpög, és nem tömíti el az adagolófejeket.
            </p>
          </div>
          <div class="pt-4 mt-4 border-t font-mono-spec text-xs text-[#91372d] font-semibold" style="border-color: var(--sv-border-light);">
            Tüskés és volumetrikus sorok
          </div>
        </article>

        <!-- Pillar 4: Packaging Scale & Slicing -->
        <article class="pt-6 pb-6 lg:p-6 flex flex-col justify-between" style="border-color: var(--sv-border);">
          <div class="space-y-3.5">
            <div class="flex items-center justify-between">
              <span class="font-mono-spec text-sm font-bold text-stone-700">04</span>
              <span class="text-xs font-mono-spec font-bold px-2.5 py-0.5 rounded text-white bg-stone-800">
                5 KG • 10 KG • 20 KG • 200 KG
              </span>
            </div>
            <div>
              <span class="text-xs font-mono-spec font-bold uppercase tracking-wider text-stone-600">
                Ipari Logisztikai Skála
              </span>
              <h3 class="font-montserrat font-bold text-xl text-stone-900 leading-snug mt-1" data-i18n="tech_card4_title">
                Kis Szériától Ipari Léptékig
              </h3>
            </div>
            <p class="text-sm sm:text-[0.9375rem] text-stone-700 leading-relaxed" data-i18n="tech_card4_desc">
              A kiszerelést a felhasználó volumenéhez igazítjuk: 5 kg-os vödrös egységek kézműves cukrászatoknak, 10–20 kg-os tömbök péküzemeknek, vagy 200 kg-os aszeptikus hordók ipari nagyüzemeknek.
            </p>
          </div>
          <div class="pt-4 mt-4 border-t font-mono-spec text-xs text-stone-600 font-semibold" style="border-color: var(--sv-border-light);">
            Tölthető tömb és vödrös
          </div>
        </article>

      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- CÉGÜNKRŐL & MÓRI ÜZEM – COMPANY HERITAGE & INDUSTRIAL PHILOSOPHY          -->
  <!-- ========================================================================= -->
  <section id="cegunkrol" class="py-16 md:py-24 border-b transition-colors" style="background-color: var(--sv-burgundy); color: #F5F2EE; border-color: rgba(255,255,255,0.15);">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      
      <!-- Eyebrow & Lead Header -->
      <div class="max-w-3xl mb-10">
        <h2 class="font-montserrat font-bold text-3xl sm:text-4xl md:text-5xl text-white leading-tight pb-1" data-i18n="about_title">
          Gyártási háttér és szakmai múlt
        </h2>
      </div>

      <!-- Asymmetrical 2-Column Presentation -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 xl:gap-14 items-stretch">
        
        <!-- Left Column: Story, Tradition & Tailored Solutions (Span 7) -->
        <div class="lg:col-span-7 space-y-6">
          <div class="p-7 sm:p-10 rounded-2xl border border-white/20 bg-white/10 backdrop-blur-sm space-y-6">
            <div class="flex items-center gap-3.5 pb-2 border-b border-white/10">
              <span class="w-12 h-12 rounded-xl flex items-center justify-center font-montserrat font-bold text-xl text-[#a3392e] bg-white shrink-0">
                SV
              </span>
              <div>
                <h3 class="font-montserrat font-extrabold text-xl sm:text-2xl text-white leading-snug" data-i18n="about_card_title">
                  Több mint 30 éves szakmai tapasztalat a gyümölcsfeldolgozásban
                </h3>
                <p class="text-xs sm:text-sm font-mono-spec text-[#FBBB9C] mt-0.5" data-i18n="about_card_sub">
                  Családi gyökerekből a hazai sütőipar megbízható beszállítója
                </p>
              </div>
            </div>
            
            <p class="text-white text-base sm:text-lg lg:text-[1.125rem] leading-relaxed sm:leading-loose border-l-4 border-[#D48054] pl-4 sm:pl-5 font-medium" data-i18n="about_p1">
              A Sun Valley szakmai alapjai több mint három évtizedes családi gyümölcsfeldolgozási hagyományra épülnek, amely 2009 óta önálló ipari gyártóként szolgálja ki a hazai és regionális sütőipart.
            </p>

            <p class="text-white/95 text-base sm:text-lg lg:text-[1.05rem] leading-relaxed sm:leading-loose font-normal" data-i18n="about_p2">
              A hagyományos gyümölcsös ízeket korszerű gyártási megoldásokkal és folyamatos termékfejlesztéssel ötvözzük móri üzemünkben. Lekvárjainkat és ipari gyümölcstöltelékeinket nemcsak az elvárt ízvilág, hanem a felhasználási terület, a kívánt állag és a partner gyártási technológiája alapján alakítjuk ki.
            </p>

            <p class="text-white/90 text-sm sm:text-base lg:text-[1rem] leading-relaxed sm:leading-loose font-normal" data-i18n="about_p3">
              Hiszünk a hosszú távú együttműködésekben és a közös gondolkodásban. Célunk, hogy rugalmas, megbízható és egyedileg kialakított megoldásainkkal hozzájáruljunk partnereink termékeinek sikeréhez. Számunkra partnereink elégedettsége nemcsak üzleti cél, hanem működésünk alapja.
            </p>
          </div>
        </div>

        <!-- Right Column: Visual Image (Span 5) - Vertically Stretched -->
        <div class="lg:col-span-5 h-full flex flex-col">
          <div class="rounded-2xl overflow-hidden border border-white/20 relative bg-black/20 group flex-1 h-full min-h-[340px] sm:min-h-[420px]">
            <picture class="w-full h-full block">
              <source srcset="assets/fruit-forest1.webp" type="image/webp">
              <img src="assets/fruit-forest1.jpg" alt="Sun Valley magyar gyümölcsfeldolgozás Mór" width="600" height="600" loading="lazy" decoding="async" class="w-full h-full min-h-[340px] sm:min-h-[420px] object-cover object-center">
            </picture>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- EGYEDI RECEPTÚRA – CUSTOM RECIPE R&D PIPELINE                             -->
  <!-- ========================================================================= -->
  <section id="egyedi-fejlesztes" class="py-16 md:py-24 border-b" style="border-color: var(--sv-border); background-color: var(--sv-green-dark);">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">

      <!-- Header: title left, description right -->
      <div class="flex flex-col lg:flex-row lg:items-start lg:justify-between gap-6 lg:gap-16 mb-10 md:mb-14">
        <div class="lg:max-w-[55%]">
          <div class="font-mono-spec text-xs uppercase tracking-widest font-semibold mb-3" style="color: var(--sv-gold);" data-i18n="rd_section_tag">
            Egyedi receptúra
          </div>
          <h2 class="font-montserrat font-bold text-3xl sm:text-4xl md:text-[2.75rem] leading-snug pb-1" style="color: var(--sv-paper-cream);">
            <span data-i18n="rd_section_title_p1">Az Ön ötlete.</span><br>
            <em class="not-italic" style="color: var(--sv-gold);" data-i18n="rd_section_title_p2">Közös fejlesztés.</em>
          </h2>
        </div>
        <div class="lg:max-w-[40%] lg:pt-10">
          <p class="text-sm sm:text-base leading-relaxed" style="color: rgba(245,242,238,0.8);" data-i18n="rd_section_desc">
            Nem minden gyártósor és késztermék egyforma. Az egyedi receptúra-fejlesztés kiindulópontja az Ön technológiája és a kívánt végeredmény.
          </p>
        </div>
      </div>

      <!-- Exotic & Tropical Fruit R&D Capabilities (Integrated Proof of Custom Development) -->
      <div class="mb-10 md:mb-12 p-6 sm:p-7 rounded-2xl border bg-black/15 backdrop-blur-xs" style="border-color: rgba(255, 255, 255, 0.15);">
        <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-4 mb-4">
          <div>
            <div class="font-mono-spec text-xs uppercase tracking-widest font-semibold" style="color: var(--sv-gold);" data-i18n="exotic_tag">
              Egyedi Fejlesztési Irányok • Innováció
            </div>
            <h3 class="font-montserrat font-bold text-xl sm:text-2xl mt-1" style="color: var(--sv-paper-cream);" data-i18n="exotic_title">
              Egzotikus Ízek. Az Ön Termékére Hangolva.
            </h3>
          </div>
          <p class="text-xs sm:text-sm max-w-xl leading-relaxed" style="color: rgba(245,242,238,0.8);" data-i18n="exotic_desc">
            Az alapízeken túl trópusi és egzotikus gyümölcsökből is fejlesztünk egyedi receptúrát a kívánt ízprofilhoz és gyártási folyamathoz. Legyen szó mangóról, maracujáról vagy citrusfélékről, élelmiszer-technológusaink a megadott viszkozitási és Brix-értékekre kalibrálják a tölteléket.
          </p>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2.5 font-mono-spec text-xs">
          <div class="p-2.5 rounded-xl border bg-white/10 flex items-center gap-2 text-stone-100" style="border-color: rgba(255, 255, 255, 0.12);">
            <span class="w-2.5 h-2.5 rounded-full bg-amber-400 shrink-0"></span>
            <span class="font-semibold" data-i18n="flavor_mango">Mangó</span>
          </div>
          <div class="p-2.5 rounded-xl border bg-white/10 flex items-center gap-2 text-stone-100" style="border-color: rgba(255, 255, 255, 0.12);">
            <span class="w-2.5 h-2.5 rounded-full bg-fuchsia-400 shrink-0"></span>
            <span class="font-semibold" data-i18n="flavor_maracuja">Maracuja</span>
          </div>
          <div class="p-2.5 rounded-xl border bg-white/10 flex items-center gap-2 text-stone-100" style="border-color: rgba(255, 255, 255, 0.12);">
            <span class="w-2.5 h-2.5 rounded-full bg-yellow-400 shrink-0"></span>
            <span class="font-semibold" data-i18n="flavor_pineapple">Ananász</span>
          </div>
          <div class="p-2.5 rounded-xl border bg-white/10 flex items-center gap-2 text-stone-100" style="border-color: rgba(255, 255, 255, 0.12);">
            <span class="w-2.5 h-2.5 rounded-full bg-lime-400 shrink-0"></span>
            <span class="font-semibold" data-i18n="flavor_kiwi">Kivi</span>
          </div>
          <div class="p-2.5 rounded-xl border bg-white/10 flex items-center gap-2 text-stone-100" style="border-color: rgba(255, 255, 255, 0.12);">
            <span class="w-2.5 h-2.5 rounded-full bg-amber-300 shrink-0"></span>
            <span class="font-semibold" data-i18n="flavor_citrus">Citrus</span>
          </div>
          <div class="p-2.5 rounded-xl border bg-white/10 flex items-center gap-2 text-stone-100" style="border-color: rgba(255, 255, 255, 0.12);">
            <span class="w-2.5 h-2.5 rounded-full bg-orange-400 shrink-0"></span>
            <span class="font-semibold" data-i18n="flavor_orange">Narancs</span>
          </div>
        </div>

        <p class="text-[11px] font-mono-spec mt-3" style="color: rgba(245,242,238,0.6);" data-i18n="exotic_note">
          * Az egzotikus receptúrákat technológiai egyeztetés és receptúra-fejlesztés alapján véglegesítjük a partner saját gépsoraira.
        </p>
      </div>

      <!-- Full-width product image -->
      <div class="rounded-2xl overflow-hidden mb-12 md:mb-16">
        <img src="assets/custom-recipe-jam-sizes.png" alt="Sun Valley egyedi receptúra – lekvárok és gyümölcstöltelékek különböző kiszerelésekben" width="1957" height="804" class="w-full h-auto object-cover" loading="lazy" decoding="async">
      </div>

      <!-- 3 numbered article steps connected visually -->
      <div class="relative">
        <!-- Desktop connecting horizontal line behind numbers -->
        <div class="hidden md:block absolute top-[11px] left-[5%] right-[5%] h-0.5 bg-white/20 pointer-events-none z-0" aria-hidden="true"></div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 md:gap-10 relative z-10">

          <!-- Step 1 -->
          <article class="flex md:flex-col items-start gap-4 md:gap-0 pl-3 md:pl-0 border-l-2 md:border-l-0 border-white/25 md:border-transparent">
            <span class="w-7 h-7 rounded-full bg-[#2D3628] border-2 border-[#D48054] text-[#D48054] font-mono-spec text-xs font-bold flex items-center justify-center shrink-0 md:mb-4 shadow-sm">
              01
            </span>
            <div>
              <h3 class="font-montserrat font-bold text-lg sm:text-xl mb-2" style="color: var(--sv-paper-cream);" data-i18n="rd_step1_title">
                Az igény megismerése
              </h3>
              <p class="text-sm leading-relaxed" style="color: rgba(245,242,238,0.7);" data-i18n="rd_step1_desc">
                Felhasználás, ízvilág, állag, összetétel és technológiai feltételek egyeztetése.
              </p>
            </div>
          </article>

          <!-- Step 2 -->
          <article class="flex md:flex-col items-start gap-4 md:gap-0 pl-3 md:pl-0 border-l-2 md:border-l-0 border-white/25 md:border-transparent">
            <span class="w-7 h-7 rounded-full bg-[#2D3628] border-2 border-[#D48054] text-[#D48054] font-mono-spec text-xs font-bold flex items-center justify-center shrink-0 md:mb-4 shadow-sm">
              02
            </span>
            <div>
              <h3 class="font-montserrat font-bold text-lg sm:text-xl mb-2" style="color: var(--sv-paper-cream);" data-i18n="rd_step2_title">
                Receptúra és próba
              </h3>
              <p class="text-sm leading-relaxed" style="color: rgba(245,242,238,0.7);" data-i18n="rd_step2_desc">
                A megfelelő megoldás kialakítása, majd a termék értékelése a tervezett felhasználásban.
              </p>
            </div>
          </article>

          <!-- Step 3 -->
          <article class="flex md:flex-col items-start gap-4 md:gap-0 pl-3 md:pl-0 border-l-2 md:border-l-0 border-white/25 md:border-transparent">
            <span class="w-7 h-7 rounded-full bg-[#2D3628] border-2 border-[#D48054] text-[#D48054] font-mono-spec text-xs font-bold flex items-center justify-center shrink-0 md:mb-4 shadow-sm">
              03
            </span>
            <div>
              <h3 class="font-montserrat font-bold text-lg sm:text-xl mb-2" style="color: var(--sv-paper-cream);" data-i18n="rd_step3_title">
                Gyártásra hangolva
              </h3>
              <p class="text-sm leading-relaxed" style="color: rgba(245,242,238,0.7);" data-i18n="rd_step3_desc">
                A végleges specifikáció, kiszerelés és rendelési igények összehangolása.
              </p>
            </div>
          </article>

        </div>
      </div>

      <!-- Direct R&D Call-to-Action to #kapcsolat -->
      <div class="mt-12 md:mt-14 pt-8 border-t border-white/15 flex flex-col sm:flex-row items-center justify-between gap-6">
        <p class="text-xs sm:text-sm text-white/80 font-mono-spec text-center sm:text-left" data-i18n="rd_cta_hint">
          Saját gépsorra kalibrált viszkozitás, egyedi Brix és gyümölcstartalom.
        </p>
        <a href="#kapcsolat" 
           class="inline-flex items-center justify-center gap-2.5 px-7 py-3.5 rounded-xl font-bold text-sm text-white transition-all transform active:scale-95 shadow-md hover:shadow-lg shrink-0"
           style="background-color: var(--sv-orange);">
          <i data-lucide="flask-conical" class="w-4 h-4"></i>
          <span data-i18n="rd_cta_btn">Egyedi receptúra egyeztetése</span>
        </a>
      </div>

    </div>
  </section>



  <!-- ========================================================================= -->
  <!-- DISCREET B2B PROSPECTUS RESOURCE STRIP                                    -->
  <!-- ========================================================================= -->
  <section id="prospektus" class="py-5 border-b transition-colors" style="background-color: var(--sv-paper-cream); color: var(--sv-text); border-color: var(--sv-border);">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      <div class="rounded-xl px-5 py-3.5 border bg-white flex flex-col md:flex-row items-center justify-between gap-4"
           style="border-color: var(--sv-border);">
        
        <div class="flex items-center gap-3.5 text-center md:text-left">
          <div class="w-9 h-9 rounded-lg flex items-center justify-center shrink-0" style="background-color: rgba(163, 57, 46, 0.08); color: var(--sv-burgundy);">
            <i data-lucide="file-text" class="w-4 h-4"></i>
          </div>
          <div>
            <div class="flex items-center gap-2 justify-center md:justify-start">
              <span class="font-montserrat font-bold text-sm text-stone-900" data-i18n="prospectus_title">Sun Valley Vállalati Prospektus</span>
              <span class="text-[10px] font-mono-spec px-1.5 py-0.5 rounded bg-stone-100 text-stone-600 border border-stone-200">PDF • 2026</span>
            </div>
            <p class="text-xs text-stone-600 font-mono-spec mt-0.5" data-i18n="prospectus_desc">
              Termékkínálatunk, technológiai hátterünk és minőségi garanciáink hivatalos összefoglalója.
            </p>
          </div>
        </div>

        <div class="shrink-0">
          <a href="assets/Sun_Valley_B2B_Prospektus.pdf" target="_blank" rel="noopener noreferrer"
             class="inline-flex items-center gap-2 px-4 py-2 rounded-lg font-semibold text-xs border text-stone-800 bg-white hover:bg-stone-50 hover:border-stone-400 transition-all active:scale-95"
             style="border-color: var(--sv-border);">
            <i data-lucide="download" class="w-3.5 h-3.5 text-stone-600"></i>
            <span data-i18n="btn_download_prospectus">Vállalati ismertető (PDF)</span>
          </a>
        </div>

      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- DEDIKÁLT AJÁNLATKÉRÉSI ÉS KAPCSOLATI SZEKCIÓ                              -->
  <!-- ========================================================================= -->
  <!-- ========================================================================= -->
  <!-- DEDIKÁLT AJÁNLATKÉRÉSI ÉS KAPCSOLATI SZEKCIÓ                              -->
  <!-- ========================================================================= -->
  <section id="kapcsolat" class="py-16 md:py-24 border-b" style="background-color: var(--sv-surface); border-color: var(--sv-border);">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-12 items-start">
        
        <!-- Bal oldal: Felhívás és közvetlen elérhetőségek -->
        <div class="lg:col-span-7 space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-lg text-xs font-mono-spec uppercase tracking-wider font-semibold border shadow-xs"
               style="background-color: rgba(163, 57, 46, 0.08); color: var(--sv-burgundy); border-color: rgba(163, 57, 46, 0.2);">
            <i data-lucide="factory" class="w-3.5 h-3.5 text-[#a3392e]"></i>
            <span data-i18n="contact_sec_tag">Közvetlen gyári egyeztetés</span>
          </div>

          <h2 class="font-montserrat font-bold text-3xl sm:text-4xl text-stone-900 leading-tight" data-i18n="contact_sec_title">
            Kérjen közvetlen gyári árajánlatot vagy technológiai egyeztetést
          </h2>

          <p class="text-stone-600 text-base leading-relaxed" data-i18n="contact_sec_lead">
            Nagyüzemi sütő- és kenyérgyári megrendelések, egyedi receptúrák és próbagyártások esetén vegye fel a kapcsolatot közvetlenül cégvezetésünkkel:
          </p>

          <!-- Direct Management Contact Card -->
          <div class="p-6 sm:p-8 rounded-2xl border bg-stone-50/60 shadow-xs space-y-5" style="border-color: var(--sv-border);">
            <div class="flex items-center justify-between flex-wrap gap-2">
              <div>
                <div class="font-bold text-stone-900 text-xl font-montserrat" data-i18n="contact_person_name">ifj. Vécsei András</div>
                <div class="text-xs font-mono-spec text-[#91372d] uppercase tracking-wider font-semibold mt-0.5" data-i18n="contact_person_title">Kereskedelem & Cégvezetés</div>
              </div>
              <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-[11px] font-mono-spec font-medium bg-emerald-100 text-emerald-800 border border-emerald-200">
                <span class="w-2 h-2 rounded-full bg-emerald-600"></span>
                <span data-i18n="contact_ready_badge">Gyári egyeztetés nyitott</span>
              </span>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-3 border-t" style="border-color: var(--sv-border-light);">
              <!-- Call -->
              <a href="tel:+36308998548" 
                 class="flex items-center gap-3 p-3 rounded-xl border bg-white hover:border-[#a3392e] text-stone-900 hover:text-[#91372d] transition-all shadow-xs group">
                <div class="w-10 h-10 rounded-lg flex items-center justify-center shrink-0 bg-red-50 text-[#a3392e] group-hover:bg-[#a3392e] group-hover:text-white transition-colors">
                  <i data-lucide="phone" class="w-5 h-5"></i>
                </div>
                <div>
                  <span class="block text-[10px] font-mono-spec uppercase tracking-wider text-stone-500" data-i18n="contact_phone_label">Közvetlen mobil</span>
                  <span class="font-mono-spec font-bold text-sm sm:text-base">+36 30 899 8548</span>
                </div>
              </a>

              <!-- Direct Email -->
              <a href="mailto:ifj.vecsei.andras@sunvalley.hu" 
                 class="flex items-center gap-3 p-3 rounded-xl border bg-white hover:border-[#a3392e] text-stone-900 hover:text-[#91372d] transition-all shadow-xs group">
                <div class="w-10 h-10 rounded-lg flex items-center justify-center shrink-0 bg-red-50 text-[#a3392e] group-hover:bg-[#a3392e] group-hover:text-white transition-colors">
                  <i data-lucide="mail" class="w-5 h-5"></i>
                </div>
                <div class="overflow-hidden">
                  <span class="block text-[10px] font-mono-spec uppercase tracking-wider text-stone-500" data-i18n="contact_email_label">Gyári e-mail</span>
                  <span class="font-mono-spec font-bold text-xs sm:text-sm truncate block">ifj.vecsei.andras@sunvalley.hu</span>
                </div>
              </a>
            </div>

            <!-- 1-Click Mailto Composer Trigger -->
            <div class="pt-2">
              <button onclick="launchInquiryComposer()" 
                      type="button"
                      class="w-full inline-flex items-center justify-center gap-2.5 px-6 py-3.5 rounded-xl font-bold text-sm text-white shadow-md hover:shadow-lg transition-all active:scale-98"
                      style="background-color: var(--sv-burgundy);"
                      onmouseover="this.style.backgroundColor='var(--sv-burgundy-hover)'"
                      onmouseout="this.style.backgroundColor='var(--sv-burgundy)'">
                <i data-lucide="send" class="w-4 h-4"></i>
                <span data-i18n="contact_compose_btn">Előre formázott ajánlatkérés küldése e-mailben</span>
              </button>
              <p class="text-[11px] font-mono-spec text-stone-500 text-center mt-2" data-i18n="contact_compose_hint">
                Megnyitja levelezőjét a gyári specifikációs sablonnal kitöltve.
              </p>
            </div>
          </div>
        </div>

        <!-- Jobb oldal: Ajánlatkérési ellenőrzőlista (segíti a pontos specifikálást) -->
        <div class="lg:col-span-5 p-6 sm:p-8 rounded-2xl border bg-white shadow-xs space-y-4" style="border-color: var(--sv-border);">
          <div class="flex items-center gap-2.5 text-xs font-mono-spec font-semibold uppercase tracking-wider" style="color: var(--sv-burgundy);">
            <i data-lucide="clipboard-check" class="w-4 h-4"></i>
            <span data-i18n="contact_checklist_tag">Műszaki Ellenőrzőlista</span>
          </div>

          <h3 class="font-montserrat font-bold text-xl text-stone-900 leading-snug" data-i18n="contact_checklist_title">
            Mit érdemes megadni az ajánlatkérésben?
          </h3>
          <p class="text-xs text-stone-600 leading-relaxed font-sans" data-i18n="contact_checklist_desc">
            A gyors és pontos specifikációhoz kérjük, tüntesse fel az alábbi adatokat a megkeresésben:
          </p>
          <ul class="space-y-3.5 text-xs sm:text-sm text-stone-700 font-mono-spec pt-2">
            <li class="flex items-start gap-3">
              <span class="w-5 h-5 rounded-md bg-red-50 text-[#a3392e] flex items-center justify-center shrink-0 mt-0.5 font-bold text-xs border border-red-200">1</span>
              <div>
                <strong class="text-stone-900 block font-semibold" data-i18n="contact_check_app_h">Tervezett felhasználás</strong>
                <span class="text-stone-600 text-xs" data-i18n="contact_check_app">pl. leveles tészta, kelt bukta, linzer, tortalap</span>
              </div>
            </li>
            <li class="flex items-start gap-3">
              <span class="w-5 h-5 rounded-md bg-red-50 text-[#a3392e] flex items-center justify-center shrink-0 mt-0.5 font-bold text-xs border border-red-200">2</span>
              <div>
                <strong class="text-stone-900 block font-semibold" data-i18n="contact_check_dosing_h">Adagolási technológia</strong>
                <span class="text-stone-600 text-xs" data-i18n="contact_check_dosing">kézi kenés vagy automata injektálósor</span>
              </div>
            </li>
            <li class="flex items-start gap-3">
              <span class="w-5 h-5 rounded-md bg-red-50 text-[#a3392e] flex items-center justify-center shrink-0 mt-0.5 font-bold text-xs border border-red-200">3</span>
              <div>
                <strong class="text-stone-900 block font-semibold" data-i18n="contact_check_heat_h">Kívánt hőtűrés</strong>
                <span class="text-stone-600 text-xs" data-i18n="contact_check_heat">hideg technológia, 180 °C vagy 220 °C</span>
              </div>
            </li>
            <li class="flex items-start gap-3">
              <span class="w-5 h-5 rounded-md bg-red-50 text-[#a3392e] flex items-center justify-center shrink-0 mt-0.5 font-bold text-xs border border-red-200">4</span>
              <div>
                <strong class="text-stone-900 block font-semibold" data-i18n="contact_check_volume_h">Volumen & kiszerelés</strong>
                <span class="text-stone-600 text-xs" data-i18n="contact_check_volume">becsült havi tétel; vödör (5–20 kg) vagy tömb / hordó</span>
              </div>
            </li>
          </ul>
        </div>

      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- UNIFIED CONTACT & FOOTER SECTION                                          -->
  <!-- ========================================================================= -->
  <footer id="site-footer" class="pt-16 pb-12 text-xs font-mono-spec transition-colors"
          style="background-color: var(--sv-burgundy-dark); color: rgba(245, 242, 238, 0.75); border-top: 1px solid rgba(255,255,255,0.1);">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      
      <!-- Top Grid: Brand / Information / Direct Contacts -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 md:gap-0">
        
        <!-- Left Column: Brand Emblem & Corporate ID (Hesi reference layout) -->
        <div class="md:pr-8 md:border-r flex flex-col justify-between" style="border-color: rgba(245,242,238,0.15);">
          <div>
            <div class="flex items-center gap-3">
              <img src="assets/sun-valley-logo.webp" alt="Sun Valley Zrt. Logo" width="160" height="44" loading="lazy" decoding="async" class="h-10 w-auto object-contain">
              <div>
                <div class="font-montserrat font-bold text-white text-base tracking-tight leading-none">Sun Valley Zrt.</div>
                <div class="text-[10px] text-white/60 mt-1 font-mono-spec" data-i18n="footer_tagline">Ipari Gyümölcstechnológia Mór</div>
              </div>
            </div>
            <p class="text-xs text-white/70 leading-relaxed mt-4 font-sans" data-i18n="footer_brand_desc">
              B2B élelmiszeripari partner. Nagyüzemi sütésálló és kenhető gyümölcstöltelékek közvetlenül a gyártótól.
            </p>
          </div>
        </div>

        <!-- Col 1: Információk -->
        <div class="md:px-8 pt-6 md:pt-0 border-t md:border-t-0 md:border-r" style="border-color: rgba(245,242,238,0.15);">
          <div class="text-xs font-mono-spec uppercase tracking-wider font-semibold text-white mb-4" data-i18n="footer_col_info">
            Információk
          </div>
          <ul class="space-y-2.5 text-xs text-white/80 font-sans">
            <li>
              <a href="#termekek" class="hover:text-white hover:underline transition-colors block" data-i18n="footer_link_catalog">
                Termékkatalógus
              </a>
            </li>
            <li>
              <a href="#technologia" class="hover:text-white hover:underline transition-colors block" data-i18n="footer_link_tech">
                Technológia & Minőség
              </a>
            </li>
            <li>
              <a href="#cegunkrol" class="hover:text-white hover:underline transition-colors block" data-i18n="footer_link_about">
                Cégünkről
              </a>
            </li>
            <li>
              <a href="#egyedi-fejlesztes" class="hover:text-white hover:underline transition-colors block" data-i18n="footer_link_rd">
                Egyedi receptúra
              </a>
            </li>
            <li>
              <a href="assets/Sun_Valley_B2B_Prospektus.pdf" target="_blank" rel="noopener noreferrer" class="hover:text-white hover:underline transition-colors block" data-i18n="btn_download_prospectus">
                Vállalati ismertető megnyitása (PDF)
              </a>
            </li>
            <li>
              <button onclick="openPrivacyModal()" class="hover:text-white hover:underline transition-colors text-left" data-i18n="footer_privacy_link">
                Adatkezelési tájékoztató
              </button>
            </li>
          </ul>
        </div>

        <!-- Col 2: Elérhetőségek (Mobil, Email, Telephely + Térkép) -->
        <div class="md:pl-8 pt-6 md:pt-0 border-t md:border-t-0" style="border-color: rgba(245,242,238,0.15);">
          <div class="text-xs font-mono-spec uppercase tracking-wider font-semibold text-white mb-4" data-i18n="footer_col_contact">
            Elérhetőségek
          </div>
          <div class="space-y-4">
            <!-- Mobil -->
            <div class="flex items-center gap-3">
              <i data-lucide="phone" class="w-4 h-4 shrink-0" style="color: var(--sv-gold);"></i>
              <a href="tel:+36308998548" class="font-bold text-sm text-white hover:underline font-mono-spec">
                +36 30 899 8548
              </a>
            </div>
            <!-- Email -->
            <div class="flex items-center gap-3">
              <i data-lucide="mail" class="w-4 h-4 shrink-0" style="color: var(--sv-gold);"></i>
              <a href="mailto:ifj.vecsei.andras@sunvalley.hu" class="text-xs text-white hover:underline font-mono-spec break-all">
                ifj.vecsei.andras@sunvalley.hu
              </a>
            </div>
            <!-- Telephely -->
            <div class="flex items-start gap-3">
              <i data-lucide="map-pin" class="w-4 h-4 shrink-0 mt-0.5" style="color: var(--sv-gold);"></i>
              <div>
                <div class="text-xs font-semibold text-white">8060 Mór, Major utca 3.</div>
                <div class="text-[10px] text-white/50 font-mono-spec mt-0.5">Hrsz. 3601/1 • Fejér vármegye</div>
                <a href="https://maps.google.com/?q=8060+Mór+Major+utca+3" target="_blank" rel="noopener" 
                   class="inline-flex items-center gap-1 text-[11px] font-semibold hover:underline mt-1.5" style="color: var(--sv-gold);">
                  <span data-i18n="link_google_maps">Megtekintés Google Térképen &rarr;</span>
                </a>
              </div>
            </div>
          </div>
        </div>

      </div>

      <!-- Bottom Copyright Row (Clean, no badges) -->
      <div class="mt-12 pt-6 border-t flex flex-col sm:flex-row items-center justify-between gap-4 text-[11px] text-white/50"
           style="border-color: rgba(255,255,255,0.1);">
        <div>
          <span data-i18n="footer_rights">© 2026 Sun Valley Kereskedelmi Zrt. • Minden jog fenntartva.</span>
        </div>
      </div>

    </div>
  </footer>


  <!-- ========================================================================= -->
  <!-- PRIVACY / GDPR MODAL DIALOGUE                                             -->
  <!-- ========================================================================= -->
  <div id="privacy-modal" class="fixed inset-0 z-50 bg-black/65 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-xl w-full max-h-[90vh] overflow-y-auto border shadow-2xl p-6 sm:p-8 relative font-sans"
         style="border-color: var(--sv-border);">
      
      <!-- Close Button -->
      <button onclick="closePrivacyModal()" class="absolute top-5 right-5 p-2 rounded-xl border text-stone-500 hover:text-stone-900 transition-colors" style="border-color: var(--sv-border-light);" aria-label="Ablak bezárása">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>

      <div class="space-y-4">
        <div class="flex items-center gap-2.5 text-xs font-mono-spec font-semibold uppercase tracking-wider" style="color: var(--sv-burgundy);">
          <i data-lucide="shield-check" class="w-4 h-4"></i>
          <span data-i18n="privacy_modal_tag">GDPR & Adatvédelem</span>
        </div>

        <h3 class="font-montserrat font-bold text-xl sm:text-2xl text-stone-900" data-i18n="privacy_modal_title">
          Adatkezelési Tájékoztató
        </h3>

        <div class="text-xs sm:text-sm text-stone-600 leading-relaxed space-y-3 font-sans">
          <p data-i18n="privacy_modal_p1">
            A Sun Valley Kereskedelmi Zrt. (Székhely: 1138 Budapest, Váci út 186., Gyártóbázis: 8060 Mór, Major utca 3.) elkötelezett üzleti partnerei személyes adatainak védelme iránt.
          </p>
          <p data-i18n="privacy_modal_p2">
            A közvetlen kapcsolatfelvétel (telefon, e-mail) során átadott szakmai adatokat kizárólag árajánlatadás, mintaküldés és szerződéskötés céljából kezeljük a GDPR és a hazai jogszabályok előírásainak megfelelően.
          </p>
          <p data-i18n="privacy_modal_p3">
            A megadott adatokat harmadik fél részére marketing célból nem értékesítjük és nem továbbítjuk.
          </p>
        </div>

        <div class="pt-4 border-t flex justify-end" style="border-color: var(--sv-border-light);">
          <button onclick="closePrivacyModal()" class="px-5 py-2.5 rounded-xl border font-mono-spec text-xs font-semibold text-stone-700 hover:bg-stone-50 transition-colors">
            <span data-i18n="privacy_modal_close">Bezárás</span>
          </button>
        </div>
      </div>

    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- JAVASCRIPT: DATA, I18N, KATALÓGUS TABS, TDS MODAL, INTERACTIVITY          -->
  <!-- ========================================================================= -->
  <script>
    // ---------------------------------------------------------------------------
    // TRILINGUAL I18N DICTIONARY (Domain-Modeling Enforced)
    // ---------------------------------------------------------------------------
    const translations = {
      hu: {

        about_title: "Gyártási háttér és szakmai múlt",
        about_card_title: "Több mint 30 éves szakmai tapasztalat a gyümölcsfeldolgozásban",
        about_card_sub: "Családi gyökerekből a hazai sütőipar megbízható beszállítója",
        about_p1: "A Sun Valley szakmai alapjai több mint három évtizedes családi gyümölcsfeldolgozási hagyományra épülnek, amely 2009 óta önálló ipari gyártóként szolgálja ki a hazai és regionális sütőipart.",
        about_p2: "A hagyományos gyümölcsös ízeket korszerű gyártási megoldásokkal és folyamatos termékfejlesztéssel ötvözzük móri üzemünkben. Lekvárjainkat és ipari gyümölcstöltelékeinket nemcsak az elvárt ízvilág, hanem a felhasználási terület, a kívánt állag és a partner gyártási technológiája alapján alakítjuk ki.",
        about_p3: "Hiszünk a hosszú távú együttműködésekben és a közös gondolkodásban. Célunk, hogy rugalmas, megbízható és egyedileg kialakított megoldásainkkal hozzájáruljunk partnereink termékeinek sikeréhez. Számunkra partnereink elégedettsége nemcsak üzleti cél, hanem működésünk alapja.",
        cookie_notice: "Weboldalunk az alapvető működéshez és a nyelvi beállítások mentéséhez szükséges sütiket használ.",
        cookie_accept: "Rendben",
        privacy_modal_p1: "A Sun Valley Kereskedelmi Zrt. (Székhely: 1138 Budapest, Váci út 186., Gyártóbázis: 8060 Mór, Major utca 3.) elkötelezett üzleti partnerei személyes adatainak védelme iránt.",
        privacy_modal_p2: "A közvetlen kapcsolatfelvétel (telefon, e-mail) során átadott szakmai adatokat kizárólag árajánlatadás, mintaküldés és szerződéskötés céljából kezeljük a GDPR és a hazai jogszabályok előírásainak megfelelően.",
        privacy_modal_p3: "A megadott adatokat harmadik fél részére marketing célból nem értékesítjük és nem továbbítjuk.",
        nav_about: "Cégünkről",
        tech_hero_tag: "Kiemelt Technológiai Garancia",
        tech_hero_check1: "Alaktartó gélmátrix: Sütés után sem lapul el, dús marad a tésztabelsőben.",
        tech_hero_check2: "Zéró tésztaelázás: Nem enged szabad vizet a kelesztési és sütési ciklus alatt.",
        tech_hero_check3: "Tiszta tepsik & gépsorok: Nem folyik ki az illesztéseknél, minimális selejtképződés.",
        btn_download_prospectus: "Vállalati ismertető megnyitása (PDF)",
        cat_category_label: "Kategória",
        cat_flip_hint: "Lapozzon a bal és jobb oldali nyilakkal",
        cat_flip_hint_mob: "Lapozzon a nyilakkal, vagy húzza el a kártyát",
        cat_section_tag: "Termékportfólió & Minőségi Specifikációk",
        cat_section_title: "Lekvárok felhasználás szerint",
        contact_email_label: "Központi Elektronikus Levelezés",
        exotic_desc: "Az alapízeken túl trópusi és egzotikus gyümölcsökből is fejlesztünk egyedi receptúrát a kívánt ízprofilhoz és gyártási folyamathoz. Legyen szó mangóról, maracujáról vagy citrusfélékről, élelmiszer-technológusaink a megadott viszkozitási és Brix-értékekre kalibrálják a tölteléket.",
        exotic_note: "* Az egzotikus receptúrákat technológiai egyeztetés és receptúra-fejlesztés alapján véglegesítjük a partner saját gépsoraira.",
        exotic_tag: "Egyedi Fejlesztési Irányok • Innováció",
        exotic_title: "Egzotikus Ízek. Az Ön Termékére Hangolva.",
        flavor_apple: "Alma",
        flavor_apricot: "Sárgabarack",
        flavor_blueberry: "Áfonya",
        flavor_citrus: "Citrus",
        flavor_classic_mixed: "Klasszikus Vegyes Gyümölcs",
        flavor_kiwi: "Kivi",
        flavor_mango: "Mangó",
        flavor_maracuja: "Maracuja",
        flavor_orange: "Narancs",
        flavor_pineapple: "Ananász",
        flavor_plum: "Szilva",
        flavor_raspberry: "Málna",
        flavor_sour_cherry: "Meggy",
        flavors_desc: "A magyar pékipar és cukrászat legkedveltebb hagyományos gyümölcseit dolgozzuk fel kíméletes eljárással, modern technológiával. A termékeket a partner technológiájához igazítva állítjuk be mind sütésálló, mind hidegen kenhető formában.",
        flavors_tag: "Hagyományos Ízvilág • Korszerű Technológia",
        flavors_title: "Ismerős Ízek. Megbízható Ipari Minőség.",
        footer_rights: "© 2026 Sun Valley Kereskedelmi Zrt. • Minden jog fenntartva.",
        footer_tagline: "Ipari Gyümölcstechnológia Mór",
        footer_col_info: "Információk",
        footer_col_contact: "Elérhetőségek",
        footer_brand_desc: "B2B élelmiszeripari partner. Nagyüzemi sütésálló és kenhető gyümölcstöltelékek közvetlenül a gyártótól.",
        footer_privacy_link: "Adatkezelési tájékoztató",
        footer_link_catalog: "Termékkatalógus",
        footer_link_tech: "Technológia & Minőség",
        footer_link_rd: "Egyedi receptúra",
        footer_link_about: "Cégünkről",
        privacy_modal_tag: "GDPR & Adatvédelem",
        privacy_modal_title: "Adatkezelési Tájékoztató",
        privacy_modal_close: "Bezárás",
        hero_target_badge: "Nagyüzemi sütő- és cukrászipari alapanyagok",
        hero_h1: "Kiforrásbiztos, formamegtartó gyümölcstöltelékek",
        hero_sub_p: "Kiforrásbiztos, 180–220 °C-ig hőtűrő és hidegen kenhető gyümölcskészítmények közvetlen a gyártóüzemünkből. Stabil viszkozitás automata adagoló- és injektálósorokra, 5 kg-tól 200 kg-os kiszerelésig.",
        hero_pill_heat: "Hőtűrés",
        hero_pill_scale: "Kiszerelés",
        hero_pill_origin: "Gyártás",
        hero_cta_inquire: "Közvetlen gyári árajánlatkérés",
        hero_cta_browse: "Termékkategóriák megtekintése",
        hero_img_badge_title: "Ipari Minőség • Formamegtartó",
        hero_img_badge_sub: "200 °C felett sem forr ki",
        contact_sec_tag: "Közvetlen gyári egyeztetés",
        contact_sec_title: "Kérjen közvetlen gyári árajánlatot vagy technológiai egyeztetést",
        contact_sec_lead: "Nagyüzemi sütő- és kenyérgyári megrendelések, egyedi receptúrák és próbagyártások esetén vegye fel a kapcsolatot közvetlenül cégvezetésünkkel:",
        contact_person_name: "ifj. Vécsei András",
        contact_person_title: "Kereskedelem & Cégvezetés",
        contact_ready_badge: "Gyári egyeztetés nyitott",
        contact_phone_label: "Közvetlen mobil",
        contact_email_label: "Gyári e-mail",
        contact_compose_btn: "Előre formázott ajánlatkérés küldése e-mailben",
        contact_compose_hint: "Megnyitja levelezőjét a gyári specifikációs sablonnal kitöltve.",
        contact_checklist_tag: "Műszaki Ellenőrzőlista",
        contact_checklist_title: "Mit érdemes megadni az ajánlatkérésben?",
        contact_checklist_desc: "A gyors és pontos specifikációhoz kérjük, tüntesse fel az alábbi adatokat a megkeresésben:",
        contact_check_app_h: "Tervezett felhasználás",
        contact_check_app: "pl. leveles tészta, kelt bukta, linzer, tortalap",
        contact_check_dosing_h: "Adagolási technológia",
        contact_check_dosing: "kézi kenés vagy automata injektálósor",
        contact_check_heat_h: "Kívánt hőtűrés",
        contact_check_heat: "hideg technológia, 180 °C vagy 220 °C",
        contact_check_volume_h: "Volumen & kiszerelés",
        contact_check_volume: "becsült havi tétel; vödör (5–20 kg) vagy tömb / hordó",
        link_google_maps: "Megtekintés Google Térképen",
        nav_contact: "Kapcsolat",
        nav_products: "Termékek & Katalógus",
        nav_prospectus: "Prospektus",
        nav_rd: "Egyedi receptúra",
        nav_tech: "Technológia",
        prod_cat1_title: "Kenhető lekvárok",
        prod_cat1_subtitle: "Selymes, homogén állag linzerekhez, piskótákhoz és tortalapokhoz",
        prod_cat1_desc: "Egyenletesen és könnyedén kenhető, homogén gyümölcskészítmények. Tiszta gyümölcsíz, csomómentes textúra és stabil hidegterülés.",
        prod_cat2_title: "Sütésálló lekvárok",
        prod_cat2_subtitle: "Formamegtartó, sütés közben sem kiforró tésztabetétek",
        prod_cat2_desc: "Összetételüknek köszönhetően magas hőfokon sem forrnak ki, és nem áztatják el a tésztát. Kihűlés után is szépen megtartják a formájukat, a töltőgépeken pedig tisztán, csepegés nélkül adagolhatók.",
        prod_cat3_title: "Extra dzsemek",
        prod_cat3_subtitle: "Válogatott gyümölcsök, intenzív gyümölcsdarabos textúra és természetes ízek",
        prod_cat3_desc: "Magas gyümölcstartalmú, kíméletes főzéssel készült prémium dzsemek egész és vágott gyümölcsdarabokkal. Kifejezetten prémium cukrászati finompékárukhoz, látványpékségi süteményekhez és desszertbetétekhez.",
        prod_flavors_label: "Elérhető Ízek (Azonos Technológiai Paraméterekkel):",
        btn_inquire_jam: "Érdeklődés & Ajánlatkérés",
        cat_apps_label_pastry: "Ajánlott Cukrászati Felhasználás:",
        cat_apps_label_bakery: "Jellemző Pékipari Felhasználás:",
        cat_apps_label_extra: "Jellemző Prémium Felhasználás:",
        flavor_forest_berry: "Erdei gyümölcs",
        flavor_lingonberry: "Erdei vörösáfonya",
        flavor_apricot_pieces: "Sárgabarack darabos",
        flavor_blackberry: "Feketeszeder",
        flavor_raspberry_seeds: "Málna magvas",
        flavor_wild_strawberry: "Szamóca",
        flavor_orange_peel: "Narancs héjjal",
        app_linzer: "Linzerkarika",
        app_roll: "Piskótatekercs",
        app_layers: "Tortalapok kenése",
        app_inserts: "Desszertbetétek",
        app_donuts: "Fánk",
        app_croissant: "Croissantok & búrkiflik",
        app_buns: "Bukták & batyuk",
        app_puff: "Leveles tészták",
        app_pouches: "Párnácskák",
        app_frozen: "Fagyasztott félkészáru",
        app_hotel: "Szállodai reggeliztetés",
        app_plated: "Tányérdesszertek",
        app_artisan: "Látványpéksütemények",
        app_macaron: "Macaron betétek",
        app_tartlet: "Tartlet tortácskák",
        pack_spread_spec: "Kiszerelés: 5 / 10 / 20 kg",
        pack_bake_spec: "Kiszerelés: 10 / 20 kg tömb & vödör",
        pack_extra_spec: "Kiszerelés: 5 / 10 kg vödör",
        prospectus_desc: "Ismerje meg termékkínálatunkat, technológiai hátterünket és minőségi garanciáinkat összefoglaló bemutatónkban.",
        prospectus_title: "Sun Valley Vállalati Prospektus",
        rd_section_desc: "Nem minden gyártósor és késztermék egyforma. Az egyedi receptúra-fejlesztés kiindulópontja az Ön technológiája és a kívánt végeredmény.",
        rd_section_tag: "Egyedi receptúra",
        rd_section_title_p1: "Az Ön ötlete.",
        rd_section_title_p2: "Közös fejlesztés.",
        rd_step1_desc: "Felhasználás, ízvilág, állag, összetétel és technológiai feltételek egyeztetése.",
        rd_step1_title: "Az igény megismerése",
        rd_step2_desc: "A megfelelő megoldás kialakítása, majd a termék értékelése a tervezett felhasználásban.",
        rd_step2_title: "Receptúra és próba",
        rd_step3_desc: "A végleges specifikáció, kiszerelés és rendelési igények összehangolása.",
        rd_step3_title: "Gyártásra hangolva",
        rd_cta_hint: "Saját gépsorra kalibrált viszkozitás, egyedi Brix és gyümölcstartalom.",
        rd_cta_btn: "Egyedi receptúra egyeztetése",
        tagline: "Ipari Gyümölcstechnológia • Mór",
        tech_badge_dosing: "AUTOMATA ADAGOLÁS",
        tech_badge_freeze: "FAGYASZTÁSÁLLÓ",
        tech_card1_desc: "Kétféle hőtűrési kategóriában (180 °C-ig és 220 °C-ig). Magas hőfokon sem forr ki a süteményből, nem ég le a tepsire, és megőrzi térfogatát a tésztában szinerézis (vízkiválás) nélkül.",
        tech_card1_title: "Garantált Sütésállóság",
        tech_pillar1_badge: "180 °C és 220 °C",
        tech_card2_desc: "Fagyasztott félkész és fagyasztva tárolt késztermékekhez kifejlesztve. Felengedéskor nem enged levet, nem áztatja el a tésztát.",
        tech_card2_title: "Fagyasztásállóság",
        tech_pillar2_tag: "Fagyasztási ciklusstabilitás (Freeze-thaw)",
        tech_card3_desc: "A kézi kenéstől a nagyteljesítményű automata tüskés injektálósorokig nyírásstabil viszkozitást garantálunk: a töltelék nem csöpög, és nem tömíti el az adagolófejeket.",
        tech_card3_title: "Gépi Tölthetőség & Pumpálás",
        tech_card4_desc: "A kiszerelést a felhasználó volumenéhez igazítjuk: 5 kg-os vödrös egységek kézműves cukrászatoknak, 10–20 kg-os tömbök péküzemeknek, vagy 200 kg-os aszeptikus hordók ipari nagyüzemeknek.",
        tech_card4_title: "Kis Szériától Ipari Léptékig",
        tech_section_desc: "A finompékáru-gyártásban a selejtképződés legfőbb oka a töltelék kiforrása, a tészta elázása vagy a gépi adagolófejek eldugulása. A Sun Valley Zrt. hidrokolloid- és pektinmátrixa négy technológiai alappillérre épül:",
        tech_section_tag: "Élelmiszer-technológiai Garanciák",
        tech_section_title: "Nem Csak Az Íz Számít. Technológia & Megbízhatóság.",
        telemetry_heat_label: "Hőtűrési küszöb",
        telemetry_heat_val: "180 °C és 220 °C",
        telemetry_heat_sub: "Két hőtűrési kategória leveles és kelt tésztákhoz",
        telemetry_pack_label: "Ipari Kiszerelés",
        telemetry_pack_val: "5–20 kg és 200 kg",
        telemetry_pack_sub: "Vödör, tömb és aszeptikus hordó (480 kg raklapos egységek)",
      },

      en: {

        about_title: "Manufacturing Heritage & Track Record",
        about_card_title: "Over 30 Years of Professional Fruit Processing Experience",
        about_card_sub: "From family roots to a trusted supplier for commercial bakeries",
        about_p1: "The foundations of Sun Valley are built on more than three decades of family fruit-processing heritage, operating as an independent industrial manufacturer since 2009 to serve regional commercial bakeries.",
        about_p2: "We combine traditional fruit heritage with modern processing technologies and continuous product development at our plant in Mór, Hungary. We formulate our bake-stable and spreadable fruit fillings not from rigid templates, but tailored to your specific application, desired texture, thermal threshold, and depositor lines.",
        about_p3: "We believe in long-term partnerships and collaborative problem solving. Our mission is to support the commercial success of our partners' baked goods through flexible, reliable, and custom-engineered fruit solutions. Customer satisfaction is our operational benchmark.",
        cookie_notice: "Our website uses essential cookies necessary for core operation and saving language preferences.",
        cookie_accept: "Accept",
        privacy_modal_p1: "Sun Valley Kereskedelmi Zrt. (Headquarters: 1138 Budapest, Váci út 186., Manufacturing Plant: 8060 Mór, Major utca 3.) is dedicated to protecting the personal and commercial data of its business partners.",
        privacy_modal_p2: "Professional contact information shared via direct inquiries (phone, email) is strictly processed for quotation, sample delivery, and contract execution purposes in compliance with GDPR and relevant regulations.",
        privacy_modal_p3: "We do not sell or transfer provided information to third parties for marketing purposes.",
        nav_about: "About Us",
        tech_hero_tag: "Primary Food-Tech Assurance",
        tech_hero_check1: "Form-retaining gel matrix: Maintains elasticity and plump volume after baking.",
        tech_hero_check2: "Zero crust sogginess: Releases no syneresis water during proofing or baking cycles.",
        tech_hero_check3: "Clean trays & depositor lines: Prevents seam boil-out, eliminating burn marks and line scrap.",
        btn_download_prospectus: "Open Corporate Brochure (PDF)",
        cat_category_label: "Category",
        cat_flip_hint: "Turn pages using left and right arrows",
        cat_flip_hint_mob: "Swipe or use arrow buttons to browse",
        cat_section_tag: "Product Portfolio & Quality Specifications",
        cat_section_title: "Jams by Application",
        contact_email_label: "Corporate Email Address",
        exotic_desc: "Beyond traditional fruit bases, we engineer customized formulations from tropical and exotic fruits tailored to your desired flavor profile and processing line. Whether mango, passionfruit, or citrus varieties, our food technologists calibrate the filling to your required viscosity and Brix specifications.",
        exotic_note: "* Exotic formulations are finalized following technical consultation and custom recipe development for your production lines.",
        exotic_tag: "Custom R&D • Product Innovation",
        exotic_title: "Exotic Flavors. Engineered for Your Product.",
        flavor_apple: "Apple",
        flavor_apricot: "Apricot",
        flavor_blueberry: "Blueberry",
        flavor_citrus: "Citrus",
        flavor_classic_mixed: "Classic Mixed Fruit",
        flavor_kiwi: "Kiwi",
        flavor_mango: "Mango",
        flavor_maracuja: "Passion Fruit",
        flavor_orange: "Orange",
        flavor_pineapple: "Pineapple",
        flavor_plum: "Plum",
        flavor_raspberry: "Raspberry",
        flavor_sour_cherry: "Sour Cherry",
        flavors_desc: "We process Hungary's most celebrated domestic fruits with gentle, modern methods, customized to your exact baking or spreading technology.",
        flavors_tag: "Heritage Flavors • Modern Processing",
        flavors_title: "Familiar Flavors. Industrial Precision.",
        footer_rights: "© 2026 Sun Valley Kereskedelmi Zrt. • All rights reserved.",
        footer_tagline: "Industrial Fruit Technology Mór",
        footer_col_info: "Information",
        footer_col_contact: "Direct Contact",
        footer_brand_desc: "B2B food technology partner. Industrial bake-stable and spreadable fruit preparations direct from the plant.",
        footer_privacy_link: "Data Privacy Policy",
        footer_link_catalog: "Product Catalog",
        footer_link_tech: "Technology & Quality",
        footer_link_rd: "Custom Recipe R&D",
        footer_link_about: "About Us",
        privacy_modal_tag: "GDPR & Data Protection",
        privacy_modal_title: "Data Privacy Policy",
        privacy_modal_close: "Close",
        hero_target_badge: "Industrial Bakery & Confectionery Ingredients",
        hero_h1: "Bake-Stable, Shape-Retaining Fruit Fillings",
        hero_sub_p: "Bake-stable up to 180–220 °C and cold-spreadable fruit preparations direct from our manufacturing facility. Shear-stable viscosity for automated depositors and injection lines, 5 kg to 200 kg packaging.",
        hero_pill_heat: "Thermal Range",
        hero_pill_scale: "Packaging",
        hero_pill_origin: "Facility",
        hero_cta_inquire: "Request Direct Factory Quote",
        hero_cta_browse: "View Product Categories",
        hero_img_badge_title: "Industrial Grade • Shape Retention",
        hero_img_badge_sub: "Zero boil-out above 200 °C",
        contact_sec_tag: "Direct Plant Consultation",
        contact_sec_title: "Request a Direct Factory Quote or Technical Consultation",
        contact_sec_lead: "For commercial bakery volume orders, custom formulations, and pilot production trials, contact management directly:",
        contact_person_name: "András Vécsei Jr.",
        contact_person_title: "Commercial Operations & Leadership",
        contact_ready_badge: "Consultation Open",
        contact_phone_label: "Direct Mobile",
        contact_email_label: "Direct Plant Email",
        contact_compose_btn: "Send Pre-Formatted Inquiry via Email",
        contact_compose_hint: "Opens your email client with the factory technical specification template pre-filled.",
        contact_checklist_tag: "Technical Specification Checklist",
        contact_checklist_title: "What to Include in Your Inquiry",
        contact_checklist_desc: "To ensure swift and precise technical specification, please provide the following details:",
        contact_check_app_h: "Intended Application",
        contact_check_app: "e.g. puff pastry, yeast dough buns, linzer cookies, cake layers",
        contact_check_dosing_h: "Dosing Technology",
        contact_check_dosing: "manual spreading or automated injection lines",
        contact_check_heat_h: "Thermal Threshold",
        contact_check_heat: "cold process, 180 °C, or 220 °C",
        contact_check_volume_h: "Volume & Packaging",
        contact_check_volume: "estimated monthly volume; buckets (5–20 kg), blocks, or drums",
        link_google_maps: "View on Google Maps",
        nav_contact: "Contact",
        nav_products: "Products & Catalog",
        nav_prospectus: "Brochure",
        nav_rd: "Custom Recipe",
        nav_tech: "Technology",
        prod_cat1_title: "Spreadable Jams",
        prod_cat1_subtitle: "Smooth, homogeneous texture for linzers, sponge rolls, and cake layers",
        prod_cat1_desc: "Evenly and easily spreadable, homogeneous fruit preparations. Pure fruit taste, lump-free texture, and stable cold spread.",
        prod_cat2_title: "Bake-Stable Jams",
        prod_cat2_subtitle: "Shape-retaining, boil-proof fillings for commercial baking",
        prod_cat2_desc: "Thanks to their formulation, they will not boil out or soak the dough even at high baking temperatures. They retain their shape cleanly upon cooling and dose without dripping on automated depositors.",
        prod_cat3_title: "Extra Jams",
        prod_cat3_subtitle: "Carefully selected whole & diced fruit pieces with vibrant natural taste",
        prod_cat3_desc: "Crafted with high fruit concentration and gentle cooking, keeping fruit pieces intact. Formulated for artisan patisserie, Danish pastries, and high-end dessert layers.",
        prod_flavors_label: "Available Flavors (Identical Technical Parameters):",
        btn_inquire_jam: "Inquire & Request Quotation",
        cat_apps_label_pastry: "Recommended Confectionery Applications:",
        cat_apps_label_bakery: "Typical Bakery Applications:",
        cat_apps_label_extra: "Typical Premium Applications:",
        flavor_forest_berry: "Forest Berries",
        flavor_lingonberry: "Lingonberry",
        flavor_apricot_pieces: "Apricot with pieces",
        flavor_blackberry: "Blackberry",
        flavor_raspberry_seeds: "Raspberry with seeds",
        flavor_wild_strawberry: "Wild Strawberry",
        flavor_orange_peel: "Orange with peel",
        app_linzer: "Linzer Cookies",
        app_roll: "Sponge Roll",
        app_layers: "Cake Layering",
        app_inserts: "Dessert Inclusions",
        app_donuts: "Donuts",
        app_croissant: "Croissants & Danish pastries",
        app_buns: "Yeast Buns & Pockets",
        app_puff: "Puff Pastries",
        app_pouches: "Bakery Pillows",
        app_frozen: "Frozen Bake-off",
        app_hotel: "Hotel Breakfast Buffet",
        app_plated: "Plated Desserts",
        app_artisan: "Artisan Pastries",
        app_macaron: "Macaron Fillings",
        app_tartlet: "Tartlet Fillings",
        pack_spread_spec: "Packaging: 5 / 10 / 20 kg",
        pack_bake_spec: "Packaging: 10 / 20 kg block & bucket",
        pack_extra_spec: "Packaging: 5 / 10 kg bucket",
        prospectus_desc: "Explore our product portfolio, processing technology, and quality assurances in our presentation.",
        prospectus_title: "Sun Valley Corporate Brochure",
        rd_section_desc: "Every production line is unique. Custom recipe development starts with your technology and the desired end result.",
        rd_section_tag: "Custom Recipe",
        rd_section_title_p1: "Your concept.",
        rd_section_title_p2: "Joint development.",
        rd_step1_desc: "Aligning on application, flavor profile, texture, composition and technological requirements.",
        rd_step1_title: "Understanding the need",
        rd_step2_desc: "Formulating the right solution, then evaluating the product in its intended application.",
        rd_step2_title: "Recipe & trial",
        rd_step3_desc: "Finalizing specifications, packaging and aligning order requirements.",
        rd_step3_title: "Production-ready",
        rd_cta_hint: "Viscosity calibrated for your production equipment, custom Brix & fruit percentage.",
        rd_cta_btn: "Discuss Custom Recipe",
        tagline: "Industrial Food Technology • Mór",
        tech_badge_dosing: "AUTOMATED DOSING",
        tech_badge_freeze: "FREEZE-THAW STABLE",
        tech_card1_desc: "Available in two thermal threshold grades (up to 180 °C and up to 220 °C). Will not boil out even at high baking temperatures, does not scorch, and maintains volume in dough without syneresis.",
        tech_card1_title: "Guaranteed Bake-Stability",
        tech_pillar1_badge: "180 °C & 220 °C",
        tech_card2_desc: "Formulated for frozen unbaked and par-baked doughs. Zero water separation upon defrosting.",
        tech_card2_title: "Freeze-Thaw Stability",
        tech_pillar2_tag: "Freeze-Thaw Cycle Stability",
        tech_card3_desc: "Shear-thinning viscosity designed for automated needle depositors (doughnuts, croissants) without dripping.",
        tech_card3_title: "Automated Dosing & Injection",
        tech_card4_desc: "5 kg buckets for confectioneries, 10–20 kg carton blocks and buckets for bread factories, or 200 kg drums for large plants.",
        tech_card4_title: "From Trial to Factory Scale",
        tech_section_desc: "In commercial pastry production, scrap rates are driven by boil-outs, crust sogginess, or nozzle clogging. Sun Valley's hydrocolloid matrix is built on four core technical pillars:",
        tech_section_tag: "Food Engineering Assurances",
        tech_section_title: "More than Flavor. Process Engineering.",
        telemetry_heat_label: "Thermal Threshold",
        telemetry_heat_val: "180 °C & 220 °C",
        telemetry_heat_sub: "Two thermal threshold categories for puff and yeast doughs",
        telemetry_pack_label: "Packaging Scale",
        telemetry_pack_val: "5–20 kg & 200 kg",
        telemetry_pack_sub: "Buckets, blocks & aseptic drums (480 kg palletized units)",
      }
    };

    const catalogData = {
      "spreadable": {
        indexNum: "01",
        num: "01",
        badge: { hu: "CUKRÁSZATI VÖDRÖS & HORDÓS", en: "CONFECTIONERY BUCKET & DRUM" },
        badgeColor: "var(--sv-green-dark)",
        badgeBg: "var(--sv-green-dark)",
        imageBadge: { hu: "Hideg Technológia • Azonnal Kenhető", en: "Cold Process • Instantly Spreadable" },
        imageBadgeBg: "#2D3628",
        badgeOverlay: { hu: "Hideg Technológia • Azonnal Kenhető", en: "Cold Process • Instantly Spreadable" },
        badgeOverlayBg: "#2D3628",
        title: { hu: "Kenhető lekvárok", en: "Spreadable Jams" },
        subtitle: { hu: "Selymes, homogén állag linzerekhez, piskótákhoz és tortalapokhoz", en: "Smooth, homogeneous texture for linzers, sponge rolls, and cake layers" },
        desc: {
          hu: "Egyenletesen és könnyedén kenhető, homogén gyümölcskészítmények. Tiszta gyümölcsíz, csomómentes textúra és stabil hidegterülés.",
          en: "Evenly and easily spreadable, homogeneous fruit preparations. Pure fruit taste, lump-free texture, and stable cold spread."
        },
        specs: [
          { label: { hu: "Technológia", en: "Technology" }, val: { hu: "Hideg eljárás", en: "Cold process" }, isHighlight: true },
          { label: { hu: "Szavatosság", en: "Shelf Life" }, val: { hu: "9–12 hónap", en: "9–12 months" } }
        ],
        flavorsLabel: { hu: "Elérhető Ízek (Azonos Technológiai Paraméterekkel):", en: "Available Flavors (Identical Technical Parameters):" },
        flavors: {
          hu: ["Sárgabarack", "Málna", "Meggy", "Áfonya", "Erdei gyümölcs"],
          en: ["Apricot", "Raspberry", "Sour Cherry", "Blueberry", "Forest Berries"]
        },
        appsLabel: { hu: "Ajánlott Cukrászati Felhasználás:", en: "Recommended Confectionery Applications:" },
        apps: {
          hu: ["Linzerkarika", "Piskótatekercs", "Tortalapok kenése", "Desszertbetétek", "Fánk"],
          en: ["Linzer Cookies", "Sponge Roll", "Cake Layering", "Dessert Inclusions", "Donuts"]
        },
        imageWebp: "assets/catalog-jam1.webp",
        imgWebp: "assets/catalog-jam1.webp",
        imageJpg: "assets/catalog-jam1.jpg",
        imgJpg: "assets/catalog-jam1.jpg",
        caption: {
          hu: "Cukrászati felhasználás • Homogén selymes terülés piskótán, tortalapokon és linzereken",
          en: "Confectionery application • Smooth, silky spreading on sponge rolls, cakes, and linzers"
        },
        imgAlt: {
          hu: "Kenhető lekvárok bemutató",
          en: "Spreadable confectionery jams demonstration"
        }
      },
      "bake-stable": {
        indexNum: "02",
        num: "02",
        badge: { hu: "IPARI PÉKIPARI TÖMB & VÖDÖR", en: "INDUSTRIAL BAKE-STABLE BLOCK & BUCKET" },
        badgeColor: "var(--sv-burgundy)",
        badgeBg: "#a3392e",
        imageBadge: { hu: "Hőtűrő 180°C – 220°C • Forma- és Alaktartó", en: "Bake-Stable 180°C – 220°C • Shape Retaining" },
        imageBadgeBg: "#91372d",
        badgeOverlay: { hu: "Hőtűrő 180°C – 220°C • Forma- és Alaktartó", en: "Bake-Stable 180°C – 220°C • Shape Retaining" },
        badgeOverlayBg: "#91372d",
        title: { hu: "Sütésálló lekvárok", en: "Bake-Stable Jams" },
        subtitle: { hu: "Formamegtartó, sütés közben sem kiforró tésztabetétek", en: "Shape-retaining, boil-proof fillings for commercial baking" },
        desc: {
          hu: "Összetételüknek köszönhetően magas hőfokon sem forrnak ki, és nem áztatják el a tésztát. Kihűlés után is szépen megtartják a formájukat, a töltőgépeken pedig tisztán, csepegés nélkül adagolhatók.",
          en: "Thanks to their formulation, they will not boil out or soak the dough even at high baking temperatures. They retain their shape cleanly upon cooling and dose without dripping on automated depositors."
        },
        specs: [
          { label: { hu: "Tulajdonság", en: "Property" }, val: { hu: "Alaktartó, nem forr ki", en: "Shape-retaining / No boil-out" }, isHighlight: true },
          { label: { hu: "Szavatosság", en: "Shelf Life" }, val: { hu: "12 hónap", en: "12 months" } }
        ],
        flavorsLabel: { hu: "Elérhető Ízek (Azonos Technológiai Paraméterekkel):", en: "Available Flavors (Identical Technical Parameters):" },
        flavors: {
          hu: ["Kajszibarack", "Szilva", "Meggy", "Erdei gyümölcs", "Alma", "Eper"],
          en: ["Apricot", "Plum", "Sour Cherry", "Forest Berries", "Apple", "Strawberry"]
        },
        appsLabel: { hu: "Jellemző Pékipari Felhasználás:", en: "Typical Bakery Applications:" },
        apps: {
          hu: ["Croissantok & búrkiflik", "Bukták & lekváros batyuk", "Leveles tészták", "Párnácskák & tasakok", "Fagyasztott pékipari félkészáru"],
          en: ["Croissants & Danish pastries", "Yeast dough buns & pockets", "Puff pastry pillows", "Filled bakery snacks", "Frozen bake-off products"]
        },
        imageWebp: "assets/catalog-jam2.webp",
        imgWebp: "assets/catalog-jam2.webp",
        imageJpg: "assets/catalog-jam2.jpg",
        imgJpg: "assets/catalog-jam2.jpg",
        caption: {
          hu: "Sütésállósági teszt • Kelt tészta bukták 200 °C feletti sütés után, alaktartó töltelékkel",
          en: "Bake-stability test • Yeast dough buns baked above 200 °C with shape-retaining filling"
        },
        imgAlt: {
          hu: "Sütésálló gyümölcstöltelékek ipari finompékárukban",
          en: "Bake-stable fruit fillings in industrial bakery goods"
        }
      },
      "extra-jam": {
        indexNum: "03",
        num: "03",
        badge: { hu: "PRÉMIUM CUKRÁSZATI & PÉKIPARI", en: "PREMIUM CONFECTIONERY & BAKERY" },
        badgeColor: "var(--sv-orange)",
        badgeBg: "var(--sv-orange)",
        imageBadge: { hu: "Prémium Gyümölcsdarabos • Magas Gyümölcstartalom", en: "Premium Fruit Pieces • High Fruit Content" },
        imageBadgeBg: "#B84511",
        badgeOverlay: { hu: "Prémium Gyümölcsdarabos • Magas Gyümölcstartalom", en: "Premium Fruit Pieces • High Fruit Content" },
        badgeOverlayBg: "#B84511",
        title: { hu: "Extra dzsemek", en: "Extra Jams" },
        subtitle: { hu: "Válogatott gyümölcsök, intenzív gyümölcsdarabos textúra és természetes ízek", en: "Carefully selected whole & diced fruit pieces with vibrant natural taste" },
        desc: {
          hu: "Magas gyümölcstartalmú, kíméletes főzéssel készült prémium dzsemek egész és vágott gyümölcsdarabokkal. Kifejezetten prémium cukrászati finompékárukhoz, látványpékségi süteményekhez és desszertbetétekhez.",
          en: "Crafted with high fruit concentration and gentle cooking, keeping fruit pieces intact. Formulated for artisan patisserie, Danish pastries, and high-end dessert layers."
        },
        specs: [
          { label: { hu: "Gyümölcsjelleg", en: "Fruit Character" }, val: { hu: "Válogatott gyümölcsök", en: "Selected whole & sliced fruit" }, isHighlight: true },
          { label: { hu: "Szavatosság", en: "Shelf Life" }, val: { hu: "12 hónap", en: "12 months" } }
        ],
        flavorsLabel: { hu: "Elérhető Ízek (Azonos Technológiai Paraméterekkel):", en: "Available Flavors (Identical Technical Parameters):" },
        flavors: {
          hu: ["Erdei vörösáfonya", "Sárgabarack darabos", "Feketeszeder", "Málna magvas", "Szamóca", "Narancs héjjal"],
          en: ["Lingonberry", "Apricot with pieces", "Blackberry", "Raspberry with seeds", "Strawberry", "Orange with peel"]
        },
        appsLabel: { hu: "Jellemző Gasztro & Cukrászati Felhasználás:", en: "Typical Gastro & Pastry Applications:" },
        apps: {
          hu: ["Prémium szállodai reggeliztetés", "Tányérdesszertek & monodeszertek", "Nyitott látványpéksütemények", "Macaron & tartlet betétek"],
          en: ["Premium hotel breakfast buffets", "Plated & mono desserts", "Open-faced artisan pastries", "Macaron & tartlet fillings"]
        },
        imageWebp: "assets/catalog-jam-3.webp",
        imgWebp: "assets/catalog-jam-3.webp",
        imageJpg: "assets/catalog-jam-3.jpg",
        imgJpg: "assets/catalog-jam-3.jpg",
        caption: {
          hu: "Prémium finompékáru • Intenzív gyümölcsdarabos textúra croissant-ban és dán pékáruban",
          en: "Artisan pastry • Intensely fruity texture in croissants and Danish pastries"
        },
        imgAlt: {
          hu: "Extra dzsemek és prémium gyümölcskészítmények",
          en: "Extra jams and premium fruit preparations"
        }
      }
    };

    let currentLang = 'hu';

    // ---------------------------------------------------------------------------
    // COOKIE HELPERS
    // ---------------------------------------------------------------------------
    function getCookie(name) {
      try {
        const match = document.cookie.match(new RegExp('(?:^|;\\s*)' + name + '=([^;]+)'));
        return match ? decodeURIComponent(match[1]) : null;
      } catch (e) {
        return null;
      }
    }

    function setCookie(name, value, days = 365) {
      try {
        const maxAge = days * 24 * 60 * 60;
        document.cookie = `${name}=${encodeURIComponent(value)}; path=/; max-age=${maxAge}; SameSite=Lax`;
      } catch (e) {}
    }

    // ---------------------------------------------------------------------------
    // LANGUAGE SWITCHER ENGINE
    // ---------------------------------------------------------------------------
    function setLanguage(lang) {
      if (!translations[lang]) return;
      currentLang = lang;

      // Persist language selection in cookie (1 year) and localStorage
      setCookie('sv_lang', lang, 365);
      try {
        localStorage.setItem('sv_lang', lang);
      } catch (e) {}

      // Update switcher button styles while strictly preserving responsive classes & full height!
      ['hu', 'en'].forEach(l => {
        const btn = document.getElementById(`lang-${l}`);
        if (!btn) return;
        if (l === lang) {
          btn.className = "h-full px-2 sm:px-2.5 flex items-center justify-center rounded font-bold transition-all bg-[#a3392e] text-white shadow-sm text-[11px] sm:text-xs";
        } else {
          btn.className = "h-full px-2 sm:px-2.5 flex items-center justify-center rounded font-medium text-stone-600 hover:text-[#91372d] transition-all text-[11px] sm:text-xs";
        }
      });

      // Update static text elements with data-i18n
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (translations[lang][key]) {
          el.innerText = translations[lang][key];
        }
      });

      // Update placeholders with data-i18n-ph
      document.querySelectorAll('[data-i18n-ph]').forEach(el => {
        const key = el.getAttribute('data-i18n-ph');
        if (translations[lang][key]) {
          el.setAttribute('placeholder', translations[lang][key]);
        }
      });

      // Re-render dynamic components
      if (svFlip) svFlip.update();
      renderMobileCard(currentMobIdx);

      // Re-init lucide icons
      lucide.createIcons();

      // Clear any active field errors on language switch so errors don't persist in previous language
      clearFormErrors();
    }

    // ---------------------------------------------------------------------------
    // PRODUCT PORTFOLIO FLIPBOOK ENGINE (StPageFlip Canvas-Curl Physics for Desktop >= 1024px)
    // ---------------------------------------------------------------------------
    let svFlip = null;
    let svBusy = false;
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

    function updateSvFlipUI() {
      if (!svFlip) return;
      const curPage = svFlip.getCurrentPageIndex();
      const count = svFlip.getPageCount();
      const catIdx = Math.min(2, Math.floor(curPage / 2));
      currentMobIdx = catIdx;
      const curNum = document.getElementById('cat-current-num');
      if (curNum) curNum.textContent = '0' + (catIdx + 1);

      [0, 1, 2].forEach(i => {
        const dot = document.getElementById(`cat-dot-${i}`);
        if (!dot) return;
        if (i === catIdx) {
          dot.className = 'h-2.5 rounded-full transition-all duration-300 w-9 bg-[#a3392e]';
        } else {
          dot.className = 'h-2.5 rounded-full transition-all duration-300 w-3 bg-stone-300 hover:bg-stone-400';
        }
      });

      const prevBtn = document.getElementById('cat-side-prev');
      const nextBtn = document.getElementById('cat-side-next');
      if (prevBtn) prevBtn.disabled = svBusy || curPage === 0;
      if (nextBtn) nextBtn.disabled = svBusy || curPage >= count - 2;
    }

    function svFlipNext() {
      if (!svFlip || svBusy) return;
      if (reducedMotion.matches) svFlip.turnToNextPage();
      else svFlip.flipNext();
    }

    function svFlipPrev() {
      if (!svFlip || svBusy) return;
      if (reducedMotion.matches) svFlip.turnToPrevPage();
      else svFlip.flipPrev();
    }

    function svFlipGoToCategory(catIdx) {
      if (!svFlip || svBusy) return;
      const targetPage = catIdx * 2;
      if (reducedMotion.matches) svFlip.turnToPage(targetPage);
      else svFlip.flip(targetPage);
    }

    function initSvCatalog() {
      if (window.innerWidth < 1024) return;
      const book = document.getElementById('sv-book');
      if (!book) return;
      if (!window.St?.PageFlip) {
        setTimeout(initSvCatalog, 50);
        return;
      }
      if (svFlip) return;

      const pages = book.querySelectorAll('.sv-page');
      
      svFlip = new St.PageFlip(book, {
        width: 500,
        height: 600,
        size: 'stretch',
        minWidth: 420,
        maxWidth: 540,
        minHeight: 560,
        maxHeight: 620,
        showCover: false,
        usePortrait: false,
        drawShadow: !reducedMotion.matches,
        flippingTime: 700,
        maxShadowOpacity: 0.35,
        useMouseEvents: !reducedMotion.matches,
        disableFlipByClick: true
      });

      svFlip.on('init', updateSvFlipUI);
      svFlip.on('flip', updateSvFlipUI);
      svFlip.on('changeOrientation', updateSvFlipUI);
      svFlip.on('changeState', e => {
        svBusy = e.data !== 'read';
        updateSvFlipUI();
      });

      svFlip.loadFromHTML(pages);
      window.svFlip = svFlip;
    }

    // ---------------------------------------------------------------------------
    // MOBILE CATEGORY SHOWCASE CONTROLLER (< 1024px)
    // ---------------------------------------------------------------------------
    const mobileCatKeys = ["spreadable", "bake-stable", "extra-jam"];
    const mobileCatMeta = [
      {
        num: "1",
        imgWebp: "assets/catalog-jam1.webp",
        imgJpg: "assets/catalog-jam1.jpg",
        appsClass: "bg-emerald-50/80 border border-emerald-200/80 text-emerald-950",
        pack: { hu: "Kiszerelés: 5 / 10 / 20 kg", en: "Packaging: 5 / 10 / 20 kg" }
      },
      {
        num: "2",
        imgWebp: "assets/catalog-jam2.webp",
        imgJpg: "assets/catalog-jam2.jpg",
        appsClass: "bg-red-50/80 border border-red-200/80 text-red-950",
        pack: { hu: "Kiszerelés: 10 / 20 kg tömb & vödör", en: "Packaging: 10 / 20 kg block & bucket" }
      },
      {
        num: "3",
        imgWebp: "assets/catalog-jam-3.webp",
        imgJpg: "assets/catalog-jam-3.jpg",
        appsClass: "bg-amber-50/80 border border-amber-200/80 text-amber-950",
        pack: { hu: "Kiszerelés: 5 / 10 kg vödör", en: "Packaging: 5 / 10 kg bucket" }
      }
    ];

    let currentMobIdx = 0;
    let isMobTransitioning = false;

    function renderMobileCard(idx) {
      const key = mobileCatKeys[idx];
      const data = catalogData[key];
      const meta = mobileCatMeta[idx];
      if (!data || !meta) return;

      const lang = currentLang;

      const imgSource = document.getElementById('mob-img-source');
      const img = document.getElementById('mob-img');
      if (imgSource) imgSource.srcset = meta.imgWebp;
      if (img) {
        img.src = meta.imgJpg;
        img.alt = (data.imgAlt && data.imgAlt[lang]) || (data.imgAlt && data.imgAlt.hu) || '';
      }

      const pageInd = document.getElementById('mob-page-indicator');
      if (pageInd) pageInd.textContent = meta.num;

      const title = document.getElementById('mob-title');
      if (title) title.textContent = (data.title && data.title[lang]) || (data.title && data.title.hu) || '';

      const subtitle = document.getElementById('mob-subtitle');
      if (subtitle) subtitle.textContent = (data.subtitle && data.subtitle[lang]) || (data.subtitle && data.subtitle.hu) || '';

      const desc = document.getElementById('mob-desc');
      if (desc) desc.textContent = (data.desc && data.desc[lang]) || (data.desc && data.desc.hu) || '';

      const flavorsLabel = document.getElementById('mob-flavors-label');
      if (flavorsLabel) flavorsLabel.textContent = (data.flavorsLabel && data.flavorsLabel[lang]) || (data.flavorsLabel && data.flavorsLabel.hu) || '';

      const flavorsContainer = document.getElementById('mob-flavors');
      if (flavorsContainer) {
        const flavorsList = (data.flavors && data.flavors[lang]) || (data.flavors && data.flavors.hu) || [];
        flavorsContainer.innerHTML = flavorsList.map(f => 
          `<span class="px-2 py-0.5 rounded text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">${f}</span>`
        ).join('');
      }

      const appsLabel = document.getElementById('mob-apps-label');
      if (appsLabel) appsLabel.textContent = (data.appsLabel && data.appsLabel[lang]) || (data.appsLabel && data.appsLabel.hu) || '';

      const appsContainer = document.getElementById('mob-apps');
      if (appsContainer) {
        const appsList = (data.apps && data.apps[lang]) || (data.apps && data.apps.hu) || [];
        appsContainer.innerHTML = appsList.map(a => 
          `<span class="${meta.appsClass} px-2 py-0.5 rounded text-xs font-mono-spec">${a}</span>`
        ).join('');
      }

      const pack = document.getElementById('mob-pack');
      if (pack) pack.textContent = (meta.pack && meta.pack[lang]) || (meta.pack && meta.pack.hu) || '';

      // Update mobile controls
      const btnPrev = document.getElementById('mob-btn-prev');
      const btnNext = document.getElementById('mob-btn-next');
      if (btnPrev) btnPrev.disabled = idx === 0;
      if (btnNext) btnNext.disabled = idx === mobileCatKeys.length - 1;

      [0, 1, 2].forEach(i => {
        const dot = document.getElementById(`mob-dot-${i}`);
        if (!dot) return;
        if (i === idx) {
          dot.className = 'h-2 rounded-full transition-all duration-300 w-8 bg-[#a3392e]';
        } else {
          dot.className = 'h-2 rounded-full transition-all duration-300 w-2.5 bg-stone-300 hover:bg-stone-400';
        }
      });

      lucide.createIcons();
    }

    function mobGoTo(targetIdx, direction = null) {
      if (targetIdx === currentMobIdx || isMobTransitioning) return;
      if (targetIdx < 0 || targetIdx >= mobileCatKeys.length) return;

      const dir = direction !== null ? direction : (targetIdx > currentMobIdx ? 1 : -1);
      const shell = document.getElementById('mobile-card-shell');
      if (!shell || (reducedMotion && reducedMotion.matches)) {
        currentMobIdx = targetIdx;
        renderMobileCard(targetIdx);
        return;
      }

      isMobTransitioning = true;
      const outClass = dir > 0 ? 'mobile-card-flip-out-next' : 'mobile-card-flip-out-prev';
      const inClass = dir > 0 ? 'mobile-card-flip-in-next' : 'mobile-card-flip-in-prev';

      shell.classList.add(outClass);

      setTimeout(() => {
        currentMobIdx = targetIdx;
        renderMobileCard(targetIdx);

        shell.classList.remove(outClass);
        shell.classList.add(inClass);

        setTimeout(() => {
          shell.classList.remove(inClass);
          isMobTransitioning = false;
        }, 50);
      }, 200);
    }

    function mobNavNext() {
      mobGoTo(currentMobIdx + 1, 1);
    }

    function mobNavPrev() {
      mobGoTo(currentMobIdx - 1, -1);
    }

    function initMobileSwipe() {
      const container = document.getElementById('mobile-catalog-container');
      if (!container) return;
      let startX = 0, startY = 0;
      container.addEventListener('touchstart', e => {
        if (e.touches.length === 1) {
          startX = e.touches[0].clientX;
          startY = e.touches[0].clientY;
        }
      }, { passive: true });

      container.addEventListener('touchend', e => {
        if (e.changedTouches.length === 1) {
          const deltaX = e.changedTouches[0].clientX - startX;
          const deltaY = e.changedTouches[0].clientY - startY;
          if (Math.abs(deltaX) > 40 && Math.abs(deltaX) > Math.abs(deltaY) * 1.3) {
            if (deltaX < 0) mobNavNext();
            else mobNavPrev();
          }
        }
      }, { passive: true });
    }

    // Keyboard navigation
    window.addEventListener('keydown', e => {
      const catSection = document.getElementById('termekek');
      if (!catSection) return;
      const rect = catSection.getBoundingClientRect();
      const inView = rect.top < window.innerHeight && rect.bottom > 0;
      if (inView && !e.target.matches('input,textarea,select')) {
        if (e.key === 'ArrowRight') {
          if (window.innerWidth >= 1024) svFlipNext();
          else mobNavNext();
        } else if (e.key === 'ArrowLeft') {
          if (window.innerWidth >= 1024) svFlipPrev();
          else mobNavPrev();
        }
      }
    });

    window.addEventListener('resize', () => {
      if (window.innerWidth >= 1024) {
        if (!svFlip) initSvCatalog();
        else svFlip.update();
      }
    });

    // Close modal on escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closePrivacyModal();
      }
    });

    // ---------------------------------------------------------------------------
    // PRIVACY / GDPR MODAL HANDLERS
    // ---------------------------------------------------------------------------
    function openPrivacyModal() {
      const modal = document.getElementById('privacy-modal');
      if (modal) {
        modal.classList.remove('hidden');
        modal.classList.add('flex');
        lucide.createIcons();
      }
    }

    function closePrivacyModal() {
      const modal = document.getElementById('privacy-modal');
      if (modal) {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
      }
    }

    document.getElementById('privacy-modal')?.addEventListener('click', (e) => {
      if (e.target.id === 'privacy-modal') closePrivacyModal();
    });

    // Dynamic Smart Header Implementation
    function initDynamicHeader() {
      const siteHeader = document.getElementById('site-header');
      const headerSpacer = document.getElementById('header-spacer');
      const topBar = document.getElementById('top-bar');
      const mainNav = document.getElementById('main-nav');
      const mobileMenu = document.getElementById('mobile-menu');

      if (!siteHeader || !headerSpacer) return;

      function updateSpacer() {
        const baseHeight = (topBar ? topBar.offsetHeight : 0) + (mainNav ? mainNav.offsetHeight : 0);
        headerSpacer.style.height = (baseHeight > 0 ? baseHeight : siteHeader.offsetHeight) + 'px';
      }

      updateSpacer();
      window.addEventListener('resize', updateSpacer, { passive: true });
      window.addEventListener('orientationchange', () => setTimeout(updateSpacer, 150), { passive: true });

      // Nav link spy setup
      const navLinks = Array.from(document.querySelectorAll('#main-nav nav a[href^="#"]'));
      const sections = ['termekek', 'technologia', 'cegunkrol', 'egyedi-fejlesztes', 'kapcsolat']
        .map(id => document.getElementById(id))
        .filter(Boolean);

      function updateActiveNav() {
        const scrollPosition = (window.pageYOffset || document.documentElement.scrollTop) + 120;
        let currentSectionId = '';

        for (let i = sections.length - 1; i >= 0; i--) {
          const sec = sections[i];
          if (sec && sec.offsetTop <= scrollPosition) {
            currentSectionId = sec.id;
            break;
          }
        }

        navLinks.forEach(link => {
          const href = link.getAttribute('href');
          if (href === '#' + currentSectionId) {
            link.classList.add('nav-item-active');
          } else {
            link.classList.remove('nav-item-active');
          }
        });
      }

      let lastScrollY = window.pageYOffset || document.documentElement.scrollTop;
      let isTicking = false;

      function onScroll() {
        const currentScrollY = window.pageYOffset || document.documentElement.scrollTop;
        const isMobileOpen = mobileMenu && !mobileMenu.classList.contains('hidden');

        updateActiveNav();

        // If mobile drawer is open, keep header visible
        if (isMobileOpen) {
          siteHeader.style.transform = 'translateY(0)';
          lastScrollY = currentScrollY;
          isTicking = false;
          return;
        }

        // At the very top: always visible and clean
        if (currentScrollY <= 20) {
          siteHeader.style.transform = 'translateY(0)';
          siteHeader.classList.remove('shadow-lg');
          lastScrollY = currentScrollY;
          isTicking = false;
          return;
        }

        const heroEl = document.getElementById('hero');
        const heroHeight = heroEl ? heroEl.offsetHeight : 550;

        // Inside the Hero section: keep header visible
        if (currentScrollY <= heroHeight) {
          siteHeader.style.transform = 'translateY(0)';
          siteHeader.classList.remove('shadow-lg');
          lastScrollY = currentScrollY;
          isTicking = false;
          return;
        }

        const delta = currentScrollY - lastScrollY;

        // Ignore micro-scroll movements (less than 10px) to avoid jitter
        if (Math.abs(delta) < 10) {
          isTicking = false;
          return;
        }

        if (delta > 0 && currentScrollY > heroHeight) {
          // Scrolling down firmly beyond Hero: tuck header away
          siteHeader.style.transform = 'translateY(-100%)';
          siteHeader.classList.remove('shadow-lg');
        } else if (delta < 0) {
          // Scrolling up: reveal header with drop shadow
          siteHeader.style.transform = 'translateY(0)';
          siteHeader.classList.add('shadow-lg');
        }

        lastScrollY = currentScrollY;
        isTicking = false;
      }

      window.addEventListener('scroll', () => {
        if (!isTicking) {
          window.requestAnimationFrame(onScroll);
          isTicking = true;
        }
      }, { passive: true });

      // Run initial check
      updateActiveNav();
    }

    // Mobile Menu Toggle with smooth slide and fade
    function toggleMobileMenu() {
      const menu = document.getElementById('mobile-menu');
      const siteHeader = document.getElementById('site-header');
      if (!menu) return;
      
      const isClosed = menu.classList.contains('hidden');
      if (isClosed) {
        menu.classList.remove('hidden');
        menu.style.opacity = '0';
        menu.style.transform = 'translateY(-10px)';
        requestAnimationFrame(() => {
          menu.style.transition = 'opacity 0.22s ease-out, transform 0.22s ease-out';
          menu.style.opacity = '1';
          menu.style.transform = 'translateY(0)';
        });
        if (siteHeader) siteHeader.style.transform = 'translateY(0)';
      } else {
        menu.style.transition = 'opacity 0.18s ease-in, transform 0.18s ease-in';
        menu.style.opacity = '0';
        menu.style.transform = 'translateY(-10px)';
        setTimeout(() => {
          menu.classList.add('hidden');
        }, 180);
      }
    }

    function clearFormErrors() {
      // Streamlined contact model: form errors no-op
    }

    // ---------------------------------------------------------------------------
    // ONE-CLICK B2B INQUIRY EMAIL COMPOSER
    // ---------------------------------------------------------------------------
    function launchInquiryComposer() {
      const email = 'ifj.vecsei.andras@sunvalley.hu';
      const isEn = (currentLang === 'en');
      
      const subject = isEn 
        ? 'Sun Valley Zrt. - Industrial Inquiry & Quotation Request'
        : 'Sun Valley Zrt. - Ajánlatkérés és Technológiai Egyeztetés';

      const body = isEn
        ? `Tisztelt ifj. Vécsei András / Sun Valley Zrt. Vezetőség!%0D%0A%0D%0A` +
          `Érdeklődni szeretnénk az Önök által gyártott ipari gyümölcstöltelékek iránt.%0D%0A%0D%0A` +
          `--- MŰSZAKI ÉS GYÁRTÁSI SPECIFIKÁCIÓK ---%0D%0A` +
          `1. Tervezett felhasználási terület (pl. leveles tészta, kelt tészta, linzer, tortalap): %0D%0A` +
          `2. Adagolási mód (pl. kézi kenés / gépi adagolás / automata injektálósor): %0D%0A` +
          `3. Kívánt hőtűrési küszöb (pl. hideg eljárás / 180 °C / 220 °C feletti sütésálló): %0D%0A` +
          `4. Becsült havi volumen és preferált kiszerelés (5-20 kg vödör / kartontömb / aszeptikus hordó): %0D%0A%0D%0A` +
          `Cégünk / Üzemünk neve: %0D%0A` +
          `Kapcsolattartó neve és telefonszáma: %0D%0A%0D%0A` +
          `Várjuk visszajelzésüket és árajánlatukat!`
        : `Tisztelt ifj. Vécsei András / Sun Valley Zrt. Vezetőség!%0D%0A%0D%0A` +
          `Érdeklődni szeretnénk az Önök által gyártott ipari gyümölcstöltelékek iránt.%0D%0A%0D%0A` +
          `--- MŰSZAKI ÉS GYÁRTÁSI SPECIFIKÁCIÓK ---%0D%0A` +
          `1. Tervezett felhasználási terület (pl. leveles tészta, kelt tészta, linzer, tortalap): %0D%0A` +
          `2. Adagolási mód (pl. kézi kenés / gépi adagolás / automata injektálósor): %0D%0A` +
          `3. Kívánt hőtűrési küszöb (pl. hideg eljárás / 180 °C / 220 °C feletti sütésálló): %0D%0A` +
          `4. Becsült havi volumen és preferált kiszerelés (5-20 kg vödör / kartontömb / aszeptikus hordó): %0D%0A%0D%0A` +
          `Cégünk / Üzemünk neve: %0D%0A` +
          `Kapcsolattartó neve és telefonszáma: %0D%0A%0D%0A` +
          `Várjuk szíves visszajelzésüket és árajánlatukat!`;

      window.location.href = `mailto:${email}?subject=${encodeURIComponent(subject)}&body=${body}`;
    }

    // ---------------------------------------------------------------------------
    // COOKIE (GDPR) BANNER CONTROLLER
    // ---------------------------------------------------------------------------
    function initCookieBanner() {
      const banner = document.getElementById('cookie-banner');
      if (!banner) return;
      try {
        const consent = localStorage.getItem('sv_cookie_consent') || getCookie('sv_cookie_consent');
        if (!consent) {
          setTimeout(() => {
            banner.classList.remove('translate-y-24', 'opacity-0', 'pointer-events-none');
          }, 800);
        }
      } catch (e) {
        banner.classList.remove('translate-y-24', 'opacity-0', 'pointer-events-none');
      }
    }

    function acceptCookies() {
      const banner = document.getElementById('cookie-banner');
      try {
        localStorage.setItem('sv_cookie_consent', 'accepted');
        setCookie('sv_cookie_consent', 'accepted', 365);
      } catch (e) {}
      if (banner) {
        banner.classList.add('translate-y-24', 'opacity-0', 'pointer-events-none');
      }
    }

    // Initial boot
    document.addEventListener('DOMContentLoaded', () => {
      // Restore persisted language preference from cookie or localStorage
      const savedLang = getCookie('sv_lang') || (function() {
        try { return localStorage.getItem('sv_lang'); } catch (e) { return null; }
      })();
      if (savedLang && translations[savedLang] && savedLang !== 'hu') {
        setLanguage(savedLang);
      }

      initDynamicHeader();
      initCookieBanner();
      initSvCatalog();
      renderMobileCard(0);
      initMobileSwipe();
      lucide.createIcons();
    });
  </script>

  <!-- ========================================================================= -->
  <!-- FLOATING COOKIE (GDPR) CONSENT BANNER                                     -->
  <!-- ========================================================================= -->
  <div id="cookie-banner" 
       class="fixed bottom-5 left-4 right-4 sm:left-auto sm:right-6 sm:max-w-md z-50 transform transition-all duration-500 ease-out translate-y-24 opacity-0 pointer-events-none" 
       role="dialog" 
       aria-live="polite">
    <div class="p-4 sm:p-5 rounded-2xl border shadow-2xl flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4"
         style="background-color: #FFFFFF; border-color: var(--sv-border); box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);">
      <div class="flex items-start gap-3">
        <div class="w-8 h-8 rounded-full flex items-center justify-center shrink-0 mt-0.5" style="background-color: rgba(163, 57, 46, 0.1); color: var(--sv-burgundy);">
          <i data-lucide="cookie" class="w-4 h-4"></i>
        </div>
        <p class="text-xs sm:text-sm text-stone-700 leading-relaxed" data-i18n="cookie_notice">
          Weboldalunk az alapvető működéshez és a nyelvi beállítások mentéséhez szükséges sütiket használ.
        </p>
      </div>
      <button onclick="acceptCookies()" 
              class="w-full sm:w-auto px-4 py-2 rounded-xl text-xs font-semibold text-white transition-all transform active:scale-95 shrink-0"
              style="background-color: var(--sv-burgundy);"
              onmouseover="this.style.backgroundColor='var(--sv-burgundy-hover)'"
              onmouseout="this.style.backgroundColor='var(--sv-burgundy)'">
        <span data-i18n="cookie_accept">Rendben</span>
      </button>
    </div>
  </div>

</body>
</html>
"""

def main():
    content = generate_html()
    with open(ROOT_INDEX, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {ROOT_INDEX} ({len(content)} characters)")
    
    proto_dir = REPO_ROOT / "prototypes" / "sun-valley-b2b"
    if proto_dir.exists():
        (proto_dir / "index_v2.html").write_text(content, encoding="utf-8")
        (proto_dir / "index.html").write_text(content, encoding="utf-8")
        print(f"Synced: {proto_dir / 'index_v2.html'} and {proto_dir / 'index.html'}")

if __name__ == "__main__":
    main()
