import numpy as np
import cv2 as cv


def func4():
    img1 = cv.imread("./CVImages/lenna.bmp", cv.IMREAD_GRAYSCALE)

    img2 = img1[200:400, 200:400]
    img3 = img1[200:400, 200:400].copy()

    img2 += 20  # img2의 값이 바뀌면 img1의 값도 바뀐다. 20을 더하는건 밝기 올리기

    cv.imshow("img1", img1)
    cv.imshow("img2", img2)
    cv.imshow("img3", img3)
    cv.waitKey()
    cv.destroyAllWindows()


func4()

# 200:400 이 밝아진것을 확인 할 수 있다.
