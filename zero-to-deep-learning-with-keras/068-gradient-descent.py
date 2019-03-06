import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

def pisahkan(judul):
    print('='*60)
    print(judul.upper())
    print('='*60)

a = np.array([1,2,3,4])
print(a)

A = np.array([[3,1,2],
            [2,3,4]])
B = np.array([[0,1],
[2,3],
[4,5]])
C = np.array([[0,1],
[2,3],[4,5],[0,1]])

print("A is a {} matrix".format(A.shape))
print("B is a {} matrix".format(B.shape))
print("C is a {} matrix".format(C.shape))

print(3*A)
print(A*A)
print(A-A)
print(A+A)
print(A/A)

print('='*60)
print('DOT PRODUCT')
print('='*60)
print(A.dot(B))



pisahkan('LEARNING RATE')
# Too large = overshoot, too small = won't get minimum point 
df = pd.read_csv('datasets/banknotes.csv')
print(df.columns) 
print(df['class'].value_counts())
# import seaborn as sns 
# sns.pairplot(df,hue='class')
# plt.show()

pisahkan('BASELINE MODEL FOR BANKNOTES FROM LEARNING RATE')
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import scale

X = scale(df.drop('class',axis=1).values)
y = df['class'].values

model = RandomForestClassifier(n_estimators=10)
check = cross_val_score(model,X,y)
print(check)

pisahkan('Logistic Regression Model')
X_train, X_test,y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)

import keras.backend as K 
from keras.models import Sequential 
from keras.layers import Dense, Activation 
from keras.optimizers import SGD 

model = Sequential() 
model.add(Dense(1,input_shape=(4,),activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='sgd',metrics=['accuracy'])
history = model.fit(X_train, y_train)
result = model.evaluate(X_test,y_test)

historydf = pd.DataFrame(history.history, index=history.epoch)
plt.plot(history.history['acc'])
plt.xlabel('epoch')
plt.legend(['train','test'],loc='best')
plt.show()
plt.title("Test accuracy: {:3.1f} % ".format(result[1]*100),fontsize=15)
plt.show()

pisahkan('Learning rates')#having trouble with lines not showing. 
dflist = []
learning_rates = [0.01,0.05,0.1,0.5]

for lr in learning_rates:
    K.clear_session()

    model = Sequential()
    model.add(Dense(1, input_shape=(4,), activation='sigmoid'))
    model.compile(loss='binary_crossentropy',optimizer=SGD(lr=lr),metrics=['accuracy'])
    h = model.fit(X_train,y_train,batch_size=16,verbose=0)
    dflist.append(pd.DataFrame(h.history, index=h.epoch))
historydf = pd.concat(dflist,axis=1)
metrics_reported = dflist[0].columns
idx = pd.MultiIndex.from_product([learning_rates,metrics_reported],names=['learning_rate','metric'])
historydf.columns = idx
print(historydf)
ax = plt.subplot(211)
historydf.xs('loss',axis=1,level='metric').plot(ylim=(0,1), ax=ax)
plt.title('Loss')

ax = plt.subplot(212)
historydf.xs('acc',axis=1,level='metric').plot(ylim=(0,1),ax=ax)
plt.title("Accuracy")
plt.xlabel("Epochs")
plt.tight_layout() 
plt.show()

pisahkan("Batch Sizes") 
