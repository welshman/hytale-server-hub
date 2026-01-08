# 🎮 Hytale Server Hub

A modern, interactive web application to discover and filter Hytale servers. Features automatic daily scraping of server data via GitHub Actions.

[![Daily Scrape](https://github.com/welshman/hytale-server-hub/actions/workflows/scrape-daily.yml/badge.svg)](https://github.com/welshman/hytale-server-hub/actions/workflows/scrape-daily.yml)

## Features

✅ **Interactive Server Listing**
- Browse 20+ Hytale servers with detailed information
- Real-time search and filtering capabilities
- Copy server IP to clipboard with one click

✅ **Advanced Filtering**
- Filter by server type: Vanilla, SMP, PvP, PvE, MMORPG, Roleplay, Creative, MiniGames, Skyblock, Anarchy, Factions, Hardcore, Modded, Adventure
- Filter by region: Spain, United States, Germany, France, Argentina
- Combine multiple filters for precise results

✅ **Automatic Updates**
- Daily automatic scraping of Hytale server listing websites
- GitHub Actions runs daily at 12:00 UTC
- Manual trigger available for immediate updates

✅ **Modern UI**
- Dark theme optimized for gaming communities
- Responsive design for desktop, tablet, and mobile
- Smooth animations and transitions
- Real-time server statistics

## Live Website

🌐 **[View Live Site](https://welshman.github.io/hytale-server-hub/)**

The site is hosted via GitHub Pages and updates automatically each day.

## Project Structure

```
hytale-server-hub/
├── index.html                    # Main website (HTML/CSS/JS)
├── scraper.py                    # Python web scraper
├── data/
│   └── servers.json             # Server data (auto-updated)
├── .github/workflows/
│   └── scrape-daily.yml        # GitHub Actions scheduler
└── README.md                     # This file
```

## Server Data Format

Each server in `data/servers.json` contains:

```json
{
  "id": 1,
  "name": "Server Name",
  "description": "Server description and features",
  "types": ["Vanilla", "SMP"],
  "ip": "play.example.com",
  "region": "United States",
  "lastUpdated": "2026-01-08"
}
```

## Getting Started

### Prerequisites

- Python 3.10+
- pip (Python package manager)
- Git

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/welshman/hytale-server-hub.git
   cd hytale-server-hub
   ```

2. **Install Python dependencies**
   ```bash
   pip install requests beautifulsoup4
   ```

3. **Run the scraper manually**
   ```bash
   python scraper.py
   ```

4. **Serve locally**
   ```bash
   # Using Python's built-in server
   python -m http.server 8000
   
   # Then visit: http://localhost:8000
   ```

## How It Works

### Website (`index.html`)

1. Loads `data/servers.json` on page load
2. Displays all servers in an interactive grid
3. Filters servers based on:
   - Search query (name/description)
   - Region selection
   - Selected server types
4. Shows real-time statistics
5. Allows copying server IPs to clipboard

### Scraper (`scraper.py`)

1. Loads existing servers from `data/servers.json`
2. Crawls Hytale server listing websites:
   - https://hytaleserverlist.me
   - https://hytaleservers.org
   - https://hytaleserver.com
3. Extracts server information:
   - Server name and description
   - Server types/tags
   - IP addresses
   - Regions
4. Updates timestamps
5. Saves to `data/servers.json`

### GitHub Actions (`scrape-daily.yml`)

1. Runs daily at **12:00 UTC**
2. Checks out the repository
3. Installs dependencies
4. Runs the Python scraper
5. Commits and pushes changes if data changed
6. Updates live GitHub Pages site automatically

## Customization

### Adding New Server Types

1. Edit `index.html` - Find the filter buttons section:
   ```html
   <button class="tag-btn" data-type="YourType">Your Type</button>
   ```

2. Update `scraper.py` - Add to the `server_types` list:
   ```python
   server_types = [
       'Vanilla', 'SMP', 'YourType', # ... etc
   ]
   ```

### Changing Scrape Schedule

Edit `.github/workflows/scrape-daily.yml`:

```yaml
on:
  schedule:
    # Change cron expression (crontab.guru for help)
    - cron: '0 12 * * *'  # Daily at 12:00 UTC
```

### Adding Manual Server Entries

Edit `data/servers.json` directly:

```json
{
  "id": 21,
  "name": "Your Server",
  "description": "Description here",
  "types": ["Vanilla", "SMP"],
  "ip": "play.yourserver.com",
  "region": "United States",
  "lastUpdated": "2026-01-08"
}
```

## Deploying with GitHub Pages

1. Go to repository **Settings** → **Pages**
2. Set source to `main` branch, root folder
3. Wait for deployment (usually 1-2 minutes)
4. Site will be available at: `https://username.github.io/hytale-server-hub/`

## Technologies Used

- **Frontend**: HTML5, CSS3, Vanilla JavaScript (no dependencies)
- **Backend Scraper**: Python 3.10+
  - `requests` - HTTP requests
  - `beautifulsoup4` - HTML parsing
- **Automation**: GitHub Actions
- **Hosting**: GitHub Pages + GitHub Actions
- **Data Format**: JSON

## Current Servers (20 servers)

| Server Name | Region | Types |
|-------------|--------|-------|
| Hytale Box | Spain | Vanilla, Modded, MMORPG, MiniGames |
| Hylanders | United States | Vanilla, Roleplay, Modded, SMP |
| DreamTale Vanilla | United States | Vanilla, SMP |
| Hylife | Germany | MMORPG, Roleplay |
| Mythlane | France | PvP, PvE, Modded, MiniGames |
| Hyzen | Spain | Adventure, MMORPG, PvE, PvP |
| Hoodexia | Spain | Creative, Factions, MiniGames, PvE |
| Hyperion Online Anarchy | United States | Anarchy |
| Hynetic | Germany | MiniGames, PvE, PvP |
| Horizons SMP | United States | Adventure, Anarchy, Hardcore, MMORPG |
| HytaleArgentum | Argentina | Adventure, PvE, PvP |
| Hylore | United States | Anarchy |
| VoxelMC.de | Germany | MiniGames, SMP, PvP |
| Mythale | Spain | Vanilla, Factions, PvP, PvE |
| Hytale Hispano | Spain | PvP, PvE, Factions, Vanilla |
| HytaleCorner | Germany | PvP, Factions, Modded, Skyblock |
| Arconi | France | Skyblock, MiniGames, MMORPG, PvE |
| 2B2H | United States | Anarchy, Adventure, Factions, Hardcore |
| HytaleVanilla | United States | Vanilla, Anarchy, SMP |
| Hybase | Germany | Factions, MiniGames, Modded, PvP |

## Contributing

Want to add servers or improve the scraper? 

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit (`git commit -m 'Add amazing feature'`)
5. Push to branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## Issues & Improvements

Found a server that's missing or incorrect? Have a feature suggestion?

- [Open an Issue](https://github.com/welshman/hytale-server-hub/issues)
- [View All Issues](https://github.com/welshman/hytale-server-hub/issues)

## License

MIT License - See LICENSE file for details

## Disclaimer

This project is not affiliated with Hytale or Hypixel Studios. Server information is gathered from public sources and may not be 100% accurate. Always verify server details before joining.

## Support & Questions

- 📧 Check GitHub Issues for common questions
- 🐛 Report bugs via GitHub Issues
- 💬 Discussions available in the repository

---

**Last Updated**: 2026-01-08  
**Total Servers**: 20  
**Next Auto-Scrape**: Daily at 12:00 UTC
