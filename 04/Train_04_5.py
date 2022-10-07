import numpy as np
import cv2 as cv

img = np.full((400, 400, 3), 255, np.uint8)

cv.line(img, (50, 50), (200, 50), (0, 0, 255))
cv.line(img, (50, 100), (200, 100), (255, 0, 255), 3)
cv.line(img, (50, 150), (200, 150), (255, 0, 0), 50)

# 끝 인자를 조절하면 두꺼워 진다.

cv.line(img, (250, 50), (350, 100), (0, 0, 255), 1, cv.LINE_4)
cv.line(img, (250, 70), (350, 120), (255, 0, 255), 1, cv.LINE_8)
cv.line(img, (250, 90), (350, 140), (255, 0, 0), 1, cv.LINE_AA)

cv.arrowedLine(img, (50, 200), (150, 200), (0, 0, 255), 1)
cv.arrowedLine(img, (50, 250), (350, 250), (255, 0, 255), 1)
cv.arrowedLine(img, (50, 300), (350, 300), (255, 0, 0), 1, cv.LINE_8, 0, 0.05)

cv.drawMarker(img, (50, 350), (0, 0, 255), cv.MARKER_CROSS)
cv.drawMarker(img, (100, 350), (0, 0, 255), cv.MARKER_TILTED_CROSS)
cv.drawMarker(img, (150, 350), (0, 0, 255), cv.MARKER_STAR)
cv.drawMarker(img, (200, 350), (0, 0, 255), cv.MARKER_DIAMOND)
cv.drawMarker(img, (250, 350), (0, 0, 255), cv.MARKER_SQUARE)
cv.drawMarker(img, (300, 350), (0, 0, 255), cv.MARKER_TRIANGLE_UP)
cv.drawMarker(img, (350, 350), (0, 0, 255), cv.MARKER_TRIANGLE_DOWN)


cv.imshow("img", img)
cv.waitKey()
cv.destroyAllWindows()
