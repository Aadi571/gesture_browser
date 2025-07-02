import cv2
import mediapipe as mp
import pyautogui
import time

# ============================
# Setup
# ============================

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

last_action_time = 0

# ============================
# Main Loop
# ============================

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmark_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmark_list.append((id, cx, cy))

            if landmark_list:
                # Finger states
                index_finger_up = landmark_list[8][2] < landmark_list[6][2]
                middle_finger_up = landmark_list[12][2] < landmark_list[10][2]
                ring_finger_up = landmark_list[16][2] < landmark_list[14][2]
                pinky_up = landmark_list[20][2] < landmark_list[18][2]
                thumb_up = landmark_list[4][1] < landmark_list[3][1]

                current_time = time.time()

                # ============== GESTURES ==============

                # 1️⃣ Switch tab
                if index_finger_up and middle_finger_up and not ring_finger_up:
                    cv2.putText(frame, "Switch Tab", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    if current_time - last_action_time > 1:
                        pyautogui.hotkey('ctrl', 'tab')
                        last_action_time = current_time

                # 2️⃣ New tab
                elif index_finger_up and not middle_finger_up:
                    cv2.putText(frame, "New Tab", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    if current_time - last_action_time > 1:
                        pyautogui.hotkey('ctrl', 't')
                        last_action_time = current_time

                # 3️⃣ Close tab
                elif index_finger_up and middle_finger_up and ring_finger_up:
                    cv2.putText(frame, "Close Tab", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                    if current_time - last_action_time > 1:
                        pyautogui.hotkey('ctrl', 'w')
                        last_action_time = current_time

                # 4️⃣ Zoom in
                elif thumb_up and not index_finger_up and not middle_finger_up:
                    cv2.putText(frame, "Zoom In", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                    if current_time - last_action_time > 1:
                        pyautogui.hotkey('ctrl', '+')
                        last_action_time = current_time

                # 5️⃣ Play/Pause video (fist)
                elif not index_finger_up and not middle_finger_up and not ring_finger_up and not pinky_up and not thumb_up:
                    cv2.putText(frame, "Play/Pause", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
                    if current_time - last_action_time > 1:
                        pyautogui.press('space')
                        last_action_time = current_time

                # 6️⃣ Screenshot (all fingers up)
                elif index_finger_up and middle_finger_up and ring_finger_up and pinky_up:
                    cv2.putText(frame, "Screenshot!", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
                    if current_time - last_action_time > 2:
                        filename = f"screenshot_{int(time.time())}.png"
                        pyautogui.screenshot().save(filename)
                        print(f"Screenshot saved: {filename}")
                        last_action_time = current_time

                # 7️⃣ Fullscreen toggle (3 fingers up + thumb)
                elif index_finger_up and middle_finger_up and ring_finger_up and thumb_up and not pinky_up:
                    cv2.putText(frame, "Toggle Fullscreen", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 165, 255), 2)
                    if current_time - last_action_time > 2:
                        pyautogui.press('f11')
                        last_action_time = current_time

    cv2.imshow("Gesture Browser Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

