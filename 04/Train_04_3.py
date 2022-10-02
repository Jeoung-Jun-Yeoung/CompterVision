import numpy as np
import cv2 as cv

from turtle import delay
import numpy as np
import cv2 as cv

cap = cv.VideoCapture("stopwatch.avi")

if not cap.isOpened():
    print("Video open failed!")
    exit()

while True:
    ret, frame = cap.read()
    # 각 frame을 읽어서

    if not ret:
        break

    inversed = ~frame
    # frame을 반전시킨다.

    cv.imshow("frame", frame)
    cv.imshow("inversed", inversed)

    if cv.waitKey(delay) == 27:
        break

cv.destroyAllWindows()
