import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    exit()

width = round(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

fps = cap.get(cv.CAP_PROP_FPS)


fourcc = cv.VideoWriter_fourcc('M', 'J', 'P', 'G')
delay = round(1000 / fps)

outputVideo = cv.VideoWriter("test.avi", fourcc, fps, (width, height))

if not outputVideo.isOpened():
    print("File open failed!")
    exit()

# delay 만큼 frame을 처리해야함

while True:
    ret, frame = cap.read()
    if not ret:
        print("Frame read failed!")
        exit()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow("frame", frame)
    outputVideo.write(frame)
    if cv.waitKey(delay) == 27:
        break


cv.destroyAllWindows()
