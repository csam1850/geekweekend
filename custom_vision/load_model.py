import os
import tensorflow as tf


def load_model_and_tags(dir_path):

    # load model and tags
    graph_def = tf.compat.v1.GraphDef()
    labels = []

    # These are set to the default names from exported models, update as needed
    filename = "model.pb"
    filepath = os.path.join(dir_path, filename)
    labels_filename = "labels.txt"
    labels_filepath = os.path.join(dir_path, labels_filename)

    # Import the TF graph
    with tf.io.gfile.GFile(filepath, 'rb') as f:
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')

    # Create a list of labels.
    with open(labels_filepath, 'rt') as lf:
        for l in lf:
            labels.append(l.strip())

    return labels
