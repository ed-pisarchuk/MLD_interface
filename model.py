import numpy as np
from keras.models import load_model
import tensorflow as tf
from mo_data import mo_data_by_classes

model = load_model('mo_classification_model.hdf5')


def process_image(picName):
    img = tf.keras.preprocessing.image.load_img(
        picName,
        target_size=(320, 320)
    )
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    mo_class = np.argmax(predictions, axis=1)[0]
    return [mo_data_by_classes[mo_class]['name'], mo_data_by_classes[mo_class]['image']]
