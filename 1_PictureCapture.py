# -*- coding: utf-8 -*-
import cv2
import time

cap = cv2.VideoCapture(1)

index = 0
while True:
    ret, frame = cap.read()
    # frame = cv2.flip(frame, -1)
    cv2.imshow("img", frame)
    times = time.time()
    key = cv2.waitKey(1)
    if key == ord('w'):
        path = "./cam/" + str(times) + ".jpg"
        cv2.imwrite(path, frame)
    index = index + 1