
# inputs = [1.2,5.1,2.1] 
# weights = [3.1, 2.1, 8.7] # the connections between neurons
# bias = 3 #each neuron has a unique bias

# output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2]\
# + bias # sum(weights*neuron) + bias

# print('%.1f' %output)

import numpy as np
import pandas as pd
from PIL import Image
import os
import keras
import tensorflow as tf
from keras.datasets import mnist
from keras.layers import Dense # Dense layers are "fully connected" layers
from keras.models import Sequential # Documentation: https://keras.io/models/sequential/
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

DirPath = r"C:\Users\DELL\OneDrive\Máy tính\Tài liệu\Introduction to AI\NIST_Dataset\zip_file\by_class\4a"
files = os.listdir(DirPath)
my_data = np.array([[[0]*128]*128])
my_label = np.array([0])
for file in files:
    filename = os.path.join(DirPath, file)
    image = Image.open(filename).convert('L')
    img_inf =  np.array(image)
    my_data = np.r_[my_data,[img_inf]]
    my_label = np.r_[my_label,[1]]

DirPath = r"C:\Users\DELL\OneDrive\Máy tính\Tài liệu\Introduction to AI\NIST_Dataset\zip_file\by_class\4b"
files = os.listdir(DirPath)
for file in files:
    filename = os.path.join(DirPath, file)
    image = Image.open(filename).convert('L')
    img_inf =  np.array(image)
    my_data = np.r_[my_data,[img_inf]]
    my_label = np.r_[my_label,[2]]

DirPath = r"C:\Users\DELL\OneDrive\Máy tính\Tài liệu\Introduction to AI\NIST_Dataset\zip_file\by_class\4c"
files = os.listdir(DirPath)
for file in files:
    filename = os.path.join(DirPath, file)
    image = Image.open(filename).convert('L')
    img_inf =  np.array(image)
    my_data = np.r_[my_data,[img_inf]]
    my_label = np.r_[my_label,[3]]

DirPath = r"C:\Users\DELL\OneDrive\Máy tính\Tài liệu\Introduction to AI\NIST_Dataset\zip_file\by_class\4d"
files = os.listdir(DirPath)
for file in files:
    filename = os.path.join(DirPath, file)
    image = Image.open(filename).convert('L')
    img_inf =  np.array(image)
    my_data = np.r_[my_data,[img_inf]]
    my_label = np.r_[my_label,[4]]

# Setup train and test splits
x_train, x_test, y_train, y_test = train_test_split(my_data,my_label,test_size = 0.2, random_state = 365)
print("Training data shape: ", x_train.shape) # (60000, 28, 28) -- 60000 images, each 28x28 pixels
print("Test data shape", x_test.shape) # (10000, 28, 28) -- 10000 images, each 28x28

# Flatten the images
image_vector_size = 128*128
x_train = x_train.reshape(x_train.shape[0], image_vector_size)
x_test = x_test.reshape(x_test.shape[0], image_vector_size)

image_size = 128*128 # 28*28
num_classes = 5 # ten unique digits

print(x_train.shape)
print(y_train.shape)
model = Sequential()

# The input layer requires the special input_shape parameter which should match
# the shape of our training data.
model.add(Dense(units=256, activation='sigmoid', input_shape=(image_size,)))
model.add(Dense(units=128, activation='sigmoid'))
model.add(Dense(units=num_classes, activation='softmax'))
model.summary()

# x_train = x_train.reshape(x_train.shape[0], image_vector_size)
# x_test = x_test.reshape(x_test.shape[0], image_vector_size)


model.compile(optimizer="sgd", loss="sparse_categorical_crossentropy", metrics=['accuracy'])
history = model.fit(x_train, y_train, batch_size=32, epochs=4, verbose=True, validation_split=.1)
loss, accuracy  = model.evaluate(x_test, y_test, verbose=True)

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['training', 'validation'], loc='best')
plt.show()

print(f'Test loss: {loss:.3}')