# MOTION DETECTOR APP

#  Motion Detector App (with GUI)

A simple Python desktop app with a Tkinter GUI that detects motion using your webcam. When movement is detected, the app captures the frame, converts it for display using Pillow, and sends an alert straight to your Gmail inbox.

##  GUI Preview

> Live camera feed with real-time motion alerts right from your desktop.

##  Features

-  Tkinter GUI for live camera feed
- Motion detection via OpenCV
-  Converts frames using Pillow (BGR to RGB)
-  Sends Gmail alerts on detection


##  Tech Stack

- Python 3.x
- Tkinter (GUI)
- OpenCV (motion tracking)
- Pillow (image conversion)
- smtplib + email.mime (Gmail alerts)
