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

    cv.imshow('test', ~img_tr)
    cv.waitKey()
    hough_circles(~img_tr)

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

    bgr_place = cv.split(src)

    noise = np.zeros(dst2.shape, np.int32)
    cv.randn(noise, 0, 5)
    cv.add(dst2, noise, dst2, dtype=cv.CV_8UC1)

    dst3 = cv.GaussianBlur(dst2, (0, 0), 5)
    # dst1 = cv.bilateralFilter(gray, -1, 10, 5)

    ret, dst4 = cv.threshold(dst3, 100, 255, cv.THRESH_BINARY)

    # cv.imshow('src', src)
    # cv.imshow('dst', dst)
    # cv.imshow('dst2', dst2)
    # cv.imshow('dst3', dst3)
    # cv.imshow('dst4', dst4)
    # cv.imshow('B', bgr_place[0])
    # cv.imshow('G', bgr_place[1])
    # cv.imshow('R', bgr_place[2])
    temp = cv.merge((bgr_place[1], bgr_place[0], bgr_place[2]))
    temp1 = cv.merge((bgr_place[2], bgr_place[0], bgr_place[1]))
    temp2 = cv.merge((bgr_place[0], bgr_place[2], bgr_place[1]))
    # cv.imshow('B + G', temp)
    # cv.imshow('B + G1', temp1)
    # cv.imshow('B + G2', temp2)

    ret, bdst = cv.threshold(bgr_place[0], 127, 255, cv.THRESH_BINARY)
    ret, gdst = cv.threshold(bgr_place[1], 150, 255, cv.THRESH_BINARY)
    ret, rdst = cv.threshold(bgr_place[2], 10, 255, cv.THRESH_BINARY)
    ret, test = cv.threshold(temp, 120, 255, cv.THRESH_BINARY)
    tet = cv.cvtColor(test, cv.COLOR_BGR2GRAY)

    # cv.imshow('bdst', bdst)
    # cv.imshow('gdst', gdst)
    # cv.imshow('rdst', rdst)
    # cv.imshow('test2', test)
    # cv.imshow('test1', tet)

    # cv.waitKey()
    # cv.destroyAllWindows()
    return tet


# rst.sort()
# rst.reverse()
# for i in rst:
#     print(f"{i}")
img = color_split()

cv.destroyAllWindows()
contours_basic(img)
exit()
# hough_circles()

# img = cv.imread(
#     "/Users/jeongjun-yeong/GitHub/CompterVision/homeWork2/case1.png", cv.IMREAD_GRAYSCALE)


# if img is None:
#     print("error")

# cv.imshow('img', img)
