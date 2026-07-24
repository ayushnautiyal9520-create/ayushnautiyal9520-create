import json
from pathlib import Path

PALETTE = [
    "#161b22",  # Level 0 - none
    "#0e4429",  # Level 1 - subtle
    "#006d32",  # Level 2 - medium
    "#26a641",  # Level 3 - bright
    "#39d353",  # Level 4 - neon
    "#69f0a0"   # Level 5 - max
]

MONTH_NAMES = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def render_heatmap():
    data_file = Path("data/contributions.json")
    if not data_file.exists():
        print("data/contributions.json not found. Run fetch_contributions.py first.")
        return

    with open(data_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    days = data.get("days", [])
    total = data.get("total_contributions", 0)
    current_streak = data.get("current_streak", 0)
    longest_streak = data.get("longest_streak", 0)
    username = data.get("username", "ayushnautiyal9520-create")

    # Layout constants
    cell_size = 11
    cell_gap = 4
    left_padding = 40
    top_padding = 45
    width = 860
    height = 210

    # Build 53 columns x 7 rows
    # Compute column positions and month labels
    svg_cells = []
    month_labels = []
    last_month = -1

    for idx, day in enumerate(days):
        col = idx // 7
        row = idx % 7
        x = left_padding + col * (cell_size + cell_gap)
        y = top_padding + row * (cell_size + cell_gap)
        
        level = min(day.get("level", 0), len(PALETTE) - 1)
        color = PALETTE[level]
        date_str = day.get("date", "")
        count = day.get("count", 0)

        # Check month change for labels
        if date_str:
            month_idx = int(date_str.split("-")[1]) - 1
            if month_idx != last_month and row == 0 and col < 52:
                month_labels.append((x, MONTH_NAMES[month_idx]))
                last_month = month_idx

        tooltip_text = f"{count} contributions on {date_str}" if count > 0 else f"No contributions on {date_str}"

        # CSS custom properties for staggered animation
        delay_ms = (col + row) * 16
        cell_svg = (
            f'<rect class="day-cell" x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" rx="2.5" ry="2.5" '
            f'fill="{color}" style="animation-delay: {delay_ms}ms;">'
            f'<title>{tooltip_text}</title></rect>'
        )
        svg_cells.append(cell_svg)

    # Month text labels SVG
    month_svg_elements = []
    for mx, mname in month_labels:
        month_svg_elements.append(f'<text x="{mx}" y="{top_padding - 12}" class="label">{mname}</text>')

    # Day labels
    day_svg_elements = [
        f'<text x="{left_padding - 12}" y="{top_padding + 1 * (cell_size + cell_gap) - 2}" class="label" text-anchor="end">Mon</text>',
        f'<text x="{left_padding - 12}" y="{top_padding + 3 * (cell_size + cell_gap) - 2}" class="label" text-anchor="end">Wed</text>',
        f'<text x="{left_padding - 12}" y="{top_padding + 5 * (cell_size + cell_gap) - 2}" class="label" text-anchor="end">Fri</text>',
    ]

    # Legend SVG
    legend_x = width - 140
    legend_y = height - 25
    legend_cells = []
    for i, pcolor in enumerate(PALETTE[:5]):
        lx = legend_x + 35 + i * (cell_size + 3)
        legend_cells.append(f'<rect x="{lx}" y="{legend_y - 9}" width="{cell_size}" height="{cell_size}" rx="2" fill="{pcolor}" />')

    legend_svg = (
        f'<text x="{legend_x}" y="{legend_y}" class="sub-label">Less</text>'
        + "".join(legend_cells) +
        f'<text x="{legend_x + 35 + 5 * (cell_size + 3) + 4}" y="{legend_y}" class="sub-label">More</text>'
    )

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&amp;display=swap');

      .bg {{
        fill: #0d1117;
        rx: 12px;
        ry: 12px;
        stroke: #30363d;
        stroke-width: 1.5;
      }}
      .title {{
        font-family: 'Fira Code', monospace;
        font-size: 14px;
        font-weight: 600;
        fill: #58a6ff;
      }}
      .stats {{
        font-family: 'Fira Code', monospace;
        font-size: 12px;
        font-weight: 400;
        fill: #8b949e;
      }}
      .stat-highlight {{
        fill: #3fb950;
        font-weight: 600;
      }}
      .label {{
        font-family: 'Fira Code', monospace;
        font-size: 10px;
        fill: #8b949e;
      }}
      .sub-label {{
        font-family: 'Fira Code', monospace;
        font-size: 10px;
        fill: #484f58;
      }}
      .day-cell {{
        opacity: 0;
        transform: translateY(-4px) scale(0.9);
        animation: cascadeIn 0.35s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      }}
      @keyframes cascadeIn {{
        to {{
          opacity: 1;
          transform: translateY(0) scale(1);
        }}
      }}
    </style>
  </defs>

  <!-- Container Background -->
  <rect class="bg" width="{width}" height="{height}" />

  <!-- Header Title -->
  <text x="{left_padding}" y="26" class="title">⚡ {total} Contributions in the Last Year</text>
  <text x="{width - 240}" y="26" class="stats">Streak: <tspan class="stat-highlight">{current_streak} days</tspan> | Best: <tspan class="stat-highlight">{data.get("best_day", {}).get("count", 0)}</tspan></text>

  <!-- Month & Day Labels -->
  {''.join(month_svg_elements)}
  {''.join(day_svg_elements)}

  <!-- Grid Cells -->
  {''.join(svg_cells)}

  <!-- Footer Legend & Stats -->
  <text x="{left_padding}" y="{height - 23}" class="stats">Longest Streak: <tspan class="stat-highlight">{longest_streak} days</tspan> · Updated Daily</text>
  {legend_svg}
</svg>
"""

    out_file = Path("contrib-heatmap.svg")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"Successfully generated contrib-heatmap.svg ({width}x{height})")

if __name__ == "__main__":
    render_heatmap()
