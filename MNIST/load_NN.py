import numpy as np
import tensorflow as tf
from tensorflow import keras

def load_data():
    train_data, test_data = keras.datasets.mnist.load_data()
    train_images, train_labels = train_data
    test_images, test_labels = test_data
    train_images = train_images / 255.0
    test_images = test_images / 255.0

    return(train_images, train_labels, test_images, test_labels)

def create_models():
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28,28)),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    return model

if __name__ == '__main__':
    (train_images, train_labels, test_images, test_labels) = load_data()

    model=create_models()
    model.load_weights('model')
    

    predictions = model.predict(test_images[0:20])

    for i in range(5):
        predicted_index = np.argmax(predictions[i])
        print(f"prediction = {predicted_index} answer = {test_labels[i]}")
