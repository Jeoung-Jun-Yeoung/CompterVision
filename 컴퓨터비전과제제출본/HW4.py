import numpy as np
import cv2 as cv
import random
import math

rst = []


def img_trim(x, y, w, h, img):
    img_tr = img[y:y + h, x: x + w]

    hough_circles(img_tr)

    return img_tr


def setLabel(img, pts, label):
    (x, y, w, h) = cv.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x+w, y+h)
    cv.rectangle(img, pt1, pt2, (0, 0, 255), 1)
    cv.putText(img, label, pt1, cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
# 1 or 6


path = "/Users/jeongjun-yeong/GitHub/CompterVision/homeWork2/hw2/case4/img4_1.png"


def contours_basic(img):
    src = cv.imread(
        path, cv.IMREAD_COLOR)

    if src is None:
        print("error")
    dst = img.copy()

    contours, hier = cv.findContours(dst, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

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

            img_trim(x, y, w, h, dst)

        else:
            lenth = cv.arcLength(pts, True)
            area = cv.contourArea(pts)
            ratio = 4. * math.pi * area / (lenth * lenth)
            if ratio > 0.85:
                setLabel(src, pts, "CIR")


def hough_circles(img):

    if img is None:
        print("error")

    blurred = cv.blur(img, (3, 3))
    circles = cv.HoughCircles(blurred,
                              cv.HOUGH_GRADIENT, 1, 25, param1=140, param2=20)

    if circles is not None:
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

    bgr_place = cv.split(src)

    noise = np.zeros(dst2.shape, np.int32)
    cv.randn(noise, 0, 5)
    cv.add(dst2, noise, dst2, dtype=cv.CV_8UC1)

    dst3 = cv.GaussianBlur(dst2, (0, 0), 5)

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


img = color_split()

contours_basic(img)

rst.sort()
for i in rst:
    print(f"{i}")
exit()
