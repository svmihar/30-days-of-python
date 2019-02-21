# find edges, and lines, then pooling. 
# squares, circles, small features. 
import tensorflow as tf 
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle

#don't have the model 
X = pickle.load(open("X.pickle","rb")) 
y = pickle.load(open("y.pickle","rb"))

X = X/255
model = Sequential()
model.add(Conv2D(64,(3,3),input_shape = X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(64))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss="binary_crossentropy",optimizer='adam',metrics=['accuracy']) #change loss to categorical
model.fit(X,y,batch_size=32, validation_split=0.15, epochs=10) #calculate 32 batches at once, depends on the size of the data

