import base64
from pathlib import Path
from PIL import Image

def make_cyber_photo_card():
    photo_path = Path("source-photo.jpg")
    if not photo_path.exists():
        print("source-photo.jpg not found.")
        return

    # Convert photo to base64 data URI
    with open(photo_path, "rb") as f:
        img_bytes = f.read()
    b64_str = base64.b64encode(img_bytes).decode("utf-8")
    img_data_uri = f"data:image/jpeg;base64,{b64_str}"

    width = 410
    height = 380

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <linearGradient id="cyber-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="50%" stop-color="#818cf8" />
      <stop offset="100%" stop-color="#c084fc" />
    </linearGradient>
    <linearGradient id="photo-overlay" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.1" />
      <stop offset="100%" stop-color="#090d16" stop-opacity="0.6" />
    </linearGradient>
    <clipPath id="avatar-clip">
      <rect x="75" y="65" width="260" height="260" rx="130" ry="130" />
    </clipPath>
    <style>
      .card-bg {{
        fill: #090d16;
        rx: 14px;
        ry: 14px;
        stroke: url(#cyber-border);
        stroke-width: 1.8;
      }}
      .window-btn-red {{ fill: #f43f5e; }}
      .window-btn-yellow {{ fill: #fbbf24; }}
      .window-btn-green {{ fill: #34d399; }}

      .title-text {{
        font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace;
        font-size: 12px;
        fill: #38bdf8;
        font-weight: 600;
        letter-spacing: 0.5px;
      }}

      .avatar-ring {{
        fill: none;
        stroke: url(#cyber-border);
        stroke-width: 3.5;
      }}
      
      .name-label {{
        font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
        font-size: 15px;
        font-weight: 700;
        fill: #f8fafc;
      }}
      .role-label {{
        font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
        font-size: 12px;
        font-weight: 600;
        fill: #38bdf8;
      }}
    </style>
  </defs>

  <!-- Card Frame -->
  <rect class="card-bg" width="{width}" height="{height}" />

  <!-- Window Header -->
  <circle cx="22" cy="24" r="5.5" class="window-btn-red" />
  <circle cx="38" cy="24" r="5.5" class="window-btn-yellow" />
  <circle cx="54" cy="24" r="5.5" class="window-btn-green" />
  <text x="{width // 2}" y="28" text-anchor="middle" class="title-text">⚡ ayush_portrait.sys</text>
  <line x1="1" y1="44" x2="{width - 1}" y2="44" stroke="#1e293b" stroke-width="1.2" />

  <!-- Avatar Photo -->
  <g>
    <circle cx="{width // 2}" cy="180" r="108" class="avatar-ring" />
    <image href="{img_data_uri}" x="{width // 2 - 104}" y="76" width="208" height="208" clip-path="url(#avatar-clip)" preserveAspectRatio="xMidYMid slice" />
    <circle cx="{width // 2}" cy="180" r="104" fill="url(#photo-overlay)" pointer-events="none" />
  </g>

  <!-- Labels -->
  <text x="{width // 2}" y="318" text-anchor="middle" class="name-label">Ayush Nautiyal</text>
  <text x="{width // 2}" y="342" text-anchor="middle" class="role-label">Full-Stack Software Developer</text>
</svg>
"""

    out_file = Path("ayush-photo-card.svg")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"Successfully generated ayush-photo-card.svg ({width}x{height})")

if __name__ == "__main__":
    make_cyber_photo_card()
