import urllib.request
import json
import datetime

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

# 2. Define the Square SVG template
svg_template = f"""<svg xmlns="http://www.w3.org/2000/svg" width="195" height="195" viewBox="0 0 195 195">
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
        font-size: 9px;
        font-weight: 700;
        fill: #C2BEB0;
        letter-spacing: 0.12em;
      }}
      .subtitle-text {{
        font-family: 'Share Tech Mono', monospace;
        font-size: 8px;
        fill: #928D7C;
      }}
      .divider {{
        stroke: #C2BEB0;
        stroke-opacity: 0.1;
        stroke-width: 1px;
      }}
      .giant-number {{
        font-family: 'Chakra Petch', sans-serif;
        font-size: 54px;
        font-weight: 700;
        fill: #E0DCC8;
      }}
      .giant-label {{
        font-family: 'Orbitron', sans-serif;
        font-size: 8px;
        fill: #928D7C;
        letter-spacing: 0.1em;
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
  <rect x="0.5" y="0.5" width="194" height="194" class="box-bg" />

  <!-- Top Header -->
  <text x="97.5" y="24" text-anchor="middle" class="title-text">GUNATEJA777</text>
  <line x1="15" y1="33" x2="180" y2="33" class="divider" />

  <!-- Main Views Column -->
  <g transform="translate(97.5, 52)">
    <!-- Views Count -->
    <text x="0" y="48" text-anchor="middle" class="giant-number">{views}</text>
    <text x="0" y="68" text-anchor="middle" class="giant-label">PROFILE VISITORS</text>
  </g>

  <!-- Bottom Divider -->
  <line x1="15" y1="150" x2="180" y2="150" class="divider" />

  <!-- Bottom Status Info -->
  <g transform="translate(15, 172)">
    <circle cx="4" cy="-3" r="3" class="blinker" />
    <text x="12" y="0" class="status-text">STATUS: ACTIVE</text>
    <text x="165" y="0" text-anchor="end" class="subtitle-text">BONE</text>
  </g>
</svg>
"""

# 3. Save SVG to file
with open("profile-visitors.svg", "w", encoding="utf-8") as f:
    f.write(svg_template)

print("Successfully generated square hyperweave visitor card profile-visitors.svg")
