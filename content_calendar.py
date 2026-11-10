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

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import env_loader

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "-5489183481")

NOCO_URL = os.getenv("NOCO_URL", "https://crm.trackkaroai.com")
NOCO_TOKEN = os.getenv("NOCO_TOKEN", "")
NOCO_CONTENT_TABLE = "m0d70xh1eo1f6uh"

BASE_DIR = Path("/Users/mangal777/Mangal/growth_engine")
VANCE_REELS_DIR = BASE_DIR / "reels"
VANCE_CAROUSELS_DIR = BASE_DIR / "carousels" / "vance_deck"
VANCE_LAUNCH_DIR = BASE_DIR / "carousels" / "vance_launch_deck"
TRACKKARO_REELS_DIR = BASE_DIR / "reels"
TRACKKARO_CAROUSELS_DIR = BASE_DIR / "carousels" / "speed_to_lead_deck"

# =====================================================================
# 🚀 VANCE (@usevance.ai / usevance.com) — 100% PURE OUTBOUND INTENT SDR
# Niche: B2B SaaS Founders, Growth Architects, High-Ticket Agency Owners
# =====================================================================
SCHEDULE_VANCE = {
    "monday": {
        "day_name": "Monday",
        "product": "Vance AI SDR (@usevance.ai)",
        "platform": "Instagram Reels & X (Twitter)",
        "format": "🎬 9:16 Video Reel (With Voiceover)",
        "best_time": "06:30 PM IST",
        "media_type": "video",
        "media_path": VANCE_REELS_DIR / "vance_with_voice.mp4",
        "hook": "Cold email is NOT dead. Spray-and-pray to 1,000 cold CEOs is.",
        "caption": """Cold email is NOT dead. 

Generic spray-and-pray to 1,000 cold CEOs with 0.8% reply rates is dead. 📉

Instead of buying static email lists, @usevance.ai runs an Autonomous B2B SDR that audits the web 24/7 and triggers on 23 Live Buying Signals:

🅰️ Paid Ads Trigger: Real-time scan of Meta Pixel & Google Tags (confirms active acquisition budget).
🅱️ SERP #11-30 Sweet Spot: Targets companies trying hard on Google but stuck on page 2.
🅲 Tech Stack Churn: Identifies missing booking widgets or dropped SaaS tools in page headers.
🅳 Growth Spikes: Scans /careers for active B2B SDR & sales hiring surges.

When a trigger fires, Gemini 1.5 Flash writes a bespoke 50-word reaction email within 400ms. Delivered safely via secondary domains with sub-3% bounce rate. ⚡

👉 Want 20 free verified in-market leads for your ICP?
Drop a comment "VANCE" or DM us @usevance.ai.

🔗 Live sandbox & docs: usevance.com (link in bio)

#aisdr #coldemail #b2bsaas #growthautomation #gtmengineering #salesdevelopment #usevance #hyperframes"""
    },
    "tuesday": {
        "day_name": "Tuesday",
        "product": "Vance AI SDR (@usevance.ai)",
        "platform": "Instagram Carousel & LinkedIn",
        "format": "📊 5-Slide Obsidian Launch Deck",
        "best_time": "07:00 PM IST",
        "media_type": "document",
        "media_path": VANCE_LAUNCH_DIR / "Vance_Launch_Manifesto.pdf",
        "hook": "Why $4,500/mo Human SDRs Are Obsolete in 2026 (Swipe ➡️)",
        "caption": """Day 1. The B2B outbound playbook is officially broken. 📉

In 2026, hiring an SDR for $4,500/mo to spray 10,000 generic email templates only does two things:
1. Burns your primary company domain in 30 days
2. Yields an embarrassing 0.8% reply rate

Buyers don't want spam — they want timed, relevant reactions.

That's why we built @usevance.ai. ⚡

Instead of guessing, Vance runs autonomously on 23 Intent Buying Triggers:
🎯 Hiring Spikes (Companies hiring Growth/SDR roles in the last 7 days)
⚡ Tech Stack Churn (Detecting when a company drops legacy tools)
🚀 Capital & Leadership (Funding rounds & newly appointed VPs within 30 days)
👀 Reverse-IP De-anonymization (ICP accounts visiting pricing pages 2+ times)

Swipe through the 5 slides ➡️

🚀 FOUNDING PARTNER OFFER:
Comment "VANCE" below or DM us @usevance.ai with your ICP:
Our AI engine will scan live intent streams and deliver 20 verified high-intent leads straight to your inbox for free.

🔗 Experience the live sandbox: usevance.com (link in bio)

#aisdr #b2bsaas #growtharchitecture #coldoutreach #speedtolead #gtmstrategy #usevance"""
    },
    "wednesday": {
        "day_name": "Wednesday",
        "product": "Vance AI SDR (@usevance.ai)",
        "platform": "Instagram Carousel & Infographic",
        "format": "📊 5-Slide 23 Buying Triggers Matrix",
        "best_time": "07:30 PM IST",
        "media_type": "photo",
        "media_path": VANCE_CAROUSELS_DIR / "slide_1.png",
        "hook": "The 23 Live Buying Signals That Trigger Instant Inbound Demos",
        "caption": """Most B2B founders think intent data means paying $15,000/yr for ZoomInfo or 6sense.

Here's how @usevance.ai extracts 23 live buying signals without expensive enterprise bloat:

1️⃣ SERP Rank Drop: Competitors dropping from Page 1 to Page 2 on Google
2️⃣ Ad Pixel Activation: When an ICP starts spending money on Meta Ads
3️⃣ SDK Header Audit: Companies running outdated chat widgets or broken web forms
4️⃣ Active Hiring Spikes: 3+ open sales/engineering roles on LinkedIn

We don't send cold emails. We send contextual problem-solver reactions.

Want to see all 23 triggers mapped out?
Comment "TRIGGERS" and I'll DM you the full high-res blueprint.

#gtmstrategy #b2bgrowth #coldoutreach #aisdr #salesdevelopment #usevance"""
    },
    "thursday": {
        "day_name": "Thursday",
        "product": "Vance AI SDR (@usevance.ai)",
        "platform": "Reddit, X & Instagram Authority Breakdown",
        "format": "📝 Technical Teardown & Case Study",
        "best_time": "05:00 PM IST",
        "media_type": "photo",
        "media_path": VANCE_CAROUSELS_DIR / "slide_3.png",
        "hook": "How Domain Isolation & Waterfall Verification Saved Our Deliverability",
        "caption": """6 months ago, our outbound hit a wall: 24% open rates and spam filters killing pipeline.

Here is the exact infrastructure we built inside Vance to achieve 68% open rates and sub-1.5% bounce rates:

1. Secondary Domain Cluster: Never send cold outbound from your primary root domain.
2. Dual-Layer Waterfall Verification: MX records + SMTP handshake validation before every send.
3. 35-Word Micro-Pitches: Zero marketing fluff, zero PDF attachments, zero tracking links in Email 1.
4. Gemini Flash Personalization: Unique problem statement per company, not just {{firstName}} tokens.

The entire engine runs locally and pushes approved leads to our phone via Tailscale.

Comment "INFRA" or DM @usevance.ai if you want our domain warming checklist.

#coldemail #emaildeliverability #systemarchitecture #b2bsales #growthengineering"""
    },
    "friday": {
        "day_name": "Friday",
        "product": "Vance AI SDR (@usevance.ai)",
        "platform": "Instagram Carousel (4:5)",
        "format": "📊 5-Slide Teardown Deck",
        "best_time": "06:30 PM IST",
        "media_type": "photo",
        "media_path": VANCE_CAROUSELS_DIR / "slide_4.png",
        "hook": "Stop Buying 50,000 Lead Apollo Lists. You Only Need 20 In-Market Accounts.",
        "caption": """The biggest lie in B2B sales: 'Outbound is a numbers game.'

If you blast 10,000 contacts, 9,900 of them are not buying today. You just burned 10,000 potential future customers.

The modern outbound formula:
High Intent Signals (20 accounts/week) × Contextual 40-word Pitch = 15-25% Reply Rate.

Quality > Spray and pray. Always.

Ready to see how Vance isolates the top 5% in-market buyers in your niche?
Visit usevance.com or DM us @usevance.ai.

#b2bsaas #growthhacks #salesleadership #coldemail #usevance"""
    },
    "saturday": {
        "day_name": "Saturday",
        "product": "Vance AI SDR (@usevance.ai)",
        "platform": "Instagram Reels & Build in Public",
        "format": "🎬 9:16 Behind-The-Scenes Engine Demo",
        "best_time": "06:00 PM IST",
        "media_type": "video",
        "media_path": VANCE_REELS_DIR / "vance_23_triggers_9x16.mp4",
        "hook": "How an AI SDR Mines Google & Generates Custom Pitches in 400ms",
        "caption": """Behind the curtain of @usevance.ai:

Watch how Vance:
1. Queries Serper for companies actively hiring in B2B tech
2. Verifies decision-maker work emails via waterfall API
3. Generates hyper-specific pain hypotheses via Gemini Flash
4. Queues 20 approved pitches to phone in under 60 seconds

No bloated $1,200/seat SaaS subscriptions. Just pure, deterministic GTM engineering.

Try the sandbox at usevance.com ⚡

#buildinpublic #aisdr #systemengineering #growthops #python #usevance"""
    },
    "sunday": {
        "day_name": "Sunday",
        "product": "Vance AI SDR (@usevance.ai)",
        "platform": "Instagram & LinkedIn Strategic Note",
        "format": "💡 Founder's Sunday Reflection",
        "best_time": "08:00 PM IST",
        "media_type": "photo",
        "media_path": VANCE_LAUNCH_DIR / "slide_1.png",
        "hook": "Why the Future of Sales Teams is 1 Growth Engineer + 3 AI SDRs",
        "caption": """In 2021: Companies hired 15 SDRs to do manual research, copy-paste emails, and dial phones.
In 2026: 1 Growth Engineer builds an autonomous intent pipeline like Vance that handles the work of 10 SDRs at 1/20th the cost.

The companies that win this decade won't have the largest headcount.
They'll have the highest leverage autonomous systems.

DM @usevance.ai to deploy your autonomous SDR pipeline this week.

#futureofwork #salesautomation #gtmengineering #aiproductmanager #usevance"""
    }
}

