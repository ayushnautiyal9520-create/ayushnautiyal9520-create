@echo off
echo Setting up Animated GitHub Profile README for Ayush Nautiyal...

if not exist .venv (
    echo Creating virtual environment...
    python -m venv .venv
)

echo Activating environment and installing dependencies...
call .venv\Scripts\activate.bat
pip install -r scripts/requirements.txt

echo.
echo 1. Downloading Avatar...
python scripts/download_avatar.py

echo 2. Prepping Portrait Photo...
python scripts/prep_photo.py source-photo.jpg

echo 3. Generating ASCII Portrait SVG...
python scripts/make_ascii_svg.py

echo 4. Generating Neofetch Info Card SVG...
python scripts/make_info_card.py

echo 5. Fetching Live Contributions...
python scripts/fetch_contributions.py --username ayushnautiyal9520-create

echo 6. Rendering Heatmap SVG...
python scripts/render_heatmap_svg.py

echo.
echo ========================================================
echo Done! All SVGs and README.md generated successfully.
echo ========================================================
pause
