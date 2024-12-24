import unittest
from unittest.mock import MagicMock, patch
import logging
from motion_detector import initialize_camera, capture_frame, CameraError

# Mocking logging to prevent actual logging output during tests
logging.getLogger().setLevel(logging.CRITICAL)


class TestMotionDetection(unittest.TestCase):
    @patch('cv2.VideoCapture')
    def test_initialize_camera(self, mock_video_capture):
        # Créer un mock pour VideoCapture
        mock_cap = MagicMock()
        mock_video_capture.return_value = mock_cap

        # Simuler l'échec de l'ouverture de la caméra
        mock_cap.isOpened.return_value = False

        # Appel de la fonction qui doit lever une
        # exception si la caméra ne s'ouvre pas
        with self.assertRaises(CameraError):
            initialize_camera()

    def test_capture_frame_success(self):
        # Simulate a successful frame capture
        cap_mock = MagicMock()
        frame_mock = MagicMock()
        # Successful frame capture
        cap_mock.read.return_value = (True, frame_mock)

        ret, frame = capture_frame(cap_mock)
        self.assertTrue(ret)
        self.assertIsNotNone(frame)

    def test_capture_frame_failure(self):
        # Simulate a failed frame capture
        cap_mock = MagicMock()
        cap_mock.read.return_value = (False, None)  # Failed frame capture

        ret, frame = capture_frame(cap_mock)
        self.assertFalse(ret)
        self.assertIsNone(frame)


if __name__ == "__main__":
    unittest.main()
