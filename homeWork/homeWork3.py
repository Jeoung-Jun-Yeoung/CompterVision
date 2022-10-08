from turtle import width
import numpy as np
import cv2 as cv


# 3. 웹캠을 사용하여 회색조(grayscale)로 동영상을 저장하되,
# 카메라로부터 들어오는 현재 프레임이 직전 프레임보다 이미지 전체의 평균 밝기가 30 넘게 바뀔 경우,
# 그 시점부터 다음 3초간 반전시켜서 output.avi로 저장해주세요.

fourcc = cv.VideoWriter_fourcc(*'XVID')


cap = cv.VideoCapture(0)

width = round(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))


if not cap.isOpened():
    print("Camera open failed!")
    exit()

fps = cap.get(cv.CAP_PROP_FPS)
delay = round(1000/fps)

outputVideo = cv.VideoWriter(
    "output.avi", fourcc, fps, (width, height), isColor=None)

if not outputVideo.isOpened():
    print("File open failed!")
    exit()

avgFrame = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    outputVideo.write(frame)
    # 현재 프레임이 직전 프레임보다 이미지 전체의 평균 밝기가 30 넘게 바뀔 경우
    if np.mean(frame) >= avgFrame + 30 or np.mean(frame) >= avgFrame - 30:
        # 3초간 저장
        for i in range(int(fps * 3)):
            outputVideo.write(~frame)

    if cv.waitKey(delay) == 27:
        break
    avgFrame = np.mean(frame)
    cv.imshow('frame', frame)

cv.destroyAllWindows()
