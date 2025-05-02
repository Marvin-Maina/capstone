import cv2
import time
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from send_email import send_email

class MotionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Motion Detection App")
        self.running = False
        self.cap = None
        self.frame1_gray = None
        self.last_email_time = 0
        self.email_cooldown = 60

        # UI
        self.start_button = tk.Button(root, text="Start Detection", command=self.start_detection)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop Detection", command=self.stop_detection, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.status_label = tk.Label(root, text="Status: Idle", fg="blue")
        self.status_label.pack(pady=10)

        self.video_label = tk.Label(root)
        self.video_label.pack()

    def start_detection(self):
        self.cap = cv2.VideoCapture(0)
        ret, frame1 = self.cap.read()
        if not ret:
            messagebox.showerror("Error", "Failed to access the webcam.")
            return

        self.frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        self.frame1_gray = cv2.GaussianBlur(self.frame1_gray, (21, 21), 0)

        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.status_label.config(text="Status: Running", fg="green")

        self.update_frame()

    def stop_detection(self):
        self.running = False
        if self.cap:
            self.cap.release()
        self.video_label.config(image='')
        self.status_label.config(text="Status: Stopped", fg="red")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def update_frame(self):
        if not self.running:
            return

        ret, frame2 = self.cap.read()
        if not ret:
            return

        frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        frame2_gray = cv2.GaussianBlur(frame2_gray, (21, 21), 0)

        diff = cv2.absdiff(self.frame1_gray, frame2_gray)
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        motion_detected = False
        for contour in contours:
            if cv2.contourArea(contour) < 1000:
                continue
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)
            motion_detected = True

        status_text = "Motion Detected" if motion_detected else "No Motion"
        color = (0, 0, 255) if motion_detected else (0, 255, 0)
        cv2.putText(frame2, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        current_time = time.time()
        if motion_detected and (current_time - self.last_email_time > self.email_cooldown):
            print("Motion detected! Sending email...")
            send_email()
            self.last_email_time = current_time

        self.frame1_gray = frame2_gray

        
        frame_rgb = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        imgtk = ImageTk.PhotoImage(image=img)
        self.video_label.imgtk = imgtk
        self.video_label.config(image=imgtk)

        self.root.after(30, self.update_frame)  

if __name__ == "__main__":
    root = tk.Tk()
    app = MotionApp(root)
    root.mainloop()
