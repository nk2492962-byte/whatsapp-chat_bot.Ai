# capture_top_coordinates.py
import pyautogui
import time
import pygetwindow as gw

print("="*60)
print("     CAPTURE COORDINATES FOR TOP-BASED APPROACH")
print("="*60)
print("\n📌 You need to capture 4 positions:")
print("   1. Chat name at the TOP of the chat area")
print("   2. Start of message (where message begins)")
print("   3. End of message (where message ends)")
print("   4. Input box (where you type)")
print("="*60)

def capture_position(label, delay=4):
    """Capture position with countdown"""
    print(f"\n📍 {label}")
    print(f"   Move your mouse there...")
    print(f"   ⏳ Capturing in {delay} seconds...")
    
    for i in range(delay, 0, -1):
        print(f"   {i}...", end=" ", flush=True)
        time.sleep(1)
    
    x, y = pyautogui.position()
    print(f"\n   ✅ CAPTURED! Position: ({x}, {y})")
    return x, y

try:
    # Activate WhatsApp
    windows = gw.getWindowsWithTitle('Chrome') + gw.getWindowsWithTitle('WhatsApp')
    for window in windows:
        if window.title and ('WhatsApp' in window.title or 'Web' in window.title):
            if window.isMinimized:
                window.restore()
            window.activate()
            print(f"✅ Found and activated: {window.title}")
            time.sleep(1)
            break
    
    print("\n" + "="*60)
    print("📋 CAPTURE POSITIONS")
    print("="*60)
    print("\nMake sure a chat is OPEN in WhatsApp Web!")
    print("="*60)
    
    positions = {}
    
    print("\n⏳ Starting in 3 seconds...")
    time.sleep(3)
    
    # 1. Chat name at top
    print("\n👉 Move mouse to the CHAT NAME at the TOP of the chat area")
    x, y = capture_position("1. CHAT NAME (top)", 4)
    positions['TOP_NAME_X'] = x
    positions['TOP_NAME_Y'] = y
    
    # 2. Start of message
    print("\n👉 Move mouse to the START of a message in the chat")
    x, y = capture_position("2. START OF MESSAGE", 4)
    positions['START_X'] = x
    positions['START_Y'] = y
    
    # 3. End of message
    print("\n👉 Move mouse to the END of the same message")
    x, y = capture_position("3. END OF MESSAGE", 4)
    positions['END_X'] = x
    positions['END_Y'] = y
    
    # 4. Input box
    print("\n👉 Move mouse to the INPUT BOX at the bottom")
    x, y = capture_position("4. INPUT BOX", 4)
    positions['INPUT_X'] = x
    positions['INPUT_Y'] = y
    
    # Show results
    print("\n" + "="*60)
    print("✅ ALL POSITIONS CAPTURED!")
    print("="*60)
    print("\n📊 YOUR COORDINATES:")
    print("-"*60)
    for key, value in positions.items():
        print(f"   {key} = {value}")
    print("-"*60)
    
    # Save to file
    with open('top_coordinates.txt', 'w') as f:
        f.write("# WhatsApp Bot Coordinates (Top-based approach)\n")
        f.write(f"# Captured on {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        for key, value in positions.items():
            f.write(f"{key} = {value}\n")
    
    print("\n💾 Coordinates saved to 'top_coordinates.txt'")
    print("\n📝 COPY these values into your whatsapp_bot_top.py")
    print("="*60)
    
except KeyboardInterrupt:
    print("\n\n❌ Cancelled by user")
except Exception as e:
    print(f"\n❌ Error: {e}")