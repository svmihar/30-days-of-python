import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
<<<<<<< HEAD
import os 
# import cv2
=======
import os, cv2, random
from tqdm import tqdm 
>>>>>>> 19b909c9ab96aa753e5850143afc2e6faab87390
from keras.preprocessing.image import ImageDataGenerator, load_img
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
<<<<<<< HEAD
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
=======

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
CATEGORIES = ['Dog','Cat']
DATADIR = r"C:\\Users\\PEMODELAN-01\\Downloads\\tian\\30-days-of-python\\keras-deeplearning-sentdex\\dataset\\PetImages\\"
>>>>>>> 19b909c9ab96aa753e5850143afc2e6faab87390

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
MODEL_NAME = 'dogs-cats-{}-{}.model'.format('LR','2conv')

def label_img(img):
    word_label = img.split('.')[-3]
    if word_label == 'cat': return [1,0]
    elif word_label == 'dog' : return [0,1]

training_data = []

IMG_SIZE=70
def create_traindata(): 
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        for img in tqdm(os.listdir(path)):
            try:
                img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                # new_array = cv2.resize(img_array, (IMAGE_SIZE, IMAGE_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e: 
                pass 
                print(e)
create_traindata()

print(len(training_data))

random.shuffle(training_data)

for sample in training_data:
    print(sample[1])
X = [] 
y = []

for features, label in training_data:
    X.append(features)
    print("features: ", features)
    y.append(label)
    print("labels: ",label)

print(X[0].reshape(-1, IMG_SIZE, IMG_SIZE,1))
X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

import pickle 
pickle_out = open('X.pickle','wb')
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open('y.pickle','wb')
pickle.dump(y, pickle_out)
pickle_out.close()


