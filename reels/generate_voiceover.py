#!/usr/bin/env python3
"""
Generate Studio AI Voiceover for Vance 17.5s Instagram Reel using Azure Neural TTS.
"""

import subprocess
import asyncio
from pathlib import Path

VOICE = "en-US-AndrewMultilingualNeural" # Warm, Confident, Authentic Tech Founder
OUTPUT_WAV = Path("/Users/mangal777/Mangal/growth_engine/reels/vance_voiceover.mp3")

# Precise timed script designed for our 17.5s timeline with slight pauses
SCRIPT = """
Blasting one thousand generic cold emails is completely dead. 
Meet Vance. An autonomous SDR monitoring 23 live buying triggers on a fifteen minute cadence.
When a signal fires, Gemini Flash writes a bespoke reaction email in four hundred milliseconds.
Stop spamming. Start closing. DM 'Vance' for twenty free verified leads.
"""

def generate():
    cmd = [
        "/Users/mangal777/.local/bin/uv", "run", "--with", "edge-tts",
        "edge-tts",
        "--voice", VOICE,
        "--text", SCRIPT.strip(),
        "--rate=+4%", # slightly punchy Silicon Valley tech pace
        "--write-media", str(OUTPUT_WAV)
    ]
    print(f"🎙️ Generating AI voiceover with {VOICE}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0 and OUTPUT_WAV.exists():
        print(f"✅ Generated voiceover: {OUTPUT_WAV} ({OUTPUT_WAV.stat().st_size} bytes)")
    else:
        print(f"❌ Failed: {res.stderr}")

if __name__ == "__main__":
    generate()
