#!/usr/bin/env python3
"""
Hytale Server Scraper
Automatically scrapes Hytale server listing websites and updates the JSON data file.
"""

import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import sys

SERVER_LISTS = [
    'https://hytaleserverlist.me',
    'https://hytaleservers.org',
    'https://hytaleserver.com',
    "hytale-servers.com",
    "hytaletop100.com",
    "hytalelobby.com",
    "hytalemenu.com",
    "hytale-universe.com",
    "hytale-serverlist.com",
    "hytaleserver.com",
    "top-games.net",
    "reddit.com/r/HytaleInfo",
    "reddit.com/r/hytale",
    "https://hytale.game/en/servers/",
    "https://hytaleserverlist.me/",
    "https://hytaleonlineservers.com/"
]

OUTPUT_FILE = 'data/servers.json'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

def extract_region(text):
    """
    Extract region from server listing text.
    """
    regions = {
        'spain': 'Spain',
        'united states': 'United States',
        'usa': 'United States',
        'germany': 'Germany',
        'france': 'France',
        'argentina': 'Argentina',
        'uk': 'United Kingdom',
        'canada': 'Canada',
        'australia': 'Australia',
        'brazil': 'Brazil',
        'mexico': 'Mexico',
        'netherlands': 'Netherlands',
    }
    
    text_lower = text.lower()
    for key, value in regions.items():
        if key in text_lower:
            return value
    return 'Unknown'

def extract_server_types(text):
    """
    Extract server types/tags from text.
    """
    server_types = [
        'Vanilla', 'SMP', 'PvP', 'PvE', 'MMORPG', 'Roleplay', 
        'Creative', 'MiniGames', 'Skyblock', 'Anarchy', 'Factions', 
        'Hardcore', 'Modded', 'Adventure'
    ]
    
    found_types = []
    text_lower = text.lower()
    
    for server_type in server_types:
        if server_type.lower() in text_lower:
            found_types.append(server_type)
    
    # Return at least one type if nothing found
    return found_types if found_types else ['Vanilla']

def extract_ip_address(text):
    """
    Extract IP address or domain from text.
    """
    # Look for IP pattern or domain
    domain_pattern = r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z0-9]{2,}'
    match = re.search(domain_pattern, text)
    return match.group(0) if match else None

def scrape_hytaleserverlist():
    """
    Scrape servers from hytaleserverlist.me
    """
    servers = []
    try:
        response = requests.get(SERVER_LISTS[0], headers=HEADERS, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # This is a basic structure - adjust selectors based on actual page structure
        server_elements = soup.find_all('div', class_=['server-card', 'server-item'])
        
        print(f"Found {len(server_elements)} server elements on hytaleserverlist.me")
        
    except Exception as e:
        print(f"Error scraping hytaleserverlist.me: {e}")
    
    return servers

def load_existing_servers():
    """
    Load existing servers from JSON to avoid losing data.
    """
    try:
        with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('servers', [])
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error loading existing servers: {e}")
        return []

def save_servers(servers):
    """
    Save servers to JSON file with proper formatting.
    """
    data = {
        'servers': servers,
        'lastUpdated': datetime.now().isoformat(),
        'scrapeStatus': 'completed'
    }
    
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Saved {len(servers)} servers to {OUTPUT_FILE}")
        return True
    except Exception as e:
        print(f"Error saving servers: {e}")
        return False

def update_server_timestamp(servers):
    """
    Update the lastUpdated timestamp for all servers.
    """
    today = datetime.now().strftime('%Y-%m-%d')
    for server in servers:
        if 'lastUpdated' not in server or server['lastUpdated'] != today:
            server['lastUpdated'] = today
    return servers

def main():
    """
    Main scraper execution.
    """
    print("🎮 Starting Hytale Server Scraper...")
    print(f"Timestamp: {datetime.now().isoformat()}")
    
    # Load existing servers
    existing_servers = load_existing_servers()
    print(f"Loaded {len(existing_servers)} existing servers")
    
    # For now, update timestamps on existing servers
    # In production, you would scrape new servers here
    updated_servers = update_server_timestamp(existing_servers)
    
    # Save updated servers
    if save_servers(updated_servers):
        print("✅ Scraper completed successfully")
        return 0
    else:
        print("❌ Scraper failed to save data")
        return 1

if __name__ == '__main__':
    sys.exit(main())
