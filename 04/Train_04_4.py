import numpy as np
import cv2 as cv

cap = cv.VideoCapture("stopwatch.avi")


if not cap.isOpened():
    print("Video open failed!")
    exit()

w = round(cap.get(cv.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

fps = cap.get(cv.CAP_PROP_FPS)

fourcc = cv.VideoWriter_fourcc(*"DIVX")
delay = round(1000 / fps)

outputVideo = cv.VideoWriter("output.avi", fourcc, fps, (w, h))

if not outputVideo.isOpened():
    print("File open failed!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    inversed = ~frame
    outputVideo.write(inversed)

    cv.imshow("frame", frame)
    cv.imshow("inversed", inversed)

    if cv.waitKey(delay) == 27:
        break

cv.destroyAllWindows()
