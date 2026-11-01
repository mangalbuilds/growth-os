#!/usr/bin/env python3
"""
📅 GTM Outreach Hacker Content Dispatcher & Telegram Approver
Automates the daily content drops for TrackKaro AI & Jarvis AI SDR:
- Pushes today's pre-formatted caption & hashtags to Telegram
- Automatically attaches the rendered video or carousel PDF
- Allows 1-Tap copy & approval directly from phone
- Syncs with NocoDB Content Assets Table
"""

import os
import sys
import json
import argparse
import urllib.request
from datetime import datetime
from pathlib import Path

TELEGRAM_BOT_TOKEN = "8445264349:AAFWHjaQe9Qomf2Zwm7MVV_6NkhRmGWLMjs"
TELEGRAM_CHAT_ID = "-5489183481"

NOCO_URL = "https://crm.trackkaroai.com"
NOCO_TOKEN = "nc_pat_gPoul6APyQs7Qr77wz3VI6AmaqaXrNg8OipLKIsu"
NOCO_CONTENT_TABLE = "m0d70xh1eo1f6uh"

BASE_DIR = Path("/Users/mangal777/Mangal/growth_engine")
REELS_DIR = BASE_DIR / "reels"
CAROUSELS_DIR = BASE_DIR / "carousels" / "speed_to_lead_deck"

SCHEDULE = {
    "monday": {
        "day_name": "Monday",
        "product": "TrackKaro AI",
        "platform": "Instagram Reels & X (Twitter)",
        "format": "🎬 9:16 Video Reel",
        "best_time": "07:30 PM IST",
        "media_type": "video",
        "media_path": REELS_DIR / "trackkaro_speed_to_lead_9x16.mp4",
        "hook": "Why 78% of High-Ticket Meta Ad Leads Never Answer Their Phone",
        "caption": """If your sales team takes more than 5 minutes to call an ad lead, you are burning 80% of your ad budget.

While traditional reps wait 4 hours to open a spreadsheet, TrackKaro AI delivers an interactive WhatsApp brochure in 8 seconds and rings the sales rep in 14.8 seconds.

Want to test your team's real response time? Comment AUDIT and I'll run a free 60-second speed test on your funnel.

#speedtolead #b2bgrowth #salesautomation #gtmengineering #metaads #trackkaroai"""
    },
    "tuesday": {
        "day_name": "Tuesday",
        "product": "TrackKaro AI",
        "platform": "LinkedIn & Instagram Carousel",
        "format": "📊 5-Slide Swipeable Carousel",
        "best_time": "07:30 PM IST",
        "media_type": "document",
        "media_path": CAROUSELS_DIR / "TrackKaro_Speed_To_Lead_Carousel.pdf",
        "hook": "The Brutal Math of Speed-to-Lead (Swipe ➡️)",
        "caption": """Most high-ticket agencies and luxury real estate teams spend $10,000+ on Meta ads, only to let their sales reps call leads 4 hours later.

In this 5-slide breakdown, I map out:
1. The exact mathematical dropoff curve (0-15s vs 5m vs 4h)
2. The autonomous webhook architecture that eliminates lead decay
3. Real benchmark: How a Dubai luxury team jumped from 4.1% to 22.6% bookings

Swipe through the slides ➡️

PS: Want to know your actual response time? Drop a comment or DM "AUDIT" — I’ll run a free 60-second speed-to-lead test on your funnel.

#b2bsales #cro #realestatemarketing #leadgeneration #gtmstrategy"""
    },
    "wednesday": {
        "day_name": "Wednesday",
        "product": "TrackKaro AI",
        "platform": "Instagram & LinkedIn Infographic",
        "format": "🖼️ System Architecture Blueprint",
        "best_time": "08:00 PM IST",
        "media_type": "photo",
        "media_path": CAROUSELS_DIR / "slide_3.png",
        "hook": "How to Build a Sub-15s Lead Response System With Zero Human Delay",
        "caption": """Modern high-ticket sales isn't about hiring more SDRs to sit on spreadsheets. It's about engineering instantaneous dispatch.

Here is the architecture we use at TrackKaro:
⚡ 0.2s: Webhook payload captured
⚡ 8.4s: WhatsApp pricing asset delivered to buyer
⚡ 12.1s: Telegram audio alert wakes sales rep
⚡ 14.8s: Lead intent scored & logged in NocoDB

Drop a comment if you want the webhook blueprint.

#systemdesign #gtmarchitect #aiagents #nocodb #automation"""
    },
    "thursday": {
        "day_name": "Thursday",
        "product": "Vance AI SDR",
        "platform": "Reddit (r/coldemail & r/SaaS) & Instagram",
        "format": "📝 High-Authority Teardown / Case Study",
        "best_time": "04:30 PM IST",
        "media_type": "none",
        "media_path": None,
        "hook": "How Custom Domain Isolation & Vance Local AI SDR Fixed Our Reply Rates",
        "caption": """I ran into the traditional cold email trap 6 months ago: paying $4,000/mo for SDRs who scrape messy lists and send generic templates that hit spam.

What fixed it for us was building an isolated local AI SDR engine (Vance):
• Scrapes intent queries via Google Serper
• Enriches verified emails through waterfall validation
• Generates 35-word experience-grammar pitches via Gemini Flash
• Lets me approve and queue 20 personalized pitches from my phone in 2 minutes via Tailscale

(Full disclosure: I built Vance as our internal prospecting engine).

Happy to share how we solved mailbox deliverability and workspace isolation if anyone is struggling with reply rates."""
    },
    "friday": {
        "day_name": "Friday",
        "product": "TrackKaro AI",
        "platform": "Instagram & X (Twitter)",
        "format": "🖼️ High-Contrast Reality Check",
        "best_time": "07:00 PM IST",
        "media_type": "photo",
        "media_path": CAROUSELS_DIR / "slide_2.png",
        "hook": "You Don't Have a Lead Problem. You Have a Speed Problem.",
        "caption": """If you spend $10,000 on paid ads but take 4 hours to call your leads, you don't have a lead problem.

You have a speed problem.

Lead intent has a half-life of 5 minutes. After 15 minutes, you are calling a stranger who forgot they even filled your form.

Fix the speed first. Then scale the ad spend.

#leadgeneration #gtmstrategy #salesleadership #marketingroi"""
    },
    "saturday": {
        "day_name": "Saturday",
        "product": "Mangal HQ (AI PM / Growth Engineer)",
        "platform": "LinkedIn & X (Twitter)",
        "format": "🚀 Proof-of-Work Build In Public",
        "best_time": "06:30 PM IST",
        "media_type": "none",
        "media_path": None,
        "hook": "Why I Stopped Applying to Jobs With Resumes and Built Autonomous GTM Systems Instead",
        "caption": """Most people apply to 500 tech roles through LinkedIn 'Easy Apply' and wonder why they get 0 interviews.

Instead of submitting PDF resumes, I spent the last 4 months building production systems:
1. TrackKaro AI: Sub-15s webhook speed-to-lead nervous system
2. Jarvis AI SDR: Multi-workspace prospecting engine running locally from my MacBook
3. Autonomous Job Hunter Copilot: Scraping Serper + Gemini Flash scoring + real-time Telegram alerts

If you are a founder looking for an AI Product Manager or Growth Engineer who builds systems that drive revenue, let's connect.

#buildinpublic #aiproductmanager #growthengineer #gtmengineering"""
    }
}

