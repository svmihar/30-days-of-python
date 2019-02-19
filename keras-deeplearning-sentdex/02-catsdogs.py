import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import os 
# import cv2
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
DATADIR = "dataset/"

FAST_RUN = False
IMAGE_WIDTH = 128
IMAGE_HEIGHT = 128
IMG_SIZE = (IMAGE_WIDTH,IMAGE_HEIGHT)
IMAGE_CHANNELS = 3

IMG_SIZE = 30
new_Array = cv2.resize(img_Array,(IMG_SIZE,IMG_SIZE))
plt.imshow(new_Array,cmap='gray')
plt.show()

training_data = []
def create_training_data():
    for category in CATEGORIES: 
        path = os.path.join(DATADIR,category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
                training_data.append([new_array,class_num])
            except Exception as e: 
                pass
                print(e)
create_training_data()