#!/usr/bin/env python3
"""
🎨 Programmatic High-Ticket B2B Carousel Generator
Generates:
1. 1080x1350 High-Res PNG Slides (for Instagram, Twitter & LinkedIn Images)
2. Interactive Swipeable PDF Document (for LinkedIn Carousel Posts)
3. Direct Telegram Push to Phone
4. Auto-logging into NocoDB Content Assets Table
"""

import os
import sys
import json
import subprocess
import urllib.request
from pathlib import Path
from PIL import Image

CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUTPUT_DIR = Path("/Users/mangal777/Mangal/growth_engine/carousels/speed_to_lead_deck")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TELEGRAM_BOT_TOKEN = "8445264349:AAFWHjaQe9Qomf2Zwm7MVV_6NkhRmGWLMjs"
TELEGRAM_CHAT_ID = "-5489183481"

NOCO_URL = "https://crm.trackkaroai.com"
NOCO_TOKEN = "nc_pat_gPoul6APyQs7Qr77wz3VI6AmaqaXrNg8OipLKIsu"
NOCO_CONTENT_TABLE = "m0d70xh1eo1f6uh"

SLIDES_DATA = [
    {
        "num": 1,
        "badge": "B2B GROWTH ARCHITECTURE",
        "badge_color": "emerald",
        "headline": "Why 78% of High-Ticket Ad Leads Ghost You in <span>5 Minutes</span>",
        "body": "Most luxury real estate agencies and aesthetic clinics spend $10,000+ on Meta ads, only to let their sales reps call leads 4 hours later.<br><br>Here is the exact 15-second nervous system that fixes lead decay forever.",
        "footer": "Swipe to see the math ➔"
    },
    {
        "num": 2,
        "badge": "LEAD DECAY MATHEMATICS",
        "badge_color": "rose",
        "headline": "The Brutal Math of <span>Speed-to-Lead</span>",
        "content_type": "stats",
        "stats": [
            {"time": "0 - 15 SECONDS", "val": "+391% Conversion", "note": "Buyer is still looking at their phone. Intent is peak.", "color": "#10b981"},
            {"time": "5 MINUTES", "val": "-80% Response Drop", "note": "They closed Instagram and opened an email or work tab.", "color": "#f59e0b"},
            {"time": "4 HOURS", "val": "❌ 94% Ghost Rate", "note": "Lead already booked a consultation with a faster competitor.", "color": "#f43f5e"}
        ],
        "footer": "The fastest team wins ➔"
    },
    {
        "num": 3,
        "badge": "SYSTEM BLUEPRINT",
        "badge_color": "cyan",
        "headline": "The TrackKaro AI <span>Nervous System</span>",
        "content_type": "pipeline",
        "steps": [
            {"step": "01", "name": "Ad Form Submission", "desc": "Meta / Google Webhook captures intent in real-time.", "tag": "0.2s"},
            {"step": "02", "name": "Instant WhatsApp Asset", "desc": "Interactive brochure & personalized pricing PDF delivered.", "tag": "8.4s"},
            {"step": "03", "name": "Telegram Audio Rep Alert", "desc": "Sales rep gets a sound alert + 1-tap call button.", "tag": "12.1s"},
            {"step": "04", "name": "Autonomous CRM Sync", "desc": "Lead intent scored and logged directly to NocoDB / Supabase.", "tag": "14.8s"}
        ],
        "footer": "Real-world benchmark ➔"
    },
    {
        "num": 4,
        "badge": "REAL CASE STUDY",
        "badge_color": "emerald",
        "headline": "Dubai Luxury Real Estate <span>Benchmark</span>",
        "content_type": "case_study",
        "before": {
            "title": "TRADITIONAL AGENCY",
            "time": "4.2 Hours",
            "rate": "4.1% Booking Rate",
            "status": "$14,000 ad spend wasted"
        },
        "after": {
            "title": "WITH TRACKKARO AI",
            "time": "14.8 Seconds",
            "rate": "22.6% Booking Rate",
            "status": "3.8x High-ticket deals closed"
        },
        "footer": "How to implement this ➔"
    },
    {
        "num": 5,
        "badge": "NEXT ACTION",
        "badge_color": "emerald",
        "headline": "Want to Audit Your <span>Response Time?</span>",
        "body": "If you are running paid ads for high-ticket clients, I'll run a <b>Free 60-Second Speed-to-Lead Audit</b> on your funnel.<br><br>I will submit a test lead and show you the exact seconds of delay before your team responds.",
        "cta_button": "trackkaroai.com",
        "author": "Mangal Soren • Founder & AI GTM Architect",
        "footer": "Share this with a founder who runs ads"
    }
]

