# 🕵️‍♂️ Motion Detector App (with GUI)

A simple Python desktop app with a Tkinter GUI that detects motion using your webcam. When movement is detected, the app captures the frame, converts it for display using Pillow, and sends an alert straight to your Gmail inbox.

## 🖼️ GUI Preview

> Live camera feed with real-time motion alerts right from your desktop.

## 🚀 Features

- 🖥️ Tkinter GUI for live camera feed
- 🔍 Motion detection via OpenCV
- 🎨 Converts frames using Pillow (BGR ➡️ RGB)
- 📬 Sends Gmail alerts on detection
- 💾 Saves snapshots of detected movement

## 🛠️ Tech Stack

- Python 3.x
- Tkinter (GUI)
- OpenCV (motion tracking)
- Pillow (image conversion)
- smtplib + email.mime (Gmail alerts)

## 📦 Installation

1. **Clone the repo:**

   ```bash
   git clone https://github.com/your-username/motion-detector-gui.git
   cd motion-detector-gui
# 🕵️‍♂️ Motion Detector App (with GUI)

A simple Python desktop app with a Tkinter GUI that detects motion using your webcam. When movement is detected, the app captures the frame, converts it for display using Pillow, and sends an alert straight to your Gmail inbox.

## 🖼️ GUI Preview

> Live camera feed with real-time motion alerts right from your desktop.

## 🚀 Features

- 🖥️ Tkinter GUI for live camera feed
- 🔍 Motion detection via OpenCV
- 🎨 Converts frames using Pillow (BGR ➡️ RGB)
- 📬 Sends Gmail alerts on detection
- 💾 Saves snapshots of detected movement

## 🛠️ Tech Stack

- Python 3.x
- Tkinter (GUI)
- OpenCV (motion tracking)
- Pillow (image conversion)
- smtplib + email.mime (Gmail alerts)

## 📦 Installation

1. **Clone the repo:**

   ```bash
   git clone https://github.com/your-username/motion-detector-gui.git
   cd motion-detector-gui

2. **Install Dependencies**
```bash
pip install opencv-python Pillow

```
3.**Configure Gmail credentials in email_config.py**
```
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
RECEIVER_EMAIL = "recipient_email@gmail.com"
```
4.**▶️ How to Run**
```
python motion_detector_gui.py
```

