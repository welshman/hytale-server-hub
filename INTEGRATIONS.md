# Integrations & Extensions

This document shows how to integrate the Hytale Server Hub with other platforms and extend functionality.

---

## Discord Bot Integration

### Using the JSON API

You can fetch server data from your Discord bot:

```python
import discord
import json
import requests

bot = discord.ext.commands.Bot(command_prefix='!')

@bot.command(name='hytaleservers')
async def list_servers(ctx):
    """Fetch and display Hytale servers from the hub"""
    
    # Load servers from GitHub raw content
    url = 'https://raw.githubusercontent.com/welshman/hytale-server-hub/main/data/servers.json'
    response = requests.get(url)
    data = response.json()
    
    # Create Discord embed
    embed = discord.Embed(
        title="🎮 Hytale Servers",
        description="Available servers from Hytale Server Hub",
        color=discord.Color.purple()
    )
    
    # Add servers to embed
    for server in data['servers'][:10]:  # Show first 10
        embed.add_field(
            name=f"{server['name']} 🇻{server['region']}",
            value=f"`{server['ip']}`\n{server['description'][:100]}...",
            inline=False
        )
    
    embed.set_footer(text=f"Total servers: {len(data['servers'])}")
    await ctx.send(embed=embed)

bot.run('YOUR_TOKEN')
```

### Discord Webhook Notifications

Add to `.github/workflows/scrape-daily.yml`:

```yaml
- name: Notify Discord
  if: success()
  run: |
    curl -X POST ${{ secrets.DISCORD_WEBHOOK }} \
      -H 'Content-Type: application/json' \
      -d '{
        "content": "✅ Hytale servers updated at '$(date)'",
        "embeds": [{
          "title": "Server Hub Updated",
          "description": "Daily scrape completed",
          "color": 3066993
        }]
      }'
```

**Setup:**
1. Create Discord webhook in channel
2. Go to GitHub repo Settings → Secrets
3. Add `DISCORD_WEBHOOK` with webhook URL

---

## Slack Bot Integration

```python
from slack_bolt import App
import requests
import json

app = App(token="your-token", signing_secret="your-secret")

@app.command("/hytaleservers")
def handle_hytale_command(ack, body, respond):
    ack()
    
    # Fetch server data
    url = 'https://raw.githubusercontent.com/welshman/hytale-server-hub/main/data/servers.json'
    response = requests.get(url)
    data = response.json()
    
    # Format for Slack
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "🎮 Hytale Servers"
            }
        }
    ]
    
    for server in data['servers'][:5]:
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{server['name']}*\n`{server['ip']}`\n{server['description']}"
            }
        })
    
    respond(blocks=blocks)

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
```

---

## Website Embedding

### Embed Server List in Another Site

```html
<!-- In your website -->
<iframe 
    src="https://welshman.github.io/hytale-server-hub/" 
    width="100%" 
    height="600" 
    style="border: none; border-radius: 8px;"
></iframe>
```

### Fetch and Display Server Data

```html
<div id="hytale-servers"></div>

<script>
    async function loadHytaleServers() {
        const response = await fetch(
            'https://raw.githubusercontent.com/welshman/hytale-server-hub/main/data/servers.json'
        );
        const data = await response.json();
        
        const container = document.getElementById('hytale-servers');
        
        data.servers.forEach(server => {
            const div = document.createElement('div');
            div.className = 'server-card';
            div.innerHTML = `
                <h3>${server.name}</h3>
                <p>${server.description}</p>
                <code>${server.ip}</code>
                <span>${server.region}</span>
            `;
            container.appendChild(div);
        });
    }
    
    loadHytaleServers();
</script>
```

---

## API Endpoints

### Raw JSON Data

```
GET https://raw.githubusercontent.com/welshman/hytale-server-hub/main/data/servers.json
```

Returns complete server list:
```json
{
  "servers": [
    {
      "id": 1,
      "name": "Hytale Box",
      "description": "...",
      "types": [...],
      "ip": "play.hytale-box.com",
      "region": "Spain",
      "lastUpdated": "2026-01-08"
    }
  ]
}
```

### Query Parameters

You can filter in your client-side code:

```javascript
// Filter by type
const pvpServers = servers.filter(s => s.types.includes('PvP'));

// Filter by region
const usServers = servers.filter(s => s.region === 'United States');

// Search by name
const search = servers.filter(s => 
    s.name.toLowerCase().includes('vanilla')
);
```

---

## Webhook Updates

### Listen for Updates

Modify GitHub Actions to call your webhook:

