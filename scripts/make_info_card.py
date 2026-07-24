from pathlib import Path

def make_info_card():
    width = 490
    height = 360

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600;700&amp;display=swap');

      .card-bg {{
        fill: #0d1117;
        rx: 12px;
        ry: 12px;
        stroke: #30363d;
        stroke-width: 1.5;
      }}
      .window-btn-red {{ fill: #ff5f56; }}
      .window-btn-yellow {{ fill: #ffbd2e; }}
      .window-btn-green {{ fill: #27c93f; }}

      .term-text {{
        font-family: 'Fira Code', monospace;
        font-size: 12.5px;
        line-height: 1.6;
      }}
      
      .line {{
        opacity: 0;
        transform: translateX(-8px);
        animation: printLine 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      }}

      .user-host {{ fill: #58a6ff; font-weight: 700; }}
      .separator {{ fill: #484f58; }}
      .key {{ fill: #79c0ff; font-weight: 600; }}
      .val {{ fill: #c9d1d9; }}
      .val-accent {{ fill: #7ee787; font-weight: 500; }}
      .val-pink {{ fill: #ff7b72; }}
      .val-orange {{ fill: #ffa657; }}
      .val-purple {{ fill: #d2a8ff; }}
      
      .color-block-1 {{ fill: #ff7b72; }}
      .color-block-2 {{ fill: #ffa657; }}
      .color-block-3 {{ fill: #d2a8ff; }}
      .color-block-4 {{ fill: #79c0ff; }}
      .color-block-5 {{ fill: #7ee787; }}
      .color-block-6 {{ fill: #a5d6ff; }}

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
  <circle cx="22" cy="22" r="5.5" class="window-btn-red" />
  <circle cx="38" cy="22" r="5.5" class="window-btn-yellow" />
  <circle cx="54" cy="22" r="5.5" class="window-btn-green" />
  <text x="{width // 2}" y="26" text-anchor="middle" font-family="'Fira Code', monospace" font-size="11" fill="#8b949e" font-weight="500">ayush@github ~ neofetch</text>

  <!-- Line Dividers -->
  <line x1="1" y1="42" x2="{width - 1}" y2="42" stroke="#21262d" stroke-width="1" />

  <!-- Terminal Content Lines -->
  <g class="term-text">
    <!-- Header Line -->
    <g class="line" style="animation-delay: 100ms;">
      <text x="24" y="68" class="user-host">ayushnautiyal9520-create<tspan fill="#8b949e">@</tspan>github</text>
    </g>
    
    <!-- Separator -->
    <g class="line" style="animation-delay: 180ms;">
      <text x="24" y="86" class="separator">-----------------------------------------</text>
    </g>

    <!-- Details -->
    <g class="line" style="animation-delay: 260ms;">
      <text x="24" y="112"><tspan class="key">OS</tspan><tspan class="val">: macOS / Web Terminal</tspan></text>
    </g>

    <g class="line" style="animation-delay: 340ms;">
      <text x="24" y="136"><tspan class="key">Role</tspan><tspan class="val">: </tspan><tspan class="val-accent">Full-Stack Software Developer</tspan></text>
    </g>

    <g class="line" style="animation-delay: 420ms;">
      <text x="24" y="160"><tspan class="key">Stack</tspan><tspan class="val">: React, Node.js, Express, Python, Tailwind</tspan></text>
    </g>

    <g class="line" style="animation-delay: 500ms;">
      <text x="24" y="184"><tspan class="key">Projects</tspan><tspan class="val">: </tspan><tspan class="val-purple">Grymail Sender</tspan><tspan class="val">, </tspan><tspan class="val-orange">Onward Web</tspan></text>
    </g>

    <g class="line" style="animation-delay: 580ms;">
      <text x="24" y="208"><tspan class="key">Portfolio</tspan><tspan class="val">: </tspan><tspan class="val-pink">https://gryven.vercel.app</tspan></text>
    </g>

    <g class="line" style="animation-delay: 660ms;">
      <text x="24" y="232"><tspan class="key">Email</tspan><tspan class="val">: ayushnautiyal9520@gmail.com</tspan></text>
    </g>

    <g class="line" style="animation-delay: 740ms;">
      <text x="24" y="256"><tspan class="key">Focus</tspan><tspan class="val">: Scalable SaaS, PWAs, Clean Architecture</tspan></text>
    </g>

    <g class="line" style="animation-delay: 820ms;">
      <text x="24" y="280"><tspan class="key">Status</tspan><tspan class="val">: 🚀 Open to exciting opportunities</tspan></text>
    </g>

    <!-- Color Palette Blocks -->
    <g class="line" style="animation-delay: 900ms;">
      <rect x="24" y="308" width="22" height="14" rx="3" class="color-block-1" />
      <rect x="52" y="308" width="22" height="14" rx="3" class="color-block-2" />
      <rect x="80" y="308" width="22" height="14" rx="3" class="color-block-3" />
      <rect x="108" y="308" width="22" height="14" rx="3" class="color-block-4" />
      <rect x="136" y="308" width="22" height="14" rx="3" class="color-block-5" />
      <rect x="164" y="308" width="22" height="14" rx="3" class="color-block-6" />
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
