import cv2
import numpy as np
import mediapipe as mp

# Load MediaPipe model
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path="hand_landmarker.task"),
    running_mode=VisionRunningMode.IMAGE,
    num_hands=1
)

detector = HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)

canvas = None
prev_x, prev_y = 0, 0

colors = [(255,0,0),(0,255,0),(0,0,255),(0,255,255)]
color_names = ["Blue","Green","Red","Yellow"]
current_color = colors[0]

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    if canvas is None:
        canvas = np.zeros_like(frame)

    # Draw buttons
    for i, color in enumerate(colors):
        cv2.rectangle(frame, (i*100,0), ((i+1)*100,80), color, -1)
        cv2.putText(frame, color_names[i], (i*100+10,50),
                    cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)

    cv2.rectangle(frame, (500,0), (640,80), (0,255,255), -1)
    cv2.putText(frame, "CLEAR", (510,50),
                cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),2)

    # Convert to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)

    result = detector.detect(mp_image)

    if result.hand_landmarks:
        hand = result.hand_landmarks[0]

        h, w, _ = frame.shape
        x = int(hand[8].x * w)   # index finger tip
        y = int(hand[8].y * h)

        cv2.circle(frame, (x,y), 10, (0,255,255), -1)

        # Check if ONLY index finger is up
        if hand[8].y < hand[6].y and hand[12].y > hand[10].y:
            
            if y < 80:
                index = x // 100

                if index < 4:
                    current_color = colors[index]
                    prev_x, prev_y = 0, 0

                elif 500 < x < 640:
                    canvas = np.zeros_like(frame)
                    prev_x, prev_y = 0, 0
            else:
                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = x, y

                cv2.line(canvas, (prev_x, prev_y), (x, y), current_color, 5)
                prev_x, prev_y = x, y
        else:
            prev_x, prev_y = 0, 0

    # Merge canvas
    gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, inv = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY_INV)
    inv = cv2.cvtColor(inv, cv2.COLOR_GRAY2BGR)

    frame = cv2.bitwise_and(frame, inv)
    frame = cv2.bitwise_or(frame, canvas)

    cv2.imshow("Air Canvas", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()