def generate_html_slide(slide):
    badge_colors = {
        "emerald": ("rgba(16, 185, 129, 0.15)", "#34d399", "#10b981"),
        "rose": ("rgba(244, 63, 94, 0.15)", "#fb7185", "#f43f5e"),
        "cyan": ("rgba(6, 182, 212, 0.15)", "#38bdf8", "#06b6d4"),
    }
    bg_pill, text_pill, dot_color = badge_colors.get(slide.get("badge_color", "emerald"))

    content_html = ""
    c_type = slide.get("content_type", "default")
    
    if c_type == "stats":
        for s in slide["stats"]:
            content_html += f"""
            <div class="stat-card" style="border-left: 6px solid {s['color']};">
                <div class="stat-header">
                    <span class="stat-time">{s['time']}</span>
                    <span class="stat-val" style="color: {s['color']};">{s['val']}</span>
                </div>
                <div class="stat-note">{s['note']}</div>
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
    elif c_type == "case_study":
        b = slide["before"]
        a = slide["after"]
        content_html = f"""
        <div class="case-grid">
            <div class="case-card bad">
                <div class="case-label">{b['title']}</div>
                <div class="case-stat">{b['time']}</div>
                <div class="case-sub">{b['rate']}</div>
                <div class="case-badge red">{b['status']}</div>
            </div>
            <div class="case-card good">
                <div class="case-label">{a['title']}</div>
                <div class="case-stat" style="color: #34d399;">{a['time']}</div>
                <div class="case-sub">{a['rate']}</div>
                <div class="case-badge green">{a['status']}</div>
            </div>
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
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800;900&family=JetBrains+Mono:wght@600;800&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            width: 1080px;
            height: 1350px;
            overflow: hidden;
            background: #080a10;
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
            background: radial-gradient(circle at 80% 15%, rgba(16, 185, 129, 0.12) 0%, transparent 60%),
                        radial-gradient(circle at 20% 85%, rgba(6, 182, 212, 0.08) 0%, transparent 55%),
                        #080a10;
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
            border: 1px solid rgba(255, 255, 255, 0.1);
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
            box-shadow: 0 0 12px {dot_color};
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
            margin: 30px 0;
        }}
        .headline span {{
            background: linear-gradient(135deg, #10b981 0%, #06b6d4 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .main-body {{
            font-size: 34px;
            color: #cbd5e1;
            font-weight: 600;
            line-height: 1.5;
            margin-top: 20px;
        }}
        .stat-card {{
            background: rgba(18, 22, 34, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 24px;
            padding: 32px 36px;
            margin-bottom: 24px;
        }}
        .stat-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
        }}
        .stat-time {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 26px;
            font-weight: 800;
            color: #94a3b8;
        }}
        .stat-val {{
            font-size: 34px;
            font-weight: 900;
        }}
        .stat-note {{
            font-size: 26px;
            color: #cbd5e1;
            font-weight: 500;
        }}
        .pipe-card {{
            background: rgba(18, 22, 34, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 24px 30px;
            display: flex;
            align-items: center;
            gap: 24px;
            margin-bottom: 20px;
        }}
        .pipe-num {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 32px;
            font-weight: 900;
            color: #10b981;
        }}
        .pipe-info {{ flex: 1; }}
        .pipe-name {{
            font-size: 28px;
            font-weight: 800;
            margin-bottom: 6px;
        }}
        .pipe-desc {{
            font-size: 22px;
            color: #94a3b8;
            font-weight: 500;
        }}
        .pipe-tag {{
            font-family: 'JetBrains Mono', monospace;
            background: rgba(16, 185, 129, 0.15);
            color: #34d399;
            padding: 8px 16px;
            border-radius: 10px;
            font-size: 22px;
            font-weight: 800;
        }}
        .case-grid {{
            display: flex;
            flex-direction: column;
            gap: 24px;
        }}
        .case-card {{
            border-radius: 28px;
            padding: 36px 40px;
            border: 2px solid rgba(255, 255, 255, 0.08);
        }}
        .case-card.bad {{
            background: rgba(244, 63, 94, 0.08);
            border-color: rgba(244, 63, 94, 0.3);
        }}
        .case-card.good {{
            background: rgba(16, 185, 129, 0.08);
            border-color: rgba(16, 185, 129, 0.4);
        }}
        .case-label {{
            font-size: 24px;
            font-weight: 800;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            color: #94a3b8;
            margin-bottom: 12px;
        }}
        .case-stat {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 64px;
            font-weight: 900;
            margin-bottom: 8px;
        }}
        .case-sub {{
            font-size: 26px;
            color: #cbd5e1;
            font-weight: 700;
            margin-bottom: 12px;
        }}
        .case-badge {{
            display: inline-block;
            font-size: 22px;
            font-weight: 800;
            padding: 6px 18px;
            border-radius: 10px;
        }}
        .case-badge.red {{ background: rgba(244, 63, 94, 0.2); color: #fb7185; }}
        .case-badge.green {{ background: rgba(16, 185, 129, 0.2); color: #34d399; }}
        .cta-btn {{
            display: inline-block;
            background: linear-gradient(135deg, #10b981 0%, #06b6d4 100%);
            color: #06080d;
            font-size: 38px;
            font-weight: 900;
            padding: 24px 50px;
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
            <div class="brand-name">TRACKKARO AI • SPEED-TO-LEAD</div>
            <div class="footer-text">{slide['footer']}</div>
        </div>
    </div>
</body>
</html>"""
    return html

def render_slides_to_png():
    print("🎨 Rendering 5 Carousel Slides to 1080x1350 PNG...")
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
    pdf_path = OUTPUT_DIR / "TrackKaro_Speed_To_Lead_Carousel.pdf"
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

TRACKKARO_INSTA_CAPTION = \"\"\"78% of high-ticket B2B leads ghost you if you don't respond in the first 5 minutes. 📉

Most luxury agencies and clinics spend $10,000+ on Meta ads, only to let their sales reps call leads 4 hours later.

By then? The buyer closed Instagram, went back to work, or already booked a call with a faster competitor.

⚡ The Sub-15s TrackKaro Nervous System:
1️⃣ Ad Form Submitted ➔ Captured via instant webhook (0.2s)
2️⃣ Personalized Asset Delivered ➔ WhatsApp brochure & pricing sent (8.4s)
3️⃣ Sales Rep Alerted ➔ Telegram sound alert + 1-tap call button (12.1s)
4️⃣ Autonomous CRM Sync ➔ Lead scored and synced to CRM (14.8s)

Stop burning ad spend. Speed to lead is the only moat left in high-ticket sales.

👉 Want to test your team's response time?
Comment "AUDIT" below or visit trackkaroai.com (link in bio) for a Free 60-Second Speed-to-Lead Audit.

#speedtolead #salesautomation #inboundmarketing #leadconversion #trackkaroai #b2bgrowth #agencygrowth\"\"\"

def send_to_telegram(pdf_path, png_paths):
    print("\n📲 Sending TrackKaro Carousel Assets to Telegram...")
    
    # 1. Send all 5 PNG slides as a native Instagram Album
    print("  📸 Uploading 5 PNG slides album for Instagram...")
    try:
        boundary_album = "----WebKitFormBoundaryAlbumTrackkaro"
        album_data = []
        album_data.append(f"--{boundary_album}".encode())
        album_data.append(b'Content-Disposition: form-data; name="chat_id"\r\n')
        album_data.append(TELEGRAM_CHAT_ID.encode())
        
        media_items = []
        for i in range(1, len(png_paths) + 1):
            media_items.append({
                "type": "photo",
                "media": f"attach://slide_{i}",
                "caption": "📊 <b>TrackKaro AI • Slide 1/5: Why 78% of High-Ticket Leads Ghost You</b>\n\n👉 <i>Swipe right to see all 5 slides. Save to Photos & upload directly to Instagram!</i>" if i == 1 else "",
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
            f"{TRACKKARO_INSTA_CAPTION}\n\n"
            "────────────────────────\n"
            "💡 <b>Instagram Posting Tips:</b>\n"
            "1. Open Instagram ➔ Tap '+' ➔ Select the 5 saved PNGs (Order 1 to 5).\n"
            "2. Paste this exact caption.\n"
            "3. Add Location: 'Dubai, United Arab Emirates' or 'Miami, Florida' for high-ticket agency reach."
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
        caption_pdf = "📑 <b>TrackKaro AI • 5-Slide B2B Swipeable PDF (LinkedIn Ready)</b>\n\n📌 <b>Topic:</b> Why 78% of High-Ticket Ad Leads Ghost You in 5 Minutes\n\n👉 <b>LinkedIn Post:</b> Upload this PDF as a 'Document' post ➔ LinkedIn renders it as an interactive carousel!\n🔗 <b>CTA:</b> trackkaroai.com"
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
            print("  ✅ Sent TrackKaro Carousel PDF to Telegram!")
    except Exception as e:
        print(f"  ⚠️ Telegram PDF error: {e}")

def log_to_nocodb(pdf_path):
    print("\n🌐 Logging Carousel to NocoDB Content Assets Table...")
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
            "Project": "trackkaro",
            "Target Platform": "LinkedIn & Instagram Carousel",
            "Asset Type": "5-Slide PDF & PNG Carousel",
            "Hook / Title": "Why 78% of High-Ticket Ad Leads Ghost You in 5 Minutes",
            "Script / Prompt / Code": f"PDF: {pdf_path.name}\n5 Slides: Math of Decay, TrackKaro Webhook Nervous System, Dubai Real Estate Case Study, 60s Free Audit.",
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
    print("\n🎉 All Done! Carousel generated, compiled to PDF, sent to Telegram, and saved in NocoDB!")

if __name__ == "__main__":
    main()
