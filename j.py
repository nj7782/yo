import cv2
import numpy as np
from iou_utils import calculate_iou

# Specify the correct paths to the Haar Cascade files
face_cascade_path = 'C:\\nj\\haarcascade_frontalface_default.xml'
eye_cascade_path = 'C:\\Users\\jitin\\Downloads\\haarcascade_eye.xml'
video_path = 'C:\\nj\\ABA Therapy - Play.mp4'

# Create a VideoCapture object and read from the input file
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Load the Haar Cascades
face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

if face_cascade.empty() or eye_cascade.empty():
    print("Error: Could not load Haar Cascade file(s).")
    exit()

# Create a dictionary to store face IDs and their corresponding rectangles
face_ids = {}
next_id = 1

# Read until the video is completed
while True:
    # Capture frame by frame
    ret, frame = cap.read()
    if not ret:
        print("End of video file or no frames captured.")
        break

    # Convert the video into gray video without color
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the video
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Create a list to store current detected faces with IDs
    current_faces = []

    for (x, y, w, h) in faces:
        face_roi = gray[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(face_roi)
        if len(eyes) >= 2:  # At least two eyes detected
            current_faces.append((x, y, w, h))

    # Track faces and update IDs
    updated_face_ids = {}
    for (x, y, w, h) in current_faces:
        found = False
        for face_id, (x1, y1, w1, h1) in face_ids.items():
            iou = calculate_iou(x, y, w, h, x1, y1, w1, h1)
            if iou > 0.5:
                found = True
                updated_face_ids[face_id] = (x, y, w, h)
                break

        if not found:
            updated_face_ids[next_id] = (x, y, w, h)
            next_id += 1

    # Update face_ids with current frame's detected faces
    face_ids = updated_face_ids

    # Draw rectangles around the faces with unique IDs
    for face_id, (x, y, w, h) in face_ids.items():
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.putText(frame, str(face_id), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Press Q on the keyboard to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# When everything is done, release the video capture object and close all frames
cap.release()
cv2.destroyAllWindows()

def calculate_iou(x1, y1, w1, h1, x2, y2, w2, h2):
    # Calculate the coordinates of the intersection rectangle
    x_overlap = max(0, min(x1 + w1, x2 + w2) - max(x1, x2))
    y_overlap = max(0, min(y1 + h1, y2 + h2) - max(y1, y2))
    intersection_area = x_overlap * y_overlap

    # Calculate the union area
    union_area = w1 * h1 + w2 * h2 - intersection_area

    # Calculate the IoU
    iou = intersection_area / union_area
    return iou
