from Sequential import Sequential
from Conv2D import Conv2D
from Pool import Pool
from Dense import Dense
from Flatten import Flatten
from Dropout import Dropout
from Preprocessing import normalize
import numpy as np
import pandas as pd

model = Sequential()
# model.add(Conv2D(6, (3, 3), padding='same', activation='relu', input_shape=(28, 28, 1)))
# model.add(Pool((2, 2), method='average', strides=(2, 2), input_shape=(28, 28, 6)))
# model.add(Conv2D(16, (5, 5), padding='valid', activation='relu', input_shape=(14, 14, 6)))
# model.add(Pool((2, 2), method='max', strides=(2, 2), input_shape=(10, 10, 16)))
# model.add(Flatten())
# model.add(Dense(400, 120, activation='relu', input_shape=(5, 5, 16)))
# model.add(Dense(120, 84, activation='relu', input_shape=(400, 1)))
# model.add(Dense(84, 10, activation='softmax', input_shape=(84, 1)))


# model.add(Conv2D(6, (5, 5), padding='valid', activation='relu', input_shape=(28, 28, 1)))
# model.add(Pool((2, 2), method='average', strides=(2, 2), input_shape=(28, 28, 6)))
# model.add(Conv2D(16, (5, 5), padding='valid', activation='relu', input_shape=(12, 12, 6)))
# model.add(Pool((2, 2), method='max', strides=(2, 2), input_shape=(6, 6, 16)))
# model.add(Flatten())
# model.add(Dense(256, 10, activation='softmax', input_shape=(5, 5, 16)))


model.add(Dense(784, 256, activation='relu', input_shape=(784, 1)))
# model.add(Dropout(0.2))
model.add(Dense(256, 64, activation='relu', input_shape=(256, 1)))
# model.add(Dropout(0.2))
model.add(Dense(64, 10, activation='softmax', input_shape=(128, 1)))

training_set = pd.read_csv('D:/Cpp/DigitRecognition/dataset/mnist_train.csv')
X = training_set.iloc[:, 1:].values
Y = training_set.iloc[:, 0].values.reshape(1, -1)
X = X.astype('float64')
X /= 255
# X = X.reshape((-1, 28, 28, 1), order='F')

test_set = pd.read_csv('D:/Cpp/DigitRecognition/dataset/mnist_test.csv')
X_test = test_set.iloc[:, 1:].values
Y_test = test_set.iloc[:, 0].values.reshape(1, -1)
X_test = X_test.astype('float64')
X_test /= 255
# X_test = X_test.reshape((-1, 28, 28, 1), order='F')

model.summary()

model.train(X, Y, epochs=20, batch_size=100, learning_rate=0.1)

Y_pred = model.forward(X_test)
Y_pred = np.argmax(Y_pred, axis=0)
Y_test = Y_test.reshape(-1)
print(model.accuracy(Y_test, Y_pred))
