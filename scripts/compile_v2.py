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
    /* 3D CATALOG FLIP BOOK STYLES (Pantastico / Heyzine inspired page turn)     */
    /* ------------------------------------------------------------------------- */
    .catalog-viewport {
      perspective: 2000px;
      perspective-origin: center center;
    }
    #catalog-card {
      transform-style: preserve-3d;
      backface-visibility: hidden;
      will-change: transform, opacity, filter, box-shadow;
    }
    
    .catalog-flip-next-out {
      animation: svPageFlipNextOut 0.20s cubic-bezier(0.4, 0, 0.2, 1) forwards;
    }
    .catalog-flip-next-in {
      animation: svPageFlipNextIn 0.25s cubic-bezier(0, 0, 0.2, 1) forwards;
    }
    .catalog-flip-prev-out {
      animation: svPageFlipPrevOut 0.20s cubic-bezier(0.4, 0, 0.2, 1) forwards;
    }
    .catalog-flip-prev-in {
      animation: svPageFlipPrevIn 0.25s cubic-bezier(0, 0, 0.2, 1) forwards;
    }

    @keyframes svPageFlipNextOut {
      0% {
        transform: rotateY(0deg) scale(1) translateX(0);
        opacity: 1;
        filter: brightness(1);
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08);
      }
      100% {
        transform: rotateY(-28deg) scale(0.96) translateX(-18px);
        opacity: 0.2;
        filter: brightness(0.85);
        box-shadow: -25px 20px 35px -8px rgba(0, 0, 0, 0.22);
      }
    }

    @keyframes svPageFlipNextIn {
      0% {
        transform: rotateY(28deg) scale(0.96) translateX(18px);
        opacity: 0.2;
        filter: brightness(1.1);
        box-shadow: 25px 20px 35px -8px rgba(0, 0, 0, 0.22);
      }
      100% {
        transform: rotateY(0deg) scale(1) translateX(0);
        opacity: 1;
        filter: brightness(1);
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08);
      }
    }

    @keyframes svPageFlipPrevOut {
      0% {
        transform: rotateY(0deg) scale(1) translateX(0);
        opacity: 1;
        filter: brightness(1);
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08);
      }
      100% {
        transform: rotateY(28deg) scale(0.96) translateX(18px);
        opacity: 0.2;
        filter: brightness(0.85);
        box-shadow: 25px 20px 35px -8px rgba(0, 0, 0, 0.22);
      }
    }

    @keyframes svPageFlipPrevIn {
      0% {
        transform: rotateY(-28deg) scale(0.96) translateX(-18px);
        opacity: 0.2;
        filter: brightness(1.1);
        box-shadow: -25px 20px 35px -8px rgba(0, 0, 0, 0.22);
      }
      100% {
        transform: rotateY(0deg) scale(1) translateX(0);
        opacity: 1;
        filter: brightness(1);
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08);
      }
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

    @keyframes pulse-ring {
      0% { box-shadow: 0 0 0 0 rgba(145, 55, 45, 0.6); }
      70% { box-shadow: 0 0 0 12px rgba(145, 55, 45, 0); }
      100% { box-shadow: 0 0 0 0 rgba(145, 55, 45, 0); }
    }
    .focus-pulse {
      animation: pulse-ring 1.5s cubic-bezier(0.24, 0, 0.38, 1) 2;
    }
  </style>
