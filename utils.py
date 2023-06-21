import cv2
import numpy as np


def open_image_cv(image_path: str) -> np.ndarray:
    image = cv2.imread(image_path)
    # return resize_image(image)
    return image

def resize_image(image) -> np.ndarray:
    size = max(image.shape[:2])
    return cv2.resize(image, (600, 600))
    # return cv2.resize(image, (size, size), interpolation=cv2.INTER_LINEAR)

open_image_cv('test_static/test_happy_woman.png')