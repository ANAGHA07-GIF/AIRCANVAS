import cv2
import numpy as np
import math


def initialize_canvas(width, height, background_color=(0, 0, 0)):
    return np.full((height, width, 3), background_color, dtype=np.uint8)


def clear_canvas(canvas, background_color=(0, 0, 0)):
    canvas[:] = background_color
    return canvas


def draw_stroke(canvas, current_point, previous_point, color, thickness):
    x, y = map(int, current_point)

    if previous_point is None:
        cv2.circle(canvas, (x, y), thickness // 2, color, -1, cv2.LINE_AA)
    else:
        px, py = map(int, previous_point)
        cv2.line(canvas, (px, py), (x, y), color, thickness, cv2.LINE_AA)

    return canvas


