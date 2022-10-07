import numpy as np
import cv2 as cv

img = np.full((500, 800, 3), 255, np.uint8)

cv.putText(img, "FONT_HERSHEY_SIMPLEX", (20, 50),
           cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))

cv.putText(img, "FONT_HERSHEY_PLAIN", (20, 100),
           cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))

cv.putText(img, "FONT_HERSHEY_DUPLEX", (20, 150),
           cv.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))

cv.putText(img, "FONT_HERSHEY_COMPLEX", (20, 200),
           cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))

cv.putText(img, "FONT_HERSHEY_TRIPLEX", (20, 250),
           cv.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255))

cv.putText(img, "FONT_HERSHEY_COMPLEX_SMALL", (20, 300),
           cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255))

cv.putText(img, "FONT_HERSHEY_SCRIPT_SIMPLEX", (20, 350),
           cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255, 0, 255))

cv.putText(img, "FONT_HERSHEY_SCRIPT_COMPLEX", (20, 400),
           cv.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 255))

cv.putText(img, "FONT_HERSHEY_SCRIPT_COMPLEX | FOMT_ITALITC", (20, 400),
           cv.FONT_HERSHEY_SCRIPT_COMPLEX | cv.FONT_ITALIC, 1, (255, 0, 0))


cv.imshow("img", img)
cv.waitKey()
cv.destroyAllWindows()
