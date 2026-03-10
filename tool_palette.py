"""
Air Canvas Studio - Tool Palette
Handles tool and color selection UI.
"""

import cv2

# Color options (BGR format)
COLOR_OPTIONS = [
    ("Red", (0, 0, 255)),
    ("Green", (0, 255, 0)),
    ("Blue", (255, 0, 0)),
    ("Yellow", (0, 255, 255)),
    ("Cyan", (255, 255, 0)),
    ("Magenta", (255, 0, 255)),
    ("White", (255, 255, 255)),
    ("Black", (0, 0, 0)),
]

BUTTON_WIDTH = 60
BUTTON_SPACING = 10


class PaletteButton:
    def __init__(self, x, y, color, size=60, action=None):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.action = action

    def contains_point(self, point):
        px, py = point
        return (
            self.x <= px <= self.x + self.size and
            self.y <= py <= self.y + self.size
        )


def create_color_buttons():
    buttons = []
    start_x = 20
    y = 20

    for i, (_, color) in enumerate(COLOR_OPTIONS):
        x = start_x + i * (BUTTON_WIDTH + BUTTON_SPACING)
        button = PaletteButton(
            x=x,
            y=y,
            color=color,
            size=BUTTON_WIDTH,
            action=("color", color)
        )
        buttons.append(button)

    return buttons


def render_palette(frame, buttons, current_color, current_mode):
    for button in buttons:
        x, y = button.x, button.y
        size = button.size
        color = button.color

        cv2.rectangle(frame, (x, y), (x + size, y + size), color, -1)

        if color == current_color:
            cv2.rectangle(frame, (x, y), (x + size, y + size), (255, 255, 255), 3)

    return frame


def check_palette_selection(finger_position, buttons):
    for button in buttons:
        if button.contains_point(finger_position):
            return button.action
    return None

