#!/usr/bin/env python3
"""
🎨 Programmatic High-Ticket B2B Carousel Generator — Vance AI SDR Post #2
Theme: The $5,700/mo Human SDR Unit Economics Breakdown (Why Autonomous SDRs Win in 2026)
Generates:
1. 1080x1350 High-Res Dark PNG Slides (Obsidian Dark Mode + Neon Emerald & Cyan)
2. Interactive Swipeable PDF Document (for LinkedIn)
3. Direct Push to Telegram: 5 PNG Album + 1-Tap Copy-Paste Caption
"""

import os
import sys
import json
import subprocess
import urllib.request
from pathlib import Path
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import env_loader

CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUTPUT_DIR = Path("/Users/mangal777/Mangal/growth_engine/carousels/vance_economics_deck")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8445264349:AAFWHjaQe9Qomf2Zwm7MVV_6NkhRmGWLMjs")
TELEGRAM_CHAT_ID = os.getenv("VANCE_TELEGRAM_CHAT_ID", "-1003882353811")

CAROUSEL_CAPTION = """Why hiring a $5,700/mo human SDR is financial suicide for B2B startups in 2026: 📉

Most B2B founders calculate an SDR hire as just "$4,500/mo base".

Here is the real P&L reality they discover 90 days later:
❌ $4,500/mo Base Salary
❌ $1,200/mo Tech Stack Tax (Apollo + ZoomInfo + Salesloft + LinkedIn Sales Nav)
❌ 90 Days Ramp Time ($17,100 burned before seeing deal #1)
❌ 60 manual emails/day with a 0.8% reply rate
❌ Burnt primary company domain in month 2 from template spam penalties

The outcome? $2,850 cost per qualified meeting booked.

Instead of burning headcount, @usevance.ai deploys an Autonomous Intent Outbound SDR on a $1,500/mo flat retainer:

⚡ 24/7 Live Intent Radar: Audits commercial buying triggers (Hiring surges, tech stack churn, funding rounds, reverse-IP pricing page hits).
⚡ 15-Minute Cadence Engine: Reaches out while the prospect is actively evaluating solutions.
⚡ Secondary Domain Fleet: 3 isolated domains + automated warmup with <2% bounce target. 0% primary domain burn risk.
⚡ Hard Economics: $160 cost per qualified meeting. 94.3% cost reduction.

👉 Want to see who is actively showing intent in your market right now?
Comment "AUDIT" below or DM us @usevance.ai:
Our engine will run a free intent scan on your ICP and send you 20 verified high-intent leads straight to your inbox.

🔗 Test the live sandbox: usevance.com (link in bio)

Built with conviction by @mangal777

#b2bsaas #aisdr #growtharchitecture #coldoutreach #gtmstrategy #uniteconomics #usevance #salesdevelopment
"""

SLIDES = [
    # SLIDE 1: CONTRARIAN HOOK
    {
        "num": 1,
        "badge": "B2B UNIT ECONOMICS AUDIT",
        "badge_color": "rose",
        "headline": "Why Paying $5,700/mo For a Human SDR Is <span>Financial Suicide</span> in 2026.",
        "content_type": "slide_1_hook",
        "footer": "Swipe to see the P&L math ➔"
    },
    # SLIDE 2: THE BRUTAL P&L REALITY
    {
        "num": 2,
        "badge": "THE HIDDEN BALANCE SHEET TAX",
        "badge_color": "rose",
        "headline": "The Real 90-Day P&L of <span>1 Human SDR</span>",
        "content_type": "slide_2_pain",
        "footer": "The autonomous architecture ➔"
    },
    # SLIDE 3: THE VANCE 4-LAYER SYSTEM
    {
        "num": 3,
        "badge": "THE NEW INFRASTRUCTURE",
        "badge_color": "emerald",
        "headline": "How Vance Replaces $5,700/mo Burn for <span>$1,500/mo</span>",
        "content_type": "slide_3_system",
        "footer": "Side-by-side benchmark comparison ➔"
    },
    # SLIDE 4: THE 90-DAY HARD BENCHMARK
    {
        "num": 4,
        "badge": "HARD METRIC BENCHMARK",
        "badge_color": "cyan",
        "headline": "Human SDR vs Vance AI SDR <span>(90-Day P&L Comparison)</span>",
        "content_type": "slide_4_benchmark",
        "footer": "Claim your 20 free leads ➔"
    },
    # SLIDE 5: LOW-FRICTION OFFER & CTA
    {
        "num": 5,
        "badge": "FREE ICP INTENT SCAN",
        "badge_color": "emerald",
        "headline": "Stop Burning Cash on <span>Manual Template Blasts</span>",
        "content_type": "slide_5_cta",
        "footer": "Save this post for your 2026 outbound strategy"
    }
]

