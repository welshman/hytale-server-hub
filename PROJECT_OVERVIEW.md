# 🎮 Hytale Server Hub - Project Overview

## What You've Got

A complete, production-ready **Hytale server discovery platform** with:

✅ **Fully Functional Website** - Interactive, modern UI  
✅ **Automatic Scraper** - Crawls Hytale server lists  
✅ **Daily Updates** - GitHub Actions runs every day  
✅ **20 Real Servers** - Pre-loaded with current Hytale servers  
✅ **GitHub Pages Hosting** - Free, automatic deployment  
✅ **Complete Documentation** - README, Setup guides, code comments  

---

## Project Files

### Website Files

**`index.html`** (17 KB)
- Complete standalone web application
- No external dependencies
- Loads server data from `data/servers.json`
- Features:
  - Real-time search and filtering
  - Filter by 15 server types
  - Filter by 5 regions
  - Copy IP to clipboard
  - Responsive dark theme
  - Live statistics

### Backend Files

**`scraper.py`** (4.7 KB)
- Python web scraper
- Crawls 3 Hytale server listing websites
- Extracts: names, descriptions, types, IPs, regions
- Updates timestamps automatically
- Preserves existing servers while updating

**`data/servers.json`** (6.7 KB)
- JSON database of 20 servers
- Contains: ID, name, description, types, IP, region, lastUpdated
- Auto-updated by scraper daily
- Easy to edit manually

### Automation

**`.github/workflows/scrape-daily.yml`** (1.3 KB)
- GitHub Actions workflow
- Runs daily at 12:00 UTC
- Can be manually triggered anytime
- Auto-commits changes to repository
- Updates live website automatically

### Configuration

**`requirements.txt`**
- `requests==2.31.0` - HTTP library for scraper
- `beautifulsoup4==4.12.2` - HTML parsing library

**`.gitignore`**
- Ignores Python cache, virtual envs, IDE files
- Keeps repository clean

### Documentation

**`README.md`** - Main documentation
- Features overview
- Getting started guide
- Project structure
- Current servers list
- Contributing guidelines

**`SETUP.md`** - Detailed setup guide
- Quick start (5 minutes)
- Local development
- GitHub Pages deployment
- Customization examples
- Troubleshooting

**`PROJECT_OVERVIEW.md`** - This file
- High-level project summary
- File descriptions
- Feature checklist
- Next steps

---

## Key Features

### 🔍 Advanced Filtering

**By Server Type:**
- Vanilla, SMP, PvP, PvE, MMORPG
- Roleplay, Creative, MiniGames
- Skyblock, Anarchy, Factions
- Hardcore, Modded, Adventure

**By Region:**
- Spain, United States, Germany
- France, Argentina

**By Search:**
- Name search
- Description search
- Real-time filtering

### 📊 Server Information

Each server shows:
- ✅ Server name (prominent)
- ✅ Full description
- ✅ Server types/tags
- ✅ IP address (copy button)
- ✅ Region location
- ✅ Last update date

### 🤖 Automatic Updates

- Daily scraping via GitHub Actions
- Runs at 12:00 UTC
- Manual trigger available
- Auto-commits to repository
- Zero manual maintenance

### 📱 Responsive Design

- Works on desktop (1400px+)
- Optimized for tablets
- Mobile-friendly layout
- Touch-friendly buttons

### 🎨 Modern UI

- Dark theme (gaming community vibe)
- Smooth animations
- Gradient backgrounds
- Clear typography
- Intuitive navigation

---

## Current Server Data

**20 Servers Across 5 Regions:**

| Region | Count | Examples |
|--------|-------|----------|
| Spain | 6 | Hytale Box, Hyzen, Hoodexia, Mythale, Hytale Hispano |
| United States | 7 | Hylanders, DreamTale, Hyperion, Horizons, HytaleVanilla, Hylore, 2B2H |
| Germany | 5 | Hylife, Hynetic, VoxelMC, HytaleCorner, Hybase |
| France | 2 | Mythlane, Arconi |
| Argentina | 1 | HytaleArgentum |

**Server Types Coverage:**
- Vanilla: 5 servers
- SMP: 5 servers
- MMORPG: 5 servers
- PvP: 8 servers
- Factions: 4 servers
- Minigames: 5 servers
- Anarchy: 4 servers
- Modded: 4 servers
- And more...

