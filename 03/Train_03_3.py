import numpy as np
import cv2 as cv


def func2():
    img1 = np.empty((480, 640), np.uint8)
    img2 = np.zeros((480, 640), np.uint8)
    img3 = np.ones((480, 640), np.uint32)
    img4 = np.full((480, 640), 0, np.uint8)

    mat1 = np.array([[11, 12, 13, 14],
                    [21, 22, 23, 24],
                    [31, 32, 33, 34]]).astype(np.uint8)
    # astype으로 int형으로 만들어 줄 수 있다.

    mat1[0, 1] = 100  # 12번째 원소를 100으로 바꾼다.
    mat1[2, :] = 200  # 3번째 행을 200으로 바꾼다.

    print(mat1)
    print(img1)
    print(img2)
    print(img3)
    print(img4)

    print(type(mat1[0, 0]))
    # astype을 안해주면 int64로 적용된다.


func2()
