import pandas as pd
import colorgram
import numpy as np
import tensorflow as tf
import os

def rgb_to_hex(r, g, b):
    '''Function to convert RGB to hexcode'''
    return '#%02x%02x%02x' % (r, g, b)

colors_df = pd.DataFrame({"label" : range(11), "color": ['red', 'green', 'blue',
    'yellow', 'orange', 'pink', 'purple', 'brown', 'grey', 'black', 'white']})
v = np.vectorize(rgb_to_hex)

lts = os.listdir("covers")

model = tf.keras.models.load_model('color_model.h5')

appended_df = pd.DataFrame()

for fn in lts:
    red, green, blue, proportion = [], [], [], []
    colors = colorgram.extract("covers/"+fn, 6)
    for y in range(len(colors)):
        if colors[y].proportion > 0.05:
            red.append(colors[y].rgb[0])
            green.append(colors[y].rgb[1])
            blue.append(colors[y].rgb[2])
            proportion.append(colors[y].proportion)

    working_final = pd.DataFrame({"red": red, "green":green, "blue":blue})

    predictions = model.predict(working_final)
    predicted_encoded = np.argmax(predictions, axis=1)
    predicted_encoded_labels = pd.DataFrame(predicted_encoded, columns=['label'])

    final = predicted_encoded_labels.merge(colors_df, how='left')
    working_final['hexcode'] = working_final.apply(lambda x: rgb_to_hex(x.red, x.green, x.blue), axis = 1)

    json_df = pd.DataFrame({"proportion": proportion, "hexcode": working_final["hexcode"], "color": final["color"]})
    json_df['book'] = fn
    appended_df = appended_df.append(json_df)
appended_df.to_csv("all_book_cover_colors.csv", index=False)
