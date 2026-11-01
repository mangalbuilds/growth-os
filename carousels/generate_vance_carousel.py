#!/usr/bin/env python3
"""
🎨 Programmatic High-Ticket B2B Carousel Generator — Vance AI SDR (Clean Light Silicon Valley Mode)
Generates:
1. 1080x1350 High-Res PNG Slides (Light Theme: Clean Apple/Linear/Stripe Memo Aesthetic)
2. Interactive Swipeable PDF Document (for LinkedIn Carousel Posts & Telegram)
3. Direct Telegram Push to Phone
4. Auto-logging into NocoDB Content Assets Table under 'vance'
"""

import os
import sys
import json
import subprocess
import urllib.request
from pathlib import Path
from PIL import Image

CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUTPUT_DIR = Path("/Users/mangal777/Mangal/growth_engine/carousels/vance_deck")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TELEGRAM_BOT_TOKEN = "8445264349:AAFWHjaQe9Qomf2Zwm7MVV_6NkhRmGWLMjs"
TELEGRAM_CHAT_ID = "-5489183481"

NOCO_URL = "https://crm.trackkaroai.com"
NOCO_TOKEN = "nc_pat_gPoul6APyQs7Qr77wz3VI6AmaqaXrNg8OipLKIsu"
NOCO_CONTENT_TABLE = "m0d70xh1eo1f6uh"

SLIDES_DATA = [
    {
        "num": 1,
        "badge": "AUTONOMOUS OUTBOUND BLUEPRINT",
        "badge_color": "emerald",
        "headline": "The 23 Buying Triggers That Replace a <span>$4,000/mo Human SDR</span>",
        "body": "Most B2B companies burn $4,000 to $6,000 every month hiring SDRs who manually spray 50 generic templates a day with a 0.8% reply rate.<br><br>Here is the exact <b>23-trigger intent architecture</b> powering <b>Vance AI</b> to book high-ticket discovery calls on autopilot.",
        "footer": "Swipe to see the 23 triggers ➔"
    },
    {
        "num": 2,
        "badge": "INTENT TRIGGER MATRIX",
        "badge_color": "indigo",
        "headline": "We don't send cold emails. We send <span>timed reactions.</span>",
        "content_type": "triggers",
        "triggers": [
            {
                "cat": "HIRING SURGES",
                "code": "TRIGGERS 01 - 06",
                "desc": "Target company posts job for Head of Growth, SDR, or Sales Director in last 7 days.",
                "color": "#059669"
            },
            {
                "cat": "TECH STACK CHURN",
                "code": "TRIGGERS 07 - 12",
                "desc": "Domain installs Segment, switches CRM, or starts testing tools detected via HTTP header audit.",
                "color": "#4f46e5"
            },
            {
                "cat": "CAPITAL & LEADERSHIP",
                "code": "TRIGGERS 13 - 18",
                "desc": "Secured Seed/Series A round, or new VP/C-Suite executive appointed within 30 days.",
                "color": "#d97706"
            },
            {
                "cat": "WEBSITE DE-ANONYMIZATION",
                "code": "TRIGGERS 19 - 23",
                "desc": "Target ICP visits pricing or product case study page 2+ times via reverse IP lookup.",
                "color": "#e11d48"
            }
        ],
        "footer": "The brutal economics comparison ➔"
    },
    {
        "num": 3,
        "badge": "THE ECONOMIC AUDIT",
        "badge_color": "emerald",
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
            {"step": "03", "name": "Context Angle Synthesis", "desc": "Gemini 1.5 Flash writes custom 60-word pitch tied to trigger.", "tag": "No Templates"},
            {"step": "04", "name": "Inbox Cadence Dispatch", "desc": "Sent from warm secondary domains directly to primary inbox.", "tag": "99.2% SLA"}
        ],
        "footer": "Get your first 20 leads ➔"
    },
    {
        "num": 5,
        "badge": "START QUALIFYING",
        "badge_color": "emerald",
        "headline": "Want 20 Verified ICP Leads <span>Qualified on Intent?</span>",
        "body": "Tell me your B2B ICP (Job Title, Industry, Target Tech Stack).<br><br>Vance will run an autonomous intent scan and deliver <b>20 verified high-intent leads with personalized hooks</b> directly to your inbox.<br><br>👉 <b>DM 'VANCE'</b> or test the engine live:",
        "cta_button": "usevance.com",
        "author": "Mangal Soren • Founder & AI GTM Architect",
        "footer": "Save this post for your outbound playbook"
    }
]

