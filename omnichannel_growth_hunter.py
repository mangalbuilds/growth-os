#!/usr/bin/env python3
"""
⚡ Omnichannel Growth & Social Lead Hunter
Engineered for Mangal Soren (TrackKaro AI, Jarvis, Creatigen, Kanjo, UGhar)
- Multi-Project & Multi-Platform Support (from projects.yaml)
- Database Storage & Deduplication (growth_vault.db)
- High-Converting AI Drafting (Gemini Flash)
- Instant Mobile Push with Clickable Links (Telegram Bot)
- NocoDB Ready Schema & CSV Export
"""

import sys
import os
import re
import json
import sqlite3
import argparse
import urllib.request
import urllib.parse
from datetime import datetime
from pathlib import Path

import env_loader

# --- Configuration & Credentials ---
SERPER_API_KEY = os.environ.get("SERPER_API_KEY", "")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "-5489183481")

DB_PATH = Path.home() / "Mangal" / "growth_engine" / "growth_vault.db"
PROJECTS_CONFIG = Path.home() / "Mangal" / "growth_engine" / "config" / "projects.yaml"

# NocoDB Direct CRM Configuration
NOCO_URL = os.environ.get("NOCO_URL", "https://crm.trackkaroai.com")
NOCO_TOKEN = os.environ.get("NOCO_TOKEN", "")
NOCO_BASE_ID = "p2xijprsqm6nold"
NOCO_OPPS_TABLE = "mr4g9hepgu68ut6"
NOCO_STRATEGIES_TABLE = "mbgtvbu3rf6fycm"
NOCO_PROJECTS_TABLE = "mnm2vnaadnaxqd9"

def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS growth_opportunities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                project TEXT NOT NULL,
                platform TEXT NOT NULL,
                thread_id TEXT UNIQUE NOT NULL,
                source_channel TEXT,
                title TEXT,
                url TEXT,
                op_query TEXT,
                ai_draft TEXT,
                status TEXT DEFAULT 'ALERTED',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                posted_at TIMESTAMP
            )
        """)
        conn.commit()

def load_projects_config():
    if not PROJECTS_CONFIG.is_file():
        print(f"❌ Error: Config file missing at {PROJECTS_CONFIG}")
        sys.exit(1)
    
    # Simple PyYAML-free parser for projects.yaml
    content = PROJECTS_CONFIG.read_text(encoding="utf-8")
    import yaml
    return yaml.safe_load(content).get("projects", {})

def search_reddit_opportunities(project_key, project_data, limit=4):
    keywords = project_data.get("trigger_keywords", [])
    subreddits = project_data.get("target_subreddits", [])
    
    if not keywords or not subreddits:
        return []
    
    opportunities = []
    seen_ids = set()
    
    # Generate focused search queries to catch fresh discussions naturally
    queries = []
    for sub in subreddits[:3]:
        for kw in keywords[:2]:
            queries.append(f'site:reddit.com/{sub.strip()} {kw}')
    
    url = "https://google.serper.dev/search"
    
    for q in queries[:3]:
        if len(opportunities) >= limit:
            break
            
        # TBS 'qdr:m' strictly restricts Google Serper to Past Month (active threads only!)
        payload = json.dumps({
            "q": q,
            "num": limit * 2,
            "tbs": "qdr:m"
        }).encode()
        
        req = urllib.request.Request(url, data=payload, headers={
            "X-API-KEY": SERPER_API_KEY,
            "Content-Type": "application/json"
        })
        
        try:
            with urllib.request.urlopen(req, timeout=25) as resp:
                data = json.loads(resp.read().decode())
                results = data.get("organic", [])
                for r in results:
                    link = r.get("link", "")
                    if "/comments/" in link:
                        match = re.search(r"/comments/([a-z0-9]+)/", link)
                        t_id = match.group(1) if match else link
                        
                        # Filter out ancient thread IDs (e.g. 5-6 letter base36 IDs like 'vz6mxu' from 4 years ago)
                        # Modern 2025/2026 thread IDs are 7 characters and start with '1'
                        if len(t_id) < 6 or (len(t_id) == 6 and not t_id.startswith("1")):
                            continue
                            
                        if t_id not in seen_ids:
                            seen_ids.add(t_id)
                            # Negative intent filtering to prevent interview/salary mismatch
                        title_lower = r.get("title", "").lower()
                        snippet_lower = r.get("snippet", "").lower()
                        combined_text = f"{title_lower} {snippet_lower}"
                        
                        negative_intents = [
                            "final round", "interview prep", "salary negotiation",
                            "leetcode", "technical interview", "behavioral interview",
                            "failed interview", "got rejected after final"
                        ]
                        
                        if any(neg in combined_text for neg in negative_intents):
                            continue
                            
                        opportunities.append({
                                "thread_id": t_id,
                                "title": r.get("title", ""),
                                "url": link,
                                "snippet": r.get("snippet", ""),
                                "date": r.get("date", "Active This Month"),
                                "channel": "/".join(link.split("/")[:5])
                            })
                            if len(opportunities) >= limit:
                                break
        except Exception as e:
            print(f"⚠️ Search error for {project_key} ({q}): {e}")
            continue
            
    return opportunities[:limit]

def draft_ai_response(project_key, project_data, opp):
    p_name = project_data.get("name", "TrackKaro")
    one_liner = project_data.get("one_liner", "")
    disclosure = project_data.get("disclosure", "")
    
    if project_key in ['prex', 'getprex']:
        prompt = f"""You are a cynical, pragmatic tech builder & software engineer posting casually on Reddit.
