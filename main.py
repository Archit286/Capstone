import cv2
from time import time
from face import blink
from yawn import yawn
import firebase

blink_counter = 0
yawn_counter = 0
alarm_level_1 = 6
alarm_level_2 = 12

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


def detect(img):
    global blink_counter, yawn_counter, alarm_level_2, alarm_level_1
    blink_status, final_img = blink(img)
    print("Blink_Status = " + blink_status)
    yawn_status = yawn(img)
    print("Yawn Status = " + yawn_status)

    if blink_status == "Closed":
        blink_counter = blink_counter + 1
    else:
        blink_counter = 0
        firebase.setAlarm(0)

    if yawn_status == "Yawn":
        yawn_counter = yawn_counter + 1
    else:
        yawn_counter = 0
        firebase.setAlarm(0)

    if yawn_counter > alarm_level_2 or blink_counter > alarm_level_2:
        firebase.setAlarm(2)
    elif yawn_counter > alarm_level_1 or blink_counter > alarm_level_1:
        firebase.setAlarm(1)

    if firebase.checkAlarm() == 2:
        print("Trigger Vibration Motor")

    # check sos

    text = "Blink Counter = " + str(blink_counter) + ", Yawn Counter = " + str(yawn_counter)
    final_img = cv2.rectangle(final_img, (0, 0), (final_img.shape[1], 50), (0, 0, 0), -1)
    final_img = cv2.putText(final_img, text, (int(final_img.shape[1] / 4), 25), cv2.FONT_HERSHEY_TRIPLEX, 0.5,
                            (0, 0, 255), 1, cv2.LINE_AA)

    return final_img


while True:
    t0 = time()

    frame = None
    success, frame = cap.read()

    if success:
        img = detect(frame)
        cv2.imshow("FRAME", img)
        cv2.waitKey(0)
    else:
        print('Error in Camera')  # For debugging purposes
        continue

    print('time taken:   ')
    print(time() - t0)
