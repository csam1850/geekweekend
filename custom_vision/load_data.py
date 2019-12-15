"""
This module serves for importing the data in the BGR color space
"""

import custom_vision.custom_vision_utilities as cvu
from PIL import Image
import tensorflow as tf

# Load from a file
path = "C:\\Users\\tim.lechner\\source\\productionizing_ML_models\\application3\\tests\\Orange.jpg"  # noqa: E501


def load_image(path):
    """
    this function load an image and converts it into the necessary format
    for further processing

    Args:
        path (str):
            a string specifying the path to an image
    Returns:
        augmented_image (np.array):
            an 3-dimensional array for further processing with each pixel in
            three color space (bgr)
    """
    image = Image.open(path)

    # Update orientation based on EXIF tags, if the file has orientation info.
    image = cvu.update_orientation(image)

    # Convert to OpenCV format
    image = cvu.convert_to_opencv(image)

    # If the image has either w or h greater than 1600 we resize it down
    # respecting aspect ratio such that the largest dimension is 1600
    image = cvu.resize_down_to_1600_max_dim(image)

    # We next get the largest center square
    h, w = image.shape[:2]
    min_dim = min(w, h)
    max_square_image = cvu.crop_center(image, min_dim, min_dim)

    # Resize that square down to 256x256
    augmented_image = cvu.resize_to_256_square(max_square_image)

    # Get the input size of the model
    with tf.compat.v1.Session() as sess:
        input_tensor_shape = \
            sess.graph.get_tensor_by_name('Placeholder:0').shape.as_list()
    network_input_size = input_tensor_shape[1]

    # Crop the center for the specified network_input_Size
    augmented_image = cvu.crop_center(augmented_image, network_input_size,
                                      network_input_size)

    return augmented_image
