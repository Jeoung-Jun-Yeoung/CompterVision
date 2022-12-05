import numpy as np
import cv2 as cv
import random
import math

rst = []


def img_trim(x, y, w, h, img):
    img_tr = img[y:y + h, x: x + w]
    # cv.imshow('test', img_tr)
    # cv.waitKey()
    hough_circles(img_tr)

    return img_tr


def setLabel(img, pts, label):
    (x, y, w, h) = cv.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x+w, y+h)
    cv.rectangle(img, pt1, pt2, (0, 0, 255), 1)
    cv.putText(img, label, pt1, cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))


# /Users/jeongjun-yeong/GitHub/CompterVision/homeWork2/hw2/case3/img3_2.png -> 통과

# /Users/jeongjun-yeong/GitHub/CompterVision/homeWork2/hw2/case3/img3_4.png -> 통과


def contours_basic():
    src = cv.imread(
        "/Users/jeongjun-yeong/GitHub/CompterVision/homeWork2/hw2/case3/img3_2.png", cv.IMREAD_COLOR)

    if src is None:
        print("error")

    noise = np.zeros(src.shape, np.int32)
    cv.randn(noise, 0, 5)
    cv.add(src, noise, src, dtype=cv.CV_8UC1)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    dst1 = cv.GaussianBlur(gray, (0, 0), 5)

    ret, dst = cv.threshold(dst1, 127, 255, cv.THRESH_BINARY)

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
            # print(f"사각형 좌표 {x, y, w, h}")
            img_trim(x, y, w, h, dst)

        else:
            lenth = cv.arcLength(pts, True)
            area = cv.contourArea(pts)
            ratio = 4. * math.pi * area / (lenth * lenth)
            if ratio > 0.85:
                setLabel(src, pts, "CIR")

    cv.imshow('src', src)
    cv.waitKey()
    cv.destroyAllWindows()


def hough_circles(img):

    if img is None:
        print("error")

    blurred = cv.blur(img, (3, 3))

    circles = cv.HoughCircles(blurred,
                              cv.HOUGH_GRADIENT, 1, 30, param1=150, param2=20)

    if circles is not None:
        rst.append(len(circles[0]))


contours_basic()
rst.sort()

for i in rst:
    print(f"{i}")
exit()
