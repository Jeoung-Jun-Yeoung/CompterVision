import numpy as np
import cv2 as cv
import random
import math
import matplotlib.pyplot as plt

# 7 , 11

rst = []


def setLabel(img, pts, label):

    (x, y, w, h) = cv.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x+w, y+h)
    cv.rectangle(img, pt1, pt2, (0, 0, 255), 1)
    cv.putText(img, label, pt1, cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))


# 5,6,8,11pass
path = "/Users/jeongjun-yeong/GitHub/CompterVision/homeWork2/hw2/case5/img5_11.png"

src = cv.imread(path, cv.IMREAD_COLOR)

if src is None:
    print("src error")
    exit()

img = cv.cvtColor(src, cv.COLOR_BGR2GRAY)


def erode_dilate(img):

    ret, src_bin = cv.threshold(
        img, 160, 255, cv.THRESH_BINARY_INV)

    dst1 = cv.erode(src_bin, None)
    dst2 = cv.dilate(src_bin, None)
    dst5 = cv.dilate(dst2, None)
    dst5 = cv.dilate(dst5, None)
    dst5 = cv.dilate(dst5, None)

    global result
    result = 0

    contours, hier = cv.findContours(dst5, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    for pts in contours:
        if cv.contourArea(pts) < 50:
            continue
        approx = cv.approxPolyDP(pts, cv.arcLength(pts, True)*0.03, True)
        vtc = len(approx)

        if vtc == 3:
            setLabel(src_bin, pts, "TRI")
        if vtc == 4:
            setLabel(src_bin, pts, "RECT")
        else:
            lenth = cv.arcLength(pts, True)
            area = cv.contourArea(pts)
            ratio = 4. * math.pi * area / (lenth * lenth)
            if ratio > 0.60:
                # 이부분을 잘라서 원찾기?
                x, y, w, h = cv.boundingRect(pts)
                result += 1

                setLabel(src_bin, pts, "CIR")


erode_dilate(img)
print(result)
