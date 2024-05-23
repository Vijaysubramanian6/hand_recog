import cv2
import mediapipe as mp
import numpy as np

# Initialize Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Access the webcam
cap = cv2.VideoCapture(0)

def distance(point1, point2):
    return np.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2 + (point1.z - point2.z)**2)

def is_hand_closed(landmarks, threshold=0.1):
    """
    Detects if the hand is closed based on the distance between fingertips and their corresponding MCPs.
    """
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]

    thumb_mcp = landmarks[2]
    index_mcp = landmarks[5]
    middle_mcp = landmarks[9]
    ring_mcp = landmarks[13]
    pinky_mcp = landmarks[17]

    # Compute distances from fingertips to their respective MCPs
    d_thumb = distance(thumb_tip, thumb_mcp)
    d_index = distance(index_tip, index_mcp)
    d_middle = distance(middle_tip, middle_mcp)
    d_ring = distance(ring_tip, ring_mcp)
    d_pinky = distance(pinky_tip, pinky_mcp)

    # Check if the average distance is below the threshold
    avg_distance = (d_thumb + d_index + d_middle + d_ring + d_pinky) / 5.0
    print(avg_distance)
    return avg_distance < threshold

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and detect hands
    results = hands.process(frame_rgb)

    # Draw hand landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            hand_closed = is_hand_closed(hand_landmarks.landmark)
            if hand_closed:
                cv2.putText(frame, "Closed", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                cv2.putText(frame, "Open", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the frame
    cv2.imshow('Hand Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
