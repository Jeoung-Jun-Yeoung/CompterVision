import numpy as np
import cv2 as cv


def hough_circles():
    img = cv.imread(
        "/Users/jeongjun-yeong/GitHub/CompterVision/homeWork2/case1.png", cv.IMREAD_GRAYSCALE)

    if img is None:
        print("error")

    img = cv.medianBlur(img, 5)

    circles = cv.HoughCircles(img,
                              cv.HOUGH_GRADIENT, 1, 20, param1=150, param2=30)

    circles = np.uint16(np.around(circles))

    print(len(circles[0]))  # type: ignore


hough_circles()