Do NOT sound like ChatGPT, an AI assistant, or a corporate LinkedIn thought leader. Zero formal greetings, zero 'Honestly,', zero boilerplate.
Tone: Blunt, lowercase/casual punctuation, high-signal developer reality.
Length: 2 to 3 sentences max (under 45 words).

Reddit Post to reply to:
Title: {opp['title']}
Context: {opp['snippet']}

Rules:
1. State the ground reality: most early-stage AI startups don't even push to LinkedIn due to spam; they only maintain active Ashby or Greenhouse endpoints.
2. End with an irresistible 'Asset Bait' that sparks comments/DMs (e.g. 'i have a raw list of ~120 stealth/seed ai startups hiring on ashby this week without linkedin posts, shoot me a dm if you want it'). NEVER say 'drop a comment and i will dm you' — always make the user initiate the DM to bypass Reddit outbound rate limits.
3. NEVER paste any website links. Zero emojis, zero hashtags.

Write the casual raw comment only:"""
    else:
        prompt = f"""You are a pragmatic B2B engineer posting casually on Reddit.
Do NOT sound like ChatGPT, Claude, or a sales rep.
Tone: Direct, cynical, experience-driven. 2 to 3 sentences max (under 45 words).

Reddit Post to reply to:
Title: {opp['title']}
Context: {opp['snippet']}

Rules:
1. Focus on real technical solutions (e.g. inbox reputation, buying signals vs cold spray).
2. End with an offer to share the raw checklist or data via DM/comment.
3. Zero links, zero emojis, zero corporate fluff.

Write the raw comment only:"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={GEMINI_API_KEY}"
    payload = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode()
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            res = json.loads(resp.read().decode())
            return res["candidates"][0]["content"]["parts"][0]["text"].strip()
    except Exception as e:
        # Dynamic context-aware authentic fallback per project
        if project_key in ['prex', 'getprex']:
            return f"most early ai startups dont even push to linkedin anymore, way too much bot spam. they just keep active ashby or greenhouse boards. i put together a raw sheet of ~120 stealth/seed ai startups hiring on ashby this week without linkedin posts, drop a comment or dm if you want the link."
        elif project_key in ['vance', 'usevance', 'jarvis']:
            return f"Cold email deliverability is night and day once you switch from cold bulk blasts to signal-based triggers. What solved it for us was waiting for actual buying intent triggers (hiring surges, tech churn) and keeping reply volumes under 35 per mailbox with strict SPF/DKIM/DMARC alignment. ({disclosure})"
        else:
            return f"I ran into this exact challenge recently. What worked for us was tightening the workflow and eliminating manual handoffs with real-time signal triggers. ({disclosure})"

