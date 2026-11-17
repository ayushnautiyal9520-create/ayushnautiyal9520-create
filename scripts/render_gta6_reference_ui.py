"""
GTA VI Reference UI Vector Generator - Refined Edition
100% Faithful to User's Reference Screenshot:
1. gta6-hero-banner.svg: Detailed sunset skyline, high-stance sports car, tall curved palms, glowing red taillights, status pill, ticker.
2. The 4 action buttons (2x2 grid layout, generous widths, 0 text clipping):
   - btn-hud.svg: [LIVE HUD UI | EXPLORE INTERACTIVE RADAR ↗]
   - btn-portfolio.svg: [PORTFOLIO | GRYVEN.VERCEL.APP ↗]
   - btn-github.svg: [GITHUB | AYUSHNAUTIYAL9520-CREATE ↗]
   - btn-dispatch.svg: [DISPATCH | AYUSHNAUTIYAL8936-GMAIL.COM ↗]
3. gta6-heatmap.svg: Sunset skyline + palm tree background on right, 4,689 contributions, Jan 3 - Nov 17, 2026.
4. gta6-batches-showcase.svg: Perfect non-overlapping title, glowing icon badges, pink/orange/cyan columns.
STRICT: ZERO EMOJIS, 100% VALID XML.
"""

import json
import xml.etree.ElementTree as ET
from pathlib import Path