def generate_html_slide(slide):
    badge_colors = {
        "emerald": ("rgba(16, 229, 138, 0.12)", "#10E58A", "#10E58A", "rgba(16, 229, 138, 0.35)"),
        "rose": ("rgba(255, 51, 75, 0.12)", "#FF334B", "#FF334B", "rgba(255, 51, 75, 0.35)"),
        "cyan": ("rgba(56, 189, 248, 0.12)", "#38bdf8", "#38bdf8", "rgba(56, 189, 248, 0.35)")
    }
    bg_pill, text_pill, dot_color, border_pill = badge_colors.get(slide.get("badge_color", "emerald"))

    c_type = slide.get("content_type")
    content_html = ""

    if c_type == "slide_1_hook":
        content_html = """
        <div class="hook-box">
            <p class="hook-desc">
                Most founders think hiring an SDR costs <b>$4,500/mo</b>.<br><br>
                They don't account for the <b>$1,200 tech stack tax</b>, the <b>90-day onboarding lag</b>, or the <b>burnt company domain</b> from spray-and-pray blast volume.
            </p>
            <div class="vs-strip">
                <div class="vs-col bad">
                    <span class="vs-label">HUMAN SDR</span>
                    <span class="vs-num red">$5,700/mo</span>
                    <span class="vs-sub">0.8% Reply • 90d Ramp</span>
                </div>
                <div class="vs-divider">VS</div>
                <div class="vs-col good">
                    <span class="vs-label">VANCE INTENT SDR</span>
                    <span class="vs-num emerald">$1,500/mo</span>
                    <span class="vs-sub">15m Cadence • Intent Radar</span>
                </div>
            </div>
        </div>
        """
    elif c_type == "slide_2_pain":
        content_html = """
        <div class="cards-grid">
            <div class="cost-card">
                <div class="cost-num-row">
                    <span class="cost-badge">COST 01</span>
                    <span class="cost-val red">$4,500/mo</span>
                </div>
                <div class="cost-title">Base Salary + OTE Drag</div>
                <div class="cost-desc">For an average output of 60 manual copy-pasted emails a day with low conversion.</div>
            </div>
            <div class="cost-card">
                <div class="cost-num-row">
                    <span class="cost-badge">COST 02</span>
                    <span class="cost-val red">$1,200/mo</span>
                </div>
                <div class="cost-title">The Required Tech Stack Tax</div>
                <div class="cost-desc">Apollo ($149) + ZoomInfo ($750) + Salesloft ($125) + LinkedIn Sales Navigator ($80).</div>
            </div>
            <div class="cost-card">
                <div class="cost-num-row">
                    <span class="cost-badge">COST 03</span>
                    <span class="cost-val red">90 Days</span>
                </div>
                <div class="cost-title">Ramp & Onboarding Waste</div>
                <div class="cost-desc">$17,100 burned in salary & software before seeing the first closed-won deal.</div>
            </div>
            <div class="cost-card">
                <div class="cost-num-row">
                    <span class="cost-badge">COST 04</span>
                    <span class="cost-val red">92% Burn</span>
                </div>
                <div class="cost-title">Primary Domain Spam Penalty</div>
                <div class="cost-desc">Blasting cold templates from company.com destroys corporate email deliverability forever.</div>
            </div>
        </div>
        """
    elif c_type == "slide_3_system":
        content_html = """
        <div class="arch-container">
            <div class="arch-card">
                <div class="arch-icon">🎯</div>
                <div class="arch-info">
                    <div class="arch-title">Layer 1: 24/7 Live Intent Radar</div>
                    <div class="arch-desc">Audits commercial buying triggers: hiring surges, tech stack churn, funding rounds, and pricing page reverse-IP tracking.</div>
                </div>
            </div>
            <div class="arch-card">
                <div class="arch-icon">⚡</div>
                <div class="arch-info">
                    <div class="arch-title">Layer 2: 15-Minute Cadence Engine</div>
                    <div class="arch-desc">Eliminates lead decay. Dispatches a bespoke 40-word problem-solver pitch while the buyer is still at their desk.</div>
                </div>
            </div>
            <div class="arch-card">
                <div class="arch-icon">🛡️</div>
                <div class="arch-info">
                    <div class="arch-title">Layer 3: Secondary Domain Fleet</div>
                    <div class="arch-desc">3 isolated secondary domains + automated warmups with &lt; 2% bounce cap. 0% company domain risk.</div>
                </div>
            </div>
            <div class="arch-card">
                <div class="arch-icon">💼</div>
                <div class="arch-info">
                    <div class="arch-title">Layer 4: Autonomous SDR Retainer</div>
                    <div class="arch-desc">$1,500/mo flat retainer for B2B SaaS & Dev Agencies. Zero hiring fees, zero onboarding headaches.</div>
                </div>
            </div>
        </div>
        """
    elif c_type == "slide_4_benchmark":
        content_html = """
        <div class="table-card">
            <div class="t-row t-head">
                <span class="t-cell metric">METRIC</span>
                <span class="t-cell human">HUMAN SDR</span>
                <span class="t-cell vance">VANCE AI SDR</span>
            </div>
            <div class="t-row">
                <span class="t-cell metric">90-Day All-in Cost</span>
                <span class="t-cell human red">$17,100</span>
                <span class="t-cell vance emerald">$4,500 (-73.6%)</span>
            </div>
            <div class="t-row">
                <span class="t-cell metric">Qualified Meetings</span>
                <span class="t-cell human">6 meetings</span>
                <span class="t-cell vance emerald">28 meetings (+366%)</span>
            </div>
            <div class="t-row">
                <span class="t-cell metric">Cost Per Meeting</span>
                <span class="t-cell human red">$2,850</span>
                <span class="t-cell vance emerald">$160 (94.3% savings)</span>
            </div>
            <div class="t-row">
                <span class="t-cell metric">Lead Decay Window</span>
                <span class="t-cell human">4 Days (Cold)</span>
                <span class="t-cell vance emerald">15 Minutes (Live)</span>
            </div>
            <div class="t-row">
                <span class="t-cell metric">Deliverability Target</span>
                <span class="t-cell human red">&lt; 68% (Spam trap)</span>
                <span class="t-cell vance emerald">&lt; 2% Bounce Cap</span>
            </div>
        </div>
        """
    elif c_type == "slide_5_cta":
        content_html = """
        <div class="cta-wrap">
            <div class="cta-inner">
                <p class="cta-main-text">
                    We deploy and manage the full <b>Autonomous Intent SDR Retainer</b> for B2B SaaS and Tech Dev Agencies.
                </p>
                <div class="cta-offer-box">
                    <div class="offer-header">🎁 COMPLIMENTARY INTENT SCAN</div>
                    <div class="offer-sub">Comment <b>"AUDIT"</b> below or DM <b>@usevance.ai</b>:</div>
                    <p class="offer-desc">We will audit your outbound domain deliverability and deliver <b>20 verified high-intent ICP leads</b> straight to your inbox.</p>
                </div>
                <div class="cta-domain-button">
                    <span>EXPLORE SANDBOX ➔ USEVANCE.COM</span>
                </div>
                <div class="cta-brand-footer">
                    <span>⚡ Vance AI • Autonomous B2B Intent SDR • by Mangal Soren</span>
                </div>
            </div>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Vance Slide {slide['num']}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800;900&family=Space+Grotesk:wght@600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-obsidian: #06080d;
            --card-bg: #0c1017;
            --emerald-glow: #10E58A;
            --red-alert: #FF334B;
            --cyan-accent: #38bdf8;
            --text-muted: #94a3b8;
            --font-head: 'Space Grotesk', sans-serif;
            --font-ui: 'Plus Jakarta Sans', sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            width: 1080px;
            height: 1350px;
            overflow: hidden;
            background: var(--bg-obsidian);
            font-family: var(--font-ui);
            color: #ffffff;
            position: relative;
        }}
        .ambient-glow-top {{
            position: absolute;
            top: -150px;
            left: 50%;
            transform: translateX(-50%);
            width: 900px;
            height: 500px;
            background: radial-gradient(circle, rgba(16, 229, 138, 0.14) 0%, transparent 70%);
            pointer-events: none;
            z-index: 1;
        }}
        .canvas {{
            position: relative;
            z-index: 10;
            width: 1080px;
            height: 1350px;
            padding: 70px 75px 65px 75px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        .header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .brand-badge {{
            display: flex;
            align-items: center;
            gap: 12px;
            background: rgba(15, 23, 42, 0.85);
            border: 1.5px solid rgba(16, 229, 138, 0.35);
            padding: 10px 24px;
            border-radius: 999px;
        }}
        .brand-name {{
            font-family: var(--font-head);
            font-size: 20px;
            font-weight: 800;
            letter-spacing: -0.02em;
        }}
        .brand-name span {{ color: var(--emerald-glow); }}
        .slide-counter {{
            font-family: var(--font-mono);
            font-size: 17px;
            font-weight: 700;
            color: var(--emerald-glow);
            background: rgba(16, 229, 138, 0.1);
            padding: 8px 18px;
            border-radius: 999px;
            border: 1px solid rgba(16, 229, 138, 0.25);
        }}
        .content-area {{
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            margin: 30px 0;
        }}
        .badge-pill {{
            align-self: flex-start;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            background: {bg_pill};
            border: 1.5px solid {border_pill};
            color: {text_pill};
            font-family: var(--font-mono);
            font-size: 16px;
            font-weight: 800;
            padding: 10px 20px;
            border-radius: 10px;
            letter-spacing: 0.05em;
            margin-bottom: 24px;
        }}
        .badge-dot {{
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: {dot_color};
            box-shadow: 0 0 10px {dot_color};
        }}
        .headline {{
            font-family: var(--font-head);
            font-size: 50px;
            font-weight: 800;
            line-height: 1.15;
            letter-spacing: -0.03em;
            margin-bottom: 30px;
        }}
        .headline span {{ color: {text_pill}; }}
        
        /* Slide 1 styles */
        .hook-box {{
            background: rgba(15, 23, 42, 0.65);
            border: 1.5px solid #1e293b;
            border-radius: 24px;
            padding: 36px;
        }}
        .hook-desc {{
            font-size: 24px;
            line-height: 1.5;
            color: #cbd5e1;
            margin-bottom: 32px;
        }}
        .hook-desc b {{ color: #ffffff; }}
        .vs-strip {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: #090d14;
            border: 1px solid #1e293b;
            border-radius: 18px;
            padding: 24px 32px;
        }}
        .vs-col {{
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}
        .vs-label {{
            font-family: var(--font-mono);
            font-size: 14px;
            font-weight: 700;
            color: #64748b;
        }}
        .vs-num {{
            font-family: var(--font-head);
            font-size: 38px;
            font-weight: 900;
        }}
        .vs-num.red {{ color: var(--red-alert); }}
        .vs-num.emerald {{ color: var(--emerald-glow); }}
        .vs-sub {{
            font-family: var(--font-mono);
            font-size: 14px;
            color: #94a3b8;
        }}
        .vs-divider {{
            font-family: var(--font-mono);
            font-size: 20px;
            font-weight: 800;
            color: #475569;
            background: #0f172a;
            padding: 8px 16px;
            border-radius: 10px;
        }}

        /* Slide 2 styles */
        .cards-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }}
        .cost-card {{
            background: #0d121c;
            border: 1.5px solid #231b25;
            border-radius: 20px;
            padding: 28px;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }}
        .cost-num-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .cost-badge {{
            font-family: var(--font-mono);
            font-size: 13px;
            font-weight: 800;
            color: #64748b;
        }}
        .cost-val.red {{
            font-family: var(--font-mono);
            font-size: 26px;
            font-weight: 900;
            color: var(--red-alert);
        }}
        .cost-title {{
            font-family: var(--font-head);
            font-size: 20px;
            font-weight: 700;
            color: #ffffff;
            margin-top: 4px;
        }}
        .cost-desc {{
            font-size: 16px;
            line-height: 1.45;
            color: #94a3b8;
        }}

        /* Slide 3 styles */
        .arch-container {{
            display: flex;
            flex-direction: column;
            gap: 16px;
        }}
        .arch-card {{
            background: #0d121c;
            border: 1.5px solid #1e293b;
            border-radius: 20px;
            padding: 22px 28px;
            display: flex;
            align-items: center;
            gap: 22px;
        }}
        .arch-icon {{
            font-size: 34px;
            width: 60px;
            height: 60px;
            background: rgba(16, 229, 138, 0.1);
            border: 1px solid rgba(16, 229, 138, 0.25);
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }}
        .arch-info {{
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}
        .arch-title {{
            font-family: var(--font-head);
            font-size: 20px;
            font-weight: 700;
            color: #ffffff;
        }}
        .arch-desc {{
            font-size: 16px;
            line-height: 1.4;
            color: #94a3b8;
        }}

        /* Slide 4 styles */
        .table-card {{
            background: #0d121c;
            border: 1.5px solid #1e293b;
            border-radius: 22px;
            overflow: hidden;
        }}
        .t-row {{
            display: grid;
            grid-template-columns: 1.6fr 1.2fr 1.5fr;
            padding: 20px 28px;
            border-bottom: 1px solid #1e293b;
            align-items: center;
        }}
        .t-row:last-child {{ border-bottom: none; }}
        .t-head {{
            background: #080c14;
            font-family: var(--font-mono);
            font-size: 14px;
            font-weight: 800;
            color: #64748b;
        }}
        .t-cell.metric {{
            font-family: var(--font-ui);
            font-size: 18px;
            font-weight: 600;
            color: #cbd5e1;
        }}
        .t-cell.human {{
            font-family: var(--font-mono);
            font-size: 17px;
            font-weight: 700;
            color: #94a3b8;
        }}
        .t-cell.human.red {{ color: var(--red-alert); }}
        .t-cell.vance {{
            font-family: var(--font-mono);
            font-size: 17px;
            font-weight: 800;
        }}
        .t-cell.vance.emerald {{ color: var(--emerald-glow); }}

        /* Slide 5 styles */
        .cta-wrap {{
            background: #0d121c;
            border: 2px solid rgba(16, 229, 138, 0.4);
            border-radius: 26px;
            padding: 40px;
            box-shadow: 0 0 50px rgba(16, 229, 138, 0.1);
        }}
        .cta-main-text {{
            font-size: 24px;
            line-height: 1.5;
            color: #cbd5e1;
            margin-bottom: 26px;
        }}
        .cta-main-text b {{ color: #ffffff; }}
        .cta-offer-box {{
            background: #080d14;
            border: 1px dashed rgba(16, 229, 138, 0.5);
            border-radius: 18px;
            padding: 24px;
            margin-bottom: 28px;
        }}
        .offer-header {{
            font-family: var(--font-mono);
            font-size: 16px;
            font-weight: 800;
            color: var(--emerald-glow);
            margin-bottom: 8px;
        }}
        .offer-sub {{
            font-size: 20px;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 6px;
        }}
        .offer-sub b {{ color: var(--emerald-glow); }}
        .offer-desc {{
            font-size: 17px;
            line-height: 1.45;
            color: #94a3b8;
        }}
        .cta-domain-button {{
            background: var(--emerald-glow);
            color: #06080d;
            font-family: var(--font-mono);
            font-size: 20px;
            font-weight: 900;
            padding: 20px;
            border-radius: 16px;
            text-align: center;
            letter-spacing: 0.04em;
            margin-bottom: 20px;
        }}
        .cta-brand-footer {{
            font-family: var(--font-mono);
            font-size: 15px;
            color: #64748b;
            text-align: center;
        }}

        .footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid #1e293b;
            padding-top: 24px;
        }}
        .footer-brand {{
            font-family: var(--font-mono);
            font-size: 15px;
            color: #64748b;
        }}
        .footer-swipe {{
            font-family: var(--font-mono);
            font-size: 15px;
            font-weight: 700;
            color: var(--emerald-glow);
            letter-spacing: 0.02em;
        }}
    </style>
</head>
<body>
    <div class="ambient-glow-top"></div>
    <div class="canvas">
        <div class="header">
            <div class="brand-badge">
                <span class="brand-name">VANCE<span>.AI</span></span>
            </div>
            <div class="slide-counter">{slide['num']}/5</div>
        </div>

        <div class="content-area">
            <div class="badge-pill">
                <span class="badge-dot"></span>
                <span>{slide['badge']}</span>
            </div>
            <h1 class="headline">{slide['headline']}</h1>
            {content_html}
        </div>

        <div class="footer">
            <div class="footer-brand">@usevance.ai • usevance.com</div>
            <div class="footer-swipe">{slide['footer']}</div>
        </div>
    </div>
</body>
</html>"""
    return html

