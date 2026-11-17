"""
GTA VI SVG Renderer
Renders high-definition, vectorized, responsive SVG cards:
1. gta6-heatmap.svg & contrib-heatmap.svg (Full year Jan 3 - Nov 17, 2026, 4,689 contributions, 0 emojis)
2. gta6-batches-showcase.svg (3-batch developer stats card, 0 emojis)
"""

import json
import datetime
from pathlib import Path

# GTA VI Vice City Neon Palette
PALETTE = [
    "#150a24",  # Level 0 - Midnight void
    "#3d115e",  # Level 1 - Dusk purple
    "#7e177b",  # Level 2 - Electric magenta
    "#d8137f",  # Level 3 - Vice hot pink
    "#ff5e00",  # Level 4 - Sunset orange
    "#00f0ff"   # Level 5 - Overdrive cyan
]

MONTH_NAMES = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

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
    longest_streak = data.get("longest_streak", 78)
    best_day = data.get("best_day", {})

    width = 920
    height = 230
    cell_size = 12
    cell_gap = 4
    left_padding = 45
    top_padding = 52

    # Parse days
    svg_cells = []
    month_labels = []
    last_month = -1

    # Date to col/row mapping based on 2026-01-03
    # Jan 3, 2026 was Saturday (weekday = 5 in Python: Mon=0..Sun=6; GitHub calendar row: Sun=0..Sat=6, so Sat=6)
    # Let's align by standard calendar week columns
    
    # Anchor date: start_date is Jan 3, 2026 (Saturday)
    # Pre-pad cells in week 0 from Sunday (Dec 28, 2025) to Friday (Jan 2, 2026) with level 0 inactive
    first_date_str = days[0]["date"] if days else "2026-01-03"
    first_dt = datetime.datetime.strptime(first_date_str, "%Y-%m-%d").date()
    # In standard Sunday-first calendar: Sunday=0, Monday=1, ..., Saturday=6
    first_day_col_row = (first_dt.weekday() + 1) % 7 # Sunday=0, Sat=6

    # Build calendar matrix
    cur_col = 0
    cur_row = first_day_col_row

    for idx, day in enumerate(days):
        x = left_padding + cur_col * (cell_size + cell_gap)
        y = top_padding + cur_row * (cell_size + cell_gap)

        level = min(day.get("level", 0), len(PALETTE) - 1)
        color = PALETTE[level]
        date_str = day.get("date", "")
        count = day.get("count", 0)

        # Track month label at row 0 or first encounter
        if date_str:
            month_idx = int(date_str.split("-")[1]) - 1
            if month_idx != last_month and cur_row in (0, 1):
                month_labels.append((x, MONTH_NAMES[month_idx]))
                last_month = month_idx

        tooltip_text = f"{count} contributions on {date_str}" if count > 0 else f"Strategic pause on {date_str}"
        glow_attr = 'filter="url(#neon-glow)"' if level >= 4 else ''

        cell_svg = (
            f'<rect class="cell" x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" rx="2" ry="2" '
            f'fill="{color}" {glow_attr}><title>{tooltip_text}</title></rect>'
        )
        svg_cells.append(cell_svg)

        # Move to next day
        cur_row += 1
        if cur_row > 6:
            cur_row = 0
            cur_col += 1

    # Month SVG text
    month_svg_elements = []
    for mx, mname in month_labels:
        month_svg_elements.append(f'<text x="{mx}" y="{top_padding - 14}" class="hud-label">{mname}</text>')

    # Day SVG text (Mon, Wed, Fri)
    day_svg_elements = [
        f'<text x="{left_padding - 12}" y="{top_padding + 1 * (cell_size + cell_gap) + 9}" class="hud-label" text-anchor="end">MON</text>',
        f'<text x="{left_padding - 12}" y="{top_padding + 3 * (cell_size + cell_gap) + 9}" class="hud-label" text-anchor="end">WED</text>',
        f'<text x="{left_padding - 12}" y="{top_padding + 5 * (cell_size + cell_gap) + 9}" class="hud-label" text-anchor="end">FRI</text>',
    ]

    # Legend
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

    # 5 Vector Stars for Wanted Level (NO EMOJIS)
    star_svg = []
    star_start_x = width - 150
    for s_idx in range(5):
        sx = star_start_x + (s_idx * 22)
        sy = 19
        star_svg.append(f'''
        <polygon points="{sx+8},{sy} {sx+10.5},{sy+5.5} {sx+16},{sy+6.2} {sx+12},{sy+10.2} {sx+13},{sy+16} {sx+8},{sy+13} {sx+3},{sy+16} {sx+4},{sy+10.2} {sx},{sy+6.2} {sx+5.5},{sy+5.5}" fill="#ffd700" filter="url(#gold-glow)"/>
        ''')

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <!-- Vice City Gradients -->
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

    <!-- Neon Glow Filter -->
    <filter id="neon-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="gold-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="1.5" result="blur" />
      <feColorMatrix type="matrix" values="1 0 0 0 1   0 0.8 0 0 0.8   0 0 0 0 0  0 0 0 1 0" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <style>
      .hud-bg {{
        fill: #0a0514;
        stroke: url(#gta-border);
        stroke-width: 1.6;
        rx: 10px;
        ry: 10px;
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
      .cell {{
        shape-rendering: geometricPrecision;
      }}
    </style>
  </defs>

  <!-- Container Base -->
  <rect class="hud-bg" width="{width}" height="{height}" />

  <!-- Tactical Corner Crosshairs (GTA HUD Aesthetic) -->
  <path d="M 12 20 L 12 12 L 20 12" class="corner-accent" />
  <path d="M {width - 12} 20 L {width - 12} 12 L {width - 20} 12" class="corner-accent" />
  <path d="M 12 {height - 20} L 12 {height - 12} L 20 {height - 12} class="corner-accent" />
  <path d="M {width - 12} {height - 20} L {width - 12} {height - 12} L {width - 20} {height - 12}" class="corner-accent" />

  <!-- Top Header -->
  <text x="{left_padding}" y="28" class="hud-title">[VICE CITY // LEONIDA STATE] 4,689 CONTRIBUTIONS IN THE LAST YEAR</text>
  <text x="{left_padding}" y="42" class="hud-badge">JAN 03, 2026 - NOV 17, 2026 // PRO DEVELOPER DOSSIER</text>

  <!-- Wanted Level 5-Stars (NO EMOJIS) -->
  <g>
    <text x="{star_start_x - 70}" y="31" class="hud-badge">WANTED:</text>
    {''.join(star_svg)}
  </g>

  <!-- Month & Day Labels -->
  {''.join(month_svg_elements)}
  {''.join(day_svg_elements)}

  <!-- Contribution Cells -->
  {''.join(svg_cells)}

  <!-- Footer Stats & Countdown -->
  <text x="{left_padding}" y="{height - 20}" class="hud-stats">
    STREAK: <tspan class="stat-highlight">{current_streak} DAYS ACTIVE</tspan> | 
    BEST DAY: <tspan class="stat-cyan">{best_day.get('count', 41)} COMMITS</tspan> | 
    DAILY COUNTDOWN: <tspan class="stat-cyan">DAY 319 / 365</tspan>
  </text>
  {legend_svg}
</svg>
"""

    out_file = Path("gta6-heatmap.svg")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(svg_content)

    # Also update contrib-heatmap.svg so existing README references point to new layout
    with open(Path("contrib-heatmap.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"Generated gta6-heatmap.svg and updated contrib-heatmap.svg ({width}x{height})")


def render_batches_svg():
    stats_file = Path("data/gta6_stats.json")
    if not stats_file.exists():
        print("data/gta6_stats.json not found.")
        return

    with open(stats_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    batches = data.get("batches", {})
    b1 = batches.get("batch_1", {})
    b2 = batches.get("batch_2", {})
    b3 = batches.get("batch_3", {})

    width = 920
    height = 360
    col_width = 275
    col_gap = 20
    col_x_starts = [35, 35 + col_width + col_gap, 35 + (col_width + col_gap) * 2]

    def render_col(col_idx, batch_obj, border_color):
        x = col_x_starts[col_idx]
        b_id = batch_obj.get("id", f"BATCH_0{col_idx+1}")
        codename = batch_obj.get("codename", "")
        category = batch_obj.get("category", "")
        items = batch_obj.get("items", [])

        items_svg = []
        for i_idx, item in enumerate(items):
            iy = 125 + (i_idx * 70)
            items_svg.append(f"""
            <!-- Item {i_idx + 1} -->
            <rect x="{x + 12}" y="{iy}" width="{col_width - 24}" height="60" rx="4" fill="#130826" stroke="#2a124a" stroke-width="1" />
            <text x="{x + 22}" y="{iy + 18}" class="item-metric">{item.get('metric', '')}</text>
            <text x="{x + 22}" y="{iy + 36}" class="item-value">{item.get('value', '')}</text>
            <text x="{x + 22}" y="{iy + 50}" class="item-subtext">{item.get('subtext', '')[:44]}</text>
            """)

        return f"""
        <!-- Column {col_idx + 1}: {b_id} -->
        <g>
          <rect x="{x}" y="55" width="{col_width}" height="280" rx="6" fill="#0d041a" stroke="{border_color}" stroke-width="1.4" />
          <path d="M {x} 55 L {x + 15} 55 L {x} 70 Z" fill="{border_color}" />
          <path d="M {x + col_width} 55 L {x + col_width - 15} 55 L {x + col_width} 70 Z" fill="{border_color}" />
          
          <!-- Column Header -->
          <rect x="{x + 12}" y="67" width="{col_width - 24}" height="44" rx="4" fill="#170630" stroke="#37105e" stroke-width="1" />
          <text x="{x + 22}" y="83" class="col-id">{b_id} // {codename}</text>
          <text x="{x + 22}" y="99" class="col-category">{category}</text>
          
          {''.join(items_svg)}
        </g>
        """

    col1_svg = render_col(0, b1, "#ff007f")
    col2_svg = render_col(1, b2, "#ff5e00")
    col3_svg = render_col(2, b3, "#00f0ff")

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <linearGradient id="card-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff007f" />
      <stop offset="50%" stop-color="#ff5e00" />
      <stop offset="100%" stop-color="#00f0ff" />
    </linearGradient>

    <linearGradient id="title-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff007f" />
      <stop offset="50%" stop-color="#ff5e00" />
      <stop offset="100%" stop-color="#ffd700" />
    </linearGradient>

    <style>
      .bg {{
        fill: #080310;
        stroke: url(#card-border);
        stroke-width: 1.6;
        rx: 10px;
        ry: 10px;
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
        fill: url(#title-grad);
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
        fill: #a855f7;
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
        font-size: 8.5px;
        font-weight: 500;
        fill: #94a3b8;
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
  {col1_svg}
  {col2_svg}
  {col3_svg}

  <!-- Bottom HUD Status -->
  <text x="35" y="{height - 12}" class="footer-hud">[MISSION DISPATCH] DAILY COUNTDOWN ACTIVE // UPDATED DAILY VIA GITHUB ACTIONS</text>
  <text x="{width - 35}" y="{height - 12}" text-anchor="end" class="footer-hud">CLASSIFICATION: <tspan class="footer-highlight">TIER-S PRO DEVELOPER</tspan></text>
</svg>
"""

    out_file = Path("gta6-batches-showcase.svg")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"Generated gta6-batches-showcase.svg ({width}x{height})")


if __name__ == "__main__":
    render_heatmap_svg()
    render_batches_svg()
