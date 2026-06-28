# 🤖 WhatsApp Chat Bot Ai

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()
[![WhatsApp](https://img.shields.io/badge/WhatsApp-Web-blue.svg)](https://web.whatsapp.com)
[![Gemini](https://img.shields.io/badge/Gemini-AI-orange.svg)](https://deepmind.google/technologies/gemini/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

> **An intelligent WhatsApp bot that reads messages and replies automatically using Google's Gemini AI. Built with Python and PyAutoGUI.**

## 📸 Demo

![WhatsApp Bot Demo](https://via.placeholder.com/800x400?text=WhatsApp+Bot+Demo)

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔄 **Auto-Read** | Automatically reads the latest message from the active chat |
| 🤖 **AI Replies** | Uses Google Gemini AI to generate natural, contextual responses |
| 💬 **Conversational** | Responds like a real person named Marcus |
| 🌐 **Web Integration** | Works seamlessly with WhatsApp Web in Chrome |
| 🎯 **Easy Setup** | Simple coordinate configuration with visual guide |
| 🔒 **Secure** | API keys stored in .env file (not in code) |
| 📝 **Chat History** | Maintains context for more natural conversations |
| 🎭 **Multi-language** | Supports both English and Hindi responses |
| ⚡ **Fast** | Quick response generation with Gemini Flash model |

## 📋 Table of Contents

- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Disclaimer](#-disclaimer)

## 📋 Prerequisites

Before you begin, ensure you have:

### 🖥️ System Requirements
- **Windows 10/11** (Mac/Linux support coming soon)
- **Python 3.8** or higher
- **Google Chrome** browser
- **WhatsApp Account** (active)

### 🔑 API Requirements
- **Google Gemini API Key** ([Get it here](https://ai.google.dev/))
- **Internet Connection**

### 📦 Required Python Packages
pyautogui - Mouse/keyboard automation
pyperclip - Clipboard management
pygetwindow - Window management
python-dotenv - Environment variables
google-generativeai - Gemini API client
Pillow - Image processing (optional)
opencv-python - Computer vision (optional)

text

## 🚀 Installation

### Step 1: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/nk2492962-byte/whatsapp-chat_bot.Ai.git

# Navigate to project directory
cd whatsapp-chat_bot.Ai
Step 2: Set Up Virtual Environment (Recommended)
bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
Step 3: Install Dependencies
bash
# Install required packages
pip install -r requirements.txt

# Or install individually
pip install pyautogui pyperclip pygetwindow python-dotenv google-generativeai
Step 4: Set Up API Key
Get your Gemini API key:

Go to Google AI Studio

Create or sign in with your Google account

Navigate to "Get API Key"

Create a new API key

Copy the key

Create .env file:

bash
# Create .env file
echo "GEMINI_API_KEY=your_api_key_here" > .env
Or manually create .env file in the project root:

text
GEMINI_API_KEY=AIzaSy...your_actual_key_here
Step 5: Verify Installation
bash
# Test the API connection
python test_api.py

# Expected output:
# ✅ API Key found!
# ✅ Gemini API connection successful!
# Test response: Hello! 👋
🎯 Configuration
Finding Your Screen Coordinates
The bot needs to know where to click on your screen. Use the coordinate finder:

bash
# Run the coordinate finder
python find_coords.py
Follow these steps:

Open WhatsApp Web in Chrome

Open a chat with someone

Run find_coords.py

Move your mouse to the specified positions when prompted:

📍 TOP-LEFT of the message area (where the first message appears)

📍 BOTTOM-RIGHT of the message area (where the last message appears)

📍 CENTER of the input box (where you type)

The script will output coordinates like:

text
MESSAGE_START_X = 479
MESSAGE_START_Y = 148
MESSAGE_END_X = 1348
MESSAGE_END_Y = 687
INPUT_BOX_X = 995
INPUT_BOX_Y = 725
Updating Coordinates
Open whatsapp_bot.py and update these values:

python
# ============================================
# COORDINATES - UPDATE WITH YOUR VALUES
# ============================================
MESSAGE_START_X = 479   # Your value
MESSAGE_START_Y = 148   # Your value
MESSAGE_END_X = 1348    # Your value
MESSAGE_END_Y = 687     # Your value
INPUT_BOX_X = 995       # Your value
INPUT_BOX_Y = 725       # Your value
# ============================================
🚀 Usage
Basic Usage
bash
# Run the bot
python whatsapp_bot.py
Step-by-Step Guide
Launch the bot:

bash
python whatsapp_bot.py
Wait for WhatsApp Web to open:

The bot will open WhatsApp Web in Chrome

Scan QR code with your phone if needed

Wait for the chat list to load

Select a chat:

Manually click on any chat in the left sidebar

Make sure the chat is open and messages are visible

The bot will detect the active chat

Bot starts working:

Reads the latest message

Generates an AI response

Sends the reply automatically

Waits for new messages

Stop the bot:

Press Ctrl+C in the terminal

The bot will show a summary

Example Interaction
text
🤖 Bot is running!
🔄 Checking for new messages... (Loop #1)
📖 Reading message...
📝 Message: Hey! How are you doing?

🤔 Generating response...
💬 Response: I'm doing great! Thanks for asking. How about you? 😊

✍️ Sending response...
✅ Response sent!
⏳ Waiting 30 seconds before next check...
🔧 How It Works
Architecture
text
┌─────────────────────────────────────────────────────────────┐
│                     WhatsApp Bot System                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐ │
│  │  WhatsApp    │    │   PyAutoGUI  │    │   Gemini AI  │ │
│  │    Web       │◄───│   Automation │───►│    API       │ │
│  └──────────────┘    └──────────────┘    └──────────────┘ │
│        ▲                    ▲                    ▲         │
│        │                    │                    │         │
│  ┌─────┴─────┐      ┌──────┴──────┐      ┌─────┴─────┐   │
│  │ Read Msg  │      │ Click/Type  │      │ Generate  │   │
│  │           │      │             │      │ Response  │   │
│  └───────────┘      └─────────────┘      └───────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
Workflow
Window Activation

Finds WhatsApp Web window

Activates and maximizes it

Message Reading

Clicks in message area

Selects and copies text

Extracts the latest message

AI Response Generation

Sends message to Gemini API

Maintains chat history for context

Returns natural response

Reply Sending

Clicks input box

Pastes the response

Sends the message

🛠️ Troubleshooting
Common Issues and Solutions
1. "Hey! Sorry about that. Can you say that again?"
Problem: Gemini API is not working

Solutions:

bash
# Test your API connection
python test_api.py

# Check .env file
cat .env  # Should show: GEMINI_API_KEY=your_key

# Regenerate API key
# Go to Google AI Studio and create a new key
2. Bot Clicks Wrong Areas
Problem: Coordinates are incorrect

Solutions:

bash
# Re-run coordinate finder
python find_coords.py

# Make sure WhatsApp Web is maximized
# The bot automatically maximizes the window
3. "Could not find WhatsApp Web window"
Problem: Chrome not detected

Solutions:

Manually open WhatsApp Web in Chrome

Make sure Chrome is installed

Check if Chrome is in default location

4. Bot Not Reading Messages
Problem: Selection area wrong

Solutions:

Make sure chat is open and scrolled to bottom

Click on the chat manually first

Update coordinates

5. API Key Not Found
Problem: .env file not loaded

Solutions:

bash
# Make sure .env is in the same folder
ls -la | grep .env

# Create .env with correct format
echo "GEMINI_API_KEY=your_key_here" > .env
Debug Mode
Run with debug logging:

python
# Add this at the top of whatsapp_bot.py
import logging
logging.basicConfig(level=logging.DEBUG)
🤝 Contributing
Contributions are welcome! Here's how you can help:

Ways to Contribute
🐛 Report bugs - Create an issue

💡 Suggest features - Open a discussion

📝 Improve documentation - Submit a PR

🔧 Fix issues - Submit a pull request

⭐ Star the project - Show your support

Development Setup
bash
# Fork the repository
# Clone your fork
git clone https://github.com/nk2492962-byte/whatsapp-chat_bot.Ai.git

# Create a new branch
git checkout -b feature/your-feature

# Make changes
# Test your changes

# Commit and push
git add .
git commit -m "Add: your feature description"
git push origin feature/your-feature

# Create a pull request
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

text
MIT License

Copyright (c) 2024 Nk2492962-byte

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
⚠️ Disclaimer
Important: This bot is for educational purposes only.

🚫 Don't use for spam - This violates WhatsApp's Terms of Service

🚫 Don't automate illegal activities

✅ Use responsibly - Only for learning and personal use

✅ Respect privacy - Don't store messages without consent

WhatsApp Terms of Service
Using automated bots may violate WhatsApp's Terms of Service:

WhatsApp Terms of Service

This bot is for educational purposes only

Use at your own risk

🙏 Acknowledgments
Google Gemini AI - For the powerful AI API

PyAutoGUI - For cross-platform automation

All contributors - For making this project better

📞 Support
Where to Get Help
Issues: GitHub Issues

Discussions: GitHub Discussions

🚀 Roadmap
Upcoming Features
Support for Mac/Linux

GUI Configuration Tool

Multiple Language Support

Customizable Response Templates

Message Filtering

Scheduled Replies

Web Dashboard

💖 Support the Project
If you find this project helpful, consider:

⭐ Starring the repository

🍴 Forking the repository

📢 Sharing with others

📝 Quick Start Commands
bash
# Clone the repository
git clone https://github.com/nk2492962-byte/whatsapp-chat_bot.Ai.git
cd whatsapp-chat_bot.Ai

# Install dependencies
pip install -r requirements.txt

# Set up API key
echo "GEMINI_API_KEY=your_key_here" > .env

# Find coordinates
python find_coords.py

# Run the bot
python whatsapp_bot.py
Made with ❤️ by Nk2492962-byte

https://img.shields.io/github/followers/nk