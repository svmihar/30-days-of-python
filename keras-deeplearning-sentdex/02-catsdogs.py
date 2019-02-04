import numpy as np 
import matplotlib.pyplot as plt 
import os 
import cv2

CATEGORIES = ['Dog','Cat']
DATADIR='dataset/PetImages'
for category in CATEGORIES: 
    path = os.path.join(DATADIR, category) #path to cats or dogs 
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
        plt.imshow(img_array,cmap='gray')
        plt.show()
        break 
    break 