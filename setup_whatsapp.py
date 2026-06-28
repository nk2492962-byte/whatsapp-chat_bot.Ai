# setup_whatsapp.py
import subprocess
import sys

print("="*50)
print("WhatsApp Bot Setup")
print("="*50)

# Install requirements
print("📦 Installing dependencies...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "google-genai", "python-dotenv", "pyautogui", "pyperclip", "pygetwindow"])

print("\n✅ Installation complete!")

print("\n📋 Next steps:")
print("1. Run: python whatsapp_coordinates.py")
print("2. Follow the instructions to capture coordinates")
print("3. Update the coordinates in whatsapp_bot.py")
print("4. Run: python whatsapp_bot.py")

print("\n="*50)