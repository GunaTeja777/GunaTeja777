import urllib.request
import json

def app(environ, start_response):
    views = 0
    try:
        # Fetch count and increment it (hit endpoint) with timeout
        url = "https://countapi.mileshilliard.com/api/v1/hit/GunaTeja777_readme"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            views = data.get("value", 0) + 2579
    except Exception as e:
        views = 2579  # fallback

    svg_template = f"""<svg xmlns="http://www.w3.org/2000/svg" width="195" height="195" viewBox="0 0 195 195">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@700&amp;family=Orbitron:wght@700&amp;family=Share+Tech+Mono&amp;display=swap');
      .box-bg {{
        fill: url(#boxGradient);
        stroke: #93C5FD;
        stroke-opacity: 0.35;
        stroke-width: 1px;
        rx: 6px;
      }}
      .title-text {{
        font-family: 'Orbitron', sans-serif;
        font-size: 10px;
        font-weight: 700;
        fill: #E0F2FE;
        letter-spacing: 0.12em;
      }}
      .subtitle-text {{
        font-family: 'Share Tech Mono', monospace;
        font-size: 8px;
        fill: #BFDBFE;
      }}
      .divider {{
        stroke: #E0F2FE;
        stroke-opacity: 0.25;
        stroke-width: 1px;
      }}
      .giant-number {{
        font-family: 'Chakra Petch', sans-serif;
        font-size: 54px;
        font-weight: 700;
        fill: #FFFFFF;
        filter: url(#softGlow);
      }}
      .status-text {{
        font-family: 'Share Tech Mono', monospace;
        font-size: 8px;
        fill: #E0F2FE;
      }}
      @keyframes blink {{
        0%, 100% {{ opacity: 0.3; }}
        50% {{ opacity: 1; }}
      }}
      @keyframes pulseGlow {{
        0%, 100% {{ opacity: 0.6; }}
        50% {{ opacity: 1; }}
      }}
      @keyframes scan {{
        0% {{ transform: translateY(-195px); }}
        100% {{ transform: translateY(195px); }}
      }}
      .blinker {{
        animation: blink 2s infinite;
        fill: #A7F3D0;
      }}
      .pulse-ring {{
        animation: pulseGlow 3s infinite;
      }}
      .scan-line {{
        animation: scan 4s linear infinite;
      }}
    </style>

    <linearGradient id="boxGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1D4ED8" />
      <stop offset="55%" stop-color="#2563EB" />
      <stop offset="100%" stop-color="#1E3A8A" />
    </linearGradient>

    <radialGradient id="cornerGlow" cx="100%" cy="0%" r="80%">
      <stop offset="0%" stop-color="#BFDBFE" stop-opacity="0.25" />
      <stop offset="100%" stop-color="#BFDBFE" stop-opacity="0" />
    </radialGradient>

    <filter id="softGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="1.6" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <clipPath id="clipBox">
      <rect x="0.5" y="0.5" width="194" height="194" rx="6" />
    </clipPath>
  </defs>

  <!-- Background Card: full blue box -->
  <rect x="0.5" y="0.5" width="194" height="194" class="box-bg" />
  <rect x="0.5" y="0.5" width="194" height="194" fill="url(#cornerGlow)" rx="6" />

  <!-- Animated scan line, clipped inside the box -->
  <g clip-path="url(#clipBox)">
    <rect x="0" y="0" width="195" height="40" fill="#FFFFFF" opacity="0.05" class="scan-line" />
  </g>

  <!-- Header -->
  <text x="97.5" y="24" text-anchor="middle" class="title-text">VISITORS</text>
  <line x1="15" y1="33" x2="180" y2="33" class="divider" />

  <!-- Value -->
  <text x="97.5" y="110" text-anchor="middle" class="giant-number">{views}</text>

  <!-- Footer Divider -->
  <line x1="15" y1="150" x2="180" y2="150" class="divider" />

  <!-- Footer Status -->
  <g transform="translate(15, 172)">
    <circle cx="4" cy="-3" r="4" fill="#A7F3D0" opacity="0.25" class="pulse-ring" />
    <circle cx="4" cy="-3" r="3" class="blinker" />
    <text x="12" y="0" class="status-text">STATUS: ACTIVE</text>
    <text x="165" y="0" text-anchor="end" class="subtitle-text">BONE</text>
  </g>
</svg>
"""
    status = '200 OK'
    headers = [
        ('Content-type', 'image/svg+xml'),
        ('Cache-Control', 'no-cache, no-store, must-revalidate'),
        ('Pragma', 'no-cache'),
        ('Expires', '0')
    ]
    start_response(status, headers)
    return [svg_template.encode('utf-8')]
