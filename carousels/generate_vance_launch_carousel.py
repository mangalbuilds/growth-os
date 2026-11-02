#!/usr/bin/env python3
"""
🎨 Programmatic High-Ticket B2B Carousel Generator — Vance AI SDR Launch Post #1 (Dark Obsidian + Neon Emerald Cybernetic Aesthetic)
Generates:
1. 1080x1350 High-Res Dark PNG Slides (Optimized for Instagram Dark Mode & Mobile Screen Pop)
2. Interactive Swipeable PDF Document (for LinkedIn)
3. Direct Push to Telegram: 5 PNG Album + 1-Tap Copy-Paste Launch Caption + LinkedIn PDF
4. Auto-logging into NocoDB Content Assets Table under 'vance'
"""

import os
import sys
import json
import subprocess
import urllib.request
from pathlib import Path
from PIL import Image

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import env_loader

CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUTPUT_DIR = Path("/Users/mangal777/Mangal/growth_engine/carousels/vance_launch_deck")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "-5489183481")

NOCO_URL = os.getenv("NOCO_URL", "https://crm.trackkaroai.com")
NOCO_TOKEN = os.getenv("NOCO_TOKEN", "")
NOCO_CONTENT_TABLE = "m0d70xh1eo1f6uh"

LAUNCH_CAPTION = """Day 1. The B2B outbound playbook is officially broken. 📉

In 2026, hiring an SDR for $4,500/mo to spray 10,000 generic email templates only does two things:
1. Burns your primary company domain in 30 days
2. Yields an embarrassing 0.8% reply rate

Buyers are numb to cold templates. They don't want spam — they want timed, relevant reactions.

That's why we built @usevance.ai. ⚡

Instead of guessing, Vance runs autonomously on 23 Intent Buying Triggers:
🎯 Hiring Spikes (Companies hiring Growth/SDR roles in the last 7 days)
⚡ Tech Stack Churn (Detecting when a company drops legacy tools or installs modern software)
🚀 Capital & Leadership (Funding rounds & newly appointed VPs within 30 days)
👀 Reverse-IP De-anonymization (ICP accounts visiting pricing/case-study pages 2+ times)

We don't buy static lists. We audit live web signals and react in 15 minutes with hyper-personalized 40-word pitches.

🚀 DAY 1 FOUNDING PARTNER OFFER:
We are onboarding our first 10 B2B tech companies and agencies this week.

Comment "VANCE" below or DM us @usevance.ai with your ICP:
Our AI engine will scan live intent streams and deliver 20 verified high-intent leads straight to your inbox for free.

🔗 Experience the live sandbox: usevance.com (link in bio)

Built with conviction by @mangal777 

#buildinpublic #aisdr #b2bsaas #growtharchitecture #outboundautomation #gtmstrategy #usevance #foundermode
"""