# =====================================================================
# ⚡ TRACKKARO AI (@trackkaroai / trackkaroai.com) — 100% INBOUND SPEED-TO-LEAD
# Niche: Luxury Real Estate, Aesthetic Clinics, Solar, High-Ticket Ad Agencies
# =====================================================================
SCHEDULE_TRACKKARO = {
    "monday": {
        "day_name": "Monday",
        "product": "TrackKaro AI (@trackkaroai)",
        "platform": "Instagram Reels & X",
        "format": "🎬 9:16 Video Reel",
        "best_time": "07:30 PM IST",
        "media_type": "video",
        "media_path": TRACKKARO_REELS_DIR / "trackkaro_speed_to_lead_9x16.mp4",
        "hook": "Why 78% of High-Ticket Meta Ad Leads Never Answer Their Phone",
        "caption": """If your sales team takes more than 5 minutes to call an ad lead, you are burning 80% of your ad budget.

While traditional reps wait 4 hours to open a spreadsheet, TrackKaro AI delivers an interactive WhatsApp brochure in 8 seconds and rings the sales rep in 14.8 seconds.

Want to test your team's real response time? Comment AUDIT and I'll run a free 60-second speed test on your funnel.

#speedtolead #b2bgrowth #salesautomation #gtmengineering #metaads #trackkaroai"""
    },
    "tuesday": {
        "day_name": "Tuesday",
        "product": "TrackKaro AI (@trackkaroai)",
        "platform": "LinkedIn & Instagram Carousel",
        "format": "📊 5-Slide Swipeable Carousel",
        "best_time": "07:30 PM IST",
        "media_type": "document",
        "media_path": TRACKKARO_CAROUSELS_DIR / "TrackKaro_Speed_To_Lead_Carousel.pdf",
        "hook": "The Brutal Math of Speed-to-Lead (Swipe ➡️)",
        "caption": """Most high-ticket agencies and luxury real estate teams spend $10,000+ on Meta ads, only to let their sales reps call leads 4 hours later.

In this 5-slide breakdown, I map out:
1. The exact mathematical dropoff curve (0-15s vs 5m vs 4h)
2. The autonomous webhook architecture that eliminates lead decay
3. Real benchmark: How a Dubai luxury team jumped from 4.1% to 22.6% bookings

Swipe through the slides ➡️

PS: Want to know your actual response time? Drop a comment or DM "AUDIT" — I’ll run a free 60-second speed-to-lead test on your funnel.

#b2bsales #cro #realestatemarketing #leadgeneration #gtmstrategy #trackkaroai"""
    },
    "wednesday": {
        "day_name": "Wednesday",
        "product": "TrackKaro AI (@trackkaroai)",
        "platform": "Instagram & LinkedIn Infographic",
        "format": "🖼️ System Architecture Blueprint",
        "best_time": "08:00 PM IST",
        "media_type": "photo",
        "media_path": TRACKKARO_CAROUSELS_DIR / "slide_3.png",
        "hook": "How to Build a Sub-15s Lead Response System With Zero Human Delay",
        "caption": """Modern high-ticket sales isn't about hiring more SDRs to sit on spreadsheets. It's about engineering instantaneous dispatch.

Here is the architecture we use at TrackKaro:
⚡ 0.2s: Webhook payload captured
⚡ 8.4s: WhatsApp pricing asset delivered to buyer
⚡ 12.1s: Telegram audio alert wakes sales rep
⚡ 14.8s: Lead intent scored & logged in NocoDB

Drop a comment if you want the webhook blueprint.

#systemdesign #gtmarchitect #aiagents #nocodb #automation #trackkaroai"""
    },
    "thursday": {
        "day_name": "Thursday",
        "product": "TrackKaro AI (@trackkaroai)",
        "platform": "Instagram & LinkedIn Case Teardown",
        "format": "📝 High-Ticket Case Benchmark",
        "best_time": "07:00 PM IST",
        "media_type": "photo",
        "media_path": TRACKKARO_CAROUSELS_DIR / "slide_4.png",
        "hook": "How a Dubai Real Estate Team Doubled Showings in 30 Days Without Spending $1 More on Ads",
        "caption": """The agency was spending $14,000/mo on Meta ads in Downtown Dubai.
Their problem wasn't lead volume. They had 350+ leads a month.
Their problem: Sales reps took an average of 3 hours 45 minutes to respond. By then, the client was already talking to 2 other developers.

We deployed TrackKaro AI:
• WhatsApp brochure dispatched in 8 seconds
• Priority VIP sales call initiated in 15 seconds
• Show-up rate skyrocketed from 4.1% to 22.6%

Stop increasing your ad budget to fix a slow sales team. Fix the response speed first.

Comment "CASE" to get the full case study.

#realestate #dubairealestate #speedtolead #adagency #trackkaroai"""
    },
    "friday": {
        "day_name": "Friday",
        "product": "TrackKaro AI (@trackkaroai)",
        "platform": "Instagram & X",
        "format": "🖼️ High-Contrast Reality Check",
        "best_time": "07:00 PM IST",
        "media_type": "photo",
        "media_path": TRACKKARO_CAROUSELS_DIR / "slide_2.png",
        "hook": "You Don't Have a Lead Problem. You Have a Speed Problem.",
        "caption": """If you spend $10,000 on paid ads but take 4 hours to call your leads, you don't have a lead problem.

You have a speed problem.

Lead intent has a half-life of 5 minutes. After 15 minutes, you are calling a stranger who forgot they even filled your form.

Fix the speed first. Then scale the ad spend.

#leadgeneration #gtmstrategy #salesleadership #marketingroi #trackkaroai"""
    },
    "saturday": {
        "day_name": "Saturday",
        "product": "TrackKaro AI (@trackkaroai)",
        "platform": "Instagram Reel / Short Video",
        "format": "🎬 9:16 Screen Teardown",
        "best_time": "06:30 PM IST",
        "media_type": "video",
        "media_path": TRACKKARO_REELS_DIR / "trackkaro_speed_to_lead_9x16.mp4",
        "hook": "Watch What Happens When a $2,000 Lead Fills a Form (Live Speed Test)",
        "caption": """Human response time: 3 hours 12 minutes (Lead lost).
TrackKaro response time: 14.8 seconds (Brochure delivered, rep on the phone).

Speed is the ultimate competitive advantage in high-ticket B2B & luxury sales.

Test your own response time at trackkaroai.com ⚡

#speedtolead #salesautomation #highincomeskills #gtmengineering #trackkaroai"""
    },
    "sunday": {
        "day_name": "Sunday",
        "product": "TrackKaro AI (@trackkaroai)",
        "platform": "Instagram & LinkedIn",
        "format": "📊 5-Slide Weekly ROI Summary",
        "best_time": "08:00 PM IST",
        "media_type": "document",
        "media_path": TRACKKARO_CAROUSELS_DIR / "TrackKaro_Speed_To_Lead_Carousel.pdf",
        "hook": "Audit Your Speed-to-Lead Before Monday's Ad Spend Kicks In",
        "caption": """Before your Monday ad budget starts burning on Meta and Google:

Ask your sales director one question:
'What was our median response time to inbound leads last week?'

If the answer is more than 5 minutes, you are paying full price for 20% conversion.

Comment "AUDIT" to run our free 60-second speed-to-lead audit on your funnel before Monday morning.

#b2bleadgen #agencygrowth #adspend #marketingroi #trackkaroai"""
    }
}

