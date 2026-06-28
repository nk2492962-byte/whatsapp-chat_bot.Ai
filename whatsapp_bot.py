# whatsapp_bot.py
import time
import pyautogui
import pyperclip
import os
import pygetwindow as gw
import webbrowser
from dotenv import load_dotenv
from google import genai
import re
import subprocess

# Load environment variables
load_dotenv()

# Initialize Gemini client
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)

print("✓ Gemini API loaded successfully!")
print("🤖 WhatsApp Bot Starting...")

# Screen size
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
print(f"📱 Screen resolution: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")

# ============================================
# COORDINATES - UPDATE THESE WITH YOUR VALUES
# Run find_coords.py or manually update these
# ============================================
MESSAGE_START_X = 479   # Top-left of message area
MESSAGE_START_Y = 148   # Top-left of message area
MESSAGE_END_X = 1348    # Bottom-right of message area
MESSAGE_END_Y = 687     # Bottom-right of message area
INPUT_BOX_X = 995       # Center of input box
INPUT_BOX_Y = 725       # Center of input box
# ============================================

def open_whatsapp_web():
    """Open WhatsApp Web in Chrome"""
    try:
        print("🌐 Opening WhatsApp Web...")
        
        # Check if already open
        windows = gw.getWindowsWithTitle('WhatsApp')
        if windows:
            print("✅ WhatsApp Web already open!")
            return True
        
        # Open in Chrome
        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        ]
        
        for chrome_path in chrome_paths:
            if os.path.exists(chrome_path):
                subprocess.Popen([chrome_path, "https://web.whatsapp.com"])
                print("✅ Opening WhatsApp Web in Chrome...")
                break
        else:
            webbrowser.open("https://web.whatsapp.com")
            print("✅ Opening WhatsApp Web in default browser...")
        
        print("⚠️  Please scan QR code with your phone if needed")
        print("⏳ Waiting 30 seconds for WhatsApp to load...")
        time.sleep(30)
        return True
        
    except Exception as e:
        print(f"❌ Error opening WhatsApp: {e}")
        return False

def find_whatsapp_window():
    """Find the Chrome window with WhatsApp Web"""
    try:
        # Try to find WhatsApp window
        windows = gw.getWindowsWithTitle('WhatsApp')
        if windows:
            print(f"✅ Found WhatsApp window: {windows[0].title}")
            return windows[0]
        
        # Try Chrome with WhatsApp
        chrome_windows = gw.getWindowsWithTitle('Chrome')
        for window in chrome_windows:
            if 'WhatsApp' in window.title or 'web.whatsapp.com' in window.title.lower():
                print(f"✅ Found WhatsApp in Chrome: {window.title}")
                return window
        
        # Use first Chrome window
        if chrome_windows:
            print(f"✅ Using Chrome window: {chrome_windows[0].title}")
            return chrome_windows[0]
        
        return None
        
    except Exception as e:
        print(f"❌ Error finding window: {e}")
        return None

def activate_whatsapp_window():
    """Activate the WhatsApp Web window"""
    try:
        window = find_whatsapp_window()
        if window:
            if window.isMinimized:
                window.restore()
            window.activate()
            time.sleep(1)
            
            # Try to maximize
            try:
                window.maximize()
                time.sleep(1)
            except:
                pass
            
            return True
        else:
            print("❌ Could not find WhatsApp Web window")
            return False
    except Exception as e:
        print(f"❌ Error activating window: {e}")
        return False

def read_whatsapp_message():
    """Read the latest WhatsApp message"""
    try:
        print("📖 Reading message...")
        
        # Click in message area to focus
        pyautogui.click(MESSAGE_START_X + 50, MESSAGE_START_Y + 50)
        time.sleep(0.3)
        
        # Method 1: Try drag selection
        print("🔄 Selecting messages...")
        pyautogui.moveTo(MESSAGE_START_X + 50, MESSAGE_START_Y + 50)
        pyautogui.dragTo(MESSAGE_END_X - 50, MESSAGE_END_Y - 50, duration=0.5, button='left')
        time.sleep(0.2)
        
        # Copy selected text
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.3)
        
        # Get text from clipboard
        full_text = pyperclip.paste().strip()
        
        # If drag didn't work, try triple click
        if not full_text:
            print("🔄 Trying triple click method...")
            pyautogui.click(MESSAGE_END_X - 50, MESSAGE_END_Y - 50)
            time.sleep(0.2)
            pyautogui.click(MESSAGE_END_X - 50, MESSAGE_END_Y - 50)
            time.sleep(0.2)
            pyautogui.click(MESSAGE_END_X - 50, MESSAGE_END_Y - 50)
            time.sleep(0.2)
            pyautogui.hotkey("ctrl", "c")
            time.sleep(0.3)
            full_text = pyperclip.paste().strip()
        
        # Extract last message
        if full_text:
            lines = full_text.split('\n')
            message = ""
            
            # Find last meaningful message
            for line in reversed(lines):
                line = line.strip()
                if line and len(line) > 3:
                    # Skip timestamps and metadata
                    if not re.match(r'^[\d:]+$', line) and not line.startswith('['):
                        message = line
                        break
            
            if not message and lines:
                message = lines[-1].strip()
            
            if message:
                # Clean up
                message = re.sub(r'^[\W_]+', '', message)
                message = message.strip()
                print(f"📝 Message: {message[:50]}..." if len(message) > 50 else f"📝 Message: {message}")
                return message
        
        print("⚠️ No message found")
        return None
        
    except Exception as e:
        print(f"❌ Error reading message: {e}")
        return None