---

## Technology Stack

### Frontend
- **HTML5** - Semantic structure
- **CSS3** - Modern styling, variables, flexbox, grid
- **Vanilla JavaScript** - No frameworks, no dependencies
- **JSON** - Data format

### Backend/Scraper
- **Python 3.10+**
- **requests** - HTTP client
- **beautifulsoup4** - HTML parser

### Infrastructure
- **GitHub Repository** - Version control
- **GitHub Pages** - Hosting (free)
- **GitHub Actions** - Automation (free)

### Data Flow
```
Hytale Server Websites
        ↓
    Scraper (Python)
        ↓
  servers.json
        ↓
    index.html
        ↓
   User Browser
```

---

## How to Use

### For Users

1. Visit: https://welshman.github.io/hytale-server-hub/
2. Browse or filter servers
3. Click "Copy" to get server IP
4. Paste into Hytale launcher
5. Join the server!

### For Developers

**Clone & Run Locally:**
```bash
git clone https://github.com/welshman/hytale-server-hub.git
cd hytale-server-hub
pip install -r requirements.txt
python -m http.server 8000
# Visit: http://localhost:8000
```

**Run Scraper Manually:**
```bash
python scraper.py
```

**Trigger Daily Scraper:**
- Go to GitHub repo → Actions tab
- Click "Daily Hytale Server Scrape"
- Click "Run workflow"

---

## Customization Examples

### Change Website Colors

Edit CSS variables in `index.html`:
```css
:root {
    --primary: #6366f1;        /* Change this */
    --bg-dark: #0f172a;        /* And this */
}
```

### Add New Server Type

1. Add button in `index.html`:
   ```html
   <button class="tag-btn" data-type="MyType">My Type</button>
   ```

2. Add to scraper in `scraper.py`:
   ```python
   'MyType' in server_types
   ```

### Change Scrape Schedule

Edit `.github/workflows/scrape-daily.yml`:
```yaml
- cron: '0 */6 * * *'  # Every 6 hours instead of daily
```

### Add Server Manually

Edit `data/servers.json`:
```json
{
  "id": 21,
  "name": "My Server",
  "description": "Server description",
  "types": ["Vanilla", "SMP"],
  "ip": "play.example.com",
  "region": "Country",
  "lastUpdated": "2026-01-08"
}
```

---

## Next Steps

### Immediate (5 mins)

- ✅ Clone the repository
- ✅ Test website locally
- ✅ Explore the code

### Short-term (1 hour)

- [ ] Enable GitHub Pages
- [ ] Test live deployment
- [ ] Share with friends
- [ ] Add more servers

### Medium-term (1-2 days)

- [ ] Customize colors/branding
- [ ] Add new server types
- [ ] Improve scraper accuracy
- [ ] Add new regions

### Long-term (1+ weeks)

- [ ] Integrate with Discord
- [ ] Add server ratings
- [ ] Implement favorites/bookmarks
- [ ] Add player count tracking
- [ ] Create admin panel

---

## Repository Links

- 🏠 **GitHub**: [welshman/hytale-server-hub](https://github.com/welshman/hytale-server-hub)
- 🌐 **Live Site**: [welshman.github.io/hytale-server-hub/](https://welshman.github.io/hytale-server-hub/)
- 🔧 **Issues**: [GitHub Issues](https://github.com/welshman/hytale-server-hub/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/welshman/hytale-server-hub/discussions)

---

## Stats

- **Total Files**: 9
- **Total Lines of Code**: ~1,500
- **Servers**: 20
- **Server Types**: 15
- **Regions**: 5
- **Zero Dependencies** (frontend)
- **Zero Cost** (GitHub + GitHub Pages + GitHub Actions)

---

## License

MIT License - Free to use, modify, and distribute

---

## Final Notes

This is a **complete, production-ready project** that:

✨ Works right out of the box  
✨ Requires no server or database  
✨ Automatically updates daily  
✨ Scales to thousands of servers  
✨ Fully customizable  
✨ Easy to understand and modify  
✨ Perfect for portfolio projects  
✨ Great learning resource  

**Enjoy! 🎮**
