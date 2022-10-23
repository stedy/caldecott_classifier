"""This script uses a pre-compiled list of RGB values mapped to color names and
then builds a model using tensorflow and outputs that model as an hd5 file"""

import pandas as pd
import tensorflow as tf

raw_data = \
pd.read_csv("https://raw.githubusercontent.com/AjinkyaChavan9/RGB-Color-Classifier-with-Deep-Learning-using-Keras-and-Tensorflow/master/Dataset/final_data.csv",
        sep = ",")

numerical_data = pd.get_dummies(raw_data, columns = ['label'])

train_dataset = numerical_data.sample(frac=0.8, random_state=108)
test_dataset = numerical_data.drop(train_dataset.index)

colors = ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Pink',\
        'Purple', 'Brown', 'Grey', 'Black', 'White']
color_labels = ['label_' + x for x in colors]

train_labels = pd.DataFrame([train_dataset.pop(x) for x in color_labels]).T
test_labels = pd.DataFrame([test_dataset.pop(x) for x in color_labels]).T

model = tf.keras.Sequential([
    tf.keras.layers.Dense(3, kernel_regularizer=tf.keras.regularizers.l2(0.001),
        activation='relu', input_shape=[len(train_dataset.keys())]),
    tf.keras.layers.Dense(24, kernel_regularizer=tf.keras.regularizers.l2(0.001), activation='relu'),
    tf.keras.layers.Dense(24, kernel_regularizer=tf.keras.regularizers.l2(0.001), activation='relu'),
    tf.keras.layers.Dense(16, kernel_regularizer=tf.keras.regularizers.l2(0.001), activation='relu'),
    tf.keras.layers.Dense(11)
  ])

optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
loss_function = tf.keras.losses.CategoricalCrossentropy(from_logits=True)

model.compile(loss=loss_function,
                optimizer=optimizer,
                metrics=['accuracy'])

print(model.summary())

history = model.fit(x=train_dataset, y=train_labels, validation_split = 0.2,
        epochs = 5000, batch_size = 2048, shuffle=True)

model.save('color_model.h5')


print(model.summary())
