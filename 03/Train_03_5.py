import numpy as np
import cv2 as cv


def func3():
    img1 = cv.imread('./CVImages/cat.bmp')

    img2 = img1
    img3 = img1.copy()
    img1[:, :] = (255, 0, 255)
    # yellow

    cv.imshow('img1', img1)
    cv.imshow('img2', img2)
    cv.imshow('img3', img3)
    cv.waitKey()
    cv.destroyAllWindows()


func3()

# img에서도 행렬의 복사과정이 드러난다.
