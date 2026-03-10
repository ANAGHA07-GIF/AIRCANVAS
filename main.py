import cv2
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

from drawing_engine import draw_stroke, clear_canvas, initialize_canvas
from tool_palette import render_palette, check_palette_selection, create_color_buttons
from gesture_controller import detect_hand_landmarks, interpret_gesture
from visual_feedback import draw_cursor, display_mode_indicator, show_color_preview

WINDOW_NAME = "Air Canvas Studio"
CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 720
DEFAULT_COLOR = (255, 0, 0)
DEFAULT_THICKNESS = 5


class ApplicationState:
    def __init__(self):
        self.canvas = initialize_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
        self.current_color = DEFAULT_COLOR
        self.current_thickness = DEFAULT_THICKNESS
        self.previous_point = None


def initialize_mediapipe():
    base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
    options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=1)
    return vision.HandLandmarker.create_from_options(options)


def main():
    detector = initialize_mediapipe()
    cap = cv2.VideoCapture(0)

    state = ApplicationState()
    buttons = create_color_buttons()

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        import mediapipe as mp
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        result = detector.detect(mp_image)

        landmarks = None

        if result.hand_landmarks:
            hand = result.hand_landmarks[0]
            landmarks = detect_hand_landmarks(hand, frame.shape)
            gesture = interpret_gesture(landmarks)

            finger = landmarks["index_tip"]

            action = check_palette_selection(finger, buttons)
            if action and action[0] == "color":
                state.current_color = action[1]

            if gesture == "draw":
                state.canvas = draw_stroke(
                    state.canvas,
                    finger,
                    state.previous_point,
                    state.current_color,
                    state.current_thickness
                )
                state.previous_point = finger
            else:
                state.previous_point = None

        # ---- OUTPUT ----
        output = frame.copy()

        # Blend canvas FIRST
        canvas_resized = cv2.resize(state.canvas, (frame.shape[1], frame.shape[0]))
        output = cv2.addWeighted(frame, 1.0, canvas_resized, 0.6, 0)



        # Then UI on top
        output = render_palette(output, buttons, state.current_color, "draw")

        if landmarks:
            output = draw_cursor(output, landmarks, "draw")
            output = show_color_preview(output, landmarks, state.current_color)

        output = display_mode_indicator(output, "draw")

        cv2.imshow(WINDOW_NAME, output)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    detector.close()


if __name__ == "__main__":
    main()

