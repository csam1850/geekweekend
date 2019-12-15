"""
This module serves for importing the data in the BGR color space
"""

import custom_vision.custom_vision_utilities as cvu
from PIL import Image


# Load from a file
path = "C:\\Users\\tim.lechner\\source\\productionizing_ML_models\\application3\\tests\\Orange.jpg"  # noqa: E501


def load_image(path):
    """
    this function load an image and converts it into the necessary format
    for further processing

    Args:
        path (str): a string specifying the path to an image
    Returns:
        image (np.array): an 3-dimensional array for further processing with
                          each pixel in three color space (bgr)
    """
    image = Image.open(path)

    # Update orientation based on EXIF tags, if the file has orientation info.
    image = cvu.update_orientation(image)

    # Convert to OpenCV format
    image = cvu.convert_to_opencv(image)

    # If the image has either w or h greater than 1600 we resize it down
    # respecting aspect ratio such that the largest dimension is 1600
    image = cvu.resize_down_to_1600_max_dim(image)

    return image