def render_slides():
    print("🎨 Rendering 5 Vance Dark Obsidian Slides (1080x1350)...")
    png_paths = []
    
    for slide in SLIDES:
        num = slide["num"]
        html_content = generate_html_slide(slide)
        html_file = OUTPUT_DIR / f"slide_{num}.html"
        png_file = OUTPUT_DIR / f"slide_{num}.png"
        
        with open(html_file, "w") as f:
            f.write(html_content)
            
        cmd = [
            CHROME_BIN,
            "--headless=new",
            "--window-size=1080,1350",
            "--force-device-scale-factor=1",
            "--hide-scrollbars",
            f"--screenshot={png_file}",
            f"file://{html_file}"
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if png_file.exists():
            png_paths.append(png_file)
            print(f"  ✓ Slide {num}/5 rendered: {png_file.name} ({png_file.stat().st_size / 1024:.1f} KB)")
        else:
            print(f"  ❌ Failed to render Slide {num}")

    return png_paths

def generate_pdf(png_paths):
    print("\n📄 Generating LinkedIn Swipeable PDF Document...")
    pdf_path = OUTPUT_DIR / "vance_sdr_unit_economics_audit.pdf"
    images = [Image.open(p).convert("RGB") for p in png_paths]
    images[0].save(pdf_path, save_all=True, append_images=images[1:], quality=95)
    print(f"  ✅ PDF Created: {pdf_path.name} ({pdf_path.stat().st_size / 1024:.1f} KB)")
    return pdf_path

def send_to_telegram(png_paths, pdf_path):
    print("\n📲 Sending Vance Post #2 Assets to Vance Supergroup (-1003882353811)...")

    # 1. Send Header Alert
    print("  🔔 Sending Header Notification...")
    header_text = (
        "🔥 <b>VANCE AI (@usevance.ai) FRESH CONTENT DROP • POST #2</b>\n\n"
        "Bhai, ye raha Vance ka <b>BRAND NEW Post #2 Carousel (The $5,700/mo Human SDR Unit Economics Audit)</b>!\n"
        "Zero repeat content — full fresh P&L breakdown, side-by-side benchmark, aur ready-to-copy caption:"
    )
    payload_h = json.dumps({"chat_id": TELEGRAM_CHAT_ID, "text": header_text, "parse_mode": "HTML"}).encode("utf-8")
    req_h = urllib.request.Request(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", data=payload_h, headers={"Content-Type": "application/json"})
    urllib.request.urlopen(req_h, timeout=15)

    # 2. Send 5 PNG Slides Album via curl
    print("  📸 Uploading 5-Slide Album via curl...")
    cmd_album = [
        "curl", "-s", "-X", "POST",
        f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMediaGroup",
        "-F", f"chat_id={TELEGRAM_CHAT_ID}",
        "-F", 'media=[{"type":"photo","media":"attach://s1"},{"type":"photo","media":"attach://s2"},{"type":"photo","media":"attach://s3"},{"type":"photo","media":"attach://s4"},{"type":"photo","media":"attach://s5"}]',
        "-F", f"s1=@{png_paths[0]}",
        "-F", f"s2=@{png_paths[1]}",
        "-F", f"s3=@{png_paths[2]}",
        "-F", f"s4=@{png_paths[3]}",
        "-F", f"s5=@{png_paths[4]}"
    ]
    res_a = subprocess.run(cmd_album, capture_output=True, text=True)
    print("  Album result:", res_a.stdout[:150])

    # 3. Send 1-Tap Copy Caption
    print("  📝 Sending 1-Tap Copy Caption...")
    import html
    escaped_caption = html.escape(CAROUSEL_CAPTION)
    msg_caption = (
        "📋 <b>POST #5 CAROUSEL CAPTION (1-Tap Copy & Paste)</b>\n"
        "────────────────────────\n\n"
        f"<code>{escaped_caption}</code>\n\n"
        "────────────────────────\n"
        "💡 <b>Strategy Tips:</b>\n"
        "• Schedule: Upload between 6:30 PM – 7:30 PM IST.\n"
        "• Grid format: 1080x1350 (4:5 Portrait).\n"
        "• Comment 'AUDIT' aate hi: Send 20 sample ICP leads via DM."
    )
    payload_c = json.dumps({"chat_id": TELEGRAM_CHAT_ID, "text": msg_caption, "parse_mode": "HTML"}).encode("utf-8")
    req_c = urllib.request.Request(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", data=payload_c, headers={"Content-Type": "application/json"})
    urllib.request.urlopen(req_c, timeout=15)

    # 4. Send LinkedIn PDF
    print("  📑 Sending LinkedIn Document PDF...")
    cmd_pdf = [
        "curl", "-s", "-X", "POST",
        f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendDocument",
        "-F", f"chat_id={TELEGRAM_CHAT_ID}",
        "-F", f"document=@{pdf_path}",
        "-F", "caption=📄 <b>Vance Post #2 Swipeable PDF (For LinkedIn Document Posts)</b>\nTitle: Why Hiring a $5,700/mo Human SDR Is Financial Suicide in 2026",
        "-F", "parse_mode=HTML"
    ]
    res_p = subprocess.run(cmd_pdf, capture_output=True, text=True)
    print("  PDF result:", res_p.stdout[:150])

if __name__ == "__main__":
    pngs = render_slides()
    pdf = generate_pdf(pngs)
    send_to_telegram(pngs, pdf)
    print("🎉 VANCE POST #2 CAROUSEL COMPLETELY DISPATCHED TO TELEGRAM!")

