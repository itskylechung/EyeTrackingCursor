import cv2
import mediapipe as mp
import pyautogui
from screeninfo import get_monitors

# Get all monitor info
monitors = get_monitors()
screen_regions = [(m.x, m.x + m.width) for m in monitors]

# Init video and face mesh
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

# Track which screen we're currently in
current_screen_index = None

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    frame_h, frame_w, _ = frame.shape

    if output.multi_face_landmarks:
        landmarks = output.multi_face_landmarks[0].landmark

        # Use nose tip (index 1) and eye center (average of landmark 145 & 159)
        nose_tip = landmarks[1]
        left_eye_top = landmarks[145]
        left_eye_bottom = landmarks[159]

        eye_y = (left_eye_top.y + left_eye_bottom.y) / 2
        nose_x = nose_tip.x * frame_w

        # Estimate horizontal face position (left/mid/right)
        face_center_x = nose_x

        # Determine which screen region we're currently facing
        screen_index = None
        for i, (x_start, x_end) in enumerate(screen_regions):
            region_center = (x_start + x_end) / 2
            if face_center_x < frame_w / len(screen_regions) * (i + 1):
                screen_index = i
                break

        # Switch cursor if screen changed
        if screen_index is not None and screen_index != current_screen_index:
            current_screen_index = screen_index
            target_screen = monitors[screen_index]
            center_x = target_screen.x + target_screen.width // 2
            center_y = target_screen.y + target_screen.height // 2
            pyautogui.moveTo(center_x, center_y)
            print(f"Switched to screen {screen_index}")

    cv2.imshow("Eye/Nose Controlled Screen Switch", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
        break

cam.release()
cv2.destroyAllWindows()
