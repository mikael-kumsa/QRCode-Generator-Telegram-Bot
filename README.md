# 🤖 QR Code Generator Bot

A sleek Telegram bot that transforms text into QR codes instantly.

![QR Code Bot](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram)
![Python](https://img.shields.io/badge/Python-3.8%2B-yellow?logo=python)

## ✨ Features

- 🚀 Instant QR code generation
- 💬 Simple conversation flow
- 🎨 Clean QR code output
- ⚡ Fast response times

## 🛠️ Setup

### Requirements
- Python 3.8+
- Telegram account
- Bot Token from [@BotFather](https://t.me/BotFather)

### Installation

1. **Clone and setup**
   ```bash
   git clone https://github.com/mikael-kumsa/QRCode-Generator-Telegram-Bot.git
   cd QRCode-Generator-Telegram-Bot
   pip install -r requirements.txt
   ```

2. **Configure environment**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` file:
   ```env
   BOT_TOKEN=your_telegram_bot_token_here
   ```

3. **Run the bot**
   ```bash
   python bot.py
   ```

## 🎯 Usage

1. Start chat with your bot on Telegram
2. Send `/start` command
3. Enter text to encode
4. Receive QR code image

**Example conversation:**
```
User: /start
Bot: 👋 Hi there! What do you want the content of your QR Code to be?
User: https://github.com
Bot: 📸 Here's your QR code! [QR Code Image]
```

## 🔧 Configuration

### Environment Variables
- `BOT_TOKEN` - Telegram Bot API token

### Dependencies
- `python-telegram-bot`
- `qrcode`
- `python-dotenv`
---

<div align="center">

** ⭐ Star this repo if you find it useful!**

</div>
```
