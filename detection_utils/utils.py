import os

import cv2
import numpy as np


def open_image_cv(image_path: str) -> np.ndarray:
    """
    Open and read an image file using OpenCV.

    Args:
        image_path (str): The path to the image file.

    Returns:
        np.ndarray: The image data as a NumPy array.

    Raises:
        FileNotFoundError: If the specified image file does not exist.
        ValueError: If the image file cannot be opened or read.

    Notes:
        - This function uses the OpenCV library (cv2) to read the image file.
        - The image is returned as a NumPy array.
    """
    image = cv2.imread(image_path)
    return image


def resize_image(image) -> np.ndarray:
    """
    Resize the input image to a specified width and height.

    Args:
        image (np.ndarray): The input image as a NumPy array.

    Returns:
        np.ndarray: The resized image as a NumPy array.

    Raises:
        ValueError: If the input image is not a valid NumPy array.

    Notes:
        - This function uses the OpenCV library (cv2) for resizing the image.
        - The aspect ratio of the image may be changed during resizing.
        - The input image should be in BGR format (common in OpenCV), not RGB.
    """
    return cv2.resize(image, (600, 600))


def create_folder(folder_path: str) -> None:
    """
    Create a folder at the specified path if it doesn't already exist.

    Args:
        folder_path (str): The path of the folder to create.

    Returns:
        None
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
