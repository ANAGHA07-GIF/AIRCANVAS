# Air Canvas Studio 🎨✋

A **gesture-controlled drawing application** that lets you draw in the air using your hand movements. Built with **Python**, **OpenCV**, and **MediaPipe Hands**.

---

README.md
3 KB
opencv-python
mediapipe
numpy
requirements.txt
1 KB
﻿
Ima
ima_bleh
 
 
 
I was supposed to be you Barry
# Air Canvas Studio 🎨✋

A **gesture-controlled drawing application** that lets you draw in the air using your hand movements. Built with **Python**, **OpenCV**, and **MediaPipe Hands**.

---

## 📁 Project Structure

```
├── main.py               # Application entry point
├── drawing_engine.py     # Drawing operations (strokes, shapes, erasing)
├── tool_palette.py       # Tool & color selection UI
├── gesture_controller.py # Hand landmark detection & gesture logic
├── visual_feedback.py    # Cursor, indicators, visual hints
├── requirements.txt      # Python dependencies
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Create & activate virtual environment

**Windows**

```bash
python -m venv venv
.\venv\Scripts\Activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python main.py
```

---

## ⌨️ Keyboard Controls

| Key | Action           |
| --- | ---------------- |
| `q` | Quit application |
| `c` | Clear canvas     |

---

## ✋ Gestures (To Be Implemented)

| Gesture         | Action         |
| --------------- | -------------- |
| Index finger up | Draw mode      |
| Two fingers up  | Select mode    |
| Fist            | Stop drawing   |
| Open palm       | Special action |

---

## 🛠️ Implementation Tasks

### `drawing_engine.py`

* `draw_stroke()` – Continuous freehand drawing
* `draw_shape()` – Draw basic shapes (line, rectangle, circle)
* `erase_stroke()` – Erase drawn content
* `blend_canvas_with_frame()` – Overlay canvas on video frame

### `gesture_controller.py`

* `detect_hand_landmarks()` – Extract hand landmarks using MediaPipe
* `is_finger_up()` – Detect finger state (up/down)
* `interpret_gesture()` – Classify gestures from landmarks

### `tool_palette.py`

* `PaletteButton.contains_point()` – Button hit detection
* `render_palette()` – Render tool & color palette UI
* `check_palette_selection()` – Handle tool/color selection

### `visual_feedback.py`

* `draw_cursor()` – Draw fingertip cursor
* `display_mode_indicator()` – Show current mode (draw/select/erase)
* `show_color_preview()` – Display selected color preview

---

## 🚀 Future Enhancements

* Save drawings as images
* Gesture-based undo/redo
* Multi-hand support
* Shape snapping & smoothing

---

## 🧠 Tech Stack

* Python
* OpenCV
* MediaPipe Hands
* NumPy

---

Happy hacking! ✨

README.md
3 KB    
