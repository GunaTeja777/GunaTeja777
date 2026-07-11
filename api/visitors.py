from http.server import BaseHTTPRequestHandler
import urllib.request
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        views = 0
        try:
            # Fetch count and increment it (hit endpoint)
            url = "https://countapi.mileshilliard.com/api/v1/hit/GunaTeja777_readme"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                views = data.get("value", 0) + 2579
        except Exception as e:
            views = 2579  # fallback

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
        font-size: 10px;
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

  <!-- Header -->
  <text x="97.5" y="24" text-anchor="middle" class="title-text">VISITORS</text>
  <line x1="15" y1="33" x2="180" y2="33" class="divider" />

  <!-- Value -->
  <text x="97.5" y="110" text-anchor="middle" class="giant-number">{views}</text>

  <!-- Footer Divider -->
  <line x1="15" y1="150" x2="180" y2="150" class="divider" />

  <!-- Footer Status -->
  <g transform="translate(15, 172)">
    <circle cx="4" cy="-3" r="3" class="blinker" />
    <text x="12" y="0" class="status-text">STATUS: ACTIVE</text>
    <text x="165" y="0" text-anchor="end" class="subtitle-text">BONE</text>
  </g>
</svg>
"""
        
        self.send_response(200)
        self.send_header('Content-type', 'image/svg+xml')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.end_headers()
        self.wfile.write(svg_template.encode('utf-8'))
        return
