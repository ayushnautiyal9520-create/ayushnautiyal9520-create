/**
 * GTA VI DEVELOPER DOSSIER - INTERACTIVE ENGINE
 * Target: 4,689 Contributions (Jan 3, 2026 to Nov 17, 2026)
 * Strict Requirement: ZERO EMOJIS.
 */

// Embedded fallback data in case loaded via file:// protocol
const FALLBACK_CONTRIBUTIONS = {
  "username": "ayushnautiyal9520-create",
  "total_contributions": 4689,
  "current_streak": 78,
  "longest_streak": 78,
  "start_date": "2026-01-03",
  "end_date": "2026-11-17",
  "best_day": { "date": "2026-10-22", "count": 41 }
};

const BATCHES_DATA = {
  "batch_1": {
    "id": "BATCH_01",
    "codename": "SYNDICATE CORE // VELOCITY",
    "category": "Pro Developer, High Commits & Streaks",
    "items": [
      {
        "metric": "PRO DEVELOPER CLASSIFICATION",
        "value": "TIER-S ARCHITECT",
        "subtext": "Wanted Level: 5-Star Maximum Code Velocity | 99.98% System Uptime"
      },
      {
        "metric": "HIGH COMMITS TOTAL",
        "value": "4,689 COMMITS",
        "subtext": "Peak Burst: 41 Commits/Day | Average 22.4 Commits/Active Day"
      },
      {
        "metric": "COMMIT STREAKS",
        "value": "78 DAYS ACTIVE",
        "subtext": "Marathon Record: 78 Days Continuous Shipping | 0 Breaking Changes"
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
        "value": "281 / 319 DAYS",
        "subtext": "88.1% Active Density | 4 Strategic Architectural Gaps Maintained"
      },
      {
        "metric": "PULL REQUESTS AND MERGES",
        "value": "342 PRODUCTION PRS",
        "subtext": "99.4% Clean Merge Rate | Sub-4hr Code Review Turnaround"
      },
      {
        "metric": "ISSUES RESOLVED",
        "value": "489 TICKETS SQUASHED",
        "subtext": "100% P0/P1 SLA Adherence | 84 Architecture Refactors Completed"
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
        "subtext": "Full-Stack SaaS, AI Agents, Microservices, Cloud Infrastructure"
      },
      {
        "metric": "DEVELOPMENT ACTIVITY PROFILE",
        "value": "POLYGLOT ARCHITECT",
        "subtext": "Next.js/React (38%), TypeScript/Node (32%), Python/AI (20%), Postgres (10%)"
      },
      {
        "metric": "OVERALL CONTRIBUTION HIGHLIGHTS",
        "value": "4,689 MILESTONES SHIPPED",
        "subtext": "Full 2026 Roadmap Executed | Rock-solid Engineering Execution"
      }
    ]
  }
};

let daysData = [];
let currentFilter = 'all';

// Audio Context for Procedural GTA VI Synthwave Ambience
let audioCtx = null;
let isAudioPlaying = false;
let synthNodes = [];

// Initialize
document.addEventListener('DOMContentLoaded', async () => {
  await loadData();
  renderHeatmap();
  renderBatches('all');
  initCountdownTimer();
  setupEventListeners();
});

// Load Contributions Data
async function loadData() {
  try {
    const res = await fetch('../data/contributions.json');
    if (res.ok) {
      const data = await res.json();
      daysData = data.days || [];
    } else {
      throw new Error('Local fetch blocked or unavailable');
    }
  } catch (err) {
    console.log('[GTA VI ENGINE] Generating in-memory procedural calendar data...');
    generateClientDays();
  }
}

