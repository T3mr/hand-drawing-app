import cv2
import numpy as np
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

colors = {
    "blue": (255, 0, 0),
    "green": (0, 255, 0),
    "red": (0, 0, 255),
    "yellow": (0, 255, 255),
    "clear": (0, 0, 0)
}

current_color = "red"
drawing = False

cap = cv2.VideoCapture(0)

canvas = np.zeros((480, 640, 3), np.uint8)

with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                h, w, c = frame.shape
                cx, cy = int(index_finger_tip.x * w), int(index_finger_tip.y * h)

                if drawing:
                    cv2.circle(frame, (cx, cy), 5, colors[current_color], -1)
                    cv2.circle(canvas, (cx, cy), 5, colors[current_color], -1)

                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        
        frame[:50, :640] = 255 
        cv2.putText(frame, 'CLEAR', (10, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(frame, 'BLUE', (130, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(frame, 'GREEN', (250, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, 'RED', (380, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(frame, 'YELLOW', (490, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                h, w, c = frame.shape
                cx, cy = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
                
                if cy < 50:
                    if 0 < cx < 120:
                        canvas[:] = 0 
                    elif 120 < cx < 240:
                        current_color = "blue"
                    elif 240 < cx < 360:
                        current_color = "green"
                    elif 360 < cx < 480:
                        current_color = "red"
                    elif 480 < cx < 600:
                        current_color = "yellow"

        frame = cv2.add(frame, canvas)
        
        cv2.imshow('Paint', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # 'ESC' tuşuna basarak çıkış yapabilirsiniz
            break
        elif key == ord('d'):  # 'd' tuşuna basarak çizim modunu aç/kapa
            drawing = not drawing

cap.release()
cv2.destroyAllWindows()
