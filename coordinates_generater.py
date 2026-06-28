# show_coordinates.py
import pyautogui
import time

print("🎯 Live Coordinate Tracker")
print("Move your mouse anywhere to see coordinates")
print("Press Ctrl+C to exit")
print("="*50)

try:
    while True:
        # Get current mouse position
        x, y = pyautogui.position()
        
        # Clear the line and show coordinates
        print(f"\r📍 X: {x:4d}  Y: {y:4d}  ", end="", flush=True)
        
        # Small delay to prevent CPU overuse
        time.sleep(0.1)
        
except KeyboardInterrupt:
    print("\n\n✅ Exited! Final coordinates were:")
    x, y = pyautogui.position()
    print(f"📍 X: {x}, Y: {y}")
    print("\n👋 Goodbye!")