```yaml
- name: Call Custom Webhook
  if: success()
  run: |
    curl -X POST https://yourapi.com/webhook \
      -H "Content-Type: application/json" \
      -d '{
        "event": "servers_updated",
        "timestamp": "'$(date -u +'%Y-%m-%dT%H:%M:%SZ')'",
        "repository": "hytale-server-hub",
        "action": "daily-scrape"
      }'
```

### Webhook Handler (Node.js/Express)

```javascript
const express = require('express');
const app = express();

app.post('/webhook', express.json(), (req, res) => {
    console.log('Servers updated:', req.body);
    
    // Trigger your own updates
    updateServerCache();
    notifyUsers();
    
    res.json({ success: true });
});

app.listen(3000);
```

---

## Database Sync

### Sync to Firebase

```python
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

# Initialize Firebase
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-project.firebaseio.com'
})

# Load servers
with open('data/servers.json') as f:
    data = json.load(f)

# Sync to Firebase
ref = db.reference('hytale_servers')
for server in data['servers']:
    ref.child(str(server['id'])).set(server)

print(f"Synced {len(data['servers'])} servers to Firebase")
```

### Sync to MongoDB

```python
from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')
db = client['hytale']
collection = db['servers']

with open('data/servers.json') as f:
    data = json.load(f)

# Delete old data and insert new
collection.delete_many({})
collection.insert_many(data['servers'])

print(f"Synced {len(data['servers'])} servers to MongoDB")
```

---

## Mobile App Integration

### React Native Example

```javascript
import React, { useState, useEffect } from 'react';
import { View, Text, FlatList, TouchableOpacity } from 'react-native';

export default function ServersScreen() {
    const [servers, setServers] = useState([]);
    
    useEffect(() => {
        fetch('https://raw.githubusercontent.com/welshman/hytale-server-hub/main/data/servers.json')
            .then(res => res.json())
            .then(data => setServers(data.servers));
    }, []);
    
    return (
        <FlatList
            data={servers}
            renderItem={({ item }) => (
                <View style={styles.card}>
                    <Text style={styles.name}>{item.name}</Text>
                    <Text>{item.description}</Text>
                    <TouchableOpacity onPress={() => copyIP(item.ip)}>
                        <Text style={styles.ip}>{item.ip}</Text>
                    </TouchableOpacity>
                </View>
            )}
            keyExtractor={item => item.id.toString()}
        />
    );
}
```

### Flutter Example

```dart
import 'package:http/http.dart' as http;
import 'dart:convert';

Future<List<HytaleServer>> fetchServers() async {
    final response = await http.get(
        Uri.parse('https://raw.githubusercontent.com/welshman/hytale-server-hub/main/data/servers.json')
    );
    
    if (response.statusCode == 200) {
        List jsonResponse = json.decode(response.body)['servers'];
        return jsonResponse.map((server) => HytaleServer.fromJson(server)).toList();
    } else {
        throw Exception('Failed to load servers');
    }
}
```

---

## Analytics Integration

### Track Popular Servers

```javascript
// Add to index.html
window.dataLayer = window.dataLayer || [];

function trackServerClick(serverName) {
    gtag('event', 'server_clicked', {
        'server_name': serverName,
        'event_category': 'servers'
    });
}

// Call when server is clicked
document.querySelectorAll('.copy-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        trackServerClick(this.dataset.serverName);
    });
});
```

---

## Advanced Features

### Server Health Check

Add to scraper to verify servers are online:

```python
import socket

def check_server_status(ip_address):
    try:
        # Try to resolve hostname
        socket.gethostbyname(ip_address)
        return 'online'
    except socket.gaierror:
        return 'offline'

# Add to each server
for server in servers:
    server['status'] = check_server_status(server['ip'])
```

### Server Ranking

Add popularity scoring:

```python
from datetime import datetime

def calculate_score(server):
    # Bonus for recent updates
    days_old = (datetime.now() - datetime.fromisoformat(server['lastUpdated'])).days
    recency_bonus = max(0, 10 - days_old)
    
    # Bonus for multiple features
    features_bonus = len(server['types']) * 2
    
    return recency_bonus + features_bonus

for server in servers:
    server['score'] = calculate_score(server)
```

---

## Contributing Extensions

Want to add an integration? 

1. Create a new file in `extensions/`
2. Document the integration
3. Submit a pull request
4. Share it with the community!

---

## Resources

- [Discord.py Documentation](https://discordpy.readthedocs.io/)
- [Slack Bolt Framework](https://slack.dev/bolt-python/)
- [Firebase Documentation](https://firebase.google.com/docs)
- [MongoDB Documentation](https://docs.mongodb.com/)
- [React Native Docs](https://reactnative.dev/)
- [Flutter Documentation](https://flutter.dev/docs)

---

**Have an integration idea? Open an issue on GitHub! 🌟**
