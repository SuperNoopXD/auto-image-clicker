import pyautogui
import time
import keyboard

image_path = r"C:\111111111111111111\auto ready\ready.png"

time.sleep(3)
print("▶️ Script is running...")
print("❌ Press Ctrl + X to exit")

while True:
    # Exit hotkey (ONLY way to stop)
    if keyboard.is_pressed('ctrl+x'):
        print("⛔ Exit key pressed. Closing script...")
        break

    try:
        location = pyautogui.locateOnScreen(image_path, confidence=0.8)
    except Exception:
        # Ignore any screen capture errors
        time.sleep(1)
        continue

    if location:
        x, y = pyautogui.center(location)
        pyautogui.click(x, y)
        print("🖱️ Image found. Clicked.")
        time.sleep(1)  # click every 1 second while visible
    else:
        print("🔍 Image not found. Scanning...")
        time.sleep(1)  # scan every 1 second
