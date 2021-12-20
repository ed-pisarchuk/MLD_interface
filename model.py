import numpy as np
from keras.models import load_model
import tensorflow as tf
from mo_data import mo_data_by_classes
import numpy as np

model = load_model('mo_classification_model.hdf5')


def show_cards_by_prediction(predictions):
    cards = []
    i = 0

    for class_num in np.argsort(-predictions):
        cards.append({
            'name': mo_data_by_classes[class_num]['name'],
            'image': mo_data_by_classes[class_num]['image'],
            'percent': '{:3.3f}'.format(predictions[class_num] * 100)
        })
        i += 1
        if i == 3:
            break
    print(predictions, cards)
    return cards


def process_image(picName):
    img = tf.keras.preprocessing.image.load_img(
        picName,
        target_size=(320, 320)
    )
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    return [picName.split('/')[-1], show_cards_by_prediction(predictions[0])]
