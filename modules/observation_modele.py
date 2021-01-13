import tensorflow as tf

from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt

def plot_layer(model: Model, test_image: str, layer_index_list: list, cmap='plasma'):

    layer_outputs = [layer.output for layer in model.layers]

    # Le chargement de l'image doit être augmenté puisque notre model prend des lots d'images.
    img = image.load_img(test_image, target_size=(32,32, 1))
    img_arr = image.img_to_array(img)
    img_arr = np.expand_dims(img_arr, axis=0)

    activation_model = Model(inputs=model.input, outputs=layer_outputs)
    activations = activation_model.predict(img_arr)
    
    for layer_index in layer_index_list:
        title = model.layers[layer_index].name
        __display_activation(activations[layer_index], title, 8, 4, cmap=cmap)

def __display_activation(activation, title, col_size, row_size, cmap): 
    
    activation_index=0
    fig, ax = plt.subplots(row_size, col_size, figsize=(row_size*13.5,col_size*2.5))
    fig.suptitle(title, fontsize=150)
    for row in range(0,row_size):
        for col in range(0,col_size):
            ax[row][col].imshow(activation[0, :, :, activation_index], cmap=cmap)
            activation_index += 1