SLIDES_DATA = [
    {
        "num": 1,
        "badge": "DAY 01 • THE GENESIS",
        "badge_color": "emerald",
        "headline": "The B2B Outbound Playbook Is Dead. <span>Here is what replaces it.</span>",
        "body": "In 2026, spraying 10,000 generic cold emails a month burns your domain in 30 days and yields an embarrassing 0.8% reply rate.<br><br>Buyers don't want templates. They want <b>timed reactions</b>.<br><br>Here is why we built <b>Vance AI</b> (@usevance.ai).",
        "footer": "Swipe to see the new architecture ➔"
    },
    {
        "num": 2,
        "badge": "THE ROOT PROBLEM",
        "badge_color": "rose",
        "headline": "Why the $4,500/mo Human SDR Model Is <span>Collapsing</span>",
        "content_type": "pain_points",
        "points": [
            {
                "num": "01",
                "title": "Spray & Pray Deliverability Trap",
                "desc": "Email providers now aggressively penalize template blast volume. Real inbox rate drops to <65%.",
                "tag": "Burnt Domains"
            },
            {
                "num": "02",
                "title": "Astronomical Burn Rate",
                "desc": "$4,000 to $6,000/mo base salary + 3 months ramp time for an average 1.2% qualified meeting rate.",
                "tag": "$60k/yr Wasted"
            },
            {
                "num": "03",
                "title": "Zero Intent Signal Awareness",
                "desc": "Reaching out blindly when the target account has zero budget, no open roles, and zero interest.",
                "tag": "94% Ghost Rate"
            }
        ],
        "footer": "The autonomous solution ➔"
    },
    {
        "num": 3,
        "badge": "THE SOLUTION",
        "badge_color": "emerald",
        "headline": "Meet Vance: <span>Autonomous Intent SDR</span>",
        "content_type": "solution_features",
        "features": [
            {"icon": "⚡", "title": "23 Buying Triggers", "desc": "Hiring surges, tech stack churn, funding rounds, and website reverse-IP tracking."},
            {"icon": "⏱️", "title": "15-Min Cadence Engine", "desc": "Captures buyer attention in real-time while their intent trigger is at its absolute peak."},
            {"icon": "🧠", "title": "Zero Boilerplate Pitching", "desc": "Gemini 1.5 Flash crafts hyper-specific 50-word angles tied directly to the trigger."},
            {"icon": "🛡️", "title": "99.2% Deliverability SLA", "desc": "Isolated secondary warm domain network keeps your primary domain 100% safe."}
        ],
        "footer": "The two-pillar architecture ➔"
    },
    {
        "num": 4,
        "badge": "THE ARCHITECTURE",
        "badge_color": "cyan",
        "headline": "Two Pillars: <span>Live Signals + Micro-Pitching</span>",
        "content_type": "dual_system",
        "outbound": {
            "title": "PILLAR 1: LIVE INTENT AUDIT",
            "desc": "Scans 23 signals 24/7 (hiring spikes on LinkedIn, Google SERP sweet spots, SDK headers).",
            "stat": "23 Live Signals"
        },
        "inbound": {
            "title": "PILLAR 2: BESPOKE DISPATCH",
            "desc": "Generates 40-word problem-solver reaction pitches. Delivered via isolated domains with <2% bounce rate.",
            "stat": "Sub-2% Bounce SLA"
        },
        "footer": "Claim founding partner perks ➔"
    },
    {
        "num": 5,
        "badge": "DAY 01 INVITATION",
        "badge_color": "emerald",
        "headline": "We're Onboarding <span>10 Founding B2B Partners</span>",
        "body": "To celebrate Day 1, we are offering complimentary intent audits for 10 high-growth B2B companies.<br><br>Tell us your ICP (Industry, Title, Tech Stack) — Vance will scan live streams and deliver <b>20 verified high-intent leads</b> straight to your inbox.<br><br>👉 <b>DM 'VANCE'</b> to @usevance.ai or test the engine live:",
        "cta_button": "usevance.com",
        "author": "Vance AI • Autonomous B2B Intent Engine (@usevance.ai)",
        "footer": "Save this post for your 2026 outbound playbook"
    }
]

