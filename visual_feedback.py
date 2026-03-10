"""
Air Canvas Studio - Visual Feedback
Handles cursor, mode indicators, and visual cues.
"""

import cv2
import numpy as np

# Visual settings
CURSOR_RADIUS = 10
CURSOR_THICKNESS = 2
MODE_COLORS = {
    "draw": (0, 255, 0),
    "select": (255, 255, 0),
    "erase": (0, 0, 255),
    "idle": (128, 128, 128)
}
FONT = cv2.FONT_HERSHEY_SIMPLEX


def draw_cursor(frame, landmarks, current_mode):
    if "index_tip" not in landmarks:
        return frame

    x, y = landmarks["index_tip"]
    color = MODE_COLORS.get(current_mode, (255, 255, 255))

    if current_mode == "draw":
        cv2.circle(frame, (x, y), CURSOR_RADIUS, color, -1)
    elif current_mode == "erase":
        cv2.circle(frame, (x, y), CURSOR_RADIUS + 5, color, CURSOR_THICKNESS)
    else:
        cv2.circle(frame, (x, y), CURSOR_RADIUS, color, CURSOR_THICKNESS)

    return frame



def display_mode_indicator(frame, current_mode):
    text = f"MODE: {current_mode.upper()}"
    h, w, _ = frame.shape

    (tw, th), _ = cv2.getTextSize(text, FONT, 0.7, 2)

    x, y = 10, h - 20

    cv2.rectangle(frame, (x - 5, y - th - 10), (x + tw + 5, y + 5), (0, 0, 0), -1)
    cv2.putText(frame, text, (x, y), FONT, 0.7, (255, 255, 255), 2)

    return frame


def show_color_preview(frame, landmarks, current_color, size=30):
    if "index_tip" not in landmarks:
        return frame

    x, y = landmarks["index_tip"]

    top_left = (x + 15, y - 15)
    bottom_right = (top_left[0] + size, top_left[1] + size)

    cv2.rectangle(frame, top_left, bottom_right, current_color, -1)
    cv2.rectangle(frame, top_left, bottom_right, (255, 255, 255), 2)

    return frame



def draw_fingertip_trail(frame, trail_points, color, max_points=20):
    recent_points = trail_points[-max_points:]

    for i, point in enumerate(recent_points):
        radius = int(8 * (i + 1) / len(recent_points))
        cv2.circle(frame, point, radius, color, -1)

    return frame




def show_status_message(frame, message, position="top"):
    h, w, _ = frame.shape
    (tw, th), _ = cv2.getTextSize(message, FONT, 0.8, 2)

    x = (w - tw) // 2
    y = 40 if position == "top" else h - 40

    cv2.rectangle(frame, (x - 10, y - th - 10), (x + tw + 10, y + 10), (0, 0, 0), -1)
    cv2.putText(frame, message, (x, y), FONT, 0.8, (255, 255, 255), 2)

    return frame
