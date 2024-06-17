import cv2
import numpy as np

def get_color_limit(color):
    """
    Given a BGR color, return the lower and upper HSV limits for masking.
    
    Args:
    - color (list): BGR color list.

    Returns:
    - tuple: lower and upper HSV limits.
    """
    C = np.uint8([[color]])
    hsv_color = cv2.cvtColor(C, cv2.COLOR_BGR2HSV)

    h = hsv_color[0][0][0]
    lower_limit = np.array([h-10, 100, 100], dtype=np.uint8)
    upper_limit = np.array([h+10, 255, 255], dtype=np.uint8)

    return lower_limit, upper_limit
