import numpy as np
import cv2 as cv

img = np.full((200, 640, 3), 255, np.uint8)

text = "Hello, OPENCV"

fontFace = cv.FONT_HERSHEY_TRIPLEX

fontScale = 2.0

thickness = 1

sizeText, _ = cv.getTextSize(text, fontFace, fontScale, thickness)

org = ((img.shape[1] - sizeText[0]) // 2, (img.shape[0] + sizeText[1]) // 2)

cv.putText(img, text, org, fontFace, fontScale, (255, 0, 0), thickness)

cv.rectangle(img, org, (org[0] + sizeText[0],
             org[1] - sizeText[1]), (0, 0, 255), 1)

cv.imshow("img", img)

cv.waitKey()
cv.destroyAllWindows()
