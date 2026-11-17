@echo off
echo Setting up GTA VI Developer Showcase for Ayush Nautiyal...

echo.
echo 1. Generating GTA VI Dataset (4,689 Contributions, Jan 3 to Nov 17, 2026)...
python scripts/gta6_engine.py

echo.
echo 2. Rendering GTA VI SVG Heatmap and 3-Batch Showcase...
python scripts/render_gta6_svgs.py

echo.
echo 3. Testing Daily Sync Engine...
python scripts/fetch_live_daily.py --username ayushnautiyal9520-create

echo.
echo ========================================================
echo Done! All GTA VI SVGs, Data and Web UI Ready.
echo Zero Emojis, 4,689 Contributions, Daily Tracking Active.
echo ========================================================
pause
