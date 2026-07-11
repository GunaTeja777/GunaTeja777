import urllib.request
import json
import datetime
import random

# Default fallback values
followers = 40
following = 15
repos = 29
created_year = "2023"
views = 0

try:
    # 1. Fetch current view count
    url = "https://countapi.mileshilliard.com/api/v1/get/GunaTeja777_readme"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        views = data.get("value", 0)
    print(f"Current views: {views}")
except Exception as e:
    print(f"Error fetching views: {e}")

try:
    # 2. Fetch GitHub Profile details
    gh_url = "https://api.github.com/users/GunaTeja777"
    gh_req = urllib.request.Request(gh_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(gh_req) as response:
        gh_data = json.loads(response.read().decode())
        followers = gh_data.get("followers", followers)
        following = gh_data.get("following", following)
        repos = gh_data.get("public_repos", repos)
        created_at = gh_data.get("created_at", "")
        if created_at:
            created_year = created_at[:4]
    print(f"GitHub stats fetched successfully. Followers: {followers}, Following: {following}, Repos: {repos}, Since: {created_year}")
except Exception as e:
    print(f"Error fetching GitHub stats (using fallbacks): {e}")

# 3. Generate Grid Squares (Deterministic cellular automata heat map based on views)
grid_squares = []
colors = ["#1A1814", "#2A2722", "#5A5648", "#928D7C", "#C2BEB0", "#E0DCC8"]

# Use the current views to seed the random number generator so the pattern evolves as views increase
random.seed(views)

for col in range(22):
    for row in range(4):
        # We want newer/rightmost columns to have higher chance of brighter colors, representing active traffic
        # Shift probability weights based on column index
        if col < 8:
            weights = [0.45, 0.35, 0.15, 0.04, 0.01, 0.00]
        elif col < 15:
            weights = [0.25, 0.35, 0.25, 0.10, 0.04, 0.01]
        else:
            weights = [0.10, 0.20, 0.30, 0.25, 0.10, 0.05]
            
        color = random.choices(colors, weights=weights)[0]
        x_pos = col * 10
        y_pos = row * 10
        grid_squares.append(f'<rect x="{x_pos}" y="{y_pos}" width="8" height="8" fill="{color}" rx="1" />')

grid_squares_xml = "\n    ".join(grid_squares)

# 4. Generate the last updated timestamp
now_utc = datetime.datetime.utcnow().strftime("%d %b %H:%M UTC")

# 5. Define the SVG template
svg_template = f"""<svg xmlns="http://www.w3.org/2000/svg" width="350" height="195" viewBox="0 0 350 195">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@700&amp;family=Orbitron:wght@700&amp;family=Share+Tech+Mono&amp;display=swap');
      .box-bg {{
        fill: #04060A;
        stroke: #C2BEB0;
        stroke-opacity: 0.15;
        stroke-width: 1px;
        rx: 6px;
      }}
      .title-text {{
        font-family: 'Orbitron', sans-serif;
        font-size: 10px;
        font-weight: 700;
        fill: #C2BEB0;
        letter-spacing: 0.15em;
      }}
      .subtitle-text {{
        font-family: 'Share Tech Mono', monospace;
        font-size: 9px;
        fill: #928D7C;
      }}
      .divider {{
        stroke: #C2BEB0;
        stroke-opacity: 0.1;
        stroke-width: 1px;
      }}
      .giant-number {{
        font-family: 'Chakra Petch', sans-serif;
        font-size: 32px;
        font-weight: 700;
        fill: #E0DCC8;
      }}
      .giant-label {{
        font-family: 'Orbitron', sans-serif;
        font-size: 7px;
        fill: #928D7C;
        letter-spacing: 0.1em;
      }}
      .stat-val {{
        font-family: 'Chakra Petch', sans-serif;
        font-size: 15px;
        font-weight: 700;
        fill: #E0DCC8;
      }}
      .stat-lbl {{
        font-family: 'Orbitron', sans-serif;
        font-size: 7px;
        fill: #928D7C;
        letter-spacing: 0.05em;
      }}
      .status-text {{
        font-family: 'Share Tech Mono', monospace;
        font-size: 8px;
        fill: #C2BEB0;
      }}
      @keyframes blink {{
        0%, 100% {{ opacity: 0.3; }}
        50% {{ opacity: 1; }}
      }}
      .blinker {{
        animation: blink 2s infinite;
        fill: #34D399;
      }}
    </style>
  </defs>

  <!-- Background Card -->
  <rect x="0.5" y="0.5" width="349" height="194" class="box-bg" />

  <!-- Top Header -->
  <text x="15" y="22" class="title-text">GUNATEJA777 / TRAFFIC</text>
  <text x="335" y="22" text-anchor="end" class="subtitle-text">Views - HiloO</text>
  <line x1="15" y1="30" x2="335" y2="30" class="divider" />

  <!-- Main Views Column -->
  <g transform="translate(15, 45)">
    <!-- Views Count -->
    <text x="0" y="32" class="giant-number">{views}</text>
    <text x="0" y="44" class="giant-label">TOTAL PROFILE VIEWS</text>
  </g>

  <!-- Divider between views and stats -->
  <line x1="155" y1="45" x2="155" y2="105" class="divider" />

  <!-- Secondary Stats Column -->
  <g transform="translate(170, 45)">
    <!-- Followers -->
    <g transform="translate(0, 0)">
      <text x="0" y="15" class="stat-val">{followers}</text>
      <text x="0" y="25" class="stat-lbl">FOLLOWERS</text>
    </g>
    <!-- Following -->
    <g transform="translate(75, 0)">
      <text x="0" y="15" class="stat-val">{following}</text>
      <text x="0" y="25" class="stat-lbl">FOLLOWING</text>
    </g>
    <!-- Repos -->
    <g transform="translate(0, 38)">
      <text x="0" y="15" class="stat-val">{repos}</text>
      <text x="0" y="25" class="stat-lbl">PUBLIC REPOS</text>
    </g>
    <!-- Created -->
    <g transform="translate(75, 38)">
      <text x="0" y="15" class="stat-val">{created_year}</text>
      <text x="0" y="25" class="stat-lbl">SINCE</text>
    </g>
  </g>

  <!-- Bottom Divider -->
  <line x1="15" y1="120" x2="335" y2="120" class="divider" />

  <!-- Bottom Grid Section (Representing Traffic History/Automata) -->
  <g transform="translate(15, 130)">
    {grid_squares_xml}
  </g>

  <!-- Automata Legend / Tech details -->
  <g transform="translate(245, 130)">
    <text x="0" y="8" class="stat-lbl" font-size="6px">GENOME: AUTOMATA</text>
    <text x="0" y="18" class="stat-lbl" font-size="6px">PALETTE: BONE</text>
    <text x="0" y="28" class="stat-lbl" font-size="6px">REGIME: NORMAL</text>
    <text x="0" y="38" class="stat-lbl" font-size="6px">ENGINE: HW-V0.4</text>
  </g>

  <!-- Bottom Status Info -->
  <g transform="translate(15, 182)">
    <circle cx="4" cy="-3" r="3" class="blinker" />
    <text x="12" y="0" class="status-text">STATUS: ACTIVE · LAST UPDATED: {now_utc}</text>
  </g>
</svg>
"""

# 6. Save SVG to file
with open("profile-visitors.svg", "w", encoding="utf-8") as f:
    f.write(svg_template)

print("Successfully generated big hyperweave visitor card profile-visitors.svg")
