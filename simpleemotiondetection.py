import cv2
import numpy as np

# Load the Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open webcam
cap = cv2.VideoCapture(0)

print("Simple Emotion Detection - Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Convert to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        # Draw rectangle around face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Extract face region
        face_roi = gray[y:y+h, x:x+w]

        # Simple emotion detection based on face size
        # (This is a very basic approximation – real systems use ML/DL models)
        face_area = w * h
        if face_area > 10000:   # Large face area
            emotion_text = "Happy Face Detected! 😀"
            color = (0, 255, 0)  # Green
        elif face_area > 5000:  # Medium face area
            emotion_text = "Neutral Face Detected 🙂"
            color = (255, 255, 0)  # Yellow
        else:                   # Small face area
            emotion_text = "Face Detected 👤"
            color = (255, 0, 255)  # Magenta

        # Put text on the video frame
        cv2.putText(frame, emotion_text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, color, 2, cv2.LINE_AA)

    # If no faces detected
    if len(faces) == 0:
        cv2.putText(frame, "No Face Detected", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Show the webcam feed
    cv2.imshow("Simple Emotion Detection", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
print("Camera released. Goodbye!")
