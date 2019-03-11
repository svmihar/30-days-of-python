from keras.optimizers import SGD, Adam, Adagrad, RMSprop
import keras.backend as K
from keras.models import Sequential
from keras.layers import Dense, Activation
import pandas as pd 

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import scale

import matplotlib.pyplot as plt 

def pisahkan(judul): 
    print('\n',60*'=')
    print(judul.upper())
    print(60*'=','\n')


dflist = []

df = pd.read_csv('datasets/banknotes.csv')
X = scale(df.drop('class', axis=1).values)
y = df['class'].values
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3,
                                                    random_state=42)
pisahkan('Optimizer')

optimizers = ['SGD(lr=0.01)',

'SGD(lr=0.01, momentum=0.03)',
'SGD(lr=0.01, momentum=0.03, nesterov=True)',
'Adam(lr=0.01)',
'Adagrad(lr=0.01)',
'RMSprop(lr=0.01)']
""" for opt in optimizers: 
    K.clear_session()
    model = Sequential()
    model.add(Dense(1, input_shape=(4,),activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer=eval(opt), metrics=['accuracy'])
    h = model.fit(X_train, y_train, batch_size=16, epochs=5, verbose=1)
    dflist.append(pd.DataFrame(h.history, index=h.epoch))

historydf = pd.concat(dflist, axis=1)
metrics_reported = dflist[0].columns

idx = pd.MultiIndex.from_product([optimizers,metrics_reported], names=['optimizers','metric'])
historydf.columns = idx

ax = plt.subplot(211)
historydf.xs('loss',axis=1, level='metric').plot(ylim=(0,1), ax=ax)
plt.title('Loss')

ax = plt.subplot(212)
historydf.xs('acc', axis=1, level='metric').plot(ylim=(0,1),ax=ax)
plt.title("Accuracy")
plt.xlabel("Epochs")

plt.tight_layout()
plt.show() """



pisahkan('Initializer')

dflist = []
initializers = ['zeros', 'uniform','normal','he_normal', 'lecun_uniform']
for init in initializers: 
    K.clear_session()
    model = Sequential()
    model.add(Dense(1,input_shape=(4,),kernel_initializer=init, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='rmsprop',metrics=['accuracy'])
    
    h = model.fit(X_train, y_train, batch_size=16, epochs=5, verbose=1)
    dflist.append(pd.DataFrame(h.history, index=h.epoch))

historydf = pd.concat(dflist, axis=1)
metrics_reported = dflist[0].columns

idx = pd.MultiIndex.from_product([initializers,metrics_reported], names=['optimizers','metric'])
historydf.columns = idx


ax = plt.subplot(211)
historydf.xs('loss',axis=1, level='metric').plot(ylim=(0,1), ax=ax)
plt.title('Loss')

ax = plt.subplot(212)
historydf.xs('acc', axis=1, level='metric').plot(ylim=(0,1),ax=ax)
plt.title("Accuracy")
plt.xlabel("Epochs")
plt.tight_layout()
plt.show()

pisahkan('Inner layer representation')

K.clear_session()
model = Sequential()
model.add(Dense(2, input_shape=(4,), activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer=RMSprop(lr=0.01),metrics=['accuracy'])

h = model.fit(X_train, y_train, batch_size=16, epochs=20, verbose=1, validation_split=0.3)
result = model.evaluate(X_test,y_test)
print(result)
print(model.summary())
print(model.layers)