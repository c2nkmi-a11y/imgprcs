import cv2
import numpy as np

def read_image(file_path: str) -> np.ndarray:
    """Read an image from a file path."""
    img = cv2.imread(file_path)
    if img is None:
        raise ValueError(f"Could not read image from {file_path}")
    return img