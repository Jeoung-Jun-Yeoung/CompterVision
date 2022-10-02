from turtle import delay
import numpy as np
import cv2 as cv

cap = cv.VideoCapture("stopwatch.avi")

if not cap.isOpened():
    print("Video open failed!")
    exit()

print('Frame width:', int(cap.get(cv.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
print('Frame count:', int(cap.get(cv.CAP_PROP_FRAME_COUNT)))


fps = cap.get(cv.CAP_PROP_FPS)

print('FPS:', fps)
delay = round(1000 / fps)
