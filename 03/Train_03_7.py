import numpy as np
import cv2 as cv

# 부분행렬 추출후 반전


def func5():
    img1 = cv.imread('./CVImages/cat.bmp')

    img2 = img1[100:400, 100:400]

    img2 = 255 - img2

    cv.imshow('img1', img1)
    cv.imshow('img2', img2)
    cv.waitKey()
    cv.destroyAllWindows()


func5()