def send_whatsapp_message(response):
    """Send a response message"""
    try:
        print("✍️ Sending response...")
        
        # Click input box
        pyautogui.click(INPUT_BOX_X, INPUT_BOX_Y)
        time.sleep(0.3)
        
        # Clear input
        pyautogui.hotkey("ctrl", "a")
        time.sleep(0.1)
        pyautogui.press("delete")
        time.sleep(0.1)
        
        # Type response
        pyperclip.copy(response)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.3)
        
        # Send
        pyautogui.press("enter")
        print("✅ Response sent!")
        return True
        
    except Exception as e:
        print(f"❌ Error sending message: {e}")
        return False

def get_gemini_response(message, chat_history=""):
    """Get response from Gemini API"""
    try:
        system_prompt = """You are Marcus, a friendly and helpful person from India who speaks both Hindi and English.
        You're chatting on WhatsApp. Respond naturally, conversationally, and keep your replies short (1-3 sentences).
        Be warm, friendly, and engaging like you're talking to a friend.
        If someone asks for code, provide clean, working code.
        If someone asks for help, be supportive and practical."""
        
        full_prompt = f"{system_prompt}\n\nChat History: {chat_history}\nLatest Message: {message}\n\nMarcus's Reply:"
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=full_prompt
        )
        
        return response.text.strip()
        
    except Exception as e:
        print(f"❌ Error getting Gemini response: {e}")
        return "Hey! Sorry about that. Can you say that again? 😊"

def auto_reply():
    """Main function to automate WhatsApp replies"""
    print("="*60)
    print("WhatsApp Auto-Reply Bot (Marcus)")
    print("="*60)
    print("📌 HOW IT WORKS:")
    print("   1. Opens WhatsApp Web in Chrome")
    print("   2. YOU manually select a chat")
    print("   3. Bot reads the latest message")
    print("   4. Generates response using Gemini AI")
    print("   5. Sends the reply automatically")
    print("="*60)
    
    # Open WhatsApp Web
    if not open_whatsapp_web():
        print("❌ Could not open WhatsApp Web")
        return
    
    # Activate WhatsApp window
    if not activate_whatsapp_window():
        print("❌ Could not find WhatsApp Web window")
        print("Please open WhatsApp Web in Chrome manually and try again.")
        return
    
    # Wait for user to select a chat
    print("\n" + "="*60)
    print("👆 PLEASE SELECT A CHAT MANUALLY")
    print("="*60)
    print("1. Click on any chat in the left sidebar")
    print("2. Make sure the chat is open and visible")
    print("3. The bot will then start reading messages")
    print("="*60)
    print("\n⏳ Waiting 15 seconds for you to select a chat...")
    for i in range(15, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    
    # Start the bot
    print("\n" + "="*60)
    print("🤖 Bot is running!")
    print("📋 It will read messages and reply automatically")
    print("="*60)
    
    chat_history = ""
    last_message = ""
    message_count = 0
    
    while True:
        try:
            print(f"\n🔄 Checking for new messages... (Loop #{message_count + 1})")
            
            # Read message
            message = read_whatsapp_message()
            
            # Check if it's new
            if message and message != last_message and message.strip():
                message_count += 1
                print(f"📩 New message detected! (#{message_count})")
                last_message = message
                
                # Generate response
                print("🤔 Generating response...")
                response = get_gemini_response(message, chat_history)
                print(f"💬 Response: {response[:100]}..." if len(response) > 100 else f"💬 Response: {response}")
                
                # Send response
                send_whatsapp_message(response)
                
                # Update history
                chat_history += f"\nUser: {message}\nMarcus: {response}"
                chat_history = '\n'.join(chat_history.split('\n')[-20:])
                
                print("⏳ Waiting 30 seconds before next check...")
                time.sleep(30)
            else:
                if message == last_message and message:
                    print("⏳ Same message, waiting for new messages...")
                else:
                    print("⏳ No new message found")
                time.sleep(10)
                
        except KeyboardInterrupt:
            print("\n" + "="*60)
            print(f"👋 Bot stopped by user")
            print(f"📊 Total messages processed: {message_count}")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            print("⏳ Retrying in 10 seconds...")
            time.sleep(10)

if __name__ == "__main__":
    auto_reply()