import os
from pathlib import Path
from PIL import Image

RAMP = " .`:-=+*cs#%@"  # Bright (sparse) -> Dark (dense)

def image_to_ascii(img_path, cols=84, aspect_ratio=0.55):
    img = Image.open(img_path).convert("L")
    w, h = img.size
    rows = int((h / w) * cols * aspect_ratio)
    img_resized = img.resize((cols, rows), Image.Resampling.LANCZOS)
    
    ascii_rows = []
    ramp_len = len(RAMP)
    for y in range(rows):
        row_str = ""
        for x in range(cols):
            pixel = img_resized.getpixel((x, y))
            # Invert: white background -> space (sparse), dark hair/features -> dense characters
            idx = int((255 - pixel) / 255 * (ramp_len - 1))
            char = RAMP[idx]
            # Replace spaces with non-breaking space for XML preserving if needed
            row_str += char
        ascii_rows.append(row_str)
    
    return ascii_rows, cols, rows

def make_ascii_svg():
    input_img = Path("source-prepped.png")
    if not input_img.exists():
        input_img = Path("source-photo.jpg")

    if not input_img.exists():
        print("No source-prepped.png or source-photo.jpg found.")
        return

    print(f"Generating ASCII SVG from {input_img}...")
    ascii_rows, cols, num_rows = image_to_ascii(input_img, cols=82)

    width = 370
    height = 360
    font_size = 6.8
    row_height = 7.4
    left_margin = 16
    top_margin = 46

    row_elements = []
    for idx, row_text in enumerate(ascii_rows):
        y_pos = top_margin + idx * row_height
        delay_ms = idx * 55
        # Escape special XML chars
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
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&amp;display=swap');

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

      .title-text {{
        font-family: 'Fira Code', monospace;
        font-size: 11px;
        fill: #8b949e;
        font-weight: 500;
      }}

      .ascii-row {{
        font-family: 'Fira Code', 'Courier New', monospace;
        font-size: {font_size}px;
        fill: #8b949e;
        white-space: pre;
        opacity: 0;
        transform: translateX(-4px);
        animation: typeRow 0.25s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      }}

      @keyframes typeRow {{
        to {{
          opacity: 1;
          transform: translateX(0);
          fill: #c9d1d9;
        }}
      }}
    </style>
  </defs>

  <!-- Card Background -->
  <rect class="card-bg" width="{width}" height="{height}" />

  <!-- Window Header -->
  <circle cx="22" cy="22" r="5.5" class="window-btn-red" />
  <circle cx="38" cy="22" r="5.5" class="window-btn-yellow" />
  <circle cx="54" cy="22" r="5.5" class="window-btn-green" />
  <text x="{width // 2}" y="26" text-anchor="middle" class="title-text">ayush_portrait.ascii</text>
  <line x1="1" y1="42" x2="{width - 1}" y2="42" stroke="#21262d" stroke-width="1" />

  <!-- ASCII Portrait Rows -->
  {''.join(row_elements)}
</svg>
"""

    out_file = Path("ayush-ascii.svg")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"Successfully generated ayush-ascii.svg ({width}x{height})")

if __name__ == "__main__":
    make_ascii_svg()
