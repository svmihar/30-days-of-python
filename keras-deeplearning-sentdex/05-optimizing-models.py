dense_layers = [0,1,2]
layers_sizes = [32,64,128]
conv_layers = [1,2,3]

import tensorflow as tf 
# import tensorflow.keras.datasets import cifar10
# from tensorflow.keras.preprocessing import ImageDataGenerator
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
import pickle, time

for dense_layer in dense_layers:
    for layer_size in layers_sizes:
        for conv_layer in conv_layers:
            NAME = "{conv_layer}-conv-{layer_size}-nodes-{dense_layer}-{int(time.time()}"
            print(NAME)

            model = Sequential()

            
