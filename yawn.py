import numpy as np
import tensorflow as tf
import cv2

labels = ["no_yawn", "yawn"]
model = tf.keras.models.load_model("./input/yawn.h5")


def yawn(img):
    new_array = cv2.resize(img, (224, 224))
    X_input = np.array(new_array).reshape(1, 224, 224, 3)
    X_input = X_input / 255.0
    prediction = model.predict(X_input)
    return labels[prediction.astype(int)[0][0]]
