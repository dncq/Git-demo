# ANN FOR HANDWRITTEN DIGITS CLASSIFICATION USING KERAS, TENSORFLOW

# import all needed modules and libraries
import os
import numpy as np              # (important) working with pixel arrays
import cv2 as cv                # (important) computer vision: load the image
import matplotlib.pyplot as plt # (optional) used for output visualization
import tensorflow as tf         # (important) machine learning

# --------------------------------

# Import datasets
# mnist = tf.keras.datasets.mnist

# # Split into traing and testing data
# # '''X: pixel data (the handwritten digit itself)
# #    y: classified value (the number of image)'''

# (x_train, y_train), (x_test, y_test) = mnist.load_data()

# # Normalizing data (scaling down the pixel values between 0 and 1)
# x_train = tf.keras.utils.normalize(x_train, axis = 1)
# x_test = tf.keras.utils.normalize(x_test, axis = 1)

# #-------------------------------

# # TRAINING PROCESS
# # Working with neural network
# model = tf.keras.models.Sequential()
# model.add(tf.keras.layers.Flatten(input_shape = (28, 28))) # Flattened Layer (Input Layer)
# model.add(tf.keras.layers.Dense(128, activation = 'relu')) # Dense Layer (Hidden Layer)
# model.add(tf.keras.layers.Dense(128, activation = 'relu')) # Dense Layer (Hidden Layer)
# model.add(tf.keras.layers.Dense(10, activation = 'softmax'))  # Output Layer

# # (The softmax function makes sure that all the 10 neurons add up to one,
# # which return the probability between 0 and 1)

# model.compile(optimizer='adam', loss= 'sparse_categorical_crossentropy', metrics = ['accuracy'])

# # Fit the model (train the model)
# model.fit(x_train, y_train, epochs=10)

# model.save('Handwritten.Model')

# LOADING MODEL
model = tf.keras.models.load_model('Handwritten.Model')

# EVALUATING MODEL

# loss, accuracy = model.evaluate(x_test, y_test)

# print(loss)
# print(accuracy)

# READ THE DIGITS
image_number = 0
while os.path.isfile(f"digits/digit{image_number}.png"):
    try:
        img = cv.imread(f"digits/digit{image_number}.png")[:,:,0]
        img = np.invert(np.array([img]))
        prediction = model.predict(img)
        print(f"This digit is probably a {np.argmax(prediction)}")
        plt.imshow(img[0], cmap = plt.cm.binary)
        plt.show()
    except:
        print("Error!")
    finally:
        image_number += 1 
