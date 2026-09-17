import os

HTML_CONTENT = """<!DOCTYPE html>
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

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Syne:wght@600;700;800&display=swap" rel="stylesheet">

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

    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: var(--sv-paper-cream);
      color: var(--sv-text-main);
    }

    .font-syne {
      font-family: 'Syne', 'Plus Jakarta Sans', sans-serif;
      letter-spacing: -0.025em;
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
  </style>
</head>
<body class="bg-tech-grid min-h-screen flex flex-col antialiased selection:bg-[#E36527] selection:text-white">

  <!-- ========================================================================= -->
  <!-- TOP EMERGENCY / DIRECT CONTACT BAR                                       -->
  <!-- ========================================================================= -->
  <div class="border-b text-xs font-mono-spec py-1.5 px-3.5 sm:px-8 transition-colors"
       style="background-color: var(--sv-burgundy-dark); color: #F5F2EE; border-color: rgba(255,255,255,0.1);">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-2">
      <div class="flex items-center gap-3">
        <span class="inline-flex items-center gap-1.5 text-[#E36527] font-semibold uppercase tracking-wider text-[11px] sm:text-xs">
          <span class="w-2 h-2 rounded-full bg-[#E36527] animate-pulse"></span>
          <span data-i18n="topbar_scale">Ipari Gyártóbázis: Mór (Major u. 3.)</span>
        </span>
        <span class="hidden md:inline text-white/40">|</span>
        <span class="hidden md:inline text-white/80" data-i18n="topbar_capacity">Éves kapacitás: 1,1–1,3 Mrd Ft forgalom</span>
        <span class="hidden lg:inline text-white/40">|</span>
        <span class="hidden lg:inline text-[#FBBB9C]" data-i18n="topbar_rating">AA+ Pénzügyi Minősítés</span>
      </div>
      <div class="flex items-center gap-3 sm:gap-4 text-[11px] sm:text-xs">
        <a href="tel:+36308998548" class="hover:text-[#FBBB9C] transition-colors flex items-center gap-1.5 font-semibold">
          <i data-lucide="phone" class="w-3.5 h-3.5 text-[#E36527]"></i>
          <span>+36 30 899 8548</span>
        </a>
        <span class="hidden sm:inline text-white/40">|</span>
        <a href="mailto:vecsei.andras@sunvalley.hu" class="hidden sm:flex hover:text-[#FBBB9C] transition-colors items-center gap-1.5">
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
          style="background-color: rgba(245, 242, 238, 0.95); border-color: var(--sv-border);">
    <div class="max-w-7xl mx-auto px-3.5 sm:px-8 py-3 sm:py-3.5 flex items-center justify-between gap-2 sm:gap-4">
      
      <!-- Brand Crest & Identity (Authentic Sun Valley Logo) -->
      <a href="#" class="flex items-center gap-3 group shrink-0">
        <img src="assets/sun-valley-logo.png" alt="Sun Valley Zrt. Logo" class="h-10 sm:h-11 w-auto object-contain transition-transform group-hover:scale-105">
        <div>
          <div class="font-syne font-bold text-base sm:text-lg tracking-tight leading-none" style="color: var(--sv-burgundy);">
            SUN VALLEY <span class="text-[11px] sm:text-xs font-mono-spec font-medium px-1.5 py-0.5 rounded ml-1" style="background-color: rgba(95,33,37,0.08); color: var(--sv-burgundy);">ZRT.</span>
          </div>
          <p class="text-[10px] font-mono-spec tracking-wider uppercase hidden md:block mt-0.5" style="color: var(--sv-text-muted);" data-i18n="tagline">
            Ipari Gyümölcstechnológia • Est. 2009
          </p>
        </div>
      </a>

      <!-- Desktop Nav Links -->
      <nav class="hidden lg:flex items-center gap-4 xl:gap-6 text-xs xl:text-sm font-semibold">
        <a href="#katalogus" class="hover:text-[#E36527] transition-colors py-1 relative group" data-i18n="nav_catalog">
          Gasztro-Katalógus
          <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#E36527] transition-all group-hover:w-full"></span>
        </a>
        <a href="#termekek" class="hover:text-[#E36527] transition-colors py-1 relative group" data-i18n="nav_products">
          Termékek & TDS
          <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#E36527] transition-all group-hover:w-full"></span>
        </a>
        <a href="#technologia" class="hover:text-[#E36527] transition-colors py-1 relative group" data-i18n="nav_tech">
          Sütésállóság (200°C)
          <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#E36527] transition-all group-hover:w-full"></span>
        </a>
        <a href="#egyedi-fejlesztes" class="hover:text-[#E36527] transition-colors py-1 relative group" data-i18n="nav_rd">
          Receptúra-fejlesztés
          <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#E36527] transition-all group-hover:w-full"></span>
        </a>
        <a href="#prospektus" class="hover:text-[#E36527] transition-colors py-1 relative group" data-i18n="nav_prospectus">
          Prospektus
          <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#E36527] transition-all group-hover:w-full"></span>
        </a>
        <a href="#disztribucio" class="hover:text-[#E36527] transition-colors py-1 relative group" data-i18n="nav_distribution">
          Nagykereskedelmi Hálózat
          <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#E36527] transition-all group-hover:w-full"></span>
        </a>
        <a href="#kapcsolat" class="hover:text-[#E36527] transition-colors py-1 relative group" data-i18n="nav_contact">
          Gyártóüzem
          <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-[#E36527] transition-all group-hover:w-full"></span>
        </a>
      </nav>

      <!-- Right Controls: Language Switcher & Direct Call CTA -->
      <div class="flex items-center gap-2 sm:gap-3">
        
        <!-- TRILINGUAL SWITCHER (HU / EN / DE) -->
        <div class="flex items-center p-0.5 rounded-lg border font-mono-spec text-xs shrink-0"
             style="background-color: var(--sv-surface); border-color: var(--sv-border);">
          <button onclick="setLanguage('hu')" id="lang-hu" class="px-1.5 sm:px-2 py-0.5 sm:py-1 rounded font-bold transition-all bg-[#5F2125] text-white shadow-sm text-[11px] sm:text-xs">
            HU
          </button>
          <button onclick="setLanguage('en')" id="lang-en" class="px-1.5 sm:px-2 py-0.5 sm:py-1 rounded font-medium text-stone-600 hover:text-[#E36527] transition-all text-[11px] sm:text-xs">
            EN
          </button>
          <button onclick="setLanguage('de')" id="lang-de" class="px-1.5 sm:px-2 py-0.5 sm:py-1 rounded font-medium text-stone-600 hover:text-[#E36527] transition-all text-[11px] sm:text-xs">
            DE
          </button>
        </div>

        <!-- Direct Sample Request Button -->
        <a href="#mintakeres" 
           class="hidden sm:inline-flex items-center gap-2 px-4 py-2 rounded-lg font-semibold text-xs transition-all transform active:scale-95 shadow-sm"
           style="background-color: var(--sv-orange); color: white;">
          <i data-lucide="package-check" class="w-3.5 h-3.5"></i>
          <span data-i18n="btn_sample_short">Próbagyártási Minta</span>
        </a>

        <!-- Mobile Menu Toggle -->
        <button onclick="toggleMobileMenu()" class="lg:hidden p-1.5 sm:p-2 rounded-lg border shrink-0" style="border-color: var(--sv-border);">
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
        <a href="#egyedi-fejlesztes" onclick="toggleMobileMenu()" class="py-1 text-stone-800 hover:text-[#E36527]" data-i18n="nav_rd">Receptúra-fejlesztés</a>
        <a href="#prospektus" onclick="toggleMobileMenu()" class="py-1 text-stone-800 hover:text-[#E36527]" data-i18n="nav_prospectus">Prospektus</a>
        <a href="#disztribucio" onclick="toggleMobileMenu()" class="py-1 text-stone-800 hover:text-[#E36527]" data-i18n="nav_distribution">Nagykereskedelmi Hálózat</a>
        <a href="#kapcsolat" onclick="toggleMobileMenu()" class="py-1 text-stone-800 hover:text-[#E36527]" data-i18n="nav_contact">Gyártóüzem & Elérhetőség</a>
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
          <h1 class="font-syne font-extrabold text-[1.35rem] xs:text-2xl sm:text-4xl md:text-5xl lg:text-[2.6rem] xl:text-[3.2rem] tracking-tight leading-[1.2] pb-1"
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
          <div class="pt-2 flex flex-wrap items-center gap-3 sm:gap-4">
            <a href="#katalogus" 
               class="inline-flex items-center gap-2 px-6 py-3.5 rounded-lg font-semibold text-sm shadow-md hover:shadow-lg transition-all transform active:scale-95"
               style="background-color: var(--sv-burgundy); color: #F5F2EE;">
              <i data-lucide="book-open" class="w-4 h-4 text-[#E36527]"></i>
              <span data-i18n="hero_cta_catalog">Lapozható Gasztro-Katalógus</span>
            </a>

            <a href="#mintakeres" 
               class="inline-flex items-center gap-2 px-6 py-3.5 rounded-lg font-semibold text-sm transition-all transform active:scale-95 shadow"
               style="background-color: var(--sv-orange); color: white;">
              <i data-lucide="package-check" class="w-4 h-4"></i>
              <span data-i18n="hero_cta_sample">Üzemi Tesztminta Kérése</span>
            </a>

            <a href="assets/Sun_Valley_B2B_Prospektus_V1_4.pptx" download
               class="inline-flex items-center gap-2 px-4 py-3.5 rounded-lg font-semibold text-xs font-mono-spec border transition-all hover:bg-white"
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
              <img src="assets/apricot-hero.png" alt="Ipari kajszibarack gyümölcstöltelék hosszmetszet" 
                   class="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-500">
              <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent"></div>
              
              <!-- Floating QC Badge -->
              <div class="absolute top-4 left-4 inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-[11px] font-mono-spec font-bold tracking-wider uppercase text-white shadow-sm"
                   style="background-color: var(--sv-burgundy); border: 1px solid var(--sv-gold);">
                <i data-lucide="shield-check" class="w-3.5 h-3.5 text-[#E36527]"></i>
                <span>THERMO-STABLE • 200°C+</span>
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
                <span>MÓR PLANT QC REF #SV-2026</span>
                <span class="text-[#E36527] font-semibold">DIRECT FACTORY SUPPLY</span>
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
          <div class="font-syne font-extrabold text-2xl sm:text-3xl text-[#FBBB9C]">1,1 – 1,3 Mrd Ft</div>
          <p class="text-xs text-white/80 font-mono-spec" data-i18n="stat_revenue">Éves árbevétel (Stabil tőkeerő)</p>
        </div>

        <!-- Stat 2 -->
        <div class="space-y-1 md:border-l md:pl-6 border-white/10">
          <div class="font-syne font-extrabold text-2xl sm:text-3xl text-white">AA+</div>
          <p class="text-xs text-white/80 font-mono-spec" data-i18n="stat_rating">Pénzügyi minősítés (Adósságmentes)</p>
        </div>

        <!-- Stat 3 -->
        <div class="space-y-1 md:border-l md:pl-6 border-white/10">
          <div class="font-syne font-extrabold text-2xl sm:text-3xl text-[#E36527]">15+ Év</div>
          <p class="text-xs text-white/80 font-mono-spec" data-i18n="stat_heritage">Gyümölcsfeldolgozói múlt (Vitamór bázis)</p>
        </div>

        <!-- Stat 4 -->
        <div class="space-y-1 md:border-l md:pl-6 border-white/10">
          <div class="font-syne font-extrabold text-2xl sm:text-3xl text-white">VEP Díjas</div>
          <p class="text-xs text-white/80 font-mono-spec" data-i18n="stat_energy">Energiatudatos Móri Gyártelep</p>
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
      <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-10">
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

        <!-- Catalog Tab Switcher Buttons -->
        <div class="flex items-center gap-2 p-1.5 rounded-xl border bg-white font-mono-spec text-xs shrink-0 self-start md:self-end shadow-sm"
             style="border-color: var(--sv-border);">
          <button onclick="switchCatalogTab('bake-stable')" id="tab-btn-bake-stable" 
                  class="catalog-tab active px-3 py-2 rounded-lg font-semibold transition-all text-xs">
            1. Sütésálló Töltelékek
          </button>
          <button onclick="switchCatalogTab('spreadable')" id="tab-btn-spreadable" 
                  class="catalog-tab px-3 py-2 rounded-lg font-semibold transition-all text-stone-700 hover:text-[#E36527] text-xs">
            2. Kenhető Készítmények
          </button>
          <button onclick="switchCatalogTab('extra-jam')" id="tab-btn-extra-jam" 
                  class="catalog-tab px-3 py-2 rounded-lg font-semibold transition-all text-stone-700 hover:text-[#E36527] text-xs">
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
                <span class="px-2.5 py-1 rounded-md text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">Sárgabarackos bukta</span>
                <span class="px-2.5 py-1 rounded-md text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">Lekváros papucs</span>
                <span class="px-2.5 py-1 rounded-md text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">Rácsos linzer</span>
                <span class="px-2.5 py-1 rounded-md text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">Leveles táskák</span>
                <span class="px-2.5 py-1 rounded-md text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">Piték & derelyék</span>
              </div>
            </div>

            <!-- Key specs summary -->
            <div id="cat-specs" class="grid grid-cols-3 gap-3 p-4 rounded-xl border bg-stone-50 font-mono-spec text-xs" style="border-color: var(--sv-border-light);">
              <div>
                <div class="text-[10px] text-stone-500 uppercase">Hőtűrés</div>
                <div class="font-bold text-emerald-700 text-sm mt-0.5">≥ 200 °C</div>
              </div>
              <div>
                <div class="text-[10px] text-stone-500 uppercase">Szárazanyag</div>
                <div class="font-bold text-stone-900 text-sm mt-0.5">58–64° Brix</div>
              </div>
              <div>
                <div class="text-[10px] text-stone-500 uppercase">Kiszerelés</div>
                <div class="font-bold text-stone-900 text-sm mt-0.5">10 kg karton</div>
              </div>
            </div>

            <!-- Action buttons -->
            <div class="flex flex-wrap items-center gap-3 pt-2">
              <button id="cat-tds-btn" onclick="openTdsModal(0)" 
                      class="inline-flex items-center gap-2 px-5 py-2.5 rounded-lg text-xs font-semibold font-mono-spec transition-all shadow"
                      style="background-color: var(--sv-burgundy); color: white;">
                <i data-lucide="file-spreadsheet" class="w-3.5 h-3.5 text-[#E36527]"></i>
                <span data-i18n="btn_view_category_tds">TDS Adatlap Megtekintése</span>
              </button>

              <a href="#mintakeres" 
                 class="inline-flex items-center gap-2 px-5 py-2.5 rounded-lg text-xs font-semibold font-mono-spec transition-all border hover:bg-stone-50"
                 style="border-color: var(--sv-orange); color: var(--sv-orange);">
                <i data-lucide="package-check" class="w-3.5 h-3.5"></i>
                <span data-i18n="btn_request_cat_sample">Minta Kérése Ebből a Kategóriából</span>
              </a>
            </div>

          </div>

          <!-- Right Image Showcase (Span 6) -->
          <div class="lg:col-span-6">
            <div class="relative rounded-2xl overflow-hidden border shadow-md bg-stone-100" style="border-color: var(--sv-border-light);">
              <img id="cat-image" src="assets/catalog-bake-stable.png" alt="Sütésálló gyümölcstöltelék gasztronómiai bemutató" 
                   class="w-full h-80 sm:h-96 object-cover object-center transition-all duration-500">
              <div class="absolute bottom-0 inset-x-0 bg-gradient-to-t from-black/80 via-black/40 to-transparent p-4 text-white text-xs font-mono-spec flex items-center justify-between">
                <span id="cat-img-caption">Üzemi próbasütési minta • 10 kg tömbösített kiszerelés</span>
                <span class="text-[#FBBB9C] font-semibold">MÓR QC APPROVED</span>
              </div>
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
            <img src="assets/familiar-jams-group.png" alt="Hét ismerős hazai gyümölcsíz Sun Valley" 
                 class="w-full h-80 sm:h-96 object-cover object-center group-hover:scale-105 transition-transform duration-500">
            <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent"></div>
            <div class="absolute bottom-4 left-4 right-4 text-white font-mono-spec text-xs">
              <span class="text-[#FBBB9C] uppercase font-bold text-[10px]">HAZAI GYÜMÖLCSBÁZIS</span>
              <div class="font-syne font-bold text-lg text-white">7 Alapvető Pékipari Gyümölcsíz</div>
            </div>
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

          <!-- 7 Flavors Grid -->
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-2 font-mono-spec text-xs">
            <div class="p-3 rounded-xl border bg-stone-50 flex items-center gap-2" style="border-color: var(--sv-border-light);">
              <span class="w-2.5 h-2.5 rounded-full bg-amber-500 shrink-0"></span>
              <span class="font-bold text-stone-800">Sárgabarack</span>
            </div>
            <div class="p-3 rounded-xl border bg-stone-50 flex items-center gap-2" style="border-color: var(--sv-border-light);">
              <span class="w-2.5 h-2.5 rounded-full bg-indigo-900 shrink-0"></span>
              <span class="font-bold text-stone-800">Szilva</span>
            </div>
            <div class="p-3 rounded-xl border bg-stone-50 flex items-center gap-2" style="border-color: var(--sv-border-light);">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-600 shrink-0"></span>
              <span class="font-bold text-stone-800">Alma</span>
            </div>
            <div class="p-3 rounded-xl border bg-stone-50 flex items-center gap-2" style="border-color: var(--sv-border-light);">
              <span class="w-2.5 h-2.5 rounded-full bg-rose-800 shrink-0"></span>
              <span class="font-bold text-stone-800">Meggy</span>
            </div>
            <div class="p-3 rounded-xl border bg-stone-50 flex items-center gap-2" style="border-color: var(--sv-border-light);">
              <span class="w-2.5 h-2.5 rounded-full bg-pink-600 shrink-0"></span>
              <span class="font-bold text-stone-800">Málna</span>
            </div>
            <div class="p-3 rounded-xl border bg-stone-50 flex items-center gap-2" style="border-color: var(--sv-border-light);">
              <span class="w-2.5 h-2.5 rounded-full bg-purple-900 shrink-0"></span>
              <span class="font-bold text-stone-800">Áfonya</span>
            </div>
            <div class="p-3 rounded-xl border bg-stone-50 flex items-center gap-2 col-span-2 sm:col-span-2" style="border-color: var(--sv-border-light);">
              <span class="w-2.5 h-2.5 rounded-full bg-red-700 shrink-0"></span>
              <span class="font-bold text-stone-800">Klasszikus Vegyes Gyümölcs</span>
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
              <span>Mangó & Maracuja</span>
            </div>
            <div class="p-3 rounded-xl border bg-amber-50/50 border-amber-200 text-stone-800 font-semibold flex items-center gap-2">
              <i data-lucide="sparkles" class="w-3.5 h-3.5 text-[#E36527]"></i>
              <span>Ananász & Kivi</span>
            </div>
            <div class="p-3 rounded-xl border bg-amber-50/50 border-amber-200 text-stone-800 font-semibold flex items-center gap-2 col-span-2 sm:col-span-1">
              <i data-lucide="sparkles" class="w-3.5 h-3.5 text-[#E36527]"></i>
              <span>Citrus & Narancs</span>
            </div>
          </div>

          <p class="text-xs text-stone-500 font-mono-spec" data-i18n="exotic_note">
            * Az egzotikus receptúrákat ipari próbagyártás és technológiai egyeztetés alapján véglegesítjük a partner saját gépsoraira.
          </p>
        </div>

        <!-- Right Visual (Span 5) -->
        <div class="lg:col-span-5">
          <div class="rounded-2xl overflow-hidden border shadow-lg relative bg-stone-50 group" style="border-color: var(--sv-border);">
            <img src="assets/exotic-fruits-fresh-v2.png" alt="Egzotikus gyümölcsök alapanyag Sun Valley" 
                 class="w-full h-80 sm:h-96 object-cover object-center group-hover:scale-105 transition-transform duration-500">
            <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent"></div>
            <div class="absolute bottom-4 left-4 right-4 text-white font-mono-spec text-xs">
              <span class="text-[#FBBB9C] uppercase font-bold text-[10px]">R&D LABORATÓRIUM</span>
              <div class="font-syne font-bold text-lg text-white">Egyedi Gyümölcskombinációk</div>
            </div>
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
              <img src="assets/technology-baking-pastry-v2.png" alt="Sütésállósági teszt péksütemény" class="w-full h-full object-cover">
              <div class="absolute top-3 left-3 bg-[#5F2125] text-white text-[10px] font-mono-spec font-bold px-2 py-0.5 rounded">
                180 °C – 220 °C
              </div>
            </div>
            <div class="p-5 space-y-2">
              <h3 class="font-syne font-bold text-lg text-stone-900" data-i18n="tech_card1_title">Garantált Sütésállóság</h3>
              <p class="text-xs text-stone-600 leading-relaxed" data-i18n="tech_card1_desc">
                200 °C felett sem forr ki a süteményből, nem ég le a tepsire, és megőrzi térfogatát a tésztában szinerézis (vízkiválás) nélkül.
              </p>
            </div>
          </div>
          <div class="p-5 pt-0 border-t mt-4 text-[11px] font-mono-spec text-[#E36527] font-semibold" style="border-color: var(--sv-border-light);">
            ✓ Zéró tepsileégés
          </div>
        </div>

        <!-- Tech Card 2: Freezing Stability -->
        <div class="rounded-2xl border bg-white overflow-hidden shadow-sm hover:shadow-md transition-all flex flex-col justify-between"
             style="border-color: var(--sv-border);">
          <div>
            <div class="h-48 overflow-hidden bg-stone-100 relative">
              <img src="assets/technology-freezing-cake.png" alt="Fagyasztásálló gyümölcstöltelék" class="w-full h-full object-cover">
              <div class="absolute top-3 left-3 bg-[#2D3628] text-white text-[10px] font-mono-spec font-bold px-2 py-0.5 rounded">
                FREEZE / THAW STABLE
              </div>
            </div>
            <div class="p-5 space-y-2">
              <h3 class="font-syne font-bold text-lg text-stone-900" data-i18n="tech_card2_title">Fagyasztásállóság</h3>
              <p class="text-xs text-stone-600 leading-relaxed" data-i18n="tech_card2_desc">
                Fagyasztott félkész és fagyasztva tárolt késztermékekhez kifejlesztve. Felengedéskor nem enged levet, nem áztatja el a tésztát.
              </p>
            </div>
          </div>
          <div class="p-5 pt-0 border-t mt-4 text-[11px] font-mono-spec text-[#2D3628] font-semibold" style="border-color: var(--sv-border-light);">
            ✓ Fagyasztási stabilitás
          </div>
        </div>

        <!-- Tech Card 3: Pumpability & Dosing -->
        <div class="rounded-2xl border bg-white overflow-hidden shadow-sm hover:shadow-md transition-all flex flex-col justify-between"
             style="border-color: var(--sv-border);">
          <div>
            <div class="h-48 overflow-hidden bg-stone-100 relative">
              <img src="assets/technology-pumpable-doughnut.png" alt="Gépi pumpálható töltelék fánk injektálás" class="w-full h-full object-cover">
              <div class="absolute top-3 left-3 bg-[#E36527] text-white text-[10px] font-mono-spec font-bold px-2 py-0.5 rounded">
                AUTOMATED DOSING
              </div>
            </div>
            <div class="p-5 space-y-2">
              <h3 class="font-syne font-bold text-lg text-stone-900" data-i18n="tech_card3_title">Gépi Tölthetőség & Pumpálás</h3>
              <p class="text-xs text-stone-600 leading-relaxed" data-i18n="tech_card3_desc">
                A kézi kenéstől a nagyteljesítményű automata tüskés injektálósorokig (fánkok, croissant-ok) állandó, nyírásra stabil viszkozitás.
              </p>
            </div>
          </div>
          <div class="p-5 pt-0 border-t mt-4 text-[11px] font-mono-spec text-[#5F2125] font-semibold" style="border-color: var(--sv-border-light);">
            ✓ Nem dugul el a tű
          </div>
        </div>

        <!-- Tech Card 4: Packaging Scale & Slicing -->
        <div class="rounded-2xl border bg-white overflow-hidden shadow-sm hover:shadow-md transition-all flex flex-col justify-between"
             style="border-color: var(--sv-border);">
          <div>
            <div class="h-48 overflow-hidden bg-stone-100 relative">
              <img src="assets/custom-recipe-jam-sizes.png" alt="Ipari kiszerelések vödörtől hordóig" class="w-full h-full object-cover">
              <div class="absolute top-3 left-3 bg-stone-800 text-white text-[10px] font-mono-spec font-bold px-2 py-0.5 rounded">
                5 KG • 10 KG • 200 KG
              </div>
            </div>
            <div class="p-5 space-y-2">
              <h3 class="font-syne font-bold text-lg text-stone-900" data-i18n="tech_card4_title">Kis Szériától Ipari Léptékig</h3>
              <p class="text-xs text-stone-600 leading-relaxed" data-i18n="tech_card4_desc">
                5 kg-os vödörben a cukrászatoknak, 10 kg-os szeletelhető kartontömbökben kenyérgyáraknak, vagy 200 kg-os hordókban nagyüzemeknek.
              </p>
            </div>
          </div>
          <div class="p-5 pt-0 border-t mt-4 text-[11px] font-mono-spec text-emerald-700 font-semibold" style="border-color: var(--sv-border-light);">
            ✓ Raklapos paritás
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
        <h2 class="font-syne font-bold text-3xl sm:text-4xl text-stone-900 leading-snug" data-i18n="rd_section_title">
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
          <h3 class="font-syne font-bold text-xl text-stone-900" data-i18n="rd_step1_title">
            Az Igény Megismerése
          </h3>
          <p class="text-xs sm:text-sm text-stone-600 leading-relaxed" data-i18n="rd_step1_desc">
            Felhasználás, ízvilág, elvárt gyümölcstartalom, állag, sütési hőmérséklet (180–220 °C) és a gépsor adagolási feltételeinek pontos felmérése.
          </p>
          <div class="pt-2 font-mono-spec text-[11px] text-stone-400 border-t" style="border-color: var(--sv-border-light);">
            Audit & Paraméterezés
          </div>
        </div>

        <!-- Step 2 -->
        <div class="rounded-2xl border bg-white p-6 sm:p-8 space-y-4 shadow-sm" style="border-color: var(--sv-border);">
          <div class="w-12 h-12 rounded-xl flex items-center justify-center font-mono-spec font-bold text-lg text-white"
               style="background-color: var(--sv-orange);">
            02
          </div>
          <h3 class="font-syne font-bold text-xl text-stone-900" data-i18n="rd_step2_title">
            Receptúra & Üzemi Próba
          </h3>
          <p class="text-xs sm:text-sm text-stone-600 leading-relaxed" data-i18n="rd_step2_desc">
            Laboratóriumi minta készítése, majd 5–10 kg-os üzemi próbagyártási minta kiküldése a partner saját gyártósorán történő sütési validációra.
          </p>
          <div class="pt-2 font-mono-spec text-[11px] text-stone-400 border-t" style="border-color: var(--sv-border-light);">
            Tesztminta & Visszacsatolás
          </div>
        </div>

        <!-- Step 3 -->
        <div class="rounded-2xl border bg-white p-6 sm:p-8 space-y-4 shadow-sm" style="border-color: var(--sv-border);">
          <div class="w-12 h-12 rounded-xl flex items-center justify-center font-mono-spec font-bold text-lg text-white"
               style="background-color: var(--sv-green-dark);">
            03
          </div>
          <h3 class="font-syne font-bold text-xl text-stone-900" data-i18n="rd_step3_title">
            Gyártásra Hangolva
          </h3>
          <p class="text-xs sm:text-sm text-stone-600 leading-relaxed" data-i18n="rd_step3_desc">
            A végleges műszaki specifikáció (TDS) rögzítése, a csomagolás (vödör, kartontömb, hordó) kiválasztása és a stabil ütemezett raklapos szállítás elindítása.
          </p>
          <div class="pt-2 font-mono-spec text-[11px] text-stone-400 border-t" style="border-color: var(--sv-border-light);">
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
        <!-- Injected via JavaScript with i18n support -->
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
            <span>Formátum: Microsoft PowerPoint (.pptx)</span>
            <span>•</span>
            <span>Méret: ~11,1 MB</span>
            <span>•</span>
            <span>Verzió: V1.4 (2026)</span>
          </div>
        </div>

        <div class="shrink-0">
          <a href="assets/Sun_Valley_B2B_Prospektus_V1_4.pptx" download
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

      <!-- Qualified Form Container -->
      <form id="sample-request-form" onsubmit="handleSampleSubmit(event)" class="rounded-3xl border p-6 sm:p-10 shadow-lg space-y-6"
            style="background-color: var(--sv-paper-cream); border-color: var(--sv-border);">
        
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
          
          <div>
            <label class="block text-xs font-mono-spec font-bold text-stone-700 uppercase mb-1.5" data-i18n="form_name_label">
              Kapcsolattartó Neve & Pozíciója *
            </label>
            <input type="text" required placeholder="pl. Kovács Péter (Üzemvezető / Technológus)" 
                   class="w-full px-4 py-3 rounded-xl border bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[#E36527] transition-all"
                   style="border-color: var(--sv-border-light);">
          </div>

          <div>
            <label class="block text-xs font-mono-spec font-bold text-stone-700 uppercase mb-1.5" data-i18n="form_company_label">
              Cégnév & Adószám * (B2B szűrés)
            </label>
            <input type="text" required placeholder="pl. Minta Pékség Kft. • 12345678-2-41" 
                   class="w-full px-4 py-3 rounded-xl border bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[#E36527] transition-all"
                   style="border-color: var(--sv-border-light);">
          </div>

          <div>
            <label class="block text-xs font-mono-spec font-bold text-stone-700 uppercase mb-1.5" data-i18n="form_email_label">
              Munkahelyi E-mail Cím *
            </label>
            <input type="email" required placeholder="technologia@pekseg.hu" 
                   class="w-full px-4 py-3 rounded-xl border bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[#E36527] transition-all"
                   style="border-color: var(--sv-border-light);">
          </div>

          <div>
            <label class="block text-xs font-mono-spec font-bold text-stone-700 uppercase mb-1.5" data-i18n="form_phone_label">
              Közvetlen Telefonszám *
            </label>
            <input type="tel" required placeholder="+36 30 123 4567" 
                   class="w-full px-4 py-3 rounded-xl border bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[#E36527] transition-all"
                   style="border-color: var(--sv-border-light);">
          </div>

          <div>
            <label class="block text-xs font-mono-spec font-bold text-stone-700 uppercase mb-1.5" data-i18n="form_product_label">
              Érdeklődés Tárgya (Kért Termék)
            </label>
            <select class="w-full px-4 py-3 rounded-xl border bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[#E36527] transition-all"
                    style="border-color: var(--sv-border-light);">
              <option value="sutesallo-vegyes">SV Sütésálló Vegyes Gyümölcsíz (10 kg tömb)</option>
              <option value="sutesallo-kajszi">SV Sütésálló Kajszibarack készítmény (10 kg tömb)</option>
              <option value="kenheto-malna">SV Málna ízű készítmény (5 kg vödör)</option>
              <option value="kenheto-afonya">SV Áfonya készítmény (5 kg vödör)</option>
              <option value="sutesallo-extra-meggy">SV Sütésálló Extra Meggy (darabos prémium)</option>
              <option value="egyedi-receptura">Egyedi receptúra fejlesztése</option>
            </select>
          </div>

          <div>
            <label class="block text-xs font-mono-spec font-bold text-stone-700 uppercase mb-1.5" data-i18n="form_volume_label">
              Tervezett Havi Felhasználás
            </label>
            <select class="w-full px-4 py-3 rounded-xl border bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[#E36527] transition-all"
                    style="border-color: var(--sv-border-light);">
              <option value="vol-small">&lt; 500 kg / hó (Nagykereskedelmi raktárból)</option>
              <option value="vol-mid">500 kg – 2 tonna / hó (Közvetlen gyári raklap)</option>
              <option value="vol-large">&gt; 2 tonna / hó (Ipari kenyérgyári keretszerződés)</option>
            </select>
          </div>

        </div>

        <div>
          <label class="block text-xs font-mono-spec font-bold text-stone-700 uppercase mb-1.5" data-i18n="form_notes_label">
            Technológiai Megjegyzés / Próbasütés Célja
          </label>
          <textarea rows="3" placeholder="pl. 210 °C-os leveles tészta automata adagolófejjel történő próbagyártása..." 
                    class="w-full px-4 py-3 rounded-xl border bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[#E36527] transition-all"
                    style="border-color: var(--sv-border-light);"></textarea>
        </div>

        <div class="flex items-center gap-2">
          <input type="checkbox" id="form-gdpr" required class="w-4 h-4 rounded text-[#E36527] focus:ring-[#E36527]">
          <label for="form-gdpr" class="text-xs text-stone-600 font-mono-spec">
            Elfogadom az adatkezelési tájékoztatót a mintaküldés és technológiai egyeztetés céljából.
          </label>
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
            <span>B2B Ipari partnerek részére ingyenes próbaminta</span>
          </div>
        </div>

        <div id="form-success-message" class="hidden p-4 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-900 font-mono-spec text-xs">
          ✓ Köszönjük! Mintaigénylését rögzítettük. Műszaki tanácsadónk 24 órán belül felveszi Önnel a kapcsolatot a próbasütési tétel logisztikájával kapcsolatban.
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
                <span>Adószám:</span>
                <span class="font-bold text-stone-900">14650969-2-41</span>
              </div>
              <div class="flex justify-between">
                <span>Cégjegyzékszám:</span>
                <span class="font-bold text-stone-900">01-10-046300</span>
              </div>
              <div class="flex justify-between">
                <span>Pénzügyi besorolás:</span>
                <span class="font-bold text-emerald-700">AA+ Bonitás (Dun & Bradstreet)</span>
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
          <img src="assets/sun-valley-logo.png" alt="Sun Valley Zrt." class="h-8 w-auto brightness-0 invert opacity-90">
          <div>
            <div class="font-bold text-white font-syne text-base">SUN VALLEY ZRT.</div>
            <div class="text-[10px] text-white/50">Ipari Gyümölcstechnológia Mór • Est. 2009</div>
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
          © 2026 Sun Valley Kereskedelmi Zrt. • Minden jog fenntartva.
        </div>
        <div class="flex items-center gap-4">
          <span>AA+ Financial Rating</span>
          <span>•</span>
          <span>ISO / HACCP Standard</span>
          <span>•</span>
          <span>Mór Industrial Plant</span>
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
      <button onclick="closeTdsModal()" class="absolute top-5 right-5 p-2 rounded-xl border text-stone-500 hover:text-stone-900 transition-colors" style="border-color: var(--sv-border-light);">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>

      <!-- Modal Content Area -->
      <div id="tds-modal-content">
        <!-- Dynamically injected via JavaScript -->
      </div>

    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- VIBE-CODING / LIVE THEME CUSTOMIZER WIDGET                                -->
  <!-- ========================================================================= -->
  <div class="fixed bottom-4 right-4 z-50">
    <div class="relative">
      <button onclick="toggleVibePanel()" 
              class="flex items-center gap-2 px-3.5 py-2 rounded-full font-mono-spec text-xs font-bold text-white shadow-xl hover:scale-105 transition-all"
              style="background-color: var(--sv-burgundy); border: 2px solid var(--sv-gold);">
        <span>🎨 Vibe Colors</span>
      </button>

      <div id="vibe-panel" class="hidden absolute bottom-12 right-0 w-80 bg-white rounded-2xl shadow-2xl border p-4 font-sans text-xs space-y-4" style="border-color: var(--sv-border);">
        <div class="flex items-center justify-between border-b pb-2">
          <span class="font-bold font-syne text-sm text-stone-900">Vibe-Code Theme Tokens</span>
          <button onclick="toggleVibePanel()" class="text-stone-400 hover:text-stone-700">✕</button>
        </div>
        <p class="text-[11px] text-stone-500">
          A színek CSS változókkal működnek (`--sv-*`), azonnal tesztelhetsz új hangulatokat:
        </p>

        <div class="space-y-1.5">
          <span class="font-mono-spec text-[10px] uppercase font-bold text-stone-400">Téma Presetek:</span>
          <div class="grid grid-cols-3 gap-1.5 font-mono-spec text-[11px]">
            <button onclick="applyPreset('classic')" class="p-1.5 rounded-lg border bg-stone-50 hover:bg-stone-100 font-semibold text-center">Classic</button>
            <button onclick="applyPreset('harvest')" class="p-1.5 rounded-lg border bg-stone-50 hover:bg-stone-100 font-semibold text-center">Harvest</button>
            <button onclick="applyPreset('modern')" class="p-1.5 rounded-lg border bg-stone-50 hover:bg-stone-100 font-semibold text-center">Modern</button>
          </div>
        </div>

        <div class="space-y-2 pt-2 border-t font-mono-spec text-[11px]">
          <div class="flex items-center justify-between">
            <span>Primary (Bordó):</span>
            <input type="color" id="picker-burgundy" value="#5F2125" onchange="updateCustomColor('--sv-burgundy', this.value)" class="w-7 h-7 rounded border cursor-pointer">
          </div>
          <div class="flex items-center justify-between">
            <span>Accent (Narancs):</span>
            <input type="color" id="picker-orange" value="#E36527" onchange="updateCustomColor('--sv-orange', this.value)" class="w-7 h-7 rounded border cursor-pointer">
          </div>
          <div class="flex items-center justify-between">
            <span>Nature (Zöld):</span>
            <input type="color" id="picker-green" value="#2D3628" onchange="updateCustomColor('--sv-green-dark', this.value)" class="w-7 h-7 rounded border cursor-pointer">
          </div>
          <div class="flex items-center justify-between">
            <span>Background (Krém):</span>
            <input type="color" id="picker-cream" value="#F5F2EE" onchange="updateCustomColor('--sv-paper-cream', this.value)" class="w-7 h-7 rounded border cursor-pointer">
          </div>
        </div>

        <button onclick="resetColors()" class="w-full py-1.5 rounded-lg border text-stone-600 hover:bg-stone-50 font-mono-spec text-[10px] text-center">
          Alapértelmezett visszaállítása
        </button>
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
        topbar_scale: "Ipari Gyártóbázis: Mór (Major u. 3.)",
        topbar_capacity: "Éves kapacitás: 1,1–1,3 Mrd Ft forgalom",
        topbar_rating: "AA+ Pénzügyi Minősítés",
        tagline: "Ipari Gyümölcstechnológia • Est. 2009",
        nav_catalog: "Gasztro-Katalógus",
        nav_products: "Termékek & TDS",
        nav_tech: "Sütésállóság (200°C)",
        nav_rd: "Receptúra-fejlesztés",
        nav_prospectus: "Prospektus",
        nav_distribution: "Nagykereskedelmi Hálózat",
        nav_contact: "Gyártóüzem & Elérhetőség",
        btn_sample_short: "Próbagyártási Minta",
        hero_badge: "B2B Kenyérgyári & Finompékáru Alapanyagok",
        hero_h1_p1: "200 °C felett sem forr ki.",
        hero_h1_p2: "Ipari sütésálló",
        hero_h1_p3: "gyümölcstöltelékek közvetlenül a gyártótól.",
        hero_desc: "A Sun Valley Zrt. a magyar finompékáru-üzemek és ipari kenyérgyárak megbízható belföldi beszállítója. Forma- és alaktartó, gépileg szeletelhető tésztabetétek 10 kg-os kartonos és 5 kg-os vödrös kiszerelésben, közvetlen móri gyártóbázisról.",
        hero_cta_catalog: "Lapozható Gasztro-Katalógus",
        hero_cta_sample: "Üzemi Tesztminta Kérése",
        hero_cta_prospectus: "Prospektus (PPTX)",
        telemetry_heat_label: "Hőtűrési küszöb",
        telemetry_heat_sub: "Nem forr ki, alaktartó",
        telemetry_pack_label: "Ipari Kiszerelés",
        telemetry_pack_sub: "480 kg raklapos tétel",
        telemetry_geo_label: "Gyártótelep",
        telemetry_geo_sub: "Major utca 3.",
        card_hero_cat: "PRÉMIUM PÉKIPARI TÉSZTABETÉT",
        card_hero_title: "SV Sütésálló Kajszibarack & Vegyes Íz",
        card_hero_desc: "Formatartó, természetes aromájú töltelék magas hőmérsékletű sütéshez. Leveles tésztákban és kelt tésztákban sem enged szabad vizet.",
        spec_brix: "Szárazanyagtartalom (Brix)",
        spec_thermo: "Hőállóság (200°C / 15 perc)",
        spec_thermo_val: "Alaktartó / Nem forr ki",
        spec_slice: "Szeletelhetőség (Gépi késállás)",
        spec_slice_val: "Kiváló / Tiszta vágás",
        btn_view_full_tds: "Részletes TDS Műszaki Adatlap",
        stat_revenue: "Éves árbevétel (Stabil tőkeerő)",
        stat_rating: "Pénzügyi minősítés (Adósságmentes)",
        stat_heritage: "Gyümölcsfeldolgozói múlt (Vitamór bázis)",
        stat_energy: "Energiatudatos Móri Gyártelep",
        cat_section_tag: "Lapozható Gasztronómiai Katalógus",
        cat_section_title: "Gyümölcstöltelékek Felhasználás Szerint",
        cat_section_desc: "Válasszon technológiai kategóriát: lapozzon a sütésálló tömbök, a hidegen kenhető készítmények és az extra dzsemek között.",
        cat_apps_label: "Jellemző Pékipari Alkalmazások:",
        btn_view_category_tds: "TDS Adatlap Megtekintése",
        btn_request_cat_sample: "Minta Kérése Ebből a Kategóriából",
        flavors_tag: "Hagyományos Ízvilág • Korszerű Technológia",
        flavors_title: "Ismerős Ízek. Megbízható Ipari Minőség.",
        flavors_desc: "A magyar pékipar és cukrászat legkedveltebb hagyományos gyümölcseit dolgozzuk fel korszerű vákuumüstjeinkben. A termékeket a partner technológiájához igazítva állítjuk be mind sütésálló, mind hidegen kenhető formában.",
        flavors_cta: "Részletes műszaki paraméterek megtekintése a termékmátrixban",
        exotic_tag: "Egyedi Fejlesztési Irányok • Innováció",
        exotic_title: "Egzotikus Ízek. Az Ön Termékére Hangolva.",
        exotic_desc: "Az alapízeken túl trópusi és egzotikus gyümölcsökből is fejlesztünk egyedi receptúrát a kívánt ízvilághoz, állaghoz és technológiához. Legyen szó mangóról, maracujáról vagy citrusos készítményekről, móri laborunkban finomhangoljuk a hőtűrést és a viszkozitást.",
        exotic_note: "* Az egzotikus receptúrákat ipari próbagyártás és technológiai egyeztetés alapján véglegesítjük a partner saját gépsoraira.",
        tech_section_tag: "Élelmiszer-technológiai Garanciák",
        tech_section_title: "Nem Csak Az Íz Számít. Technológia & Megbízhatóság.",
        tech_section_desc: "A finompékáru-gyártásban a selejtképződés legfőbb oka a töltelék kiforrása, a tészta elázása vagy a gépi adagolófejek eldugulása. A Sun Valley Zrt. hidrokolloid- és pektinmátrixa négy technológiai alappillérre épül:",
        tech_card1_title: "Garantált Sütésállóság",
        tech_card1_desc: "200 °C felett sem forr ki a süteményből, nem ég le a tepsire, és megőrzi térfogatát a tésztában szinerézis (vízkiválás) nélkül.",
        tech_card2_title: "Fagyasztásállóság",
        tech_card2_desc: "Fagyasztott félkész és fagyasztva tárolt késztermékekhez kifejlesztve. Felengedéskor nem enged levet, nem áztatja el a tésztát.",
        tech_card3_title: "Gépi Tölthetőség & Pumpálás",
        tech_card3_desc: "A kézi kenéstől a nagyteljesítményű automata tüskés injektálósorokig (fánkok, croissant-ok) állandó, nyírásra stabil viszkozitás.",
        tech_card4_title: "Kis Szériától Ipari Léptékig",
        tech_card4_desc: "5 kg-os vödörben a cukrászatoknak, 10 kg-os szeletelhető kartontömbökben kenyérgyáraknak, vagy 200 kg-os hordókban nagyüzemeknek.",
        rd_section_tag: "Egyedi Termékfejlesztési Folyamat",
        rd_section_title: "Az Ön Ötlete. Közös Ipari Fejlesztés.",
        rd_section_desc: "Nem minden gyártósor és késztermék egyforma. Az egyedi receptúra-fejlesztés során a technológusokkal közösen alakítjuk ki az ideális tölteléket 3 lépésben:",
        rd_step1_title: "Az Igény Megismerése",
        rd_step1_desc: "Felhasználás, ízvilág, elvárt gyümölcstartalom, állag, sütési hőmérséklet (180–220 °C) és a gépsor adagolási feltételeinek pontos felmérése.",
        rd_step2_title: "Receptúra & Üzemi Próba",
        rd_step2_desc: "Laboratóriumi minta készítése, majd 5–10 kg-os üzemi próbagyártási minta kiküldése a partner saját gyártósorán történő sütési validációra.",
        rd_step3_title: "Gyártásra Hangolva",
        rd_step3_desc: "A végleges műszaki specifikáció (TDS) rögzítése, a csomagolás (vödör, kartontömb, hordó) kiválasztása és a stabil ütemezett raklapos szállítás elindítása.",
        prod_section_tag: "Termékportfólió & Minőségi Specifikációk",
        prod_section_title: "Ipari Sütésálló & Kenhető Gyümölcskészítmények",
        prod_section_desc: "Minden termékünk standardizált laboratóriumi paraméterekkel, szigorú mikrobiológiai ellenőrzés mellett készül. Kattintson a TDS adatlapokra a részletes mérnöki specifikációkért (Brix, pH, allergének).",
        prospectus_badge: "HIVATALOS B2B DOKUMENTÁCIÓ • V1.4",
        prospectus_title: "Töltse le a Sun Valley Zrt. Hivatalos Vállalati Prospektusát",
        prospectus_desc: "A prezentáció részletesen bemutatja móri üzemünk technológiai gépsorait, a teljes sütésálló és hidegtechnológiás termékpalettát, a logisztikai paritásokat és a minőségbiztosítási garanciákat.",
        btn_download_prospectus: "Prospektus Letöltése (.PPTX)",
        dist_section_tag: "Értékesítési Csatornák & Logisztika",
        dist_section_title: "Hogyan Jut El a Termék az Ön Üzemébe?",
        dist_section_desc: "Rugalmas logisztikai modellünk két csatornán biztosítja az ellátásbiztonságot: közvetlen gyári szerződéssel ipari mennyiségekre, vagy országos nagykereskedelmi partnereinken keresztül azonnali raktári kiszolgálásra.",
        dist_t1_badge: "1. CSATORNA • IPARI SZERZŐDÉSEK",
        dist_t1_title: "Közvetlen Gyári Szállítás (Raklapos & Kamionos Tételek)",
        dist_t1_desc: "Nagyipari kenyérgyárak és finompékáru-üzemek részére (>500 kg / megrendelés). Közvetlen gyári egyedi árképzés, ütemezett lehívások, tételes sarzshomogenitás és folyamatos technológiai támogatás.",
        dist_t1_p1: "480 kg raklapos standard egységek",
        dist_t1_p2: "Garantált tételes sarzs-homogenitás",
        dist_t1_p3: "Közvetlen telephelyi kapcsolattartó",
        dist_t1_cta: "Ipari Keretszerződés Egyeztetése",
        dist_t2_badge: "2. CSATORNA • RAKTÁRI KISZOLGÁLÁS",
        dist_t2_title: "Országos Nagykereskedelmi Partnerhálózat",
        dist_t2_desc: "Közepes cukrászatok és kézműves pékségek az országos lefedettségű partner-nagykereskedőink raktáraiból azonnal megvásárolhatják az 5–10 kg-os kiszereléseket.",
        dist_t2_footer: "Érdeklődjön helyi pékszövetségi vagy nagykereskedelmi területi képviselőjénél.",
        form_section_tag: "Üzemi Próbagyártási Minta",
        form_section_title: "Kérjen Tesztmintát Saját Gyártósorára",
        form_section_desc: "Töltse ki az alábbi űrlapot, és szakmai csapatunk eljuttatja üzemébe a kívánt 5–10 kg-os tesztmintát próbasütéshez.",
        form_name_label: "Kapcsolattartó Neve & Pozíciója *",
        form_company_label: "Cégnév & Adószám * (B2B szűrés)",
        form_email_label: "Munkahelyi E-mail Cím *",
        form_phone_label: "Közvetlen Telefonszám *",
        form_product_label: "Érdeklődés Tárgya (Kért Termék)",
        form_volume_label: "Tervezett Havi Felhasználás",
        form_notes_label: "Technológiai Megjegyzés / Próbasütés Célja",
        form_submit_btn: "Üzemi Tesztminta Igénylése",
        contact_section_tag: "Hivatalos Elérhetőségek",
        contact_section_title: "Közvetlen Kapcsolat a Gyárral",
        contact_section_desc: "Ipari mintakérések, árajánlatok és technológiai kérdések esetén vegye fel a kapcsolatot közvetlenül gyárvezetésünkkel.",
        contact_mobile_label: "Közvetlen Mobilkapcsolat",
        contact_rep_name: "ifj. Vécsei András • Kereskedelem & Vezetés",
        contact_plant_phone_label: "Telephelyi Vezetékes",
        contact_plant_phone_sub: "Móri Gyártóüzem Központ",
        contact_email_label: "Központi Elektronikus Levelezés",
        contact_email_sub: "Írásbeli ajánlatkérés és műszaki specifikációk továbbítása",
        plant_loc_title: "Telephely & Üzem",
        corp_hq_title: "Hivatalos Székhely",
        link_google_maps: "Megtekintés Google Térképen"
      },

      en: {
        topbar_scale: "Industrial Plant: Mór, Hungary (Major u. 3.)",
        topbar_capacity: "Annual capacity: €2.8M–€3.3M turnover",
        topbar_rating: "AA+ Financial Credit Rating",
        tagline: "Industrial Food Technology • Est. 2009",
        nav_catalog: "Gastro-Catalog",
        nav_products: "Products & TDS",
        nav_tech: "Thermo-Stability (200°C)",
        nav_rd: "Custom R&D",
        nav_prospectus: "Brochure",
        nav_distribution: "Wholesale Network",
        nav_contact: "Plant & Contact",
        btn_sample_short: "Trial Sample",
        hero_badge: "B2B Commercial Bakery & Pastry Ingredients",
        hero_h1_p1: "No boil-out above 200 °C.",
        hero_h1_p2: "Industrial bake-stable",
        hero_h1_p3: "fruit preparations directly from manufacturer.",
        hero_desc: "Sun Valley Zrt. is a proven supplier for industrial bread factories and commercial pastry plants. Shape-retaining, mechanically sliceable fruit fillings in 10 kg cartons and 5 kg buckets directly from our Mór facility.",
        hero_cta_catalog: "Interactive Gastro-Catalog",
        hero_cta_sample: "Request Trial Batch Sample",
        hero_cta_prospectus: "Download Brochure (PPTX)",
        telemetry_heat_label: "Thermal Threshold",
        telemetry_heat_sub: "No boil-over, shape-stable",
        telemetry_pack_label: "Packaging Scale",
        telemetry_pack_sub: "480 kg palletized standard",
        telemetry_geo_label: "Plant Facility",
        telemetry_geo_sub: "Major utca 3., Mór",
        card_hero_cat: "COMMERCIAL BAKERY INSERT",
        card_hero_title: "SV Bake-Stable Apricot & Mixed Fruit",
        card_hero_desc: "Form-retaining fruit preparation with intense natural aroma for high-heat baking. Zero synaeresis in puff pastries and yeast doughs.",
        spec_brix: "Dry Matter (Brix)",
        spec_thermo: "Heat stability (200°C / 15 min)",
        spec_thermo_val: "Form-stable / No boil-out",
        spec_slice: "Sliceability (Machine cut)",
        spec_slice_val: "Clean cut edge / Firm gel",
        btn_view_full_tds: "View Detailed TDS Specification",
        stat_revenue: "Annual Turnover (Financial strength)",
        stat_rating: "Credit Rating (Debt-free AA+)",
        stat_heritage: "Fruit Processing Experience (Vitamór plant)",
        stat_energy: "Energy-Conscious Plant Award",
        cat_section_tag: "Interactive Gastro-Catalog",
        cat_section_title: "Fruit Preparations by Application",
        cat_section_desc: "Select your technology category: browse bake-stable blocks, cold-spreadable fillings, and premium extra jams.",
        cat_apps_label: "Verified Industrial Applications:",
        btn_view_category_tds: "View Category TDS Sheet",
        btn_request_cat_sample: "Request Category Sample",
        flavors_tag: "Heritage Flavors • Modern Processing",
        flavors_title: "Familiar Flavors. Industrial Precision.",
        flavors_desc: "We process Hungary's most celebrated domestic fruits in modern vacuum boiling vessels, customized to your exact baking or spreading technology.",
        flavors_cta: "View technical parameters in the product matrix",
        exotic_tag: "Custom R&D • Product Innovation",
        exotic_title: "Exotic Flavors. Engineered for Your Product.",
        exotic_desc: "Beyond traditional fruit bases, we engineer customized formulations from tropical and exotic fruits tailored to your desired flavor profile, viscosity, and thermal requirements.",
        exotic_note: "* Exotic formulations are finalized following laboratory trials and on-site pilot baking at your facility.",
        tech_section_tag: "Food Engineering Assurances",
        tech_section_title: "More than Flavor. Process Engineering.",
        tech_section_desc: "In commercial pastry production, scrap rates are driven by boil-outs, crust sogginess, or nozzle clogging. Sun Valley's hydrocolloid matrix is built on four core technical pillars:",
        tech_card1_title: "Guaranteed Bake-Stability",
        tech_card1_desc: "Maintains geometry and volume above 200 °C without boiling out or scorching baking trays.",
        tech_card2_title: "Freeze-Thaw Stability",
        tech_card2_desc: "Formulated for frozen unbaked and par-baked doughs. Zero water separation upon defrosting.",
        tech_card3_title: "Automated Dosing & Injection",
        tech_card3_desc: "Shear-thinning viscosity designed for automated needle depositors (doughnuts, croissants) without dripping.",
        tech_card4_title: "From Trial to Factory Scale",
        tech_card4_desc: "5 kg buckets for artisan confectionery, 10 kg sliceable carton blocks, and 200 kg aseptic drums for large plants.",
        rd_section_tag: "Custom Formulation Pipeline",
        rd_section_title: "Your Concept. Collaborative R&D.",
        rd_section_desc: "Every production line is unique. We partner with industrial bakeries in 3 structured phases:",
        rd_step1_title: "Requirement Scoping",
        rd_step1_desc: "Auditing application type, fruit %, viscosity, oven profile (180–220 °C), and depositor nozzle specifications.",
        rd_step2_title: "Formulation & Pilot Batch",
        rd_step2_desc: "Laboratory formulation followed by a 5–10 kg trial batch dispatched for validation on your production line.",
        rd_step3_title: "Production Integration",
        rd_step3_desc: "Locking technical specifications (TDS), selecting packaging units, and scheduling ongoing palletized deliveries.",
        prod_section_tag: "Product Matrix & Laboratory Specifications",
        prod_section_title: "Industrial Bake-Stable & Spreadable Fruit Fillings",
        prod_section_desc: "Standardized laboratory parameters with rigorous microbiological control. Click on any product for its Technical Data Sheet.",
        prospectus_badge: "OFFICIAL B2B BROCHURE • V1.4",
        prospectus_title: "Download the Official Sun Valley Corporate Brochure",
        prospectus_desc: "Detailed presentation covering our Mór manufacturing facility, boiling technology, complete product portfolio, logistics parities, and quality assurance standards.",
        btn_download_prospectus: "Download Brochure (.PPTX)",
        dist_section_tag: "Distribution & Logistics",
        dist_section_title: "How Products Reach Your Facility",
        dist_section_desc: "Our dual-track distribution ensures absolute reliability: direct factory contracts for bulk tonnage, or regional wholesale partners for immediate depot pick-up.",
        dist_t1_badge: "CHANNEL 1 • ENTERPRISE CONTRACTS",
        dist_t1_title: "Direct Factory Supply (Pallet & Truckload Orders)",
        dist_t1_desc: "For industrial bread factories (>500 kg / delivery). Direct factory pricing, scheduled shipments, and dedicated technical line support.",
        dist_t1_p1: "480 kg palletized standard units",
        dist_t1_p2: "Guaranteed batch-to-batch homogeneity",
        dist_t1_p3: "Direct plant account manager",
        dist_t1_cta: "Discuss Enterprise Framework",
        dist_t2_badge: "CHANNEL 2 • REGIONAL DEPOTS",
        dist_t2_title: "Authorized Wholesale Partner Network",
        dist_t2_desc: "Mid-sized bakeries and confectioneries can source 5–10 kg containers directly from our authorized distributors across Hungary.",
        dist_t2_footer: "Contact your regional bakery supply distributor.",
        form_section_tag: "Pilot Batch Request",
        form_section_title: "Request a Trial Sample for Your Production Line",
        form_section_desc: "Submit your details, and our technical team will prepare and dispatch a 5–10 kg pilot bucket for test baking.",
        form_name_label: "Contact Name & Position *",
        form_company_label: "Company & Tax ID * (B2B verification)",
        form_email_label: "Work Email *",
        form_phone_label: "Direct Phone *",
        form_product_label: "Product of Interest",
        form_volume_label: "Estimated Monthly Volume",
        form_notes_label: "Technical Notes / Test Objectives",
        form_submit_btn: "Request Industrial Sample",
        contact_section_tag: "Official Contact",
        contact_section_title: "Direct Communication with Plant Management",
        contact_section_desc: "For trial batch requests, quotes, or food engineering inquiries, reach out directly to our leadership team.",
        contact_mobile_label: "Direct Mobile Line",
        contact_rep_name: "András Vécsei Jr. • Commercial Director",
        contact_plant_phone_label: "Plant Landline",
        contact_plant_phone_sub: "Mór Manufacturing Headquarters",
        contact_email_label: "Corporate Email Address",
        contact_email_sub: "Formal quotes and technical inquiries",
        plant_loc_title: "Plant & Production Site",
        corp_hq_title: "Corporate Headquarters",
        link_google_maps: "View on Google Maps"
      },

      de: {
        topbar_scale: "Produktionswerk: Mór, Ungarn (Major u. 3.)",
        topbar_capacity: "Jahreskapazität: 2,8–3,3 Mio. € Umsatz",
        topbar_rating: "AA+ Bonitätsbewertung",
        tagline: "Industrielle Fruchttechnologie • Gegr. 2009",
        nav_catalog: "Gastro-Katalog",
        nav_products: "Produkte & TDS",
        nav_tech: "Hitzestabilität (200°C)",
        nav_rd: "Rezepturentwicklung",
        nav_prospectus: "Broschüre",
        nav_distribution: "Großhandelsnetz",
        nav_contact: "Werk & Kontakt",
        btn_sample_short: "Probemuster",
        hero_badge: "B2B Großbäckerei- & Feingebäck-Rohstoffe",
        hero_h1_p1: "Kein Auskochen über 200 °C.",
        hero_h1_p2: "Industrielle backstabile",
        hero_h1_p3: "Fruchtzubereitungen direkt vom Hersteller.",
        hero_desc: "Sun Valley Zrt. ist der verlässliche Partner für Großbäckereien und Feingebäckhersteller. Formstabile, maschinell schneidbare Fruchtfüllungen in 10 kg Kartons und 5 kg Eimern direkt aus Mór.",
        hero_cta_catalog: "Gastro-Katalog Durchblättern",
        hero_cta_sample: "Produktionsmuster Anfordern",
        hero_cta_prospectus: "Broschüre (.PPTX)",
        telemetry_heat_label: "Hitzestabilität",
        telemetry_heat_sub: "Kochfest, formbeständig",
        telemetry_pack_label: "Verpackung",
        telemetry_pack_sub: "480 kg Paletteneinheit",
        telemetry_geo_label: "Produktionsstandort",
        telemetry_geo_sub: "Major utca 3., Mór",
        card_hero_cat: "INDUSTRIELLE FEINGEBÄCK-FÜLLUNG",
        card_hero_title: "SV Backstabile Aprikosen- & Mischfruchtfüllung",
        card_hero_desc: "Formstabile Fruchtzubereitung für Hochtemperatur-Backprozesse. Keine Synärese in Blätterteig und Hefegebäck.",
        spec_brix: "Trockensubstanz (Brix)",
        spec_thermo: "Hitzetest (200°C / 15 Min.)",
        spec_thermo_val: "Formbeständig / Kein Auslaufen",
        spec_slice: "Schneidbarkeit (Maschinenschnitt)",
        spec_slice_val: "Exzellent / Fester Gelkörper",
        btn_view_full_tds: "Technisches Datenblatt (TDS)",
        stat_revenue: "Jahresumsatz (Solide Eigenkapitalbasis)",
        stat_rating: "Bonitätsbewertung (Schuldenfrei AA+)",
        stat_heritage: "Fruchtverarbeitungs-Tradition (Vitamór Bäckerei)",
        stat_energy: "Auszeichnung Energiebewusstes Werk",
        cat_section_tag: "Blätterbarer Gastro-Katalog",
        cat_section_title: "Fruchtzubereitungen nach Anwendung",
        cat_section_desc: "Wählen Sie Ihre Technologie: Blättern Sie durch backstabile Blöcke, streichfähige Füllungen und Extra-Konfitüren.",
        cat_apps_label: "Typische Bäckereianwendungen:",
        btn_view_category_tds: "TDS Datenblatt Ansehen",
        btn_request_cat_sample: "Muster Aus Dieser Kategorie Anfordern",
        flavors_tag: "Traditionelle Früchte • Moderne Technologie",
        flavors_title: "Vertraute Aromen. Industrielle Verlässlichkeit.",
        flavors_desc: "Wir verarbeiten ungarische Früchte schonend in modernen Vakuumkesseln, abgestimmt auf Ihre Back- oder Kalttechnologie.",
        flavors_cta: "Detaillierte Parameter in der Produktmatrix",
        exotic_tag: "Sonderrezepturen • Innovation",
        exotic_title: "Exotische Früchte. Maßgeschneidert.",
        exotic_desc: "Neben den Grundsorten entwickeln wir maßgeschneiderte Rezepturen aus exotischen Früchten (Mango, Maracuja, Zitrus) für Ihr Endprodukt.",
        exotic_note: "* Exotische Rezepturen werden nach Laborversuchen und Probeproduktion vor Ort finalisiert.",
        tech_section_tag: "Lebensmitteltechnologische Garantien",
        tech_section_title: "Nicht Nur Geschmack. Prozesssicherheit.",
        tech_section_desc: "Ausschuss entsteht meist durch auskochende Füllungen oder verklebte Dosierdüsen. Das Sun Valley System basiert auf vier Säulen:",
        tech_card1_title: "Garantierte Backstabilität",
        tech_card1_desc: "Behält selbst über 200 °C Form und Volumen, ohne Backbleche zu verbrennen.",
        tech_card2_title: "Gefrier-Auftau-Stabilität",
        tech_card2_desc: "Für tiefgekühlte Teiglinge. Kein Wasserverlust beim Auftauen.",
        tech_card3_title: "Maschinelle Dosierbarkeit",
        tech_card3_desc: "Optimierte Viskosität für automatische Injektionsnadeln (Berliner, Croissants) ohne Nachtropfen.",
        tech_card4_title: "Kleinserie bis Großindustrie",
        tech_card4_desc: "5 kg Eimer, 10 kg schneidbare Blockware oder 200 kg Aseptikfässer für Großwerke.",
        rd_section_tag: "Rezepturentwicklungs-Prozess",
        rd_section_title: "Ihre Idee. Gemeinsame Entwicklung.",
        rd_section_desc: "Gemeinsam mit Ihren Bäckereitechnologen in 3 klaren Schritten:",
        rd_step1_title: "Bedarfsanalyse",
        rd_step1_desc: "Erfassung von Viskosität, Fruchtanteil, Backtemperatur (180–220 °C) und Dosieranlagen.",
        rd_step2_title: "Rezeptur & Werksmuster",
        rd_step2_desc: "Laborabstimmung und Versand eines 5–10 kg Probemusters für Testbacken auf Ihrer Linie.",
        rd_step3_title: "Serienfertigung",
        rd_step3_desc: "Fixierung des TDS-Datenblatts, Auswahl der Gebinde und Start der planbaren Belieferung.",
        prod_section_tag: "Produktportfolio & Spezifikationen",
        prod_section_title: "Industrielle Backstabile & Streichfähige Fruchtzubereitungen",
        prod_section_desc: "Standardisierte Laborwerte unter strenger mikrobiologischer Kontrolle. Klicken Sie auf ein TDS für Details.",
        prospectus_badge: "OFFIZIELLE B2B DOKUMENTATION • V1.4",
        prospectus_title: "Unternehmensbroschüre der Sun Valley Zrt. Herunterladen",
        prospectus_desc: "Präsentation über unsere Produktionsanlagen in Mór, das Sortiment, Logistik und Qualitätszertifikate.",
        btn_download_prospectus: "Broschüre Herunterladen (.PPTX)",
        dist_section_tag: "Vertriebskanäle & Logistik",
        dist_section_title: "Wie Gelangen die Produkte in Ihr Werk?",
        dist_section_desc: "Unser duales Vertriebsmodell sichert höchste Versorgungssicherheit: Direkte Werkverträge oder autorisierte Großhandelspartner.",
        dist_t1_badge: "KANAL 1 • INDUSTRIEVERTRÄGE",
        dist_t1_title: "Direkte Werksbelieferung (Paletten- & LKW-Ladungen)",
        dist_t1_desc: "Für Großbäckereien (>500 kg pro Bestellung). Werkskonditionen, Rahmenverträge und kontinuierliche Betreuung.",
        dist_t1_p1: "480 kg Paletteneinheiten",
        dist_t1_p2: "Garantierte Chargenhomogenität",
        dist_t1_p3: "Direkter Werksansprechpartner",
        dist_t1_cta: "Industrielle Rahmenvereinbarung",
        dist_t2_badge: "KANAL 2 • REGIONALLAGER",
        dist_t2_title: "Autorisiertes Großhandelsnetzwerk",
        dist_t2_desc: "Konditoreien und Bäckereien beziehen 5–10 kg Gebinde unkompliziert über regionale Bäckereigroßhändler.",
        dist_t2_footer: "Fragen Sie Ihren regionalen Bäckereifachgroßhändler.",
        form_section_tag: "Betriebliches Produktionsmuster",
        form_section_title: "Testmuster für Ihre Produktionslinie Anfordern",
        form_section_desc: "Füllen Sie das Formular aus; wir senden Ihnen ein 5–10 kg Probemuster für Testbacken.",
        form_name_label: "Name & Position *",
        form_company_label: "Firma & Steuernummer * (B2B)",
        form_email_label: "Geschäftliche E-Mail *",
        form_phone_label: "Telefonnummer *",
        form_product_label: "Gewünschtes Produkt",
        form_volume_label: "Geplanter Monatsbedarf",
        form_notes_label: "Technologische Anmerkungen",
        form_submit_btn: "Betriebsmuster Anfordern",
        contact_section_tag: "Offizielle Kontaktdaten",
        contact_section_title: "Direkter Draht zur Werksleitung",
        contact_section_desc: "Für Probemuster, Preisrahmenverträge oder lebensmitteltechnische Fragen kontaktieren Sie bitte unsere Leitung.",
        contact_mobile_label: "Direkte Mobilnummer",
        contact_rep_name: "András Vécsei jun. • Vertriebsleitung",
        contact_plant_phone_label: "Werksfestnetz",
        contact_plant_phone_sub: "Produktionsstandort Mór",
        contact_email_label: "Zentrale E-Mail-Adresse",
        contact_email_sub: "Schriftliche Preisanfragen & Spezifikationen",
        plant_loc_title: "Produktionswerk & Standort",
        corp_hq_title: "Offizieller Firmensitz",
        link_google_maps: "Auf Google Maps Anzeigen"
      }
    };

    // ---------------------------------------------------------------------------
    // KATALÓGUS DATA (TABBED FLIPBOOK)
    // ---------------------------------------------------------------------------
    const catalogData = {
      "bake-stable": {
        badge: { hu: "10 KG KARTON • SÜTÉSÁLLÓ TÖMB", en: "10 KG CARTON • BAKE-STABLE BLOCK", de: "10 KG KARTON • BACKSTABILER BLOCK" },
        title: { hu: "Sütésálló Gyümölcstöltelékek", en: "Bake-Stable Fruit Preparations", de: "Backstabile Fruchtzubereitungen" },
        subtitle: { hu: "200 °C felett alaktartó, gépileg szeletelhető tésztabetétek", en: "Shape-retaining above 200 °C, automated sliceable blocks", de: "Formstabil über 200 °C, maschinell schneidbare Blöcke" },
        desc: {
          hu: "Speciális pektinhálójuk révén a tészta 200 °C feletti sütése során sem forrnak ki, nem áztatják el a tésztát, és hűlés után is megőrzik rugalmas gélállagukat. Kiválóan alkalmasak ipari automatizált töltő- és szeletelősorokra.",
          en: "Engineered with a high-performance pectin network that prevents boil-outs even above 200 °C. Eliminates dough sogginess and retains elastic gel consistency after baking. Optimized for automated dough sheeters and depositors.",
          de: "Dank der speziellen Pektinstruktur kochen diese Füllungen auch über 200 °C nicht aus und weichen den Teig nicht auf. Behalten nach dem Abkühlen ihre elastische Gelform. Perfekt für Schneid- und Dosiermaschinen."
        },
        apps: ["Sárgabarackos bukta", "Lekváros papucs", "Rácsos linzer", "Leveles táskák", "Piték & derelyék"],
        specs: { heat: "≥ 200 °C", brix: "58–64° Brix", pack: "10 kg karton" },
        image: "assets/catalog-bake-stable.png",
        caption: "Üzemi próbasütési minta • 10 kg tömbösített kiszerelés",
        tdsIndex: 0
      },
      "spreadable": {
        badge: { hu: "5 KG MŰANYAG VÖDÖR • HIDEG TECHNOLÓGIA", en: "5 KG BUCKET • COLD PROCESS", de: "5 KG EIMER • KALTTECHNOLOGIE" },
        title: { hu: "Kenhető Gyümölcskészítmények", en: "Cold-Spreadable Fruit Preparations", de: "Streichfähige Fruchtzubereitungen" },
        subtitle: { hu: "Homogén, selymes kenhetőség cukrászati felületekre", en: "Homogeneous, velvety spreadability for pastry layers", de: "Homogene, samtige Streichfähigkeit für Konditoreiböden" },
        desc: {
          hu: "Hideg technológiára kifejlesztett, egyenletesen terülő gyümölcskészítmények piskótatekercsek, tortalapok és linzer sütemények gyors és tiszta kenéséhez. Magas gyümölcsös aroma és intenzív fényesség jellemzi.",
          en: "Formulated for ambient and cold pastry assembly. Smoothly spreads over sponge cakes, swiss rolls, and linzer cookies without tearing tender crumbs. Delivers vibrant fruit gloss and rich aromatic profile.",
          de: "Entwickelt für die kalte Konditoreiverarbeitung. Lässt sich mühelos auf Biskuitböden, Rouladen und Linzer Gebäck verstreichen, ohne den Teig zu beschädigen. Ausgezeichneter Fruchtglanz."
        },
        apps: ["Linzer karika", "Piskótatekercs", "Epres/málnás tortalap", "Sütemény áthúzás", "Desszertbetét"],
        specs: { heat: "Hideg eljárás", brix: "62–66° Brix", pack: "5 kg vödör" },
        image: "assets/catalog-spreadable.png",
        caption: "Hidegen kenhető málnás & erdei gyümölcsös minták • 5 kg vödör",
        tdsIndex: 2
      },
      "extra-jam": {
        badge: { hu: "PRÉMIUM GYÜMÖLCSDARABOS • EXTRA DZSEM", en: "PREMIUM FRUIT PIECES • EXTRA JAM", de: "PREMIUM FRUCHTSTÜCKE • EXTRA KONFITÜRE" },
        title: { hu: "Sütésálló Extra Dzsemek", en: "Bake-Stable Extra Jams", de: "Backstabile Extra-Konfitüren" },
        subtitle: { hu: "Látványos gyümölcsdarabok magas hőtűréssel ötvözve", en: "Identifiable fruit pieces combined with high thermal resistance", de: "Sichtbare Fruchtstücke kombiniert mit hoher Hitzebeständigkeit" },
        desc: {
          hu: "Kifejezetten prémium finompékárukhoz és kézműves cukrászati termékekhez megalkotott készítmények egész vagy darabolt gyümölcsökkel. A gyümölcsdarabok a sütés során is felismerhetőek és zamatosak maradnak.",
          en: "Crafted for premium viennoiserie and high-end baked goods featuring recognizable fruit pieces. The fruit inclusions retain their succulent bite and color without bleeding excessively into the surrounding crust.",
          de: "Entwickelt für Premium-Plundergebäcke und anspruchsvolle Konditoreiprodukte mit ganzen oder stückigen Früchten. Die Fruchtstücke bleiben beim Backen saftig und formstabil."
        },
        apps: ["Kézműves croissant", "Gyümölcskosárka", "Dán pékáru", "Prémium leveles tészta", "Rácsos sütemény"],
        specs: { heat: "≥ 190 °C", brix: "60–65° Brix", pack: "5 kg / 10 kg" },
        image: "assets/catalog-extra-jam.png",
        caption: "Extra meggyes & barackos sütemény fotók • Prémium minőség",
        tdsIndex: 4
      }
    };

    // ---------------------------------------------------------------------------
    // PRODUCT DATA REPOSITORY (FULL 6 ITEMS)
    // ---------------------------------------------------------------------------
    const products = [
      {
        id: "sv-vegyes-10kg",
        category: "sutesallo",
        names: {
          hu: "SV Sütésálló Vegyes Gyümölcsíz",
          en: "SV Bake-Stable Mixed Fruit Preparation",
          de: "SV Backstabile Gemischte Fruchtzubereitung"
        },
        badge: { hu: "SÜTÉSÁLLÓ TÖMB • VEGÁN", en: "BAKE-STABLE BLOCK • VEGAN", de: "BACKSTABIL BLOCK • VEGAN" },
        pack: "10 kg karton (480 kg/raklap)",
        specs: {
          brix: "58–62° Brix",
          ph: "3.3 – 3.6",
          heat: "≥ 200 °C (15 perc)",
          shelfLife: "12 hónap / months",
          sliceability: { hu: "Kiváló, késálló gépi szeletelés", en: "Excellent, clean automated slicing", de: "Exzellent, messerfeste Schneidbarkeit" }
        },
        desc: {
          hu: "Hagyományos receptúrájú, természetes színezékkel készülő, tömbösített sütésálló gyümölcstöltelék. Kifejezetten ipari bukták, táskák és kelt tészták gépileg szeletelhető töltésére kifejlesztve.",
          en: "Traditional recipe thermo-stable fruit block made with natural colors. Engineered specifically for automated slicing and filling of commercial yeast buns, turnovers, and puff pastries.",
          de: "Traditionell hergestellte, backstabile Blockfruchtzubereitung mit natürlichen Farbstoffen. Speziell entwickelt für maschinelles Schneiden und Füllen von Buchteln und Hefegebäcken."
        }
      },
      {
        id: "sv-kajszi-10kg",
        category: "sutesallo",
        names: {
          hu: "SV Sütésálló Kajszibarack Ízű Készítmény",
          en: "SV Bake-Stable Apricot Preparation",
          de: "SV Backstabile Aprikosenzubereitung"
        },
        badge: { hu: "200°C HŐTŰRŐ • GÉLÁLLÓ", en: "200°C HEAT-STABLE • GEL", de: "200°C HITZEFEST • GEL" },
        pack: "10 kg kartondoboz",
        specs: {
          brix: "60–64° Brix",
          ph: "3.2 – 3.5",
          heat: "≥ 200 °C (Formamegtartó)",
          shelfLife: "12 hónap / months",
          sliceability: { hu: "Késálló, tiszta vágási él", en: "Firm gel, clean cut edge", de: "Fester Gelkörper, saubere Kante" }
        },
        desc: {
          hu: "Intenzív kajszibarack ízvilágú, aranysárga színű forma- és alaktartó gél. Leveles tészták, piték és finompékáruk magas hőfokú sütéséhez.",
          en: "Vibrant golden apricot flavor gel. Maintains sharp geometry and volume in high-temperature puff pastry, pies, and Danish pastries.",
          de: "Intensiver Aprikosengeschmack mit goldgelber Farbe. Behält Form und Volumen beim Hochtemperaturbacken in Blätterteig und Kuchen."
        }
      },
      {
        id: "sv-malna-5kg",
        category: "kenheto",
        names: {
          hu: "SV Málna Ízű Gyümölcskészítmény",
          en: "SV Raspberry Confectionery Preparation",
          de: "SV Himbeer-Fruchtzubereitung"
        },
        badge: { hu: "HIDEGEN KENHETŐ • VÖDRÖS", en: "COLD SPREADABLE • BUCKET", de: "KALT STREICHFÄHIG • EIMER" },
        pack: "5 kg műanyag vödör",
        specs: {
          brix: "65° Brix",
          ph: "3.2 – 3.4",
          heat: "Hideg technológia / Cold process",
          shelfLife: "9 hónap / months",
          sliceability: { hu: "Selymes, homogén kenhetőség", en: "Smooth, velvety spreadability", de: "Seidig-glatte Streichfähigkeit" }
        },
        desc: {
          hu: "Homogén állagú, hidegen könnyen kenhető málnás gyümölcskészítmény piskótatekercsek, linzer sütemények és tortalapok összetöltéséhez.",
          en: "Smooth, cold-spreadable raspberry preparation designed for sponge cake layering, linzer cookies, and premium confectionery fillings.",
          de: "Homogene, kalt streichfähige Himbeerzubereitung für Biskuitrouladen, Linzer Plätzchen und Tortenfüllungen."
        }
      },
      {
        id: "sv-afonya-5kg",
        category: "kenheto",
        names: {
          hu: "SV Áfonya Ízű Gyümölcskészítmény",
          en: "SV Blueberry Confectionery Preparation",
          de: "SV Heidelbeer-Fruchtzubereitung"
        },
        badge: { hu: "PRÉMIUM AROMA • HIDEG STABIL", en: "PREMIUM AROMA • COLD STABLE", de: "PREMIUM AROMA • KALTSTABIL" },
        pack: "5 kg műanyag vödör",
        specs: {
          brix: "65° Brix",
          ph: "3.2 – 3.5",
          heat: "Hideg technológia / Cold process",
          shelfLife: "9 hónap / months",
          sliceability: { hu: "Kiváló tapadás és eloszlás", en: "Superior adhesion & spread", de: "Hervorragende Haftung & Verlauf" }
        },
        desc: {
          hu: "Mélybordó-kékes árnyalatú, gazdag erdei áfonya karakterű gyümölcsbetét prémium desszertekhez, fánkokhoz és cukrászati termékekhez.",
          en: "Deep purple-blue hue with rich wild blueberry profile. Designed for premium dessert inserts, donut injecting, and patisserie glazing.",
          de: "Tiefblau-violette Farbe mit vollem Waldheidelbeer-Aroma. Konzipiert für Premium-Desserts, Berliner-Injektionen und Konditoreiwaren."
        }
      },
      {
        id: "sv-extra-meggy-10kg",
        category: "sutesallo",
        names: {
          hu: "SV Sütésálló Extra Meggy Töltelék",
          en: "SV Bake-Stable Extra Sour Cherry Filling",
          de: "SV Backstabile Extra-Sauerkirschfüllung"
        },
        badge: { hu: "DARABOS GYÜMÖLCS • SÜTÉSÁLLÓ", en: "FRUIT PIECES • BAKE-STABLE", de: "FRUCHTSTÜCKE • BACKSTABIL" },
        pack: "10 kg karton / 5 kg vödör",
        specs: {
          brix: "60–63° Brix",
          ph: "3.1 – 3.4",
          heat: "≥ 195 °C",
          shelfLife: "12 hónap / months",
          sliceability: { hu: "Formamegtartó, nem folyós", en: "Shape-retaining pieces, non-bleeding", de: "Formbeständige Stücke, kein Auslaufen" }
        },
        desc: {
          hu: "Kellemesen fanyar, valódi fekete és cigánymeggy szemekkel készült prémium töltelék rétesekhez, pitékhez és dán pékárukhoz.",
          en: "Pleasantly tart, rich sour cherry filling with intact fruit pieces. Formulated for strudels, rustic pies, and Danish pastries.",
          de: "Angenehm herbe, vollaromatische Sauerkirschfüllung mit ganzen Fruchtstücken für Strudel, Kuchen und Plunder."
        }
      },
      {
        id: "sv-egzotik-mango-5kg",
        category: "egyedi",
        names: {
          hu: "SV Egzotikus Mangó-Maracuja Töltelék",
          en: "SV Exotic Mango-Passionfruit Filling",
          de: "SV Exotische Mango-Maracuja-Füllung"
        },
        badge: { hu: "INNOVATÍV R&D • EGYEDI", en: "INNOVATIVE R&D • CUSTOM", de: "INNOVATIVE F&E • SONDERREZEPTUR" },
        pack: "5 kg vödör / 200 kg tartály",
        specs: {
          brix: "60–65° Brix (állítható)",
          ph: "3.2 – 3.5",
          heat: "180 °C – 210 °C (igény szerint)",
          shelfLife: "9–12 hónap / months",
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

      // Update switcher button styles
      ['hu', 'en', 'de'].forEach(l => {
        const btn = document.getElementById(`lang-${l}`);
        if (l === lang) {
          btn.className = "px-2 py-1 rounded font-bold transition-all bg-[#5F2125] text-white shadow-sm";
        } else {
          btn.className = "px-2 py-1 rounded font-medium text-stone-600 hover:text-[#E36527] transition-all";
        }
      });

      // Update static text elements with data-i18n
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (translations[lang][key]) {
          el.innerText = translations[lang][key];
        }
      });

      // Re-render dynamic components
      renderCatalogTab();
      renderProducts();

      // Re-init lucide icons
      lucide.createIcons();
    }

    // ---------------------------------------------------------------------------
    // KATALÓGUS TAB HANDLER
    // ---------------------------------------------------------------------------
    function switchCatalogTab(tabKey) {
      currentCatalogTab = tabKey;
      
      // Update tab buttons
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

      // Apps list
      const appsContainer = document.getElementById('cat-apps');
      appsContainer.innerHTML = data.apps.map(app => `
        <span class="px-2.5 py-1 rounded-md text-xs font-mono-spec bg-stone-100 text-stone-800 border border-stone-200">${app}</span>
      `).join('');

      // Specs
      const specsContainer = document.getElementById('cat-specs');
      specsContainer.innerHTML = `
        <div>
          <div class="text-[10px] text-stone-500 uppercase">${currentLang === 'de' ? 'HITZESTABILITÄT' : currentLang === 'en' ? 'HEAT STABILITY' : 'HŐTŰRÉS'}</div>
          <div class="font-bold text-emerald-700 text-sm mt-0.5">${data.specs.heat}</div>
        </div>
        <div>
          <div class="text-[10px] text-stone-500 uppercase">${currentLang === 'de' ? 'TROCKENSUBSTANZ' : currentLang === 'en' ? 'DRY MATTER' : 'SZÁRAZANYAG'}</div>
          <div class="font-bold text-stone-900 text-sm mt-0.5">${data.specs.brix}</div>
        </div>
        <div>
          <div class="text-[10px] text-stone-500 uppercase">${currentLang === 'de' ? 'GEBINDE' : currentLang === 'en' ? 'PACKAGING' : 'KISZERELÉS'}</div>
          <div class="font-bold text-stone-900 text-sm mt-0.5">${data.specs.pack}</div>
        </div>
      `;

      // Image & caption
      const img = document.getElementById('cat-image');
      img.src = data.image;
      document.getElementById('cat-img-caption').innerText = data.caption;

      // TDS button click
      const tdsBtn = document.getElementById('cat-tds-btn');
      tdsBtn.onclick = () => openTdsModal(data.tdsIndex);
    }

    // ---------------------------------------------------------------------------
    // PRODUCT MATRIX RENDERER
    // ---------------------------------------------------------------------------
    function renderProducts() {
      const container = document.getElementById('product-list');
      if (!container) return;

      container.innerHTML = products.map((p, idx) => `
        <div class="rounded-2xl border p-6 bg-white flex flex-col justify-between transition-all hover:shadow-md hover:border-[#E36527]/40" style="border-color: var(--sv-border);">
          <div class="space-y-3">
            
            <div class="flex items-center justify-between flex-wrap gap-1.5">
              <span class="text-[10px] font-mono-spec font-bold px-2 py-0.5 rounded border tracking-wider uppercase"
                    style="background-color: rgba(95, 33, 37, 0.05); color: var(--sv-burgundy); border-color: var(--sv-border);">
                ${p.badge[currentLang] || p.badge.hu}
              </span>
              <span class="text-[11px] font-mono-spec text-stone-500">${p.pack}</span>
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
                <span class="text-stone-500">${currentLang === 'de' ? 'Hitzestabilität' : currentLang === 'en' ? 'Heat resistance' : 'Hőtűrés'}:</span>
                <span class="font-bold text-emerald-700">${p.specs.heat}</span>
              </div>
            </div>

          </div>

          <div class="pt-4 mt-4 border-t flex items-center justify-between gap-3" style="border-color: var(--sv-border-light);">
            <button onclick="openTdsModal(${idx})" 
                    class="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-lg text-xs font-semibold font-mono-spec transition-all border hover:bg-stone-50"
                    style="border-color: var(--sv-burgundy); color: var(--sv-burgundy);">
              <i data-lucide="file-text" class="w-3.5 h-3.5 text-[#E36527]"></i>
              <span>${currentLang === 'hu' ? 'TDS Adatlap' : currentLang === 'de' ? 'TDS Datenblatt' : 'TDS Sheet'}</span>
            </button>

            <a href="#mintakeres" class="text-xs font-semibold font-mono-spec text-[#E36527] hover:underline flex items-center gap-1">
              <i data-lucide="send" class="w-3 h-3"></i>
              <span>${currentLang === 'hu' ? 'Mintakérés' : currentLang === 'de' ? 'Muster' : 'Sample'}</span>
            </a>
          </div>
        </div>
      `).join('');
    }

    // ---------------------------------------------------------------------------
    // TDS MODAL HANDLER
    // ---------------------------------------------------------------------------
    function openTdsModal(productIndex) {
      const p = products[productIndex];
      if (!p) return;

      const modal = document.getElementById('tds-modal');
      const content = document.getElementById('tds-modal-content');

      content.innerHTML = `
        <div class="space-y-6">
          
          <div class="border-b pb-4">
            <div class="flex items-center gap-2 text-xs font-mono-spec text-[#E36527] font-semibold uppercase">
              <span>SUN VALLEY ZRT. • MÓR PLANT</span>
              <span>•</span>
              <span>QC DOCUMENT #TDS-2026</span>
            </div>
            <h2 class="font-syne font-bold text-2xl text-stone-900 mt-1">
              ${p.names[currentLang] || p.names.hu}
            </h2>
            <p class="text-xs font-mono-spec text-stone-500 mt-0.5">
              Termékkód: SV-${p.id.toUpperCase()} • Kiszerelés: ${p.pack}
            </p>
          </div>

          <div class="space-y-4 font-mono-spec text-xs">
            <h4 class="font-bold text-stone-900 uppercase text-[11px] tracking-wider text-stone-400">
              ${currentLang === 'de' ? 'PHYSIKO-CHEMISCHE LABORWERTE' : currentLang === 'en' ? 'LABORATORY SPECIFICATIONS' : 'LABORATÓRIUMI PARAMÉTEREK'}
            </h4>

            <div class="grid grid-cols-2 gap-2 border rounded-xl p-3 bg-stone-50" style="border-color: var(--sv-border-light);">
              <div class="py-1 border-b border-stone-200">
                <span class="text-stone-500">Refraktometriás Brix:</span>
                <span class="font-bold text-stone-900 block mt-0.5">${p.specs.brix}</span>
              </div>
              <div class="py-1 border-b border-stone-200">
                <span class="text-stone-500">pH Érték (20°C):</span>
                <span class="font-bold text-stone-900 block mt-0.5">${p.specs.ph}</span>
              </div>
              <div class="py-1 border-b border-stone-200">
                <span class="text-stone-500">Hőtűrési küszöb:</span>
                <span class="font-bold text-emerald-700 block mt-0.5">${p.specs.heat}</span>
              </div>
              <div class="py-1 border-b border-stone-200">
                <span class="text-stone-500">Szavatossági idő:</span>
                <span class="font-bold text-stone-900 block mt-0.5">${p.specs.shelfLife}</span>
              </div>
              <div class="py-1 col-span-2">
                <span class="text-stone-500">Szeletelhetőség & Viszkozitás:</span>
                <span class="font-bold text-stone-900 block mt-0.5">${p.specs.sliceability[currentLang] || p.specs.sliceability.hu}</span>
              </div>
            </div>

            <div class="space-y-1.5 pt-2">
              <h5 class="font-bold text-stone-900 uppercase text-[10px] tracking-wider text-stone-400">
                ${currentLang === 'de' ? 'MIKROBIOLOGIE & ALLERGENE' : currentLang === 'en' ? 'MICROBIOLOGY & ALLERGEN STATUS' : 'MIKROBIOLÓGIA & ALLERGÉN STÁTUSZ'}
              </h5>
              <p class="text-stone-600 text-xs">
                Összcsíraszám: &lt; 1000 CFU/g • Élesztő & Penész: &lt; 100 CFU/g • Salmonella: Negatív/25g • Gluténmentes, Vegán formula, Természetes színezék.
              </p>
            </div>

            <div class="p-3.5 rounded-xl border bg-amber-50/70 border-amber-200 text-stone-700 text-xs space-y-1">
              <div class="font-bold text-stone-900">Ipari Próbagyártási Paritás:</div>
              <p class="text-[11px] leading-relaxed">
                A fenti műszaki specifikáció kiindulási referencia. Egyedi gyártósorokhoz (hőfok, sütési idő, viszkozitás) móri laboratóriumunk díjmentesen elvégzi a finomhangolást.
              </p>
            </div>

          </div>

          <div class="pt-4 border-t flex flex-wrap items-center justify-between gap-3" style="border-color: var(--sv-border-light);">
            <a href="#mintakeres" onclick="closeTdsModal()" 
               class="px-5 py-2.5 rounded-xl font-bold text-xs shadow text-white flex items-center gap-2"
               style="background-color: var(--sv-orange);">
              <i data-lucide="package-check" class="w-4 h-4"></i>
              <span>Minta Igénylése Ebből a Termékből</span>
            </a>

            <button onclick="closeTdsModal()" class="px-4 py-2.5 rounded-xl border font-mono-spec text-xs text-stone-600 hover:bg-stone-50">
              Bezárás
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

    // Sample Form Submission
    function handleSampleSubmit(e) {
      e.preventDefault();
      const msg = document.getElementById('form-success-message');
      msg.classList.remove('hidden');
      e.target.reset();
      setTimeout(() => {
        msg.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }, 100);
    }

    // ---------------------------------------------------------------------------
    // VIBE-CODING / LIVE THEME CUSTOMIZER ENGINE
    // ---------------------------------------------------------------------------
    function toggleVibePanel() {
      const panel = document.getElementById('vibe-panel');
      panel.classList.toggle('hidden');
    }

    function updateCustomColor(variable, value) {
      document.documentElement.style.setProperty(variable, value);
    }

    const themePresets = {
      classic: {
        '--sv-burgundy': '#5F2125',
        '--sv-burgundy-dark': '#451C1B',
        '--sv-orange': '#E36527',
        '--sv-green-dark': '#2D3628',
        '--sv-paper-cream': '#F5F2EE'
      },
      harvest: {
        '--sv-burgundy': '#6E262A',
        '--sv-burgundy-dark': '#4E1B1E',
        '--sv-orange': '#D96B27',
        '--sv-green-dark': '#3A4833',
        '--sv-paper-cream': '#FAF7F2'
      },
      modern: {
        '--sv-burgundy': '#3B181A',
        '--sv-burgundy-dark': '#281012',
        '--sv-orange': '#EA580C',
        '--sv-green-dark': '#1C2618',
        '--sv-paper-cream': '#F4F4F5'
      }
    };

    function applyPreset(name) {
      const preset = themePresets[name];
      if (!preset) return;
      for (const [key, val] of Object.entries(preset)) {
        document.documentElement.style.setProperty(key, val);
      }
      document.getElementById('picker-burgundy').value = preset['--sv-burgundy'];
      document.getElementById('picker-orange').value = preset['--sv-orange'];
      document.getElementById('picker-green').value = preset['--sv-green-dark'];
      document.getElementById('picker-cream').value = preset['--sv-paper-cream'];
    }

    function resetColors() {
      applyPreset('classic');
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

# Write to index_v2.html
with open(r"c:\Users\csern\Desktop\sun valley\prototypes\sun-valley-b2b\index_v2.html", "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

# Also update index.html to point to v2
with open(r"c:\Users\csern\Desktop\sun valley\prototypes\sun-valley-b2b\index.html", "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print("Successfully written index_v2.html and synchronized index.html!")