def escape_xml(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")

# ==============================================================================
# 1. HERO BANNER SVG (Sunset, Skyline, Sports Car, Palms, Ticker)
# ==============================================================================
def render_hero_banner():
    width = 960
    height = 240

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <!-- Outer Card Border Gradient -->
    <linearGradient id="hero-card-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff007f" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#ff5e00" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#00f0ff" stop-opacity="0.8" />
    </linearGradient>

    <!-- Sunset Sky Gradient for Scenic Right Half -->
    <linearGradient id="sunset-sky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1b0326" />
      <stop offset="25%" stop-color="#5a084c" />
      <stop offset="55%" stop-color="#be116a" />
      <stop offset="75%" stop-color="#ff501e" />
      <stop offset="90%" stop-color="#ff9020" />
      <stop offset="100%" stop-color="#ffd240" />
    </linearGradient>

    <!-- Water Surface Gradient -->
    <linearGradient id="sunset-water" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ff3b68" stop-opacity="0.6" />
      <stop offset="40%" stop-color="#550944" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#0d021a" />
    </linearGradient>

    <!-- Giant Sun Gradient -->
    <radialGradient id="sun-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="35%" stop-color="#ffe666" />
      <stop offset="70%" stop-color="#ff6611" />
      <stop offset="100%" stop-color="#be116a" stop-opacity="0" />
    </radialGradient>

    <!-- Title Nautiyal Gradient -->
    <linearGradient id="title-nautiyal-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff007f" />
      <stop offset="100%" stop-color="#ff2e9e" />
    </linearGradient>

    <!-- Clip Path for Inside the Rounded Card -->
    <clipPath id="hero-clip">
      <rect x="0" y="0" width="{width}" height="{height}" rx="12" ry="12" />
    </clipPath>

    <style>
      .font-display {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      }}
      .font-mono {{
        font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, Menlo, monospace;
      }}
      .hero-title-ayush {{
        font-size: 42px;
        font-weight: 900;
        font-style: italic;
        fill: #ffffff;
        letter-spacing: 1px;
      }}
      .hero-title-nautiyal {{
        font-size: 42px;
        font-weight: 900;
        font-style: italic;
        fill: url(#title-nautiyal-grad);
        letter-spacing: 1px;
      }}
      .hero-sub {{
        font-size: 11.5px;
        font-weight: 700;
        fill: #cbd5e1;
        letter-spacing: 1.6px;
      }}
      .status-text {{
        font-size: 10.5px;
        font-weight: 800;
        fill: #f8fafc;
        letter-spacing: 1.2px;
      }}
      .ticker-box {{
        fill: #0c031a;
        stroke: rgba(255, 0, 127, 0.35);
        stroke-width: 1.2;
        rx: 6px;
        ry: 6px;
      }}
      .ticker-text {{
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.8px;
        fill: #cbd5e1;
      }}
    </style>
  </defs>

  <g clip-path="url(#hero-clip)">
    <!-- Base Canvas -->
    <rect width="{width}" height="{height}" fill="#0a0214" />

    <!-- Right Side Scenic Background (Sunset over Vice City) -->
    <g transform="translate(410, 0)">
      <!-- Sunset Sky -->
      <rect x="0" y="0" width="550" height="175" fill="url(#sunset-sky)" />

      <!-- Giant Setting Sun in Center-Right of Scene -->
      <circle cx="270" cy="110" r="58" fill="url(#sun-glow)" opacity="0.95" />

      <!-- Vice City Skyline Silhouettes -->
      <path d="M 0 160 
               L 35 160 L 35 135 L 50 135 L 50 160 
               L 75 160 L 75 120 L 85 108 L 92 108 L 98 120 L 98 160 
               L 115 160 L 115 100 L 130 100 L 130 160 
               L 145 160 L 145 125 L 160 125 L 160 160 
               L 175 160 L 175 90 L 182 72 L 186 72 L 194 90 L 194 160 
               L 210 160 L 210 115 L 222 115 L 222 160 
               L 240 160 L 240 120 L 252 120 L 252 160 
               L 270 160 L 270 105 L 282 105 L 282 160 
               L 300 160 L 300 95 L 314 95 L 314 160 
               L 335 160 L 335 130 L 350 130 L 350 160 
               L 370 160 L 370 110 L 385 110 L 385 160 
               L 415 160 L 415 125 L 435 125 L 435 160 
               L 550 160 L 550 175 L 0 175 Z" fill="#1b0326" />

      <!-- Windows Lights in Skyline -->
      <circle cx="82" cy="130" r="1.2" fill="#00f0ff" opacity="0.8" />
      <circle cx="122" cy="115" r="1.2" fill="#ffd544" opacity="0.9" />
      <circle cx="122" cy="125" r="1.2" fill="#00f0ff" opacity="0.7" />
      <circle cx="188" cy="98" r="1.4" fill="#ffd544" opacity="0.9" />
      <circle cx="188" cy="118" r="1.2" fill="#ffffff" opacity="0.8" />
      <circle cx="276" cy="118" r="1.2" fill="#00f0ff" opacity="0.7" />
      <circle cx="308" cy="110" r="1.2" fill="#ffd544" opacity="0.8" />

      <!-- Water Surface with Sunset Reflection -->
      <rect x="0" y="160" width="550" height="25" fill="url(#sunset-water)" />
      
      <!-- Horizontal Water Shimmer Lines -->
      <line x1="200" y1="165" x2="330" y2="165" stroke="#ffd544" stroke-width="1.4" opacity="0.7" />
      <line x1="230" y1="170" x2="310" y2="170" stroke="#ff7722" stroke-width="1.4" opacity="0.8" />
      <line x1="160" y1="173" x2="370" y2="173" stroke="#ff007f" stroke-width="0.9" opacity="0.6" />

      <!-- White Retro Sports Car / Supercar (Detailed Rear 3/4 View) -->
      <g transform="translate(325, 122)">
        <!-- Ground Shadow -->
        <ellipse cx="105" cy="58" rx="85" ry="9" fill="#06010c" opacity="0.95" />
        
        <!-- Car Silhouette & Main White Body Shell -->
        <path d="M 22 45 
                 C 38 32, 65 16, 95 13 
                 C 132 10, 158 20, 174 34 
                 L 198 38 
                 C 205 42, 206 48, 202 52 
                 L 22 52 
                 C 18 48, 20 46, 22 45 Z" fill="#f1f5f9" />
        
        <!-- Cabin Glass & Pillars (Tinted Sunset Violet) -->
        <path d="M 55 40 L 92 18 L 142 18 L 162 40 Z" fill="#180424" />
        <path d="M 98 20 L 138 20 L 156 39 L 98 39 Z" fill="#29073b" />

        <!-- Rear Trunk & Spoiler Lip -->
        <path d="M 152 38 L 202 40 L 204 46 L 152 46 Z" fill="#cbd5e1" />

        <!-- Full-Width Glowing Red Neon Taillight Bar -->
        <rect x="170" y="44" width="34" height="4.5" rx="1.5" fill="#ff0033" />
        <rect x="173" y="45" width="28" height="2.5" rx="1" fill="#ff99aa" />
        <line x1="170" y1="46" x2="204" y2="46" stroke="#ffffff" stroke-width="0.8" />

        <!-- Lower Bumper Diffuser (Black) -->
        <path d="M 166 49 L 203 49 L 201 54 L 166 54 Z" fill="#0f172a" />
        
        <!-- Twin Exhaust Tips -->
        <circle cx="174" cy="52" r="1.8" fill="#94a3b8" />
        <circle cx="182" cy="52" r="1.8" fill="#94a3b8" />

        <!-- Wheels / Tires -->
        <ellipse cx="50" cy="51" rx="12" ry="10" fill="#0f0518" />
        <circle cx="50" cy="51" r="5" fill="#475569" />
        <ellipse cx="170" cy="53" rx="14" ry="11" fill="#0f0518" />
        <circle cx="170" cy="53" r="6" fill="#64748b" />
      </g>

      <!-- Palm Trees on Far Right -->
      <!-- Main Palm Tree -->
      <g transform="translate(480, 25)">
        <path d="M 22 150 Q 15 80, -2 15" stroke="#12011a" stroke-width="5.5" fill="none" stroke-linecap="round" />
        <!-- Detailed Fan Fronds -->
        <path d="M -2 15 Q -35 -2, -65 12" stroke="#12011a" stroke-width="3.5" fill="none" />
        <path d="M -2 15 Q -25 -25, -55 -22" stroke="#12011a" stroke-width="3.5" fill="none" />
        <path d="M -2 15 Q 5 -38, -5 -60" stroke="#12011a" stroke-width="3.5" fill="none" />
        <path d="M -2 15 Q 30 -25, 55 -15" stroke="#12011a" stroke-width="3.5" fill="none" />
        <path d="M -2 15 Q 40 5, 55 25" stroke="#12011a" stroke-width="3.5" fill="none" />
      </g>
      <!-- Background Palm Tree -->
      <g transform="translate(440, 50)">
        <path d="M 12 125 Q 8 65, -5 18" stroke="#1c0328" stroke-width="3.8" fill="none" stroke-linecap="round" />
        <path d="M -5 18 Q -28 2, -45 14" stroke="#1c0328" stroke-width="2.6" fill="none" />
        <path d="M -5 18 Q -18 -20, -38 -20" stroke="#1c0328" stroke-width="2.6" fill="none" />
        <path d="M -5 18 Q 12 -28, 8 -45" stroke="#1c0328" stroke-width="2.6" fill="none" />
        <path d="M -5 18 Q 28 -14, 45 -2" stroke="#1c0328" stroke-width="2.6" fill="none" />
      </g>
    </g>

    <!-- Palm Trees on Left Background -->
    <g transform="translate(10, 15)">
      <path d="M 10 165 Q 28 90, 52 20" stroke="#12011a" stroke-width="6" fill="none" stroke-linecap="round" />
      <path d="M 52 20 Q 20 -2, -15 10" stroke="#12011a" stroke-width="3.5" fill="none" />
      <path d="M 52 20 Q 25 -25, 5 -32" stroke="#12011a" stroke-width="3.5" fill="none" />
      <path d="M 52 20 Q 65 -35, 55 -55" stroke="#12011a" stroke-width="3.5" fill="none" />
      <path d="M 52 20 Q 85 -20, 105 -8" stroke="#12011a" stroke-width="3.5" fill="none" />
      <path d="M 52 20 Q 90 12, 100 30" stroke="#12011a" stroke-width="3.5" fill="none" />
    </g>
    <g transform="translate(58, 42)">
      <path d="M 10 138 Q 22 80, 38 22" stroke="#1b0328" stroke-width="4.5" fill="none" stroke-linecap="round" />
      <path d="M 38 22 Q 12 2, -15 10" stroke="#1b0328" stroke-width="2.8" fill="none" />
      <path d="M 38 22 Q 18 -20, 0 -28" stroke="#1b0328" stroke-width="2.8" fill="none" />
      <path d="M 38 22 Q 50 -25, 45 -42" stroke="#1b0328" stroke-width="2.8" fill="none" />
      <path d="M 38 22 Q 68 -15, 82 -2" stroke="#1b0328" stroke-width="2.8" fill="none" />
    </g>

    <!-- Dark Gradient Shade over Left Half for Text Contrast -->
    <rect x="0" y="0" width="480" height="{height}" fill="url(#hero-shade)" />
    <linearGradient id="hero-shade" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#080112" stop-opacity="0.98" />
      <stop offset="70%" stop-color="#0a0216" stop-opacity="0.92" />
      <stop offset="100%" stop-color="#0a0216" stop-opacity="0" />
    </linearGradient>

    <!-- Left Header Content -->
    <g transform="translate(42, 26)">
      <!-- Main Title: AYUSH NAUTIYAL -->
      <text x="0" y="52" class="font-display">
        <tspan class="hero-title-ayush">AYUSH </tspan>
        <tspan class="hero-title-nautiyal">NAUTIYAL</tspan>
      </text>

      <!-- Subtitle -->
      <text x="2" y="78" class="font-mono hero-sub">FULL-STACK SAAS ARCHITECT <tspan fill="#ff007f">//</tspan> CODE ENFORCEMENT</text>

      <!-- Status Pill -->
      <g transform="translate(2, 95)">
        <circle cx="7" cy="7" r="4.5" fill="#00ff88" />
        <circle cx="7" cy="7" r="7" fill="#00ff88" opacity="0.3" />
        <text x="22" y="11" class="font-mono status-text">STATUS: PRODUCTION ACTIVE</text>
      </g>
    </g>

    <!-- Bottom Ticker Bar -->
    <g transform="translate(42, 178)">
      <rect x="0" y="0" width="{width - 84}" height="38" class="ticker-box" />
      
      <!-- Left Accent Notch -->
      <path d="M 0 0 L 4 0 L 4 38 L 0 38 Z" fill="#ff007f" />
      
      <!-- Metrics text -->
      <text x="24" y="23" class="font-mono ticker-text">
        TARGET TOTAL: <tspan fill="#ff007f" font-weight="900">4,689 CONTRIBUTIONS</tspan>
        <tspan fill="#475569">   |   </tspan>
        SPAN: <tspan fill="#ffffff" font-weight="800">JAN 03 -&gt; NOV 17, 2026</tspan>
        <tspan fill="#475569">   |   </tspan>
        UNBROKEN STREAK: <tspan fill="#ffd700" font-weight="900">78 DAYS</tspan>
        <tspan fill="#475569">   |   </tspan>
        COUNTDOWN: <tspan fill="#00f0ff" font-weight="900">DAY 319 / 365</tspan>
      </text>
    </g>
  </g>

  <!-- Card Outer Border -->
  <rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="11" ry="11" fill="none" stroke="url(#hero-card-border)" stroke-width="1.8" />
</svg>
"""

    out_file = Path("gta6-hero-banner.svg")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(svg_content)

    ET.fromstring(svg_content)
    print(f"Generated pixel-perfect gta6-hero-banner.svg ({width}x{height})")


# ==============================================================================
# 2. THE 4 CUSTOM 2-TONE ACTION BUTTONS (2x2 Grid Friendly, Zero Clipping)
# ==============================================================================
def render_action_buttons():
    # Widths sized generously so text never clips
    buttons = [
        {
            "filename": "btn-hud.svg",
            "tag_icon": "radar",
            "tag_text": "LIVE HUD UI",
            "tag_width": 105,
            "action_text": "EXPLORE INTERACTIVE RADAR",
            "action_bg": "#ff007f",
            "action_text_color": "#ffffff",
            "total_width": 315
        },
        {
            "filename": "btn-portfolio.svg",
            "tag_icon": "vercel",
            "tag_text": "PORTFOLIO",
            "tag_width": 98,
            "action_text": "GRYVEN.VERCEL.APP",
            "action_bg": "#ff5e00",
            "action_text_color": "#ffffff",
            "total_width": 250
        },
        {
            "filename": "btn-github.svg",
            "tag_icon": "github",
            "tag_text": "GITHUB",
            "tag_width": 88,
            "action_text": "AYUSHNAUTIYAL9520-CREATE",
            "action_bg": "#00f0ff",
            "action_text_color": "#06020c",
            "total_width": 295
        },
        {
            "filename": "btn-dispatch.svg",
            "tag_icon": "mail",
            "tag_text": "DISPATCH",
            "tag_width": 95,
            "action_text": "AYUSHNAUTIYAL8936-GMAIL.COM",
            "action_bg": "#ffd700",
            "action_text_color": "#06020c",
            "total_width": 315
        }
    ]

    height = 36

    for btn in buttons:
        w = btn["total_width"]
        fn = btn["filename"]
        tag_w = btn["tag_width"]
        action_w = w - tag_w - 4

        # Vector Icons inside Tag
        if btn["tag_icon"] == "radar":
            icon_svg = '<circle cx="16" cy="18" r="6" stroke="#ffffff" stroke-width="1.2" fill="none"/><line x1="16" y1="12" x2="16" y2="24" stroke="#ffffff" stroke-width="1"/><line x1="10" y1="18" x2="22" y2="18" stroke="#ffffff" stroke-width="1"/><circle cx="18" cy="16" r="1.5" fill="#ff007f"/>'
        elif btn["tag_icon"] == "vercel":
            icon_svg = '<polygon points="16,13 22,23 10,23" fill="#ffffff"/>'
        elif btn["tag_icon"] == "github":
            icon_svg = '<path d="M 16 11 C 12.7 11 10 13.7 10 17 C 10 19.6 11.7 21.8 14 22.6 C 14.3 22.7 14.4 22.5 14.4 22.3 L 14.4 21.2 C 12.7 21.6 12.4 20.4 12.4 20.4 C 12.1 19.7 11.7 19.5 11.7 19.5 C 11.1 19.1 11.7 19.1 11.7 19.1 C 12.3 19.1 12.7 19.7 12.7 19.7 C 13.2 20.6 14.1 20.4 14.4 20.2 C 14.5 19.8 14.6 19.5 14.8 19.3 C 13.5 19.1 12.1 18.6 12.1 16.3 C 12.1 15.6 12.3 15.1 12.7 14.7 C 12.6 14.5 12.4 13.8 12.8 12.9 C 12.8 12.9 13.4 12.7 14.8 13.6 C 15.4 13.4 16 13.3 16.6 13.3 C 17.2 13.3 17.8 13.4 18.4 13.6 C 19.8 12.7 20.4 12.9 20.4 12.9 C 20.8 13.8 20.6 14.5 20.5 14.7 C 20.9 15.1 21.1 15.6 21.1 16.3 C 21.1 18.6 19.7 19.1 18.4 19.3 C 18.6 19.5 18.8 19.9 18.8 20.5 L 18.8 22.3 C 18.8 22.5 18.9 22.7 19.2 22.6 C 21.5 21.8 23.2 19.6 23.2 17 C 23.2 13.7 20.5 11 17.2 11 Z" fill="#ffffff"/>'
        else: # mail
            icon_svg = '<rect x="10" y="13" width="12" height="10" rx="1.5" stroke="#ffffff" stroke-width="1.2" fill="none"/><polyline points="10,14 16,18.5 22,14" stroke="#ffffff" stroke-width="1.2" fill="none"/>'

        svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {height}" width="{w}" height="{height}">
  <style>
    .btn-font {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif; }}
    .tag-text {{ font-size: 10px; font-weight: 800; fill: #f8fafc; letter-spacing: 1px; }}
    .act-text {{ font-size: 10px; font-weight: 900; fill: {btn['action_text_color']}; letter-spacing: 0.8px; }}
  </style>
  
  <!-- Left Pill (Dark Tag) -->
  <rect x="0" y="0" width="{tag_w}" height="{height}" rx="6" fill="#140924" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1" />
  {icon_svg}
  <text x="{32 if btn['tag_icon'] != 'github' else 30}" y="22" class="btn-font tag-text">{btn['tag_text']}</text>

  <!-- Right Pill (Neon Action with ↗) -->
  <g transform="translate({tag_w + 3}, 0)">
    <rect x="0" y="0" width="{action_w}" height="{height}" rx="6" fill="{btn['action_bg']}" />
    <text x="14" y="22" class="btn-font act-text">{btn['action_text']}</text>
    <!-- Arrow ↗ -->
    <path d="M {action_w - 20} 21 L {action_w - 12} 13 M {action_w - 18} 13 L {action_w - 12} 13 L {action_w - 12} 19" stroke="{btn['action_text_color']}" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round" />
  </g>
</svg>
"""
        with open(fn, "w", encoding="utf-8") as f:
            f.write(svg_content)
        ET.fromstring(svg_content)
        print(f"Generated valid button {fn} ({w}x{height})")


# ==============================================================================
# 3. HEATMAP SVG WITH VICE CITY RIGHT-SIDE SKYLINE SCENE
# ==============================================================================
def render_heatmap_svg():
    data_file = Path("data/contributions.json")
    if not data_file.exists():
        print("data/contributions.json not found.")
        return

    with open(data_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    days = data.get("days", [])
    total = data.get("total_contributions", 4689)
    current_streak = data.get("current_streak", 78)
    best_day = data.get("best_day", {})

    width = 960
    height = 260
    cell_size = 12
    cell_gap = 4
    left_padding = 45
    top_padding = 90

    # Color Palette matching reference image:
    # 0: deep purple, 1: dark magenta, 2: vibrant pink, 3: hot pink, 4: orange, 5: gold
    HEATMAP_PALETTE = [
        "#1b0b2e",  # Level 0 - Void
        "#500c5c",  # Level 1 - Low heat
        "#9b0c72",  # Level 2 - Medium
        "#e50073",  # Level 3 - Active pink
        "#ff5e00",  # Level 4 - Sunset orange
        "#ffd000"   # Level 5 - Overdrive gold
    ]

    MONTH_NAMES = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

    svg_cells = []
    month_labels = []
    last_month = -1

    first_date_str = days[0]["date"] if days else "2026-01-03"
    import datetime
    first_dt = datetime.datetime.strptime(first_date_str, "%Y-%m-%d").date()
    first_day_col_row = (first_dt.weekday() + 1) % 7 # Sunday=0, Sat=6

    cur_col = 0
    cur_row = first_day_col_row

    for day in days:
        x = left_padding + cur_col * (cell_size + cell_gap)
        y = top_padding + cur_row * (cell_size + cell_gap)

        level = min(day.get("level", 0), len(HEATMAP_PALETTE) - 1)
        color = HEATMAP_PALETTE[level]
        date_str = day.get("date", "")
        count = day.get("count", 0)

        if date_str:
            month_idx = int(date_str.split("-")[1]) - 1
            if month_idx != last_month and cur_row in (0, 1):
                month_labels.append((x, MONTH_NAMES[month_idx]))
                last_month = month_idx

        tooltip_text = f"{count} contributions on {date_str}" if count > 0 else f"Strategic pause on {date_str}"
        tooltip_esc = escape_xml(tooltip_text)

        cell_svg = (
            f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" rx="2.5" ry="2.5" '
            f'fill="{color}"><title>{tooltip_esc}</title></rect>'
        )
        svg_cells.append(cell_svg)

        cur_row += 1
        if cur_row > 6:
            cur_row = 0
            cur_col += 1

    month_svg_elements = []
    for mx, mname in month_labels:
        month_svg_elements.append(f'<text x="{mx}" y="{top_padding - 12}" class="hud-label">{mname}</text>')

    day_svg_elements = [
        f'<text x="{left_padding - 14}" y="{top_padding + 1 * (cell_size + cell_gap) + 9}" class="hud-label" text-anchor="end">MON</text>',
        f'<text x="{left_padding - 14}" y="{top_padding + 3 * (cell_size + cell_gap) + 9}" class="hud-label" text-anchor="end">WED</text>',
        f'<text x="{left_padding - 14}" y="{top_padding + 5 * (cell_size + cell_gap) + 9}" class="hud-label" text-anchor="end">FRI</text>',
    ]

    legend_x = width - 210
    legend_y = height - 20
    legend_cells = []
    for i, pcolor in enumerate(HEATMAP_PALETTE):
        lx = legend_x + 40 + i * (cell_size + 3)
        legend_cells.append(f'<rect x="{lx}" y="{legend_y - 10}" width="{cell_size}" height="{cell_size}" rx="2" fill="{pcolor}" />')

    legend_svg = (
        f'<text x="{legend_x}" y="{legend_y}" class="hud-sub">LESS</text>'
        + "".join(legend_cells) +
        f'<text x="{legend_x + 40 + 6 * (cell_size + 3) + 4}" y="{legend_y}" class="hud-sub">MORE</text>'
    )

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <linearGradient id="heatmap-card-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff007f" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#ff5e00" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#00f0ff" stop-opacity="0.8" />
    </linearGradient>

    <!-- Sunset Gradient for Skyline Background on Right -->
    <linearGradient id="hm-sunset-sky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#2a0438" stop-opacity="0.4" />
      <stop offset="50%" stop-color="#a01264" stop-opacity="0.7" />
      <stop offset="85%" stop-color="#ff5511" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#ffd533" />
    </linearGradient>

    <clipPath id="hm-clip">
      <rect x="0" y="0" width="{width}" height="{height}" rx="12" ry="12" />
    </clipPath>

    <style>
      .font-display {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; }}
      .font-mono {{ font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, Menlo, monospace; }}
      
      .hm-title-num {{
        font-size: 26px;
        font-weight: 900;
        font-style: italic;
        fill: #ff007f;
        letter-spacing: 1px;
      }}
      .hm-title-text {{
        font-size: 26px;
        font-weight: 900;
        font-style: italic;
        fill: #ffffff;
        letter-spacing: 1.2px;
      }}
      .hm-subhead {{
        font-size: 11px;
        font-weight: 700;
        fill: #94a3b8;
        letter-spacing: 1.2px;
      }}
      .hud-label {{
        font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, Menlo, monospace;
        font-size: 10px;
        font-weight: 700;
        fill: #64748b;
        letter-spacing: 0.5px;
      }}
      .hud-sub {{
        font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, Menlo, monospace;
        font-size: 9.5px;
        font-weight: 700;
        fill: #64748b;
        letter-spacing: 0.6px;
      }}
      .footer-stat {{
        font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, Menlo, monospace;
        font-size: 11px;
        font-weight: 700;
        fill: #cbd5e1;
        letter-spacing: 0.8px;
      }}
    </style>
  </defs>

  <g clip-path="url(#hm-clip)">
    <!-- Base Background -->
    <rect width="{width}" height="{height}" fill="#0b0317" />

    <!-- Right Side Vice City Skyline Illustration -->
    <g transform="translate(680, 0)">
      <!-- Sunset Glow Backdrop -->
      <rect x="0" y="20" width="280" height="195" fill="url(#hm-sunset-sky)" opacity="0.65" />
      <ellipse cx="140" cy="180" rx="100" ry="25" fill="#ff4466" opacity="0.5" />

      <!-- City Skyline Silhouettes -->
      <path d="M 0 190 
               L 15 190 L 15 170 L 25 170 L 25 190 
               L 40 190 L 40 155 L 50 155 L 50 190 
               L 65 190 L 65 140 L 78 140 L 78 190 
               L 95 190 L 95 160 L 110 160 L 110 190 
               L 130 190 L 130 148 L 145 148 L 145 190 
               L 170 190 L 170 165 L 185 165 L 185 190 
               L 210 190 L 210 150 L 225 150 L 225 190 
               L 280 190 L 280 200 L 0 200 Z" fill="#13021f" />
      
      <!-- Palm Tree on the Far Right Edge -->
      <g transform="translate(230, 90)">
        <path d="M 12 110 Q 5 50, -10 10" stroke="#0e0117" stroke-width="5" fill="none" stroke-linecap="round" />
        <path d="M -10 10 Q -40 0, -60 12" stroke="#0e0117" stroke-width="3" fill="none" />
        <path d="M -10 10 Q -35 -20, -50 -20" stroke="#0e0117" stroke-width="3" fill="none" />
        <path d="M -10 10 Q 0 -35, -5 -50" stroke="#0e0117" stroke-width="3" fill="none" />
        <path d="M -10 10 Q 25 -20, 45 -10" stroke="#0e0117" stroke-width="3" fill="none" />
        <path d="M -10 10 Q 30 10, 40 25" stroke="#0e0117" stroke-width="3" fill="none" />
      </g>
    </g>

    <!-- Dark Gradient Shade to Protect Left Heatmap Readability -->
    <rect x="0" y="0" width="750" height="{height}" fill="url(#hm-shade)" />
    <linearGradient id="hm-shade" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0b0317" stop-opacity="1" />
      <stop offset="85%" stop-color="#0b0317" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#0b0317" stop-opacity="0" />
    </linearGradient>

    <!-- Header Titles -->
    <g transform="translate({left_padding}, 22)">
      <text x="0" y="24" class="font-display">
        <tspan class="hm-title-num">4,689 </tspan>
        <tspan class="hm-title-text">CONTRIBUTIONS IN THE LAST YEAR</tspan>
      </text>
      <text x="0" y="44" class="font-mono hm-subhead">JAN 03, 2026 -&gt; NOV 17, 2026 <tspan fill="#ff007f">//</tspan> PRO DEVELOPER DOSSIER</text>
    </g>

    <!-- Month & Day Labels -->
    {''.join(month_svg_elements)}
    {''.join(day_svg_elements)}

    <!-- Contribution Cells Matrix -->
    {''.join(svg_cells)}

    <!-- Footer Stats & Legend -->
    <g transform="translate({left_padding}, {height - 20})">
      <path d="M 0 -11 L 3 -11 L 3 3 L 0 3 Z" fill="#ff007f" />
      <text x="12" y="0" class="footer-stat">
        STREAK: <tspan fill="#ff007f" font-weight="900">{current_streak} DAYS ACTIVE</tspan>
        <tspan fill="#475569">   |   </tspan>
        BEST DAY: <tspan fill="#ff007f" font-weight="900">{best_day.get('count', 41)} COMMITS</tspan>
        <tspan fill="#475569">   |   </tspan>
        COUNTDOWN: <tspan fill="#00f0ff" font-weight="900">DAY 319 / 365</tspan>
      </text>
    </g>

    {legend_svg}
  </g>

  <!-- Outer Card Border -->
  <rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="11" ry="11" fill="none" stroke="url(#heatmap-card-border)" stroke-width="1.8" />
</svg>
"""

    out_file = Path("gta6-heatmap.svg")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(svg_content)

    with open(Path("contrib-heatmap.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)

    ET.fromstring(svg_content)
    print(f"Generated pixel-perfect gta6-heatmap.svg and contrib-heatmap.svg ({width}x{height})")


# ==============================================================================
# 4. DEVELOPER DOSSIER // 3-BATCH INTELLIGENCE REPORT SVG (With Vector Icons)
# ==============================================================================
def render_batches_svg():
    width = 960
    height = 425

    batches = [
        {
            "id": "BATCH_01",
            "codename": "SYNDICATE CORE // VELOCITY",
            "category": "Pro Developer, High Commits // Streaks",
            "border_color": "#ff007f",
            "tag_color": "#ff007f",
            "items": [
                {
                    "icon": "shield-star",
                    "metric": "PRO DEVELOPER CLASSIFICATION",
                    "value": "TIER-S ARCHITECT",
                    "subtext": "Wanted: 5-Star Velocity // 99.98% System Uptime"
                },
                {
                    "icon": "layers",
                    "metric": "HIGH COMMITS TOTAL",
                    "value": "4,689 COMMITS",
                    "subtext": "Peak: 41 Commits/Day // 22.4 Commits/Active Day"
                },
                {
                    "icon": "lightning",
                    "metric": "COMMIT STREAKS",
                    "value": "78 DAYS ACTIVE",
                    "subtext": "78-Day Marathon Record // 0 Breaking Changes"
                }
            ]
        },
        {
            "id": "BATCH_02",
            "codename": "HEIST OPS // CODE DISCIPLINE",
            "category": "Daily Contributions, PRs // Issues",
            "border_color": "#ff6600",
            "tag_color": "#ffaa00",
            "items": [
                {
                    "icon": "calendar",
                    "metric": "DAILY CONTRIBUTIONS DENSITY",
                    "value": "281 / 319 DAYS",
                    "subtext": "281 Active Days // 38 Strategic Rest Days"
                },
                {
                    "icon": "git-pr",
                    "metric": "PULL REQUESTS AND MERGES",
                    "value": "342 PRODUCTION PRS",
                    "subtext": "99.4% Clean Merge Rate // Sub-4hr Review Time"
                },
                {
                    "icon": "check-circle",
                    "metric": "ISSUES RESOLVED",
                    "value": "489 TICKETS SQUASHED",
                    "subtext": "100% P0/P1 SLA Met // 84 Architecture Refactors"
                }
            ]
        },
        {
            "id": "BATCH_03",
            "codename": "THE EMPIRE // FIELD IMPACT",
            "category": "Projects, Stack // Milestones",
            "border_color": "#00e5ff",
            "tag_color": "#00f0ff",
            "items": [
                {
                    "icon": "monitor",
                    "metric": "PROJECTS & ACTIVE REPOSITORIES",
                    "value": "18 REPOSITORIES",
                    "subtext": "18 Repos // SaaS, AI Agents, Microservices"
                },
                {
                    "icon": "code",
                    "metric": "DEVELOPMENT ACTIVITY PROFILE",
                    "value": "POLYGLOT ARCHITECT",
                    "subtext": "Next.js, TypeScript, Python, PostgreSQL"
                },
                {
                    "icon": "trophy",
                    "metric": "OVERALL CONTRIBUTION HIGHLIGHTS",
                    "value": "4,689 MILESTONES SHIPPED",
                    "subtext": "Full 2026 Roadmap Executed // Production Ready"
                }
            ]
        }
    ]

    def get_icon_svg(icon_name, cx, cy, color):
        if icon_name == "shield-star":
            return f"""
            <g transform="translate({cx-14}, {cy-14})">
              <path d="M 14 3 L 24 7 L 24 16 C 24 22 14 26 14 26 C 14 26 4 22 4 16 L 4 7 Z" fill="none" stroke="{color}" stroke-width="1.8" />
              <polygon points="14,9 15.5,13 20,13.5 16.5,16.5 17.5,21 14,18.5 10.5,21 11.5,16.5 8,13.5 12.5,13" fill="{color}" />
            </g>
            """
        elif icon_name == "layers":
            return f"""
            <g transform="translate({cx-14}, {cy-14})">
              <polygon points="14,4 25,10 14,16 3,10" fill="none" stroke="{color}" stroke-width="1.8" stroke-linejoin="round" />
              <path d="M 3 14 L 14 20 L 25 14" fill="none" stroke="{color}" stroke-width="1.8" stroke-linejoin="round" />
              <path d="M 3 18 L 14 24 L 25 18" fill="none" stroke="{color}" stroke-width="1.8" stroke-linejoin="round" />
            </g>
            """
        elif icon_name == "lightning":
            return f"""
            <g transform="translate({cx-14}, {cy-14})">
              <polygon points="15,3 6,15 13,15 11,26 21,13 14,13" fill="none" stroke="{color}" stroke-width="2" stroke-linejoin="round" />
            </g>
            """
        elif icon_name == "calendar":
            return f"""
            <g transform="translate({cx-14}, {cy-14})">
              <rect x="4" y="6" width="20" height="19" rx="3" fill="none" stroke="{color}" stroke-width="1.8" />
              <line x1="4" y1="12" x2="24" y2="12" stroke="{color}" stroke-width="1.8" />
              <line x1="9" y1="3" x2="9" y2="7" stroke="{color}" stroke-width="2" stroke-linecap="round" />
              <line x1="19" y1="3" x2="19" y2="7" stroke="{color}" stroke-width="2" stroke-linecap="round" />
              <circle cx="9" cy="17" r="1.5" fill="{color}" />
              <circle cx="14" cy="17" r="1.5" fill="{color}" />
              <circle cx="19" cy="17" r="1.5" fill="{color}" />
            </g>
            """
        elif icon_name == "git-pr":
            return f"""
            <g transform="translate({cx-14}, {cy-14})">
              <circle cx="8" cy="7" r="3" fill="none" stroke="{color}" stroke-width="1.8" />
              <circle cx="8" cy="21" r="3" fill="none" stroke="{color}" stroke-width="1.8" />
              <circle cx="20" cy="14" r="3" fill="none" stroke="{color}" stroke-width="1.8" />
              <line x1="8" y1="10" x2="8" y2="18" stroke="{color}" stroke-width="1.8" />
              <path d="M 8 13 C 12 13 14 14 17 14" fill="none" stroke="{color}" stroke-width="1.8" />
            </g>
            """
        elif icon_name == "check-circle":
            return f"""
            <g transform="translate({cx-14}, {cy-14})">
              <circle cx="14" cy="14" r="11" fill="none" stroke="{color}" stroke-width="1.8" />
              <polyline points="9,14 13,18 20,10" fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" />
            </g>
            """
        elif icon_name == "monitor":
            return f"""
            <g transform="translate({cx-14}, {cy-14})">
              <rect x="3" y="5" width="22" height="15" rx="2" fill="none" stroke="{color}" stroke-width="1.8" />
              <line x1="14" y1="20" x2="14" y2="24" stroke="{color}" stroke-width="2" />
              <line x1="8" y1="24" x2="20" y2="24" stroke="{color}" stroke-width="2" stroke-linecap="round" />
            </g>
            """
        elif icon_name == "code":
            return f"""
            <g transform="translate({cx-14}, {cy-14})">
              <polyline points="9,8 3,14 9,20" fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" />
              <polyline points="19,8 25,14 19,20" fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" />
              <line x1="16" y1="6" x2="12" y2="22" stroke="{color}" stroke-width="1.8" stroke-linecap="round" />
            </g>
            """
        else: # trophy
            return f"""
            <g transform="translate({cx-14}, {cy-14})">
              <path d="M 6 6 L 22 6 L 22 13 C 22 17.5 18.5 21 14 21 C 9.5 21 6 17.5 6 13 Z" fill="none" stroke="{color}" stroke-width="1.8" />
              <path d="M 6 9 L 3 9 C 3 13 5 15 7 15" fill="none" stroke="{color}" stroke-width="1.6" />
              <path d="M 22 9 L 25 9 C 25 13 23 15 21 15" fill="none" stroke="{color}" stroke-width="1.6" />
              <line x1="14" y1="21" x2="14" y2="24" stroke="{color}" stroke-width="2" />
              <line x1="9" y1="24" x2="19" y2="24" stroke="{color}" stroke-width="2" stroke-linecap="round" />
            </g>
            """

    col_width = 286
    col_gap = 17
    col_x_starts = [35, 35 + col_width + col_gap, 35 + (col_width + col_gap) * 2]

    col_elements = []
    for col_idx, b in enumerate(batches):
        x = col_x_starts[col_idx]
        b_id = escape_xml(b["id"])
        codename = escape_xml(b["codename"])
        category = escape_xml(b["category"])
        border_color = b["border_color"]
        tag_color = b["tag_color"]

        items_svg = []
        for i_idx, item in enumerate(b["items"]):
            iy = 138 + (i_idx * 78)
            metric_str = escape_xml(item['metric'])
            val_str = escape_xml(item['value'])
            sub_str = escape_xml(item['subtext'])
            icon_markup = get_icon_svg(item['icon'], x + 32, iy + 34, border_color)

            items_svg.append(f"""
            <!-- Item {i_idx + 1} -->
            <rect x="{x + 10}" y="{iy}" width="{col_width - 20}" height="68" rx="5" fill="#130726" stroke="#250d44" stroke-width="1" />
            
            <!-- Left Vector Icon Container -->
            <rect x="{x + 18}" y="{iy + 15}" width="{38}" height="{38}" rx="6" fill="#1a0933" stroke="{border_color}" stroke-width="0.8" opacity="0.9" />
            {icon_markup}

            <!-- Text Fields -->
            <text x="{x + 66}" y="{iy + 21}" class="item-metric" fill="{tag_color}">[{metric_str}]</text>
            <text x="{x + 66}" y="{iy + 41}" class="item-value">{val_str}</text>
            <text x="{x + 66}" y="{iy + 56}" class="item-subtext">{sub_str}</text>
            """)

        col_elements.append(f"""
        <!-- Column {col_idx + 1}: {b_id} -->
        <g>
          <!-- Main Card Box -->
          <rect x="{x}" y="65" width="{col_width}" height="320" rx="8" fill="#0d031c" stroke="{border_color}" stroke-width="1.6" />
          
          <!-- Column Header Pill Box -->
          <rect x="{x + 10}" y="76" width="{col_width - 20}" height="48" rx="5" fill="#170530" stroke="#360c63" stroke-width="1" />
          <text x="{x + 18}" y="95" class="col-id" fill="#ffffff">{b_id} // {codename}</text>
          <text x="{x + 18}" y="112" class="col-category">{category}</text>
          
          {''.join(items_svg)}
        </g>
        """)

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <linearGradient id="dossier-card-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff007f" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#ff5e00" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#00f0ff" stop-opacity="0.8" />
    </linearGradient>

    <style>
      .font-display {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; }}
      .font-mono {{ font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, Menlo, monospace; }}
      
      .dossier-title {{
        font-size: 17.5px;
        font-weight: 900;
        font-style: italic;
        fill: #ffffff;
        letter-spacing: 0.8px;
      }}
      .dossier-subhead {{
        font-size: 11px;
        font-weight: 700;
        fill: #94a3b8;
        letter-spacing: 1.2px;
      }}
      .col-id {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-size: 11px;
        font-weight: 900;
        letter-spacing: 0.8px;
      }}
      .col-category {{
        font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, Menlo, monospace;
        font-size: 9.5px;
        font-weight: 600;
        fill: #94a3b8;
      }}
      .item-metric {{
        font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, Menlo, monospace;
        font-size: 8.5px;
        font-weight: 800;
        letter-spacing: 0.8px;
      }}
      .item-value {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-size: 14px;
        font-weight: 900;
        fill: #ffffff;
        letter-spacing: 0.6px;
      }}
      .item-subtext {{
        font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, Menlo, monospace;
        font-size: 8.5px;
        font-weight: 500;
        fill: #94a3b8;
      }}
      .footer-hud {{
        font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, Menlo, monospace;
        font-size: 10.5px;
        font-weight: 700;
        fill: #94a3b8;
        letter-spacing: 0.8px;
      }}
    </style>
  </defs>

  <!-- Container Base -->
  <rect width="{width}" height="{height}" rx="12" ry="12" fill="#0b0317" stroke="url(#dossier-card-border)" stroke-width="1.8" />

  <!-- Top Header with Generous Spacing -->
  <g transform="translate(35, 20)">
    <text x="0" y="20" class="font-display dossier-title">DEVELOPER DOSSIER <tspan fill="#ff007f">//</tspan> 3-BATCH INTELLIGENCE REPORT</text>
    <text x="0" y="38" class="font-mono dossier-subhead">4,689 CONTRIBUTIONS <tspan fill="#ff007f">//</tspan> ZERO-DEFECT PRODUCTION OPS</text>
    
    <!-- Top Right Status -->
    <text x="{width - 70}" y="20" text-anchor="end" class="font-mono footer-hud">
      COUNTDOWN: <tspan fill="#ffd700" font-weight="900">DAY 319 / 365</tspan>
      <tspan fill="#475569">   |   </tspan>
      STATUS: <tspan fill="#00ff88" font-weight="900">ACTIVE</tspan>
    </text>
  </g>

  <!-- 3 Batches Columns -->
  {''.join(col_elements)}

  <!-- Bottom Footer Status Bar -->
  <g transform="translate(35, {height - 22})">
    <path d="M 0 -10 L 3.5 -10 L 3.5 4 L 0 4 Z" fill="#ff007f" />
    <text x="12" y="0" class="footer-hud">[MISSION DISPATCH] DAILY COUNTDOWN ACTIVE // UPDATED DAILY VIA GITHUB ACTIONS</text>
    <text x="{width - 70}" y="0" text-anchor="end" class="footer-hud">CLASSIFICATION: <tspan fill="#ffd700" font-weight="900">TIER-S PRO DEVELOPER</tspan></text>
  </g>
</svg>
"""

    out_file = Path("gta6-batches-showcase.svg")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(svg_content)

    ET.fromstring(svg_content)
    print(f"Generated pixel-perfect gta6-batches-showcase.svg ({width}x{height})")


if __name__ == "__main__":
    render_hero_banner()
    render_action_buttons()
    render_heatmap_svg()
    render_batches_svg()
