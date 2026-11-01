#!/usr/bin/env python3
"""
Generate Vector Logo Assets for Vance AI SDR:
1. Option B: Dark Obsidian Minimal Vector (1024x1024 PNG + SVG)
2. Option C: Clean Light Silicon Valley Vector (1024x1024 PNG + SVG)
3. Horizontal Wordmark Logo for Website & Headers (2048x600 PNG + SVG)
"""

import subprocess
from pathlib import Path

CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUTPUT_DIR = Path("/Users/mangal777/Mangal/growth_engine/branding")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 1. Dark Obsidian Minimal Vector Avatar
SVG_DARK = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <radialGradient id="bgGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#020617"/>
    </radialGradient>
    <linearGradient id="vGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#94a3b8"/>
    </linearGradient>
    <filter id="neonGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="16" result="blur1"/>
      <feGaussianBlur stdDeviation="32" result="blur2"/>
      <feMerge>
        <feMergeNode in="blur2"/>
        <feMergeNode in="blur1"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1024" height="1024" fill="url(#bgGlow)"/>

  <!-- Subtle Circular Ring (Radar) -->
  <circle cx="512" cy="512" r="380" fill="none" stroke="rgba(255,255,255,0.04)" stroke-width="2"/>
  <circle cx="512" cy="512" r="240" fill="none" stroke="rgba(16,185,129,0.08)" stroke-width="2"/>

  <!-- Geometric V -->
  <!-- Left Wing -->
  <path d="M 280 260 L 410 260 L 512 660 L 440 660 Z" fill="url(#vGrad)"/>
  <!-- Right Wing -->
  <path d="M 744 260 L 614 260 L 512 660 L 584 660 Z" fill="url(#vGrad)"/>

  <!-- Vertex Chevron Cap -->
  <polygon points="512,740 440,640 584,640" fill="#0f172a"/>

  <!-- Glowing Intent Beacon at Vertex -->
  <circle cx="512" cy="620" r="44" fill="#10b981" filter="url(#neonGlow)"/>
  <circle cx="512" cy="620" r="20" fill="#ffffff"/>
</svg>"""

# 2. Clean Light Silicon Valley Vector Avatar
SVG_LIGHT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <linearGradient id="vGradLight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <filter id="lightGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="12" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1024" height="1024" fill="#ffffff"/>
  <rect x="32" y="32" width="960" height="960" rx="220" fill="#fafaf9" stroke="#e2e8f0" stroke-width="8"/>

  <!-- Geometric V -->
  <path d="M 280 270 L 410 270 L 512 670 L 440 670 Z" fill="url(#vGradLight)"/>
  <path d="M 744 270 L 614 270 L 512 670 L 584 670 Z" fill="url(#vGradLight)"/>

  <!-- Glowing Emerald Intent Node -->
  <circle cx="512" cy="630" r="46" fill="#10b981" filter="url(#lightGlow)"/>
  <circle cx="512" cy="630" r="22" fill="#ffffff"/>
</svg>"""

# 3. Horizontal Wordmark Logo (V + VANCE + AI SDR)
HTML_WORDMARK = """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@800;900&family=JetBrains+Mono:wght@700;800&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      width: 1400px;
      height: 400px;
      background: #090d16;
      display: flex;
      align-items: center;
      padding: 0 80px;
      font-family: 'Plus Jakarta Sans', sans-serif;
    }
    .logo-container {
      display: flex;
      align-items: center;
      gap: 48px;
    }
    .icon-box {
      width: 180px;
      height: 180px;
    }
    .text-box {
      display: flex;
      flex-direction: column;
    }
    .brand-title {
      font-size: 110px;
      font-weight: 900;
      letter-spacing: -0.04em;
      color: #ffffff;
      line-height: 1;
    }
    .brand-sub {
      font-family: 'JetBrains Mono', monospace;
      font-size: 26px;
      font-weight: 800;
      color: #10b981;
      letter-spacing: 0.25em;
      text-transform: uppercase;
      margin-top: 14px;
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .beacon {
      width: 12px;
      height: 12px;
      background: #10b981;
      border-radius: 50%;
      box-shadow: 0 0 12px #10b981;
    }
  </style>
</head>
<body>
  <div class="logo-container">
    <svg class="icon-box" viewBox="0 0 1024 1024">
      <defs>
        <linearGradient id="vGradW" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#ffffff"/>
          <stop offset="100%" stop-color="#94a3b8"/>
        </linearGradient>
        <filter id="neonGlowW">
          <feGaussianBlur stdDeviation="20" result="blur"/>
          <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
          </feMerge>
        </filter>
      </defs>
      <path d="M 240 220 L 400 220 L 512 680 L 420 680 Z" fill="url(#vGradW)"/>
      <path d="M 784 220 L 624 220 L 512 680 L 604 680 Z" fill="url(#vGradW)"/>
      <circle cx="512" cy="630" r="50" fill="#10b981" filter="url(#neonGlowW)"/>
      <circle cx="512" cy="630" r="22" fill="#ffffff"/>
    </svg>
    <div class="text-box">
      <div class="brand-title">Vance</div>
      <div class="brand-sub"><div class="beacon"></div>Autonomous B2B SDR • usevance.com</div>
    </div>
  </div>
</body>
</html>"""

def render_assets():
    print("🎨 Generating Vector Logo Assets...")
    
    # 1. Dark Vector
    dark_svg_path = OUTPUT_DIR / "vance_avatar_dark.svg"
    dark_png_path = OUTPUT_DIR / "vance_avatar_dark.png"
    dark_svg_path.write_text(SVG_DARK, encoding="utf-8")
    subprocess.run([
        CHROME_BIN, "--headless=new", "--disable-gpu",
        "--window-size=1024,1024",
        f"--screenshot={dark_png_path}",
        f"file://{dark_svg_path.resolve()}"
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"  ✓ Dark Avatar PNG: {dark_png_path.name}")

    # 2. Light Vector
    light_svg_path = OUTPUT_DIR / "vance_avatar_light.svg"
    light_png_path = OUTPUT_DIR / "vance_avatar_light.png"
    light_svg_path.write_text(SVG_LIGHT, encoding="utf-8")
    subprocess.run([
        CHROME_BIN, "--headless=new", "--disable-gpu",
        "--window-size=1024,1024",
        f"--screenshot={light_png_path}",
        f"file://{light_svg_path.resolve()}"
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"  ✓ Light Avatar PNG: {light_png_path.name}")

    # 3. Horizontal Wordmark
    wordmark_html_path = OUTPUT_DIR / "vance_wordmark.html"
    wordmark_png_path = OUTPUT_DIR / "vance_wordmark.png"
    wordmark_html_path.write_text(HTML_WORDMARK, encoding="utf-8")
    subprocess.run([
        CHROME_BIN, "--headless=new", "--disable-gpu",
        "--window-size=1400,400",
        f"--screenshot={wordmark_png_path}",
        f"file://{wordmark_html_path.resolve()}"
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"  ✓ Horizontal Wordmark PNG: {wordmark_png_path.name}")

if __name__ == "__main__":
    render_assets()
