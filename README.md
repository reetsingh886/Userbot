<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=43cea2,185a9d&height=200&section=header&text=Telegram%20Userbot%20AutoMessage&fontSize=40&fontColor=ffffff" />
</p>

<p align="center">
  <b>🤖 Telegram Userbot to auto-send messages at intervals from your own account!</b><br>
  <i>Built for reminders, automation, promotion, alerts, or fun! Deployed on Heroku or Replit!</i>
</p>

<p align="center">
  <a href="https://github.com/babaji067/userbot">
    <img src="https://img.shields.io/github/stars/babaji067/userbot?style=flat-square&color=yellow" />
  </a>
  <a href="https://github.com/babaji067/userbot/fork">
    <img src="https://img.shields.io/github/forks/babaji067/userbot?style=flat-square&color=blue" />
  </a>
  <a href="https://github.com/babaji067/userbot/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/babaji067/userbot?style=flat-square&color=lightgrey" />
  </a>
</p>

---

## 🖼️ Preview Screenshot

> Below is how your Telegram userbot looks when running.

<p align="center">
  <img src="https://raw.githubusercontent.com/babaji067/userbot/main/assets/screenshot.png" width="600" alt="Bot Preview">
</p>

---

## 🚀 Deploy to Heroku

Click below to deploy directly on Heroku:

<p align="center">
  <a href="https://heroku.com/deploy?template=https://github.com/reetsingh886/Userbot">
    <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heroku">
  </a>
</p>

---

## 🧰 Features

✅ Auto-send message to chats/groups  
✅ Easily configure delay + message  
✅ Secure session system  
✅ Simple `/autosend` and `/autostop`  
✅ Fully open-source

---

## ⚙️ Config Vars (Set in Heroku)

| Variable         | Required | Description                             |
|------------------|----------|-----------------------------------------|
| `API_ID`         | ✅        | From [my.telegram.org](https://my.telegram.org) |
| `API_HASH`       | ✅        | Same as above                          |
| `SESSION_STRING` | ✅        | Generated via code below               |

---

## ✨ Commands Guide

| Command              | Description                                  |
|----------------------|----------------------------------------------|
| `/setmessage`        | Set the auto-send message                    |
| `/setmute 60`        | Set delay (in seconds, e.g. 60 seconds)      |
| `/autosend`          | Starts auto messaging                        |
| `/autostop`          | Stops messaging                              |

---

## 🔐 Session String Generator

> Use this to create `SESSION_STRING` for Heroku config

```python
from pyrogram import Client
api_id = int(input("API ID: "))
api_hash = input("API HASH: ")
with Client(":session", api_id, api_hash) as app:
    print("Session String:", app.export_session_string())
