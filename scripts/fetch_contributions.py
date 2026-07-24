import argparse
import json
import re
import os
from pathlib import Path
import requests
from bs4 import BeautifulSoup

DEFAULT_USERNAME = "ayushnautiyal9520-create"

def fetch_contributions(username: str):
    url = f"https://github.com/users/{username}/contributions"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract total count string e.g. "151 contributions in the last year"
    heading = soup.find("h2", id="js-contribution-activity-description")
    total_str = heading.get_text(strip=True) if heading else ""
    total_match = re.search(r"([\d,]+)\s+contributions", total_str, re.IGNORECASE)
    total_count = int(total_match.group(1).replace(",", "")) if total_match else 0

    # Parse days
    days = []
    tooltips = {}
    
    # Map tooltips by `for` attribute
    for tt in soup.find_all("tool-tip"):
        for_id = tt.get("for")
        if for_id:
            tooltips[for_id] = tt.get_text(strip=True)

    td_days = soup.find_all("td", class_="ContributionCalendar-day")
    
    for td in td_days:
        date_str = td.get("data-date")
        if not date_str:
            continue
        level = int(td.get("data-level", "0"))
        day_id = td.get("id")
        
        count = 0
        tt_text = tooltips.get(day_id, "")
        count_match = re.search(r"(\d+)\s+contribution", tt_text, re.IGNORECASE)
        if count_match:
            count = int(count_match.group(1))
        elif "No contributions" in tt_text:
            count = 0
        else:
            # Fallback level approximation if count tooltip missing
            count = level * 3 if level > 0 else 0

        days.append({
            "date": date_str,
            "count": count,
            "level": level,
            "tooltip": tt_text
        })

    # Sort days chronologically
    days.sort(key=lambda d: d["date"])

    # Calculate Streaks
    current_streak = 0
    longest_streak = 0
    temp_streak = 0
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

    # Current streak from recent active days
    rev_days = list(reversed(days))
    for d in rev_days:
        if d["count"] > 0:
            current_streak += 1
        else:
            # allow today/yesterday 0 count if checking live day end
            if current_streak > 0:
                break

    output_data = {
        "username": username,
        "total_contributions": total_count or sum(d["count"] for d in days),
        "current_streak": current_streak,
        "longest_streak": longest_streak,
        "best_day": best_day,
        "days": days
    }

    out_dir = Path("data")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "contributions.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)

    print(f"Successfully fetched contributions for '{username}'. Total: {output_data['total_contributions']}, Streaks: {current_streak} current / {longest_streak} max.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch public GitHub contribution calendar.")
    parser.add_argument("--username", type=str, default=DEFAULT_USERNAME, help="GitHub Username")
    args = parser.parse_args()
    fetch_contributions(args.username)
