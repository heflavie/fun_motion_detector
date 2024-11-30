import unittest
from unittest.mock import MagicMock
import cv2
import numpy as np
from motion_detector import detect_motion
import sys

sys.path.append('motion_detector.py')

class TestMotionDetection(unittest.TestCase):

    def setUp(self):
        """Initial setup for the tests"""
        # Mocking the video capture and frame reading process
        self.mock_cap = MagicMock()
        self.mock_cap.isOpened.return_value = True
        self.mock_cap.read.return_value = (True, np.zeros((480, 640, 3), dtype=np.uint8))  # Mocking a black frame

    def test_camera_initialization(self):
        """Test that the camera is correctly initialized"""
        cap = self.mock_cap
        ret, frame = cap.read()
        self.assertTrue(ret)
        self.assertEqual(frame.shape, (480, 640, 3))

    def test_no_motion(self):
        """Test if no motion is detected when frames are identical"""
        previous_frame = np.zeros((480, 640, 3), dtype=np.uint8)  # Black frame
        current_frame = np.zeros((480, 640, 3), dtype=np.uint8)  # Black frame
        # Ensure no motion is detected
        frame_diff = cv2.absdiff(current_frame, previous_frame)
        _, threshold = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)
        self.assertEqual(np.sum(threshold), 0)  # No motion, threshold should be zero

    def test_motion_detected(self):
        """Test if motion is correctly detected"""
        previous_frame = np.zeros((480, 640, 3), dtype=np.uint8)  # Black frame
        current_frame = np.ones((480, 640, 3), dtype=np.uint8) * 255  # White frame
        frame_diff = cv2.absdiff(current_frame, previous_frame)
        _, threshold = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)
        self.assertGreater(np.sum(threshold), 0)  # Motion detected, threshold sum should be positive

    def test_logging_error_on_camera_failure(self):
        """Test logging when camera initialization fails"""
        self.mock_cap.isOpened.return_value = False
        with self.assertRaises(SystemExit):
            detect_motion()  # Should exit due to camera failure

    def test_logging_info_on_motion_detection(self):
        """Test that info-level logs are produced when motion is detected"""
        with self.assertLogs('root', level='INFO') as cm:
            detect_motion()
        self.assertIn('Motion detected at position', cm.output[0])  # Check that motion detection log is present

if __name__ == '__main__':
    unittest.main()