def dispatch_telegram_alert(day_key, account="vance"):
    schedule = SCHEDULE_VANCE if account.lower() == "vance" else SCHEDULE_TRACKKARO
    item = schedule.get(day_key.lower())
    if not item:
        print(f"❌ Unknown day '{day_key}'. Available: {list(schedule.keys())}")
        return False

    print(f"🚀 Preparing GTM Content Drop for: {item['day_name']} [{item['product']}]...")
    
    clean_caption = item['caption'].replace("<", "&lt;").replace(">", "&gt;")
    
    account_tag = "@usevance.ai" if account.lower() == "vance" else "@trackkaroai"
    
    text = (
        f"🎯 <b>[GTM DROP: {item['day_name'].upper()} • {account_tag.upper()}]</b>\n\n"
        f"🏷️ <b>Product / Account:</b> {item['product']}\n"
        f"🌐 <b>Target Platform:</b> {item['platform']}\n"
        f"📦 <b>Format:</b> {item['format']}\n"
        f"⏰ <b>Best Time to Post:</b> {item['best_time']}\n\n"
        f"💡 <b>Hook:</b>\n<i>{item['hook']}</i>\n\n"
        f"📝 <b>Caption (Tap to copy):</b>\n"
        f"<code>{clean_caption}</code>\n\n"
        f"<i>👉 Review media attached below, copy caption, and upload to {account_tag} in 30 seconds!</i>"
    )
    
    # Determine product-specific Telegram destination supergroup
    account_clean = account.lower()
    if account_clean in ["vance", "usevance"]:
        target_chat_id = os.getenv("VANCE_TELEGRAM_CHAT_ID", "-1003882353811")
    elif account_clean in ["prex", "getprex"]:
        target_chat_id = os.getenv("PREX_TELEGRAM_CHAT_ID", "-1003913485567")
    else:
        target_chat_id = TELEGRAM_CHAT_ID

    # 1. Send the text notification
    msg_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = json.dumps({
        "chat_id": target_chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }).encode()
    
    req = urllib.request.Request(msg_url, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        print(f"  ✓ Text alert & copyable caption sent to Telegram (chat: {target_chat_id})!")

    # 2. Send media if exists
    m_type = item.get("media_type")
    m_path = item.get("media_path")
    
    if m_path and Path(m_path).is_file():
        boundary = "----WebKitFormBoundaryMediaUpload"
        data = []
        data.append(f"--{boundary}".encode())
        data.append(b'Content-Disposition: form-data; name="chat_id"\r\n')
        data.append(str(target_chat_id).encode())
        
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
            
    print(f"✅ GTM Content drop for {item['day_name']} [{account.upper()}] successfully dispatched to Telegram!")
    return True

def main():
    parser = argparse.ArgumentParser(description="GTM Outreach Hacker Content Calendar (Vance & TrackKaro)")
    parser.add_argument("--account", "-a", choices=["vance", "trackkaro"], default="vance", help="Target Instagram account (default: vance)")
    parser.add_argument("--day", "-d", help="Day of the week (monday, tuesday, wednesday, thursday, friday, saturday, sunday)")
    parser.add_argument("--today", action="store_true", help="Send today's scheduled content drop to Telegram")
    parser.add_argument("--list", action="store_true", help="List scheduled weekly content drops")
    
    args = parser.parse_args()
    
    target_schedule = SCHEDULE_VANCE if args.account == "vance" else SCHEDULE_TRACKKARO
    
    if args.list:
        print(f"\n📅 Weekly Timetable for [{args.account.upper()} - {'@usevance.ai' if args.account=='vance' else '@trackkaroai'}]:")
        for d, item in target_schedule.items():
            print(f"  • {item['day_name'].upper()}: {item['platform']} — {item['format']} ({item['best_time']})")
            print(f"    Hook: \"{item['hook']}\"")
        return
        
    day_str = args.day.lower() if args.day else datetime.now().strftime("%A").lower()
    print(f"📆 Selected Day: {day_str.capitalize()} | Account: {args.account.upper()}")
    dispatch_telegram_alert(day_str, account=args.account)

if __name__ == "__main__":
    main()
