import numpy as np

FINGERTIP_INDICES = {"thumb": 4, "index": 8, "middle": 12, "ring": 16, "pinky": 20}
FINGER_PIP_INDICES = {"thumb": 3, "index": 6, "middle": 10, "ring": 14, "pinky": 18}


def detect_hand_landmarks(hand_landmarks, frame_shape):
    height, width, _ = frame_shape
    raw_landmarks = []

    for landmark in hand_landmarks:
        px = int(landmark.x * width)
        py = int(landmark.y * height)
        raw_landmarks.append((px, py))

    return {
        "raw": raw_landmarks,
        "index_tip": raw_landmarks[8]
    }


def is_finger_up(landmarks, finger_name):
    raw = landmarks["raw"]

    tip_idx = FINGERTIP_INDICES[finger_name]
    pip_idx = FINGER_PIP_INDICES[finger_name]

    tip = raw[tip_idx]
    pip = raw[pip_idx]

    if finger_name == "thumb":
        return abs(tip[0] - pip[0]) > 30

    return tip[1] < pip[1] - 10


def interpret_gesture(landmarks):
    if landmarks is None:
        return None

    fingers = []
    for finger in ["thumb", "index", "middle", "ring", "pinky"]:
        if is_finger_up(landmarks, finger):
            fingers.append(finger)

    if fingers == ["index"]:
        return "draw"

    return None
