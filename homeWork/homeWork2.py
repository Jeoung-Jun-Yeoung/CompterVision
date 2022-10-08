import numpy as np
import cv2 as cv

# 1.sample.jpg 회색조로 열기
# 2.img 평균 밝기를 기준으로 명암비 조절 결과를 constrast.jpg로 저장하기
# 3.결과 저장시 saturation 연산을 적용

src = cv.imread('homeWork/sample-2.jpeg', cv.IMREAD_GRAYSCALE)

if src is None:
    print("Image load failed!")

averageBrightness = np.mean(src)  # 평균밝기

alpha = 2.0

src = cv.convertScaleAbs(src, alpha=1+alpha,
                         beta=-averageBrightness * alpha)

cv.imwrite('homeWork/constrast.jpg', src)
cv.waitKey()
cv.destroyAllWindows()
