import os
import cv2
from time import time
from face import blink
from yawn import yawn

blink_counter = 0
blink_threshold = 6
yawn_counter = 0
yawn_threshold = 6
test = "./test"


def detect(img):
    global blink_counter, blink_threshold, yawn_threshold, yawn_counter
    blink_status, final_img = blink(img)
    print("Blink_Status = " + blink_status)
    yawn_status = yawn(img)
    print("Yawn Status = " + yawn_status)

    if blink_status == "Closed":
        blink_counter = blink_counter + 1
    elif blink_status == "Open":
        blink_counter = 0

    if yawn_status == "yawn":
        yawn_counter = yawn_counter + 1
    elif yawn_status == "no_yawn":
        yawn_counter = 0

    if yawn_counter > yawn_threshold:
        print("Yawning")

    if blink_counter > blink_threshold:
        print("Sleepy")

    text = "Blink Counter = " + str(blink_counter) + ", Yawn Counter = " + str(yawn_counter)
    final_img = cv2.rectangle(final_img, (0, 0), (final_img.shape[1], 50), (0, 0, 0), -1)
    final_img = cv2.putText(final_img, text, (int(final_img.shape[1]/4), 25), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

    return final_img


for image in os.listdir(test):
    path = os.path.join(test, image)
    final_path = os.path.join("./result", image)
    t0 = time()

    img = cv2.imread(path)
    final_img = detect(img)
    cv2.imwrite(final_path, final_img)

    print('time taken:   ')
    print(time() - t0)