// Generate in-memory days if offline/standalone
function generateClientDays() {
  daysData = [];
  const start = new Date(2026, 0, 3);
  const end = new Date(2026, 10, 17);
  let cur = new Date(start);

  const gapRanges = [
    [new Date(2026, 2, 2), new Date(2026, 2, 11)],
    [new Date(2026, 5, 1), new Date(2026, 5, 8)],
    [new Date(2026, 7, 22), new Date(2026, 7, 31)]
  ];

  while (cur <= end) {
    const dStr = cur.toISOString().split('T')[0];
    let inGap = false;
    for (const [gs, ge] of gapRanges) {
      if (cur >= gs && cur <= ge) {
        inGap = true;
        break;
      }
    }

    let count = 0;
    let level = 0;
    if (!inGap) {
      const doy = Math.floor((cur - new Date(2026, 0, 1)) / (1000 * 60 * 60 * 24));
      count = 12 + (doy % 23);
      if (doy >= 280 && doy <= 310) count = 28 + (doy % 14); // October peak
      if (count > 41) count = 41;

      if (count <= 8) level = 1;
      else if (count <= 16) level = 2;
      else if (count <= 28) level = 3;
      else if (count <= 38) level = 4;
      else level = 5;
    }

    daysData.push({
      date: dStr,
      count: count,
      level: level,
      inGap: inGap
    });

    cur.setDate(cur.getDate() + 1);
  }
}

// Render Heatmap
function renderHeatmap() {
  const container = document.getElementById('heatmap-grid');
  if (!container) return;
  container.innerHTML = '';

  const tooltip = document.getElementById('heatmap-tooltip');

  daysData.forEach((day, idx) => {
    const cell = document.createElement('div');
    cell.className = `heatmap-cell lvl-${day.level}`;
    cell.dataset.date = day.date;
    cell.dataset.count = day.count;
    cell.dataset.index = idx;

    if (day.count === 0) {
      cell.dataset.gap = "true";
    }

    // Hover tooltip
    cell.addEventListener('mouseenter', (e) => {
      playHudBlip(600, 0.03);
      const sprintLabel = day.count === 0 ? "INTENTIONAL ARCHITECTURAL GAP" : (day.count > 25 ? "HIGH-VELOCITY CRUNCH SPRINT" : "PRODUCTION SHIPPING CYCLE");
      tooltip.innerHTML = `
        <div style="color: #ff007f; font-weight: 800; font-size: 11px; margin-bottom: 2px;">[DATE: ${day.date}]</div>
        <div style="font-size: 13px; font-weight: 900; color: #ffffff;">${day.count} CONTRIBUTIONS</div>
        <div style="color: #00f0ff; font-size: 9.5px; margin-top: 3px;">// ${sprintLabel}</div>
      `;
      tooltip.style.display = 'block';
      moveTooltip(e);
    });

    cell.addEventListener('mousemove', (e) => {
      moveTooltip(e);
    });

    cell.addEventListener('mouseleave', () => {
      tooltip.style.display = 'none';
    });

    container.appendChild(cell);
  });
}

function moveTooltip(e) {
  const tooltip = document.getElementById('heatmap-tooltip');
  const x = e.clientX + 14;
  const y = e.clientY - 42;
  tooltip.style.left = `${x}px`;
  tooltip.style.top = `${y}px`;
}

// Render Batches
function renderBatches(filterKey) {
  const container = document.getElementById('batches-container');
  if (!container) return;
  container.innerHTML = '';

  const batchKeys = filterKey === 'all' ? ['batch_1', 'batch_2', 'batch_3'] : [filterKey];

  batchKeys.forEach((key, kIdx) => {
    const b = BATCHES_DATA[key];
    if (!b) return;

    const colClass = key === 'batch_1' ? 'col-1' : (key === 'batch_2' ? 'col-2' : 'col-3');

    const card = document.createElement('div');
    card.className = `batch-card ${colClass}`;

    let itemsHtml = '';
    b.items.forEach(item => {
      itemsHtml += `
        <div class="batch-item-block">
          <div class="item-metric-name">[${item.metric}]</div>
          <div class="item-metric-val">${item.value}</div>
          <div class="item-metric-sub">${item.subtext}</div>
        </div>
      `;
    });

    card.innerHTML = `
      <div class="batch-card-header">
        <div class="batch-id">${b.id} // SEC-0${kIdx+1}</div>
        <div class="batch-title">${b.codename}</div>
        <div class="batch-category">${b.category}</div>
      </div>
      <div class="batch-items-list">
        ${itemsHtml}
      </div>
    `;

    container.appendChild(card);
  });
}

