import cv2
import numpy as np

def to_grayscale(img: np.ndarray):
    """Convert the image to grayscale."""
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def blur_image(img: np.ndarray, k=5):
    """Apply a Gaussian blur to the image."""
    return cv2.GaussianBlur(img, (k,k), 0)

def edge_detection(img: np.ndarray):
    """Perform edge detection using Canny."""
    return cv2.Canny(img, 50, 150)

def adjust_brightness_contrast(img, brightness=0, contrast=0):
    """Adjust the brightness and contrast of the image."""
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow) / 255
        gamma_b = shadow
        img = cv2.addWeighted(img, alpha_b, img, 0, gamma_b)

    if contrast != 0:
        f = 131 * (contrast + 127) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127 * (1 - f)
        img = cv2.addWeighted(img, alpha_c, img, 0, gamma_c)

    return img

def adjust_saturation(img, scale=1.0):
    """Adjust the saturation of the image."""
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    s = cv2.multiply(s, scale)
    s = cv2.min(s, 255)
    hsv = cv2.merge((h, s, v))
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

def resize_image(img, width=None, height=None):
    """Resize the image while maintaining aspect ratio."""
    if width is None and height is None:
        return img
    h, w = img.shape[:2]
    if width is not None:
        r = width / float(w)
        dim = (width, int(h * r))
    else:
        r = height / float(h)
        dim = (int(w * r), height)
    return cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
