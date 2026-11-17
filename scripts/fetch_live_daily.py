"""
GTA VI Daily Contribution Sync Engine
Anchor Date: November 17, 2026.
Continuously updates daily contributions based on actual GitHub commits,
maintaining the full-year 4,689 base, active streaks, countdowns, and SVG rendering.
STRICT: NO EMOJIS.
"""

import json
import datetime
import re
import argparse
from pathlib import Path
import urllib.request
import urllib.error

DEFAULT_USERNAME = "ayushnautiyal9520-create"

def fetch_live_day_count(username: str, target_date_str: str) -> int:
    """Fetches real-time contribution count for the given user from GitHub public profile."""
    url = f"https://github.com/users/{username}/contributions"
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
    )
    
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8")
            
        # Match target date cell e.g. data-date="2026-11-17"
        date_pattern = re.compile(rf'data-date="{target_date_str}"[^>]*id="([^"]+)"')
        match = date_pattern.search(html)
        if match:
            cell_id = match.group(1)
            # Find associated tooltip
            tt_pattern = re.compile(rf'<tool-tip[^>]*for="{cell_id}"[^>]*>(.*?)</tool-tip>', re.DOTALL)
            tt_match = tt_pattern.search(html)
            if tt_match:
                tt_text = tt_match.group(1).strip()
                count_match = re.search(r"(\d+)\s+contribution", tt_text, re.IGNORECASE)
                if count_match:
                    return int(count_match.group(1))
    except Exception as e:
        print(f"[GTA VI SYNC] Notice: Live fetch returned fallback or network limitation: {e}")
        
    return 0

def update_daily_contributions(username: str = DEFAULT_USERNAME):
    data_file = Path("data/contributions.json")
    if not data_file.exists():
        print("[ERROR] data/contributions.json not found. Run gta6_engine.py first.")
        return

    with open(data_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    days = data.get("days", [])
    today_str = datetime.date.today().strftime("%Y-%m-%d")

    # If running in 2026 or testing
    anchor_date_str = "2026-11-17"
    effective_today = today_str if today_str >= "2026-11-17" else anchor_date_str

    print(f"[GTA VI SYNC] Running daily sync for user '{username}' on date {effective_today}...")
    actual_commits = fetch_live_day_count(username, effective_today)
    print(f"[GTA VI SYNC] Live actual contributions fetched for {effective_today}: {actual_commits}")

    # Find or append effective_today
    day_entry = None
    for d in days:
        if d["date"] == effective_today:
            day_entry = d
            break

    if day_entry is None:
        day_entry = {
            "date": effective_today,
            "count": max(actual_commits, 1),
            "level": 1,
            "tooltip": f"{max(actual_commits, 1)} contributions on {effective_today}"
        }
        days.append(day_entry)
    else:
        # If new actual commits occurred, update count
        if actual_commits > day_entry["count"]:
            diff = actual_commits - day_entry["count"]
            day_entry["count"] = actual_commits
            data["total_contributions"] = data.get("total_contributions", 4689) + diff

    # Recalculate level
    c = day_entry["count"]
    if c == 0: day_entry["level"] = 0
    elif c <= 8: day_entry["level"] = 1
    elif c <= 16: day_entry["level"] = 2
    elif c <= 28: day_entry["level"] = 3
    elif c <= 42: day_entry["level"] = 4
    else: day_entry["level"] = 5

    # Recalculate streaks
    longest_streak = 0
    temp_streak = 0
    current_streak = 0
    best_day = {"date": "", "count": 0}

    for d in days:
        cnt = d["count"]
        if cnt > best_day["count"]:
            best_day = {"date": d["date"], "count": cnt}
        if cnt > 0:
            temp_streak += 1
            if temp_streak > longest_streak:
                longest_streak = temp_streak
        else:
            temp_streak = 0

    for d in reversed(days):
        if d["count"] > 0:
            current_streak += 1
        else:
            break

    data["current_streak"] = current_streak
    data["longest_streak"] = longest_streak
    data["best_day"] = best_day
    data["days"] = days

    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    # Re-render SVGs
    import render_gta6_svgs
    render_gta6_svgs.render_hero_banner()
    render_gta6_svgs.render_heatmap_svg()
    render_gta6_svgs.render_batches_svg()

    print(f"[GTA VI SYNC] Successfully updated daily graph! Total: {data.get('total_contributions')}, Current Streak: {current_streak} days.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GTA VI Daily Sync Engine")
    parser.add_argument("--username", type=str, default=DEFAULT_USERNAME)
    args = parser.parse_args()
    update_daily_contributions(args.username)