</head>
<body id="top" class="bg-tech-grid min-h-screen flex flex-col antialiased selection:bg-[#f1c7a6] selection:text-[#451C1B]">

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
          <img src="assets/sun-valley-logo.webp" alt="Sun Valley Logo" width="160" height="44" class="h-8 sm:h-11 w-auto object-contain transition-transform group-hover:scale-105">
          <div>
            <div class="font-syne font-extrabold text-sm sm:text-base md:text-lg tracking-tight leading-none" style="color: var(--sv-burgundy);">
              Sun Valley
            </div>
            <p class="text-[10px] font-mono-spec tracking-wider uppercase hidden md:block mt-0.5" style="color: var(--sv-text-muted);" data-i18n="tagline">
              Ipari Gyümölcstechnológia • Alapítva 2009
            </p>
          </div>
        </a>

        <!-- Desktop Nav Links (Streamlined 4 Essential Links) -->
        <nav class="hidden lg:flex items-center gap-5 xl:gap-8 text-xs xl:text-sm font-semibold">
          <a href="#termekek" class="hover:text-[#91372d] transition-colors py-1 relative group" data-i18n="nav_products">
            Termékek & Katalógus
            <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#91372d] transition-all group-hover:w-full"></span>
          </a>
          <a href="#technologia" class="hover:text-[#91372d] transition-colors py-1 relative group" data-i18n="nav_tech">
            Sütésállóság (200°C)
            <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#91372d] transition-all group-hover:w-full"></span>
          </a>
          <a href="#egyedi-fejlesztes" class="hover:text-[#91372d] transition-colors py-1 relative group" data-i18n="nav_rd">
            Receptúra & Fejlesztés
            <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#91372d] transition-all group-hover:w-full"></span>
          </a>
          <a href="#kapcsolat" class="hover:text-[#91372d] transition-colors py-1 relative group" data-i18n="nav_contact">
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
          <a href="#termekek" onclick="toggleMobileMenu()" class="py-1 text-stone-800 hover:text-[#91372d]" data-i18n="nav_products">Termékek & Kategóriák</a>
          <a href="#technologia" onclick="toggleMobileMenu()" class="py-1 text-stone-800 hover:text-[#91372d]" data-i18n="nav_tech">Sütésállóság (200°C)</a>
          <a href="#egyedi-fejlesztes" onclick="toggleMobileMenu()" class="py-1 text-stone-800 hover:text-[#91372d]" data-i18n="nav_rd">Receptúra & Fejlesztés</a>
          <a href="#prospektus" onclick="toggleMobileMenu()" class="py-1 text-stone-800 hover:text-[#91372d]" data-i18n="nav_prospectus">Prospektus</a>
          <a href="#disztribucio" onclick="toggleMobileMenu()" class="py-1 text-stone-800 hover:text-[#91372d]" data-i18n="nav_distribution">Nagykereskedelmi Hálózat</a>
          <a href="#kapcsolat" onclick="toggleMobileMenu()" class="py-1 text-stone-800 hover:text-[#91372d]" data-i18n="nav_contact">Kapcsolat & Gyártóüzem</a>
        </div>
        <div class="pt-3 border-t flex flex-col gap-2" style="border-color: var(--sv-border);">
          <a href="#kapcsolat" onclick="toggleMobileMenu()" class="flex items-center justify-center gap-2 py-2.5 rounded-lg text-white font-semibold text-sm" style="background-color: var(--sv-burgundy);">
            <i data-lucide="mail" class="w-4 h-4"></i>
            <span data-i18n="nav_contact">Kapcsolat & Gyártóüzem</span>
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
  <section class="relative overflow-hidden pt-10 pb-16 md:pt-16 md:pb-20 border-b" style="border-color: var(--sv-border);">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      
      <!-- Asymmetric Two-Column Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-8 xl:gap-12 items-center">
        
        <!-- Left Column: High-Conviction Value Proposition (Span 7) -->
        <div class="lg:col-span-7 space-y-6">
          
          <!-- Category Badge -->
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full border text-xs font-mono-spec uppercase tracking-wider"
               style="background-color: rgba(163, 57, 46, 0.06); border-color: var(--sv-border); color: var(--sv-burgundy);">
            <span class="w-1.5 h-1.5 rounded-full" style="background-color: var(--sv-orange);"></span>
            <span data-i18n="hero_badge">B2B Kenyérgyári & Finompékáru Alapanyagok</span>
          </div>

          <!-- Headline -->
          <h1 class="font-montserrat font-extrabold text-2xl xs:text-3xl sm:text-4xl lg:text-[2.5rem] xl:text-[2.85rem] tracking-tight pb-1 break-words"
              style="color: var(--sv-burgundy);">
            <span class="block mb-3.5 sm:mb-4 leading-snug sm:leading-tight" data-i18n="hero_h1_p1">200 °C felett sem forr ki.</span>
            <span class="block font-normal text-xl xs:text-2xl sm:text-3xl lg:text-[2.05rem] xl:text-[2.35rem] leading-snug" style="color: var(--sv-burgundy);">
              <span class="italic font-normal" style="color: var(--sv-orange);" data-i18n="hero_h1_p2">Ipari sütésálló</span> 
              <span data-i18n="hero_h1_p3">gyümölcstöltelékek közvetlenül a gyártótól.</span>
            </span>
          </h1>

          <!-- Body Description -->
          <p class="text-base sm:text-lg leading-relaxed max-w-2xl" style="color: var(--sv-text-muted);" data-i18n="hero_desc">
            A Sun Valley Zrt. a magyar finompékáru-üzemek és ipari kenyérgyárak megbízható belföldi beszállítója. 
            Forma- és alaktartó, gépileg szeletelhető tésztabetétek 10 kg-os kartonos és 5 kg-os vödrös kiszerelésben, közvetlen móri gyártóbázisról.
          </p>

          <!-- Action Buttons -->
          <div class="pt-2 flex flex-col sm:flex-row flex-wrap items-stretch sm:items-center gap-3 sm:gap-4">
            <a href="#termekek" 
               class="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-5 sm:px-6 py-3.5 rounded-lg font-semibold text-sm shadow-md hover:shadow-lg transition-all transform active:scale-95 text-center"
               style="background-color: var(--sv-burgundy); color: #F5F2EE;">
              <i data-lucide="book-open" class="w-4 h-4 text-[#FBBB9C]"></i>
              <span data-i18n="hero_cta_catalog">Lapozható Termékkatalógus</span>
            </a>

            <a href="#kapcsolat" 
               class="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-5 sm:px-6 py-3.5 rounded-lg font-semibold text-sm transition-all transform active:scale-95 shadow text-center"
               style="background-color: var(--sv-orange); color: white;">
              <i data-lucide="mail-check" class="w-4 h-4"></i>
              <span data-i18n="hero_cta_sample">Kapcsolatfelvétel & Ajánlatkérés</span>
            </a>

            <a href="assets/Sun_Valley_B2B_Prospektus_V1_4.pptx" download="Sun_Valley_B2B_Prospektus_V1_4.pptx"
               class="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-4 py-3.5 rounded-lg font-semibold text-xs font-mono-spec border transition-all hover:bg-white text-center"
               style="border-color: var(--sv-border); color: var(--sv-burgundy); background-color: var(--sv-surface);">
              <i data-lucide="download" class="w-3.5 h-3.5 text-[#91372d]"></i>
              <span data-i18n="hero_cta_prospectus">Prospektus (PPTX)</span>
            </a>
          </div>

          <!-- Key Technical Telemetry Badges -->
          <div class="pt-6 border-t grid grid-cols-1 sm:grid-cols-3 gap-3 sm:gap-4 text-left font-mono-spec text-xs" style="border-color: var(--sv-border);">
            <div>
              <div class="text-[10px] uppercase text-stone-500" data-i18n="telemetry_heat_label">Hőtűrési küszöb</div>
              <div class="font-bold text-sm sm:text-base text-stone-900 mt-0.5">≥ 200 °C</div>
              <div class="text-[11px] text-stone-500" data-i18n="telemetry_heat_sub">Nem forr ki, alaktartó</div>
            </div>
            <div class="sm:border-l sm:pl-4" style="border-color: var(--sv-border);">
              <div class="text-[10px] uppercase text-stone-500" data-i18n="telemetry_pack_label">Ipari Kiszerelés</div>
              <div class="font-bold text-sm sm:text-base text-stone-900 mt-0.5">10 kg / 5 kg / 200 kg</div>
              <div class="text-[11px] text-stone-500" data-i18n="telemetry_pack_sub">480 kg raklapos tétel</div>
            </div>
            <div class="sm:border-l sm:pl-4" style="border-color: var(--sv-border);">
              <div class="text-[10px] uppercase text-stone-500" data-i18n="telemetry_geo_label">Gyártótelep</div>
              <div class="font-bold text-sm sm:text-base text-stone-900 mt-0.5">Mór (Fejér vm.)</div>
              <div class="text-[11px] text-stone-500" data-i18n="telemetry_geo_sub">Major utca 3.</div>
            </div>
          </div>

        </div>

        <!-- Right Column: High-Impact Visual Card with apricot-hero.png (Span 5) -->
        <div class="lg:col-span-5">
          <div class="rounded-2xl border shadow-xl relative overflow-hidden transition-all duration-300 group"
               style="background-color: var(--sv-surface); border-color: var(--sv-border);">
            
            <!-- Hero Image Banner -->
            <div class="relative h-64 sm:h-72 w-full overflow-hidden bg-stone-100">
              <picture>
                <source srcset="assets/apricot.webp" type="image/webp">
                <img src="assets/apricot.jpg" alt="Sun Valley sütésálló kajszibarack gyümölcstöltelék" width="600" height="400" fetchpriority="high" decoding="async" class="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-500">
              </picture>
              <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent"></div>
              
              <!-- Floating QC Badge -->
              <div class="absolute top-4 left-4 inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-[11px] font-mono-spec font-bold tracking-wider uppercase text-white shadow-sm"
                   style="background-color: var(--sv-burgundy); border: 1px solid var(--sv-gold);">
                <i data-lucide="shield-check" class="w-3.5 h-3.5 text-[#91372d]"></i>
                <span data-i18n="hero_card_pill">SÜTÉSÁLLÓ • 200°C+</span>
              </div>

              <!-- Product overlay title -->
              <div class="absolute bottom-4 left-4 right-4 text-white">
                <span class="text-[10px] font-mono-spec uppercase tracking-widest text-[#FBBB9C]" data-i18n="card_hero_cat">PRÉMIUM PÉKIPARI TÉSZTABETÉT</span>
                <h3 class="font-syne font-bold text-lg sm:text-xl text-white leading-tight mt-0.5" data-i18n="card_hero_title">
                  SV Sütésálló Kajszibarack & Vegyes Íz
                </h3>
              </div>
            </div>

            <!-- Card Bottom Spec Matrix -->
            <div class="p-5 sm:p-6 space-y-4">
              <p class="text-xs text-stone-600 leading-relaxed" data-i18n="card_hero_desc">
                Formatartó, természetes aromájú töltelék magas hőmérsékletű sütéshez. Leveles tésztákban és kelt tésztákban sem enged szabad vizet.
              </p>

              <!-- Parameter Spec Table -->
              <div class="space-y-1.5 border-y py-2.5 font-mono-spec text-xs" style="border-color: var(--sv-border-light);">
                <div class="flex justify-between py-0.5">
                  <span class="text-stone-500" data-i18n="spec_brix">Szárazanyagtartalom (Brix)</span>
                  <span class="font-bold text-stone-900">58–64° Brix</span>
                </div>
                <div class="flex justify-between py-0.5 border-t" style="border-color: var(--sv-border-light);">
                  <span class="text-stone-500" data-i18n="spec_thermo">Hőállóság (200°C / 15 perc)</span>
                  <span class="font-bold text-emerald-700" data-i18n="spec_thermo_val">Alaktartó / Nem forr ki</span>
                </div>
                <div class="flex justify-between py-0.5 border-t" style="border-color: var(--sv-border-light);">
                  <span class="text-stone-500" data-i18n="spec_slice">Szeletelhetőség (Gépi késállás)</span>
                  <span class="font-bold text-stone-900" data-i18n="spec_slice_val">Kiváló / Tiszta vágás</span>
                </div>
              </div>

              <!-- Direct Call to Action Inside Card -->
              <div class="flex items-center gap-3 pt-1">
                <button onclick="openTdsModal(1)" 
                        class="w-full py-2.5 px-4 rounded-lg text-xs font-semibold font-mono-spec flex items-center justify-center gap-2 transition-all border hover:bg-stone-50"
                        style="border-color: var(--sv-burgundy); color: var(--sv-burgundy);">
                  <i data-lucide="file-spreadsheet" class="w-3.5 h-3.5 text-[#91372d]"></i>
                  <span data-i18n="btn_view_full_tds">Részletes TDS Műszaki Adatlap</span>
                </button>
              </div>

              <div class="pt-1 flex items-center justify-between text-[10px] font-mono-spec text-stone-400">
                <span data-i18n="hero_qc_badge">MÓRI GYÁRI MINŐSÉG-ELLENŐRZÉS #SV-2026</span>
                <span data-i18n="hero_direct_badge" class="text-[#91372d] font-semibold">KÖZVETLEN GYÁRI SZÁLLÍTÁS</span>
              </div>
            </div>

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
      
      <!-- Section Header with Title & Top Paginator Controls -->
      <div class="flex flex-col lg:flex-row lg:items-end justify-between gap-6">
        <div class="max-w-2xl">
          <div class="font-mono-spec text-xs uppercase tracking-widest text-[#91372d] font-semibold mb-2" data-i18n="cat_section_tag">
            Termékportfólió & Minőségi Specifikációk
          </div>
          <h2 class="font-montserrat font-bold text-3xl sm:text-4xl text-stone-900 leading-snug pb-1" data-i18n="cat_section_title">
            Lekvárok felhasználás szerint
          </h2>
          <p class="text-stone-600 mt-2 text-sm sm:text-base leading-relaxed" data-i18n="cat_section_desc">
            Válasszon technológiai kategóriát: lapozzon a kenhető lekvárok, a 180–220 °C sütésálló töltelékek és az extra dzsemek között a bal és jobb oldali nyilakkal.
          </p>
        </div>

        <!-- Catalog Paginator Toolbar: Category Tabs + Prev/Next Controls + Page Index -->
        <div class="flex flex-wrap items-center gap-3 self-start lg:self-end">
          
          <!-- Category Selector Tabs -->
          <div class="flex flex-wrap items-center gap-1.5 p-1 rounded-xl border bg-white font-mono-spec text-xs shadow-sm" style="border-color: var(--sv-border);">
            <button onclick="switchCatalogTab('spreadable')" id="tab-btn-spreadable" data-i18n="cat_tab_spreadable"
                    class="catalog-tab active px-3.5 py-2 rounded-lg font-bold transition-all text-xs whitespace-nowrap shadow-sm">
              1. Kenhető lekvárok
            </button>
            <button onclick="switchCatalogTab('bake-stable')" id="tab-btn-bake-stable" data-i18n="cat_tab_bake_stable"
                    class="catalog-tab px-3.5 py-2 rounded-lg font-semibold transition-all text-stone-700 hover:text-[#91372d] text-xs whitespace-nowrap">
              2. Sütésálló lekvárok
            </button>
            <button onclick="switchCatalogTab('extra-jam')" id="tab-btn-extra-jam" data-i18n="cat_tab_extra_jam"
                    class="catalog-tab px-3.5 py-2 rounded-lg font-semibold transition-all text-stone-700 hover:text-[#91372d] text-xs whitespace-nowrap">
              3. Extra dzsemek
            </button>
          </div>

          <!-- Page Arrows & Counter (Like Preview / Pantastico) -->
          <div class="flex items-center gap-2 p-1 rounded-xl border bg-white font-mono-spec text-xs shadow-sm" style="border-color: var(--sv-border);">
            <button onclick="navigateCatalog(-1)" id="cat-prev-btn" aria-label="Előző kategória"
                    class="w-8 h-8 rounded-lg flex items-center justify-center border border-stone-200 text-stone-600 hover:text-[#a3392e] hover:border-[#a3392e] hover:bg-stone-50 transition-all">
              <i data-lucide="chevron-left" class="w-4 h-4"></i>
            </button>
            <div id="cat-page-counter" class="px-2 font-bold text-xs tracking-wider text-stone-800">
              <span id="cat-current-num">01</span> <span class="text-stone-400 font-normal">/</span> <span>03</span>
            </div>
            <button onclick="navigateCatalog(1)" id="cat-next-btn" aria-label="Következő kategória"
                    class="w-8 h-8 rounded-lg flex items-center justify-center border border-stone-200 text-stone-600 hover:text-[#a3392e] hover:border-[#a3392e] hover:bg-stone-50 transition-all">
              <i data-lucide="chevron-right" class="w-4 h-4"></i>
            </button>
          </div>

        </div>
      </div>

      <!-- Flippable Catalog Card Container with 3D Perspective -->
      <div class="relative catalog-viewport max-w-6xl mx-auto px-2 sm:px-4 md:px-10 lg:px-12">
        
        <!-- Left Side Navigation Arrow (Flanking the Card) -->
        <button onclick="navigateCatalog(-1)" id="cat-side-prev" aria-label="Előző termékkategória" title="Előző termékkategória"
                class="flex absolute left-0 sm:left-1 md:left-1 lg:left-0 top-44 md:top-1/2 md:-translate-y-1/2 z-30 w-11 h-11 sm:w-12 sm:h-12 md:w-13 md:h-13 rounded-full bg-white/95 backdrop-blur-md border border-stone-200 hover:border-[#a3392e] shadow-lg hover:shadow-xl items-center justify-center text-stone-800 hover:text-white hover:bg-[#a3392e] hover:scale-105 active:scale-95 transition-all focus:outline-none focus:ring-2 focus:ring-[#a3392e]/40 cursor-pointer">
          <i data-lucide="chevron-left" class="w-6 h-6 stroke-[2.5]"></i>
        </button>

        <!-- Right Side Navigation Arrow (Flanking the Card) -->
        <button onclick="navigateCatalog(1)" id="cat-side-next" aria-label="Következő termékkategória" title="Következő termékkategória"
                class="flex absolute right-0 sm:right-1 md:right-1 lg:right-0 top-44 md:top-1/2 md:-translate-y-1/2 z-30 w-11 h-11 sm:w-12 sm:h-12 md:w-13 md:h-13 rounded-full bg-white/95 backdrop-blur-md border border-stone-200 hover:border-[#a3392e] shadow-lg hover:shadow-xl items-center justify-center text-stone-800 hover:text-white hover:bg-[#a3392e] hover:scale-105 active:scale-95 transition-all focus:outline-none focus:ring-2 focus:ring-[#a3392e]/40 cursor-pointer">
          <i data-lucide="chevron-right" class="w-6 h-6 stroke-[2.5]"></i>
        </button>

        <!-- Active Page Card (Turns with 3D Flip Animation) -->
        <div id="catalog-card" class="rounded-3xl border bg-white p-6 sm:p-10 shadow-lg relative overflow-hidden" 
             style="border-color: var(--sv-border);">
          
          <!-- Book Flip Crease / Shine Overlay -->
          <div id="catalog-flip-shine" class="pointer-events-none absolute inset-0 z-30 opacity-0 transition-opacity duration-200"></div>

          <!-- Card Content Grid: Left Image (Span 6) / Right Specs (Span 6) -->
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center">
            
            <!-- Left Column: Product Image (Span 6) -->
            <div class="lg:col-span-6 space-y-3">
              <div class="rounded-2xl overflow-hidden border shadow-md bg-stone-100 relative group" style="border-color: var(--sv-border-light);">
                <picture id="cat-picture">
                  <source id="cat-img-source" srcset="assets/jam.webp" type="image/webp">
                  <img id="cat-image" src="assets/jam.jpg" alt="Kenhető lekvárok bemutató" width="640" height="420" loading="lazy" decoding="async" class="w-full h-72 sm:h-96 object-cover object-center group-hover:scale-105 transition-transform duration-500">
                </picture>
                <div id="cat-badge-overlay" class="absolute top-3 left-3 bg-[#2D3628] text-white text-[11px] font-mono-spec font-bold px-3 py-1 rounded-md shadow-sm uppercase tracking-wider" data-i18n="badge_cold_process">
                  Hideg Technológia • Azonnal Kenhető
                </div>
              </div>
              <p id="cat-img-caption" class="text-[11px] font-mono-spec text-stone-500 italic text-center sm:text-left" data-i18n="cat_img_caption_spread">
                Cukrászati felhasználás • Homogén selymes terülés piskótán, tortalapokon és linzereken
              </p>
            </div>

            <!-- Right Column: Specs & Flavors (Span 6) -->
            <div class="lg:col-span-6 space-y-5">
              <div>
                <div id="cat-badge" class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-[11px] font-mono-spec font-bold uppercase tracking-wider text-white mb-2" style="background-color: var(--sv-green-dark);" data-i18n="prod_cat1_badge">
                  CUKRÁSZATI VÖDRÖS & HORDÓS
                </div>
                <h3 id="cat-title" class="font-montserrat font-bold text-2xl sm:text-3xl text-stone-900 leading-tight" data-i18n="prod_cat1_title">
                  Kenhető lekvárok
                </h3>
                <p id="cat-subtitle" class="text-sm text-[#91372d] font-semibold font-mono-spec mt-1" data-i18n="prod_cat1_subtitle">
                  Selymes, homogén állag linzerekhez, piskótákhoz és tortalapokhoz
                </p>
              </div>

              <p id="cat-desc" class="text-stone-600 text-sm leading-relaxed" data-i18n="prod_cat1_desc">
                Hideg technológiára kifejlesztett, egyenletesen és könnyen kenhető gyümölcskészítmények piskótatekercsek, tortalapok és linzer sütemények tiszta, szakadásmentes töltéséhez. Kiemelkedő természetes gyümölcsös aroma, tiszta ízvilág és intenzív fényesség jellemzi.
              </p>

              <!-- Specifications Matrix (No Brix, No pH) -->
              <div id="cat-specs" class="grid grid-cols-3 gap-3 p-4 rounded-xl border bg-stone-50 font-mono-spec text-xs" style="border-color: var(--sv-border-light);">
                <div>
                  <div class="text-[10px] text-stone-500 uppercase tracking-wider" data-i18n="spec_lbl_tech">Technológia</div>
                  <div class="font-bold text-emerald-700 text-sm mt-0.5" data-i18n="spec_val_cold">Hideg eljárás</div>
                </div>
                <div>
                  <div class="text-[10px] text-stone-500 uppercase tracking-wider" data-i18n="spec_lbl_pack">Kiszerelések</div>
                  <div class="font-bold text-stone-900 text-sm mt-0.5">5, 10, 20, 200 kg</div>
                </div>
                <div>
                  <div class="text-[10px] text-stone-500 uppercase tracking-wider" data-i18n="spec_lbl_shelf">Szavatosság</div>
                  <div class="font-bold text-stone-900 text-sm mt-0.5" data-i18n="spec_val_shelf9">9–12 hónap</div>
                </div>
              </div>

              <!-- Available Flavors with Identical Parameters -->
              <div>
                <div class="text-xs font-mono-spec uppercase tracking-wider text-stone-500 font-semibold mb-2" data-i18n="prod_flavors_label">
                  Elérhető Ízek (Azonos Technológiai Paraméterekkel):
                </div>
                <div id="cat-flavors" class="flex flex-wrap gap-2">
                  <span class="px-2.5 py-1 rounded-md text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200 font-medium">Sárgabarack</span>
                  <span class="px-2.5 py-1 rounded-md text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200 font-medium">Málna</span>
                  <span class="px-2.5 py-1 rounded-md text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200 font-medium">Eper</span>
                  <span class="px-2.5 py-1 rounded-md text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200 font-medium">Kerti meggy</span>
                  <span class="px-2.5 py-1 rounded-md text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200 font-medium">Erdei áfonya</span>
                  <span class="px-2.5 py-1 rounded-md text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200 font-medium">Feketeribizli</span>
                  <span class="px-2.5 py-1 rounded-md text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200 font-medium">Narancs</span>
                </div>
              </div>

              <!-- Applications -->
              <div>
                <div id="cat-apps-label" class="text-xs font-mono-spec uppercase tracking-wider text-stone-500 font-semibold mb-2" data-i18n="cat_apps_label_pastry">
                  Jellemző Cukrászati Felhasználás:
                </div>
                <div id="cat-apps" class="flex flex-wrap gap-2 text-xs text-stone-600 font-mono-spec">
                  <span class="bg-emerald-50/70 border border-emerald-200/80 px-2.5 py-1 rounded-md">Linzerkarika</span>
                  <span class="bg-emerald-50/70 border border-emerald-200/80 px-2.5 py-1 rounded-md">Piskótatekercs</span>
                  <span class="bg-emerald-50/70 border border-emerald-200/80 px-2.5 py-1 rounded-md">Tortalapok kenése</span>
                  <span class="bg-emerald-50/70 border border-emerald-200/80 px-2.5 py-1 rounded-md">Desszertbetétek</span>
                  <span class="bg-emerald-50/70 border border-emerald-200/80 px-2.5 py-1 rounded-md">Fánkáthúzás</span>
                </div>
              </div>

              <!-- Action CTA -->
              <div class="pt-2 flex flex-wrap items-center gap-3">
                <a href="#kapcsolat" class="inline-flex items-center gap-2 px-6 py-3 rounded-xl font-semibold text-xs font-mono-spec transition-all shadow-sm" style="background-color: var(--sv-orange); color: white;">
                  <i data-lucide="mail-check" class="w-4 h-4"></i>
                  <span data-i18n="btn_inquire_jam">Érdeklődés & Ajánlatkérés</span>
                </a>
                
                <span class="text-[11px] font-mono-spec text-stone-400 hidden sm:inline-flex items-center gap-1.5 ml-auto">
                  <i data-lucide="book-open" class="w-3.5 h-3.5 text-stone-400"></i>
                  <span data-i18n="cat_flip_hint">Lapozzon a nyilakkal vagy fülekkel</span>
                </span>
              </div>

            </div>

          </div>

        </div>

        <!-- Bottom Paginator Indicator Dots -->
        <div class="flex items-center justify-center gap-2 mt-6">
          <button onclick="switchCatalogTab('spreadable')" id="cat-dot-spreadable" aria-label="1. Kenhető lekvárok" class="h-2 rounded-full transition-all duration-300 w-8 bg-[#a3392e]"></button>
          <button onclick="switchCatalogTab('bake-stable')" id="cat-dot-bake-stable" aria-label="2. Sütésálló lekvárok" class="h-2 rounded-full transition-all duration-300 w-2.5 bg-stone-300 hover:bg-stone-400"></button>
          <button onclick="switchCatalogTab('extra-jam')" id="cat-dot-extra-jam" aria-label="3. Extra dzsemek" class="h-2 rounded-full transition-all duration-300 w-2.5 bg-stone-300 hover:bg-stone-400"></button>
        </div>

      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 7 FAMILIAR FLAVORS & EXOTIC FRUIT R&D PORTFOLIO                          -->
  <!-- ========================================================================= -->
  <section class="py-16 md:py-20 border-b" style="border-color: var(--sv-border); background-color: var(--sv-surface);">
    <div class="max-w-7xl mx-auto px-4 sm:px-8 space-y-16">
      
      <!-- Sub-section 1: 7 Familiar Domestic Flavors -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
        
        <!-- Left Visual (Span 5) -->
        <div class="lg:col-span-5 order-2 lg:order-1">
          <div class="rounded-2xl overflow-hidden border shadow-lg relative bg-stone-50 group" style="border-color: var(--sv-border);">
            <img src="assets/fruits.jpg" alt="Hét ismerős hazai gyümölcsíz Sun Valley" 
                 loading="lazy" decoding="async"
                 class="w-full h-80 sm:h-96 object-cover object-center group-hover:scale-105 transition-transform duration-500">
          </div>
        </div>

        <!-- Right Content (Span 7) -->
        <div class="lg:col-span-7 space-y-6 order-1 lg:order-2">
          <div class="font-mono-spec text-xs uppercase tracking-widest text-[#91372d] font-semibold" data-i18n="flavors_tag">
            Hagyományos Ízvilág • Korszerű Technológia
          </div>
          <h2 class="font-syne font-bold text-3xl sm:text-4xl text-stone-900 leading-tight" data-i18n="flavors_title">
            Ismerős Ízek. Megbízható Ipari Minőség.
          </h2>
          <p class="text-stone-600 text-sm sm:text-base leading-relaxed" data-i18n="flavors_desc">
            A magyar pékipar és cukrászat legkedveltebb hagyományos gyümölcseit dolgozzuk fel korszerű vákuumüstjeinkben. 
            A termékeket a partner technológiájához igazítva állítjuk be mind sütésálló, mind hidegen kenhető formában.
          </p>

          <!-- 7 Flavors Grid with Trilingual Keys -->
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-2 font-mono-spec text-xs">
            <div class="p-3 rounded-xl border bg-stone-50 flex items-center gap-2" style="border-color: var(--sv-border-light);">
              <span class="w-2.5 h-2.5 rounded-full bg-amber-500 shrink-0"></span>
              <span class="font-bold text-stone-800" data-i18n="flavor_apricot">Sárgabarack</span>
            </div>
            <div class="p-3 rounded-xl border bg-stone-50 flex items-center gap-2" style="border-color: var(--sv-border-light);">
              <span class="w-2.5 h-2.5 rounded-full bg-indigo-900 shrink-0"></span>
              <span class="font-bold text-stone-800" data-i18n="flavor_plum">Szilva</span>
            </div>
            <div class="p-3 rounded-xl border bg-stone-50 flex items-center gap-2" style="border-color: var(--sv-border-light);">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-600 shrink-0"></span>
              <span class="font-bold text-stone-800" data-i18n="flavor_apple">Alma</span>
            </div>
            <div class="p-3 rounded-xl border bg-stone-50 flex items-center gap-2" style="border-color: var(--sv-border-light);">
              <span class="w-2.5 h-2.5 rounded-full bg-rose-800 shrink-0"></span>
              <span class="font-bold text-stone-800" data-i18n="flavor_sour_cherry">Meggy</span>
            </div>
            <div class="p-3 rounded-xl border bg-stone-50 flex items-center gap-2" style="border-color: var(--sv-border-light);">
              <span class="w-2.5 h-2.5 rounded-full bg-pink-600 shrink-0"></span>
              <span class="font-bold text-stone-800" data-i18n="flavor_raspberry">Málna</span>
            </div>
            <div class="p-3 rounded-xl border bg-stone-50 flex items-center gap-2" style="border-color: var(--sv-border-light);">
              <span class="w-2.5 h-2.5 rounded-full bg-purple-900 shrink-0"></span>
              <span class="font-bold text-stone-800" data-i18n="flavor_blueberry">Áfonya</span>
            </div>
            <div class="p-3 rounded-xl border bg-stone-50 flex items-center gap-2 col-span-2 sm:col-span-2" style="border-color: var(--sv-border-light);">
              <span class="w-2.5 h-2.5 rounded-full bg-red-700 shrink-0"></span>
              <span class="font-bold text-stone-800" data-i18n="flavor_classic_mixed">Klasszikus Vegyes Gyümölcs</span>
            </div>
          </div>

          <div class="pt-2">
            <a href="#termekek" class="inline-flex items-center gap-2 text-xs font-mono-spec font-semibold hover:underline" style="color: var(--sv-burgundy);">
              <i data-lucide="arrow-right" class="w-4 h-4 text-[#91372d]"></i>
              <span data-i18n="flavors_cta">Részletes műszaki paraméterek megtekintése a termékmátrixban</span>
            </a>
          </div>
        </div>

      </div>

      <!-- Sub-section 2: Exotic Fruits & Innovation -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center border-t pt-16" style="border-color: var(--sv-border-light);">
        
        <!-- Left Content (Span 7) -->
        <div class="lg:col-span-7 space-y-6">
          <div class="font-mono-spec text-xs uppercase tracking-widest text-[#91372d] font-semibold" data-i18n="exotic_tag">
            Egyedi Fejlesztési Irányok • Innováció
          </div>
          <h2 class="font-syne font-bold text-3xl sm:text-4xl text-stone-900 leading-tight" data-i18n="exotic_title">
            Egzotikus Ízek. Az Ön Termékére Hangolva.
          </h2>
          <p class="text-stone-600 text-sm sm:text-base leading-relaxed" data-i18n="exotic_desc">
            Az alapízeken túl trópusi és egzotikus gyümölcsökből is fejlesztünk egyedi receptúrát a kívánt ízvilághoz, állaghoz és technológiához. 
            Legyen szó mangóról, maracujáról vagy citrusos készítményekről, móri laborunkban finomhangoljuk a hőtűrést és a viszkozitást.
          </p>

          <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 font-mono-spec text-xs">
            <div class="p-3 rounded-xl border bg-amber-50/50 border-amber-200 text-stone-800 font-semibold flex items-center gap-2">
              <i data-lucide="sparkles" class="w-3.5 h-3.5 text-[#91372d]"></i>
              <span data-i18n="exotic_mango">Mangó & Maracuja</span>
            </div>
            <div class="p-3 rounded-xl border bg-amber-50/50 border-amber-200 text-stone-800 font-semibold flex items-center gap-2">
              <i data-lucide="sparkles" class="w-3.5 h-3.5 text-[#91372d]"></i>
              <span data-i18n="exotic_pineapple">Ananász & Kivi</span>
            </div>
            <div class="p-3 rounded-xl border bg-amber-50/50 border-amber-200 text-stone-800 font-semibold flex items-center gap-2 col-span-2 sm:col-span-1">
              <i data-lucide="sparkles" class="w-3.5 h-3.5 text-[#91372d]"></i>
              <span data-i18n="exotic_citrus">Citrus & Narancs</span>
            </div>
          </div>

          <p class="text-xs text-stone-500 font-mono-spec" data-i18n="exotic_note">
            * Az egzotikus receptúrákat technológiai egyeztetés és receptúra-fejlesztés alapján véglegesítjük a partner saját gépsoraira.
          </p>
        </div>

        <!-- Right Visual (Span 5) -->
        <div class="lg:col-span-5">
          <div class="rounded-2xl overflow-hidden border shadow-lg relative bg-stone-50 group" style="border-color: var(--sv-border);">
            <img src="assets/retes.jpg" alt="Egzotikus gyümölcsök és innovatív töltelékek Sun Valley" 
                 loading="lazy" decoding="async"
                 class="w-full h-80 sm:h-96 object-cover object-center group-hover:scale-105 transition-transform duration-500">
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- FOOD-TECH ENGINEERING ADVANTAGES & APPLICATION PHOTOGRAPHY                -->
  <!-- ========================================================================= -->
  <section id="technologia" class="py-16 md:py-24 border-b" style="background-color: rgba(163, 57, 46, 0.02); border-color: var(--sv-border);">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      
      <!-- Section Title -->
      <div class="max-w-3xl mb-12">
        <div class="font-mono-spec text-xs uppercase tracking-widest text-[#91372d] font-semibold mb-2" data-i18n="tech_section_tag">
          Élelmiszer-technológiai Garanciák
        </div>
        <h2 class="font-syne font-bold text-3xl sm:text-4xl text-stone-900 leading-snug pb-1" data-i18n="tech_section_title">
          Nem Csak Az Íz Számít. Technológia & Megbízhatóság.
        </h2>
        <p class="text-stone-600 mt-3 text-sm sm:text-base leading-relaxed" data-i18n="tech_section_desc">
          A finompékáru-gyártásban a selejtképződés legfőbb oka a töltelék kiforrása, a tészta elázása vagy a gépi adagolófejek eldugulása. 
          A Sun Valley Zrt. hidrokolloid- és pektinmátrixa négy technológiai alappillérre épül:
        </p>
      </div>

      <!-- 4-Card Visual Engineering Grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        
        <!-- Tech Card 1: Baking Stability -->
        <div class="rounded-2xl border bg-white overflow-hidden shadow-sm hover:shadow-md transition-all flex flex-col justify-between"
             style="border-color: var(--sv-border);">
          <div>
            <div class="h-48 overflow-hidden bg-stone-100 relative">
              <img src="assets/lekvaros-bukta.webp" alt="Sütésállósági teszt péksütemény" width="400" height="250" loading="lazy" decoding="async" class="w-full h-full object-cover">
              <div class="absolute top-3 left-3 bg-[#a3392e] text-white text-[10px] font-mono-spec font-bold px-2 py-0.5 rounded">
                180 °C – 220 °C
              </div>
            </div>
            <div class="p-5 space-y-2">
              <h3 class="font-syne font-bold text-lg text-stone-900 leading-snug pb-0.5" data-i18n="tech_card1_title">Garantált Sütésállóság</h3>
              <p class="text-xs text-stone-600 leading-relaxed" data-i18n="tech_card1_desc">
                200 °C felett sem forr ki a süteményből, nem ég le a tepsire, és megőrzi térfogatát a tésztában szinerézis (vízkiválás) nélkül.
              </p>
            </div>
          </div>
        </div>

        <!-- Tech Card 2: Freezing Stability -->
        <div class="rounded-2xl border bg-white overflow-hidden shadow-sm hover:shadow-md transition-all flex flex-col justify-between"
             style="border-color: var(--sv-border);">
          <div>
            <div class="h-48 overflow-hidden bg-stone-100 relative">
              <img src="assets/retes.webp" alt="Fagyasztásálló gyümölcstöltelék" width="400" height="250" loading="lazy" decoding="async" class="w-full h-full object-cover">
              <div class="absolute top-3 left-3 bg-[#2D3628] text-white text-[10px] font-mono-spec font-bold px-2 py-0.5 rounded" data-i18n="tech_badge_freeze">
                FAGYASZTÁSÁLLÓ
              </div>
            </div>
            <div class="p-5 space-y-2">
              <h3 class="font-syne font-bold text-lg text-stone-900 leading-snug pb-0.5" data-i18n="tech_card2_title">Fagyasztásállóság</h3>
              <p class="text-xs text-stone-600 leading-relaxed" data-i18n="tech_card2_desc">
                Fagyasztott félkész és fagyasztva tárolt késztermékekhez kifejlesztve. Felengedéskor nem enged levet, nem áztatja el a tésztát.
              </p>
            </div>
          </div>
        </div>

        <!-- Tech Card 3: Pumpability & Dosing -->
        <div class="rounded-2xl border bg-white overflow-hidden shadow-sm hover:shadow-md transition-all flex flex-col justify-between"
             style="border-color: var(--sv-border);">
          <div>
            <div class="h-48 overflow-hidden bg-stone-100 relative">
              <img src="assets/jam.webp" alt="Gépi pumpálható töltelék adagolás" width="400" height="250" loading="lazy" decoding="async" class="w-full h-full object-cover">
              <div class="absolute top-3 left-3 bg-[#91372d] text-white text-[10px] font-mono-spec font-bold px-2 py-0.5 rounded" data-i18n="tech_badge_dosing">
                AUTOMATA ADAGOLÁS
              </div>
            </div>
            <div class="p-5 space-y-2">
              <h3 class="font-syne font-bold text-lg text-stone-900 leading-snug pb-0.5" data-i18n="tech_card3_title">Gépi Tölthetőség & Pumpálás</h3>
              <p class="text-xs text-stone-600 leading-relaxed" data-i18n="tech_card3_desc">
                A kézi kenéstől a nagyteljesítményű automata tüskés injektálósorokig (fánkok, croissant-ok) állandó, nyírásra stabil viszkozitás.
              </p>
            </div>
          </div>
        </div>

        <!-- Tech Card 4: Packaging Scale & Slicing -->
        <div class="rounded-2xl border bg-white overflow-hidden shadow-sm hover:shadow-md transition-all flex flex-col justify-between"
             style="border-color: var(--sv-border);">
          <div>
            <div class="h-48 overflow-hidden bg-stone-100 relative">
              <img src="assets/jam-cookie.webp" alt="Ipari kiszerelések vödörtől kartontömbökig" width="400" height="250" loading="lazy" decoding="async" class="w-full h-full object-cover">
              <div class="absolute top-3 left-3 bg-stone-800 text-white text-[10px] font-mono-spec font-bold px-2 py-0.5 rounded">
                5 KG • 10 KG • 200 KG
              </div>
            </div>
            <div class="p-5 space-y-2">
              <h3 class="font-syne font-bold text-lg text-stone-900 leading-snug pb-0.5" data-i18n="tech_card4_title">Kis Szériától Ipari Léptékig</h3>
              <p class="text-xs text-stone-600 leading-relaxed" data-i18n="tech_card4_desc">
                5 kg-os vödörben a cukrászatoknak, 10 kg-os szeletelhető kartontömbökben kenyérgyáraknak, vagy 200 kg-os hordókban nagyüzemeknek.
              </p>
            </div>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 3-STEP CUSTOM RECIPE R&D PIPELINE                                         -->
  <!-- ========================================================================= -->
  <section id="egyedi-fejlesztes" class="py-16 md:py-20 border-b" style="border-color: var(--sv-border); background-color: var(--sv-paper-cream);">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      
      <div class="max-w-3xl mb-12">
        <div class="font-mono-spec text-xs uppercase tracking-widest text-[#91372d] font-semibold mb-2" data-i18n="rd_section_tag">
          Egyedi Termékfejlesztési Folyamat
        </div>
        <h2 class="font-syne font-bold text-3xl sm:text-4xl text-stone-900 leading-snug pb-1" data-i18n="rd_section_title">
          Az Ön Ötlete. Közös Ipari Fejlesztés.
        </h2>
        <p class="text-stone-600 mt-2 text-sm sm:text-base leading-relaxed" data-i18n="rd_section_desc">
          Nem minden gyártósor és késztermék egyforma. Az egyedi receptúra-fejlesztés során a technológusokkal közösen alakítjuk ki az ideális tölteléket 3 lépésben:
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        <!-- Step 1 -->
        <div class="rounded-2xl border bg-white p-6 sm:p-8 space-y-4 shadow-sm" style="border-color: var(--sv-border);">
          <div class="w-12 h-12 rounded-xl flex items-center justify-center font-mono-spec font-bold text-lg text-white"
               style="background-color: var(--sv-burgundy);">
            01
          </div>
          <h3 class="font-syne font-bold text-xl text-stone-900 leading-snug pb-0.5" data-i18n="rd_step1_title">
            Az Igény Megismerése
          </h3>
          <p class="text-xs sm:text-sm text-stone-600 leading-relaxed" data-i18n="rd_step1_desc">
            Felhasználás, ízvilág, elvárt gyümölcstartalom, állag, sütési hőmérséklet (180–220 °C) és a gépsor adagolási feltételeinek pontos felmérése.
          </p>
          <div class="pt-2 font-mono-spec text-[11px] text-stone-400 border-t" style="border-color: var(--sv-border-light);" data-i18n="rd_tag_1">
            Audit & Paraméterezés
          </div>
        </div>

        <!-- Step 2 -->
        <div class="rounded-2xl border bg-white p-6 sm:p-8 space-y-4 shadow-sm" style="border-color: var(--sv-border);">
          <div class="w-12 h-12 rounded-xl flex items-center justify-center font-mono-spec font-bold text-lg text-white"
               style="background-color: var(--sv-green-dark);">
            02
          </div>
          <h3 class="font-syne font-bold text-xl text-stone-900 leading-snug pb-0.5" data-i18n="rd_step2_title">
            Receptúra & Technológiai Hangolás
          </h3>
          <p class="text-xs sm:text-sm text-stone-600 leading-relaxed" data-i18n="rd_step2_desc">
            Laboratóriumi fejlesztés és kísérleti próbasütés, a receptúra pontos beállítása a partner saját gépsorain történő technológiai elvárásokhoz.
          </p>
          <div class="pt-2 font-mono-spec text-[11px] text-stone-400 border-t" style="border-color: var(--sv-border-light);" data-i18n="rd_tag_2">
            Fejlesztés & Validáció
          </div>
        </div>

        <!-- Step 3 -->
        <div class="rounded-2xl border bg-white p-6 sm:p-8 space-y-4 shadow-sm" style="border-color: var(--sv-border);">
          <div class="w-12 h-12 rounded-xl flex items-center justify-center font-mono-spec font-bold text-lg text-white"
               style="background-color: var(--sv-burgundy);">
            03
          </div>
          <h3 class="font-syne font-bold text-xl text-stone-900 leading-snug pb-0.5" data-i18n="rd_step3_title">
            Gyártásra Hangolva
          </h3>
          <p class="text-xs sm:text-sm text-stone-600 leading-relaxed" data-i18n="rd_step3_desc">
            A végleges műszaki specifikáció (TDS) rögzítése, a csomagolás (vödör, kartontömb, hordó) kiválasztása és a stabil ütemezett raklapos szállítás elindítása.
          </p>
          <div class="pt-2 font-mono-spec text-[11px] text-stone-400 border-t" style="border-color: var(--sv-border-light);" data-i18n="rd_tag_3">
            TDS Rögzítés & Szállítás
          </div>
        </div>

      </div>

    </div>
  </section>



  <!-- ========================================================================= -->
  <!-- OFFICIAL B2B PROSPECTUS DOWNLOAD SHOWCASE                                 -->
  <!-- ========================================================================= -->
  <section id="prospektus" class="py-14 border-b transition-colors" style="background-color: var(--sv-burgundy); color: #F5F2EE; border-color: var(--sv-border);">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      <div class="rounded-2xl p-6 sm:p-10 border flex flex-col lg:flex-row items-center justify-between gap-8"
           style="background-color: var(--sv-burgundy-dark); border-color: rgba(255,255,255,0.15);">
        
        <div class="space-y-4 max-w-2xl text-center lg:text-left">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-mono-spec uppercase tracking-wider bg-white/10 text-[#FBBB9C]">
            <i data-lucide="file-text" class="w-3.5 h-3.5 text-[#FBBB9C]"></i>
            <span data-i18n="prospectus_badge">HIVATALOS B2B DOKUMENTÁCIÓ • V1.4</span>
          </div>

          <h3 class="font-syne font-bold text-2xl sm:text-3xl text-white leading-tight" data-i18n="prospectus_title">
            Töltse le a Sun Valley Zrt. Hivatalos Vállalati Prospektusát
          </h3>

          <p class="text-sm text-white/80 leading-relaxed font-mono-spec" data-i18n="prospectus_desc">
            A prezentáció részletesen bemutatja móri üzemünk technológiai gépsorait, a teljes sütésálló és hidegtechnológiás termékpalettát, a logisztikai paritásokat és a minőségbiztosítási garanciákat.
          </p>

          <div class="flex flex-wrap items-center justify-center lg:justify-start gap-4 text-xs font-mono-spec text-white/60">
            <span data-i18n="prospectus_format">Formátum: Microsoft PowerPoint (.pptx)</span>
            <span>•</span>
            <span data-i18n="prospectus_size">Méret: ~11,1 MB</span>
            <span>•</span>
            <span data-i18n="prospectus_version">Verzió: V1.4 (2026)</span>
          </div>
        </div>

        <div class="shrink-0">
          <a href="assets/Sun_Valley_B2B_Prospektus_V1_4.pptx" download="Sun_Valley_B2B_Prospektus_V1_4.pptx"
             class="inline-flex items-center gap-3 px-8 py-4 rounded-xl font-bold text-sm shadow-xl hover:scale-105 transition-all transform active:scale-95"
             style="background-color: var(--sv-orange); color: white;">
            <i data-lucide="download" class="w-5 h-5"></i>
            <span data-i18n="btn_download_prospectus">Prospektus Letöltése (.PPTX)</span>
          </a>
        </div>

      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- DUAL-TRACK DISTRIBUTION NETWORK                                           -->
  <!-- ========================================================================= -->
  <section id="disztribucio" class="py-16 md:py-24 border-b" style="border-color: var(--sv-border); background-color: var(--sv-paper-cream);">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      
      <div class="max-w-3xl mb-12">
        <div class="font-mono-spec text-xs uppercase tracking-widest text-[#91372d] font-semibold mb-2" data-i18n="dist_section_tag">
          Értékesítési Csatornák & Logisztika
        </div>
        <h2 class="font-syne font-bold text-3xl sm:text-4xl text-stone-900 leading-snug pb-1" data-i18n="dist_section_title">
          Hogyan Jut El a Termék az Ön Üzemébe?
        </h2>
        <p class="text-stone-600 mt-3 text-sm sm:text-base leading-relaxed" data-i18n="dist_section_desc">
          Rugalmas logisztikai modellünk két csatornán biztosítja az ellátásbiztonságot: közvetlen gyári szerződéssel ipari mennyiségekre, 
          vagy országos nagykereskedelmi partnereinken keresztül azonnali raktári kiszolgálásra.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
        
        <!-- Track 1: Direct Factory Supply -->
        <div class="rounded-2xl p-6 sm:p-8 border bg-white flex flex-col justify-between shadow-sm" style="border-color: var(--sv-border);">
          <div class="space-y-4">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-mono-spec font-semibold text-[#a3392e] bg-[#a3392e]/10">
              <i data-lucide="truck" class="w-3.5 h-3.5 text-[#91372d]"></i>
              <span data-i18n="dist_t1_badge">1. CSATORNA • IPARI SZERZŐDÉSEK</span>
            </div>

            <h3 class="font-syne font-bold text-2xl text-stone-900" data-i18n="dist_t1_title">
              Közvetlen Gyári Szállítás (Raklapos & Kamionos Tételek)
            </h3>

            <p class="text-sm text-stone-600 leading-relaxed" data-i18n="dist_t1_desc">
              Nagyipari kenyérgyárak és finompékáru-üzemek részére (>500 kg / megrendelés). 
              Közvetlen gyári egyedi árképzés, ütemezett lehívások, tételes sarzshomogenitás és folyamatos technológiai támogatás.
            </p>

            <ul class="space-y-2 text-xs font-mono-spec text-stone-700 pt-2">
              <li class="flex items-center gap-2">
                <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-600"></i>
                <span data-i18n="dist_t1_p1">480 kg raklapos standard egységek</span>
              </li>
              <li class="flex items-center gap-2">
                <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-600"></i>
                <span data-i18n="dist_t1_p2">Garantált tételes sarzs-homogenitás</span>
              </li>
              <li class="flex items-center gap-2">
                <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-600"></i>
                <span data-i18n="dist_t1_p3">Közvetlen telephelyi kapcsolattartó</span>
              </li>
            </ul>
          </div>

          <div class="pt-6 mt-6 border-t" style="border-color: var(--sv-border-light);">
            <a href="#kapcsolat" class="inline-flex items-center gap-2 font-semibold text-sm hover:underline" style="color: var(--sv-burgundy);">
              <i data-lucide="arrow-right-circle" class="w-4 h-4 text-[#91372d]"></i>
              <span data-i18n="dist_t1_cta">Ipari Keretszerződés Egyeztetése</span>
            </a>
          </div>
        </div>

        <!-- Track 2: Authorized Wholesale Network -->
        <div class="rounded-2xl p-6 sm:p-8 border bg-white flex flex-col justify-between shadow-sm" style="border-color: var(--sv-border);">
          <div class="space-y-4">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-mono-spec font-semibold text-[#2D3628] bg-[#2D3628]/10">
              <i data-lucide="store" class="w-3.5 h-3.5 text-[#5F6E4D]"></i>
              <span data-i18n="dist_t2_badge">2. CSATORNA • RAKTÁRI KISZOLGÁLÁS</span>
            </div>

            <h3 class="font-syne font-bold text-2xl text-stone-900" data-i18n="dist_t2_title">
              Országos Nagykereskedelmi Partnerhálózat
            </h3>

            <p class="text-sm text-stone-600 leading-relaxed" data-i18n="dist_t2_desc">
              Közepes cukrászatok és kézműves pékségek az országos lefedettségű partner-nagykereskedőink raktáraiból azonnal megvásárolhatják az 5–10 kg-os kiszereléseket.
            </p>

            <!-- Verified Partners Badge List -->
            <div class="pt-2 grid grid-cols-2 sm:grid-cols-3 gap-2 text-xs font-mono-spec">
              <div class="p-2.5 rounded border text-center font-bold bg-stone-50 text-stone-800" style="border-color: var(--sv-border-light);">
                Békás Kft.
              </div>
              <div class="p-2.5 rounded border text-center font-bold bg-stone-50 text-stone-800" style="border-color: var(--sv-border-light);">
                Busa Kft.
              </div>
              <div class="p-2.5 rounded border text-center font-bold bg-stone-50 text-stone-800" style="border-color: var(--sv-border-light);">
                Csubi-Ker Kft.
              </div>
              <div class="p-2.5 rounded border text-center font-bold bg-stone-50 text-stone-800" style="border-color: var(--sv-border-light);">
                Pille Hungária Kft.
              </div>
              <div class="p-2.5 rounded border text-center font-bold bg-stone-50 text-stone-800" style="border-color: var(--sv-border-light);">
                GALLA Zrt.
              </div>
              <div class="p-2.5 rounded border text-center font-bold bg-stone-50 text-stone-800" style="border-color: var(--sv-border-light);">
                Cukrászcentrum
              </div>
            </div>
          </div>

          <div class="pt-6 mt-6 border-t" style="border-color: var(--sv-border-light);">
            <p class="text-xs text-stone-500 font-mono-spec" data-i18n="dist_t2_footer">
              Érdeklődjön helyi pékszövetségi vagy nagykereskedelmi területi képviselőjénél.
            </p>
          </div>
        </div>

      </div>

    </div>
  </section>



  <!-- ========================================================================= -->
  <!-- CONTACT & MANUFACTURING PLANT SECTION                                    -->
  <!-- ========================================================================= -->
  <section id="kapcsolat" class="py-16 md:py-24 border-b" style="background-color: var(--sv-paper-cream); border-color: var(--sv-border);">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      
      <!-- Section Header -->
      <div class="max-w-3xl mb-12">
        <div class="font-mono-spec text-xs uppercase tracking-widest text-[#91372d] font-semibold mb-2" data-i18n="contact_section_tag">
          Hivatalos Elérhetőségek
        </div>
        <h2 class="font-syne font-bold text-3xl sm:text-4xl text-stone-900 leading-snug pb-1" data-i18n="contact_section_title">
          Közvetlen Kapcsolat a Gyárral
        </h2>
        <p class="text-stone-600 mt-3 text-sm sm:text-base leading-relaxed" data-i18n="contact_section_desc">
          Árajánlatkérés, beszállítói partnerség és technológiai egyeztetés esetén vegye fel a kapcsolatot közvetlenül gyárvezetésünkkel.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch">
        
        <!-- Left: Contact Details & Direct Dials (Span 7) -->
        <div class="lg:col-span-7 flex flex-col justify-between">
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 h-full">
            
            <!-- Phone Box 1 -->
            <a href="tel:+36308998548" class="p-5 rounded-2xl border transition-all hover:shadow-md group flex flex-col justify-between" style="border-color: var(--sv-border); background-color: var(--sv-surface);">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl flex items-center justify-center text-white shrink-0" style="background-color: var(--sv-burgundy);">
                  <i data-lucide="phone" class="w-5 h-5"></i>
                </div>
                <div>
                  <div class="text-[11px] font-mono-spec text-stone-500 uppercase" data-i18n="contact_mobile_label">Közvetlen Mobilkapcsolat</div>
                  <div class="font-syne font-bold text-base text-stone-900 group-hover:text-[#91372d] transition-colors">
                    +36 30 899 8548
                  </div>
                </div>
              </div>
              <p class="text-xs text-stone-600 mt-3 font-mono-spec" data-i18n="contact_rep_name">ifj. Vécsei András • Kereskedelem & Vezetés</p>
            </a>

            <!-- Phone Box 2 -->
            <a href="tel:+3622400984" class="p-5 rounded-2xl border transition-all hover:shadow-md group flex flex-col justify-between" style="border-color: var(--sv-border); background-color: var(--sv-surface);">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl flex items-center justify-center text-white shrink-0" style="background-color: var(--sv-green-dark);">
                  <i data-lucide="factory" class="w-5 h-5"></i>
                </div>
                <div>
                  <div class="text-[11px] font-mono-spec text-stone-500 uppercase" data-i18n="contact_plant_phone_label">Telephelyi Vezetékes</div>
                  <div class="font-syne font-bold text-base text-stone-900 group-hover:text-[#91372d] transition-colors">
                    +36 22 400 984
                  </div>
                </div>
              </div>
              <p class="text-xs text-stone-600 mt-3 font-mono-spec" data-i18n="contact_plant_phone_sub">Móri Gyártóüzem Központ</p>
            </a>

            <!-- Email Box -->
            <a href="mailto:ifj.vecsei.andras@sunvalley.hu" class="p-5 rounded-2xl border transition-all hover:shadow-md group sm:col-span-2 flex flex-col justify-between" style="border-color: var(--sv-border); background-color: var(--sv-surface);">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl flex items-center justify-center text-white shrink-0" style="background-color: var(--sv-orange);">
                  <i data-lucide="mail" class="w-5 h-5"></i>
                </div>
                <div>
                  <div class="text-[11px] font-mono-spec text-stone-500 uppercase" data-i18n="contact_email_label">Központi Elektronikus Levelezés</div>
                  <div class="font-syne font-bold text-base text-stone-900 group-hover:text-[#91372d] transition-colors">
                    ifj.vecsei.andras@sunvalley.hu
                  </div>
                </div>
              </div>
              <p class="text-xs text-stone-600 mt-3 font-mono-spec" data-i18n="contact_email_sub">Írásbeli ajánlatkérés és műszaki specifikációk továbbítása</p>
            </a>

          </div>
        </div>

        <!-- Right: Plant Addresses & Official Registry (Span 5) -->
        <div class="lg:col-span-5 flex flex-col">
          <div class="rounded-2xl p-6 sm:p-8 border flex flex-col justify-between h-full space-y-5" style="border-color: var(--sv-border); background-color: var(--sv-surface);">
            
            <div>
              <span class="text-xs font-mono-spec uppercase tracking-wider text-[#91372d] font-semibold" data-i18n="plant_loc_title">Telephely & Üzem</span>
              <h3 class="font-syne font-bold text-xl text-stone-900 mt-0.5">8060 Mór, Major utca 3.</h3>
              <p class="text-xs text-stone-600 mt-1 font-mono-spec">Hrsz. 3601/1 • Fejér vármegye</p>
              <a href="https://maps.google.com/?q=8060+Mór+Major+utca+3" target="_blank" rel="noopener" 
                 class="inline-flex items-center gap-1.5 text-xs font-semibold mt-2 hover:underline" style="color: var(--sv-burgundy);">
                <i data-lucide="map-pin" class="w-3.5 h-3.5 text-[#91372d]"></i>
                <span data-i18n="link_google_maps">Megtekintés Google Térképen</span>
              </a>
            </div>

            <div class="border-t pt-4" style="border-color: var(--sv-border);">
              <span class="text-xs font-mono-spec uppercase tracking-wider text-stone-500 font-semibold" data-i18n="corp_hq_title">Hivatalos Székhely</span>
              <p class="text-sm font-semibold text-stone-900 mt-0.5">1138 Budapest, Váci út 186.</p>
            </div>

            <div class="border-t pt-4 font-mono-spec text-xs space-y-1.5 text-stone-600" style="border-color: var(--sv-border);">
              <div class="flex justify-between">
                <span data-i18n="tax_id_label">Adószám:</span>
                <span class="font-bold text-stone-900">14650969-2-41</span>
              </div>
              <div class="flex justify-between">
                <span data-i18n="reg_id_label">Cégjegyzékszám:</span>
                <span class="font-bold text-stone-900">01-10-046300</span>
              </div>
              <div class="flex justify-between">
                <span data-i18n="rating_label">Pénzügyi besorolás:</span>
                <span class="font-bold text-emerald-700" data-i18n="rating_badge">AA+ Bonitás (Dun & Bradstreet)</span>
              </div>
            </div>

          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- FOOTER                                                                    -->
  <!-- ========================================================================= -->
  <footer class="py-10 border-t text-xs font-mono-spec transition-colors"
          style="background-color: var(--sv-burgundy-dark); color: rgba(245, 242, 238, 0.7); border-color: rgba(255,255,255,0.1);">
    <div class="max-w-7xl mx-auto px-4 sm:px-8 space-y-6">
      
      <div class="flex flex-col md:flex-row items-center justify-between gap-4 border-b pb-6 border-white/10">
        <div class="flex items-center gap-3">
          <img src="assets/sun-valley-logo.webp" alt="Sun Valley Logo" width="160" height="40" loading="lazy" decoding="async" class="h-9 sm:h-10 w-auto object-contain">
          <div>
            <div class="font-bold text-white font-syne text-base">Sun Valley Zrt.</div>
            <div class="text-[10px] text-white/60" data-i18n="footer_tagline">Ipari Gyümölcstechnológia Mór • Alapítva: 2009</div>
          </div>
        </div>

        <div class="flex flex-wrap items-center gap-6 text-white/80">
          <a href="#termekek" class="hover:text-white transition-colors" data-i18n="nav_products">Termékek</a>
          <a href="#technologia" class="hover:text-white transition-colors" data-i18n="nav_tech">Technológia</a>
          <a href="#egyedi-fejlesztes" class="hover:text-white transition-colors" data-i18n="nav_rd">Receptúra</a>
          <a href="#disztribucio" class="hover:text-white transition-colors" data-i18n="nav_distribution">Disztribúció</a>
          <a href="#kapcsolat" class="hover:text-white transition-colors" data-i18n="nav_contact">Kapcsolat</a>
        </div>
      </div>

      <div class="flex flex-col md:flex-row items-center justify-between gap-4 text-[11px] text-white/50">
        <div>
          <span data-i18n="footer_rights">© 2026 Sun Valley Kereskedelmi Zrt. • Minden jog fenntartva.</span>
        </div>
        <div class="flex items-center gap-4">
          <span data-i18n="topbar_rating">AA+ Pénzügyi Minősítés</span>
          <span>•</span>
          <span data-i18n="footer_cert_iso">ISO / HACCP Szabvány</span>
          <span>•</span>
          <span data-i18n="footer_cert_plant">Móri Gyártóbázis</span>
        </div>
      </div>

    </div>
  </footer>

  <!-- ========================================================================= -->
  <!-- INTERACTIVE TDS MODAL DIALOGUE                                            -->
  <!-- ========================================================================= -->
  <div id="tds-modal" class="fixed inset-0 z-50 bg-black/65 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-2xl w-full max-h-[90vh] overflow-y-auto border shadow-2xl p-6 sm:p-8 relative font-sans"
         style="border-color: var(--sv-border);">
      
      <!-- Close Button -->
      <button onclick="closeTdsModal()" class="absolute top-5 right-5 p-2 rounded-xl border text-stone-500 hover:text-stone-900 transition-colors" style="border-color: var(--sv-border-light);" aria-label="Ablak bezárása">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>

      <!-- Modal Content Area -->
      <div id="tds-modal-content">
        <!-- Dynamically injected via JavaScript with full i18n -->
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
        btn_download_prospectus: "Prospektus Letöltése (.PPTX)",
        btn_view_category_tds: "TDS Adatlap Megtekintése",
        btn_view_full_tds: "Részletes TDS Műszaki Adatlap",
        card_hero_cat: "PRÉMIUM PÉKIPARI TÉSZTABETÉT",
        card_hero_desc: "Formatartó, természetes aromájú töltelék magas hőmérsékletű sütéshez. Leveles tésztákban és kelt tésztákban sem enged szabad vizet.",
        card_hero_title: "SV Sütésálló Kajszibarack & Vegyes Íz",
        cat_apps_label: "Jellemző Pékipari Alkalmazások:",
        cat_section_desc: "Válasszon technológiai kategóriát: lapozzon a kenhető lekvárok, a 180–220 °C sütésálló töltelékek és az extra dzsemek között a bal és jobb oldali nyilakkal.",
        cat_section_tag: "Termékportfólió & Minőségi Specifikációk",
        cat_section_title: "Lekvárok felhasználás szerint",
        cat_tab_spreadable: "1. Kenhető lekvárok",
        cat_tab_bake_stable: "2. Sütésálló lekvárok",
        cat_tab_extra_jam: "3. Extra dzsemek",
        cat_flip_hint: "Lapozzon a nyilakkal vagy fülekkel",
        contact_email_label: "Központi Elektronikus Levelezés",
        contact_email_sub: "Írásbeli ajánlatkérés és műszaki specifikációk továbbítása",
        contact_mobile_label: "Közvetlen Mobilkapcsolat",
        contact_plant_phone_label: "Telephelyi Vezetékes",
        contact_plant_phone_sub: "Móri Gyártóüzem Központ",
        contact_rep_name: "ifj. Vécsei András • Kereskedelem & Vezetés",
        contact_section_desc: "Árajánlatkérés, beszállítói partnerség és technológiai egyeztetés esetén vegye fel a kapcsolatot közvetlenül gyárvezetésünkkel.",
        contact_section_tag: "Hivatalos Elérhetőségek",
        contact_section_title: "Közvetlen Kapcsolat a Gyárral",
        corp_hq_title: "Hivatalos Székhely",
        dist_section_desc: "Rugalmas logisztikai modellünk két csatornán biztosítja az ellátásbiztonságot: közvetlen gyári szerződéssel ipari mennyiségekre, vagy országos nagykereskedelmi partnereinken keresztül azonnali raktári kiszolgálásra.",
        dist_section_tag: "Értékesítési Csatornák & Logisztika",
        dist_section_title: "Hogyan Jut El a Termék az Ön Üzemébe?",
        dist_t1_badge: "1. CSATORNA • IPARI SZERZŐDÉSEK",
        dist_t1_cta: "Ipari Keretszerződés Egyeztetése",
        dist_t1_desc: "Nagyipari kenyérgyárak és finompékáru-üzemek részére (>500 kg / megrendelés). Közvetlen gyári egyedi árképzés, ütemezett lehívások, tételes sarzshomogenitás és folyamatos technológiai támogatás.",
        dist_t1_p1: "480 kg raklapos standard egységek",
        dist_t1_p2: "Garantált tételes sarzs-homogenitás",
        dist_t1_p3: "Közvetlen telephelyi kapcsolattartó",
        dist_t1_title: "Közvetlen Gyári Szállítás (Raklapos & Kamionos Tételek)",
        dist_t2_badge: "2. CSATORNA • RAKTÁRI KISZOLGÁLÁS",
        dist_t2_desc: "Közepes cukrászatok és kézműves pékségek az országos lefedettségű partner-nagykereskedőink raktáraiból azonnal megvásárolhatják az 5–10 kg-os kiszereléseket.",
        dist_t2_footer: "Érdeklődjön helyi pékszövetségi vagy nagykereskedelmi területi képviselőjénél.",
        dist_t2_title: "Országos Nagykereskedelmi Partnerhálózat",
        exotic_citrus: "Citrus & Narancs",
        exotic_desc: "Az alapízeken túl trópusi és egzotikus gyümölcsökből is fejlesztünk egyedi receptúrát a kívánt ízvilághoz, állaghoz és technológiához. Legyen szó mangóról, maracujáról vagy citrusos készítményekről, móri laborunkban finomhangoljuk a hőtűrést és a viszkozitást.",
        exotic_img_badge: "R&D LABORATÓRIUM",
        exotic_img_title: "Egyedi Gyümölcskombinációk",
        exotic_mango: "Mangó & Maracuja",
        exotic_note: "* Az egzotikus receptúrákat technológiai egyeztetés és receptúra-fejlesztés alapján véglegesítjük a partner saját gépsoraira.",
        exotic_pineapple: "Ananász & Kivi",
        exotic_tag: "Egyedi Fejlesztési Irányok • Innováció",
        exotic_title: "Egzotikus Ízek. Az Ön Termékére Hangolva.",
        flavor_apple: "Alma",
        flavor_apricot: "Sárgabarack",
        flavor_blueberry: "Áfonya",
        flavor_classic_mixed: "Klasszikus Vegyes Gyümölcs",
        flavor_plum: "Szilva",
        flavor_raspberry: "Málna",
        flavor_sour_cherry: "Meggy",
        flavors_badge: "HAZAI GYÜMÖLCSBÁZIS",
        flavors_cta: "Részletes műszaki paraméterek megtekintése a termékmátrixban",
        flavors_desc: "A magyar pékipar és cukrászat legkedveltebb hagyományos gyümölcseit dolgozzuk fel korszerű vákuumüstjeinkben. A termékeket a partner technológiájához igazítva állítjuk be mind sütésálló, mind hidegen kenhető formában.",
        flavors_img_title: "7 Alapvető Pékipari Gyümölcsíz",
        flavors_tag: "Hagyományos Ízvilág • Korszerű Technológia",
        flavors_title: "Ismerős Ízek. Megbízható Ipari Minőség.",
        footer_cert_iso: "ISO / HACCP Szabvány",
        footer_cert_plant: "Móri Gyártóbázis",
        footer_rights: "© 2026 Sun Valley Kereskedelmi Zrt. • Minden jog fenntartva.",
        footer_tagline: "Ipari Gyümölcstechnológia Mór • Alapítva: 2009",
        hero_badge: "B2B Kenyérgyári & Finompékáru Alapanyagok",
        hero_card_pill: "SÜTÉSÁLLÓ • 200°C+",
        hero_cta_catalog: "Lapozható Termékkatalógus",
        hero_cta_prospectus: "Prospektus (.PPTX)",
        hero_cta_sample: "Kapcsolatfelvétel & Ajánlatkérés",
        hero_desc: "A Sun Valley Zrt. a magyar finompékáru-üzemek és ipari kenyérgyárak megbízható belföldi beszállítója. Forma- és alaktartó, gépileg szeletelhető tésztabetétek 10 kg-os kartonos és 5 kg-os vödrös kiszerelésben, közvetlen móri gyártóbázisról.",
        hero_direct_badge: "KÖZVETLEN GYÁRI SZÁLLÍTÁS",
        hero_h1_p1: "200 °C felett sem forr ki.",
        hero_h1_p2: "Ipari sütésálló",
        hero_h1_p3: "gyümölcstöltelékek közvetlenül a gyártótól.",
        hero_qc_badge: "MÓRI GYÁRI MINŐSÉG-ELLENŐRZÉS #SV-2026",
        link_google_maps: "Megtekintés Google Térképen",
        nav_catalog: "Termékkatalógus",
        nav_contact: "Gyártóüzem & Elérhetőség",
        nav_distribution: "Nagykereskedelmi Hálózat",
        nav_products: "Termékek & TDS",
        nav_prospectus: "Prospektus",
        nav_rd: "Receptúra & Fejlesztés",
        nav_tech: "Sütésállóság (200°C)",
        plant_loc_title: "Telephely & Üzem",
        prod_section_desc: "Nagyüzemi pékségek, kenyérgyárak és cukrászatok számára gyártott megbízható gyümölcskészítmények közvetlenül a Fejér vármegyei móri gyárunkból.",
        prod_section_tag: "Termékportfólió & Minőségi Specifikációk",
        prod_section_title: "Három Fő Termékkategória. Garantált Ipari Teljesítmény.",
        prod_cat1_badge: "CUKRÁSZATI VÖDRÖS & HORDÓS",
        prod_cat1_title: "Kenhető lekvárok",
        prod_cat1_subtitle: "Selymes, homogén állag linzerekhez, piskótákhoz és tortalapokhoz",
        prod_cat1_desc: "Hideg technológiára kifejlesztett, egyenletesen és könnyen kenhető gyümölcskészítmények piskótatekercsek, tortalapok és linzer sütemények tiszta, szakadásmentes töltéséhez. Kiemelkedő természetes gyümölcsös aroma, tiszta ízvilág és intenzív fényesség jellemzi.",
        prod_cat2_badge: "IPARI PÉKIPARI TÖMB & VÖDÖR",
        prod_cat2_title: "Sütésálló lekvárok",
        prod_cat2_subtitle: "Formamegtartó, 180 °C és 220 °C között sem kiforró tésztabetétek",
        prod_cat2_desc: "Speciális hidrokolloid- és pektinmátrix révén a tészta magas hőfokú sütése során sem forrnak ki, nem áztatják el a tésztát, és hűlés után is megőrzik rugalmas, alaktartó gélállagukat. Kiválóan alkalmasak ipari adagoló-, töltő- és automata szeletelőgépekre.",
        prod_cat3_badge: "PRÉMIUM CUKRÁSZATI & PÉKIPARI",
        prod_cat3_title: "Extra dzsemek",
        prod_cat3_subtitle: "Válogatott gyümölcsök, intenzív gyümölcsdarabos textúra és természetes ízek",
        prod_cat3_desc: "Magas gyümölcshányadú, kíméletes vákuumfőzéssel készült prémium dzsemek egész és vágott gyümölcsdarabokkal. Kifejezetten prémium cukrászati finompékárukhoz, látványpékségi süteményekhez és desszertbetétekhez.",
        prod_flavors_label: "Elérhető Ízek (Azonos Technológiai Paraméterekkel):",
        btn_inquire_jam: "Érdeklődés & Ajánlatkérés",
        badge_cold_process: "Hideg Technológia • Azonnal Kenhető",
        badge_heat_stable: "180 °C – 220 °C Sütésálló",
        badge_extra_jam: "Prémium Gyümölcsdarabos • Magas Gyümölcstartalom",
        cat_img_caption_spread: "Cukrászati felhasználás • Homogén selymes terülés piskótán, tortalapokon és linzereken",
        cat_img_caption_bake: "Sütésállósági teszt • Kelt tészta bukták 200 °C feletti sütés után, alaktartó töltelékkel",
        cat_img_caption_extra: "Prémium finompékáru • Intenzív gyümölcsdarabos textúra croissant-ban és dán pékáruban",
        cat_apps_label_pastry: "Jellemző Cukrászati Felhasználás:",
        cat_apps_label_extra: "Jellemző Felhasználás:",
        spec_lbl_tech: "Technológia",
        spec_val_cold: "Hideg eljárás",
        spec_lbl_heat: "Hőtűrés",
        spec_lbl_texture: "Textúra",
        spec_val_chunky: "Darabos prémium",
        spec_lbl_pack: "Kiszerelések",
        spec_lbl_shelf: "Szavatosság",
        spec_val_shelf9: "9–12 hónap",
        spec_val_shelf12: "12 hónap",
        prospectus_badge: "HIVATALOS B2B DOKUMENTÁCIÓ • V1.4",
        prospectus_desc: "A prezentáció részletesen bemutatja móri üzemünk technológiai gépsorait, a teljes sütésálló és hidegtechnológiás termékpalettát, a logisztikai paritásokat és a minőségbiztosítási garanciákat.",
        prospectus_format: "Formátum: Microsoft PowerPoint (.pptx)",
        prospectus_size: "Méret: ~11,1 MB",
        prospectus_title: "Töltse le a Sun Valley Zrt. Hivatalos Vállalati Prospektusát",
        prospectus_version: "Verzió: V1.4 (2026)",
        rating_badge: "AA+ Bonitás (Dun & Bradstreet)",
        rating_label: "Pénzügyi besorolás:",
        rd_section_desc: "Nem minden gyártósor és késztermék egyforma. Az egyedi receptúra-fejlesztés során a technológusokkal közösen alakítjuk ki az ideális tölteléket 3 lépésben:",
        rd_section_tag: "Egyedi Termékfejlesztési Folyamat",
        rd_section_title: "Az Ön Ötlete. Közös Ipari Fejlesztés.",
        rd_step1_desc: "Felhasználás, ízvilág, elvárt gyümölcstartalom, állag, sütési hőmérséklet (180–220 °C) és a gépsor adagolási feltételeinek pontos felmérése.",
        rd_step1_title: "Az Igény Megismerése",
        rd_step2_desc: "Laboratóriumi fejlesztés és kísérleti próbasütés, a receptúra pontos beállítása a partner saját gépsorain történő technológiai elvárásokhoz.",
        rd_step2_title: "Receptúra & Technológiai Hangolás",
        rd_step3_desc: "A végleges műszaki specifikáció (TDS) rögzítése, a csomagolás (vödör, kartontömb, hordó) kiválasztása és a stabil ütemezett raklapos szállítás elindítása.",
        rd_step3_title: "Gyártásra Hangolva",
        rd_tag_1: "Audit & Paraméterezés",
        rd_tag_2: "Fejlesztés & Validáció",
        rd_tag_3: "TDS Rögzítés & Szállítás",
        reg_id_label: "Cégjegyzékszám:",
        spec_brix: "Szárazanyagtartalom (Brix)",
        spec_slice: "Szeletelhetőség (Gépi késállás)",
        spec_slice_val: "Kiváló / Tiszta vágás",
        spec_thermo: "Hőállóság (200 °C / 15 perc)",
        spec_thermo_val: "Alaktartó / Nem forr ki",
        stat_energy: "Energiatudatos Móri Gyártelep",
        stat_energy_val: "VEP Díjas",
        stat_heritage: "Gyümölcsfeldolgozói múlt (Vitamór bázis)",
        stat_heritage_val: "15+ Év",
        stat_rating: "Pénzügyi minősítés (Adósságmentes)",
        stat_revenue: "Éves árbevétel (Stabil tőkeerő)",
        stat_revenue_val: "1,1 – 1,3 Mrd Ft",
        tagline: "Ipari Gyümölcstechnológia • Alapítva: 2009",
        tax_id_label: "Adószám:",
        tech_badge_dosing: "AUTOMATA ADAGOLÁS",
        tech_badge_freeze: "FAGYASZTÁSÁLLÓ",
        tech_card1_desc: "200 °C felett sem forr ki a süteményből, nem ég le a tepsire, és megőrzi térfogatát a tésztában szinerézis (vízkiválás) nélkül.",
        tech_card1_title: "Garantált Sütésállóság",
        tech_card2_desc: "Fagyasztott félkész és fagyasztva tárolt késztermékekhez kifejlesztve. Felengedéskor nem enged levet, nem áztatja el a tésztát.",
        tech_card2_title: "Fagyasztásállóság",
        tech_card3_desc: "A kézi kenéstől a nagyteljesítményű automata tüskés injektálósorokig (fánkok, croissant-ok) állandó, nyírásra stabil viszkozitás.",
        tech_card3_title: "Gépi Tölthetőség & Pumpálás",
        tech_card4_desc: "5 kg-os vödörben a cukrászatoknak, 10 kg-os szeletelhető kartontömbökben kenyérgyáraknak, vagy 200 kg-os hordókban nagyüzemeknek.",
        tech_card4_title: "Kis Szériától Ipari Léptékig",
        tech_section_desc: "A finompékáru-gyártásban a selejtképződés legfőbb oka a töltelék kiforrása, a tészta elázása vagy a gépi adagolófejek eldugulása. A Sun Valley Zrt. hidrokolloid- és pektinmátrixa négy technológiai alappillérre épül:",
        tech_section_tag: "Élelmiszer-technológiai Garanciák",
        tech_section_title: "Nem Csak Az Íz Számít. Technológia & Megbízhatóság.",
        telemetry_geo_label: "Gyártótelep",
        telemetry_geo_sub: "Major utca 3.",
        telemetry_heat_label: "Hőtűrési küszöb",
        telemetry_heat_sub: "Nem forr ki, alaktartó",
        telemetry_pack_label: "Ipari Kiszerelés",
        telemetry_pack_sub: "480 kg raklapos tétel",
        topbar_capacity: "Éves árbevétel: 1,1–1,3 Mrd Ft",
        topbar_rating: "AA+ Pénzügyi Minősítés",
        topbar_scale: "Ipari Gyártóbázis: Mór (Major u. 3.)"
      },

      en: {
        btn_download_prospectus: "Download Brochure (.PPTX)",
        btn_view_category_tds: "View Category TDS Sheet",
        btn_view_full_tds: "View Detailed TDS Specification",
        card_hero_cat: "COMMERCIAL BAKERY INSERT",
        card_hero_desc: "Form-retaining fruit preparation with intense natural aroma for high-heat baking. Zero syneresis in puff pastries and yeast doughs.",
        card_hero_title: "SV Bake-Stable Apricot & Mixed Fruit",
        cat_apps_label: "Verified Industrial Applications:",
        cat_section_desc: "Select an industrial category: flip through spreadable jams, 180–220 °C bake-stable fillings, and extra jams using the left and right navigation arrows.",
        cat_section_tag: "Product Portfolio & Quality Specifications",
        cat_section_title: "Jams by Application",
        cat_tab_spreadable: "1. Spreadable Jams",
        cat_tab_bake_stable: "2. Bake-Stable Jams",
        cat_tab_extra_jam: "3. Extra Jams",
        cat_flip_hint: "Flip with arrows or tabs",
        contact_email_label: "Corporate Email Address",
        contact_email_sub: "Formal quotes and technical inquiries",
        contact_mobile_label: "Direct Mobile Line",
        contact_plant_phone_label: "Plant Landline",
        contact_plant_phone_sub: "Mór Manufacturing Headquarters",
        contact_rep_name: "András Vécsei Jr. • Commercial Director",
        contact_section_desc: "For quotations, supplier partnerships, and technical inquiries, reach out directly to our plant leadership team.",
        contact_section_tag: "Official Contact",
        contact_section_title: "Direct Communication with Plant Management",
        corp_hq_title: "Corporate Headquarters",
        dist_section_desc: "Our dual-track distribution ensures absolute reliability: direct factory contracts for bulk tonnage, or regional wholesale partners for immediate depot pick-up.",
        dist_section_tag: "Distribution & Logistics",
        dist_section_title: "How Products Reach Your Facility",
        dist_t1_badge: "CHANNEL 1 • ENTERPRISE CONTRACTS",
        dist_t1_cta: "Discuss Enterprise Framework",
        dist_t1_desc: "For industrial bread factories (>500 kg / delivery). Direct factory pricing, scheduled shipments, and dedicated technical line support.",
        dist_t1_p1: "480 kg palletized standard units",
        dist_t1_p2: "Guaranteed batch-to-batch homogeneity",
        dist_t1_p3: "Direct plant account manager",
        dist_t1_title: "Direct Factory Supply (Pallet & Truckload Orders)",
        dist_t2_badge: "CHANNEL 2 • REGIONAL DEPOTS",
        dist_t2_desc: "Mid-sized bakeries and confectioneries can source 5–10 kg containers directly from our authorized distributors across Hungary.",
        dist_t2_footer: "Contact your regional bakery supply distributor.",
        dist_t2_title: "Authorized Wholesale Partner Network",
        exotic_citrus: "Citrus & Orange",
        exotic_desc: "Beyond traditional fruit bases, we engineer customized formulations from tropical and exotic fruits tailored to your desired flavor profile, viscosity, and thermal requirements.",
        exotic_img_badge: "R&D LABORATORY",
        exotic_img_title: "Custom Fruit Combinations",
        exotic_mango: "Mango & Passionfruit",
        exotic_note: "* Exotic formulations are finalized following technical consultation and custom recipe development for your production lines.",
        exotic_pineapple: "Pineapple & Kiwi",
        exotic_tag: "Custom R&D • Product Innovation",
        exotic_title: "Exotic Flavors. Engineered for Your Product.",
        flavor_apple: "Apple",
        flavor_apricot: "Apricot",
        flavor_blueberry: "Blueberry",
        flavor_classic_mixed: "Classic Mixed Fruit",
        flavor_plum: "Plum",
        flavor_raspberry: "Raspberry",
        flavor_sour_cherry: "Sour Cherry",
        flavors_badge: "DOMESTIC FRUIT BASE",
        flavors_cta: "View technical parameters in the product matrix",
        flavors_desc: "We process Hungary's most celebrated domestic fruits in modern vacuum boiling vessels, customized to your exact baking or spreading technology.",
        flavors_img_title: "7 Essential Bakery Fruit Flavors",
        flavors_tag: "Heritage Flavors • Modern Processing",
        flavors_title: "Familiar Flavors. Industrial Precision.",
        footer_cert_iso: "ISO / HACCP Standard",
        footer_cert_plant: "Mór Manufacturing Plant",
        footer_rights: "© 2026 Sun Valley Kereskedelmi Zrt. • All rights reserved.",
        footer_tagline: "Industrial Fruit Technology Mór • Est. 2009",
        hero_badge: "B2B Commercial Bakery & Pastry Ingredients",
        hero_card_pill: "BAKE-STABLE • 200°C+",
        hero_cta_catalog: "Flippable Product Catalog",
        hero_cta_prospectus: "Download Brochure (.PPTX)",
        hero_cta_sample: "Contact & Request Quote",
        hero_desc: "Sun Valley Zrt. is a proven supplier for industrial bread factories and commercial pastry plants. Shape-retaining, mechanically sliceable fruit fillings in 10 kg cartons and 5 kg buckets directly from our Mór facility.",
        hero_direct_badge: "DIRECT FACTORY SUPPLY",
        hero_h1_p1: "No boil-out above 200 °C.",
        hero_h1_p2: "Industrial bake-stable",
        hero_h1_p3: "Fruit preparations directly from the manufacturer.",
        hero_qc_badge: "MÓR FACTORY QC #SV-2026",
        link_google_maps: "View on Google Maps",
        nav_catalog: "Product Catalog",
        nav_contact: "Plant & Contact",
        nav_distribution: "Wholesale Network",
        nav_products: "Products & TDS",
        nav_prospectus: "Brochure",
        nav_rd: "Formulation & R&D",
        nav_tech: "Thermo-Stability (200°C)",
        plant_loc_title: "Plant & Production Site",
        prod_section_desc: "Reliable fruit preparations manufactured for industrial bakeries, bread factories and confectioneries directly from our plant in Mór, Hungary.",
        prod_section_tag: "Product Portfolio & Quality Specifications",
        prod_section_title: "Three Core Product Categories. Guaranteed Industrial Performance.",
        prod_cat1_badge: "CONFECTIONERY BUCKET & DRUM",
        prod_cat1_title: "Spreadable Jams",
        prod_cat1_subtitle: "Smooth, homogeneous texture for linzers, sponge rolls, and cake layers",
        prod_cat1_desc: "Formulated for cold processing, offering uniform, tear-free spreadability for sponge rolls, cake bases, and linzer pastries with rich natural fruit aroma and bright gloss.",
        prod_cat2_badge: "INDUSTRIAL BAKE-STABLE BLOCK & BUCKET",
        prod_cat2_title: "Bake-Stable Jams",
        prod_cat2_subtitle: "Shape-retaining, boil-proof fillings between 180 °C and 220 °C",
        prod_cat2_desc: "Engineered with a proprietary hydrocolloid and pectin matrix to prevent boiling out at high temperatures, avoiding sogginess and maintaining an elastic shape upon cooling. Ideal for automated depositors and cutters.",
        prod_cat3_badge: "PREMIUM CONFECTIONERY & BAKERY",
        prod_cat3_title: "Extra Jams",
        prod_cat3_subtitle: "Carefully selected whole & diced fruit pieces with vibrant natural taste",
        prod_cat3_desc: "Crafted with high fruit concentration and gentle vacuum cooking, keeping fruit pieces intact. Formulated for artisan patisserie, Danish pastries, and high-end dessert layers.",
        prod_flavors_label: "Available Flavors (Identical Technical Parameters):",
        btn_inquire_jam: "Inquire & Request Quotation",
        badge_cold_process: "Cold Process • Instantly Spreadable",
        badge_heat_stable: "180 °C – 220 °C Bake-Stable",
        badge_extra_jam: "Premium Fruit Pieces • High Fruit Content",
        cat_img_caption_spread: "Confectionery application • Smooth, silky spreading on sponge rolls, cakes, and linzers",
        cat_img_caption_bake: "Bake-stability test • Yeast dough buns baked above 200 °C with shape-retaining filling",
        cat_img_caption_extra: "Artisan pastry • Intensely fruity texture in croissants and Danish pastries",
        cat_apps_label_pastry: "Typical Confectionery Applications:",
        cat_apps_label_extra: "Typical Applications:",
        spec_lbl_tech: "Technology",
        spec_val_cold: "Cold process",
        spec_lbl_heat: "Heat Stability",
        spec_lbl_texture: "Texture",
        spec_val_chunky: "Chunky premium",
        spec_lbl_pack: "Packaging",
        spec_lbl_shelf: "Shelf Life",
        spec_val_shelf9: "9–12 months",
        spec_val_shelf12: "12 months",
        prospectus_badge: "OFFICIAL B2B BROCHURE • V1.4",
        prospectus_desc: "Detailed presentation covering our Mór manufacturing facility, boiling technology, complete product portfolio, logistics parities, and quality assurance standards.",
        prospectus_format: "Format: Microsoft PowerPoint (.pptx)",
        prospectus_size: "File size: ~11.1 MB",
        prospectus_title: "Download the Official Sun Valley Corporate Brochure",
        prospectus_version: "Version: V1.4 (2026)",
        rating_badge: "AA+ Rating (Dun & Bradstreet)",
        rating_label: "Credit Rating:",
        rd_section_desc: "Every production line is unique. We partner with industrial bakeries in 3 structured phases:",
        rd_section_tag: "Custom Formulation Pipeline",
        rd_section_title: "Your Concept. Collaborative R&D.",
        rd_step1_desc: "Auditing application type, fruit %, viscosity, oven profile (180–220 °C), and depositor nozzle specifications.",
        rd_step1_title: "Requirement Scoping",
        rd_step2_desc: "Laboratory development and experimental test baking, precisely adjusting the formula to meet production line criteria.",
        rd_step2_title: "Formulation & Line Optimization",
        rd_step3_desc: "Locking technical specifications (TDS), selecting packaging units, and scheduling ongoing palletized deliveries.",
        rd_step3_title: "Production Integration",
        rd_tag_1: "Audit & Specifications",
        rd_tag_2: "Development & Validation",
        rd_tag_3: "TDS Finalization & Logistics",
        reg_id_label: "Company Reg.:",
        spec_brix: "Dry Matter (Brix)",
        spec_slice: "Sliceability (Machine cut)",
        spec_slice_val: "Clean cut edge / Firm gel",
        spec_thermo: "Heat stability (200 °C / 15 min)",
        spec_thermo_val: "Form-stable / No boil-out",
        stat_energy: "Energy-Conscious Plant Award",
        stat_energy_val: "VEP Awarded",
        stat_heritage: "Fruit Processing Heritage (Vitamór heritage)",
        stat_heritage_val: "15+ Years",
        stat_rating: "Credit Rating (Debt-free AA+)",
        stat_revenue: "Annual Turnover (Financial strength)",
        stat_revenue_val: "€2.8M – €3.3M",
        tagline: "Industrial Food Technology • Est. 2009",
        tax_id_label: "Tax ID / VAT:",
        tech_badge_dosing: "AUTOMATED DOSING",
        tech_badge_freeze: "FREEZE-THAW STABLE",
        tech_card1_desc: "Maintains geometry and volume above 200 °C without boiling out or scorching baking trays.",
        tech_card1_title: "Guaranteed Bake-Stability",
        tech_card2_desc: "Formulated for frozen unbaked and par-baked doughs. Zero water separation upon defrosting.",
        tech_card2_title: "Freeze-Thaw Stability",
        tech_card3_desc: "Shear-thinning viscosity designed for automated needle depositors (doughnuts, croissants) without dripping.",
        tech_card3_title: "Automated Dosing & Injection",
        tech_card4_desc: "5 kg buckets for artisan confectionery, 10 kg sliceable carton blocks, and 200 kg aseptic drums for large plants.",
        tech_card4_title: "From Trial to Factory Scale",
        tech_section_desc: "In commercial pastry production, scrap rates are driven by boil-outs, crust sogginess, or nozzle clogging. Sun Valley's hydrocolloid matrix is built on four core technical pillars:",
        tech_section_tag: "Food Engineering Assurances",
        tech_section_title: "More than Flavor. Process Engineering.",
        telemetry_geo_label: "Plant Facility",
        telemetry_geo_sub: "Major utca 3., Mór",
        telemetry_heat_label: "Thermal Threshold",
        telemetry_heat_sub: "No boil-out, form-stable",
        telemetry_pack_label: "Packaging Scale",
        telemetry_pack_sub: "480 kg palletized standard",
        topbar_capacity: "Annual Turnover: €2.8M–€3.3M",
        topbar_rating: "AA+ Financial Credit Rating",
        topbar_scale: "Manufacturing Plant: Mór, Hungary (Major u. 3.)"
      }
    };

    const catalogData = {
      "spreadable": {
        indexNum: "01",
        badge: { hu: "CUKRÁSZATI VÖDRÖS & HORDÓS", en: "CONFECTIONERY BUCKET & DRUM" },
        badgeColor: "var(--sv-green-dark)",
        imageBadge: { hu: "Hideg Technológia • Azonnal Kenhető", en: "Cold Process • Instantly Spreadable" },
        imageBadgeBg: "#2D3628",
        title: { hu: "Kenhető lekvárok", en: "Spreadable Jams" },
        subtitle: { hu: "Selymes, homogén állag linzerekhez, piskótákhoz és tortalapokhoz", en: "Smooth, homogeneous texture for linzers, sponge rolls, and cake layers" },
        desc: {
          hu: "Hideg technológiára kifejlesztett, egyenletesen és könnyen kenhető gyümölcskészítmények piskótatekercsek, tortalapok és linzer sütemények tiszta, szakadásmentes töltéséhez. Kiemelkedő természetes gyümölcsös aroma, tiszta ízvilág és intenzív fényesség jellemzi.",
          en: "Formulated for cold processing, offering uniform, tear-free spreadability for sponge rolls, cake bases, and linzer pastries with rich natural fruit aroma and bright gloss."
        },
        specs: [
          { label: { hu: "Technológia", en: "Technology" }, val: { hu: "Hideg eljárás", en: "Cold process" }, isHighlight: true },
          { label: { hu: "Kiszerelések", en: "Packaging" }, val: { hu: "5, 10, 20, 200 kg", en: "5, 10, 20, 200 kg" } },
          { label: { hu: "Szavatosság", en: "Shelf Life" }, val: { hu: "9–12 hónap", en: "9–12 months" } }
        ],
        flavors: ["Sárgabarack", "Málna", "Eper", "Kerti meggy", "Erdei áfonya", "Feketeribizli", "Narancs"],
        appsLabel: { hu: "Jellemző Cukrászati Felhasználás:", en: "Typical Confectionery Applications:" },
        apps: {
          hu: ["Linzerkarika", "Piskótatekercs", "Tortalapok kenése", "Desszertbetétek", "Fánkáthúzás"],
          en: ["Linzer Cookies", "Sponge Roll", "Cake Layering", "Dessert Inclusions", "Donut Glazing"]
        },
        imageWebp: "assets/jam.webp",
        imageJpg: "assets/jam.jpg",
        caption: {
          hu: "Cukrászati felhasználás • Homogén selymes terülés piskótán, tortalapokon és linzereken",
          en: "Confectionery application • Smooth, silky spreading on sponge rolls, cakes, and linzers"
        }
      },
      "bake-stable": {
        indexNum: "02",
        badge: { hu: "IPARI PÉKIPARI TÖMB & VÖDÖR", en: "INDUSTRIAL BAKE-STABLE BLOCK & BUCKET" },
        badgeColor: "var(--sv-burgundy)",
        imageBadge: { hu: "180 °C – 220 °C Sütésálló", en: "180 °C – 220 °C Bake-Stable" },
        imageBadgeBg: "#a3392e",
        title: { hu: "Sütésálló lekvárok", en: "Bake-Stable Jams" },
        subtitle: { hu: "Formamegtartó, 180 °C és 220 °C között sem kiforró tésztabetétek", en: "Shape-retaining, boil-proof fillings between 180 °C and 220 °C" },
        desc: {
          hu: "Speciális hidrokolloid- és pektinmátrix révén a tészta magas hőfokú sütése során sem forrnak ki, nem áztatják el a tésztát, és hűlés után is megőrzik rugalmas, alaktartó gélállagukat. Kiválóan alkalmasak ipari adagoló-, töltő- és automata szeletelőgépekre.",
          en: "Engineered with a proprietary hydrocolloid and pectin matrix to prevent boiling out at high temperatures, avoiding sogginess and maintaining an elastic shape upon cooling. Ideal for automated depositors and cutters."
        },
        specs: [
          { label: { hu: "Hőtűrés", en: "Heat Stability" }, val: { hu: "180 °C – 220 °C", en: "180 °C – 220 °C" }, isHighlight: true },
          { label: { hu: "Kiszerelések", en: "Packaging" }, val: { hu: "5, 10, 20, 200 kg", en: "5, 10, 20, 200 kg" } },
          { label: { hu: "Szavatosság", en: "Shelf Life" }, val: { hu: "12 hónap", en: "12 months" } }
        ],
        flavors: ["Vegyes gyümölcsíz", "Sárgabarack", "Szilva", "Feketeerdő meggy", "Alma-fahéj", "Eper", "Erdei gyümölcs"],
        appsLabel: { hu: "Jellemző Pékipari Felhasználás:", en: "Typical Bakery Applications:" },
        apps: {
          hu: ["Lekváros bukta", "Rétesek", "Lekváros papucs", "Rácsos linzer", "Leveles táskák"],
          en: ["Jam Buns", "Strudels", "Fruit Turnovers", "Lattice Linz Tarts", "Puff Pastries"]
        },
        imageWebp: "assets/lekvaros-bukta.webp",
        imageJpg: "assets/lekvaros-bukta.jpg",
        caption: {
          hu: "Sütésállósági teszt • Kelt tészta bukták 200 °C feletti sütés után, alaktartó töltelékkel",
          en: "Bake-stability test • Yeast dough buns baked above 200 °C with shape-retaining filling"
        }
      },
      "extra-jam": {
        indexNum: "03",
        badge: { hu: "PRÉMIUM CUKRÁSZATI & PÉKIPARI", en: "PREMIUM CONFECTIONERY & BAKERY" },
        badgeColor: "var(--sv-orange)",
        imageBadge: { hu: "Prémium Gyümölcsdarabos • Magas Gyümölcstartalom", en: "Premium Fruit Pieces • High Fruit Content" },
        imageBadgeBg: "#E36527",
        title: { hu: "Extra dzsemek", en: "Extra Jams" },
        subtitle: { hu: "Válogatott gyümölcsök, intenzív gyümölcsdarabos textúra és természetes ízek", en: "Carefully selected whole & diced fruit pieces with vibrant natural taste" },
        desc: {
          hu: "Magas gyümölcshányadú, kíméletes vákuumfőzéssel készült prémium dzsemek egész és vágott gyümölcsdarabokkal. Kifejezetten prémium cukrászati finompékárukhoz, látványpékségi süteményekhez és desszertbetétekhez.",
          en: "Crafted with high fruit concentration and gentle vacuum cooking, keeping fruit pieces intact. Formulated for artisan patisserie, Danish pastries, and high-end dessert layers."
        },
        specs: [
          { label: { hu: "Textúra", en: "Texture" }, val: { hu: "Darabos prémium", en: "Chunky premium" }, isHighlight: true },
          { label: { hu: "Kiszerelések", en: "Packaging" }, val: { hu: "5, 10, 20, 200 kg", en: "5, 10, 20, 200 kg" } },
          { label: { hu: "Szavatosság", en: "Shelf Life" }, val: { hu: "12 hónap", en: "12 months" } }
        ],
        flavors: ["Prémium sárgabarack (darabos)", "Erdei áfonya (egész szemes)", "Erdei szamóca", "Meggydarabos", "Feketeribizli"],
        appsLabel: { hu: "Jellemző Felhasználás:", en: "Typical Applications:" },
        apps: {
          hu: ["Töltött croissant", "Dán pékáru", "Prémium tarte & torták", "Pohárdesszertek", "Látványpékségek"],
          en: ["Filled Croissants", "Danish Pastry", "Premium Tartes & Cakes", "Dessert Cups", "Bake-off Shops"]
        },
        imageWebp: "assets/jam-cookie.webp",
        imageJpg: "assets/jam-cookie.jpg",
        caption: {
          hu: "Prémium finompékáru • Intenzív gyümölcsdarabos textúra croissant-ban és dán pékáruban",
          en: "Artisan pastry • Intensely fruity texture in croissants and Danish pastries"
        }
      }
    };

    // ---------------------------------------------------------------------------
    // PRODUCT DATA REPOSITORY (FULL 6 ITEMS)
    // ---------------------------------------------------------------------------
    const products = [
      {
        id: "sutesallo-vegyes",
        category: "sutesallo",
        names: {
          hu: "SV Sütésálló Vegyes Gyümölcsíz",
          en: "SV Bake-Stable Mixed Fruit Preparation"
        },
        badge: { hu: "SÜTÉSÁLLÓ TÖMB • VEGÁN", en: "BAKE-STABLE BLOCK • VEGAN" },
        pack: { hu: "10 kg karton (480 kg/raklap)", en: "10 kg carton (480 kg/pallet)" },
        specs: {
          brix: "58–62° Brix",
          ph: "3.3 – 3.6",
          heat: "≥ 200 °C (15 perc)",
          shelfLife: { hu: "12 hónap", en: "12 months" },
          sliceability: { hu: "Kiváló, késálló gépi szeletelés", en: "Excellent, clean automated slicing" }
        },
        desc: {
          hu: "Hagyományos receptúrájú, természetes színezékkel készülő, tömbösített sütésálló gyümölcstöltelék. Kifejezetten ipari bukták, táskák és kelt tészták gépileg szeletelhető töltésére kifejlesztve.",
          en: "Traditional recipe thermo-stable fruit block made with natural colors. Engineered specifically for automated slicing and filling of commercial yeast buns, turnovers, and puff pastries."
        }
      },
      {
        id: "sutesallo-kajszi",
        category: "sutesallo",
        names: {
          hu: "SV Sütésálló Kajszibarack Ízű Készítmény",
          en: "SV Bake-Stable Apricot Preparation"
        },
        badge: { hu: "200°C HŐTŰRŐ • GÉLÁLLÓ", en: "200°C HEAT-STABLE • GEL" },
        pack: { hu: "10 kg kartondoboz", en: "10 kg carton box" },
        specs: {
          brix: "60–64° Brix",
          ph: "3.2 – 3.5",
          heat: "≥ 200 °C (Formamegtartó)",
          shelfLife: { hu: "12 hónap", en: "12 months" },
          sliceability: { hu: "Késálló, tiszta vágási él", en: "Firm gel, clean cut edge" }
        },
        desc: {
          hu: "Intenzív kajszibarack ízvilágú, aranysárga színű forma- és alaktartó gél. Leveles tészták, piték és finompékáruk magas hőfokú sütéséhez.",
          en: "Vibrant golden apricot flavor gel. Maintains sharp geometry and volume in high-temperature puff pastry, pies, and Danish pastries."
        }
      },
      {
        id: "kenheto-malna",
        category: "kenheto",
        names: {
          hu: "SV Málna Ízű Gyümölcskészítmény",
          en: "SV Raspberry Confectionery Preparation"
        },
        badge: { hu: "HIDEGEN KENHETŐ • VÖDRÖS", en: "COLD SPREADABLE • BUCKET" },
        pack: { hu: "5 kg műanyag vödör", en: "5 kg plastic bucket" },
        specs: {
          brix: "65° Brix",
          ph: "3.2 – 3.4",
          heat: { hu: "Hideg technológia", en: "Cold process" },
          shelfLife: { hu: "9 hónap", en: "9 months" },
          sliceability: { hu: "Selymes, homogén kenhetőség", en: "Smooth, velvety spreadability" }
        },
        desc: {
          hu: "Homogén állagú, hidegen könnyen kenhető málnás gyümölcskészítmény piskótatekercsek, linzer sütemények és tortalapok összetöltéséhez.",
          en: "Smooth, cold-spreadable raspberry preparation designed for sponge cake layering, linzer cookies, and premium confectionery fillings."
        }
      },
      {
        id: "kenheto-afonya",
        category: "kenheto",
        names: {
          hu: "SV Áfonya Ízű Gyümölcskészítmény",
          en: "SV Blueberry Confectionery Preparation"
        },
        badge: { hu: "PRÉMIUM AROMA • HIDEG STABIL", en: "PREMIUM AROMA • COLD STABLE" },
        pack: { hu: "5 kg műanyag vödör", en: "5 kg plastic bucket" },
        specs: {
          brix: "65° Brix",
          ph: "3.2 – 3.5",
          heat: { hu: "Hideg technológia", en: "Cold process" },
          shelfLife: { hu: "9 hónap", en: "9 months" },
          sliceability: { hu: "Kiváló tapadás és eloszlás", en: "Superior adhesion & spread" }
        },
        desc: {
          hu: "Mélybordó-kékes árnyalatú, gazdag erdei áfonya karakterű gyümölcsbetét prémium desszertekhez, fánkokhoz és cukrászati termékekhez.",
          en: "Deep purple-blue hue with rich wild blueberry profile. Designed for premium dessert inserts, donut injecting, and patisserie glazing."
        }
      },
      {
        id: "sutesallo-extra-meggy",
        category: "sutesallo",
        names: {
          hu: "SV Sütésálló Extra Meggy Töltelék",
          en: "SV Bake-Stable Extra Sour Cherry Filling"
        },
        badge: { hu: "DARABOS GYÜMÖLCS • SÜTÉSÁLLÓ", en: "FRUIT PIECES • BAKE-STABLE" },
        pack: { hu: "10 kg karton / 5 kg vödör", en: "10 kg carton / 5 kg bucket" },
        specs: {
          brix: "60–63° Brix",
          ph: "3.1 – 3.4",
          heat: "≥ 195 °C",
          shelfLife: { hu: "12 hónap", en: "12 months" },
          sliceability: { hu: "Formamegtartó, nem folyós", en: "Shape-retaining pieces, non-bleeding" }
        },
        desc: {
          hu: "Kellemesen fanyar, valódi fekete és cigánymeggy szemekkel készült prémium töltelék rétesekhez, pitékhez és dán pékárukhoz.",
          en: "Pleasantly tart, rich sour cherry filling with intact fruit pieces. Formulated for strudels, rustic pies, and Danish pastries."
        }
      },
      {
        id: "egyedi-receptura",
        category: "egyedi",
        names: {
          hu: "SV Egzotikus Mangó-Maracuja Töltelék",
          en: "SV Exotic Mango-Passionfruit Filling"
        },
        badge: { hu: "INNOVATÍV R&D • EGYEDI", en: "INNOVATIVE R&D • CUSTOM" },
        pack: { hu: "5 kg vödör / 200 kg tartály", en: "5 kg bucket / 200 kg drum" },
        specs: {
          brix: "60–65° Brix (állítható)",
          ph: "3.2 – 3.5",
          heat: "180 °C – 210 °C",
          shelfLife: { hu: "9–12 hónap", en: "9–12 months" },
          sliceability: { hu: "Injektálható vagy kenhető", en: "Injectable or spreadable" }
        },
        desc: {
          hu: "Trópusi hangulatú, intenzív sárga színű és friss gyümölcsös savgerincű készítmény. Croissant-ok, finompékáruk és prémium desszertek újító alapanyaga.",
          en: "Tropical flavor profile with vivid golden color and vibrant fruit acidity. Next-generation filling for croissants, artisan tarts, and patisserie items."
        }
      }
    ];

    let currentLang = 'hu';
    let currentCatalogTab = 'spreadable';
    let isCatalogFlipping = false;
    const catalogTabs = ['spreadable', 'bake-stable', 'extra-jam'];

    // ---------------------------------------------------------------------------
    // LANGUAGE SWITCHER ENGINE
    // ---------------------------------------------------------------------------
    function setLanguage(lang) {
      if (!translations[lang]) return;
      currentLang = lang;

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
      renderCatalogTab();
      renderProducts();

      // Re-init lucide icons
      lucide.createIcons();

      // Clear any active field errors on language switch so errors don't persist in previous language
      clearFormErrors();
    }

    // ---------------------------------------------------------------------------
    // KATALÓGUS TAB & 3D FLIP NAVIGATION HANDLER (PANTASTICO / HEYZINE INSPIRED)
    // ---------------------------------------------------------------------------
    function navigateCatalog(step) {
      if (isCatalogFlipping) return;
      const currentIndex = catalogTabs.indexOf(currentCatalogTab);
      let newIndex = currentIndex + step;
      if (newIndex < 0) newIndex = catalogTabs.length - 1;
      if (newIndex >= catalogTabs.length) newIndex = 0;
      switchCatalogTab(catalogTabs[newIndex], step);
    }

    function switchCatalogTab(tabKey, forcedDirection) {
      if (currentCatalogTab === tabKey && !forcedDirection) return;
      if (isCatalogFlipping) return;

      const oldIndex = catalogTabs.indexOf(currentCatalogTab);
      const newIndex = catalogTabs.indexOf(tabKey);
      const direction = forcedDirection !== undefined ? forcedDirection : (newIndex >= oldIndex ? 1 : -1);

      isCatalogFlipping = true;
      currentCatalogTab = tabKey;

      const card = document.getElementById('catalog-card');
      const shine = document.getElementById('catalog-flip-shine');

      // Update tab buttons while preserving i18n text
      catalogTabs.forEach(k => {
        const btn = document.getElementById(`tab-btn-${k}`);
        if (btn) {
          if (k === tabKey) {
            btn.className = "catalog-tab active px-3.5 py-2 rounded-lg font-bold transition-all text-xs whitespace-nowrap shadow-sm";
          } else {
            btn.className = "catalog-tab px-3.5 py-2 rounded-lg font-semibold transition-all text-stone-700 hover:text-[#91372d] text-xs whitespace-nowrap";
          }
        }
        const dot = document.getElementById(`cat-dot-${k}`);
        if (dot) {
          if (k === tabKey) {
            dot.className = "h-2 rounded-full transition-all duration-300 w-8 bg-[#a3392e]";
          } else {
            dot.className = "h-2 rounded-full transition-all duration-300 w-2.5 bg-stone-300 hover:bg-stone-400";
          }
        }
      });

      // Update counter
      const counterEl = document.getElementById('cat-current-num');
      if (counterEl) {
        const numStr = (newIndex + 1).toString().padStart(2, '0');
        counterEl.innerText = numStr;
      }

      if (card) {
        card.classList.remove('catalog-flip-next-out', 'catalog-flip-next-in', 'catalog-flip-prev-out', 'catalog-flip-prev-in');
        card.classList.add(direction > 0 ? 'catalog-flip-next-out' : 'catalog-flip-prev-out');

        if (shine) {
          shine.style.background = direction > 0 
            ? 'linear-gradient(90deg, rgba(0,0,0,0.18) 0%, transparent 45%, rgba(255,255,255,0.2) 65%, transparent 100%)'
            : 'linear-gradient(-90deg, rgba(0,0,0,0.18) 0%, transparent 45%, rgba(255,255,255,0.2) 65%, transparent 100%)';
          shine.style.opacity = '1';
        }

        setTimeout(() => {
          renderCatalogTab();
          card.classList.remove('catalog-flip-next-out', 'catalog-flip-prev-out');
          card.classList.add(direction > 0 ? 'catalog-flip-next-in' : 'catalog-flip-prev-in');
          if (shine) shine.style.opacity = '0';

          setTimeout(() => {
            card.classList.remove('catalog-flip-next-in', 'catalog-flip-prev-in');
            isCatalogFlipping = false;
            lucide.createIcons();
          }, 160);
        }, 140);
      } else {
        renderCatalogTab();
        isCatalogFlipping = false;
        lucide.createIcons();
      }
    }

    function renderCatalogTab() {
      const card = document.getElementById('catalog-card');
      if (!card) return;
      const data = catalogData[currentCatalogTab];
      if (!data) return;

      // Badges
      const catBadge = document.getElementById('cat-badge');
      if (catBadge) {
        catBadge.innerText = data.badge[currentLang] || data.badge.hu;
        catBadge.style.backgroundColor = data.badgeColor;
      }
      const imgBadge = document.getElementById('cat-badge-overlay');
      if (imgBadge) {
        imgBadge.innerText = data.imageBadge[currentLang] || data.imageBadge.hu;
        imgBadge.style.backgroundColor = data.imageBadgeBg;
      }

      // Titles & descriptions
      const titleEl = document.getElementById('cat-title');
      if (titleEl) titleEl.innerText = data.title[currentLang] || data.title.hu;
      const subEl = document.getElementById('cat-subtitle');
      if (subEl) subEl.innerText = data.subtitle[currentLang] || data.subtitle.hu;
      const descEl = document.getElementById('cat-desc');
      if (descEl) descEl.innerText = data.desc[currentLang] || data.desc.hu;

      // Image
      const imgSrc = document.getElementById('cat-img-source');
      if (imgSrc) imgSrc.srcset = data.imageWebp;
      const imgEl = document.getElementById('cat-image');
      if (imgEl) {
        imgEl.src = data.imageJpg;
        imgEl.alt = (data.title[currentLang] || data.title.hu) + " bemutató";
      }
      const captionEl = document.getElementById('cat-img-caption');
      if (captionEl) captionEl.innerText = data.caption[currentLang] || data.caption.hu;

      // Specifications Matrix (Standardized 5, 10, 20, 200 kg; No Brix, No pH)
      const specsContainer = document.getElementById('cat-specs');
      if (specsContainer) {
        specsContainer.innerHTML = data.specs.map(s => {
          const lbl = typeof s.label === 'object' ? (s.label[currentLang] || s.label.hu) : s.label;
          const val = typeof s.val === 'object' ? (s.val[currentLang] || s.val.hu) : s.val;
          const valClass = s.isHighlight ? "font-bold text-emerald-700 text-sm mt-0.5" : "font-bold text-stone-900 text-sm mt-0.5";
          return `
            <div>
              <div class="text-[10px] text-stone-500 uppercase tracking-wider">${lbl}</div>
              <div class="${valClass}">${val}</div>
            </div>
          `;
        }).join('');
      }

      // Flavors
      const flavorsContainer = document.getElementById('cat-flavors');
      if (flavorsContainer) {
        flavorsContainer.innerHTML = data.flavors.map(f => `
          <span class="px-2.5 py-1 rounded-md text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200 font-medium">${f}</span>
        `).join('');
      }

      // Apps
      const appsLabelEl = document.getElementById('cat-apps-label');
      if (appsLabelEl) appsLabelEl.innerText = data.appsLabel[currentLang] || data.appsLabel.hu;
      const appsContainer = document.getElementById('cat-apps');
      if (appsContainer) {
        const appList = data.apps[currentLang] || data.apps.hu;
        appsContainer.innerHTML = appList.map(a => `
          <span class="bg-emerald-50/70 border border-emerald-200/80 text-stone-700 px-2.5 py-1 rounded-md">${a}</span>
        `).join('');
      }
    }

    // Touch swipe and keyboard navigation for catalog
    (function initCatalogInteractions() {
      const cardContainer = document.querySelector('.catalog-viewport');
      if (cardContainer) {
        let startX = 0;
        let startY = 0;
        cardContainer.addEventListener('touchstart', e => {
          startX = e.changedTouches[0].screenX;
          startY = e.changedTouches[0].screenY;
        }, { passive: true });
        cardContainer.addEventListener('touchend', e => {
          const diffX = e.changedTouches[0].screenX - startX;
          const diffY = e.changedTouches[0].screenY - startY;
          if (Math.abs(diffX) > 40 && Math.abs(diffX) > Math.abs(diffY)) {
            if (diffX < 0) {
              navigateCatalog(1);
            } else {
              navigateCatalog(-1);
            }
          }
        }, { passive: true });
      }

      window.addEventListener('keydown', e => {
        const catSection = document.getElementById('termekek');
        if (!catSection) return;
        const rect = catSection.getBoundingClientRect();
        const inView = rect.top < window.innerHeight && rect.bottom > 0;
        if (inView) {
          if (e.key === 'ArrowRight') {
            navigateCatalog(1);
          } else if (e.key === 'ArrowLeft') {
            navigateCatalog(-1);
          }
        }
      });
    })();

    // ---------------------------------------------------------------------------
    // PRODUCT MATRIX RENDERER
    // ---------------------------------------------------------------------------
    function renderProducts() {
      const container = document.getElementById('product-list');
      if (!container) return;

      container.innerHTML = products.map((p, idx) => {
        const packVal = typeof p.pack === 'object' ? (p.pack[currentLang] || p.pack.hu) : p.pack;
        const heatVal = typeof p.specs.heat === 'object' ? (p.specs.heat[currentLang] || p.specs.heat.hu) : p.specs.heat;
        const tdsLabel = currentLang === 'en' ? 'TDS Sheet' : 'TDS Adatlap';
        const sampleLabel = currentLang === 'en' ? 'Inquire' : 'Ajánlatkérés';
        const heatTitle = currentLang === 'en' ? 'Heat resistance' : 'Hőtűrés';

        return `
        <div class="rounded-2xl border p-6 bg-white flex flex-col justify-between transition-all hover:shadow-md hover:border-[#91372d]/40" style="border-color: var(--sv-border);">
          <div class="space-y-3">
            
            <div class="flex items-center justify-between flex-wrap gap-1.5">
              <span class="text-[10px] font-mono-spec font-bold px-2 py-0.5 rounded border tracking-wider uppercase"
                    style="background-color: rgba(163, 57, 46, 0.05); color: var(--sv-burgundy); border-color: var(--sv-border);">
                ${p.badge[currentLang] || p.badge.hu}
              </span>
              <span class="text-[11px] font-mono-spec text-stone-500">${packVal}</span>
            </div>

            <h3 class="font-syne font-bold text-xl text-stone-900 mt-1 leading-snug">
              ${p.names[currentLang] || p.names.hu}
            </h3>

            <p class="text-xs text-stone-600 leading-relaxed">
              ${p.desc[currentLang] || p.desc.hu}
            </p>

            <div class="pt-2.5 border-t font-mono-spec text-xs space-y-1" style="border-color: var(--sv-border-light);">
              <div class="flex justify-between text-stone-700">
                <span class="text-stone-500">Brix:</span>
                <span class="font-bold">${p.specs.brix}</span>
              </div>
              <div class="flex justify-between text-stone-700">
                <span class="text-stone-500">pH:</span>
                <span class="font-bold">${p.specs.ph}</span>
              </div>
              <div class="flex justify-between text-stone-700">
                <span class="text-stone-500">${heatTitle}:</span>
                <span class="font-bold text-emerald-700">${heatVal}</span>
              </div>
            </div>

          </div>

          <div class="pt-4 mt-4 border-t flex items-center justify-between gap-3" style="border-color: var(--sv-border-light);">
            <button onclick="openTdsModal(${idx})" 
                    class="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-lg text-xs font-semibold font-mono-spec transition-all border hover:bg-stone-50"
                    style="border-color: var(--sv-burgundy); color: var(--sv-burgundy);">
              <i data-lucide="file-text" class="w-3.5 h-3.5 text-[#91372d]"></i>
              <span>${tdsLabel}</span>
            </button>

            <button onclick="selectProductAndScroll('${p.id}')" 
                    class="text-xs font-semibold font-mono-spec text-[#91372d] hover:underline flex items-center gap-1">
              <i data-lucide="send" class="w-3 h-3"></i>
              <span>${sampleLabel}</span>
            </button>
          </div>
        </div>
        `;
      }).join('');
    }

    // ---------------------------------------------------------------------------
    // TDS MODAL HANDLER (COMPLETELY LOCALIZED)
    // ---------------------------------------------------------------------------
    function openTdsModal(productIndex) {
      const p = products[productIndex];
      if (!p) return;

      const modal = document.getElementById('tds-modal');
      const content = document.getElementById('tds-modal-content');

      const packVal = typeof p.pack === 'object' ? (p.pack[currentLang] || p.pack.hu) : p.pack;
      const shelfVal = typeof p.specs.shelfLife === 'object' ? (p.specs.shelfLife[currentLang] || p.specs.shelfLife.hu) : p.specs.shelfLife;
      const heatVal = typeof p.specs.heat === 'object' ? (p.specs.heat[currentLang] || p.specs.heat.hu) : p.specs.heat;
      const sliceVal = typeof p.specs.sliceability === 'object' ? (p.specs.sliceability[currentLang] || p.specs.sliceability.hu) : p.specs.sliceability;

      const labels = {
        hu: {
          code: "Termékkód",
          pack: "Kiszerelés",
          labTitle: "LABORATÓRIUMI PARAMÉTEREK",
          brix: "Refraktometriás Brix:",
          ph: "pH Érték (20°C):",
          heat: "Hőtűrési küszöb:",
          shelf: "Szavatossági idő:",
          slice: "Szeletelhetőség & Viszkozitás:",
          microTitle: "MIKROBIOLÓGIA & ALLERGÉN STÁTUSZ",
          microBody: "Összcsíraszám: < 1000 CFU/g • Élesztő & Penész: < 100 CFU/g • Salmonella: Negatív/25g • Gluténmentes, Vegán formula, Természetes színezék.",
          pilotTitle: "Technológiai Finomhangolás:",
          pilotBody: "A fenti műszaki specifikáció kiindulási referencia. Egyedi gyártósorokhoz (hőfok, sütési idő, viszkozitás) móri laboratóriumunk díjmentesen elvégzi a szükséges paraméterezést.",
          cta: "Érdeklődés & Kapcsolatfelvétel",
          close: "Bezárás"
        },
        en: {
          code: "Product Code",
          pack: "Packaging",
          labTitle: "LABORATORY SPECIFICATIONS",
          brix: "Refractometric Brix:",
          ph: "pH Value (20°C):",
          heat: "Thermal Resistance:",
          shelf: "Shelf Life:",
          slice: "Sliceability & Viscosity:",
          microTitle: "MICROBIOLOGY & ALLERGEN STATUS",
          microBody: "Total Plate Count: < 1000 CFU/g • Yeast & Mold: < 100 CFU/g • Salmonella: Negative/25g • Gluten-free, Vegan, Natural coloring.",
          pilotTitle: "Technical Formulation Note:",
          pilotBody: "The above technical data serves as standard baseline. Our Mór laboratory provides formulation adjustments tailored to your specific processing lines.",
          cta: "Contact & Inquire",
          close: "Close"
        }
      }[currentLang] || labels.hu;

      content.innerHTML = `
        <div class="space-y-6">
          
          <div class="border-b pb-4">
            <div class="flex items-center gap-2 text-xs font-mono-spec text-[#91372d] font-semibold uppercase">
              <span>${currentLang === 'en' ? 'Sun Valley Zrt. • Mór Plant' : 'Sun Valley Zrt. • Móri Gyár'}</span>
              <span>•</span>
              <span>${currentLang === 'en' ? 'TECHNICAL DATA SHEET #TDS-2026' : 'MŰSZAKI ADATLAP #TDS-2026'}</span>
            </div>
            <h2 class="font-syne font-bold text-2xl text-stone-900 mt-1">
              ${p.names[currentLang] || p.names.hu}
            </h2>
            <p class="text-xs font-mono-spec text-stone-500 mt-0.5">
              ${labels.code}: SV-${p.id.toUpperCase()} • ${labels.pack}: ${packVal}
            </p>
          </div>

          <div class="space-y-4 font-mono-spec text-xs">
            <h4 class="font-bold text-stone-900 uppercase text-[11px] tracking-wider text-stone-400">
              ${labels.labTitle}
            </h4>

            <div class="grid grid-cols-2 gap-2 border rounded-xl p-3 bg-stone-50" style="border-color: var(--sv-border-light);">
              <div class="py-1 border-b border-stone-200">
                <span class="text-stone-500">${labels.brix}</span>
                <span class="font-bold text-stone-900 block mt-0.5">${p.specs.brix}</span>
              </div>
              <div class="py-1 border-b border-stone-200">
                <span class="text-stone-500">${labels.ph}</span>
                <span class="font-bold text-stone-900 block mt-0.5">${p.specs.ph}</span>
              </div>
              <div class="py-1 border-b border-stone-200">
                <span class="text-stone-500">${labels.heat}</span>
                <span class="font-bold text-emerald-700 block mt-0.5">${heatVal}</span>
              </div>
              <div class="py-1 border-b border-stone-200">
                <span class="text-stone-500">${labels.shelf}</span>
                <span class="font-bold text-stone-900 block mt-0.5">${shelfVal}</span>
              </div>
              <div class="py-1 col-span-2">
                <span class="text-stone-500">${labels.slice}</span>
                <span class="font-bold text-stone-900 block mt-0.5">${sliceVal}</span>
              </div>
            </div>

            <div class="space-y-1.5 pt-2">
              <h5 class="font-bold text-stone-900 uppercase text-[10px] tracking-wider text-stone-400">
                ${labels.microTitle}
              </h5>
              <p class="text-stone-600 text-xs">
                ${labels.microBody}
              </p>
            </div>

            <div class="p-3.5 rounded-xl border bg-amber-50/70 border-amber-200 text-stone-700 text-xs space-y-1">
              <div class="font-bold text-stone-900">${labels.pilotTitle}</div>
              <p class="text-[11px] leading-relaxed">
                ${labels.pilotBody}
              </p>
            </div>

          </div>

          <div class="pt-4 border-t flex flex-wrap items-center justify-between gap-3" style="border-color: var(--sv-border-light);">
            <button onclick="selectProductAndScroll('${p.id}')" 
               class="px-5 py-2.5 rounded-xl font-bold text-xs shadow text-white flex items-center gap-2"
               style="background-color: var(--sv-orange);">
              <i data-lucide="mail-check" class="w-4 h-4"></i>
              <span>${labels.cta}</span>
            </button>

            <button onclick="closeTdsModal()" class="px-4 py-2.5 rounded-xl border font-mono-spec text-xs text-stone-600 hover:bg-stone-50">
              ${labels.close}
            </button>
          </div>

        </div>
      `;

      modal.classList.remove('hidden');
      modal.classList.add('flex');
      lucide.createIcons();
    }

    function closeTdsModal() {
      const modal = document.getElementById('tds-modal');
      modal.classList.add('hidden');
      modal.classList.remove('flex');
    }

    // ---------------------------------------------------------------------------
    // HIGH CONVERSION FUNNEL: SELECT PRODUCT AND SCROLL TO CONTACT
    // ---------------------------------------------------------------------------
    function selectProductAndScroll(productId) {
      closeTdsModal();
      const contactElem = document.getElementById('kapcsolat');
      if (contactElem) {
        contactElem.scrollIntoView({ behavior: 'smooth' });
      }
    }

    // Close modal on escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeTdsModal();
    });

    // Close modal on background click
    document.getElementById('tds-modal')?.addEventListener('click', (e) => {
      if (e.target.id === 'tds-modal') closeTdsModal();
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

      let lastScrollY = window.pageYOffset || document.documentElement.scrollTop;
      let isTicking = false;

      function onScroll() {
        const currentScrollY = window.pageYOffset || document.documentElement.scrollTop;
        const isMobileOpen = mobileMenu && !mobileMenu.classList.contains('hidden');

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

        const delta = currentScrollY - lastScrollY;

        // Ignore micro-scroll movements (less than 6px) to avoid jitter
        if (Math.abs(delta) < 6) {
          isTicking = false;
          return;
        }

        if (delta > 0 && currentScrollY > 80) {
          // Scrolling down: tuck header away
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
    }

    // Mobile Menu Toggle
    function toggleMobileMenu() {
      const menu = document.getElementById('mobile-menu');
      const siteHeader = document.getElementById('site-header');
      if (!menu) return;
      const isOpening = menu.classList.contains('hidden');
      menu.classList.toggle('hidden');
      if (isOpening && siteHeader) {
        siteHeader.style.transform = 'translateY(0)';
      }
    }

    function clearFormErrors() {
      // Streamlined contact model: form errors no-op
    }

    // Initial boot
    document.addEventListener('DOMContentLoaded', () => {
      initDynamicHeader();
      renderCatalogTab();
      renderProducts();
      lucide.createIcons();
    });
  </script>
</body>
</html>
"""

def main():
    content = generate_html()
    with open(ROOT_INDEX, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {ROOT_INDEX} ({len(content)} characters)")

if __name__ == "__main__":
    main()
