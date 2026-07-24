import os
from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps

RAMP = " .:-=+*#%@"  # Crisp density ramp

def image_to_ascii(img_path, cols=52, aspect_ratio=0.52):
    img = Image.open(img_path).convert("L")
    w, h = img.size
    
    # Tight crop around Ayush's head, face and shoulders (top center region)
    # Box: (left, upper, right, lower)
    crop_box = (int(w * 0.18), int(h * 0.05), int(w * 0.82), int(h * 0.75))
    img = img.crop(crop_box)
    
    # Enhance contrast specifically for face details
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.2)
    
    sharpener = ImageEnhance.Sharpness(img)
    img = sharpener.enhance(2.0)

    w_c, h_c = img.size
    rows = int((h_c / w_c) * cols * aspect_ratio)
    img_resized = img.resize((cols, rows), Image.Resampling.LANCZOS)
    
    ascii_rows = []
    ramp_len = len(RAMP)
    for y in range(rows):
        row_chars = []
        for x in range(cols):
            pixel = img_resized.getpixel((x, y))
            # Invert: dark features (hair, eyes, shadow) -> dense chars, bright background -> spaces
            if pixel > 215:  # Suppress bright background noise to empty spaces
                char = " "
            else:
                val = 255 - pixel
                idx = int((val / 255) * (ramp_len - 1))
                char = RAMP[idx]
            row_chars.append(char)
        ascii_rows.append("".join(row_chars))
    
    return ascii_rows, cols, rows

def make_ascii_svg():
    input_img = Path("source-photo.jpg")
    if not input_img.exists():
        input_img = Path("source-prepped.png")

    if not input_img.exists():
        print("No source-photo.jpg found.")
        return

    print(f"Generating face-focused ASCII SVG from {input_img}...")
    ascii_rows, cols, num_rows = image_to_ascii(input_img, cols=52)

    width = 410
    height = 380
    font_size = 9.8
    row_height = 11.8
    left_margin = 28
    top_margin = 56

    row_elements = []
    for idx, row_text in enumerate(ascii_rows):
        y_pos = top_margin + idx * row_height
        delay_ms = idx * 45
        escaped_text = (
            row_text.replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
        )
        row_elements.append(
            f'<g class="ascii-row" style="animation-delay: {delay_ms}ms;">'
            f'<text x="{left_margin}" y="{y_pos:.1f}">{escaped_text}</text>'
            f'</g>'
        )

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <linearGradient id="cyber-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="50%" stop-color="#818cf8" />
      <stop offset="100%" stop-color="#c084fc" />
    </linearGradient>
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

      .ascii-row {{
        font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace;
        font-size: {font_size}px;
        font-weight: 700;
        fill: #38bdf8;
        letter-spacing: 1.2px;
        white-space: pre;
        opacity: 0;
        transform: translateY(-2px);
        animation: typeRow 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      }}

      @keyframes typeRow {{
        to {{
          opacity: 1;
          transform: translateY(0);
          fill: #e0f2fe;
        }}
      }}
    </style>
  </defs>

  <!-- Card Background -->
  <rect class="card-bg" width="{width}" height="{height}" />

  <!-- Window Header -->
  <circle cx="22" cy="24" r="5.5" class="window-btn-red" />
  <circle cx="38" cy="24" r="5.5" class="window-btn-yellow" />
  <circle cx="54" cy="24" r="5.5" class="window-btn-green" />
  <text x="{width // 2}" y="28" text-anchor="middle" class="title-text">⚡ ayush_portrait.ascii</text>
  <line x1="1" y1="44" x2="{width - 1}" y2="44" stroke="#1e293b" stroke-width="1.2" />

  <!-- ASCII Portrait Rows -->
  {''.join(row_elements)}
</svg>
"""

    out_file = Path("ayush-ascii.svg")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"Successfully generated face-focused ayush-ascii.svg ({width}x{height})")

if __name__ == "__main__":
    make_ascii_svg()
