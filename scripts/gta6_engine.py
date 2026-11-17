"""
GTA VI Contribution Data Engine
Generates full-year dataset (Jan 3, 2026 to Nov 17, 2026) with exactly 4,689 contributions,
realistic intentional gaps, active streaks, and three-batch developer statistics.
STRICT: NO EMOJIS.
"""

import json
import datetime
from pathlib import Path

def generate_gta6_dataset():
    start_date = datetime.date(2026, 1, 3)
    end_date = datetime.date(2026, 11, 17)
    target_total = 4689

    # Intentional Gap intervals (0 contributions)
    gap_ranges = [
        (datetime.date(2026, 3, 2), datetime.date(2026, 3, 11)),   # Q1 Architecture Review
        (datetime.date(2026, 6, 1), datetime.date(2026, 6, 8)),    # Cloud Infrastructure Migration
        (datetime.date(2026, 8, 22), datetime.date(2026, 8, 31)),  # Strategic Mid-Year Recharge
    ]

    # Scattered rest days (isolated gaps in early year)
    scattered_rest = {
        datetime.date(2026, 1, 18),
        datetime.date(2026, 1, 25),
        datetime.date(2026, 2, 8),
        datetime.date(2026, 2, 22),
        datetime.date(2026, 4, 12),
        datetime.date(2026, 4, 26),
        datetime.date(2026, 5, 17),
        datetime.date(2026, 7, 5),
        datetime.date(2026, 7, 19),
        datetime.date(2026, 8, 9),
    }

    def is_in_gap(d):
        if d in scattered_rest:
            return True
        for g_start, g_end in gap_ranges:
            if g_start <= d <= g_end:
                return True
        return False

    days = []
    curr = start_date
    while curr <= end_date:
        days.append({
            "date": curr.strftime("%Y-%m-%d"),
            "date_obj": curr,
            "in_gap": is_in_gap(curr),
            "count": 0,
            "level": 0
        })
        curr += datetime.timedelta(days=1)

    active_days = [d for d in days if not d["in_gap"]]
    num_active = len(active_days)

    # Base allocation: distribute 4689 across active days realistically
    # Peak crunch days (high commits): 50-54 commits
    # Heavy sprint days: 25-45 commits
    # Standard days: 12-24 commits
    # Light days: 5-11 commits
    
    # Deterministic pseudo-random generation based on date
    raw_weights = []
    for d in active_days:
        dt = d["date_obj"]
        # Seed by day of year and weekday
        doy = dt.timetuple().tm_yday
        weekday = dt.weekday() # 0 = Monday, 6 = Sunday
        
        # High crunch phases: late Feb, late April, mid-July, October (Q4 push)
        if 280 <= doy <= 310: # October sprint
            weight = 32 + (doy % 23)
        elif 190 <= doy <= 220: # July sprint
            weight = 28 + (doy % 19)
        elif 105 <= doy <= 135: # April release
            weight = 24 + (doy % 17)
        elif doy >= 315: # November crunch towards today Nov 17
            weight = 22 + (doy % 15)
        else:
            weight = 12 + (doy % 13)
        
        # Weekday tuning (higher Tue-Thu, slightly lighter on weekends)
        if weekday in (1, 2, 3):
            weight = int(weight * 1.2)
        elif weekday in (5, 6):
            weight = max(5, int(weight * 0.75))
            
        raw_weights.append(weight)

    sum_weights = sum(raw_weights)
    
    # Scale exactly to 4689
    counts = [int(w * target_total / sum_weights) for w in raw_weights]
    diff = target_total - sum(counts)
    
    # Distribute remainder to peak sprint days
    idx = 0
    while diff > 0:
        counts[idx % len(counts)] += 1
        diff -= 1
        idx += 3
    while diff < 0:
        counts[idx % len(counts)] -= 1
        diff += 1
        idx += 5

    # Assign back to active days
    for d, c in zip(active_days, counts):
        d["count"] = c
        # Map levels (0 to 5)
        if c == 0:
            d["level"] = 0
        elif c <= 8:
            d["level"] = 1
        elif c <= 16:
            d["level"] = 2
        elif c <= 28:
            d["level"] = 3
        elif c <= 42:
            d["level"] = 4
        else:
            d["level"] = 5

    # Remove temporary date_obj
    clean_days = []
    for d in days:
        clean_days.append({
            "date": d["date"],
            "count": d["count"],
            "level": d["level"],
            "tooltip": f"{d['count']} contributions on {d['date']}" if d["count"] > 0 else f"Strategic pause / 0 contributions on {d['date']}"
        })

    # Calculate streaks
    longest_streak = 0
    temp_streak = 0
    current_streak = 0
    best_day = {"date": "", "count": 0}

    for d in clean_days:
        cnt = d["count"]
        if cnt > best_day["count"]:
            best_day = {"date": d["date"], "count": cnt}

        if cnt > 0:
            temp_streak += 1
            if temp_streak > longest_streak:
                longest_streak = temp_streak
        else:
            temp_streak = 0

    # Current streak leading up to 2026-11-17
    for d in reversed(clean_days):
        if d["count"] > 0:
            current_streak += 1
        else:
            break

    # Structured 3 Batches Data
    stats_data = {
        "dataset_scope": {
            "start_date": "2026-01-03",
            "end_date": "2026-11-17",
            "total_days": len(clean_days),
            "active_days": len(active_days),
            "intentional_gap_days": len(clean_days) - len(active_days),
            "total_contributions": sum(d["count"] for d in clean_days),
            "current_streak": current_streak,
            "longest_streak": longest_streak,
            "best_day": best_day,
            "theme": "GTA VI - Vice City / Leonida State",
            "updated_anchor": "2026-11-17"
        },
        "batches": {
            "batch_1": {
                "id": "BATCH_01",
                "codename": "SYNDICATE CORE // VELOCITY",
                "category": "Pro Developer, High Commits & Streaks",
                "items": [
                    {
                        "metric": "PRO DEVELOPER CLASSIFICATION",
                        "value": "TIER-S ARCHITECT",
                        "subtext": "Wanted Level: 5-Star Maximum Code Velocity | 99.98% System Uptime",
                        "code": "PRO_DEV_S_TIER"
                    },
                    {
                        "metric": "HIGH COMMITS TOTAL",
                        "value": "4,689 COMMITS",
                        "subtext": "Peak Burst: 54 Commits/Day | Average 22.4 Commits/Active Day",
                        "code": "VOL_PEAK_CRUNCH"
                    },
                    {
                        "metric": "COMMIT STREAKS",
                        "value": f"{current_streak} DAYS ACTIVE",
                        "subtext": f"Marathon Record: {longest_streak} Days Continuous Shipping | 0 Breaking Changes",
                        "code": "STREAK_UNBROKEN"
                    }
                ]
            },
            "batch_2": {
                "id": "BATCH_02",
                "codename": "HEIST OPS // CODE DISCIPLINE",
                "category": "Daily Contributions, PRs & Issues Resolved",
                "items": [
                    {
                        "metric": "DAILY CONTRIBUTIONS DENSITY",
                        "value": f"{len(active_days)} / {len(clean_days)} DAYS",
                        "subtext": "86.8% Active Density | 4 Strategic Architectural Gaps Maintained",
                        "code": "DAILY_HEATMAP_46WK"
                    },
                    {
                        "metric": "PULL REQUESTS AND MERGES",
                        "value": "342 PRODUCTION PRS",
                        "subtext": "99.4% Clean Merge Rate | Sub-4hr Code Review Turnaround",
                        "code": "PR_ZERO_DEFECT"
                    },
                    {
                        "metric": "ISSUES RESOLVED",
                        "value": "489 TICKETS SQUASHED",
                        "subtext": "100% P0/P1 SLA Adherence | 84 Architecture Refactors Completed",
                        "code": "ISSUES_HARDENED"
                    }
                ]
            },
            "batch_3": {
                "id": "BATCH_03",
                "codename": "THE EMPIRE // FIELD IMPACT",
                "category": "Projects, Development Activity & Highlights",
                "items": [
                    {
                        "metric": "PROJECTS & ACTIVE REPOSITORIES",
                        "value": "18 REPOSITORIES",
                        "subtext": "Full-Stack SaaS, AI Agents, Microservices, Cloud Infrastructure",
                        "code": "PROJ_SAAS_ECOSYSTEM"
                    },
                    {
                        "metric": "DEVELOPMENT ACTIVITY PROFILE",
                        "value": "POLYGLOT ARCHITECT",
                        "subtext": "Next.js/React (38%), TypeScript/Node (32%), Python/AI (20%), Postgres (10%)",
                        "code": "STACK_PRODUCTION_TIER"
                    },
                    {
                        "metric": "OVERALL CONTRIBUTION HIGHLIGHTS",
                        "value": "4,689 MILESTONES SHIPPED",
                        "subtext": "Full 2026 Roadmap Executed | Rock-solid Engineering Execution",
                        "code": "MISSION_PASSED_RESPECT"
                    }
                ]
            }
        }
    }

    out_contributions = {
        "username": "ayushnautiyal9520-create",
        "total_contributions": target_total,
        "current_streak": current_streak,
        "longest_streak": longest_streak,
        "best_day": best_day,
        "start_date": "2026-01-03",
        "end_date": "2026-11-17",
        "days": clean_days
    }

    data_dir = Path("data")
    data_dir.mkdir(parents=True, exist_ok=True)

    with open(data_dir / "contributions.json", "w", encoding="utf-8") as f:
        json.dump(out_contributions, f, indent=2)

    with open(data_dir / "gta6_stats.json", "w", encoding="utf-8") as f:
        json.dump(stats_data, f, indent=2)

    print(f"Generated {len(clean_days)} days from {start_date} to {end_date}.")
    print(f"Total Contributions: {sum(d['count'] for d in clean_days)} (Target: {target_total}).")
    print(f"Active Days: {len(active_days)}, Gap Days: {len(clean_days) - len(active_days)}.")
    print(f"Current Streak: {current_streak} days, Longest Streak: {longest_streak} days, Best Day: {best_day['date']} ({best_day['count']} commits).")

if __name__ == "__main__":
    generate_gta6_dataset()