def generate_html_slide(slide):
    badge_colors = {
        "emerald": ("#ecfdf5", "#047857", "#10b981", "#a7f3d0"),
        "indigo": ("#eef2ff", "#4338ca", "#6366f1", "#c7d2fe"),
        "cyan": ("#ecfeff", "#0e7490", "#06b6d4", "#a5f3fc"),
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
                <div class="comp-label" style="color: #047857;">{v['title']}</div>
                <div class="comp-cost" style="color: #059669;">{v['cost']}</div>
                <div class="comp-rate" style="color: #0f172a;">{v['rate']}</div>
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
            background: #ffffff;
            font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
            color: #0f172a;
            position: relative;
        }}
        .canvas {{
            width: 1080px;
            height: 1350px;
            padding: 90px 80px 70px 80px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            background: #fafaf9;
            background-image: radial-gradient(rgba(148, 163, 184, 0.15) 1px, transparent 1px);
            background-size: 28px 28px;
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
            box-shadow: 0 0 10px {dot_color};
        }}
        .slide-counter {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 26px;
            font-weight: 800;
            color: #94a3b8;
        }}
        .headline {{
            font-size: 64px;
            font-weight: 900;
            line-height: 1.15;
            letter-spacing: -0.04em;
            color: #0f172a;
            margin: 30px 0;
        }}
        .headline span {{
            color: #059669;
            text-decoration: underline;
            text-decoration-color: #a7f3d0;
            text-underline-offset: 8px;
        }}
        .main-body {{
            font-size: 34px;
            color: #334155;
            font-weight: 500;
            line-height: 1.55;
            margin-top: 20px;
        }}
        .main-body b {{
            color: #0f172a;
            font-weight: 800;
        }}
        .trigger-card {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 22px;
            padding: 24px 32px;
            margin-bottom: 20px;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03);
        }}
        .trigger-top {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        }}
        .trigger-cat {{
            font-size: 24px;
            font-weight: 800;
            letter-spacing: 0.04em;
            text-transform: uppercase;
        }}
        .trigger-code {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 20px;
            font-weight: 800;
            color: #94a3b8;
            background: #f1f5f9;
            padding: 4px 12px;
            border-radius: 8px;
        }}
        .trigger-desc {{
            font-size: 24px;
            color: #475569;
            font-weight: 600;
            line-height: 1.4;
        }}
        .comp-grid {{
            display: flex;
            flex-direction: column;
            gap: 24px;
        }}
        .comp-card {{
            border-radius: 28px;
            padding: 34px 40px;
            background: #ffffff;
            border: 2px solid #e2e8f0;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.04);
        }}
        .comp-card.bad {{
            background: #fff5f5;
            border-color: #fecdd3;
        }}
        .comp-card.good {{
            background: #f0fdf4;
            border-color: #bbf7d0;
            box-shadow: 0 10px 30px rgba(5, 150, 105, 0.08);
        }}
        .comp-label {{
            font-size: 22px;
            font-weight: 800;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            color: #64748b;
            margin-bottom: 10px;
        }}
        .comp-cost {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 58px;
            font-weight: 900;
            color: #e11d48;
            margin-bottom: 6px;
        }}
        .comp-rate {{
            font-size: 28px;
            color: #334155;
            font-weight: 800;
            margin-bottom: 10px;
        }}
        .comp-sub {{
            font-size: 24px;
            color: #64748b;
            font-weight: 600;
            margin-bottom: 14px;
        }}
        .comp-badge {{
            display: inline-block;
            font-size: 20px;
            font-weight: 800;
            padding: 6px 18px;
            border-radius: 10px;
        }}
        .bad-badge {{ background: #ffe4e6; color: #be123c; }}
        .good-badge {{ background: #dcfce7; color: #15803d; }}
        .pipe-card {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 22px;
            padding: 24px 30px;
            display: flex;
            align-items: center;
            gap: 24px;
            margin-bottom: 20px;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03);
        }}
        .pipe-num {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 32px;
            font-weight: 900;
            color: #059669;
        }}
        .pipe-info {{ flex: 1; }}
        .pipe-name {{
            font-size: 28px;
            font-weight: 800;
            color: #0f172a;
            margin-bottom: 6px;
        }}
        .pipe-desc {{
            font-size: 22px;
            color: #64748b;
            font-weight: 500;
        }}
        .pipe-tag {{
            font-family: 'JetBrains Mono', monospace;
            background: #ecfdf5;
            color: #047857;
            border: 1px solid #a7f3d0;
            padding: 8px 16px;
            border-radius: 10px;
            font-size: 20px;
            font-weight: 800;
        }}
        .cta-btn {{
            display: inline-block;
            background: #0f172a;
            color: #ffffff;
            font-size: 38px;
            font-weight: 800;
            padding: 24px 52px;
            border-radius: 999px;
            font-family: 'JetBrains Mono', monospace;
            margin: 34px 0 24px 0;
            box-shadow: 0 10px 30px rgba(15, 23, 42, 0.2);
        }}
        .author-tag {{
            font-size: 26px;
            color: #64748b;
            font-weight: 700;
        }}
        .footer-row {{
            border-top: 2px solid #e2e8f0;
            padding-top: 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .brand-name {{
            font-size: 24px;
            font-weight: 800;
            letter-spacing: 0.05em;
            color: #94a3b8;
        }}
        .footer-text {{
            font-size: 24px;
            font-weight: 800;
            color: #059669;
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
    print("🎨 Rendering 5 Vance Light-Theme Slides to 1080x1350 PNG...")
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

INSTA_CAPTION = \"\"\"Most B2B founders burn $4,000 to $6,000/mo hiring human SDRs to spray 50 generic cold emails a day. 

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

#aisdr #b2bsaas #growtharchitecture #coldoutreach #speedtolead #gtmstrategy #salesautomation #usevance\"\"\"

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
                "caption": "📊 <b>VANCE AI • Slide 1/5: The 23 Buying Triggers That Replace a $4,000/mo Human SDR</b>\n\n👉 <i>Swipe right to see all 5 slides. Save to Photos & upload directly to Instagram!</i>" if i == 1 else "",
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
        caption_pdf = "📑 <b>Vance AI • 5-Slide B2B Swipeable PDF (LinkedIn Ready)</b>\n\n📌 <b>Topic:</b> The 23 Buying Triggers That Replace a $4,000/mo Human SDR\n\n👉 <b>LinkedIn Post:</b> Upload this PDF as a 'Document' post ➔ LinkedIn renders it as an interactive carousel!\n🔗 <b>CTA:</b> usevance.com"
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
            "Asset Type": "5-Slide PDF & PNG Carousel (Light Mode)",
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
    print("\n🎉 Vance Carousel generated, compiled to PDF, sent to Telegram, and saved in NocoDB!")

if __name__ == "__main__":
    main()
