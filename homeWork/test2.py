import numpy as np
import cv2 as cv

cap = cv.VideoCapture('computervison_video.mp4')

if not cap.isOpened():
    print("Camera open failed!")
    exit()

width = round(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

fps = cap.get(cv.CAP_PROP_FPS)


fourcc = cv.VideoWriter_fourcc(*'DIVX')
delay = round(1000 / fps)

outputVideo = cv.VideoWriter("test.avi", fourcc, fps, (width, height))

if not outputVideo.isOpened():
    print("File open failed!")
    exit()

# delay 만큼 frame을 처리해야함

while True:
    ret, frame = cap.read()
    if not ret:
        break

    outputVideo.write(frame)
    cv.imshow("frame", frame)

    if cv.waitKey(delay) == 27:
        break

cv.destroyAllWindows()
