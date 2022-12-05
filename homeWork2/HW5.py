import numpy as np
import cv2 as cv
import random
import math

rst = []


def img_trim(x, y, w, h, img):
    img_tr = img[y:y + h, x: x + w]

    cv.imshow('test', img_tr)
    cv.waitKey()
    hough_circles(img_tr)

    return img_tr


def setLabel(img, pts, label):
    (x, y, w, h) = cv.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x+w, y+h)
    cv.rectangle(img, pt1, pt2, (0, 0, 255), 1)
    cv.putText(img, label, pt1, cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))


# 7,8,9
path = "/Users/jeongjun-yeong/GitHub/CompterVision/homeWork2/hw2/case5/img5_7.png"


def contours_basic(img):
    src = cv.imread(
        path, cv.IMREAD_COLOR)

    if src is None:
        print("error")
    dst = img.copy()

    cv.imshow("img", img)

    cv.waitKey()

    # noise = np.zeros(gray.shape, np.int32)
    # cv.randn(noise, 0, 5)
    # cv.add(gray, noise, gray, dtype=cv.CV_8UC1)

    # dst1 = cv.GaussianBlur(gray, (0, 0), 5)
    # # dst1 = cv.bilateralFilter(gray, -1, 10, 5)

    # ret, dst = cv.threshold(dst1, 127, 255, cv.THRESH_BINARY)

    contours, hier = cv.findContours(dst, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    cv.imshow("test", dst)

    cv.waitKey()

    for pts in contours:
        if cv.contourArea(pts) < 100:
            continue
        approx = cv.approxPolyDP(pts, cv.arcLength(pts, True)*0.03, True)
        vtc = len(approx)

        if vtc == 3:
            setLabel(src, pts, "TRI")
        if vtc == 4:
            setLabel(src, pts, "RECT")

            x, y, w, h = cv.boundingRect(pts)
            # print(f"사각형 좌표 {x, y, w, h}")
            img_trim(x, y, w, h, dst)

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
                              cv.HOUGH_GRADIENT, 1, 25, param1=140, param2=20)

    if circles is not None:
        print(f"check {len(circles[0])}")
        rst.append(len(circles[0]))
# 1 6


def color_split():
    src = cv.imread(
        path, cv.IMREAD_COLOR)
    dst = cv.cvtColor(src, cv.COLOR_YCrCb2RGB)
    dst2 = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    if src is None:
        print("error")
        return

    noise = np.zeros(dst2.shape, np.int32)
    cv.randn(noise, 0, 5)
    cv.add(dst2, noise, dst2, dtype=cv.CV_8UC1)

    dst3 = cv.subtract(dst2, 30)  # type: ignore

    cv.imshow('test1', dst3)
    cv.imshow('test2', dst2)

    cv.waitKey()

    # dst1 = cv.bilateralFilter(gray, -1, 10, 5)

    ret, test = cv.threshold(dst3, 120, 255, cv.THRESH_BINARY)

    # cv.imshow('bdst', bdst)
    # cv.imshow('gdst', gdst)
    # cv.imshow('rdst', rdst)
    # cv.imshow('test2', test)
    cv.imshow('test0', test)

    cv.waitKey()
    cv.destroyAllWindows()
    return test


img = color_split()

cv.destroyAllWindows()
contours_basic(img)
exit()
