# pyrefly: ignore [missing-import]
import cv2
import logging
from pathlib import Path
from datetime import datetime

logger = logging.getLogger(__name__)


def capture_image() -> Path:
    """
    Captures a single image from the default webcam, saves it in the
    'captures' directory with a timestamped filename, and returns the path.

    Raises:
        RuntimeError: If the camera cannot be opened, a frame cannot be
        captured, or the image cannot be saved.
    """
    cam = cv2.VideoCapture(0)

    try:
        if not cam.isOpened():
            raise RuntimeError("Could not open the camera.")

        ret, frame = cam.read()

        if not ret:
            raise RuntimeError("Failed to capture image from camera.")

        captures_dir = Path("captures")
        captures_dir.mkdir(parents=True, exist_ok=True)

        filename = captures_dir / datetime.now().strftime("%Y%m%d_%H%M%S_%f.jpg")

        if not cv2.imwrite(str(filename), frame):
            raise RuntimeError("Failed to save captured image.")

        logger.info("Image saved: %s", filename)

        return filename

    finally:
        cam.release()