import numpy as np
import cv2 as cv
import random
import math

path = "/Users/jeongjun-yeong/GitHub/CompterVision/homeWork2/hw2/case4/img4_1.png"


def color_split():
    src = cv.imread(
        path, cv.IMREAD_COLOR)
    dst = cv.cvtColor(src, cv.COLOR_YCrCb2RGB)
    dst2 = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    if src is None:
        print("error")
        return

    bgr_place = cv.split(src)

    noise = np.zeros(dst2.shape, np.int32)
    cv.randn(noise, 0, 5)
    cv.add(dst2, noise, dst2, dtype=cv.CV_8UC1)

    dst3 = cv.GaussianBlur(dst2, (0, 0), 5)
    # dst1 = cv.bilateralFilter(gray, -1, 10, 5)

    ret, dst4 = cv.threshold(dst3, 100, 255, cv.THRESH_BINARY)

    temp = cv.merge((bgr_place[1], bgr_place[0], bgr_place[2]))
    temp1 = cv.merge((bgr_place[2], bgr_place[0], bgr_place[1]))
    temp2 = cv.merge((bgr_place[0], bgr_place[2], bgr_place[1]))

    ret, bdst = cv.threshold(bgr_place[0], 127, 255, cv.THRESH_BINARY)
    ret, gdst = cv.threshold(bgr_place[1], 150, 255, cv.THRESH_BINARY)
    ret, rdst = cv.threshold(bgr_place[2], 10, 255, cv.THRESH_BINARY)
    ret, test = cv.threshold(temp, 120, 255, cv.THRESH_BINARY)
    tet = cv.cvtColor(test, cv.COLOR_BGR2GRAY)

    return tet


# rst.sort()
# rst.reverse()
# for i in rst:
#     print(f"{i}")
img = color_split()


def erode_dilate(img):
    cv.imshow('img', img)

    _, src_bin = cv.threshold(img, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    dst1 = cv.erode(src_bin, None)
    dst2 = cv.dilate(src_bin, None)
    cv.imshow('dst1', dst1)
    cv.imshow('dst2', dst2)
    cv.waitKey()
    cv.destroyAllWindows()


erode_dilate(img)
