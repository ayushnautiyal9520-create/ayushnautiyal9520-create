from pathlib import Path

def make_info_card():
    width = 450
    height = 380

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <linearGradient id="card-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="50%" stop-color="#818cf8" />
      <stop offset="100%" stop-color="#c084fc" />
    </linearGradient>
    <linearGradient id="title-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="100%" stop-color="#818cf8" />
    </linearGradient>
    <style>
      .card-bg {{
        fill: #090d16;
        rx: 14px;
        ry: 14px;
        stroke: url(#card-border);
        stroke-width: 1.8;
      }}
      .window-btn-red {{ fill: #f43f5e; }}
      .window-btn-yellow {{ fill: #fbbf24; }}
      .window-btn-green {{ fill: #34d399; }}

      .term-text {{
        font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace;
        font-size: 12.5px;
        line-height: 1.6;
      }}
      
      .line {{
        opacity: 0;
        transform: translateX(-10px);
        animation: printLine 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      }}

      .user-host {{ fill: url(#title-grad); font-weight: 700; font-size: 14px; letter-spacing: 0.5px; }}
      .separator {{ fill: #334155; }}
      .key {{ fill: #38bdf8; font-weight: 600; }}
      .val {{ fill: #f1f5f9; }}
      .val-accent {{ fill: #34d399; font-weight: 600; }}
      .val-pink {{ fill: #f43f5e; font-weight: 600; }}
      .val-orange {{ fill: #fb923c; }}
      .val-purple {{ fill: #c084fc; font-weight: 600; }}
      .val-cyan {{ fill: #22d3ee; }}
      
      .tag-bg {{ fill: #1e293b; rx: 4px; ry: 4px; }}
      .tag-text {{ font-size: 10px; font-weight: 600; font-family: ui-monospace, Consolas, monospace; }}

      @keyframes printLine {{
        to {{
          opacity: 1;
          transform: translateX(0);
        }}
      }}
    </style>
  </defs>

  <!-- Card Frame -->
  <rect class="card-bg" width="{width}" height="{height}" />

  <!-- Window Controls -->
  <circle cx="22" cy="24" r="5.5" class="window-btn-red" />
  <circle cx="38" cy="24" r="5.5" class="window-btn-yellow" />
  <circle cx="54" cy="24" r="5.5" class="window-btn-green" />
  <text x="{width // 2}" y="28" text-anchor="middle" font-family="ui-monospace, Consolas, monospace" font-size="11" fill="#94a3b8" font-weight="600">ayush@github ~ neofetch</text>

  <!-- Line Dividers -->
  <line x1="1" y1="44" x2="{width - 1}" y2="44" stroke="#1e293b" stroke-width="1.2" />

  <!-- Terminal Content Lines -->
  <g class="term-text">
    <!-- Header Line -->
    <g class="line" style="animation-delay: 100ms;">
      <text x="24" y="72" class="user-host">ayushnautiyal9520-create<tspan fill="#64748b">@</tspan>github</text>
    </g>
    
    <!-- Separator -->
    <g class="line" style="animation-delay: 180ms;">
      <text x="24" y="90" class="separator">-----------------------------------------</text>
    </g>

    <!-- Details -->
    <g class="line" style="animation-delay: 260ms;">
      <text x="24" y="116"><tspan class="key">OS</tspan><tspan class="val">: macOS / Web Terminal</tspan></text>
    </g>

    <g class="line" style="animation-delay: 340ms;">
      <text x="24" y="142"><tspan class="key">Role</tspan><tspan class="val">: </tspan><tspan class="val-accent">⚡ Full-Stack Software Developer</tspan></text>
    </g>

    <g class="line" style="animation-delay: 420ms;">
      <text x="24" y="168"><tspan class="key">Stack</tspan><tspan class="val">: React • Next.js • Node • Express • Tailwind</tspan></text>
    </g>

    <g class="line" style="animation-delay: 500ms;">
      <text x="24" y="194"><tspan class="key">Projects</tspan><tspan class="val">: </tspan><tspan class="val-purple">Grymail Sender</tspan><tspan class="val">, </tspan><tspan class="val-orange">Onward Web</tspan></text>
    </g>

    <g class="line" style="animation-delay: 580ms;">
      <text x="24" y="220"><tspan class="key">Portfolio</tspan><tspan class="val">: </tspan><tspan class="val-cyan">https://gryven.vercel.app</tspan></text>
    </g>

    <g class="line" style="animation-delay: 660ms;">
      <text x="24" y="246"><tspan class="key">Email</tspan><tspan class="val">: ayushnautiyal9520@gmail.com</tspan></text>
    </g>

    <g class="line" style="animation-delay: 740ms;">
      <text x="24" y="272"><tspan class="key">Focus</tspan><tspan class="val">: Scalable SaaS, Modern PWAs &amp; Web Apps</tspan></text>
    </g>

    <g class="line" style="animation-delay: 820ms;">
      <text x="24" y="298"><tspan class="key">Status</tspan><tspan class="val">: </tspan><tspan class="val-accent">🟢 Available for New Opportunities</tspan></text>
    </g>

    <!-- Tech Badge Pills -->
    <g class="line" style="animation-delay: 900ms;">
      <rect x="24" y="324" width="70" height="22" class="tag-bg" stroke="#38bdf8" stroke-width="1" />
      <text x="59" y="339" text-anchor="middle" class="tag-text" fill="#38bdf8">REACT</text>

      <rect x="104" y="324" width="70" height="22" class="tag-bg" stroke="#34d399" stroke-width="1" />
      <text x="139" y="339" text-anchor="middle" class="tag-text" fill="#34d399">NODE.JS</text>

      <rect x="184" y="324" width="70" height="22" class="tag-bg" stroke="#c084fc" stroke-width="1" />
      <text x="219" y="339" text-anchor="middle" class="tag-text" fill="#c084fc">PYTHON</text>

      <rect x="264" y="324" width="80" height="22" class="tag-bg" stroke="#fb923c" stroke-width="1" />
      <text x="304" y="339" text-anchor="middle" class="tag-text" fill="#fb923c">TAILWIND</text>

      <rect x="354" y="324" width="72" height="22" class="tag-bg" stroke="#f43f5e" stroke-width="1" />
      <text x="390" y="339" text-anchor="middle" class="tag-text" fill="#f43f5e">EXPRESS</text>
    </g>
  </g>
</svg>
"""

    out_file = Path("info-card.svg")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"Successfully generated info-card.svg ({width}x{height})")

if __name__ == "__main__":
    make_info_card()
