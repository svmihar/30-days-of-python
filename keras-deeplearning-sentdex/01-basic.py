import tensorflow as tf 

mnist = tf.keras.datasets.mnist #28x28 images of handwritten digits 0-9

(x_train, y_train),(x_test,y_test) = mnist.load_data()

#normalize, so easire to calculate
x_train=tf.keras.utils.normalize(x_train, axis=1) #0-1 
x_test = tf.keras.utils.normalize(x_test, axis=1) #0-1

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Flatten(input_shape=(x_train[0].shape))) #why do we have to flatten shit?
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu)) #activation
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu)) #activation
model.add(tf.keras.layers.Dense(10,activation=tf.nn.softmax)) #number of classification, softmax for probability dist.

#define paramaters for training
model.compile(optimizer='adam', 
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']) 
#loss function so know when to stop, optimizer always minimize loss 

#train model
model.fit(x_train, y_train, epochs=2005)

#to prevent OVERFITTING, we need evaluate the val_loss. 
# Learn pattenrs, not memorizing
val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)

# from keras.models import load_model
# save model 

"""model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

model.save_weights("model.h5")
#model.save('mnist_model_reader.model')
"""
model.save('mnist_model.model')

new_model = tf.keras.models.load_model('mnist_model.model')
predictions = new_model.predict([x_test])

print(predictions)  

# import matplotlib.pyplot as plt 

# plt.imshow(x_train[0], cmap= plt.cm.binary)
# plt.show()
# print(x_train[0])