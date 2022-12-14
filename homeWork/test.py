import numpy as np
import cv2 as cv


cap = cv.VideoCapture('test.avi')

if cap is None:
    print("Image load failed!")

width = round(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

fps = cap.get(cv.CAP_PROP_FPS)


fourcc = cv.VideoWriter_fourcc('M', 'J', 'P', 'G')
delay = round(1000 / fps)

outputVideo = cv.VideoWriter("testOutput.avi", fourcc, fps, (width, height))

if not outputVideo.isOpened():
    print("File open failed!")
    exit()


while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('gray', gray)
    outputVideo.write(gray)
    if cv.waitKey(round(1000/fps)) == 27:
        break


cv.destroyAllWindows()
