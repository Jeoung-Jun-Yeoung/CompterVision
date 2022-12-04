import numpy as np
import cv2 as cv
import random
import math

rst = []


def sharp(img):
    for sigma in range(1, 6):
        blurred = cv.GaussianBlur(img, (0, 0), sigma)

        alpha = 2.0
        dst = cv.addWeighted(img, 1 + alpha, blurred, -alpha, 0.0)

        # desc = "sigma: %d" % sigma
        # cv.putText(dst, desc, (10, 30), cv.FONT_HERSHEY_SIMPLEX,
        #            1.0, 255, 1, cv.LINE_AA)

        return dst

# /Users/jeongjun-yeong/GitHub/CompterVision/homeWork2/hw2/case3/img3_3.png
# /Users/jeongjun-yeong/GitHub/CompterVision/homeWork2/case2.jpg

# /Users/jeongjun-yeong/GitHub/CompterVision/homeWork2/images/contours.bmp


def img_trim(x, y, w, h, img):
    img_tr = img[y:y + h, x: x + w]
    # cv.imshow('test', img_tr)
    hough_circles(img_tr)

    # cv.waitKey()

    return img_tr


def setLabel(img, pts, label):
    (x, y, w, h) = cv.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x+w, y+h)
    cv.rectangle(img, pt1, pt2, (0, 0, 255), 1)
    cv.putText(img, label, pt1, cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))


def contours_basic():
    src = cv.imread(
        "/Users/jeongjun-yeong/GitHub/CompterVision/homeWork2/case2.jpg", cv.IMREAD_GRAYSCALE)

    if src is None:
        print("error")

    ret, img = cv.threshold(src, 127, 255, cv.THRESH_BINARY)

    contours, hier = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    for pts in contours:
        if cv.contourArea(pts) < 400:
            continue
        approx = cv.approxPolyDP(pts, cv.arcLength(pts, True)*0.02, True)
        vtc = len(approx)

        if vtc == 3:
            setLabel(src, pts, "TRI")
        if vtc == 4:
            setLabel(src, pts, "RECT")

            x, y, w, h = cv.boundingRect(pts)
            # print(f"사각형 좌표 {x, y, w, h}")
            img_trim(x, y, w, h, img)

        else:
            lenth = cv.arcLength(pts, True)
            area = cv.contourArea(pts)
            ratio = 4. * math.pi * area / (lenth * lenth)
            if ratio > 0.85:
                setLabel(src, pts, "CIR")

    # for i in range(len(contours)):
    #     cv.drawContours(src, [contours[i]], 0, (0, 0, 255), 2)
    #     cv.imshow("src", src)

    cv.imshow('src', src)
    cv.waitKey()
    cv.destroyAllWindows()


def hough_circles(img):

    if img is None:
        print("error")

    blurred = cv.blur(img, (3, 3))

    circles = cv.HoughCircles(blurred,
                              cv.HOUGH_GRADIENT, 1, 30, param1=150, param2=20)

    print(f"check {len(circles[0])}")
    rst.append(len(circles[0]))


contours_basic()
rst.sort()
rst.reverse()
for i in rst:
    print(f"{i}")
exit()
# hough_circles()

# img = cv.imread(
#     "/Users/jeongjun-yeong/GitHub/CompterVision/homeWork2/case1.png", cv.IMREAD_GRAYSCALE)


# if img is None:
#     print("error")

# cv.imshow('img', img)
