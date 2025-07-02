# gesture_browser
# 🖐️ Hands-Free Browser Automation 🚀

Welcome to **Hands-Free Browser Automation** — a gesture-controlled system that lets you **browse the web without touching your keyboard or mouse**!  
Built with **Python, OpenCV, and MediaPipe**, this project tracks your hand gestures in real-time and translates them into common browser actions.

## ⚙️ **Tech Stack**

- **Python**
- **MediaPipe** – Real-time hand tracking
- **OpenCV** – Video capture & image processing
- **PyAutoGUI** – Automate keyboard & mouse actions

---

## ✨ **Features**

✅ **Switch Tabs:** Raise index & middle fingers → `Ctrl + Tab`  
✅ **Open New Tab:** Raise index finger → `Ctrl + T`  
✅ **Close Tab:** Raise index, middle & ring fingers → `Ctrl + W`  
✅ **Zoom In:** Thumb up → `Ctrl + +`  
✅ **Play/Pause Video:** Make a fist → `Space`  
✅ **Take Screenshot:** Open palm → Save screenshot with timestamp  
✅ **Toggle Fullscreen:** Four fingers → `F11`

---

## 🚀 **How It Works**

1️⃣ **Hand Tracking:** Uses MediaPipe to detect hand landmarks in real-time  
2️⃣ **Gesture Detection:** Analyzes finger states (up/down)  
3️⃣ **Action Trigger:** Maps gestures to keyboard shortcuts using PyAutoGUI  
4️⃣ **Cooldown Timer:** Prevents multiple triggers while holding a gesture

---

## 🧩 **Project Structure**

