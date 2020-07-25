import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['Top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
                'Sandals', 'Shirt', 'Sneaker', 'Bag', 'Ankle Boots']

train_images = train_images / 255.0
test_images = test_images / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape = (28, 28)),
    keras.layers.Dense(128, activation= 'relu'),
    keras.layers.Dense(10, activation= 'softmax')
])

model.compile(optimizer='adam', 
                loss= 'sparse_categorical_crossentropy', 
                metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=1, shuffle=True)

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose= 1)
print('Test Accuracy is ' + str(test_acc))

prediction = model.predict(test_images)
print(class_names[np.argmax(prediction[260])])

plt.figure()
plt.imshow(test_images[260])
plt.colorbar()
plt.grid(False)
plt.show()