import numpy as np
import cv2 as cv


def sharp(img):
    for sigma in range(1, 6):
        blurred = cv.GaussianBlur(img, (0, 0), sigma)

        alpha = 1.0
        dst = cv.addWeighted(img, 1 + alpha, blurred, -alpha, 0.0)

        desc = "sigma: %d" % sigma
        cv.putText(dst, desc, (10, 30), cv.FONT_HERSHEY_SIMPLEX,
                   1.0, 255, 1, cv.LINE_AA)

        return dst


def hough_circles():
    img = cv.imread(
        "homeWork2/hw2/case3/img3_4.png", cv.IMREAD_COLOR)

    img = sharp(img)

    cv.imshow('img', img)
    if img is None:
        print("error")
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.medianBlur(img, 5)
    cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

    circles = cv.HoughCircles(img,
                              cv.HOUGH_GRADIENT, 1, 20, param1=200, param2=17, minRadius=10, maxRadius=20)

    circles = np.uint16(np.around(circles))

    print(len(circles[0]))

    for i in circles[0, :]:
        cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)

    cv.imshow('img', img)
    cv.imshow('c2', cimg)
    cv.waitKey()
    cv.destroyAllWindows()


hough_circles()
