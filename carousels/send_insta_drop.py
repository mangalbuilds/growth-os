#!/usr/bin/env python3
"""
Send Vance Carousel 5 PNG Slides Album + Ready-to-Copy Instagram Caption & Hashtags to Telegram.
"""

import os
import sys
import json
import urllib.request
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import env_loader

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
CHAT_ID = os.getenv("VANCE_TELEGRAM_CHAT_ID", "-1003882353811")  # Dedicated Vance Supergroup
DIR = Path("/Users/mangal777/Mangal/growth_engine/carousels/vance_deck")

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

#aisdr #b2bsaas #growtharchitecture #coldoutreach #speedtolead #gtmstrategy #salesautomation #usevance
"""

def send_album():
    print("📸 Sending 5 PNG slides album to Telegram...")
    boundary = "----WebKitFormBoundaryMediaGroupVance"
    data = []

    # chat_id
    data.append(f"--{boundary}".encode())
    data.append(b'Content-Disposition: form-data; name="chat_id"\r\n')
    data.append(CHAT_ID.encode())

    # media array
    media_items = []
    for i in range(1, 6):
        media_items.append({
            "type": "photo",
            "media": f"attach://slide_{i}",
            "caption": "📊 <b>VANCE AI • Slide 1/5: The 23 Buying Triggers That Replace a $4,000/mo Human SDR</b>\n\n👉 <i>Swipe right to see all 5 slides. Save to Photos & upload directly to Instagram!</i>" if i == 1 else "",
            "parse_mode": "HTML"
        })

    data.append(f"--{boundary}".encode())
    data.append(b'Content-Disposition: form-data; name="media"\r\n')
    data.append(json.dumps(media_items).encode("utf-8"))

    # attach 5 png files
    for i in range(1, 6):
        file_path = DIR / f"slide_{i}.png"
        data.append(f"--{boundary}".encode())
        data.append(f'Content-Disposition: form-data; name="slide_{i}"; filename="slide_{i}.png"\r\nContent-Type: image/png\r\n'.encode())
        with open(file_path, "rb") as f:
            data.append(f.read())

    data.append(f"--{boundary}--\r\n".encode())

    req = urllib.request.Request(
        f"https://api.telegram.org/bot{TOKEN}/sendMediaGroup",
        data=b"\r\n".join(data),
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
        method="POST"
    )

    with urllib.request.urlopen(req, timeout=40) as resp:
        res = json.loads(resp.read().decode())
        print("  ✅ 5 PNG Slides sent as Telegram Album! Result:", res.get("ok"))

def send_copy_paste_caption():
    print("\n📝 Sending Copy-Paste Instagram Caption & Hashtags...")
    msg_text = (
        "📋 <b>INSTAGRAM POST CAPTION (1-Tap Copy & Paste)</b>\n"
        "────────────────────────\n\n"
        f"{INSTA_CAPTION}\n\n"
        "────────────────────────\n"
        "💡 <b>Posting Checklist:</b>\n"
        "1. Open Instagram ➔ Tap '+' ➔ Select Carousel (select the 5 PNGs in order 1 to 5).\n"
        "2. Paste the exact caption above.\n"
        "3. Add Location: 'San Francisco, California' or 'New York' (B2B SaaS algorithm boost)."
    )

    payload = json.dumps({
        "chat_id": CHAT_ID,
        "text": msg_text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }).encode("utf-8")

    req = urllib.request.Request(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(req, timeout=20) as resp:
        res = json.loads(resp.read().decode())
        print("  ✅ Caption & Hashtags message sent to Telegram! Result:", res.get("ok"))

if __name__ == "__main__":
    send_album()
    send_copy_paste_caption()
