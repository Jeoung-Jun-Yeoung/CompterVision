import numpy as np
import cv2 as cv


def func1():
    img1 = cv.imread("./CVImages/cat.bmp", cv.IMREAD_GRAYSCALE)
    if img1 is None:
        print("Imgaes load failed!")
        return

    print("type(img1) = ", type(img1))
    print("img1.shape = ", img1.shape)

    if len(img1.shape) == 2:
        print("img1 is a grayscale image")
    elif len(img1.shape) == 3:
        print("img1 is a truecolor image")

    cv.imshow("img1", img1)
    cv.waitKey()
    cv.destroyAllWindows()


func1()


# 이미지 타입 확인하기 및 로드하기
# cat.bmp 로드하기 -> 흑백으로
# img1의 타입? -> numpy.ndarray
# img1의 shape -> (480, 640)
# shape의 길이로 타입을 확인 할 수 있다.
