#!/usr/bin/env python3
"""
Send Vance 23 Buying Triggers 9:16 Video Reel + Instagram Caption to Telegram via curl.
"""

import subprocess
import html
import json
import urllib.request
from pathlib import Path

TOKEN = "8445264349:AAFWHjaQe9Qomf2Zwm7MVV_6NkhRmGWLMjs"
CHAT_ID = "-5489183481"
VIDEO_PATH = Path("/Users/mangal777/Mangal/growth_engine/reels/vance_23_triggers_9x16.mp4")

REEL_CAPTION = """Cold email is NOT dead. 

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

#aisdr #coldemail #b2bsaas #growthautomation #gtmengineering #salesdevelopment #usevance #hyperframes
"""

def send_video():
    print(f"🎬 Uploading {VIDEO_PATH.name} to Telegram via curl...")
    cmd = [
        "curl", "-s", "-X", "POST",
        f"https://api.telegram.org/bot{TOKEN}/sendVideo",
        "-F", f"chat_id={CHAT_ID}",
        "-F", f"video=@{str(VIDEO_PATH)}",
        "-F", "caption=🎬 <b>VANCE AI • 23 Live Buying Triggers 9:16 Video Reel</b>\n\n⚡ <i>Save to Photos & publish directly to Instagram Reels or TikTok!</i>",
        "-F", "parse_mode=HTML",
        "-F", "supports_streaming=true"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if '"ok":true' in res.stdout:
        print("✅ Reel video sent successfully to Telegram!")
    else:
        print(f"❌ Failed to upload video: {res.stdout}")

def send_caption():
    print("📝 Sending 1-tap copy-paste caption...")
    msg = f"📋 <b>COPY-PASTE REEL CAPTION FOR @usevance.ai:</b>\n\n<code>{html.escape(REEL_CAPTION)}</code>"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = json.dumps({"chat_id": CHAT_ID, "text": msg, "parse_mode": "HTML"}).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode())
        if res.get("ok"):
            print("✅ Caption sent successfully!")
        else:
            print(f"❌ Caption failed: {res}")

if __name__ == "__main__":
    send_video()
    send_caption()
