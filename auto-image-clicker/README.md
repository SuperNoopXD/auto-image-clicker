# 🖱️ Auto Image Clicker (Python)

A Python automation script that detects an image on screen and clicks it automatically.  
Useful for games and apps, such as auto-accepting matches in League of Legends.

---

## 🚀 Features
- Detects an image on screen using screenshot matching
- Clicks automatically when the image appears
- Adjustable confidence level
- Safe exit using a keyboard shortcut

---

## 🧰 Requirements
- Windows
- Python 3.8 or higher

---

## 📦 Installation

### 1️⃣ Install Python
Download Python from:
https://www.python.org/downloads/

During installation, make sure to check:
**Add Python to PATH**

---

### 2️⃣ Download the Project
- Download the repository as ZIP
- Extract the files to any folder

---

### 3️⃣ Install Dependencies
Open **Command Prompt** inside the project folder and run:
```bash
pip install -r requirements.txt
▶️ Usage

Put the image you want to detect inside the assets folder

Name the image:

ready.png


Run the script:

python main.py

⏳ How It Works

The script waits 3 seconds before starting

Scans the screen every second

Clicks automatically when the image is detected

Keeps running until stopped manually

⛔ Exit

Press the following keys to stop the script safely:

Ctrl + X (deafault)

⚠️ Notes

Run the script as Administrator if keyboard input does not work

Image detection accuracy depends on screen resolution and scaling

You can adjust detection sensitivity in the code by changing:

confidence = 0.8
