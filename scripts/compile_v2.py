import os
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ROOT_INDEX = REPO_ROOT / "index.html"
OUTPUT_V2 = REPO_ROOT / "prototypes" / "sun-valley-b2b" / "index_v2.html"
OUTPUT_INDEX = REPO_ROOT / "prototypes" / "sun-valley-b2b" / "index.html"

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

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- Google Fonts: Plus Jakarta Sans & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
    :root {
      /* Sun Valley Official Palette (from szinek.md & CONTEXT.md) */
      --sv-burgundy: #5F2125;
      --sv-burgundy-dark: #451C1B;
      --sv-orange: #E36527;
      --sv-gold: #D48054;
      --sv-gold-light: #FBBB9C;
      --sv-green-dark: #2D3628;
      --sv-green-light: #5F6E4D;
      --sv-apple-red: #923833;
      --sv-soil-brown: #63412C;
      --sv-paper-cream: #F5F2EE;
      --sv-sand-watermark: #D0AE9F;
      --sv-surface: #FFFFFF;
      --sv-text-main: #181513;
      --sv-text-muted: #57524E;
      --sv-border: rgba(95, 33, 37, 0.16);
      --sv-border-light: rgba(95, 33, 37, 0.08);
    }

    *, *::before, *::after {
      box-sizing: border-box;
    }

    html, body {
      overflow-x: hidden;
      max-width: 100vw;
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--sv-paper-cream);
      color: var(--sv-text-main);
      overflow-x: hidden;
    }

    .font-syne {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      font-feature-settings: "lnum" 1, "tnum" 0;
      letter-spacing: -0.02em;
    }

    .font-mono-spec {
      font-family: 'JetBrains Mono', monospace;
    }

    /* Subtle industrial graph grid pattern */
    .bg-tech-grid {
      background-size: 40px 40px;
      background-image: 
        linear-gradient(to right, rgba(95, 33, 37, 0.035) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(95, 33, 37, 0.035) 1px, transparent 1px);
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

    @keyframes pulse-ring {
      0% { box-shadow: 0 0 0 0 rgba(227, 101, 39, 0.6); }
      70% { box-shadow: 0 0 0 12px rgba(227, 101, 39, 0); }
      100% { box-shadow: 0 0 0 0 rgba(227, 101, 39, 0); }
    }
    .focus-pulse {
      animation: pulse-ring 1.5s cubic-bezier(0.24, 0, 0.38, 1) 2;
    }
  </style>
</head>
<body id="top" class="bg-tech-grid min-h-screen flex flex-col antialiased selection:bg-[#E36527] selection:text-white">

  <!-- ========================================================================= -->
  <!-- TOP EMERGENCY / DIRECT CONTACT BAR                                       -->
  <!-- ========================================================================= -->
  <div class="border-b text-xs font-mono-spec py-1.5 px-3.5 sm:px-8 transition-colors overflow-hidden"
       style="background-color: var(--sv-burgundy-dark); color: #F5F2EE; border-color: rgba(255,255,255,0.1);">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-2">
      <div class="flex items-center gap-2 sm:gap-3 truncate">
        <span class="inline-flex items-center gap-1.5 text-[#E36527] font-semibold uppercase tracking-wider text-[11px] sm:text-xs shrink-0">
          <span class="w-2 h-2 rounded-full bg-[#E36527] animate-pulse"></span>
          <span data-i18n="topbar_scale">Mór (Major u. 3.)</span>
        </span>
        <span class="hidden md:inline text-white/40">|</span>
        <span class="hidden md:inline text-white/80" data-i18n="topbar_capacity">Éves árbevétel: 1,1–1,3 Mrd Ft</span>
        <span class="hidden sm:inline text-white/40">|</span>
        <span class="hidden sm:inline text-[#FBBB9C]" data-i18n="topbar_rating">AA+ Minősítés</span>
      </div>
      <div class="flex items-center gap-3 sm:gap-4 text-[11px] sm:text-xs shrink-0">
        <a href="tel:+36308998548" class="hover:text-[#FBBB9C] transition-colors flex items-center gap-1.5 font-semibold">
          <i data-lucide="phone" class="w-3.5 h-3.5 text-[#E36527]"></i>
          <span>+36 30 899 8548</span>
        </a>
        <span class="hidden lg:inline text-white/40">|</span>
        <a href="mailto:vecsei.andras@sunvalley.hu" class="hidden lg:flex hover:text-[#FBBB9C] transition-colors items-center gap-1.5">
          <i data-lucide="mail" class="w-3.5 h-3.5 text-[#E36527]"></i>
          <span>vecsei.andras@sunvalley.hu</span>
        </a>
      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- MAIN NAVIGATION HEADER                                                    -->
  <!-- ========================================================================= -->
  <header class="sticky top-0 z-40 backdrop-blur-md border-b transition-colors duration-300"
          style="background-color: rgba(245, 242, 238, 0.96); border-color: var(--sv-border);">
    <div class="max-w-7xl mx-auto px-3.5 sm:px-8 py-3 sm:py-3.5 flex items-center justify-between gap-2 sm:gap-4">
      
      <!-- Brand Crest & Identity (Authentic Sun Valley Logo) -->
      <a href="#top" class="flex items-center gap-2 sm:gap-3 group shrink-0">
        <img src="assets/sun-valley-logo.png" alt="Sun Valley Zrt. Logo" class="h-8 sm:h-11 w-auto object-contain transition-transform group-hover:scale-105">
        <div>
          <div class="font-syne font-extrabold text-sm sm:text-base md:text-lg tracking-tight leading-none" style="color: var(--sv-burgundy);">
            SUN VALLEY ZRT.
          </div>
          <p class="text-[10px] font-mono-spec tracking-wider uppercase hidden md:block mt-0.5" style="color: var(--sv-text-muted);" data-i18n="tagline">
            Ipari Gyümölcstechnológia • Alapítva 2009
          </p>
        </div>
      </a>

      <!-- Desktop Nav Links (Streamlined 4 Essential Links) -->
      <nav class="hidden lg:flex items-center gap-5 xl:gap-8 text-xs xl:text-sm font-semibold">
        <a href="#termekek" class="hover:text-[#E36527] transition-colors py-1 relative group" data-i18n="nav_products">
          Termékek & TDS
          <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#E36527] transition-all group-hover:w-full"></span>
        </a>
        <a href="#technologia" class="hover:text-[#E36527] transition-colors py-1 relative group" data-i18n="nav_tech">
          Sütésállóság (200°C)
          <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#E36527] transition-all group-hover:w-full"></span>
        </a>
        <a href="#egyedi-fejlesztes" class="hover:text-[#E36527] transition-colors py-1 relative group" data-i18n="nav_rd">
          Receptúra & Minták
          <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#E36527] transition-all group-hover:w-full"></span>
        </a>
        <a href="#kapcsolat" class="hover:text-[#E36527] transition-colors py-1 relative group" data-i18n="nav_contact">
          Kapcsolat
          <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#E36527] transition-all group-hover:w-full"></span>
        </a>
      </nav>

      <!-- Right Controls: Language Switcher & Direct Call CTA -->
      <div class="flex items-center gap-1.5 sm:gap-3 shrink-0">
        
        <!-- TRILINGUAL SWITCHER (HU / EN / DE) -->
        <div class="flex items-center p-0.5 rounded-lg border font-mono-spec shrink-0"
             style="background-color: var(--sv-surface); border-color: var(--sv-border);">
          <button onclick="setLanguage('hu')" id="lang-hu" class="px-1.5 py-0.5 sm:px-2 sm:py-1 rounded font-bold transition-all bg-[#5F2125] text-white shadow-sm text-[10px] sm:text-xs">
            HU
          </button>
          <button onclick="setLanguage('en')" id="lang-en" class="px-1.5 py-0.5 sm:px-2 sm:py-1 rounded font-medium text-stone-600 hover:text-[#E36527] transition-all text-[10px] sm:text-xs">
            EN
          </button>
          <button onclick="setLanguage('de')" id="lang-de" class="px-1.5 py-0.5 sm:px-2 sm:py-1 rounded font-medium text-stone-600 hover:text-[#E36527] transition-all text-[10px] sm:text-xs">
            DE
          </button>
        </div>

        <!-- Direct Sample Request Button -->
        <a href="#mintakeres" 
           class="hidden sm:inline-flex items-center gap-2 px-3.5 xl:px-4 py-2 rounded-lg font-semibold text-xs transition-all transform active:scale-95 shadow-sm shrink-0"
           style="background-color: var(--sv-orange); color: white;">
          <i data-lucide="package-check" class="w-3.5 h-3.5"></i>
          <span data-i18n="btn_sample_short">Próbagyártási Minta</span>
        </a>

        <!-- Mobile Menu Toggle -->
        <button onclick="toggleMobileMenu()" class="lg:hidden p-1.5 rounded-lg border shrink-0" style="border-color: var(--sv-border);" aria-label="Navigációs menü">
          <i data-lucide="menu" class="w-5 h-5 text-stone-800"></i>
        </button>
      </div>

    </div>

    <!-- Mobile Drawer -->
    <div id="mobile-menu" class="hidden lg:hidden border-t px-6 py-5 space-y-4" style="background-color: var(--sv-paper-cream); border-color: var(--sv-border);">
      <div class="flex flex-col space-y-3 font-semibold text-sm">
        <a href="#katalogus" onclick="toggleMobileMenu()" class="py-1 text-stone-800 hover:text-[#E36527]" data-i18n="nav_catalog">Gasztro-Katalógus</a>
        <a href="#termekek" onclick="toggleMobileMenu()" class="py-1 text-stone-800 hover:text-[#E36527]" data-i18n="nav_products">Termékek & TDS</a>
        <a href="#technologia" onclick="toggleMobileMenu()" class="py-1 text-stone-800 hover:text-[#E36527]" data-i18n="nav_tech">Sütésállóság (200°C)</a>
        <a href="#egyedi-fejlesztes" onclick="toggleMobileMenu()" class="py-1 text-stone-800 hover:text-[#E36527]" data-i18n="nav_rd">Receptúra & Minták</a>
        <a href="#prospektus" onclick="toggleMobileMenu()" class="py-1 text-stone-800 hover:text-[#E36527]" data-i18n="nav_prospectus">Prospektus</a>
        <a href="#disztribucio" onclick="toggleMobileMenu()" class="py-1 text-stone-800 hover:text-[#E36527]" data-i18n="nav_distribution">Nagykereskedelmi Hálózat</a>
        <a href="#kapcsolat" onclick="toggleMobileMenu()" class="py-1 text-stone-800 hover:text-[#E36527]" data-i18n="nav_contact">Kapcsolat & Gyártóüzem</a>
      </div>
      <div class="pt-3 border-t flex flex-col gap-2" style="border-color: var(--sv-border);">
        <a href="#mintakeres" onclick="toggleMobileMenu()" class="flex items-center justify-center gap-2 py-2.5 rounded-lg text-white font-semibold text-sm" style="background-color: var(--sv-orange);">
          <i data-lucide="package-check" class="w-4 h-4"></i>
          <span data-i18n="btn_sample_short">Próbagyártási Minta Kérése</span>
        </a>
        <a href="tel:+36308998548" class="flex items-center justify-center gap-2 py-2.5 rounded-lg text-white font-semibold text-sm" style="background-color: var(--sv-burgundy);">
          <i data-lucide="phone" class="w-4 h-4"></i>
          <span>+36 30 899 8548</span>
        </a>
      </div>
    </div>
  </header>

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
               style="background-color: rgba(95, 33, 37, 0.06); border-color: var(--sv-border); color: var(--sv-burgundy);">
            <span class="w-1.5 h-1.5 rounded-full" style="background-color: var(--sv-orange);"></span>
            <span data-i18n="hero_badge">B2B Kenyérgyári & Finompékáru Alapanyagok</span>
          </div>

          <!-- Headline -->
          <h1 class="font-syne font-extrabold text-xl xs:text-2xl sm:text-4xl md:text-4xl lg:text-[2.2rem] xl:text-[2.85rem] tracking-tight leading-[1.22] pb-1 break-words"
              style="color: var(--sv-burgundy);">
            <span data-i18n="hero_h1_p1">200 °C felett sem forr ki.</span><br>
            <span class="font-normal italic" style="color: var(--sv-orange);" data-i18n="hero_h1_p2">Ipari sütésálló</span> 
            <span data-i18n="hero_h1_p3">gyümölcstöltelékek közvetlenül a gyártótól.</span>
          </h1>

          <!-- Body Description -->
          <p class="text-base sm:text-lg leading-relaxed max-w-2xl" style="color: var(--sv-text-muted);" data-i18n="hero_desc">
            A Sun Valley Zrt. a magyar finompékáru-üzemek és ipari kenyérgyárak megbízható belföldi beszállítója. 
            Forma- és alaktartó, gépileg szeletelhető tésztabetétek 10 kg-os kartonos és 5 kg-os vödrös kiszerelésben, közvetlen móri gyártóbázisról.
          </p>

          <!-- Action Buttons -->
          <div class="pt-2 flex flex-col sm:flex-row flex-wrap items-stretch sm:items-center gap-3 sm:gap-4">
            <a href="#katalogus" 
               class="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-5 sm:px-6 py-3.5 rounded-lg font-semibold text-sm shadow-md hover:shadow-lg transition-all transform active:scale-95 text-center"
               style="background-color: var(--sv-burgundy); color: #F5F2EE;">
              <i data-lucide="book-open" class="w-4 h-4 text-[#E36527]"></i>
              <span data-i18n="hero_cta_catalog">Lapozható Gasztro-Katalógus</span>
            </a>

            <a href="#mintakeres" 
               class="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-5 sm:px-6 py-3.5 rounded-lg font-semibold text-sm transition-all transform active:scale-95 shadow text-center"
               style="background-color: var(--sv-orange); color: white;">
              <i data-lucide="package-check" class="w-4 h-4"></i>
              <span data-i18n="hero_cta_sample">Üzemi Tesztminta Kérése</span>
            </a>

            <a href="assets/Sun_Valley_B2B_Prospektus_V1_4.pptx" download="Sun_Valley_B2B_Prospektus_V1_4.pptx"
               class="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-4 py-3.5 rounded-lg font-semibold text-xs font-mono-spec border transition-all hover:bg-white text-center"
               style="border-color: var(--sv-border); color: var(--sv-burgundy); background-color: var(--sv-surface);">
              <i data-lucide="download" class="w-3.5 h-3.5 text-[#E36527]"></i>
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
              <img src="assets/apricot.jpg" alt="Sun Valley sütésálló kajszibarack gyümölcstöltelék" 
                   class="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-500">
              <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent"></div>
              
              <!-- Floating QC Badge -->
              <div class="absolute top-4 left-4 inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-[11px] font-mono-spec font-bold tracking-wider uppercase text-white shadow-sm"
                   style="background-color: var(--sv-burgundy); border: 1px solid var(--sv-gold);">
                <i data-lucide="shield-check" class="w-3.5 h-3.5 text-[#E36527]"></i>
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
                  <i data-lucide="file-spreadsheet" class="w-3.5 h-3.5 text-[#E36527]"></i>
                  <span data-i18n="btn_view_full_tds">Részletes TDS Műszaki Adatlap</span>
                </button>
              </div>

              <div class="pt-1 flex items-center justify-between text-[10px] font-mono-spec text-stone-400">
                <span data-i18n="hero_qc_badge">MÓRI GYÁRI MINŐSÉG-ELLENŐRZÉS #SV-2026</span>
                <span data-i18n="hero_direct_badge" class="text-[#E36527] font-semibold">KÖZVETLEN GYÁRI SZÁLLÍTÁS</span>
              </div>
            </div>

          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- TRUST & CORPORATE STABILITY RIBBON                                        -->
  <!-- ========================================================================= -->
  <section class="border-b py-8 transition-colors" style="background-color: var(--sv-green-dark); color: #F5F2EE; border-color: var(--sv-border);">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center md:text-left">
        
        <!-- Stat 1 -->
        <div class="space-y-1">
          <div class="font-syne font-extrabold text-base sm:text-2xl md:text-3xl text-[#FBBB9C]" data-i18n="stat_revenue_val">1,1 – 1,3 Mrd Ft</div>
          <p class="text-[11px] sm:text-xs text-white/80 font-mono-spec" data-i18n="stat_revenue">Éves árbevétel (Stabil tőkeerő)</p>
        </div>

        <!-- Stat 2 -->
        <div class="space-y-1 md:border-l md:pl-6 border-white/10">
          <div class="font-syne font-extrabold text-base sm:text-2xl md:text-3xl text-white">AA+</div>
          <p class="text-[11px] sm:text-xs text-white/80 font-mono-spec" data-i18n="stat_rating">Pénzügyi minősítés (Adósságmentes)</p>
        </div>

        <!-- Stat 3 -->
        <div class="space-y-1 md:border-l md:pl-6 border-white/10">
          <div class="font-syne font-extrabold text-base sm:text-2xl md:text-3xl text-[#E36527]" data-i18n="stat_heritage_val">15+ Év</div>
          <p class="text-[11px] sm:text-xs text-white/80 font-mono-spec" data-i18n="stat_heritage">Gyümölcsfeldolgozói múlt (Vitamór bázis)</p>
        </div>

        <!-- Stat 4 -->
        <div class="space-y-1 md:border-l md:pl-6 border-white/10">
          <div class="font-syne font-extrabold text-base sm:text-2xl md:text-3xl text-white" data-i18n="stat_energy_val">VEP Díjas</div>
          <p class="text-[11px] sm:text-xs text-white/80 font-mono-spec" data-i18n="stat_energy">Energiatudatos Móri Gyártelep</p>
        </div>

      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- INTERACTIVE GASZTRO-KATALÓGUS (LAPOZHATÓ TERMÉKKATALÓGUS)                 -->
  <!-- ========================================================================= -->
  <section id="katalogus" class="py-16 md:py-20 border-b" style="border-color: var(--sv-border); background-color: var(--sv-paper-cream);">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      
      <!-- Section Header -->
      <div class="flex flex-col lg:flex-row lg:items-end justify-between gap-6 mb-10">
        <div class="max-w-2xl">
          <div class="font-mono-spec text-xs uppercase tracking-widest text-[#E36527] font-semibold mb-2" data-i18n="cat_section_tag">
            Lapozható Gasztronómiai Katalógus
          </div>
          <h2 class="font-syne font-bold text-3xl sm:text-4xl text-stone-900 leading-snug" data-i18n="cat_section_title">
            Gyümölcstöltelékek Felhasználás Szerint
          </h2>
          <p class="text-stone-600 mt-2 text-sm sm:text-base leading-relaxed" data-i18n="cat_section_desc">
            Válasszon technológiai kategóriát: lapozzon a sütésálló tömbök, a hidegen kenhető készítmények és az extra dzsemek között.
          </p>
        </div>

        <!-- Catalog Tab Switcher Buttons (Fully localized with data-i18n) -->
        <div class="flex flex-wrap items-center gap-1.5 sm:gap-2 p-1.5 rounded-xl border bg-white font-mono-spec text-xs max-w-full shadow-sm"
             style="border-color: var(--sv-border);">
          <button onclick="switchCatalogTab('bake-stable')" id="tab-btn-bake-stable" data-i18n="cat_tab_bake_stable"
                  class="catalog-tab active px-3 py-2 rounded-lg font-semibold transition-all text-xs whitespace-nowrap">
            1. Sütésálló Töltelékek
          </button>
          <button onclick="switchCatalogTab('spreadable')" id="tab-btn-spreadable" data-i18n="cat_tab_spreadable"
                  class="catalog-tab px-3 py-2 rounded-lg font-semibold transition-all text-stone-700 hover:text-[#E36527] text-xs whitespace-nowrap">
            2. Kenhető Készítmények
          </button>
          <button onclick="switchCatalogTab('extra-jam')" id="tab-btn-extra-jam" data-i18n="cat_tab_extra_jam"
                  class="catalog-tab px-3 py-2 rounded-lg font-semibold transition-all text-stone-700 hover:text-[#E36527] text-xs whitespace-nowrap">
            3. Extra Dzsemek
          </button>
        </div>
      </div>

      <!-- Catalog Active Display Box -->
      <div class="rounded-3xl border bg-white p-6 sm:p-10 shadow-lg transition-all" style="border-color: var(--sv-border);" id="catalog-card">
        
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center">
          
          <!-- Left Content (Span 6) -->
          <div class="lg:col-span-6 space-y-6">
            
            <div class="space-y-2">
              <span id="cat-badge" class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-[11px] font-mono-spec font-bold uppercase tracking-wider text-white"
                    style="background-color: var(--sv-burgundy);">
                10 KG KARTON • SÜTÉSÁLLÓ TÖMB
              </span>
              <h3 id="cat-title" class="font-syne font-bold text-2xl sm:text-3xl text-stone-900 leading-tight">
                Sütésálló Gyümölcstöltelékek
              </h3>
              <p id="cat-subtitle" class="text-sm text-[#E36527] font-semibold font-mono-spec">
                200 °C felett alaktartó, gépileg szeletelhető tésztabetétek
              </p>
            </div>

            <p id="cat-desc" class="text-stone-600 text-sm sm:text-base leading-relaxed">
              Speciális pektinhálójuk révén a tészta 200 °C feletti sütése során sem forrnak ki, nem áztatják el a tésztát, és hűlés után is megőrzik rugalmas gélállagukat. Kiválóan alkalmasak ipari automatizált töltő- és szeletelősorokra.
            </p>

            <!-- Application Pills -->
            <div>
              <div class="text-xs font-mono-spec uppercase tracking-wider text-stone-400 font-semibold mb-2.5" data-i18n="cat_apps_label">
                Jellemző Pékipari Alkalmazások:
              </div>
              <div id="cat-apps" class="flex flex-wrap gap-2">
                <!-- Dynamically injected with language support -->
              </div>
            </div>

            <!-- Key specs summary -->
            <div id="cat-specs" class="grid grid-cols-3 gap-3 p-4 rounded-xl border bg-stone-50 font-mono-spec text-xs" style="border-color: var(--sv-border-light);">
              <!-- Dynamically injected -->
            </div>

            <!-- Action buttons: Integrated Preselection Funnel -->
            <div class="flex flex-wrap items-center gap-3 pt-2">
              <button id="cat-tds-btn" onclick="openTdsModal(0)" 
                      class="inline-flex items-center gap-2 px-5 py-2.5 rounded-lg text-xs font-semibold font-mono-spec transition-all shadow"
                      style="background-color: var(--sv-burgundy); color: white;">
                <i data-lucide="file-spreadsheet" class="w-3.5 h-3.5 text-[#E36527]"></i>
                <span data-i18n="btn_view_category_tds">TDS Adatlap Megtekintése</span>
              </button>

              <button id="cat-sample-btn" onclick="selectProductAndScroll('sutesallo-vegyes')" 
                      class="inline-flex items-center gap-2 px-5 py-2.5 rounded-lg text-xs font-semibold font-mono-spec transition-all border hover:bg-stone-50"
                      style="border-color: var(--sv-orange); color: var(--sv-orange);">
                <i data-lucide="package-check" class="w-3.5 h-3.5"></i>
                <span data-i18n="btn_request_cat_sample">Minta Kérése Ebből a Kategóriából</span>
              </button>
            </div>

          </div>

          <!-- Right Image Showcase (Span 6) -->
          <div class="lg:col-span-6">
            <div class="relative rounded-2xl overflow-hidden border shadow-md bg-stone-100" style="border-color: var(--sv-border-light);">
              <img id="cat-image" src="assets/lekvaros-bukta.jpg" alt="Sütésálló gyümölcstöltelék gasztronómiai bemutató" 
                   loading="lazy" decoding="async"
                   class="w-full h-80 sm:h-96 object-cover object-center transition-all duration-500">
            </div>
          </div>

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
          <div class="font-mono-spec text-xs uppercase tracking-widest text-[#E36527] font-semibold" data-i18n="flavors_tag">
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
              <i data-lucide="arrow-right" class="w-4 h-4 text-[#E36527]"></i>
              <span data-i18n="flavors_cta">Részletes műszaki paraméterek megtekintése a termékmátrixban</span>
            </a>
          </div>
        </div>

      </div>

      <!-- Sub-section 2: Exotic Fruits & Innovation -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center border-t pt-16" style="border-color: var(--sv-border-light);">
        
        <!-- Left Content (Span 7) -->
        <div class="lg:col-span-7 space-y-6">
          <div class="font-mono-spec text-xs uppercase tracking-widest text-[#E36527] font-semibold" data-i18n="exotic_tag">
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
              <i data-lucide="sparkles" class="w-3.5 h-3.5 text-[#E36527]"></i>
              <span data-i18n="exotic_mango">Mangó & Maracuja</span>
            </div>
            <div class="p-3 rounded-xl border bg-amber-50/50 border-amber-200 text-stone-800 font-semibold flex items-center gap-2">
              <i data-lucide="sparkles" class="w-3.5 h-3.5 text-[#E36527]"></i>
              <span data-i18n="exotic_pineapple">Ananász & Kivi</span>
            </div>
            <div class="p-3 rounded-xl border bg-amber-50/50 border-amber-200 text-stone-800 font-semibold flex items-center gap-2 col-span-2 sm:col-span-1">
              <i data-lucide="sparkles" class="w-3.5 h-3.5 text-[#E36527]"></i>
              <span data-i18n="exotic_citrus">Citrus & Narancs</span>
            </div>
          </div>

          <p class="text-xs text-stone-500 font-mono-spec" data-i18n="exotic_note">
            * Az egzotikus receptúrákat ipari próbagyártás és technológiai egyeztetés alapján véglegesítjük a partner saját gépsoraira.
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
  <section id="technologia" class="py-16 md:py-24 border-b" style="background-color: rgba(95, 33, 37, 0.02); border-color: var(--sv-border);">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      
      <!-- Section Title -->
      <div class="max-w-3xl mb-12">
        <div class="font-mono-spec text-xs uppercase tracking-widest text-[#E36527] font-semibold mb-2" data-i18n="tech_section_tag">
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
              <img src="assets/lekvaros-bukta.jpg" alt="Sütésállósági teszt péksütemény" 
                   loading="lazy" decoding="async" class="w-full h-full object-cover">
              <div class="absolute top-3 left-3 bg-[#5F2125] text-white text-[10px] font-mono-spec font-bold px-2 py-0.5 rounded">
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
              <img src="assets/retes.jpg" alt="Fagyasztásálló gyümölcstöltelék" 
                   loading="lazy" decoding="async" class="w-full h-full object-cover">
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
              <img src="assets/jam.jpg" alt="Gépi pumpálható töltelék adagolás" 
                   loading="lazy" decoding="async" class="w-full h-full object-cover">
              <div class="absolute top-3 left-3 bg-[#E36527] text-white text-[10px] font-mono-spec font-bold px-2 py-0.5 rounded" data-i18n="tech_badge_dosing">
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
              <img src="assets/jam-cookie.jpg" alt="Ipari kiszerelések vödörtől kartontömbökig" 
                   loading="lazy" decoding="async" class="w-full h-full object-cover">
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
        <div class="font-mono-spec text-xs uppercase tracking-widest text-[#E36527] font-semibold mb-2" data-i18n="rd_section_tag">
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
               style="background-color: var(--sv-orange);">
            02
          </div>
          <h3 class="font-syne font-bold text-xl text-stone-900 leading-snug pb-0.5" data-i18n="rd_step2_title">
            Receptúra & Üzemi Próba
          </h3>
          <p class="text-xs sm:text-sm text-stone-600 leading-relaxed" data-i18n="rd_step2_desc">
            Laboratóriumi minta készítése, majd 5–10 kg-os üzemi próbagyártási minta kiküldése a partner saját gyártósorán történő sütési validációra.
          </p>
          <div class="pt-2 font-mono-spec text-[11px] text-stone-400 border-t" style="border-color: var(--sv-border-light);" data-i18n="rd_tag_2">
            Tesztminta & Visszacsatolás
          </div>
        </div>

        <!-- Step 3 -->
        <div class="rounded-2xl border bg-white p-6 sm:p-8 space-y-4 shadow-sm" style="border-color: var(--sv-border);">
          <div class="w-12 h-12 rounded-xl flex items-center justify-center font-mono-spec font-bold text-lg text-white"
               style="background-color: var(--sv-green-dark);">
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
  <!-- PRODUCT MATRIX & TECHNICAL DATA SHEETS (TDS) SECTION                      -->
  <!-- ========================================================================= -->
  <section id="termekek" class="py-16 md:py-24 border-b" style="border-color: var(--sv-border); background-color: var(--sv-surface);">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      
      <!-- Section Header -->
      <div class="max-w-3xl mb-12">
        <div class="font-mono-spec text-xs uppercase tracking-widest text-[#E36527] font-semibold mb-2" data-i18n="prod_section_tag">
          Termékportfólió & Minőségi Specifikációk
        </div>
        <h2 class="font-syne font-bold text-3xl sm:text-4xl text-stone-900 leading-snug pb-1" data-i18n="prod_section_title">
          Ipari Sütésálló & Kenhető Gyümölcskészítmények
        </h2>
        <p class="text-stone-600 mt-3 text-sm sm:text-base leading-relaxed" data-i18n="prod_section_desc">
          Minden termékünk standardizált laboratóriumi paraméterekkel, szigorú mikrobiológiai ellenőrzés mellett készül. 
          Kattintson a TDS adatlapokra a részletes mérnöki specifikációkért (Brix, pH, allergének).
        </p>
      </div>

      <!-- Products Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id="product-list">
        <!-- Injected via JavaScript with full i18n & funneled sample request button -->
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
            <i data-lucide="file-presentation" class="w-3.5 h-3.5 text-[#E36527]"></i>
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
        <div class="font-mono-spec text-xs uppercase tracking-widest text-[#E36527] font-semibold mb-2" data-i18n="dist_section_tag">
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
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-mono-spec font-semibold text-[#5F2125] bg-[#5F2125]/10">
              <i data-lucide="truck" class="w-3.5 h-3.5 text-[#E36527]"></i>
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
              <i data-lucide="arrow-right-circle" class="w-4 h-4 text-[#E36527]"></i>
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
  <!-- B2B SAMPLE REQUEST & QUALIFIED INQUIRY FORM                               -->
  <!-- ========================================================================= -->
  <section id="mintakeres" class="py-16 md:py-24 border-b" style="border-color: var(--sv-border); background-color: var(--sv-surface);">
    <div class="max-w-4xl mx-auto px-4 sm:px-8">
      
      <div class="text-center max-w-2xl mx-auto mb-10">
        <div class="font-mono-spec text-xs uppercase tracking-widest text-[#E36527] font-semibold mb-2" data-i18n="form_section_tag">
          Üzemi Próbagyártási Minta
        </div>
        <h2 class="font-syne font-bold text-3xl sm:text-4xl text-stone-900 leading-tight" data-i18n="form_section_title">
          Kérjen Tesztmintát Saját Gyártósorára
        </h2>
        <p class="text-stone-600 mt-2 text-sm sm:text-base leading-relaxed" data-i18n="form_section_desc">
          Töltse ki az alábbi űrlapot, és szakmai csapatunk eljuttatja üzemébe a kívánt 5–10 kg-os tesztmintát próbasütéshez.
        </p>
      </div>

      <!-- Qualified Form Container with complete accessibility and field names -->
      <form id="sample-request-form" onsubmit="handleSampleSubmit(event)" class="rounded-3xl border p-6 sm:p-10 shadow-lg space-y-6 transition-all"
            style="background-color: var(--sv-paper-cream); border-color: var(--sv-border);">
        
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
          
          <div>
            <label for="sample-name" class="block text-xs font-mono-spec font-bold text-stone-700 uppercase mb-1.5" data-i18n="form_name_label">
              Kapcsolattartó Neve & Pozíciója *
            </label>
            <input type="text" id="sample-name" name="contact_name" required 
                   placeholder="pl. Kovács Péter (Üzemvezető / Technológus)" 
                   data-i18n-ph="form_placeholder_name"
                   class="w-full px-4 py-3 rounded-xl border bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[#E36527] transition-all"
                   style="border-color: var(--sv-border-light);">
            <span id="err-name" class="hidden text-xs text-red-600 font-mono-spec mt-1 block"></span>
          </div>

          <div>
            <label for="sample-company" class="block text-xs font-mono-spec font-bold text-stone-700 uppercase mb-1.5" data-i18n="form_company_label">
              Cégnév & Adószám * (B2B szűrés)
            </label>
            <input type="text" id="sample-company" name="company_tax_id" required 
                   placeholder="pl. Minta Pékség Kft. • 12345678-2-41" 
                   data-i18n-ph="form_placeholder_company"
                   class="w-full px-4 py-3 rounded-xl border bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[#E36527] transition-all"
                   style="border-color: var(--sv-border-light);">
            <span id="err-company" class="hidden text-xs text-red-600 font-mono-spec mt-1 block"></span>
          </div>

          <div>
            <label for="sample-email" class="block text-xs font-mono-spec font-bold text-stone-700 uppercase mb-1.5" data-i18n="form_email_label">
              Munkahelyi E-mail Cím *
            </label>
            <input type="email" id="sample-email" name="email" required 
                   placeholder="technologia@pekseg.hu" 
                   data-i18n-ph="form_placeholder_email"
                   class="w-full px-4 py-3 rounded-xl border bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[#E36527] transition-all"
                   style="border-color: var(--sv-border-light);">
            <span id="err-email" class="hidden text-xs text-red-600 font-mono-spec mt-1 block"></span>
          </div>

          <div>
            <label for="sample-phone" class="block text-xs font-mono-spec font-bold text-stone-700 uppercase mb-1.5" data-i18n="form_phone_label">
              Közvetlen Telefonszám *
            </label>
            <input type="tel" id="sample-phone" name="phone" required 
                   placeholder="+36 30 123 4567" 
                   data-i18n-ph="form_placeholder_phone"
                   class="w-full px-4 py-3 rounded-xl border bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[#E36527] transition-all"
                   style="border-color: var(--sv-border-light);">
            <span id="err-phone" class="hidden text-xs text-red-600 font-mono-spec mt-1 block"></span>
          </div>

          <div>
            <label for="sample-product" class="block text-xs font-mono-spec font-bold text-stone-700 uppercase mb-1.5" data-i18n="form_product_label">
              Érdeklődés Tárgya (Kért Termék)
            </label>
            <select id="sample-product" name="product_choice" 
                    class="w-full px-4 py-3 rounded-xl border bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[#E36527] transition-all"
                    style="border-color: var(--sv-border-light);">
              <option value="sutesallo-vegyes" data-i18n="form_opt_vegyes">SV Sütésálló Vegyes Gyümölcsíz (10 kg tömb)</option>
              <option value="sutesallo-kajszi" data-i18n="form_opt_kajszi">SV Sütésálló Kajszibarack készítmény (10 kg tömb)</option>
              <option value="kenheto-malna" data-i18n="form_opt_malna">SV Málna ízű készítmény (5 kg vödör)</option>
              <option value="kenheto-afonya" data-i18n="form_opt_afonya">SV Áfonya készítmény (5 kg vödör)</option>
              <option value="sutesallo-extra-meggy" data-i18n="form_opt_meggy">SV Sütésálló Extra Meggy (darabos prémium)</option>
              <option value="egyedi-receptura" data-i18n="form_opt_custom">Egyedi receptúra fejlesztése</option>
            </select>
          </div>

          <div>
            <label for="sample-volume" class="block text-xs font-mono-spec font-bold text-stone-700 uppercase mb-1.5" data-i18n="form_volume_label">
              Tervezett Havi Felhasználás
            </label>
            <select id="sample-volume" name="monthly_volume" 
                    class="w-full px-4 py-3 rounded-xl border bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[#E36527] transition-all"
                    style="border-color: var(--sv-border-light);">
              <option value="vol-small" data-i18n="form_vol_small">&lt; 500 kg / hó (Nagykereskedelmi raktárból)</option>
              <option value="vol-mid" data-i18n="form_vol_mid">500 kg – 2 tonna / hó (Közvetlen gyári raklap)</option>
              <option value="vol-large" data-i18n="form_vol_large">&gt; 2 tonna / hó (Ipari kenyérgyári keretszerződés)</option>
            </select>
          </div>

        </div>

        <div>
          <label for="sample-notes" class="block text-xs font-mono-spec font-bold text-stone-700 uppercase mb-1.5" data-i18n="form_notes_label">
            Technológiai Megjegyzés / Próbasütés Célja
          </label>
          <textarea id="sample-notes" name="technological_notes" rows="3" 
                    placeholder="pl. 210 °C-os leveles tészta automata adagolófejjel történő próbagyártása..." 
                    data-i18n-ph="form_placeholder_notes"
                    class="w-full px-4 py-3 rounded-xl border bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[#E36527] transition-all"
                    style="border-color: var(--sv-border-light);"></textarea>
        </div>

        <div>
          <div class="flex items-center gap-2">
            <input type="checkbox" id="form-gdpr" name="gdpr_consent" required class="w-4 h-4 rounded text-[#E36527] focus:ring-[#E36527]">
            <label for="form-gdpr" class="text-xs text-stone-600 font-mono-spec" data-i18n="form_gdpr_text">
              Elfogadom az adatkezelési tájékoztatót a mintaküldés és technológiai egyeztetés céljából.
            </label>
          </div>
          <span id="err-gdpr" class="hidden text-xs text-red-600 font-mono-spec mt-1 block"></span>
        </div>

        <div class="flex items-center justify-between flex-wrap gap-4 pt-2">
          <button type="submit" 
                  class="px-8 py-3.5 rounded-xl font-bold text-sm shadow-md hover:shadow-lg transition-all transform active:scale-95 flex items-center gap-2"
                  style="background-color: var(--sv-orange); color: white;">
            <i data-lucide="send" class="w-4 h-4"></i>
            <span data-i18n="form_submit_btn">Üzemi Tesztminta Igénylése</span>
          </button>
          <div class="text-xs text-stone-500 font-mono-spec flex items-center gap-1.5">
            <i data-lucide="shield-check" class="w-4 h-4 text-emerald-600"></i>
            <span data-i18n="form_trust_badge">B2B Ipari partnerek részére ingyenes próbaminta</span>
          </div>
        </div>

        <div id="form-success-message" class="hidden p-4 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-900 font-mono-spec text-xs whitespace-pre-line leading-relaxed">
          <!-- Dynamically populated on submission -->
        </div>

      </form>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- CONTACT & MANUFACTURING PLANT SECTION                                    -->
  <!-- ========================================================================= -->
  <section id="kapcsolat" class="py-16 md:py-24 border-b" style="background-color: var(--sv-paper-cream); border-color: var(--sv-border);">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      
      <!-- Section Header -->
      <div class="max-w-3xl mb-12">
        <div class="font-mono-spec text-xs uppercase tracking-widest text-[#E36527] font-semibold mb-2" data-i18n="contact_section_tag">
          Hivatalos Elérhetőségek
        </div>
        <h2 class="font-syne font-bold text-3xl sm:text-4xl text-stone-900 leading-snug pb-1" data-i18n="contact_section_title">
          Közvetlen Kapcsolat a Gyárral
        </h2>
        <p class="text-stone-600 mt-3 text-sm sm:text-base leading-relaxed" data-i18n="contact_section_desc">
          Ipari mintakérések, árajánlatok és technológiai kérdések esetén vegye fel a kapcsolatot közvetlenül gyárvezetésünkkel.
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
                  <div class="font-syne font-bold text-base text-stone-900 group-hover:text-[#E36527] transition-colors">
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
                  <div class="font-syne font-bold text-base text-stone-900 group-hover:text-[#E36527] transition-colors">
                    +36 22 400 984
                  </div>
                </div>
              </div>
              <p class="text-xs text-stone-600 mt-3 font-mono-spec" data-i18n="contact_plant_phone_sub">Móri Gyártóüzem Központ</p>
            </a>

            <!-- Email Box -->
            <a href="mailto:vecsei.andras@sunvalley.hu" class="p-5 rounded-2xl border transition-all hover:shadow-md group sm:col-span-2 flex flex-col justify-between" style="border-color: var(--sv-border); background-color: var(--sv-surface);">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl flex items-center justify-center text-white shrink-0" style="background-color: var(--sv-orange);">
                  <i data-lucide="mail" class="w-5 h-5"></i>
                </div>
                <div>
                  <div class="text-[11px] font-mono-spec text-stone-500 uppercase" data-i18n="contact_email_label">Központi Elektronikus Levelezés</div>
                  <div class="font-syne font-bold text-base text-stone-900 group-hover:text-[#E36527] transition-colors">
                    vecsei.andras@sunvalley.hu
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
              <span class="text-xs font-mono-spec uppercase tracking-wider text-[#E36527] font-semibold" data-i18n="plant_loc_title">Telephely & Üzem</span>
              <h3 class="font-syne font-bold text-xl text-stone-900 mt-0.5">8060 Mór, Major utca 3.</h3>
              <p class="text-xs text-stone-600 mt-1 font-mono-spec">Hrsz. 3601/1 • Fejér vármegye</p>
              <a href="https://maps.google.com/?q=8060+Mór+Major+utca+3" target="_blank" rel="noopener" 
                 class="inline-flex items-center gap-1.5 text-xs font-semibold mt-2 hover:underline" style="color: var(--sv-burgundy);">
                <i data-lucide="map-pin" class="w-3.5 h-3.5 text-[#E36527]"></i>
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
          <img src="assets/sun-valley-logo.png" alt="Sun Valley Zrt. Logo" class="h-9 sm:h-10 w-auto object-contain">
          <div>
            <div class="font-bold text-white font-syne text-base">SUN VALLEY ZRT.</div>
            <div class="text-[10px] text-white/60" data-i18n="footer_tagline">Ipari Gyümölcstechnológia Mór • Alapítva: 2009</div>
          </div>
        </div>

        <div class="flex flex-wrap items-center gap-6 text-white/80">
          <a href="#katalogus" class="hover:text-white transition-colors" data-i18n="nav_catalog">Katalógus</a>
          <a href="#termekek" class="hover:text-white transition-colors" data-i18n="nav_products">Termékek & TDS</a>
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
        btn_request_cat_sample: "Minta Kérése Ebből a Kategóriából",
        btn_sample_short: "Próbagyártási Minta",
        btn_view_category_tds: "TDS Adatlap Megtekintése",
        btn_view_full_tds: "Részletes TDS Műszaki Adatlap",
        card_hero_cat: "PRÉMIUM PÉKIPARI TÉSZTABETÉT",
        card_hero_desc: "Formatartó, természetes aromájú töltelék magas hőmérsékletű sütéshez. Leveles tésztákban és kelt tésztákban sem enged szabad vizet.",
        card_hero_title: "SV Sütésálló Kajszibarack & Vegyes Íz",
        cat_apps_label: "Jellemző Pékipari Alkalmazások:",
        cat_section_desc: "Válasszon technológiai kategóriát: lapozzon a sütésálló tömbök, a hidegen kenhető készítmények és az extra dzsemek között.",
        cat_section_tag: "Lapozható Gasztronómiai Katalógus",
        cat_section_title: "Gyümölcstöltelékek Felhasználás Szerint",
        cat_tab_bake_stable: "1. Sütésálló Töltelékek",
        cat_tab_extra_jam: "3. Extra Dzsemek",
        cat_tab_spreadable: "2. Kenhető Készítmények",
        contact_email_label: "Központi Elektronikus Levelezés",
        contact_email_sub: "Írásbeli ajánlatkérés és műszaki specifikációk továbbítása",
        contact_mobile_label: "Közvetlen Mobilkapcsolat",
        contact_plant_phone_label: "Telephelyi Vezetékes",
        contact_plant_phone_sub: "Móri Gyártóüzem Központ",
        contact_rep_name: "ifj. Vécsei András • Kereskedelem & Vezetés",
        contact_section_desc: "Ipari mintakérések, árajánlatok és technológiai kérdések esetén vegye fel a kapcsolatot közvetlenül gyárvezetésünkkel.",
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
        exotic_note: "* Az egzotikus receptúrákat ipari próbagyártás és technológiai egyeztetés alapján véglegesítjük a partner saját gépsoraira.",
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
        form_company_label: "Cégnév & Adószám * (B2B szűrés)",
        form_email_label: "Munkahelyi E-mail Cím *",
        form_gdpr_text: "Elfogadom az adatkezelési tájékoztatót a mintaküldés és technológiai egyeztetés céljából.",
        form_name_label: "Kapcsolattartó Neve & Pozíciója *",
        form_notes_label: "Technológiai Megjegyzés / Próbasütés Célja",
        form_opt_afonya: "SV Áfonya készítmény (5 kg vödör)",
        form_opt_custom: "Egyedi receptúra fejlesztése",
        form_opt_kajszi: "SV Sütésálló Kajszibarack készítmény (10 kg tömb)",
        form_opt_malna: "SV Málna ízű készítmény (5 kg vödör)",
        form_opt_meggy: "SV Sütésálló Extra Meggy (darabos prémium)",
        form_opt_vegyes: "SV Sütésálló Vegyes Gyümölcsíz (10 kg tömb)",
        form_phone_label: "Közvetlen Telefonszám *",
        form_placeholder_company: "pl. Minta Pékség Kft. • 12345678-2-41",
        form_placeholder_email: "technologia@pekseg.hu",
        form_placeholder_name: "pl. Kovács Péter (Üzemvezető / Technológus)",
        form_placeholder_notes: "pl. 210 °C-os leveles tészta automata adagolófejjel történő próbagyártása...",
        form_placeholder_phone: "+36 30 123 4567",
        form_product_label: "Érdeklődés Tárgya (Kért Termék)",
        form_section_desc: "Töltse ki az alábbi űrlapot, és szakmai csapatunk eljuttatja üzemébe a kívánt 5–10 kg-os tesztmintát próbasütéshez.",
        form_section_tag: "Üzemi Próbagyártási Minta",
        form_section_title: "Kérjen Tesztmintát Saját Gyártósorára",
        form_submit_btn: "Üzemi Tesztminta Igénylése",
        form_trust_badge: "B2B Ipari partnerek részére ingyenes próbaminta",
        form_vol_large: "> 2 tonna / hó (Ipari kenyérgyári keretszerződés)",
        form_vol_mid: "500 kg – 2 tonna / hó (Közvetlen gyári raklap)",
        form_vol_small: "< 500 kg / hó (Nagykereskedelmi raktárból)",
        form_volume_label: "Tervezett Havi Felhasználás",
        hero_badge: "B2B Kenyérgyári & Finompékáru Alapanyagok",
        hero_card_pill: "SÜTÉSÁLLÓ • 200°C+",
        hero_cta_catalog: "Lapozható Gasztro-Katalógus",
        hero_cta_prospectus: "Prospektus (.PPTX)",
        hero_cta_sample: "Üzemi Tesztminta Kérése",
        hero_desc: "A Sun Valley Zrt. a magyar finompékáru-üzemek és ipari kenyérgyárak megbízható belföldi beszállítója. Forma- és alaktartó, gépileg szeletelhető tésztabetétek 10 kg-os kartonos és 5 kg-os vödrös kiszerelésben, közvetlen móri gyártóbázisról.",
        hero_direct_badge: "KÖZVETLEN GYÁRI SZÁLLÍTÁS",
        hero_h1_p1: "200 °C felett sem forr ki.",
        hero_h1_p2: "Ipari sütésálló",
        hero_h1_p3: "gyümölcstöltelékek közvetlenül a gyártótól.",
        hero_qc_badge: "MÓRI GYÁRI MINŐSÉG-ELLENŐRZÉS #SV-2026",
        link_google_maps: "Megtekintés Google Térképen",
        nav_catalog: "Gasztro-Katalógus",
        nav_contact: "Gyártóüzem & Elérhetőség",
        nav_distribution: "Nagykereskedelmi Hálózat",
        nav_products: "Termékek & TDS",
        nav_prospectus: "Prospektus",
        nav_rd: "Receptúra-fejlesztés",
        nav_tech: "Sütésállóság (200°C)",
        plant_loc_title: "Telephely & Üzem",
        prod_section_desc: "Minden termékünk standardizált laboratóriumi paraméterekkel, szigorú mikrobiológiai ellenőrzés mellett készül. Kattintson a TDS adatlapokra a részletes mérnöki specifikációkért (Brix, pH, allergének).",
        prod_section_tag: "Termékportfólió & Minőségi Specifikációk",
        prod_section_title: "Ipari Sütésálló & Kenhető Gyümölcskészítmények",
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
        rd_step2_desc: "Laboratóriumi minta készítése, majd 5–10 kg-os üzemi próbagyártási minta kiküldése a partner saját gyártósorán történő sütési validációra.",
        rd_step2_title: "Receptúra & Üzemi Próba",
        rd_step3_desc: "A végleges műszaki specifikáció (TDS) rögzítése, a csomagolás (vödör, kartontömb, hordó) kiválasztása és a stabil ütemezett raklapos szállítás elindítása.",
        rd_step3_title: "Gyártásra Hangolva",
        rd_tag_1: "Audit & Paraméterezés",
        rd_tag_2: "Tesztminta & Visszacsatolás",
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
        btn_request_cat_sample: "Request Category Sample",
        btn_sample_short: "Trial Sample",
        btn_view_category_tds: "View Category TDS Sheet",
        btn_view_full_tds: "View Detailed TDS Specification",
        card_hero_cat: "COMMERCIAL BAKERY INSERT",
        card_hero_desc: "Form-retaining fruit preparation with intense natural aroma for high-heat baking. Zero syneresis in puff pastries and yeast doughs.",
        card_hero_title: "SV Bake-Stable Apricot & Mixed Fruit",
        cat_apps_label: "Verified Industrial Applications:",
        cat_section_desc: "Select your technology category: browse bake-stable blocks, cold-spreadable fillings, and premium extra jams.",
        cat_section_tag: "Interactive Gastro-Catalog",
        cat_section_title: "Fruit Preparations by Application",
        cat_tab_bake_stable: "1. Bake-Stable Fillings",
        cat_tab_extra_jam: "3. Extra Jams",
        cat_tab_spreadable: "2. Cold-Spreadable Fillings",
        contact_email_label: "Corporate Email Address",
        contact_email_sub: "Formal quotes and technical inquiries",
        contact_mobile_label: "Direct Mobile Line",
        contact_plant_phone_label: "Plant Landline",
        contact_plant_phone_sub: "Mór Manufacturing Headquarters",
        contact_rep_name: "András Vécsei Jr. • Commercial Director",
        contact_section_desc: "For trial batch requests, quotes, or food engineering inquiries, reach out directly to our leadership team.",
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
        exotic_note: "* Exotic formulations are finalized following laboratory trials and on-site pilot baking at your facility.",
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
        form_company_label: "Company & Tax ID * (B2B verification)",
        form_email_label: "Work Email *",
        form_gdpr_text: "I agree to data processing for sample dispatch and technical consultation.",
        form_name_label: "Contact Name & Position *",
        form_notes_label: "Technical Notes / Test Objectives",
        form_opt_afonya: "SV Blueberry Preparation (5 kg bucket)",
        form_opt_custom: "Custom Recipe R&D",
        form_opt_kajszi: "SV Bake-Stable Apricot (10 kg block)",
        form_opt_malna: "SV Raspberry Preparation (5 kg bucket)",
        form_opt_meggy: "SV Bake-Stable Extra Sour Cherry (fruit pieces)",
        form_opt_vegyes: "SV Bake-Stable Mixed Fruit (10 kg block)",
        form_phone_label: "Direct Phone *",
        form_placeholder_company: "e.g. Master Bakery Ltd. • EU VAT ID",
        form_placeholder_email: "purchasing@bakery.com",
        form_placeholder_name: "e.g. John Miller (Plant Manager / Food Technologist)",
        form_placeholder_notes: "e.g. 210 °C puff pastry trial with automated needle depositor...",
        form_placeholder_phone: "+44 20 1234 5678",
        form_product_label: "Product of Interest",
        form_section_desc: "Submit your details, and our technical team will prepare and dispatch a 5–10 kg pilot bucket for test baking.",
        form_section_tag: "Pilot Batch Request",
        form_section_title: "Request a Trial Sample for Your Production Line",
        form_submit_btn: "Request Industrial Sample",
        form_trust_badge: "Free pilot sample for verified B2B commercial bakeries",
        form_vol_large: "> 2 metric tons / month (Enterprise supply contract)",
        form_vol_mid: "500 kg – 2 metric tons / month (Direct pallet)",
        form_vol_small: "< 500 kg / month (From wholesale depot)",
        form_volume_label: "Estimated Monthly Volume",
        hero_badge: "B2B Commercial Bakery & Pastry Ingredients",
        hero_card_pill: "BAKE-STABLE • 200°C+",
        hero_cta_catalog: "Interactive Gastro-Catalog",
        hero_cta_prospectus: "Download Brochure (.PPTX)",
        hero_cta_sample: "Request Trial Batch Sample",
        hero_desc: "Sun Valley Zrt. is a proven supplier for industrial bread factories and commercial pastry plants. Shape-retaining, mechanically sliceable fruit fillings in 10 kg cartons and 5 kg buckets directly from our Mór facility.",
        hero_direct_badge: "DIRECT FACTORY SUPPLY",
        hero_h1_p1: "No boil-out above 200 °C.",
        hero_h1_p2: "Industrial bake-stable",
        hero_h1_p3: "Fruit preparations directly from the manufacturer.",
        hero_qc_badge: "MÓR FACTORY QC #SV-2026",
        link_google_maps: "View on Google Maps",
        nav_catalog: "Gastro-Catalog",
        nav_contact: "Plant & Contact",
        nav_distribution: "Wholesale Network",
        nav_products: "Products & TDS",
        nav_prospectus: "Brochure",
        nav_rd: "Custom R&D",
        nav_tech: "Thermo-Stability (200°C)",
        plant_loc_title: "Plant & Production Site",
        prod_section_desc: "Standardized laboratory parameters with rigorous microbiological control. Click on any product for its Technical Data Sheet.",
        prod_section_tag: "Product Matrix & Laboratory Specifications",
        prod_section_title: "Industrial Bake-Stable & Spreadable Fruit Fillings",
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
        rd_step2_desc: "Laboratory formulation followed by a 5–10 kg trial batch dispatched for validation on your production line.",
        rd_step2_title: "Formulation & Pilot Batch",
        rd_step3_desc: "Locking technical specifications (TDS), selecting packaging units, and scheduling ongoing palletized deliveries.",
        rd_step3_title: "Production Integration",
        rd_tag_1: "Audit & Specifications",
        rd_tag_2: "Pilot Sample & Feedback",
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
      },

      de: {
        btn_download_prospectus: "Broschüre Herunterladen (.PPTX)",
        btn_request_cat_sample: "Muster Aus Dieser Kategorie Anfordern",
        btn_sample_short: "Probemuster",
        btn_view_category_tds: "TDS Datenblatt Ansehen",
        btn_view_full_tds: "Technisches Datenblatt (TDS)",
        card_hero_cat: "INDUSTRIELLE FEINGEBÄCK-FÜLLUNG",
        card_hero_desc: "Formstabile Fruchtzubereitung für Hochtemperatur-Backprozesse. Keine Synärese in Blätterteig und Hefegebäck.",
        card_hero_title: "SV Backstabile Aprikosen- & Mischfruchtfüllung",
        cat_apps_label: "Typische Bäckereianwendungen:",
        cat_section_desc: "Wählen Sie Ihre Technologie: Blättern Sie durch backstabile Blöcke, streichfähige Füllungen und Extra-Konfitüren.",
        cat_section_tag: "Blätterbarer Gastro-Katalog",
        cat_section_title: "Fruchtzubereitungen nach Anwendung",
        cat_tab_bake_stable: "1. Backstabile Füllungen",
        cat_tab_extra_jam: "3. Extra-Konfitüren",
        cat_tab_spreadable: "2. Streichfähige Füllungen",
        contact_email_label: "Zentrale E-Mail-Adresse",
        contact_email_sub: "Schriftliche Preisanfragen & Spezifikationen",
        contact_mobile_label: "Direkte Mobilnummer",
        contact_plant_phone_label: "Werksfestnetz",
        contact_plant_phone_sub: "Produktionsstandort Mór",
        contact_rep_name: "András Vécsei jun. • Vertriebsleitung",
        contact_section_desc: "Für Probemuster, Preisrahmenverträge oder lebensmitteltechnologische Fragen kontaktieren Sie bitte direkt unsere Werksleitung.",
        contact_section_tag: "Offizielle Kontaktdaten",
        contact_section_title: "Direkter Draht zur Werksleitung",
        corp_hq_title: "Offizieller Firmensitz",
        dist_section_desc: "Unser duales Vertriebsmodell sichert höchste Versorgungssicherheit: Direkte Lieferverträge ab Werk für Großmengen oder autorisierte Großhandelspartner.",
        dist_section_tag: "Vertriebskanäle & Logistik",
        dist_section_title: "Wie Gelangen die Produkte in Ihr Werk?",
        dist_t1_badge: "KANAL 1 • INDUSTRIEVERTRÄGE",
        dist_t1_cta: "Rahmenvertrag Anfragen",
        dist_t1_desc: "Für Großbäckereien (>500 kg pro Bestellung). Werkskonditionen, Rahmenverträge und kontinuierliche Betreuung.",
        dist_t1_p1: "480 kg Paletteneinheiten",
        dist_t1_p2: "Garantierte Chargenhomogenität",
        dist_t1_p3: "Direkter Werksansprechpartner",
        dist_t1_title: "Direkte Werksbelieferung (Paletten- & LKW-Ladungen)",
        dist_t2_badge: "KANAL 2 • REGIONALLAGER",
        dist_t2_desc: "Konditoreien und Bäckereien beziehen 5–10 kg Gebinde unkompliziert über regionale Bäckereigroßhändler.",
        dist_t2_footer: "Fragen Sie Ihren regionalen Bäckereifachgroßhändler.",
        dist_t2_title: "Autorisiertes Großhandelsnetzwerk",
        exotic_citrus: "Zitrus & Orange",
        exotic_desc: "Neben den Grundsorten entwickeln wir maßgeschneiderte Rezepturen aus exotischen Früchten (Mango, Maracuja, Zitrus) für Ihr Endprodukt.",
        exotic_img_badge: "F&E-LABOR",
        exotic_img_title: "Individuelle Fruchtkombinationen",
        exotic_mango: "Mango & Maracuja",
        exotic_note: "* Exotische Rezepturen werden nach Laborversuchen und Probeproduktion vor Ort finalisiert.",
        exotic_pineapple: "Ananas & Kiwi",
        exotic_tag: "Sonderrezepturen • Innovation",
        exotic_title: "Exotische Früchte. Maßgeschneidert.",
        flavor_apple: "Apfel",
        flavor_apricot: "Aprikose",
        flavor_blueberry: "Heidelbeere",
        flavor_classic_mixed: "Klassische Mischfrucht",
        flavor_plum: "Pflaume",
        flavor_raspberry: "Himbeere",
        flavor_sour_cherry: "Sauerkirsche",
        flavors_badge: "HEIMISCHE FRUCHTBASIS",
        flavors_cta: "Detaillierte Parameter in der Produktmatrix",
        flavors_desc: "Wir verarbeiten ungarische Früchte schonend in modernen Vakuumkesseln, abgestimmt auf Ihre Back- oder Kalttechnologie.",
        flavors_img_title: "7 Grundlegende Bäckerei-Fruchtsorten",
        flavors_tag: "Traditionelle Früchte • Moderne Technologie",
        flavors_title: "Vertraute Aromen. Industrielle Verlässlichkeit.",
        footer_cert_iso: "ISO / HACCP-Standard",
        footer_cert_plant: "Produktionsstandort Mór",
        footer_rights: "© 2026 Sun Valley Kereskedelmi Zrt. • Alle Rechte vorbehalten.",
        footer_tagline: "Industrielle Fruchttechnologie Mór • Gegr. 2009",
        form_company_label: "Firma & Steuernummer * (B2B)",
        form_email_label: "Geschäftliche E-Mail *",
        form_gdpr_text: "Ich stimme der Datenverarbeitung zur Musterzusendung und technischen Beratung zu.",
        form_name_label: "Name & Position *",
        form_notes_label: "Technologische Anmerkungen",
        form_opt_afonya: "SV Heidelbeer-Zubereitung (5 kg Eimer)",
        form_opt_custom: "Individuelle Rezepturentwicklung",
        form_opt_kajszi: "SV Backstabile Aprikose (10 kg Block)",
        form_opt_malna: "SV Himbeer-Zubereitung (5 kg Eimer)",
        form_opt_meggy: "SV Backstabile Extra-Sauerkirsche (mit Stücken)",
        form_opt_vegyes: "SV Backstabile Mischfrucht (10 kg Block)",
        form_phone_label: "Telefonnummer *",
        form_placeholder_company: "z.B. Meisterbäckerei GmbH • USt-IdNr.",
        form_placeholder_email: "einkauf@baeckerei.de",
        form_placeholder_name: "z.B. Peter Schmidt (Betriebsleiter / Technologe)",
        form_placeholder_notes: "z.B. Testbacken bei 210 °C im Blätterteig mit automatischer Dosieranlage...",
        form_placeholder_phone: "+49 30 12345678",
        form_product_label: "Gewünschtes Produkt",
        form_section_desc: "Füllen Sie das Formular aus; wir senden Ihnen ein 5–10 kg Probemuster für Testbacken.",
        form_section_tag: "Betriebliches Produktionsmuster",
        form_section_title: "Testmuster für Ihre Produktionslinie Anfordern",
        form_submit_btn: "Betriebsmuster Anfordern",
        form_trust_badge: "Kostenloses Probemuster für qualifizierte B2B-Industriebäckereien",
        form_vol_large: "> 2 Tonnen / Monat (Industrieller Rahmenvertrag)",
        form_vol_mid: "500 kg – 2 Tonnen / Monat (Direktpalette)",
        form_vol_small: "< 500 kg / Monat (Über Großhandelslager)",
        form_volume_label: "Geplanter Monatsbedarf",
        hero_badge: "B2B Großbäckerei- & Feingebäck-Rohstoffe",
        hero_card_pill: "BACKSTABIL • 200°C+",
        hero_cta_catalog: "Gastro-Katalog Durchblättern",
        hero_cta_prospectus: "Broschüre (.PPTX)",
        hero_cta_sample: "Produktionsmuster Anfordern",
        hero_desc: "Sun Valley Zrt. ist der verlässliche Partner für Großbäckereien und Feingebäckhersteller. Formstabile, maschinell schneidbare Fruchtfüllungen in 10 kg Kartons und 5 kg Eimern direkt aus Mór.",
        hero_direct_badge: "DIREKTE WERKSBELIEFERUNG",
        hero_h1_p1: "Kein Auskochen über 200 °C.",
        hero_h1_p2: "Industrielle backstabile",
        hero_h1_p3: "Fruchtzubereitungen direkt vom Hersteller.",
        hero_qc_badge: "WERKS-QUALITÄTSKONTROLLE MÓR #SV-2026",
        link_google_maps: "Auf Google Maps Anzeigen",
        nav_catalog: "Gastro-Katalog",
        nav_contact: "Werk & Kontakt",
        nav_distribution: "Großhandelsnetz",
        nav_products: "Produkte & TDS",
        nav_prospectus: "Broschüre",
        nav_rd: "Rezepturentwicklung",
        nav_tech: "Hitzestabilität (200°C)",
        plant_loc_title: "Produktionswerk & Standort",
        prod_section_desc: "Standardisierte Laborwerte unter strenger mikrobiologischer Kontrolle. Klicken Sie auf ein TDS für Details.",
        prod_section_tag: "Produktportfolio & Spezifikationen",
        prod_section_title: "Industrielle Backstabile & Streichfähige Fruchtzubereitungen",
        prospectus_badge: "OFFIZIELLE B2B DOKUMENTATION • V1.4",
        prospectus_desc: "Präsentation über unsere Produktionsanlagen in Mór, das Sortiment, Logistik und Qualitätszertifikate.",
        prospectus_format: "Format: Microsoft PowerPoint (.pptx)",
        prospectus_size: "Dateigröße: ~11,1 MB",
        prospectus_title: "Unternehmensbroschüre der Sun Valley Zrt. Herunterladen",
        prospectus_version: "Version: V1.4 (2026)",
        rating_badge: "AA+ Bonität (Dun & Bradstreet)",
        rating_label: "Finanzrating:",
        rd_section_desc: "Gemeinsam mit Ihren Bäckereitechnologen in 3 klaren Schritten:",
        rd_section_tag: "Rezepturentwicklungs-Prozess",
        rd_section_title: "Ihre Idee. Gemeinsame Entwicklung.",
        rd_step1_desc: "Erfassung von Viskosität, Fruchtanteil, Backtemperatur (180–220 °C) und Dosieranlagen.",
        rd_step1_title: "Bedarfsanalyse",
        rd_step2_desc: "Laborabstimmung und Versand eines 5–10 kg Probemusters für Testbacken auf Ihrer Linie.",
        rd_step2_title: "Rezeptur & Werksmuster",
        rd_step3_desc: "Fixierung des TDS-Datenblatts, Auswahl der Gebinde und Start der planbaren Belieferung.",
        rd_step3_title: "Serienfertigung",
        rd_tag_1: "Bedarfsanalyse & Spezifikation",
        rd_tag_2: "Testmuster & Feedback",
        rd_tag_3: "TDS-Freigabe & Serienbelieferung",
        reg_id_label: "Handelsregisternr.:",
        spec_brix: "Trockensubstanz (Brix)",
        spec_slice: "Schneidbarkeit (Maschinenschnitt)",
        spec_slice_val: "Exzellent / Fester Gelkörper",
        spec_thermo: "Hitzetest (200 °C / 15 Min.)",
        spec_thermo_val: "Formstabil / Kein Auskochen",
        stat_energy: "Auszeichnung Energiebewusstes Werk",
        stat_energy_val: "VEP-Preisträger",
        stat_heritage: "Fruchtverarbeitungs-Tradition (Traditionsstandort Vitamór)",
        stat_heritage_val: "15+ Jahre",
        stat_rating: "Bonitätsbewertung (Schuldenfrei AA+)",
        stat_revenue: "Jahresumsatz (Solide Eigenkapitalbasis)",
        stat_revenue_val: "2,8 – 3,3 Mio. €",
        tagline: "Industrielle Fruchttechnologie • Gegr. 2009",
        tax_id_label: "Steuernummer:",
        tech_badge_dosing: "AUTOMATISCHE DOSIERUNG",
        tech_badge_freeze: "GEFRIER-AUFTAU-STABIL",
        tech_card1_desc: "Behält selbst über 200 °C Form und Volumen – ohne Auskochen oder Anbrennen auf dem Backblech.",
        tech_card1_title: "Garantierte Backstabilität",
        tech_card2_desc: "Für tiefgekühlte Teiglinge. Kein Wasserverlust beim Auftauen.",
        tech_card2_title: "Gefrier-Auftau-Stabilität",
        tech_card3_desc: "Optimierte Viskosität für automatische Injektionsnadeln (Berliner, Croissants) ohne Nachtropfen.",
        tech_card3_title: "Maschinelle Dosierbarkeit",
        tech_card4_desc: "5 kg Eimer für Konditoreien, 10 kg schneidbare Blockware für Großbäckereien oder 200 kg Aseptikfässer für Großwerke.",
        tech_card4_title: "Kleinserie bis Großindustrie",
        tech_section_desc: "Ausschuss entsteht meist durch auskochende Füllungen oder verklebte Dosierdüsen. Das Sun Valley System basiert auf vier Säulen:",
        tech_section_tag: "Lebensmitteltechnologische Garantien",
        tech_section_title: "Nicht Nur Geschmack. Prozesssicherheit.",
        telemetry_geo_label: "Produktionsstandort",
        telemetry_geo_sub: "Major utca 3., Mór",
        telemetry_heat_label: "Hitzestabilität",
        telemetry_heat_sub: "Kochfest, formbeständig",
        telemetry_pack_label: "Verpackung",
        telemetry_pack_sub: "480 kg Paletteneinheit",
        topbar_capacity: "Jahresumsatz: 2,8–3,3 Mio. €",
        topbar_rating: "AA+ Bonitätsbewertung",
        topbar_scale: "Produktionswerk: Mór, Ungarn (Major u. 3.)"
      }
    };

    const catalogData = {
      "bake-stable": {
        productKey: "sutesallo-vegyes",
        badge: { hu: "10 KG KARTON • SÜTÉSÁLLÓ TÖMB", en: "10 KG CARTON • BAKE-STABLE BLOCK", de: "10 KG KARTON • BACKSTABILER BLOCK" },
        title: { hu: "Sütésálló Gyümölcstöltelékek", en: "Bake-Stable Fruit Preparations", de: "Backstabile Fruchtzubereitungen" },
        subtitle: { hu: "200 °C felett alaktartó, gépileg szeletelhető tésztabetétek", en: "Shape-retaining above 200 °C, automated sliceable blocks", de: "Formstabil über 200 °C, maschinell schneidbare Blöcke" },
        desc: {
          hu: "Speciális pektinhálójuk révén a tészta 200 °C feletti sütése során sem forrnak ki, nem áztatják el a tésztát, és hűlés után is megőrzik rugalmas gélállagukat. Kiválóan alkalmasak ipari automatizált töltő- és szeletelősorokra.",
          en: "Engineered with a high-performance pectin network that prevents boil-outs even above 200 °C. Eliminates dough sogginess and retains elastic gel consistency after baking. Optimized for automated dough sheeters and depositors.",
          de: "Dank der speziellen Pektinstruktur kochen diese Füllungen auch über 200 °C nicht aus und weichen den Teig nicht auf. Behalten nach dem Abkühlen ihre elastische Gelform. Perfekt für Schneid- und Dosiermaschinen."
        },
        apps: {
          hu: ["Sárgabarackos bukta", "Lekváros papucs", "Rácsos linzer", "Leveles táskák", "Piték & derelyék"],
          en: ["Apricot Buns", "Turnovers & Pockets", "Lattice Linz Tarts", "Puff Pastry Pockets", "Pies & Strudels"],
          de: ["Aprikosenbuchteln", "Plunder-Taschen", "Linzer Schnitten", "Blätterteigtaschen", "Kuchen & Strudel"]
        },
        specs: {
          heat: "≥ 200 °C",
          brix: "58–64° Brix",
          pack: { hu: "10 kg karton", en: "10 kg carton", de: "10 kg Karton" }
        },
        image: "assets/lekvaros-bukta.jpg",
        caption: {
          hu: "Üzemi próbasütési minta • Lekváros bukta 200 °C sütés után",
          en: "Industrial test baking sample • Jam buns baked at 200 °C",
          de: "Betriebliches Testback-Muster • Buchteln gebacken bei 200 °C"
        },
        tdsIndex: 0
      },
      "spreadable": {
        productKey: "kenheto-malna",
        badge: { hu: "5 KG MŰANYAG VÖDÖR • HIDEG TECHNOLÓGIA", en: "5 KG BUCKET • COLD PROCESS", de: "5 KG EIMER • KALTTECHNOLOGIE" },
        title: { hu: "Kenhető Gyümölcskészítmények", en: "Cold-Spreadable Fruit Preparations", de: "Streichfähige Fruchtzubereitungen" },
        subtitle: { hu: "Homogén, selymes kenhetőség cukrászati felületekre", en: "Homogeneous, velvety spreadability for pastry layers", de: "Homogene, samtige Streichfähigkeit für Konditoreiböden" },
        desc: {
          hu: "Hideg technológiára kifejlesztett, egyenletesen terülő gyümölcskészítmények piskótatekercsek, tortalapok és linzer sütemények gyors és tiszta kenéséhez. Magas gyümölcsös aroma és intenzív fényesség jellemzi.",
          en: "Formulated for ambient and cold pastry assembly. Smoothly spreads over sponge cakes, swiss rolls, and linzer cookies without tearing tender crumbs. Delivers vibrant fruit gloss and rich aromatic profile.",
          de: "Entwickelt für die kalte Konditoreiverarbeitung. Lässt sich mühelos auf Biskuitböden, Rouladen und Linzer Gebäck verstreichen, ohne den Teig zu beschädigen. Ausgezeichneter Fruchtglanz."
        },
        apps: {
          hu: ["Linzer karika", "Piskótatekercs", "Epres/málnás tortalap", "Sütemény áthúzás", "Desszertbetét"],
          en: ["Linzer Cookies", "Swiss Roll Filling", "Cake Layer Spreading", "Pastry Glazing", "Dessert Inclusions"],
          de: ["Linzer Augen", "Biskuitrollen", "Tortenboden-Füllung", "Kuchen-Glasur", "Dessert-Einlagen"]
        },
        specs: {
          heat: { hu: "Hideg eljárás", en: "Cold process", de: "Kaltverfahren" },
          brix: "62–66° Brix",
          pack: { hu: "5 kg vödör", en: "5 kg bucket", de: "5 kg Eimer" }
        },
        image: "assets/jam.jpg",
        caption: {
          hu: "Hidegen kenhető gyümölcskészítmény • Homogén selymes textúra",
          en: "Cold-spreadable fruit preparation • Smooth velvety texture",
          de: "Kalt streichfähige Fruchtzubereitung • Homogene samtige Textur"
        },
        tdsIndex: 2
      },
      "extra-jam": {
        productKey: "sutesallo-extra-meggy",
        badge: { hu: "PRÉMIUM GYÜMÖLCSDARABOS • EXTRA DZSEM", en: "PREMIUM FRUIT PIECES • EXTRA JAM", de: "PREMIUM FRUCHTSTÜCKE • EXTRA KONFITÜRE" },
        title: { hu: "Sütésálló Extra Dzsemek", en: "Bake-Stable Extra Jams", de: "Backstabile Extra-Konfitüren" },
        subtitle: { hu: "Látványos gyümölcsdarabok magas hőtűréssel ötvözve", en: "Identifiable fruit pieces combined with high thermal resistance", de: "Sichtbare Fruchtstücke kombiniert mit hoher Hitzebeständigkeit" },
        desc: {
          hu: "Kifejezetten prémium finompékárukhoz és kézműves cukrászati termékekhez megalkotott készítmények egész vagy darabolt gyümölcsökkel. A gyümölcsdarabok a sütés során is felismerhetőek és zamatosak maradnak.",
          en: "Crafted for premium viennoiserie and high-end baked goods featuring recognizable fruit pieces. The fruit inclusions retain their succulent bite and color without bleeding excessively into the surrounding crust.",
          de: "Entwickelt für Premium-Plundergebäcke und anspruchsvolle Konditoreiprodukte mit ganzen oder stückigen Früchten. Die Fruchtstücke bleiben beim Backen saftig und formstabil."
        },
        apps: {
          hu: ["Kézműves croissant", "Gyümölcskosárka", "Dán pékáru", "Prémium leveles tészta", "Rácsos sütemény"],
          en: ["Artisan Croissants", "Fruit Tartlets", "Danish Pastries", "Viennoiserie", "Gourmet Lattice Pies"],
          de: ["Handwerks-Croissants", "Fruchttörtchen", "Dänisches Plundergebäck", "Premium-Blätterteig", "Gitterkuchen"]
        },
        specs: {
          heat: "≥ 190 °C",
          brix: "60–65° Brix",
          pack: { hu: "5 kg / 10 kg", en: "5 kg / 10 kg", de: "5 kg / 10 kg" }
        },
        image: "assets/jam-cookie.jpg",
        caption: {
          hu: "Prémium darabos gyümölcsbetét • Sütemény alkalmazás",
          en: "Premium fruit pieces • Pastry application",
          de: "Premium Fruchtstücke • Feingebäck-Anwendung"
        },
        tdsIndex: 4
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
          en: "SV Bake-Stable Mixed Fruit Preparation",
          de: "SV Backstabile Gemischte Fruchtzubereitung"
        },
        badge: { hu: "SÜTÉSÁLLÓ TÖMB • VEGÁN", en: "BAKE-STABLE BLOCK • VEGAN", de: "BACKSTABIL BLOCK • VEGAN" },
        pack: { hu: "10 kg karton (480 kg/raklap)", en: "10 kg carton (480 kg/pallet)", de: "10 kg Karton (480 kg/Palette)" },
        specs: {
          brix: "58–62° Brix",
          ph: "3.3 – 3.6",
          heat: "≥ 200 °C (15 perc)",
          shelfLife: { hu: "12 hónap", en: "12 months", de: "12 Monate" },
          sliceability: { hu: "Kiváló, késálló gépi szeletelés", en: "Excellent, clean automated slicing", de: "Exzellent, messerfeste Schneidbarkeit" }
        },
        desc: {
          hu: "Hagyományos receptúrájú, természetes színezékkel készülő, tömbösített sütésálló gyümölcstöltelék. Kifejezetten ipari bukták, táskák és kelt tészták gépileg szeletelhető töltésére kifejlesztve.",
          en: "Traditional recipe thermo-stable fruit block made with natural colors. Engineered specifically for automated slicing and filling of commercial yeast buns, turnovers, and puff pastries.",
          de: "Traditionell hergestellte, backstabile Blockfruchtzubereitung mit natürlichen Farbstoffen. Speziell entwickelt für maschinelles Schneiden und Füllen von Buchteln und Hefegebäcken."
        }
      },
      {
        id: "sutesallo-kajszi",
        category: "sutesallo",
        names: {
          hu: "SV Sütésálló Kajszibarack Ízű Készítmény",
          en: "SV Bake-Stable Apricot Preparation",
          de: "SV Backstabile Aprikosenzubereitung"
        },
        badge: { hu: "200°C HŐTŰRŐ • GÉLÁLLÓ", en: "200°C HEAT-STABLE • GEL", de: "200°C HITZEFEST • GEL" },
        pack: { hu: "10 kg kartondoboz", en: "10 kg carton box", de: "10 kg Kartonbox" },
        specs: {
          brix: "60–64° Brix",
          ph: "3.2 – 3.5",
          heat: "≥ 200 °C (Formamegtartó)",
          shelfLife: { hu: "12 hónap", en: "12 months", de: "12 Monate" },
          sliceability: { hu: "Késálló, tiszta vágási él", en: "Firm gel, clean cut edge", de: "Fester Gelkörper, saubere Kante" }
        },
        desc: {
          hu: "Intenzív kajszibarack ízvilágú, aranysárga színű forma- és alaktartó gél. Leveles tészták, piték és finompékáruk magas hőfokú sütéséhez.",
          en: "Vibrant golden apricot flavor gel. Maintains sharp geometry and volume in high-temperature puff pastry, pies, and Danish pastries.",
          de: "Intensiver Aprikosengeschmack mit goldgelber Farbe. Behält Form und Volumen beim Hochtemperaturbacken in Blätterteig und Kuchen."
        }
      },
      {
        id: "kenheto-malna",
        category: "kenheto",
        names: {
          hu: "SV Málna Ízű Gyümölcskészítmény",
          en: "SV Raspberry Confectionery Preparation",
          de: "SV Himbeer-Fruchtzubereitung"
        },
        badge: { hu: "HIDEGEN KENHETŐ • VÖDRÖS", en: "COLD SPREADABLE • BUCKET", de: "KALT STREICHFÄHIG • EIMER" },
        pack: { hu: "5 kg műanyag vödör", en: "5 kg plastic bucket", de: "5 kg Kunststoffeimer" },
        specs: {
          brix: "65° Brix",
          ph: "3.2 – 3.4",
          heat: { hu: "Hideg technológia", en: "Cold process", de: "Kalttechnologie" },
          shelfLife: { hu: "9 hónap", en: "9 months", de: "9 Monate" },
          sliceability: { hu: "Selymes, homogén kenhetőség", en: "Smooth, velvety spreadability", de: "Seidig-glatte Streichfähigkeit" }
        },
        desc: {
          hu: "Homogén állagú, hidegen könnyen kenhető málnás gyümölcskészítmény piskótatekercsek, linzer sütemények és tortalapok összetöltéséhez.",
          en: "Smooth, cold-spreadable raspberry preparation designed for sponge cake layering, linzer cookies, and premium confectionery fillings.",
          de: "Homogene, kalt streichfähige Himbeerzubereitung für Biskuitrouladen, Linzer Plätzchen und Tortenfüllungen."
        }
      },
      {
        id: "kenheto-afonya",
        category: "kenheto",
        names: {
          hu: "SV Áfonya Ízű Gyümölcskészítmény",
          en: "SV Blueberry Confectionery Preparation",
          de: "SV Heidelbeer-Fruchtzubereitung"
        },
        badge: { hu: "PRÉMIUM AROMA • HIDEG STABIL", en: "PREMIUM AROMA • COLD STABLE", de: "PREMIUM AROMA • KALTSTABIL" },
        pack: { hu: "5 kg műanyag vödör", en: "5 kg plastic bucket", de: "5 kg Kunststoffeimer" },
        specs: {
          brix: "65° Brix",
          ph: "3.2 – 3.5",
          heat: { hu: "Hideg technológia", en: "Cold process", de: "Kalttechnologie" },
          shelfLife: { hu: "9 hónap", en: "9 months", de: "9 Monate" },
          sliceability: { hu: "Kiváló tapadás és eloszlás", en: "Superior adhesion & spread", de: "Hervorragende Haftung & Verlauf" }
        },
        desc: {
          hu: "Mélybordó-kékes árnyalatú, gazdag erdei áfonya karakterű gyümölcsbetét prémium desszertekhez, fánkokhoz és cukrászati termékekhez.",
          en: "Deep purple-blue hue with rich wild blueberry profile. Designed for premium dessert inserts, donut injecting, and patisserie glazing.",
          de: "Tiefblau-violette Farbe mit vollem Waldheidelbeer-Aroma. Konzipiert für Premium-Desserts, Berliner-Injektionen und Konditoreiwaren."
        }
      },
      {
        id: "sutesallo-extra-meggy",
        category: "sutesallo",
        names: {
          hu: "SV Sütésálló Extra Meggy Töltelék",
          en: "SV Bake-Stable Extra Sour Cherry Filling",
          de: "SV Backstabile Extra-Sauerkirschfüllung"
        },
        badge: { hu: "DARABOS GYÜMÖLCS • SÜTÉSÁLLÓ", en: "FRUIT PIECES • BAKE-STABLE", de: "FRUCHTSTÜCKE • BACKSTABIL" },
        pack: { hu: "10 kg karton / 5 kg vödör", en: "10 kg carton / 5 kg bucket", de: "10 kg Karton / 5 kg Eimer" },
        specs: {
          brix: "60–63° Brix",
          ph: "3.1 – 3.4",
          heat: "≥ 195 °C",
          shelfLife: { hu: "12 hónap", en: "12 months", de: "12 Monate" },
          sliceability: { hu: "Formamegtartó, nem folyós", en: "Shape-retaining pieces, non-bleeding", de: "Formbeständige Stücke, kein Auslaufen" }
        },
        desc: {
          hu: "Kellemesen fanyar, valódi fekete és cigánymeggy szemekkel készült prémium töltelék rétesekhez, pitékhez és dán pékárukhoz.",
          en: "Pleasantly tart, rich sour cherry filling with intact fruit pieces. Formulated for strudels, rustic pies, and Danish pastries.",
          de: "Angenehm herbe, vollaromatische Sauerkirschfüllung mit ganzen Fruchtstücken für Strudel, Kuchen und Plunder."
        }
      },
      {
        id: "egyedi-receptura",
        category: "egyedi",
        names: {
          hu: "SV Egzotikus Mangó-Maracuja Töltelék",
          en: "SV Exotic Mango-Passionfruit Filling",
          de: "SV Exotische Mango-Maracuja-Füllung"
        },
        badge: { hu: "INNOVATÍV R&D • EGYEDI", en: "INNOVATIVE R&D • CUSTOM", de: "INNOVATIVE F&E • SONDERREZEPTUR" },
        pack: { hu: "5 kg vödör / 200 kg tartály", en: "5 kg bucket / 200 kg drum", de: "5 kg Eimer / 200 kg Fass" },
        specs: {
          brix: "60–65° Brix (állítható)",
          ph: "3.2 – 3.5",
          heat: "180 °C – 210 °C",
          shelfLife: { hu: "9–12 hónap", en: "9–12 months", de: "9–12 Monate" },
          sliceability: { hu: "Injektálható vagy kenhető", en: "Injectable or spreadable", de: "Injizierbar oder streichfähig" }
        },
        desc: {
          hu: "Trópusi hangulatú, intenzív sárga színű és friss gyümölcsös savgerincű készítmény. Croissant-ok, finompékáruk és prémium desszertek újító alapanyaga.",
          en: "Tropical flavor profile with vivid golden color and vibrant fruit acidity. Next-generation filling for croissants, artisan tarts, and patisserie items.",
          de: "Tropisches Geschmacksprofil mit lebendiger Farbe und frischer Fruchtnote. Zukunftsweisende Füllung für Croissants und Premium-Gebäcke."
        }
      }
    ];

    let currentLang = 'hu';
    let currentCatalogTab = 'bake-stable';

    // ---------------------------------------------------------------------------
    // LANGUAGE SWITCHER ENGINE
    // ---------------------------------------------------------------------------
    function setLanguage(lang) {
      if (!translations[lang]) return;
      currentLang = lang;

      // Update switcher button styles while strictly preserving responsive classes!
      ['hu', 'en', 'de'].forEach(l => {
        const btn = document.getElementById(`lang-${l}`);
        if (l === lang) {
          btn.className = "px-1.5 py-0.5 sm:px-2 sm:py-1 rounded font-bold transition-all bg-[#5F2125] text-white shadow-sm text-[10px] sm:text-xs";
        } else {
          btn.className = "px-1.5 py-0.5 sm:px-2 sm:py-1 rounded font-medium text-stone-600 hover:text-[#E36527] transition-all text-[10px] sm:text-xs";
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
    // KATALÓGUS TAB HANDLER
    // ---------------------------------------------------------------------------
    function switchCatalogTab(tabKey) {
      currentCatalogTab = tabKey;
      
      // Update tab buttons while preserving i18n text!
      ['bake-stable', 'spreadable', 'extra-jam'].forEach(k => {
        const btn = document.getElementById(`tab-btn-${k}`);
        if (k === tabKey) {
          btn.className = "catalog-tab active px-3 py-2 rounded-lg font-semibold transition-all text-xs";
        } else {
          btn.className = "catalog-tab px-3 py-2 rounded-lg font-semibold transition-all text-stone-700 hover:text-[#E36527] text-xs";
        }
      });

      renderCatalogTab();
      lucide.createIcons();
    }

    function renderCatalogTab() {
      const data = catalogData[currentCatalogTab];
      if (!data) return;

      document.getElementById('cat-badge').innerText = data.badge[currentLang] || data.badge.hu;
      document.getElementById('cat-title').innerText = data.title[currentLang] || data.title.hu;
      document.getElementById('cat-subtitle').innerText = data.subtitle[currentLang] || data.subtitle.hu;
      document.getElementById('cat-desc').innerText = data.desc[currentLang] || data.desc.hu;

      // Apps list with localized strings
      const appsContainer = document.getElementById('cat-apps');
      const localizedApps = data.apps[currentLang] || data.apps.hu;
      appsContainer.innerHTML = localizedApps.map(app => `
        <span class="px-2.5 py-1 rounded-md text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">${app}</span>
      `).join('');

      // Specs summary with localized labels & values
      const specsContainer = document.getElementById('cat-specs');
      const heatLabel = currentLang === 'de' ? 'HITZESTABILITÄT' : currentLang === 'en' ? 'HEAT STABILITY' : 'HŐTŰRÉS';
      const brixLabel = currentLang === 'de' ? 'TROCKENSUBSTANZ' : currentLang === 'en' ? 'DRY MATTER' : 'SZÁRAZANYAG';
      const packLabel = currentLang === 'de' ? 'GEBINDE' : currentLang === 'en' ? 'PACKAGING' : 'KISZERELÉS';

      const heatVal = typeof data.specs.heat === 'object' ? (data.specs.heat[currentLang] || data.specs.heat.hu) : data.specs.heat;
      const packVal = typeof data.specs.pack === 'object' ? (data.specs.pack[currentLang] || data.specs.pack.hu) : data.specs.pack;

      specsContainer.innerHTML = `
        <div>
          <div class="text-[10px] text-stone-500 uppercase">${heatLabel}</div>
          <div class="font-bold text-emerald-700 text-sm mt-0.5">${heatVal}</div>
        </div>
        <div>
          <div class="text-[10px] text-stone-500 uppercase">${brixLabel}</div>
          <div class="font-bold text-stone-900 text-sm mt-0.5">${data.specs.brix}</div>
        </div>
        <div>
          <div class="text-[10px] text-stone-500 uppercase">${packLabel}</div>
          <div class="font-bold text-stone-900 text-sm mt-0.5">${packVal}</div>
        </div>
      `;

      // Image
      const img = document.getElementById('cat-image');
      img.src = data.image;
      const captionEl = document.getElementById('cat-img-caption');
      if (captionEl) captionEl.innerText = data.caption[currentLang] || data.caption.hu;

      // TDS button click
      const tdsBtn = document.getElementById('cat-tds-btn');
      tdsBtn.onclick = () => openTdsModal(data.tdsIndex);

      // Category sample request button click
      const sampleBtn = document.getElementById('cat-sample-btn');
      sampleBtn.onclick = () => selectProductAndScroll(data.productKey);
    }

    // ---------------------------------------------------------------------------
    // PRODUCT MATRIX RENDERER
    // ---------------------------------------------------------------------------
    function renderProducts() {
      const container = document.getElementById('product-list');
      if (!container) return;

      container.innerHTML = products.map((p, idx) => {
        const packVal = typeof p.pack === 'object' ? (p.pack[currentLang] || p.pack.hu) : p.pack;
        const heatVal = typeof p.specs.heat === 'object' ? (p.specs.heat[currentLang] || p.specs.heat.hu) : p.specs.heat;
        const tdsLabel = currentLang === 'hu' ? 'TDS Adatlap' : currentLang === 'de' ? 'TDS Datenblatt' : 'TDS Sheet';
        const sampleLabel = currentLang === 'hu' ? 'Mintakérés' : currentLang === 'de' ? 'Muster' : 'Sample';
        const heatTitle = currentLang === 'de' ? 'Hitzestabilität' : currentLang === 'en' ? 'Heat resistance' : 'Hőtűrés';

        return `
        <div class="rounded-2xl border p-6 bg-white flex flex-col justify-between transition-all hover:shadow-md hover:border-[#E36527]/40" style="border-color: var(--sv-border);">
          <div class="space-y-3">
            
            <div class="flex items-center justify-between flex-wrap gap-1.5">
              <span class="text-[10px] font-mono-spec font-bold px-2 py-0.5 rounded border tracking-wider uppercase"
                    style="background-color: rgba(95, 33, 37, 0.05); color: var(--sv-burgundy); border-color: var(--sv-border);">
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
              <i data-lucide="file-text" class="w-3.5 h-3.5 text-[#E36527]"></i>
              <span>${tdsLabel}</span>
            </button>

            <button onclick="selectProductAndScroll('${p.id}')" 
                    class="text-xs font-semibold font-mono-spec text-[#E36527] hover:underline flex items-center gap-1">
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
          pilotTitle: "Ipari Próbagyártási Paritás:",
          pilotBody: "A fenti műszaki specifikáció kiindulási referencia. Egyedi gyártósorokhoz (hőfok, sütési idő, viszkozitás) móri laboratóriumunk díjmentesen elvégzi a finomhangolást.",
          cta: "Minta Igénylése Ebből a Termékből",
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
          pilotTitle: "Industrial Pilot Batch Note:",
          pilotBody: "The above technical data serves as standard baseline. Our Mór laboratory provides complimentary fine-tuning tailored to your specific line parameters (temperature, oven dwell time, shear viscosity).",
          cta: "Request Sample for This Product",
          close: "Close"
        },
        de: {
          code: "Artikelnummer",
          pack: "Gebinde",
          labTitle: "PHYSIKO-CHEMISCHE LABORWERTE",
          brix: "Refraktometrischer Brix:",
          ph: "pH-Wert (20°C):",
          heat: "Hitzestabilität:",
          shelf: "Mindesthaltbarkeit:",
          slice: "Schneidbarkeit & Viskosität:",
          microTitle: "MIKROBIOLOGIE & ALLERGENSTATUS",
          microBody: "Gesamtkeimzahl: < 1000 KBE/g • Hefe & Schimmel: < 100 KBE/g • Salmonella: Negativ/25g • Glutenfrei, Vegan, Natürliche Farbstoffe.",
          pilotTitle: "Betrieblicher Testback-Hinweis:",
          pilotBody: "Die obigen Laborwerte dienen als Standardreferenz. Unser Werk in Mór passt Viskosität, Backzeit und Hitzestabilität kostenfrei an Ihre spezifische Produktionslinie an.",
          cta: "Muster für dieses Produkt anfordern",
          close: "Schließen"
        }
      }[currentLang] || labels.hu;

      content.innerHTML = `
        <div class="space-y-6">
          
          <div class="border-b pb-4">
            <div class="flex items-center gap-2 text-xs font-mono-spec text-[#E36527] font-semibold uppercase">
              <span>${currentLang === 'de' ? 'SUN VALLEY ZRT. • WERK MÓR' : currentLang === 'en' ? 'SUN VALLEY ZRT. • MÓR PLANT' : 'SUN VALLEY ZRT. • MÓRI GYÁR'}</span>
              <span>•</span>
              <span>${currentLang === 'de' ? 'TECHNISCHES DATENBLATT #TDS-2026' : currentLang === 'en' ? 'TECHNICAL DATA SHEET #TDS-2026' : 'MŰSZAKI ADATLAP #TDS-2026'}</span>
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
              <i data-lucide="package-check" class="w-4 h-4"></i>
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
    // HIGH CONVERSION FUNNEL: SELECT PRODUCT AND SCROLL
    // ---------------------------------------------------------------------------
    function selectProductAndScroll(productId) {
      closeTdsModal();
      
      const selectElem = document.getElementById('sample-product');
      if (selectElem && productId) {
        // Map any aliases
        const validOptions = [...selectElem.options].map(o => o.value);
        if (validOptions.includes(productId)) {
          selectElem.value = productId;
        } else if (productId.includes('kajszi')) {
          selectElem.value = 'sutesallo-kajszi';
        } else if (productId.includes('malna')) {
          selectElem.value = 'kenheto-malna';
        } else if (productId.includes('afonya')) {
          selectElem.value = 'kenheto-afonya';
        } else if (productId.includes('meggy')) {
          selectElem.value = 'sutesallo-extra-meggy';
        } else if (productId.includes('receptura') || productId.includes('egzotik')) {
          selectElem.value = 'egyedi-receptura';
        } else {
          selectElem.value = 'sutesallo-vegyes';
        }
      }

      const formElem = document.getElementById('sample-request-form');
      if (formElem) {
        formElem.scrollIntoView({ behavior: 'smooth', block: 'center' });
        formElem.classList.add('focus-pulse');
        setTimeout(() => {
          formElem.classList.remove('focus-pulse');
        }, 3000);
      }

      // Focus on contact name input
      setTimeout(() => {
        document.getElementById('sample-name')?.focus();
      }, 500);
    }

    // Close modal on escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeTdsModal();
    });

    // Close modal on background click
    document.getElementById('tds-modal')?.addEventListener('click', (e) => {
      if (e.target.id === 'tds-modal') closeTdsModal();
    });

    // Mobile Menu Toggle
    function toggleMobileMenu() {
      const menu = document.getElementById('mobile-menu');
      menu.classList.toggle('hidden');
    }

    // Input Sanitization & Tag Stripping (XSS Prevention)
    function sanitizeInput(str) {
      if (!str) return '';
      return String(str).replace(/<[^>]*>/g, '').trim();
    }

    function clearFormErrors() {
      ['name', 'company', 'email', 'phone', 'gdpr'].forEach(field => {
        const input = document.getElementById(field === 'gdpr' ? 'form-gdpr' : `sample-${field}`);
        const err = document.getElementById(`err-${field}`);
        if (input) {
          input.classList.remove('border-red-500', 'ring-2', 'ring-red-300');
        }
        if (err) {
          err.innerText = '';
          err.classList.add('hidden');
        }
      });
    }

    function showFieldError(field, msg) {
      const input = document.getElementById(field === 'gdpr' ? 'form-gdpr' : `sample-${field}`);
      const err = document.getElementById(`err-${field}`);
      if (input) {
        input.classList.add('border-red-500', 'ring-2', 'ring-red-300');
        input.focus();
      }
      if (err) {
        err.innerText = msg;
        err.classList.remove('hidden');
      }
    }

    // Sample Form Submission with Robust B2B Validation
    function handleSampleSubmit(e) {
      e.preventDefault();
      clearFormErrors();

      const form = (e && e.target && e.target.nodeName === 'FORM') ? e.target : document.getElementById('sample-request-form');
      const formData = new FormData(form);

      const rawName = formData.get('contact_name') || '';
      const rawCompany = formData.get('company_tax_id') || '';
      const rawEmail = formData.get('email') || '';
      const rawPhone = formData.get('phone') || '';
      const gdprChecked = form.elements['gdpr_consent']?.checked;

      const name = sanitizeInput(rawName);
      const company = sanitizeInput(rawCompany);
      const email = sanitizeInput(rawEmail);
      const phone = sanitizeInput(rawPhone);

      const errMsgs = {
        hu: {
          name: "Kérjük, adja meg a nevét és pozícióját!",
          company: "Kérjük, adja meg a cégnevet és a legalább 8 jegyű adószámot (pl. 12345678-2-41)!",
          email: "Kérjük, adjon meg egy érvényes munkahelyi e-mail címet!",
          phone: "Kérjük, adjon meg egy érvényes telefonszámot (legalább 8 számjegy)!",
          gdpr: "A mintaküldéshez az adatkezelési tájékoztató elfogadása szükséges!"
        },
        en: {
          name: "Please provide your contact name and title.",
          company: "Please provide your company name and tax ID (at least 8 digits).",
          email: "Please enter a valid work email address.",
          phone: "Please enter a valid phone number (at least 8 digits).",
          gdpr: "You must accept data processing to receive trial samples."
        },
        de: {
          name: "Bitte geben Sie Ihren Namen und Ihre Position an.",
          company: "Bitte geben Sie Firmenname und Steuernummer (mind. 8 Ziffern) an.",
          email: "Bitte geben Sie eine gültige geschäftliche E-Mail-Adresse ein.",
          phone: "Bitte geben Sie eine gültige Telefonnummer an (mind. 8 Ziffern).",
          gdpr: "Für die Musterzusendung müssen Sie der Datenverarbeitung zustimmen."
        }
      }[currentLang] || {
        name: "Kérjük, adja meg a nevét és pozícióját!",
        company: "Kérjük, adja meg a cégnevet és a legalább 8 jegyű adószámot (pl. 12345678-2-41)!",
        email: "Kérjük, adjon meg egy érvényes munkahelyi e-mail címet!",
        phone: "Kérjük, adjon meg egy érvényes telefonszámot (legalább 8 számjegy)!",
        gdpr: "A mintaküldéshez az adatkezelési tájékoztató elfogadása szükséges!"
      };

      if (!name || name.length < 3) {
        showFieldError('name', errMsgs.name);
        return;
      }

      // Adószám validation: must contain at least 8 digits
      const digitsInCompany = (company.match(/\\d/g) || []).length;
      if (!company || company.length < 3 || digitsInCompany < 8) {
        showFieldError('company', errMsgs.company);
        return;
      }

      // Email validation: standard B2B email format (no HTML, valid domain)
      const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/;
      if (!email || !emailPattern.test(email)) {
        showFieldError('email', errMsgs.email);
        return;
      }

      // Phone validation: only allowed phone chars (+, digits, spaces, hyphens, parens, slashes), 8 to 16 digits
      const phonePattern = /^[+]?[0-9\\s\\-()\\/]{8,25}$/;
      const digitsInPhone = (phone.match(/\\d/g) || []).length;
      if (!phone || !phonePattern.test(phone) || digitsInPhone < 8 || digitsInPhone > 16) {
        showFieldError('phone', errMsgs.phone);
        return;
      }

      if (!gdprChecked) {
        showFieldError('gdpr', errMsgs.gdpr);
        return;
      }

      const refId = `SV-${new Date().getFullYear()}-${Math.floor(1000 + Math.random() * 9000)}`;

      const successTexts = {
        hu: `✓ Köszönjük, ${name}! (${company})\\nMintaigénylését sikeresen rögzítettük. Referenciaszám: [${refId}]. Móri műszaki tanácsadónk 24 órán belül felveszi Önnel a kapcsolatot a próbasütési tétel logisztikájával kapcsolatban.`,
        en: `✓ Thank you, ${name}! (${company})\\nYour pilot batch sample request has been received. Reference ID: [${refId}]. Our Mór plant food technologist will contact you within 24 hours regarding test shipment logistics.`,
        de: `✓ Vielen Dank, ${name}! (${company})\\nIhre Probemuster-Anforderung wurde erfolgreich registriert. Referenznummer: [${refId}]. Unser Bäckereitechnologe wird sich innerhalb von 24 Stunden bezüglich des Testback-Musters mit Ihnen in Verbindung setzen.`
      };

      const msg = document.getElementById('form-success-message');
      msg.textContent = successTexts[currentLang] || successTexts.hu;
      msg.classList.remove('hidden');
      form.reset();

      setTimeout(() => {
        msg.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }, 100);
    }

    // Initial boot
    document.addEventListener('DOMContentLoaded', () => {
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

    with open(OUTPUT_V2, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {OUTPUT_V2} ({len(content)} characters)")

    with open(OUTPUT_INDEX, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {OUTPUT_INDEX} ({len(content)} characters)")

if __name__ == "__main__":
    main()