def generate_html_slide(slide):
    badge_colors = {
        "emerald": ("rgba(16, 185, 129, 0.15)", "#34d399", "#10b981", "rgba(16, 185, 129, 0.4)"),
        "rose": ("rgba(244, 63, 94, 0.15)", "#fb7185", "#f43f5e", "rgba(244, 63, 94, 0.4)"),
        "cyan": ("rgba(6, 182, 212, 0.15)", "#38bdf8", "#06b6d4", "rgba(6, 182, 212, 0.4)"),
    }
    bg_pill, text_pill, dot_color, border_pill = badge_colors.get(slide.get("badge_color", "emerald"))

    content_html = ""
    c_type = slide.get("content_type", "default")

    if c_type == "pain_points":
        for pt in slide["points"]:
            content_html += f"""
            <div class="pain-card">
                <div class="pain-num">{pt['num']}</div>
                <div class="pain-content">
                    <div class="pain-title-row">
                        <span class="pain-title">{pt['title']}</span>
                        <span class="pain-tag">{pt['tag']}</span>
                    </div>
                    <div class="pain-desc">{pt['desc']}</div>
                </div>
            </div>
            """
    elif c_type == "solution_features":
        for feat in slide["features"]:
            content_html += f"""
            <div class="feat-card">
                <div class="feat-icon">{feat['icon']}</div>
                <div class="feat-text">
                    <div class="feat-title">{feat['title']}</div>
                    <div class="feat-desc">{feat['desc']}</div>
                </div>
            </div>
            """
    elif c_type == "dual_system":
        o = slide["outbound"]
        i = slide["inbound"]
        content_html = f"""
        <div class="dual-grid">
            <div class="system-card outbound">
                <div class="sys-label">🎯 {o['title']}</div>
                <div class="sys-desc">{o['desc']}</div>
                <div class="sys-tag out-tag">{o['stat']}</div>
            </div>
            <div class="system-card inbound">
                <div class="sys-label">⚡ {i['title']}</div>
                <div class="sys-desc">{i['desc']}</div>
                <div class="sys-tag in-tag">{i['stat']}</div>
            </div>
        </div>
        <div class="synced-banner">
            <span class="sync-dot"></span>
            <b>Zero Domain Decay:</b> Secondary domain network + waterfall verification = sub-2% bounce SLA.
        </div>
        """
    else:
        body = slide.get("body", "")
        cta = slide.get("cta_button")
        author = slide.get("author", "")
        content_html = f'<div class="main-body">{body}</div>'
        if cta:
            content_html += f'<div class="cta-btn">{cta}</div>'
        if author:
            content_html += f'<div class="author-tag">{author}</div>'

    html = f"""<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800;900&family=JetBrains+Mono:wght@600;700;800&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            width: 1080px;
            height: 1350px;
            overflow: hidden;
            background: #080a11;
            font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
            color: #ffffff;
            position: relative;
        }}
        .canvas {{
            width: 1080px;
            height: 1350px;
            padding: 90px 80px 70px 80px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            background: radial-gradient(circle at 85% 15%, rgba(16, 185, 129, 0.15) 0%, transparent 60%),
                        radial-gradient(circle at 15% 85%, rgba(6, 182, 212, 0.10) 0%, transparent 55%),
                        #080a11;
        }}
        .top-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .badge {{
            display: inline-flex;
            align-items: center;
            gap: 12px;
            background: {bg_pill};
            border: 1px solid {border_pill};
            padding: 14px 26px;
            border-radius: 999px;
            font-size: 22px;
            font-weight: 800;
            letter-spacing: 0.08em;
            color: {text_pill};
            text-transform: uppercase;
        }}
        .dot {{
            width: 12px;
            height: 12px;
            background: {dot_color};
            border-radius: 50%;
            box-shadow: 0 0 14px {dot_color};
        }}
        .slide-counter {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 26px;
            font-weight: 800;
            color: #64748b;
        }}
        .headline {{
            font-size: 64px;
            font-weight: 900;
            line-height: 1.15;
            letter-spacing: -0.04em;
            color: #ffffff;
            margin: 30px 0;
        }}
        .headline span {{
            background: linear-gradient(135deg, #10b981 0%, #38bdf8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .main-body {{
            font-size: 34px;
            color: #cbd5e1;
            font-weight: 500;
            line-height: 1.55;
            margin-top: 20px;
        }}
        .main-body b {{
            color: #ffffff;
            font-weight: 800;
        }}
        
        /* Pain Cards */
        .pain-card {{
            background: rgba(18, 22, 34, 0.85);
            border: 1px solid rgba(244, 63, 94, 0.25);
            border-radius: 22px;
            padding: 24px 30px;
            display: flex;
            align-items: flex-start;
            gap: 24px;
            margin-bottom: 20px;
        }}
        .pain-num {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 32px;
            font-weight: 900;
            color: #fb7185;
            background: rgba(244, 63, 94, 0.12);
            padding: 10px 18px;
            border-radius: 14px;
        }}
        .pain-content {{ flex: 1; }}
        .pain-title-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        }}
        .pain-title {{
            font-size: 28px;
            font-weight: 800;
            color: #ffffff;
        }}
        .pain-tag {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 18px;
            font-weight: 800;
            background: rgba(244, 63, 94, 0.2);
            color: #fb7185;
            padding: 4px 12px;
            border-radius: 8px;
        }}
        .pain-desc {{
            font-size: 22px;
            color: #94a3b8;
            font-weight: 500;
            line-height: 1.4;
        }}

        /* Feature Cards */
        .feat-card {{
            background: rgba(18, 22, 34, 0.85);
            border: 1px solid rgba(16, 185, 129, 0.25);
            border-radius: 22px;
            padding: 24px 30px;
            display: flex;
            align-items: center;
            gap: 24px;
            margin-bottom: 20px;
        }}
        .feat-icon {{
            font-size: 38px;
            background: rgba(16, 185, 129, 0.12);
            width: 70px;
            height: 70px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 18px;
            border: 1px solid rgba(16, 185, 129, 0.3);
        }}
        .feat-text {{ flex: 1; }}
        .feat-title {{
            font-size: 28px;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 6px;
        }}
        .feat-desc {{
            font-size: 22px;
            color: #94a3b8;
            font-weight: 500;
        }}

        /* Dual System */
        .dual-grid {{
            display: flex;
            flex-direction: column;
            gap: 20px;
            margin-bottom: 20px;
        }}
        .system-card {{
            border-radius: 24px;
            padding: 30px 36px;
            border: 2px solid rgba(255, 255, 255, 0.1);
        }}
        .system-card.outbound {{
            background: rgba(16, 185, 129, 0.08);
            border-color: rgba(16, 185, 129, 0.35);
        }}
        .system-card.inbound {{
            background: rgba(6, 182, 212, 0.08);
            border-color: rgba(6, 182, 212, 0.35);
        }}
        .sys-label {{
            font-size: 26px;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 10px;
        }}
        .sys-desc {{
            font-size: 22px;
            color: #cbd5e1;
            font-weight: 500;
            line-height: 1.45;
            margin-bottom: 14px;
        }}
        .sys-tag {{
            display: inline-block;
            font-family: 'JetBrains Mono', monospace;
            font-size: 20px;
            font-weight: 800;
            padding: 6px 16px;
            border-radius: 10px;
        }}
        .out-tag {{ background: rgba(16, 185, 129, 0.2); color: #34d399; }}
        .in-tag {{ background: rgba(6, 182, 212, 0.2); color: #38bdf8; }}

        .synced-banner {{
            background: rgba(18, 22, 34, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 18px 24px;
            font-size: 22px;
            color: #94a3b8;
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .synced-banner b {{ color: #ffffff; }}
        .sync-dot {{
            width: 10px;
            height: 10px;
            background: #10b981;
            border-radius: 50%;
            box-shadow: 0 0 10px #10b981;
        }}

        .cta-btn {{
            display: inline-block;
            background: linear-gradient(135deg, #10b981 0%, #06b6d4 100%);
            color: #06080d;
            font-size: 38px;
            font-weight: 900;
            padding: 24px 52px;
            border-radius: 999px;
            font-family: 'JetBrains Mono', monospace;
            margin: 30px 0 20px 0;
            box-shadow: 0 0 60px rgba(16, 185, 129, 0.4);
        }}
        .author-tag {{
            font-size: 26px;
            color: #94a3b8;
            font-weight: 700;
        }}
        .footer-row {{
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            padding-top: 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .brand-name {{
            font-size: 24px;
            font-weight: 800;
            letter-spacing: 0.05em;
            color: #64748b;
        }}
        .footer-text {{
            font-size: 24px;
            font-weight: 800;
            color: #10b981;
        }}
    </style>
</head>
<body>
    <div class="canvas">
        <div class="top-row">
            <div class="badge"><div class="dot"></div>{slide['badge']}</div>
            <div class="slide-counter">0{slide['num']} / 05</div>
        </div>
        
        <div>
            <h1 class="headline">{slide['headline']}</h1>
            {content_html}
        </div>

        <div class="footer-row">
            <div class="brand-name">VANCE AI • AUTONOMOUS B2B SDR</div>
            <div class="footer-text">{slide['footer']}</div>
        </div>
    </div>
</body>
</html>"""
    return html

