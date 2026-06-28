# auto_capture_no_input.py
import pyautogui
import time
import pygetwindow as gw

print("="*60)
print("     FULLY AUTOMATIC COORDINATE CAPTURE")
print("="*60)
print("\n📌 HOW IT WORKS:")
print("   1. Move your mouse to the position")
print("   2. The script captures automatically every 5 seconds!")
print("   3. No typing needed - just move your mouse!")
print("="*60)

def capture_position(label, delay=5):
    """Automatically capture position after delay"""
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
    # Try to find and activate WhatsApp
    print("\n🔍 Looking for WhatsApp window...")
    windows = gw.getWindowsWithTitle('Chrome') + gw.getWindowsWithTitle('WhatsApp')
    found = False
    
    for window in windows:
        try:
            if window.title and ('WhatsApp' in window.title or 'Web' in window.title):
                if window.isMinimized:
                    window.restore()
                window.activate()
                print(f"✅ Found and activated: {window.title}")
                found = True
                time.sleep(1)
                break
        except:
            pass
    
    if not found:
        print("⚠️ Could not find WhatsApp window automatically.")
        print("   Please make sure WhatsApp Web is open in Chrome.")
        print("   Continuing in 3 seconds...")
        time.sleep(3)
    
    print("\n" + "="*60)
    print("📋 CAPTURE 4 POSITIONS")
    print("="*60)
    print("\n  1. Chat name in left sidebar")
    print("  2. Start of message text")
    print("  3. End of message text (where you drag to)")
    print("  4. Text input box at bottom")
    print("\n" + "="*60)
    print("\n⚠️  Move your mouse to each position and wait!")
    print("   The script captures automatically every 5 seconds.")
    print("="*60)
    
    positions = {}
    
    # Give user time to prepare
    print("\n⏳ Starting in 5 seconds...")
    for i in range(5, 0, -1):
        print(f"   {i}...", end=" ", flush=True)
        time.sleep(1)
    print("\n   🚀 STARTED!")
    
    # 1. Chat name
    x, y = capture_position("1. CHAT NAME (left sidebar)", 5)
    positions['CHAT_X'] = x
    positions['CHAT_Y'] = y
    
    # 2. Start of message
    x, y = capture_position("2. START OF MESSAGE", 5)
    positions['START_X'] = x
    positions['START_Y'] = y
    
    # 3. End of message
    x, y = capture_position("3. END OF MESSAGE (drag to)", 5)
    positions['END_X'] = x
    positions['END_Y'] = y
    
    # 4. Input box
    x, y = capture_position("4. INPUT BOX (text area)", 5)
    positions['INPUT_X'] = x
    positions['INPUT_Y'] = y
    
    # Show results
    print("\n" + "="*60)
    print("✅ ALL 4 POSITIONS CAPTURED!")
    print("="*60)
    print("\n📊 YOUR COORDINATES:")
    print("-"*60)
    for key, value in positions.items():
        print(f"   {key} = {value}")
    print("-"*60)
    
    # Save to file
    with open('coordinates.txt', 'w') as f:
        f.write("# WhatsApp Bot Coordinates\n")
        f.write(f"# Captured on {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("# Copy these values into your whatsapp_bot.py\n\n")
        for key, value in positions.items():
            f.write(f"{key} = {value}\n")
    
    print("\n💾 Coordinates saved to 'coordinates.txt'")
    print("\n📝 COPY these values into your whatsapp_bot.py")
    print("="*60)
    print("\nPress Ctrl+C to exit")
    
    # Keep window open
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Done!")
    
except KeyboardInterrupt:
    print("\n\n❌ Cancelled by user")
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()