"""
this module serves for testing the classifier
"""
import os
from custom_vision.load_data import load_image
from custom_vision.load_model import load_model_and_tags
from custom_vision.predict import predict_image


def test_classifier():
    # load model and tags
    dir_path = os.path.dirname(os.path.realpath(__file__))
    labels = load_model_and_tags(dir_path)

    # Load image
    imageFile = "C:\\Users\\tim.lechner\\source\\productionizing_ML_models\\application3\\tests\\Orange.jpg"  # noqa: E501
    augmented_image = load_image(imageFile)

    # predict image
    prediction = predict_image(augmented_image, labels)
    assert prediction == "Orange"