def render_slides_to_png():
    print("🎨 Rendering 5 Vance Dark-Cybernetic Launch Slides to 1080x1350 PNG...")
    png_paths = []
    
    for s in SLIDES_DATA:
        num = s["num"]
        html_file = OUTPUT_DIR / f"slide_{num}.html"
        png_file = OUTPUT_DIR / f"slide_{num}.png"
        
        html_content = generate_html_slide(s)
        html_file.write_text(html_content, encoding="utf-8")
        
        cmd = [
            CHROME_BIN,
            "--headless=new",
            "--disable-gpu",
            "--window-size=1080,1350",
            f"--screenshot={png_file}",
            f"file://{html_file.resolve()}"
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        png_paths.append(png_file)
        print(f"  ✓ Slide {num}/5 rendered: {png_file.name}")
        
    return png_paths

def compile_pdf(png_paths):
    pdf_path = OUTPUT_DIR / "Vance_Post_01_Launch_Manifesto.pdf"
    print(f"\n📑 Compiling LinkedIn Swipeable PDF: {pdf_path.name}...")
    
    images = [Image.open(p).convert("RGB") for p in png_paths]
    images[0].save(
        pdf_path,
        save_all=True,
        append_images=images[1:],
        quality=95
    )
    print(f"  ✅ PDF Created: {pdf_path} ({pdf_path.stat().st_size / 1024:.1f} KB)")
    return pdf_path

def send_to_telegram(pdf_path, png_paths):
    print("\n📲 Sending Vance Launch Post Assets to Telegram...")
    
    # 1. Send all 5 PNG slides as a native Instagram Album
    print("  📸 Uploading 5 Dark-Cybernetic PNG slides album for Instagram...")
    try:
        boundary_album = "----WebKitFormBoundaryAlbumVanceLaunch"
        album_data = []
        album_data.append(f"--{boundary_album}".encode())
        album_data.append(b'Content-Disposition: form-data; name="chat_id"\r\n')
        album_data.append(TELEGRAM_CHAT_ID.encode())
        
        media_items = []
        for i in range(1, len(png_paths) + 1):
            media_items.append({
                "type": "photo",
                "media": f"attach://slide_{i}",
                "caption": "🔥 <b>VANCE AI • POST #1 LAUNCH MANIFESTO (Slide 1/5)</b>\n\n👉 <i>Dark Obsidian + Glowing Emerald Neon. Swipe to see all 5 slides. Save to Photos & upload to Instagram!</i>" if i == 1 else "",
                "parse_mode": "HTML"
            })
            
        album_data.append(f"--{boundary_album}".encode())
        album_data.append(b'Content-Disposition: form-data; name="media"\r\n')
        album_data.append(json.dumps(media_items).encode("utf-8"))
        
        for i, p in enumerate(png_paths, 1):
            album_data.append(f"--{boundary_album}".encode())
            album_data.append(f'Content-Disposition: form-data; name="slide_{i}"; filename="{p.name}"\r\nContent-Type: image/png\r\n'.encode())
            with open(p, "rb") as f:
                album_data.append(f.read())
        album_data.append(f"--{boundary_album}--\r\n".encode())
        
        req_album = urllib.request.Request(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMediaGroup",
            data=b"\r\n".join(album_data),
            headers={"Content-Type": f"multipart/form-data; boundary={boundary_album}"},
            method="POST"
        )
        with urllib.request.urlopen(req_album, timeout=40) as resp:
            print("  ✅ Sent 5 Dark PNG slides album to Telegram!")
    except Exception as e:
        print(f"  ⚠️ Telegram album error: {e}")

    # 2. Send 1-Tap Copy-Paste Launch Caption & Hashtags
    print("  📝 Sending formatted Instagram Launch Caption & Hashtags...")
    try:
        msg_text = (
            "📋 <b>INSTAGRAM POST #1 LAUNCH CAPTION (1-Tap Copy & Paste)</b>\n"
            "────────────────────────\n\n"
            f"{LAUNCH_CAPTION}\n\n"
            "────────────────────────\n"
            "💡 <b>First Post Strategy Tips:</b>\n"
            "1. Pin this post to the top of @usevance.ai profile (Grid Pin #1).\n"
            "2. Tag founder profile @mangal777 as collaborator or in caption.\n"
            "3. Location: 'San Francisco, California' or 'New York'."
        )
        payload = json.dumps({
            "chat_id": TELEGRAM_CHAT_ID,
            "text": msg_text,
            "parse_mode": "HTML",
            "disable_web_page_preview": True
        }).encode("utf-8")
        req_msg = urllib.request.Request(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req_msg, timeout=20) as resp:
            print("  ✅ Sent 1-tap copy-paste Launch caption to Telegram!")
    except Exception as e:
        print(f"  ⚠️ Telegram caption message error: {e}")

    # 3. Send PDF document (Swipeable on Telegram & LinkedIn)
    print("  📑 Sending LinkedIn swipeable PDF document...")
    try:
        boundary_pdf = "----WebKitFormBoundaryTelegramPDF"
        data_pdf = []
        data_pdf.append(f"--{boundary_pdf}".encode())
        data_pdf.append(b'Content-Disposition: form-data; name="chat_id"\r\n')
        data_pdf.append(TELEGRAM_CHAT_ID.encode())
        
        data_pdf.append(f"--{boundary_pdf}".encode())
        data_pdf.append(b'Content-Disposition: form-data; name="caption"\r\n')
        caption_pdf = "📑 <b>Vance AI • Post #1 Launch Manifesto PDF (LinkedIn Ready)</b>\n\n📌 <b>Topic:</b> The B2B Outbound Playbook Is Dead. Here Is What Replaces It.\n\n👉 <b>LinkedIn Post:</b> Upload this PDF as a 'Document' post ➔ Native swipeable carousel!\n🔗 <b>CTA:</b> usevance.com"
        data_pdf.append(caption_pdf.encode("utf-8"))
        
        data_pdf.append(f"--{boundary_pdf}".encode())
        data_pdf.append(b'Content-Disposition: form-data; name="parse_mode"\r\n')
        data_pdf.append(b"HTML")
        
        data_pdf.append(f"--{boundary_pdf}".encode())
        data_pdf.append(f'Content-Disposition: form-data; name="document"; filename="{pdf_path.name}"\r\nContent-Type: application/pdf\r\n'.encode())
        with open(pdf_path, "rb") as f:
            data_pdf.append(f.read())
        data_pdf.append(f"--{boundary_pdf}--\r\n".encode())
        
        req_pdf = urllib.request.Request(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendDocument",
            data=b"\r\n".join(data_pdf),
            headers={"Content-Type": f"multipart/form-data; boundary={boundary_pdf}"},
            method="POST"
        )
        with urllib.request.urlopen(req_pdf, timeout=30) as resp:
            print("  ✅ Sent Vance Launch PDF to Telegram!")
    except Exception as e:
        print(f"  ⚠️ Telegram PDF error: {e}")

def log_to_nocodb(pdf_path):
    print("\n🌐 Logging Vance Launch Post to NocoDB Content Assets Table...")
    try:
        boundary = "----WebKitFormBoundaryNocoUpload"
        data = []
        data.append(f"--{boundary}".encode())
        data.append(f'Content-Disposition: form-data; name="file"; filename="{pdf_path.name}"\r\nContent-Type: application/pdf\r\n'.encode())
        with open(pdf_path, "rb") as f:
            data.append(f.read())
        data.append(f"--{boundary}--\r\n".encode())
        
        upload_req = urllib.request.Request(
            f"{NOCO_URL}/api/v2/storage/upload",
            data=b"\r\n".join(data),
            headers={"xc-token": NOCO_TOKEN, "Content-Type": f"multipart/form-data; boundary={boundary}"},
            method="POST"
        )
        with urllib.request.urlopen(upload_req, timeout=15) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            
        record = [{
            "Project": "vance",
            "Target Platform": "LinkedIn & Instagram Carousel",
            "Asset Type": "5-Slide Dark Cybernetic Post #1 (Launch Manifesto)",
            "Hook / Title": "The B2B Outbound Playbook Is Dead. Here Is What Replaces It.",
            "Script / Prompt / Code": f"PDF: {pdf_path.name}\n5 Dark Slides: Day 1 Genesis, Collapse of $4.5k SDR, Vance 23-Trigger Engine, Inbound+Outbound OS, 10 Founding Partner Offer.\nDomain: usevance.com",
            "Production Status": "Rendered (Ready to Post)",
            "Video File (MP4)": res
        }]
        
        insert_req = urllib.request.Request(
            f"{NOCO_URL}/api/v2/tables/{NOCO_CONTENT_TABLE}/records",
            data=json.dumps(record).encode("utf-8"),
            headers={"xc-token": NOCO_TOKEN, "Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(insert_req, timeout=10) as resp:
            print("  ✅ Logged to NocoDB Content Assets table!")
    except Exception as e:
        print(f"  ⚠️ NocoDB logging error: {e}")

def main():
    png_paths = render_slides_to_png()
    pdf_path = compile_pdf(png_paths)
    send_to_telegram(pdf_path, png_paths)
    log_to_nocodb(pdf_path)
    print("\n🎉 Vance Post #1 Launch Manifesto generated, compiled to PDF, sent to Telegram, and saved in NocoDB!")

if __name__ == "__main__":
    main()
