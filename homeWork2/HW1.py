import numpy as np
import cv2 as cv


def hough_circles():
    img = cv.imread(
        "/Users/jeongjun-yeong/GitHub/CompterVision/homeWork2/case1.png", cv.IMREAD_GRAYSCALE)

    if img is None:
        print("error")

    img = cv.medianBlur(img, 5)
    cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

    circles = cv.HoughCircles(img,
                              cv.HOUGH_GRADIENT, 1, 20, param1=150, param2=30)

    circles = np.uint16(np.around(circles))

    print(len(circles[0]))

    cv.imshow('img', img)
    cv.imshow('c2', cimg)
    cv.waitKey()
    cv.destroyAllWindows()


hough_circles()

cv.waitKey()
cv.destroyAllWindows()
