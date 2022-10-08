import numpy as np
import cv2 as cv


src = cv.imread('homeWork/sample.jpeg', cv.IMREAD_GRAYSCALE)

if src is None:
    print("Image load failed!")

cv.imshow('src', src)
cv.waitKey()
cv.destroyAllWindows()
