import urllib.request
import json

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

# 2. Define the Compact Square (Cube) SVG template
svg_template = f"""<svg xmlns="http://www.w3.org/2000/svg" width="110" height="110" viewBox="0 0 110 110">
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
        font-size: 8px;
        font-weight: 700;
        fill: #C2BEB0;
        letter-spacing: 0.1em;
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
      .status-text {{
        font-family: 'Share Tech Mono', monospace;
        font-size: 7px;
        fill: #928D7C;
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
  <rect x="0.5" y="0.5" width="109" height="109" class="box-bg" />

  <!-- Header -->
  <text x="55" y="22" text-anchor="middle" class="title-text">VISITORS</text>
  <line x1="15" y1="30" x2="95" y2="30" class="divider" />

  <!-- Value -->
  <text x="55" y="70" text-anchor="middle" class="giant-number">{views}</text>

  <!-- Footer Divider -->
  <line x1="15" y1="86" x2="95" y2="86" class="divider" />

  <!-- Footer Status -->
  <g transform="translate(15, 98)">
    <circle cx="4" cy="-2.5" r="2" class="blinker" />
    <text x="12" y="0" class="status-text">STATUS: ACTIVE</text>
  </g>
</svg>
"""

# 3. Save SVG to file
with open("profile-visitors.svg", "w", encoding="utf-8") as f:
    f.write(svg_template)

print("Successfully generated compact cube visitor card profile-visitors.svg")
