import numpy as np
import cv2 as cv


# def sobel_derivative(img):
#     mx = np.array([[-1, 0, 1],
#                   [-2, 0, 2],
#                   [-1, 0, 1]], dtype=np.float32)
#     my = np.array([[-1, -2, -1],
#                    [0, 0, 0],
#                    [1, 2, 1]], dtype=np.float32)

#     dx = cv.filter2D(img, -1, mx, delta=128)
#     dx = cv.filter2D(img, -1, my, delta=128)
#     cv.imshow('soble-img', img)
#     cv.imshow('mx', mx)
#     cv.imshow('my', my)


# def sobel_edge(img):
#     dx = cv.Sobel(img, cv.CV_32F, 1, 0)
#     dy = cv.Sobel(img, cv.CV_32F, 0, 1)

#     fmag = cv.magnitude(dx, dy)

#     mag = np.uint8(np.clip(fmag, 0, 255))
#     _, edge = cv.threshold(mag, 150, 255, cv.THRESH_BINARY)  # type: ignore

#     cv.imshow("mag", mag)
#     cv.imshow('edge', edge)


# sobel_derivative(img)
# sobel_edge(img)


def hough_circles():
    img = cv.imread(
        "/Users/jeongjun-yeong/GitHub/CompterVision/homeWork2/case2.jpg", cv.IMREAD_GRAYSCALE)

    if img is None:
        print("error")

    img = cv.medianBlur(img, 5)
    cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

    circles = cv.HoughCircles(img,
                              cv.HOUGH_GRADIENT, 1, 20, param1=250, param2=30, minRadius=10, maxRadius=50)

    circles = np.uint16(np.around(circles))

    print(len(circles[0]))

    for i in circles[0, :]:
        cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)

    cv.imshow('img', img)
    cv.imshow('c2', cimg)
    cv.waitKey()
    cv.destroyAllWindows()


hough_circles()
# img = cv.imread(
#     "/Users/jeongjun-yeong/GitHub/CompterVision/homeWork2/case1.png", cv.IMREAD_GRAYSCALE)


# if img is None:
#     print("error")

# cv.imshow('img', img)

cv.waitKey()
cv.destroyAllWindows()