def dispatch_telegram_alert(day_key):
    item = SCHEDULE.get(day_key.lower())
    if not item:
        print(f"❌ Unknown day '{day_key}'. Available: {list(SCHEDULE.keys())}")
        return False

    print(f"🚀 Preparing GTM Content Drop for: {item['day_name']} ({item['product']})...")
    
    clean_caption = item['caption'].replace("<", "&lt;").replace(">", "&gt;")
    
    text = (
        f"🎯 <b>[GTM HACKER DROP: {item['day_name'].upper()}]</b>\n\n"
        f"🏷️ <b>Product:</b> {item['product']}\n"
        f"🌐 <b>Target Platform:</b> {item['platform']}\n"
        f"📦 <b>Format:</b> {item['format']}\n"
        f"⏰ <b>Best Time to Post:</b> {item['best_time']}\n\n"
        f"💡 <b>Post Title / Hook:</b>\n<i>{item['hook']}</i>\n\n"
        f"📝 <b>Caption (Tap to copy):</b>\n"
        f"<code>{clean_caption}</code>\n\n"
        f"<i>👉 Review media attached below, copy caption, and upload in 30 seconds!</i>"
    )
    
    # 1. Send the text notification
    msg_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = json.dumps({
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }).encode()
    
    req = urllib.request.Request(msg_url, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        print("  ✓ Text alert & copyable caption sent to Telegram!")

    # 2. Send media if exists
    m_type = item.get("media_type")
    m_path = item.get("media_path")
    
    if m_path and Path(m_path).is_file():
        boundary = "----WebKitFormBoundaryMediaUpload"
        data = []
        data.append(f"--{boundary}".encode())
        data.append(b'Content-Disposition: form-data; name="chat_id"\r\n')
        data.append(TELEGRAM_CHAT_ID.encode())
        
        endpoint = "sendPhoto" if m_type == "photo" else ("sendVideo" if m_type == "video" else "sendDocument")
        field_name = "photo" if m_type == "photo" else ("video" if m_type == "video" else "document")
        content_type = "image/png" if m_type == "photo" else ("video/mp4" if m_type == "video" else "application/pdf")
        
        data.append(f"--{boundary}".encode())
        data.append(f'Content-Disposition: form-data; name="{field_name}"; filename="{m_path.name}"\r\nContent-Type: {content_type}\r\n'.encode())
        with open(m_path, "rb") as f:
            data.append(f.read())
        data.append(f"--{boundary}--\r\n".encode())
        
        media_req = urllib.request.Request(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/{endpoint}",
            data=b"\r\n".join(data),
            headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
            method="POST"
        )
        with urllib.request.urlopen(media_req) as resp:
            print(f"  ✓ Attached {m_type} file sent to phone!")
            
    print(f"✅ GTM Content drop for {item['day_name']} successfully dispatched to Telegram!")
    return True

def main():
    parser = argparse.ArgumentParser(description="GTM Outreach Hacker Content Calendar")
    parser.add_argument("--day", "-d", help="Day of the week (monday, tuesday, wednesday, thursday, friday, saturday)")
    parser.add_argument("--today", action="store_true", help="Send today's scheduled content drop to Telegram")
    parser.add_argument("--list", action="store_true", help="List all scheduled weekly content drops")
    
    args = parser.parse_args()
    
    if args.list:
        print("\n📅 Weekly GTM Hacker Timetable:")
        for d, item in SCHEDULE.items():
            print(f"  • {item['day_name'].upper()}: [{item['product']}] {item['platform']} — {item['format']} ({item['best_time']})")
        return
        
    if args.day:
        dispatch_telegram_alert(args.day.lower())
    elif args.today or len(sys.argv) == 1:
        # Detect current day
        day_str = datetime.now().strftime("%A").lower()
        if day_str == "sunday":
            day_str = "monday"
        print(f"📆 Today is: {day_str.capitalize()}")
        dispatch_telegram_alert(day_str)

if __name__ == "__main__":
    main()
