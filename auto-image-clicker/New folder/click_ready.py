import pyautogui
import time
import keyboard
import os
import sys

# Check Python version
if sys.version_info < (3, 8):
    print("Python 3.8 or higher is required.")
    sys.exit(1)

# Image path (relative)
IMAGE_PATH = os.path.join("assets", "ready.png")

time.sleep(3)
print("▶️ Script is running...")
print("❌ Press Ctrl + X to exit")

while True:
    if keyboard.is_pressed('ctrl+x'):
        print("⛔ Exit key pressed. Closing script...")
        break

    try:
        location = pyautogui.locateOnScreen(IMAGE_PATH, confidence=0.8)
    except Exception:
        time.sleep(1)
        continue

    if location:
        x, y = pyautogui.center(location)
        pyautogui.click(x, y)
        print("🖱️ Image found. Clicked.")
        time.sleep(1)
    else:
        print("🔍 Image not found. Scanning...")
        time.sleep(1)
