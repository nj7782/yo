# Facedetection_with_uniqueID Using Using Haar Cascades

This project demonstrates a simple method for detecting faces in video footage using **Haar Cascades**. The system assigns a **unique ID** to each detected face and tracks them across frames by calculating the **Intersection over Union (IoU)** between detected faces. The IDs are updated when faces move across the screen, and the system continues assigning new IDs to any new faces that appear in the frame.

## Features
- **Haar Cascades** for detecting faces and eyes.
- **IoU (Intersection over Union)** for re-identifying and tracking faces across video frames.
- Unique IDs assigned to each detected face, which are continuously updated based on their IoU with previous detections.

## Requirements
- OpenCV for video capture and object detection.
- NumPy for numerical operations.
  
## Setup

1. **Clone this repository** and navigate to the project directory.

2. **Install required dependencies** by running:
   ```bash
   pip install opencv-python-headless numpy
   ```

3. **Download Haar Cascade files**:
   - You will need to download the Haar Cascade files for face and eye detection:
     - [Haarcascade Frontalface Default](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
     - [Haarcascade Eye](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml)

   Once downloaded, place them in the correct paths:
   ```bash
   C:\nj\haarcascade_frontalface_default.xml
   C:\Users\jitin\Downloads\haarcascade_eye.xml
   ```

4. **Update the video path**:
   - Make sure to specify the correct path to the input video file in the script:
     ```bash
     C:\nj\ABA Therapy - Play.mp4
     ```

## Running the Code

1. **Run the Python script**:
   ```bash
   python inference.py
   ```

2. The script will display the video frames with **rectangles drawn around each detected face**, and a **unique ID** will be assigned to each face. These IDs will be updated for every frame and will persist as long as the face is detected.

3. **Press 'Q'** on the keyboard to stop the video playback and close the application.

## Output
The system displays each frame of the video with:
- **Bounding boxes** around detected faces.
- A **unique ID** above each face that persists through the frames as long as the face is visible.

## Known Limitations
- The system relies heavily on the accuracy of Haar Cascades for both face and eye detection, which may lead to occasional false positives or negatives.
- The IoU-based re-identification works well for tracking objects that move gradually, but may struggle in complex scenarios like occlusions or fast movements.
- IDs are reassigned based on visual similarity (IoU), but re-identification may not be perfect.

## Files Included
- `inference.py`: Main script for face detection and tracking using Haar Cascades and IoU.
- `iou_utils.py`: Utility function for calculating the IoU between bounding boxes.
- `requirements.txt`: List of dependencies.
