import json
from pathlib import Path

PALETTE = [
    "#161b22",  # Level 0 - empty cell
    "#0e4429",  # Level 1 - low
    "#006d32",  # Level 2 - medium
    "#26a641",  # Level 3 - active
    "#39d353",  # Level 4 - high
    "#00f5d4"   # Level 5 - neon max
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

    cell_size = 11
    cell_gap = 4
    left_padding = 40
    top_padding = 45
    width = 860
    height = 210

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

        if date_str:
            month_idx = int(date_str.split("-")[1]) - 1
            if month_idx != last_month and row == 0 and col < 52:
                month_labels.append((x, MONTH_NAMES[month_idx]))
                last_month = month_idx

        tooltip_text = f"{count} contributions on {date_str}" if count > 0 else f"No contributions on {date_str}"

        delay_ms = (col + row) * 14
        cell_svg = (
            f'<rect class="day-cell" x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" rx="2.5" ry="2.5" '
            f'fill="{color}" style="animation-delay: {delay_ms}ms;">'
            f'<title>{tooltip_text}</title></rect>'
        )
        svg_cells.append(cell_svg)

    month_svg_elements = []
    for mx, mname in month_labels:
        month_svg_elements.append(f'<text x="{mx}" y="{top_padding - 12}" class="label">{mname}</text>')

    day_svg_elements = [
        f'<text x="{left_padding - 12}" y="{top_padding + 1 * (cell_size + cell_gap) - 2}" class="label" text-anchor="end">Mon</text>',
        f'<text x="{left_padding - 12}" y="{top_padding + 3 * (cell_size + cell_gap) - 2}" class="label" text-anchor="end">Wed</text>',
        f'<text x="{left_padding - 12}" y="{top_padding + 5 * (cell_size + cell_gap) - 2}" class="label" text-anchor="end">Fri</text>',
    ]

    legend_x = width - 150
    legend_y = height - 23
    legend_cells = []
    for i, pcolor in enumerate(PALETTE[:5]):
        lx = legend_x + 38 + i * (cell_size + 3)
        legend_cells.append(f'<rect x="{lx}" y="{legend_y - 9}" width="{cell_size}" height="{cell_size}" rx="2" fill="{pcolor}" />')

    legend_svg = (
        f'<text x="{legend_x}" y="{legend_y}" class="sub-label">Less</text>'
        + "".join(legend_cells) +
        f'<text x="{legend_x + 38 + 5 * (cell_size + 3) + 4}" y="{legend_y}" class="sub-label">More</text>'
    )

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <linearGradient id="heatmap-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="50%" stop-color="#818cf8" />
      <stop offset="100%" stop-color="#c084fc" />
    </linearGradient>
    <style>
      .bg {{
        fill: #090d16;
        rx: 14px;
        ry: 14px;
        stroke: url(#heatmap-border);
        stroke-width: 1.8;
      }}
      .title {{
        font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace;
        font-size: 14px;
        font-weight: 700;
        fill: #38bdf8;
        letter-spacing: 0.5px;
      }}
      .stats {{
        font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace;
        font-size: 12px;
        font-weight: 500;
        fill: #94a3b8;
      }}
      .stat-highlight {{
        fill: #34d399;
        font-weight: 700;
      }}
      .label {{
        font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace;
        font-size: 10px;
        fill: #64748b;
        font-weight: 500;
      }}
      .sub-label {{
        font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace;
        font-size: 10px;
        fill: #64748b;
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

  <!-- Header Title & Stats -->
  <text x="{left_padding}" y="26" class="title">⚡ {total} Contributions in the Last Year</text>
  <text x="{width - 250}" y="26" class="stats">Streak: <tspan class="stat-highlight">{current_streak} days</tspan> | Best: <tspan class="stat-highlight">{data.get("best_day", {}).get("count", 0)}</tspan></text>

  <!-- Month & Day Labels -->
  {''.join(month_svg_elements)}
  {''.join(day_svg_elements)}

  <!-- Grid Cells -->
  {''.join(svg_cells)}

  <!-- Footer Legend & Stats -->
  <text x="{left_padding}" y="{height - 21}" class="stats">Max Streak: <tspan class="stat-highlight">{longest_streak} days</tspan> · Updated Daily via GitHub Actions</text>
  {legend_svg}
</svg>
"""

    out_file = Path("contrib-heatmap.svg")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"Successfully generated modern contrib-heatmap.svg ({width}x{height})")

if __name__ == "__main__":
    render_heatmap()
