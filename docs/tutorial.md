# Motion Detection Tutorial

## Introduction

This tutorial will guide you through the process of using the motion detection system implemented in this project. The system detects motion in real-time from a camera feed and highlights moving objects with red bounding boxes.

## How It Works

The system works by continuously comparing consecutive frames from the video feed. The difference between frames is calculated, and areas with significant motion are highlighted with bounding boxes. The bounding boxes are drawn around objects that are moving, and a message is displayed on the video feed when motion is detected.

### Core Components

1. **Grayscale Conversion**: The frames are converted to grayscale to simplify the comparison.
2. **Frame Difference**: The absolute difference between the current and previous frames is computed.
3. **Thresholding**: A threshold is applied to highlight areas with significant motion.
4. **Contour Detection**: Contours are detected on the thresholded image, and bounding boxes are drawn around moving objects.

## Running the Motion Detection

To run the motion detection system, follow these steps:

1. **Start the Motion Detection**:
   - Once all dependencies are installed (refer to the `README.md` for installation), run the following command:

     ```bash
     poetry run python motion_detector.py
     ```

   - This will open a window displaying the camera feed, with motion detection running in real time.

2. **Interacting with the Program**:
   - The system will highlight detected motion with red bounding boxes.
   - The message "Motion detected!" will appear near the bounding boxes to indicate detected movement.
   - If no significant motion is detected, a warning message will appear in the log.
   - To exit the program, press the `q` key.

## Adjusting Sensitivity

The sensitivity of the motion detection can be adjusted by changing the threshold value in the code:

```python
_, threshold = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)
