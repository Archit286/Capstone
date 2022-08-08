import numpy as np
import tensorflow as tf
import cv2

labels = ["Closed", "Open"]
threshold = 0.5
model = tf.keras.models.load_model("./input/blink.h5")
faceCascade = cv2.CascadeClassifier("./input/haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("./input/haarcascade_eye.xml")


def blink(img):
    flag = 0
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) == 0:
        return "Face not detected", img
    else:
        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            eyes = eyeCascade.detectMultiScale(roi_gray)
            if len(eyes) == 0:
                return "eyes not detected", img
            else:
                for ex, ey, ew, eh in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)
                    eyes_roi = roi_color[ey:ey + eh, ex:ex + ew]
                    final_img = cv2.resize(eyes_roi, (224, 224))
                    final_img = np.expand_dims(final_img, axis=0)
                    final_img = final_img / 255.0
                    prediction = model.predict(final_img)

                    if prediction[0][0] < threshold:
                        flag = 1
                        break

    if flag:
        return labels[1], img
    else:
        return labels[0], img
