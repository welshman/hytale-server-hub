# 🚀 Getting Started - Quick Reference

## What You Have

A complete **Hytale server discovery platform** with:
- 🌐 Live website with interactive UI
- 🎮 20 pre-loaded Hytale servers
- 🤖 Automatic daily scraper
- 📄 Full documentation

**Repository:** [github.com/welshman/hytale-server-hub](https://github.com/welshman/hytale-server-hub)

---

## 5-Minute Quick Start

### 1. Clone & Setup

```bash
git clone https://github.com/welshman/hytale-server-hub.git
cd hytale-server-hub
pip install -r requirements.txt
```

### 2. Run Locally

```bash
python -m http.server 8000
# Open: http://localhost:8000
```

### 3. Test the Scraper

```bash
python scraper.py
```

Done! 🎉

---

## Deploy to GitHub Pages

### 1. Push to GitHub

If you haven't already:
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### 2. Enable Pages

1. Go to repository **Settings**
2. Click **Pages** (left sidebar)
3. Select `main` branch, root folder
4. Click **Save**

### 3. Visit Your Site

Wait 2-3 minutes, then go to:
```
https://your-username.github.io/hytale-server-hub/
```

Done! Your site is live! 🐟

---

## Project Structure

```
hytale-server-hub/
├── 🌐 index.html           # Website (open in browser)
├── 📄 data/servers.json    # Server database
├── 🎛 scraper.py           # Web scraper
├── ⚡ .github/workflows/   # Auto-scheduler
├── 📑 README.md            # Main docs
├─┠ 📑 SETUP.md             # Detailed guide
├┠ 📑 PROJECT_OVERVIEW.md  # Feature summary
└┠ 📑 INTEGRATIONS.md      # Extension examples
```

---

## Key Features

### Website Features

🔍 **Search & Filter**
- Search by server name
- Filter by 15 server types
- Filter by 5 regions
- Real-time results

📄 **Server Information**
- Name and description
- Server types/tags
- IP address (copy button)
- Region location
- Last updated date

📱 **Responsive Design**
- Desktop, tablet, mobile
- Dark theme
- Smooth animations

### Scraper Features

🤖 **Automatic Updates**
- Runs daily at 12:00 UTC
- Via GitHub Actions
- No manual maintenance

🏗 **Data Collection**
- 3 server listing websites crawled
- Server names extracted
- Types/tags identified
- Regions detected

📱 **Smart Updates**
- Preserves existing data
- Updates timestamps
- Auto-commits changes

---

## Common Tasks

### Add a Server

Edit `data/servers.json`:

```json
{
  "id": 21,
  "name": "My Server",
  "description": "Amazing survival server!",
  "types": ["Vanilla", "SMP"],
  "ip": "play.myserver.com",
  "region": "United States",
  "lastUpdated": "2026-01-08"
}
```

### Change Colors

In `index.html`, edit CSS variables (line 13):

```css
:root {
    --primary: #6366f1;          /* Change this color */
    --bg-dark: #0f172a;          /* And this one */
}
```

### Change Scrape Time

Edit `.github/workflows/scrape-daily.yml`:

```yaml
on:
  schedule:
    - cron: '0 12 * * *'  # Change this (use crontab.guru)
```

### Add Server Type

1. In `index.html` (line 385):
   ```html
   <button class="tag-btn" data-type="NewType">New Type</button>
   ```

2. In `scraper.py` (line 26):
   ```python
   'NewType' in server_types
   ```

### Add Region

1. In `index.html` (line 366):
   ```html
   <option value="Region Name">Region Name</option>
   ```

2. In `scraper.py` (line 18):
   ```python
   'region': 'Region Name',
   ```

---

## Troubleshooting

### Website won't load

- [ ] Check browser console (F12)
- [ ] Verify `data/servers.json` exists
- [ ] Clear browser cache (Ctrl+Shift+Del)
- [ ] Check file paths are correct

### Scraper not running

- [ ] Check GitHub Actions logs (Actions tab)
- [ ] Run manually: `python scraper.py`
- [ ] Verify dependencies: `pip install -r requirements.txt`

### Changes not showing

- [ ] Commit and push changes: `git push`
- [ ] Wait 1-2 minutes for GitHub Pages to update
- [ ] Hard refresh browser (Ctrl+Shift+R)

### JSON file corrupted

- [ ] Validate JSON at [jsonlint.com](https://www.jsonlint.com/)
- [ ] Check for missing commas
- [ ] Ensure proper formatting

---

## File Guide

### Essential Files

| File | Purpose | Edit? |
|------|---------|-------|
| `index.html` | Website UI | Yes - colors, types |
| `data/servers.json` | Server database | Yes - add/remove servers |
| `scraper.py` | Web scraper | Yes - improve detection |
| `.github/workflows/scrape-daily.yml` | Auto-scheduler | Yes - change time |

### Documentation Files

| File | Purpose | Read First? |
|------|---------|-------------|
| `README.md` | Main documentation | ✅ Yes |
| `SETUP.md` | Detailed setup guide | ✅ Yes |
| `PROJECT_OVERVIEW.md` | Feature summary | ✅ Yes |
| `INTEGRATIONS.md` | Extension examples | If extending |
| `GETTING_STARTED.md` | This file | You're here! |

### Config Files

| File | Purpose |
|------|----------|
| `requirements.txt` | Python dependencies |
| `.gitignore` | Git ignore rules |

---

## Recommended Reading Order

1. **This file** (2 min) - Get oriented
2. **README.md** (5 min) - Overview & features
3. **SETUP.md** (10 min) - Detailed instructions
4. **Explore the code** (20 min) - Understand structure
5. **INTEGRATIONS.md** (optional) - Advanced features

---

## Next Steps

### Week 1

- [ ] Clone repository
- [ ] Test locally
- [ ] Deploy to GitHub Pages
- [ ] Share with friends

### Week 2

- [ ] Customize colors/branding
- [ ] Add new server types
- [ ] Improve scraper
- [ ] Add more servers

### Week 3+

- [ ] Discord bot integration
- [ ] Server rating system
- [ ] Player count tracking
- [ ] Admin panel

---

## Support

📧 **Have questions?**
- Check [README.md](README.md)
- Check [SETUP.md](SETUP.md)
- Open GitHub Issue

🐛 **Found a bug?**
- Open GitHub Issue
- Include error details
- Describe steps to reproduce

🊧 **Want to contribute?**
- Fork repository
- Make changes
- Submit pull request
- See README for details

---

## Quick Links

- 🌐 [Live Website](https://welshman.github.io/hytale-server-hub/)
- 🐛 [GitHub Repository](https://github.com/welshman/hytale-server-hub)
- 💼 [GitHub Issues](https://github.com/welshman/hytale-server-hub/issues)
- 📑 [README](README.md)
- ⚡ [Setup Guide](SETUP.md)
- 🌟 [Project Overview](PROJECT_OVERVIEW.md)
- 🔗 [Integrations](INTEGRATIONS.md)

---

## Stats

- **20 Servers** from 5 regions
- **15 Server Types** available
- **100% Free Hosting** (GitHub Pages)
- **Automatic Updates** (GitHub Actions)
- **Zero Dependencies** (frontend)
- **~1500 Lines of Code** (clean & documented)

---

## Success Checklist

- [ ] Cloned repository
- [ ] Installed dependencies
- [ ] Tested locally
- [ ] Deployed to GitHub Pages
- [ ] Website is live and accessible
- [ ] Servers display correctly
- [ ] Filters work
- [ ] Copy button works
- [ ] Read documentation
- [ ] Ready to customize!

---

## You're All Set!

Your Hytale Server Hub is ready to go! 🎆

**Next:** Read [SETUP.md](SETUP.md) for detailed customization options.

---

*Last updated: 2026-01-08*