def send_telegram_alert(project_key, project_data, opp, draft):
    p_name = project_data.get("name", project_key.upper())
    
    # Strict dynamic chat routing per isolated project
    chat_id = project_data.get("telegram_chat_id")
    if not chat_id:
        if project_key in ["vance", "usevance"]:
            chat_id = os.environ.get("VANCE_TELEGRAM_CHAT_ID", "-1003882353811")
        elif project_key in ["prex", "getprex"]:
            chat_id = os.environ.get("PREX_TELEGRAM_CHAT_ID", "-1003913485567")
        elif project_key in ["trackkaro", "trackkaroai"]:
            chat_id = "-5489183481"
        else:
            chat_id = "-5489183481"
    
    clean_title = opp['title'].replace("<", "&lt;").replace(">", "&gt;")
    clean_draft = draft.replace("<", "&lt;").replace(">", "&gt;")
    post_date = opp.get("date", "Active This Month")
    
    text = (
        f"🎯 <b>[NEW REDDIT INTENT LEAD: {p_name}]</b>\n\n"
        f"📌 <b>Thread:</b> {clean_title}\n"
        f"⚡ <b>Freshness:</b> {post_date}\n"
        f"🔗 <a href=\"{opp['url']}\">👉 Click Here to Open Reddit Thread</a>\n\n"
        f"💬 <b>AI Experience Reply (Tap to Copy):</b>\n"
        f"<code>{clean_draft}</code>\n\n"
        f"<i>💡 Tap the text box above to copy, open the link, and post directly from your Reddit account u/NotNecessary- to build karma & authority!</i>"
    )
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = json.dumps({
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }).encode()
    
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            return resp.getcode() == 200
    except Exception as e:
        print(f"⚠️ Telegram alert failed for {project_key} (chat {chat_id}): {e}")
        return False

