import numpy as np
import tensorflow as tf
from tensorflow import keras



def get_random(length):
    return np.random.random(length)


def get_baker(length):
    a = np.zeros(length)
    x = np.random.random()
    for i in range(length):
        x = x * 3.0
        x = x - int(x)
        a[i] = x
    return a


def make_data(n, length):
    x = []
    y = []
    for _ in range(length):
        if (np.random.random() < 0.5):
            x.append(get_random(n))
            y.append(0)
        else:
            x.append(get_baker(n))
            y.append(1)

    x = np.array(x)
    y = np.array(y)

    return x, y


def create_model():
    model = keras.Sequential([
        keras.layers.Dense(100),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(2, activation='softmax')
    ])
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    return model


if __name__=='__main__':

    model = create_model()
    model.load_weights('backer')

    all_random_data = np.array([get_random(100) for _ in range(100)])
    all_random_labels = np.array([0] * 100)

    random_loss, random_acc = model.evaluate(all_random_data, all_random_labels)

    print("When everything is random")
    print(f"Test Loss = {random_loss}")
    print(f"Test Accuracy = {random_acc}")

    all_baker_data = np.array([get_baker(100) for _ in range(100)])
    all_baker_labels = np.array([1] * 100)

    baker_loss, baker_acc = model.evaluate(all_baker_data, all_baker_labels)

    print("When everything is baker")
    print(f"Test Loss = {baker_loss}")
    print(f"Test Accuracy = {baker_acc}")

