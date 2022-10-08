import numpy as np
import cv2 as cv

# 1. sample.jpg 회색조로 열기
# 2. img의 평균밝기 보다 어두운 픽셀들을 0으로 바꾸기
# 3. output.jpg로 저장하기

src = cv.imread('homeWork/sample.jpeg', cv.IMREAD_GRAYSCALE)

if src is None:
    print("Image load failed!")

dst = np.empty(src.shape, src.dtype)

for y in range(src.shape[0]):
    for x in range(src.shape[1]):
        if src[y, x] < np.mean(src):
            dst[y, x] = 0
        else:
            dst[y, x] = src[y, x]

# img load error 탐지

cv.imshow('src', src)
# cv.imshow('dst', dst)
cv.waitKey()
cv.destroyAllWindows()
