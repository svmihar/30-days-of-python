import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import os 
import cv2
from keras.preprocessing.image import ImageDataGenerator, load_img
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import random

# CATEGORIES = ['Dog','Cat']
# DATADIR='dataset/PetImages'
# for category in CATEGORIES: 
#     path = os.path.join(DATADIR, category) #path to cats or dogs 
#     for img in os.listdir(path):
#         img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
#         plt.imshow(img_array,cmap='gray')
#         plt.show()
#         break 
#     break 

import os 
print(os.listdir("dataset/"))
CATEGORIES = ['Dog','Cat']
DATADIR = "dataset/PetImages/"

FAST_RUN = False
IMAGE_WIDTH = 128
IMAGE_HEIGHT = 128
IMAGE_SIZE = (IMAGE_WIDTH,IMAGE_HEIGHT)
IMAGE_CHANNELS = 3

for category in CATEGORIES:
    path = os.path.join(DATADIR,category)
    for img in os.listdir(path):
        img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
        plt.imshow(img_array, cmap='gray')
        plt.show()
        break
    break
IMG_SIZE = 65
new_array = cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
plt.imshow(new_array, cmap='gray')
plt.show()

training_data= []