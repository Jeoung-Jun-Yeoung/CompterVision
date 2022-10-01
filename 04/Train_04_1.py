import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpend():
    print("Camera open failed!")
    exit()

print('Frame width:', int(cap.get(cv.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
