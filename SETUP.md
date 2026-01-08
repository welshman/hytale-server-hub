# Setup & Configuration Guide

## Quick Start (5 minutes)

### Step 1: Clone the Repository

```bash
git clone https://github.com/welshman/hytale-server-hub.git
cd hytale-server-hub
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Locally

```bash
# Start a local web server
python -m http.server 8000

# Visit: http://localhost:8000
```

## Running the Scraper

### Manual Execution

```bash
# Run once
python scraper.py

# Check data/servers.json for updated server list
```

### Automated with GitHub Actions

The project includes a GitHub Actions workflow that:
- Runs automatically every day at 12:00 UTC
- Can be manually triggered anytime

**To trigger manually:**
1. Go to your repository on GitHub
2. Click "Actions" tab
3. Click "Daily Hytale Server Scrape"
4. Click "Run workflow"

## Deployment to GitHub Pages

### Step 1: Enable GitHub Pages

1. Go to your repository **Settings**
2. Scroll to "GitHub Pages" section
3. Set source to `main` branch, root folder
4. Click Save

### Step 2: Wait for Deployment

GitHub will automatically:
- Build the site
- Deploy to GitHub Pages
- Update `gh-pages` branch

Your site will be available at:
```
https://[your-username].github.io/hytale-server-hub/
```

### Step 3: Share the Link

Your live server listing is now publicly accessible!

## Customization

### Adding New Server Types

**In `index.html`** (around line 385):

```html
<button class="tag-btn" data-type="NewType">New Type</button>
```

**In `scraper.py`** (around line 26):

```python
server_types = [
    'Vanilla', 'SMP', 'PvP', 'NewType',  # Add here
    # ... rest of types
]
```

### Changing Scrape Schedule

**In `.github/workflows/scrape-daily.yml`** (around line 8):

```yaml
on:
  schedule:
    # Use crontab.guru to generate expressions
    - cron: '0 12 * * *'  # Daily at 12:00 UTC
```

Common examples:
- `0 12 * * *` = Daily at 12:00 UTC
- `0 */6 * * *` = Every 6 hours
- `0 0 * * 0` = Weekly on Sunday at 00:00 UTC
- `*/30 * * * *` = Every 30 minutes

### Changing Website Colors

**In `index.html`** (around line 13), modify the CSS variables:

```css
:root {
    --primary: #6366f1;          /* Main color */
    --primary-dark: #4f46e5;     /* Hover color */
    --secondary: #8b5cf6;        /* Secondary color */
    --bg-dark: #0f172a;          /* Background */
    --bg-card: #1e293b;          /* Card background */
    --text-light: #f1f5f9;       /* Text color */
    --text-muted: #cbd5e1;       /* Muted text */
    --border: #334155;           /* Border color */
    --success: #10b981;          /* Success color */
    --warning: #f59e0b;          /* Warning color */
}
```

### Adding Regions

**In `index.html`** (around line 366):

```html
<select id="regionFilter" class="filter-input">
    <option value="">All Regions</option>
    <option value="New Region">New Region</option>
    <!-- ... other regions -->
</select>
```

**In `scraper.py`** (around line 18):

```python
regions = {
    'new region': 'New Region',  # Add here
    'spain': 'Spain',
    # ... other regions
}
```

## Manual Server Management

### Adding a Server

**Edit `data/servers.json`**:

```json
{
  "id": 21,
  "name": "Your Server Name",
  "description": "Brief description of the server and what makes it special.",
  "types": ["Vanilla", "SMP"],
  "ip": "play.yourserver.com",
  "region": "Your Country",
  "lastUpdated": "2026-01-08"
}
```

### Updating a Server

1. Find the server in `data/servers.json`
2. Update the fields you need to change
3. Update the `lastUpdated` date
4. Save and commit

### Removing a Server

1. Remove the entire server object from `data/servers.json`
2. Make sure there's no trailing comma
3. Save and commit

## Troubleshooting

### Website not loading

1. Check browser console for errors (F12)
2. Verify `data/servers.json` exists
3. Check that the file path is correct
4. Try clearing browser cache (Ctrl+Shift+Del)

### Scraper not running

1. Check GitHub Actions logs:
   - Go to "Actions" tab
   - Click "Daily Hytale Server Scrape"
   - Click the latest run
2. Verify `requirements.txt` is up to date
3. Check for network/firewall issues

### Servers not updating

1. Run scraper manually: `python scraper.py`
2. Check `data/servers.json` timestamp
3. Review GitHub Actions logs for errors
4. Verify JSON syntax is valid

### Website won't deploy to GitHub Pages

1. Go to repository "Settings"
2. Check "GitHub Pages" section is configured
3. Wait 1-2 minutes for deployment
4. Check Actions tab for deployment status
5. Clear browser cache if it still shows old version

## Development

### Project Structure

```
.
├── index.html                 # Main website
├── scraper.py                 # Web scraper
├── data/
│   └── servers.json            # Server data
├── .github/workflows/
│   └── scrape-daily.yml       # Automation
├── requirements.txt           # Python deps
├── README.md                 # Main docs
├── SETUP.md                  # This file
└── .gitignore                # Git config
```

### File Descriptions

- **index.html** - Interactive web interface (standalone, no build needed)
- **scraper.py** - Python script that crawls server listing websites
- **servers.json** - Database of servers (auto-updated by scraper)
- **scrape-daily.yml** - GitHub Actions workflow (auto-runs scraper)
- **requirements.txt** - Python dependencies

## Advanced Configuration

### Environment Variables

The project doesn't require environment variables by default, but you could add:

1. Create `.env` file (in `.gitignore`)
2. Add variables like:
   ```
   SCRAPE_DELAY=2
   MAX_RETRIES=3
   ```
3. Modify `scraper.py` to read them

### Custom Webhook Notifications

You can add Discord/Slack notifications after successful scrapes:

1. Add webhook URL to GitHub Secrets
2. Modify workflow to call webhook
3. Receive notifications of successful updates

### Database Integration

For larger scale, consider:

1. Moving from JSON to a database (Firebase, MongoDB)
2. Adding a backend API (Flask, Node.js)
3. Implementing user accounts/favorites
4. Adding server ratings/reviews

## Support

- 📧 **Issues**: [GitHub Issues](https://github.com/welshman/hytale-server-hub/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/welshman/hytale-server-hub/discussions)
- 🌐 **Website**: [Live Site](https://welshman.github.io/hytale-server-hub/)

---

**Happy hosting! 🎮**
