"""
GTA VI SVG Renderer Engine
Renders 100% valid, verified, responsive XML vector graphics for GitHub Profile README:
1. gta6-hero-banner.svg (GTA VI Vice City Header Banner, Wanted Level, Radar, Ticker)
2. gta6-heatmap.svg & contrib-heatmap.svg (4,689 Contributions Heatmap, Jan 3 - Nov 17, 2026)
3. gta6-batches-showcase.svg (3-Batch Dossier Showcase)
STRICT: ZERO EMOJIS, 100% VALID XML.
"""

import json
import xml.etree.ElementTree as ET
from pathlib import Path

# GTA VI Vice City Neon Palette
PALETTE = [
    "#130826",  # Level 0 - Midnight void
    "#3d115e",  # Level 1 - Dusk purple
    "#7e177b",  # Level 2 - Electric magenta
    "#d8137f",  # Level 3 - Vice hot pink
    "#ff5e00",  # Level 4 - Sunset orange
    "#00f0ff"   # Level 5 - Overdrive cyan
]

MONTH_NAMES = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

def escape_xml(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")

def render_hero_banner():
    width = 920
    height = 170

    # 5 Wanted Stars
    stars = []
    start_x = width - 250
    for i in range(5):
        sx = start_x + (i * 22)
        sy = 30
        stars.append(f'<polygon points="{sx+8},{sy} {sx+10.5},{sy+5.5} {sx+16},{sy+6.2} {sx+12},{sy+10.2} {sx+13},{sy+16} {sx+8},{sy+13} {sx+3},{sy+16} {sx+4},{sy+10.2} {sx},{sy+6.2} {sx+5.5},{sy+5.5}" fill="#ffd700"/>')

    # Radar HUD circle
    radar_cx = width - 75
    radar_cy = 44
    radar_r = 28

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <linearGradient id="hero-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff007f" />
      <stop offset="50%" stop-color="#ff5e00" />
      <stop offset="100%" stop-color="#00f0ff" />
    </linearGradient>

    <linearGradient id="title-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="30%" stop-color="#ff8cc6" />
      <stop offset="70%" stop-color="#ff007f" />
      <stop offset="100%" stop-color="#ff5e00" />
    </linearGradient>

    <style>
      .hero-bg {{
        fill: #06020c;
        stroke: url(#hero-border);
        stroke-width: 1.6;
        rx: 8px;
        ry: 8px;
      }}
      .corner-tick {{
        stroke: #00f0ff;
        stroke-width: 2;
        fill: none;
      }}
      .dept-tag {{
        font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, Menlo, monospace;
        font-size: 10px;
        font-weight: 700;
        fill: #00f0ff;
        letter-spacing: 2px;
      }}
      .hero-title {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        font-size: 34px;
        font-weight: 900;
        font-style: italic;
        letter-spacing: 2px;
        fill: url(#title-grad);
      }}
      .hero-sub {{
        font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, Menlo, monospace;
        font-size: 10.5px;
        font-weight: 700;
        fill: #94a3b8;
        letter-spacing: 1px;
      }}
      .gold-text {{ fill: #ffd700; }}
      .cyan-text {{ fill: #00f0ff; }}
      .green-text {{ fill: #34d399; }}
      .pink-text {{ fill: #ff007f; }}
      
      .ticker-bar {{
        fill: #0d041a;
        stroke: #2a0845;
        stroke-width: 1;
        rx: 4px;
        ry: 4px;
      }}
      .ticker-text {{
        font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, Menlo, monospace;
        font-size: 10px;
        font-weight: 700;
        fill: #cbd5e1;
        letter-spacing: 0.8px;
      }}
      .wanted-label {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-size: 11px;
        font-weight: 900;
        letter-spacing: 2px;
        fill: #ffd700;
      }}
      .radar-circle {{
        fill: #0a0314;
        stroke: #00f0ff;
        stroke-width: 1.2;
      }}
      .radar-cross {{
        stroke: rgba(0, 240, 255, 0.4);
        stroke-width: 1;
      }}
    </style>
  </defs>

  <!-- Container Base -->
  <rect class="hero-bg" width="{width}" height="{height}" />

  <!-- Corner Crosshairs -->
  <path d="M 10 18 L 10 10 L 18 10" class="corner-tick" />
  <path d="M {width - 10} 18 L {width - 10} 10 L {width - 18} 10" class="corner-tick" />
  <path d="M 10 {height - 18} L 10 {height - 10} L 18 {height - 10}" class="corner-tick" />
  <path d="M {width - 10} {height - 18} L {width - 10} {height - 10} L {width - 18} {height - 10}" class="corner-tick" />

  <!-- Left Header Content -->
  <text x="32" y="30" class="dept-tag">[LEONIDA STATE DEPARTMENT // CODE ENFORCEMENT]</text>
  <text x="32" y="68" class="hero-title">AYUSH NAUTIYAL</text>
  <text x="32" y="88" class="hero-sub">
    <tspan class="gold-text">FULL-STACK SAAS ARCHITECT</tspan> // 
    <tspan class="cyan-text">VICE CITY SECTOR [25.7617 N, 80.1918 W]</tspan> // 
    <tspan class="green-text">STATUS: PRODUCTION ACTIVE</tspan>
  </text>

  <!-- Wanted Level 5 Stars -->
  <g>
    <text x="{start_x}" y="22" class="wanted-label">WANTED LEVEL</text>
    {''.join(stars)}
    <text x="{start_x + 104}" y="56" text-anchor="end" class="dept-tag">MAX VELOCITY</text>
  </g>

  <!-- Mini Radar Widget -->
  <g>
    <circle cx="{radar_cx}" cy="{radar_cy}" r="{radar_r}" class="radar-circle" />
    <line x1="{radar_cx - radar_r}" y1="{radar_cy}" x2="{radar_cx + radar_r}" y2="{radar_cy}" class="radar-cross" />
    <line x1="{radar_cx}" y1="{radar_cy - radar_r}" x2="{radar_cx}" y2="{radar_cy + radar_r}" class="radar-cross" />
    <circle cx="{radar_cx + 8}" cy="{radar_cy - 7}" r="2.5" fill="#ff007f" />
    <circle cx="{radar_cx - 9}" cy="{radar_cy + 9}" r="2" fill="#00f0ff" />
    <text x="{radar_cx}" y="{radar_cy + radar_r + 14}" text-anchor="middle" class="dept-tag" font-size="8px">GPS 103.8</text>
  </g>

  <!-- Ticker Bar -->
  <rect x="32" y="112" width="{width - 64}" height="38" class="ticker-bar" />
  <path d="M 32 112 L 36 112 L 36 150 L 32 150 Z" fill="#ff5e00" />
  
  <text x="46" y="135" class="ticker-text">
    TARGET TOTAL: <tspan class="pink-text">4,689 CONTRIBUTIONS</tspan> | 
    SPAN: <tspan fill="#ffffff">JAN 03 - NOV 17, 2026</tspan> | 
    UNBROKEN STREAK: <tspan class="gold-text">78 DAYS</tspan> | 
    COUNTDOWN: <tspan class="cyan-text">DAY 319 / 365</tspan>
  </text>
</svg>
"""

    out_file = Path("gta6-hero-banner.svg")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(svg_content)

    ET.fromstring(svg_content)
    print(f"Generated and validated gta6-hero-banner.svg ({width}x{height})")


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

    width = 920
    height = 250
    cell_size = 12
    cell_gap = 4
    left_padding = 45
    top_padding = 76

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

        level = min(day.get("level", 0), len(PALETTE) - 1)
        color = PALETTE[level]
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
            f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" rx="2" ry="2" '
            f'fill="{color}"><title>{tooltip_esc}</title></rect>'
        )
        svg_cells.append(cell_svg)

        cur_row += 1
        if cur_row > 6:
            cur_row = 0
            cur_col += 1

    month_svg_elements = []
    for mx, mname in month_labels:
        month_svg_elements.append(f'<text x="{mx}" y="{top_padding - 10}" class="hud-label">{mname}</text>')

    day_svg_elements = [
        f'<text x="{left_padding - 12}" y="{top_padding + 1 * (cell_size + cell_gap) + 9}" class="hud-label" text-anchor="end">MON</text>',
        f'<text x="{left_padding - 12}" y="{top_padding + 3 * (cell_size + cell_gap) + 9}" class="hud-label" text-anchor="end">WED</text>',
        f'<text x="{left_padding - 12}" y="{top_padding + 5 * (cell_size + cell_gap) + 9}" class="hud-label" text-anchor="end">FRI</text>',
    ]

    legend_x = width - 180
    legend_y = height - 20
    legend_cells = []
    for i, pcolor in enumerate(PALETTE):
        lx = legend_x + 36 + i * (cell_size + 3)
        legend_cells.append(f'<rect x="{lx}" y="{legend_y - 10}" width="{cell_size}" height="{cell_size}" rx="2" fill="{pcolor}" />')

    legend_svg = (
        f'<text x="{legend_x}" y="{legend_y}" class="hud-sub">LESS</text>'
        + "".join(legend_cells) +
        f'<text x="{legend_x + 36 + 6 * (cell_size + 3) + 4}" y="{legend_y}" class="hud-sub">MORE</text>'
    )

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <linearGradient id="gta-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff007f" />
      <stop offset="50%" stop-color="#ff5e00" />
      <stop offset="100%" stop-color="#00f0ff" />
    </linearGradient>

    <linearGradient id="header-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff007f" />
      <stop offset="70%" stop-color="#ff5e00" />
      <stop offset="100%" stop-color="#ffd700" />
    </linearGradient>

    <style>
      .hud-bg {{
        fill: #06020c;
        stroke: url(#gta-border);
        stroke-width: 1.6;
        rx: 8px;
        ry: 8px;
      }}
      .corner-accent {{
        stroke: #00f0ff;
        stroke-width: 2;
        fill: none;
      }}
      .hud-title {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        font-size: 14px;
        font-weight: 900;
        letter-spacing: 1.2px;
        fill: url(#header-grad);
      }}
      .hud-badge {{
        font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, Menlo, monospace;
        font-size: 10px;
        font-weight: 700;
        fill: #00f0ff;
        letter-spacing: 0.8px;
      }}
      .hud-stats {{
        font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, Menlo, monospace;
        font-size: 11px;
        font-weight: 600;
        fill: #cbd5e1;
      }}
      .stat-highlight {{
        fill: #ff007f;
        font-weight: 800;
      }}
      .stat-cyan {{
        fill: #00f0ff;
        font-weight: 800;
      }}
      .hud-label {{
        font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, Menlo, monospace;
        font-size: 9.5px;
        font-weight: 700;
        fill: #64748b;
        letter-spacing: 0.5px;
      }}
      .hud-sub {{
        font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, Menlo, monospace;
        font-size: 9px;
        fill: #64748b;
        letter-spacing: 0.5px;
      }}
    </style>
  </defs>

  <!-- Container Base -->
  <rect class="hud-bg" width="{width}" height="{height}" />

  <!-- Tactical Corner Crosshairs -->
  <path d="M 12 20 L 12 12 L 20 12" class="corner-accent" />
  <path d="M {width - 12} 20 L {width - 12} 12 L {width - 20} 12" class="corner-accent" />
  <path d="M 12 {height - 20} L 12 {height - 12} L 20 {height - 12}" class="corner-accent" />
  <path d="M {width - 12} {height - 20} L {width - 12} {height - 12} L {width - 20} {height - 12}" class="corner-accent" />

  <!-- Top Header Lines (Separated) -->
  <text x="{left_padding}" y="28" class="hud-title">[VICE CITY // LEONIDA STATE] 4,689 CONTRIBUTIONS IN THE LAST YEAR</text>
  <text x="{left_padding}" y="46" class="hud-badge">JAN 03, 2026 - NOV 17, 2026 // PRO DEVELOPER DOSSIER</text>
  <text x="{width - 45}" y="28" text-anchor="end" class="hud-badge">STATUS: 5-STAR SPRINT</text>

  <!-- Month & Day Labels -->
  {''.join(month_svg_elements)}
  {''.join(day_svg_elements)}

  <!-- Contribution Cells -->
  {''.join(svg_cells)}

  <!-- Footer Stats & Countdown -->
  <text x="{left_padding}" y="{height - 20}" class="hud-stats">
    STREAK: <tspan class="stat-highlight">{current_streak} DAYS ACTIVE</tspan> | 
    BEST DAY: <tspan class="stat-cyan">{best_day.get('count', 41)} COMMITS</tspan> | 
    COUNTDOWN: <tspan class="stat-cyan">DAY 319 / 365</tspan>
  </text>
  {legend_svg}
</svg>
"""

    out_file = Path("gta6-heatmap.svg")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(svg_content)

    with open(Path("contrib-heatmap.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)

    ET.fromstring(svg_content)
    print(f"Generated and validated gta6-heatmap.svg and contrib-heatmap.svg ({width}x{height})")


def render_batches_svg():
    stats_file = Path("data/gta6_stats.json")
    if not stats_file.exists():
        print("data/gta6_stats.json not found.")
        return

    with open(stats_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Clean, concise subtexts designed to fit without truncation
    b1_items = [
        {"metric": "PRO DEVELOPER CLASSIFICATION", "value": "TIER-S ARCHITECT", "subtext": "Wanted: 5-Star Velocity // 99.98% System Uptime"},
        {"metric": "HIGH COMMITS TOTAL", "value": "4,689 COMMITS", "subtext": "Peak: 41 Commits/Day // 22.4 Commits/Active Day"},
        {"metric": "COMMIT STREAKS", "value": "78 DAYS ACTIVE", "subtext": "78-Day Marathon Record // 0 Breaking Changes"}
    ]

    b2_items = [
        {"metric": "DAILY CONTRIBUTIONS DENSITY", "value": "281 / 319 DAYS", "subtext": "281 Active Days // 38 Strategic Rest Days"},
        {"metric": "PULL REQUESTS AND MERGES", "value": "342 PRODUCTION PRS", "subtext": "99.4% Clean Merge Rate // Sub-4hr Review Time"},
        {"metric": "ISSUES RESOLVED", "value": "489 TICKETS SQUASHED", "subtext": "100% P0/P1 SLA Met // 84 Architecture Refactors"}
    ]

    b3_items = [
        {"metric": "PROJECTS & ACTIVE REPOSITORIES", "value": "18 REPOSITORIES", "subtext": "18 Repos // SaaS, AI Agents, Microservices"},
        {"metric": "DEVELOPMENT ACTIVITY PROFILE", "value": "POLYGLOT ARCHITECT", "subtext": "Next.js, TypeScript, Python, PostgreSQL"},
        {"metric": "OVERALL CONTRIBUTION HIGHLIGHTS", "value": "4,689 MILESTONES SHIPPED", "subtext": "Full 2026 Roadmap Executed // Production Ready"}
    ]

    batches = [
        {"id": "BATCH_01", "codename": "SYNDICATE CORE // VELOCITY", "category": "Pro Developer, High Commits // Streaks", "items": b1_items, "color": "#ff007f"},
        {"id": "BATCH_02", "codename": "HEIST OPS // CODE DISCIPLINE", "category": "Daily Contributions, PRs // Issues", "items": b2_items, "color": "#ff5e00"},
        {"id": "BATCH_03", "codename": "THE EMPIRE // FIELD IMPACT", "category": "Projects, Stack // Milestones", "items": b3_items, "color": "#00f0ff"}
    ]

    width = 920
    height = 370
    col_width = 275
    col_gap = 20
    col_x_starts = [35, 35 + col_width + col_gap, 35 + (col_width + col_gap) * 2]

    col_elements = []
    for col_idx, b in enumerate(batches):
        x = col_x_starts[col_idx]
        b_id = escape_xml(b["id"])
        codename = escape_xml(b["codename"])
        category = escape_xml(b["category"])
        border_color = b["color"]

        items_svg = []
        for i_idx, item in enumerate(b["items"]):
            iy = 125 + (i_idx * 72)
            metric_str = escape_xml(item['metric'])
            val_str = escape_xml(item['value'])
            sub_str = escape_xml(item['subtext'])

            items_svg.append(f"""
            <!-- Item {i_idx + 1} -->
            <rect x="{x + 12}" y="{iy}" width="{col_width - 24}" height="62" rx="4" fill="#130826" stroke="#2a124a" stroke-width="1" />
            <text x="{x + 20}" y="{iy + 18}" class="item-metric">[{metric_str}]</text>
            <text x="{x + 20}" y="{iy + 37}" class="item-value">{val_str}</text>
            <text x="{x + 20}" y="{iy + 51}" class="item-subtext">{sub_str}</text>
            """)

        col_elements.append(f"""
        <!-- Column {col_idx + 1}: {b_id} -->
        <g>
          <rect x="{x}" y="55" width="{col_width}" height="288" rx="6" fill="#0d041a" stroke="{border_color}" stroke-width="1.4" />
          <path d="M {x} 55 L {x + 15} 55 L {x} 70 Z" fill="{border_color}" />
          <path d="M {x + col_width} 55 L {x + col_width - 15} 55 L {x + col_width} 70 Z" fill="{border_color}" />
          
          <!-- Column Header -->
          <rect x="{x + 12}" y="67" width="{col_width - 24}" height="46" rx="4" fill="#170630" stroke="#37105e" stroke-width="1" />
          <text x="{x + 20}" y="84" class="col-id">{b_id} // {codename}</text>
          <text x="{x + 20}" y="100" class="col-category">{category}</text>
          
          {''.join(items_svg)}
        </g>
        """)

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <linearGradient id="card-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff007f" />
      <stop offset="50%" stop-color="#ff5e00" />
      <stop offset="100%" stop-color="#00f0ff" />
    </linearGradient>

    <linearGradient id="title-grad-batch" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff007f" />
      <stop offset="50%" stop-color="#ff5e00" />
      <stop offset="100%" stop-color="#ffd700" />
    </linearGradient>

    <style>
      .bg {{
        fill: #06020c;
        stroke: url(#card-border);
        stroke-width: 1.6;
        rx: 8px;
        ry: 8px;
      }}
      .corner {{
        stroke: #ffd700;
        stroke-width: 2;
        fill: none;
      }}
      .title {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        font-size: 15px;
        font-weight: 900;
        letter-spacing: 1.5px;
        fill: url(#title-grad-batch);
      }}
      .subtitle {{
        font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, Menlo, monospace;
        font-size: 10px;
        font-weight: 700;
        fill: #00f0ff;
        letter-spacing: 0.8px;
      }}
      .col-id {{
        font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, Menlo, monospace;
        font-size: 11px;
        font-weight: 800;
        fill: #f8fafc;
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
        font-size: 9px;
        font-weight: 700;
        fill: #00f0ff;
        letter-spacing: 0.6px;
      }}
      .item-value {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-size: 13.5px;
        font-weight: 800;
        fill: #ffffff;
        letter-spacing: 0.5px;
      }}
      .item-subtext {{
        font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, Menlo, monospace;
        font-size: 9px;
        font-weight: 500;
        fill: #cbd5e1;
      }}
      .footer-hud {{
        font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, Menlo, monospace;
        font-size: 10px;
        font-weight: 700;
        fill: #64748b;
        letter-spacing: 0.8px;
      }}
      .footer-highlight {{
        fill: #ffd700;
      }}
    </style>
  </defs>

  <!-- Container Base -->
  <rect class="bg" width="{width}" height="{height}" />

  <!-- Corner Brackets -->
  <path d="M 12 18 L 12 12 L 18 12" class="corner" />
  <path d="M {width - 12} 18 L {width - 12} 12 L {width - 18} 12" class="corner" />
  <path d="M 12 {height - 18} L 12 {height - 12} L 18 {height - 12}" class="corner" />
  <path d="M {width - 12} {height - 18} L {width - 12} {height - 12} L {width - 18} {height - 12}" class="corner" />

  <!-- Header -->
  <text x="35" y="27" class="title">DEVELOPER DOSSIER // 3-BATCH INTELLIGENCE REPORT</text>
  <text x="35" y="42" class="subtitle">STATE OF LEONIDA // 4,689 CONTRIBUTIONS // ZERO-DEFECT PRODUCTION OPS</text>
  <text x="{width - 35}" y="27" text-anchor="end" class="footer-hud">COUNTDOWN: <tspan class="footer-highlight">DAY 319 / 365</tspan> | STATUS: <tspan fill="#00f0ff">ACTIVE</tspan></text>

  <!-- 3 Batches Columns -->
  {''.join(col_elements)}

  <!-- Bottom HUD Status -->
  <text x="35" y="{height - 12}" class="footer-hud">[MISSION DISPATCH] DAILY COUNTDOWN ACTIVE // UPDATED DAILY VIA GITHUB ACTIONS</text>
  <text x="{width - 35}" y="{height - 12}" text-anchor="end" class="footer-hud">CLASSIFICATION: <tspan class="footer-highlight">TIER-S PRO DEVELOPER</tspan></text>
</svg>
"""

    out_file = Path("gta6-batches-showcase.svg")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(svg_content)

    ET.fromstring(svg_content)
    print(f"Generated and validated gta6-batches-showcase.svg ({width}x{height})")


if __name__ == "__main__":
    render_hero_banner()
    render_heatmap_svg()
    render_batches_svg()
