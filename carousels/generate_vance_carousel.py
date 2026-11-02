#!/usr/bin/env python3
"""
🎨 Programmatic High-Ticket B2B Carousel Generator — Vance AI SDR Post #3 (Obsidian Dark + Neon Emerald Cybernetic Aesthetic)
Generates:
1. 1080x1350 High-Res Dark PNG Slides (Obsidian Dark Theme matching Vance Feed Aesthetic)
2. Interactive Swipeable PDF Document (for LinkedIn Carousel Posts & Telegram)
3. Direct Telegram Push to Phone (5 PNG Album + 1-Tap Copy-Paste Caption)
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
OUTPUT_DIR = Path("/Users/mangal777/Mangal/growth_engine/carousels/vance_deck")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "-5489183481")

NOCO_URL = os.getenv("NOCO_URL", "https://crm.trackkaroai.com")
NOCO_TOKEN = os.getenv("NOCO_TOKEN", "")
NOCO_CONTENT_TABLE = "m0d70xh1eo1f6uh"

SLIDES_DATA = [
    {
        "num": 1,
        "badge": "AUTONOMOUS OUTBOUND BLUEPRINT",
        "badge_color": "emerald",
        "headline": "The 23 Buying Triggers That Replace a <span>$4,000/mo Human SDR</span>",
        "body": "Most B2B companies burn $4,000 to $6,000 every month hiring SDRs who manually spray 50 generic templates a day with a 0.8% reply rate.<br><br>Here is the exact <b>23-trigger intent architecture</b> powering <b>Vance AI</b> (@usevance.ai) to book high-ticket discovery calls on autopilot.",
        "footer": "Swipe to see the 23 triggers ➔"
    },
    {
        "num": 2,
        "badge": "INTENT TRIGGER MATRIX",
        "badge_color": "cyan",
        "headline": "We don't send cold emails. We send <span>timed reactions.</span>",
        "content_type": "triggers",
        "triggers": [
            {
                "cat": "HIRING SURGES",
                "code": "TRIGGERS 01 - 06",
                "desc": "Target company posts job for Head of Growth, SDR, or Sales Director in last 7 days.",
                "color": "#10b981",
                "border": "rgba(16, 185, 129, 0.4)",
                "bg": "rgba(16, 185, 129, 0.08)"
            },
            {
                "cat": "TECH STACK CHURN",
                "code": "TRIGGERS 07 - 12",
                "desc": "Domain installs Segment, switches CRM, or drops booking widgets detected via header audit.",
                "color": "#38bdf8",
                "border": "rgba(56, 189, 248, 0.4)",
                "bg": "rgba(56, 189, 248, 0.08)"
            },
            {
                "cat": "CAPITAL & LEADERSHIP",
                "code": "TRIGGERS 13 - 18",
                "desc": "Secured Seed/Series A round, or new VP/C-Suite executive appointed within 30 days.",
                "color": "#f59e0b",
                "border": "rgba(245, 158, 11, 0.4)",
                "bg": "rgba(245, 158, 11, 0.08)"
            },
            {
                "cat": "WEBSITE DE-ANONYMIZATION",
                "code": "TRIGGERS 19 - 23",
                "desc": "Target ICP visits pricing or product case study page 2+ times via reverse IP lookup.",
                "color": "#f43f5e",
                "border": "rgba(244, 63, 94, 0.4)",
                "bg": "rgba(244, 63, 94, 0.08)"
            }
        ],
        "footer": "The brutal economics comparison ➔"
    },
    {
        "num": 3,
        "badge": "THE ECONOMIC AUDIT",
        "badge_color": "rose",
        "headline": "Human SDR vs <span>Vance AI Retainer</span>",
        "content_type": "comparison",
        "human": {
            "title": "TRADITIONAL HUMAN SDR",
            "cost": "$4,500 / month",
            "rate": "50 manual emails/day",
            "detail": "40 hrs/wk • Needs 3-month ramp • 0.8% reply rate",
            "status": "High burn & domain burn risk"
        },
        "vance": {
            "title": "VANCE AUTONOMOUS SDR",
            "cost": "$1,500 / month",
            "rate": "15-Min Intent Cadence",
            "detail": "24/7/365 active • 0 ramp-up • 99.2% inbox deliverability",
            "status": "Scalable B2B pipeline on autopilot"
        },
        "footer": "Inside the 4-step pipeline ➔"
    },
    {
        "num": 4,
        "badge": "ENGINE ARCHITECTURE",
        "badge_color": "cyan",
        "headline": "Inside Vance's <span>4-Step Engine</span>",
        "content_type": "pipeline",
        "steps": [
            {"step": "01", "name": "Signal Ingestion", "desc": "Monitors 23 live intent streams every 15 minutes.", "tag": "15m Cycle"},
            {"step": "02", "name": "Waterfall Enrichment", "desc": "Extracts verified direct mobile and email via Apollo & Hunter.", "tag": "100% Valid"},
            {"step": "03", "name": "Context Angle Synthesis", "desc": "Gemini 1.5 Flash writes custom 50-word pitch tied to trigger.", "tag": "No Templates"},
            {"step": "04", "name": "Inbox Cadence Dispatch", "desc": "Sent from warm secondary domains directly to primary inbox.", "tag": "99.2% SLA"}
        ],
        "footer": "Get your first 20 leads ➔"
    },
    {
        "num": 5,
        "badge": "START QUALIFYING",
        "badge_color": "emerald",
        "headline": "Want 20 Verified ICP Leads <span>Qualified on Intent?</span>",
        "body": "Tell us your B2B ICP (Job Title, Industry, Target Tech Stack).<br><br>Vance will run an autonomous intent scan and deliver <b>20 verified high-intent leads with personalized hooks</b> directly to your inbox for free.<br><br>👉 <b>DM 'VANCE'</b> to @usevance.ai or test the engine live:",
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
        "indigo": ("rgba(99, 102, 241, 0.15)", "#818cf8", "#6366f1", "rgba(99, 102, 241, 0.4)"),
    }
    bg_pill, text_pill, dot_color, border_pill = badge_colors.get(slide.get("badge_color", "emerald"))

    content_html = ""
    c_type = slide.get("content_type", "default")

    if c_type == "triggers":
        for t in slide["triggers"]:
            content_html += f"""
            <div class="trigger-card" style="border-left: 6px solid {t['color']};">
                <div class="trigger-top">
                    <span class="trigger-cat" style="color: {t['color']};">{t['cat']}</span>
                    <span class="trigger-code">{t['code']}</span>
                </div>
                <div class="trigger-desc">{t['desc']}</div>
            </div>
            """
    elif c_type == "comparison":
        h = slide["human"]
        v = slide["vance"]
        content_html = f"""
        <div class="comp-grid">
            <div class="comp-card bad">
                <div class="comp-label">{h['title']}</div>
                <div class="comp-cost">{h['cost']}</div>
                <div class="comp-rate">{h['rate']}</div>
                <div class="comp-sub">{h['detail']}</div>
                <div class="comp-badge bad-badge">{h['status']}</div>
            </div>
            <div class="comp-card good">
                <div class="comp-label" style="color: #34d399;">{v['title']}</div>
                <div class="comp-cost" style="color: #34d399;">{v['cost']}</div>
                <div class="comp-rate" style="color: #ffffff;">{v['rate']}</div>
                <div class="comp-sub">{v['detail']}</div>
                <div class="comp-badge good-badge">{v['status']}</div>
            </div>
        </div>
        """
    elif c_type == "pipeline":
        for st in slide["steps"]:
            content_html += f"""
            <div class="pipe-card">
                <div class="pipe-num">{st['step']}</div>
                <div class="pipe-info">
                    <div class="pipe-name">{st['name']}</div>
                    <div class="pipe-desc">{st['desc']}</div>
                </div>
                <div class="pipe-tag">{st['tag']}</div>
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

        /* Trigger Cards (Dark Glass) */
        .trigger-card {{
            background: rgba(18, 22, 34, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 18px;
            padding: 22px 28px;
            margin-bottom: 18px;
            backdrop-filter: blur(10px);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
        }}
        .trigger-top {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        }}
        .trigger-cat {{
            font-size: 26px;
            font-weight: 800;
            letter-spacing: 0.04em;
        }}
        .trigger-code {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 18px;
            font-weight: 800;
            color: #94a3b8;
            background: rgba(255, 255, 255, 0.06);
            padding: 4px 12px;
            border-radius: 8px;
            border: 1px solid rgba(255, 255, 255, 0.08);
        }}
        .trigger-desc {{
            font-size: 22px;
            color: #94a3b8;
            font-weight: 500;
            line-height: 1.4;
        }}

        /* Comparison Cards (Dark Mode Split) */
        .comp-grid {{
            display: flex;
            flex-direction: column;
            gap: 20px;
            margin-top: 10px;
        }}
        .comp-card {{
            border-radius: 22px;
            padding: 28px 34px;
            position: relative;
            backdrop-filter: blur(10px);
        }}
        .comp-card.bad {{
            background: rgba(244, 63, 94, 0.08);
            border: 1.5px solid rgba(244, 63, 94, 0.35);
            box-shadow: 0 4px 20px rgba(244, 63, 94, 0.1);
        }}
        .comp-card.good {{
            background: rgba(16, 185, 129, 0.10);
            border: 2px solid rgba(16, 185, 129, 0.45);
            box-shadow: 0 10px 30px rgba(16, 185, 129, 0.2);
        }}
        .comp-label {{
            font-size: 20px;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: #94a3b8;
            margin-bottom: 8px;
        }}
        .comp-cost {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 52px;
            font-weight: 900;
            margin-bottom: 6px;
        }}
        .bad .comp-cost {{ color: #fb7185; }}
        .good .comp-cost {{ color: #34d399; }}
        .comp-rate {{
            font-size: 26px;
            color: #ffffff;
            font-weight: 800;
            margin-bottom: 6px;
        }}
        .comp-sub {{
            font-size: 21px;
            color: #94a3b8;
            font-weight: 500;
            margin-bottom: 14px;
        }}
        .comp-badge {{
            display: inline-block;
            font-size: 18px;
            font-weight: 800;
            padding: 6px 16px;
            border-radius: 999px;
            font-family: 'JetBrains Mono', monospace;
        }}
        .bad-badge {{
            background: rgba(244, 63, 94, 0.2);
            color: #fb7185;
            border: 1px solid rgba(244, 63, 94, 0.4);
        }}
        .good-badge {{
            background: rgba(16, 185, 129, 0.2);
            color: #34d399;
            border: 1px solid rgba(16, 185, 129, 0.4);
        }}

        /* Pipeline Cards (Dark Glass) */
        .pipe-card {{
            background: rgba(18, 22, 34, 0.85);
            border: 1px solid rgba(16, 185, 129, 0.25);
            border-radius: 20px;
            padding: 22px 28px;
            display: flex;
            align-items: center;
            gap: 24px;
            margin-bottom: 18px;
            backdrop-filter: blur(10px);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
        }}
        .pipe-num {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 32px;
            font-weight: 900;
            color: #34d399;
            background: rgba(16, 185, 129, 0.12);
            padding: 8px 16px;
            border-radius: 12px;
            border: 1px solid rgba(16, 185, 129, 0.3);
        }}
        .pipe-info {{ flex: 1; }}
        .pipe-name {{
            font-size: 26px;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 4px;
        }}
        .pipe-desc {{
            font-size: 20px;
            color: #94a3b8;
            font-weight: 500;
        }}
        .pipe-tag {{
            font-family: 'JetBrains Mono', monospace;
            background: rgba(6, 182, 212, 0.15);
            color: #38bdf8;
            border: 1px solid rgba(6, 182, 212, 0.35);
            padding: 8px 16px;
            border-radius: 10px;
            font-size: 18px;
            font-weight: 800;
        }}

        /* CTA Button */
        .cta-btn {{
            display: inline-block;
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: #041f14;
            font-size: 36px;
            font-weight: 900;
            padding: 22px 52px;
            border-radius: 999px;
            font-family: 'JetBrains Mono', monospace;
            margin: 32px 0 24px 0;
            box-shadow: 0 12px 36px rgba(16, 185, 129, 0.35);
            letter-spacing: -0.02em;
        }}
        .author-tag {{
            font-size: 24px;
            color: #64748b;
            font-weight: 700;
        }}

        /* Footer Row */
        .footer-row {{
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            padding-top: 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .brand-name {{
            font-size: 22px;
            font-weight: 800;
            letter-spacing: 0.05em;
            color: #64748b;
        }}
        .footer-text {{
            font-size: 22px;
            font-weight: 800;
            color: #34d399;
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
    print("🎨 Rendering 5 Vance Dark Obsidian Slides to 1080x1350 PNG...")
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
            "--force-device-scale-factor=1",
            "--window-size=1080,1350",
            f"--screenshot={png_file}",
            f"file://{html_file.resolve()}"
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        png_paths.append(png_file)
        print(f"  ✓ Slide {num}/5 rendered: {png_file.name}")
        
    return png_paths

def compile_pdf(png_paths):
    pdf_path = OUTPUT_DIR / "Vance_23_Buying_Triggers_Carousel.pdf"
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

INSTA_CAPTION = """Most B2B founders burn $4,000 to $6,000/mo hiring human SDRs to spray 50 generic cold emails a day. 

Result? 0.8% reply rate and a burnt domain in 30 days. 📉

Instead of cold pitching, @usevance.ai runs on 23 Autonomous Intent Buying Triggers:

1️⃣ Hiring Spikes: When a company posts jobs for Growth/Sales roles in the last 7 days.
2️⃣ Tech Stack Churn: When they drop legacy tools or install Segment/VWO detected via HTTP header audit.
3️⃣ Capital & Leadership: Seed/Series A rounds or new C-Suite execs appointed within 30 days.
4️⃣ Reverse-IP De-anonymization: High-intent ICP accounts visiting your pricing page 2+ times.

We don't send cold emails. We send timed reactions on a 15-minute cadence with a 99.2% inbox deliverability SLA. ⚡

👉 Want 20 verified high-intent ICP leads for your business?
Comment "VANCE" below or DM us @usevance.ai — our autonomous SDR will scan your ICP and deliver 20 leads straight to your inbox.

🔗 Test the live sandbox: usevance.com (link in bio)

#aisdr #b2bsaas #growtharchitecture #coldoutreach #speedtolead #gtmstrategy #salesautomation #usevance"""

def send_to_telegram(pdf_path, png_paths):
    print("\n📲 Sending Vance Carousel Assets to Telegram...")
    
    # 1. Send all 5 PNG slides as a native Instagram Album
    print("  📸 Uploading 5 PNG slides album for Instagram...")
    try:
        boundary_album = "----WebKitFormBoundaryAlbumVance"
        album_data = []
        album_data.append(f"--{boundary_album}".encode())
        album_data.append(b'Content-Disposition: form-data; name="chat_id"\r\n')
        album_data.append(TELEGRAM_CHAT_ID.encode())
        
        media_items = []
        for i in range(1, len(png_paths) + 1):
            media_items.append({
                "type": "photo",
                "media": f"attach://slide_{i}",
                "caption": "📊 <b>VANCE AI • Slide 1/5: The 23 Buying Triggers That Replace a $4,000/mo Human SDR</b>\n\n👉 <i>Swipe right to see all 5 slides in Obsidian Dark Theme. Save to Photos & upload directly to Instagram!</i>" if i == 1 else "",
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
            print("  ✅ Sent 5 PNG slides album to Telegram (Save all to Photos)!")
    except Exception as e:
        print(f"  ⚠️ Telegram album error: {e}")

    # 2. Send 1-Tap Copy-Paste Caption & Hashtags
    print("  📝 Sending formatted Instagram caption & hashtags...")
    try:
        msg_text = (
            "📋 <b>INSTAGRAM POST CAPTION (1-Tap Copy & Paste)</b>\n"
            "────────────────────────\n\n"
            f"{INSTA_CAPTION}\n\n"
            "────────────────────────\n"
            "💡 <b>Instagram Posting Tips:</b>\n"
            "1. Open Instagram ➔ Tap '+' ➔ Select the 5 saved PNGs (Order 1 to 5).\n"
            "2. Paste this exact caption.\n"
            "3. Add Location: 'San Francisco, California' or 'New York' for B2B algorithm reach."
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
            print("  ✅ Sent 1-tap copy-paste caption to Telegram!")
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
        caption_pdf = "📑 <b>Vance AI • 5-Slide B2B Swipeable PDF (LinkedIn Ready - Dark Theme)</b>\n\n📌 <b>Topic:</b> The 23 Buying Triggers That Replace a $4,000/mo Human SDR\n\n👉 <b>LinkedIn Post:</b> Upload this PDF as a 'Document' post ➔ LinkedIn renders it as an interactive carousel!\n🔗 <b>CTA:</b> usevance.com"
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
            print("  ✅ Sent Vance Carousel PDF to Telegram!")
    except Exception as e:
        print(f"  ⚠️ Telegram PDF error: {e}")

def log_to_nocodb(pdf_path):
    print("\n🌐 Logging Vance Carousel to NocoDB Content Assets Table...")
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
            "Asset Type": "5-Slide PDF & PNG Carousel (Dark Obsidian)",
            "Hook / Title": "The 23 Buying Triggers That Replace a $4,000/mo Human SDR",
            "Script / Prompt / Code": f"PDF: {pdf_path.name}\n5 Slides: $4k SDR vs Vance, Intent Trigger Matrix (01-23), 4-Step Pipeline, 20 Free Verified Leads CTA.\nDomain: usevance.com",
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
    print("\n🎉 Vance Dark Carousel generated, compiled to PDF, sent to Telegram, and saved in NocoDB!")

if __name__ == "__main__":
    main()
