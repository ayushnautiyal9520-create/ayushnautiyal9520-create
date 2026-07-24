import requests
from pathlib import Path

AVATAR_URL = "https://github.com/ayushnautiyal9520-create.png"
OUTPUT_PATH = Path("source-photo.jpg")

def download_avatar():
    print(f"Downloading avatar from {AVATAR_URL}...")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    res = requests.get(AVATAR_URL, headers=headers, timeout=15)
    res.raise_for_status()
    
    with open(OUTPUT_PATH, "wb") as f:
        f.write(res.content)
    
    print(f"Successfully saved avatar photo to {OUTPUT_PATH.resolve()}")

if __name__ == "__main__":
    download_avatar()
