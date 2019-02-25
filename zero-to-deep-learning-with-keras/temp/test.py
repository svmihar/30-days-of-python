import pandas as pd 

from keras.models import Sequential
import keras.backend as K 
from keras.layers import Dense, Activation 
from keras.optimizers import SGD
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt 
import numpy

df = pd.read_csv('../datasets/banknotes.csv')
X = scale(df.drop('class',axis=1).values)
y = df['class'].values

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)



model = Sequential()
model.add(Dense(1,input_shape=(4,),activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='sgd',metrics=['accuracy'])
history = model.fit(X,y, validation_split=0.3, epochs=20,batch_size=10)
result = model.evaluate(X_test,y_test)
print(history.history.keys())
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('accuracy')
plt.xlabel('epoch')
plt.legend(['train','test'],loc='best')
plt.show()
# historydf = pd.DataFrame(history.history, index=history.epoch)
# historydf.plot(kind='line')
# plt.show()

# dataset = numpy.loadtxt("test_data.csv", delimiter=",")
# # split into input (X) and output (Y) variables
# X = dataset[:,0:8]
# Y = dataset[:,8]
# # create model
# model = Sequential()
# model.add(Dense(12, input_dim=8, kernel_initializer='uniform', activation='relu'))
# model.add(Dense(8, kernel_initializer='uniform', activation='relu'))
# model.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))
# # Compile model
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# # Fit the model
# history = model.fit(X, Y, validation_split=0.33, epochs=150, batch_size=10)
# # list all data in history
# print(history.history.keys())
# # summarize history for accuracy
# plt.plot(history.history['acc'])
# plt.plot(history.history['val_acc'])
# plt.title('model accuracy')
# plt.ylabel('accuracy')
# plt.xlabel('epoch')
# plt.legend(['train', 'test'], loc='upper left')
# plt.show()
# # summarize history for loss
# plt.plot(history.history['loss'])
# plt.plot(history.history['val_loss'])
# plt.title('model loss')
# plt.ylabel('loss')
# plt.xlabel('epoch')
# plt.legend(['train', 'test'], loc='upper left')
# plt.show()