def sync_opportunity_to_nocodb(project_key, opp, draft):
    """Sync single opportunity to NocoDB Growth Opportunities table."""
    try:
        url = f"{NOCO_URL}/api/v2/tables/{NOCO_OPPS_TABLE}/records"
        payload = json.dumps([{
            "Project": project_key,
            "Platform": "Reddit",
            "Thread / Post Title": opp.get("title", ""),
            "Thread URL": opp.get("url", ""),
            "Author / Subreddit / Handle": opp.get("channel", "reddit"),
            "Pain Point Summary": opp.get("snippet", ""),
            "Intent Score (1-100)": 90,
            "AI Crafted Reply": draft,
            "Engagement Status": "ALERTED",
            "Discovered At": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }]).encode("utf-8")
        
        req = urllib.request.Request(
            url,
            data=payload,
            headers={"xc-token": NOCO_TOKEN, "Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=8) as resp:
            return resp.getcode() in [200, 201]
    except Exception as e:
        print(f"  ⚠️ NocoDB live sync notice: {e}")
        return False

def record_opportunity(project_key, opp, draft):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            INSERT OR IGNORE INTO growth_opportunities 
            (project, platform, thread_id, source_channel, title, url, op_query, ai_draft, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'ALERTED')
        """, (
            project_key,
            "reddit",
            opp["thread_id"],
            opp.get("channel", "reddit"),
            opp["title"],
            opp["url"],
            opp.get("snippet", ""),
            draft
        ))
        conn.commit()

def is_already_processed(thread_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM growth_opportunities WHERE thread_id = ?", (thread_id,))
        return cursor.fetchone() is not None

def run_hunter_for_project(project_key, project_data):
    p_name = project_data.get("name", project_key)
    print(f"\n🔍 Scanning opportunities for: \033[1;36m{p_name}\033[0m...")
    
    opps = search_reddit_opportunities(project_key, project_data)
    if not opps:
        print(f"  ℹ️ No fresh threads found matching keywords.")
        return 0
    
    new_count = 0
    for opp in opps:
        if is_already_processed(opp["thread_id"]):
            continue
            
        print(f"  🎯 Found: {opp['title'][:70]}...")
        draft = draft_ai_response(project_key, project_data, opp)
        
        # 1. Send push to Telegram
        sent = send_telegram_alert(project_key, project_data, opp, draft)
        if sent:
            print(f"  📲 Telegram alert sent to phone!")
            
        # 2. Record in Local Database for deduplication
        record_opportunity(project_key, opp, draft)
        
        # 3. Direct Live Sync to NocoDB
        noco_synced = sync_opportunity_to_nocodb(project_key, opp, draft)
        if noco_synced:
            print(f"  📊 Synced to NocoDB Growth Vault!")
            
        new_count += 1
        
    print(f"  ✅ Processed {new_count} new high-intent leads.")
    return new_count

def export_nocodb_csv():
    import csv
    export_file = DB_PATH.parent / "nocodb_growth_vault_import.csv"
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, project, platform, source_channel, title, url, ai_draft, status, created_at FROM growth_opportunities ORDER BY id DESC")
        rows = cursor.fetchall()
        
    with open(export_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Project", "Platform", "Subreddit_or_Channel", "Title_or_Hook", "URL", "AI_Draft_Reply", "Status", "Discovered_At"])
        for r in rows:
            writer.writerow([r["id"], r["project"], r["platform"], r["source_channel"], r["title"], r["url"], r["ai_draft"], r["status"], r["created_at"]])
            
    print(f"\n📊 NocoDB Ready CSV Exported: \033[1;32m{export_file}\033[0m ({len(rows)} records)")
    print("👉 Simply click 'Import CSV' in NocoDB to load this into your web dashboard!")

def sync_all_to_nocodb():
    """Sync all opportunities from local SQLite to NocoDB table."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT project, platform, source_channel, title, url, op_query, ai_draft, status, created_at FROM growth_opportunities")
        rows = cur.fetchall()
        
    records = []
    for r in rows:
        records.append({
            "Project": r["project"],
            "Platform": r["platform"].capitalize(),
            "Thread / Post Title": r["title"],
            "Thread URL": r["url"],
            "Author / Subreddit / Handle": r["source_channel"],
            "Pain Point Summary": r["op_query"],
            "Intent Score (1-100)": 90,
            "AI Crafted Reply": r["ai_draft"],
            "Engagement Status": r["status"],
            "Discovered At": str(r["created_at"])
        })
        
    if not records:
        print("  ℹ️ No local opportunities found to sync.")
        return
        
    try:
        url = f"{NOCO_URL}/api/v2/tables/{NOCO_OPPS_TABLE}/records"
        payload = json.dumps(records).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=payload,
            headers={"xc-token": NOCO_TOKEN, "Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=25) as resp:
            print(f"  ✅ Successfully synced {len(records)} records to NocoDB ({NOCO_URL})!")
    except Exception as e:
        print(f"  ⚠️ NocoDB bulk sync error: {e}")

def show_status():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT project, count(*) FROM growth_opportunities GROUP BY project")
        stats = cursor.fetchall()
        print("\n📊 Growth Vault — Database Summary:")
        if not stats:
            print("  (Database is empty. Run a scan to discover leads).")
        for p, count in stats:
            print(f"  • {p.upper()}: {count} opportunities tracked")
            
    print(f"\n🌐 NocoDB Cloud CRM:")
    print(f"  • Base: Growth OS - Multi-Project Social Engine ({NOCO_URL})")
    print(f"  • Base ID: {NOCO_BASE_ID}")
    print(f"  • Tables: Projects, Growth Strategies, Growth Opportunities, Content Assets")

def main():
    init_db()
    parser = argparse.ArgumentParser(description="Omnichannel Social Growth & Lead Hunter")
    parser.add_argument("--project", "-p", help="Target project key (e.g. jarvis, trackkaro, creatigen, kanjo, ughar)")
    parser.add_argument("--all", action="store_true", help="Scan opportunities for all projects in projects.yaml")
    parser.add_argument("--status", action="store_true", help="Show database lead count & NocoDB status")
    parser.add_argument("--sync-nocodb", action="store_true", help="Push all local opportunities to NocoDB")
    parser.add_argument("--export-nocodb", action="store_true", help="Export NocoDB CSV")
    
    args = parser.parse_args()
    projects = load_projects_config()
    
    if args.status:
        show_status()
        return
        
    if args.export_nocodb:
        export_nocodb_csv()
        return

    if args.sync_nocodb:
        sync_all_to_nocodb()
        return
        
    if args.project:
        p_key = args.project.lower()
        if p_key not in projects:
            print(f"❌ Unknown project '{p_key}'. Available: {list(projects.keys())}")
            sys.exit(1)
        p_data = projects[p_key]
        if not p_data.get("enabled", True):
            print(f"⚠️ Project '{p_key}' ({p_data.get('name')}) is currently disabled in projects.yaml. Skipping.")
            return
        run_hunter_for_project(p_key, p_data)
    elif args.all:
        total = 0
        for p_key, p_data in projects.items():
            if not p_data.get("enabled", True):
                print(f"  ⏭️ Skipping disabled project: {p_key} ({p_data.get('name')})")
                continue
            total += run_hunter_for_project(p_key, p_data)
        print(f"\n🎉 Omnichannel Scan Complete! Dispatched {total} alerts to Telegram.")
    else:
        # Default: Run for Jarvis
        run_hunter_for_project("jarvis", projects["jarvis"])

if __name__ == "__main__":
    main()