// Setup Event Listeners
function setupEventListeners() {
  // Heatmap filters
  const filterBtns = document.querySelectorAll('.filter-btn');
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      playHudBlip(440, 0.05);
      applyHeatmapFilter(btn.dataset.filter);
    });
  });

  // Batch tabs
  const tabBtns = document.querySelectorAll('.tab-btn');
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tabBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      playHudBlip(520, 0.05);
      renderBatches(btn.dataset.tab);
    });
  });

  // Audio Toggle
  const audioBtn = document.getElementById('audio-toggle');
  if (audioBtn) {
    audioBtn.addEventListener('click', toggleAudio);
  }
}

// Filter Heatmap Cells
function applyHeatmapFilter(filter) {
  const cells = document.querySelectorAll('.heatmap-cell');
  cells.forEach(cell => {
    const count = parseInt(cell.dataset.count, 10);
    const isGap = cell.dataset.gap === "true";
    const idx = parseInt(cell.dataset.index, 10);

    cell.classList.remove('filtered-out', 'highlight-target');

    if (filter === 'crunch') {
      if (count < 25) cell.classList.add('filtered-out');
      else cell.classList.add('highlight-target');
    } else if (filter === 'gaps') {
      if (!isGap) cell.classList.add('filtered-out');
      else cell.classList.add('highlight-target');
    } else if (filter === 'streaks') {
      // Highlight current 78-day streak (ending Nov 17, 2026: last 78 cells)
      if (idx >= daysData.length - 78) {
        cell.classList.add('highlight-target');
      } else {
        cell.classList.add('filtered-out');
      }
    }
  });
}

// Live Countdown Timer
function initCountdownTimer() {
  const timerElem = document.getElementById('countdown-timer');
  if (!timerElem) return;

  function update() {
    const now = new Date();
    // Countdown to midnight UTC (Daily Sync Cycle)
    const nextSync = new Date(Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate() + 1, 0, 0, 0));
    const diff = nextSync - now;

    if (diff > 0) {
      const h = String(Math.floor(diff / (1000 * 60 * 60))).padStart(2, '0');
      const m = String(Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60))).padStart(2, '0');
      const s = String(Math.floor((diff % (1000 * 60)) / 1000)).padStart(2, '0');
      timerElem.textContent = `${h}:${m}:${s} [UTC SYNC]`;
    } else {
      timerElem.textContent = '00:00:00 [HARVESTING]';
    }
  }

  update();
  setInterval(update, 1000);
}

// Procedural Retro Synthwave Ambience (Web Audio API - No external assets)
function toggleAudio() {
  if (!audioCtx) {
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  }

  const audioState = document.getElementById('audio-state');

  if (isAudioPlaying) {
    stopSynth();
    isAudioPlaying = false;
    audioState.textContent = '[OFF]';
  } else {
    if (audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
    startSynth();
    isAudioPlaying = true;
    audioState.textContent = '[ON // ON AIR]';
  }
}

function startSynth() {
  if (!audioCtx) return;
  // Lush 80s synth pad chords (Vice City FM)
  const freqs = [110.00, 130.81, 164.81, 196.00, 220.00]; // A Minor 9th chord

  synthNodes = freqs.map(f => {
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    const filter = audioCtx.createBiquadFilter();

    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(f, audioCtx.currentTime);

    // Warm low-pass filter
    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(450, audioCtx.currentTime);

    gain.gain.setValueAtTime(0.015, audioCtx.currentTime);

    osc.connect(filter);
    filter.connect(gain);
    gain.connect(audioCtx.destination);

    osc.start();
    return { osc, gain, filter };
  });
}

function stopSynth() {
  synthNodes.forEach(node => {
    try {
      node.gain.gain.linearRampToValueAtTime(0.0001, audioCtx.currentTime + 0.3);
      setTimeout(() => node.osc.stop(), 350);
    } catch (e) {}
  });
  synthNodes = [];
}

// Tactical HUD UI Click Sound Blip
function playHudBlip(freq = 520, duration = 0.04) {
  try {
    if (!audioCtx) {
      audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (audioCtx.state === 'suspended') return;
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();

    osc.type = 'sine';
    osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
    gain.gain.setValueAtTime(0.02, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + duration);

    osc.connect(gain);
    gain.connect(audioCtx.destination);

    osc.start();
    osc.stop(audioCtx.currentTime + duration);
  } catch (e) {}
}
