import numpy as np
import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)

# Capture the first frame
ret, previous_frame = cap.read()

while True:
    # Capture the current frame
    ret, current_frame = cap.read()
    if not ret:
        break

    # Convert frames to grayscale for processing
    previous_gray = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)
    current_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

    # Calculate the absolute difference between the current and previous frames
    frame_diff = cv2.absdiff(current_gray, previous_gray)

    # Apply threshold to highlight the areas with significant movement
    _, threshold = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)

    # Convert frame_diff to BGR to draw colored rectangles
    frame_diff_bgr = cv2.cvtColor(frame_diff, cv2.COLOR_GRAY2BGR)

    # Find contours in the threshold image
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw a bounding box around significant contours on the difference frame
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Only consider large enough areas
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame_diff_bgr, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Red rectangle
            cv2.putText(frame_diff_bgr, "ICI !!!", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # Show the frame difference with rectangles
    cv2.imshow('Frame Difference with Motion Detection', frame_diff_bgr)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Update the previous frame for the next iteration
    previous_frame = current_frame

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()
