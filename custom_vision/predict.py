import numpy as np
import tensorflow as tf


def predict_image(image, labels):
    # These names are part of the model and cannot be changed.
    output_layer = 'loss:0'
    input_node = 'Placeholder:0'

    with tf.compat.v1.Session() as sess:
        try:
            prob_tensor = sess.graph.get_tensor_by_name(output_layer)
            predictions, = sess.run(prob_tensor, {input_node: [image]})
        except KeyError:
            print("Couldn't find classification output layer: " + output_layer)
            print("Verify this a model exported from an Object Detection project.")
            exit(-1)

    # Print the highest probability label
    highest_probability_index = np.argmax(predictions)
    print('Classified as: ' + labels[highest_probability_index])
    print()

    # Or you can print out all of the results mapping labels to probabilities.
    label_index = 0
    for p in predictions:
        truncated_probablity = np.float64(np.round(p, 8))
        print(labels[label_index], truncated_probablity)
        label_index += 1
    
    return labels[highest_probability_index]
