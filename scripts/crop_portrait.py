import cv2
import numpy as np
from PIL import Image
from pathlib import Path

def crop_face_and_shoulders(image_path="source-photo.jpg"):
    img = cv2.imread(str(image_path))
    if img is None:
        print(f"Error: Could not load {image_path}")
        return None

    h, w, _ = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load OpenCV pre-trained face detector
    face_cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))

    if len(faces) > 0:
        # Find largest face
        faces = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)
        fx, fy, fw, fh = faces[0]
        print(f"Face detected at x={fx}, y={fy}, w={fw}, h={fh}")

        # Expand crop around face to include hair, head, and shoulders
        margin_x = int(fw * 1.2)
        margin_top = int(fh * 0.9)
        margin_bottom = int(fh * 1.8)

        x1 = max(0, fx - margin_x)
        y1 = max(0, fy - margin_top)
        x2 = min(w, fx + fw + margin_x)
        y2 = min(h, fy + fh + margin_bottom)

        cropped = img[y1:y2, x1:x2]
    else:
        print("No face detected by Cascade, falling back to upper-center portrait crop.")
        # Crop top-center 55% of image for upper body portrait
        crop_w = int(w * 0.65)
        crop_h = int(h * 0.70)
        start_x = max(0, (w - crop_w) // 2)
        start_y = 0
        cropped = img[start_y:start_y + crop_h, start_x:start_x + crop_w]

    cropped_rgb = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
    out_pil = Image.fromarray(cropped_rgb)
    out_file = Path("source-cropped.jpg")
    out_pil.save(out_file)
    print(f"Saved tightly cropped face portrait to {out_file.resolve()}")
    return out_file

if __name__ == "__main__":
    crop_face_and_shoulders()
