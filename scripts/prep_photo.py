import sys
from pathlib import Path
import cv2
import numpy as np
from PIL import Image

def prep_photo(input_path_str="source-photo.jpg"):
    input_path = Path(input_path_str)
    if not input_path.exists():
        print(f"Error: {input_path} not found.")
        sys.exit(1)

    print(f"Prepping photo: {input_path}...")
    
    # Try using rembg for clean background removal
    has_rembg = False
    try:
        from rembg import remove
        with open(input_path, 'rb') as i:
            input_bytes = i.read()
            output_bytes = remove(input_bytes)
        img_pil = Image.open(io.BytesIO(output_bytes)).convert("RGBA")
        
        # Composite onto white background
        bg = Image.new("RGBA", img_pil.size, (255, 255, 255, 255))
        composite = Image.alpha_composite(bg, img_pil).convert("L")
        img_np = np.array(composite)
        has_rembg = True
        print("Background successfully removed using rembg.")
    except Exception as e:
        print(f"Note: rembg background removal skipped ({e}), falling back to OpenCV contrast processing.")
        img_cv = cv2.imread(str(input_path), cv2.IMREAD_GRAYSCALE)
        img_np = img_cv

    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) for portrait definition
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(img_np)

    output_path = Path("source-prepped.png")
    cv2.imwrite(str(output_path), enhanced)
    print(f"Prepped photo saved to {output_path.resolve()}")

if __name__ == "__main__":
    inp = sys.argv[1] if len(sys.argv) > 1 else "source-photo.jpg"
    prep_photo(inp)
