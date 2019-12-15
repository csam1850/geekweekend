"""
this module serves for testing the classifier
"""
import numpy as np
import tensorflow as tf

# load model and tags
graph_def = tf.compat.v1.GraphDef()
labels = []

# These are set to the default names from exported models, update as needed.
filename = "model.pb"
labels_filename = "labels.txt"

# Import the TF graph
with tf.io.gfile.GFile(filename, 'rb') as f:
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')

# Create a list of labels.
with open(labels_filename, 'rt') as lf:
    for l in lf:
        labels.append(l.strip())

# predict image
# These names are part of the model and cannot be changed.
output_layer = 'loss:0'
input_node = 'Placeholder:0'

with tf.compat.v1.Session() as sess:
    try:
        prob_tensor = sess.graph.get_tensor_by_name(output_layer)
        predictions, = sess.run(prob_tensor, {input_node: [augmented_image]})
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
