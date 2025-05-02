# main.py
import cv2
import numpy as np
import pygame
import threading


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Motion Controlled Game")
clock = pygame.time.Clock()


player = pygame.Rect(375, 500, 50, 50)
velocity_x = 0
speed = 10


motion_direction = None

# --- Motion Detection Setup ---
cap = cv2.VideoCapture(0)
_, frame1 = cap.read()
frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

def detect_motion():
    global frame1_gray, motion_direction

    while True:
        ret, frame2 = cap.read()
        if not ret:
            continue

        frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        diff = cv2.absdiff(frame1_gray, frame2_gray)
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        motion_direction = None
        for contour in contours:
            if cv2.contourArea(contour) > 3000:
                x, y, w, h = cv2.boundingRect(contour)
                center_x = x + w // 2
                if center_x < 200:
                    motion_direction = 'left'
                elif center_x > 400:
                    motion_direction = 'right'
                break

        frame1_gray = frame2_gray.copy()

# --- Start motion detection in background thread ---
motion_thread = threading.Thread(target=detect_motion, daemon=True)
motion_thread.start()

# --- Game Loop ---
running = True
while running:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player if motion detected
    if motion_direction == 'left':
        player.x -= speed
    elif motion_direction == 'right':
        player.x += speed

    # Boundaries
    if player.x < 0: player.x = 0
    if player.x > 750: player.x = 750

    # Draw player
    pygame.draw.rect(screen, (200, 0, 100), player)

    # Update display
    pygame.display.flip()
    clock.tick(30)

# Cleanup
cap.release()
cv2.destroyAllWindows()
pygame.quit()
