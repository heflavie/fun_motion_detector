import cv2
import logging
import os
import time

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CameraError(Exception):
    """Custom exception for camera errors."""
    pass

def initialize_camera(video_path=None):
    """
    Initialize the camera or video file for motion detection.

    Args:
        video_path (str): Path to a video file, or None to use the camera.
    
    Returns:
        cv2.VideoCapture: Video capture object.
    
    Raises:
        CameraError: If the camera or video file cannot be opened.
    """
    cap = cv2.VideoCapture(video_path if video_path else 0)

    if not cap.isOpened():
        logging.error("Failed to open the video source")
        raise CameraError("Camera or video file could not be opened")
    
    return cap

def capture_frame(cap):
    """
    Captures a frame from the video source.
    
    Args:
        cap (cv2.VideoCapture): Video capture object.

    Returns:
        tuple: (bool, ndarray) - ret: success flag, frame: captured frame.
    """
    ret, frame = cap.read()
    if not ret or frame is None:
        logging.error("Failed to capture frame")
        return False, None
    return ret, frame


def detect_motion_in_frame(previous_gray, current_frame):
    """
    Detect motion by comparing the previous and current frames.

    Args:
        previous_gray (ndarray): Grayscale version of the previous frame.
        current_frame (ndarray): Current frame from the video source.

    Returns:
        motion_detected (bool): Whether motion was detected.
        frame_diff_bgr (ndarray): Frame with motion highlighted.
    """
    current_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    frame_diff = cv2.absdiff(current_gray, previous_gray)
    
    _, threshold = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motion_detected = False
    frame_diff_bgr = cv2.cvtColor(frame_diff, cv2.COLOR_GRAY2BGR)
    
    for contour in contours:
        if cv2.contourArea(contour) > 500:
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame_diff_bgr, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame_diff_bgr, "Motion detected!", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            motion_detected = True

    return motion_detected, frame_diff_bgr

def display_frame(frame_diff_bgr):
    """
    Display the frame with motion detection highlights.
    
    Args:
        frame_diff_bgr (ndarray): Frame with motion highlights.
    """
    try:
        cv2.imshow("Frame Difference with Motion Detection", frame_diff_bgr)
    except cv2.error as e:
        logging.error(f"Error displaying frame: {e}")

def release_camera(cap):
    """
    Release the camera and close any open windows.
    
    Args:
        cap (cv2.VideoCapture): Video capture object.
    """
    cap.release()
    try:
        cv2.destroyAllWindows()
    except cv2.error as e:
        logging.error(f"Error closing windows: {e}")
    logging.info("Camera released and windows closed")

def detect_motion(video_path=None):
    """
    Main function for motion detection.
    
    Args:
        video_path (str): Optional path to a video file. If not provided, the camera will be used.
    """
    cap = initialize_camera(video_path)

    ret, previous_frame = capture_frame(cap)
    if not ret:
        raise CameraError("No valid frame captured")
    
    previous_gray = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)
    
    no_display = os.getenv("NO_DISPLAY", "0") == "1"
    logging.info(f"Display is disabled: {no_display}")

    logging.info("Motion detection system initialized. Starting motion detection loop.")

    start_time = time.time()

    while True:
        ret, current_frame = capture_frame(cap)
        if not ret:
            break

        motion_detected, frame_diff_bgr = detect_motion_in_frame(previous_gray, current_frame)

        if not motion_detected:
            logging.warning("No significant motion detected in this frame.")
        
        if not no_display:
            display_frame(frame_diff_bgr)

        if no_display and time.time() - start_time > 10:
            logging.info("Exiting after 10 seconds in CI environment without display")
            break

        if not no_display and cv2.waitKey(1) & 0xFF == ord('q'):
            logging.info("Exiting motion detection loop")
            break

        previous_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

    release_camera(cap)

if __name__ == "__main__":
    detect_motion()
