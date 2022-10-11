import numpy as np
import cv2 as cv
import time


# 3. 웹캠을 사용하여 회색조(grayscale)로 동영상을 저장하되,
# 카메라로부터 들어오는 현재 프레임이 직전 프레임보다 이미지 전체의 평균 밝기가 30 넘게 바뀔 경우,
# 그 시점부터 다음 3초간 반전시켜서 output.avi로 저장해주세요.

fourcc = cv.VideoWriter_fourcc(*'MJPG')

# 동영상 저장을 위한 코덱 생성


cap = cv.VideoCapture('computervison_video.mp4')

# web캠 가져오기

width = round(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# 너비,높이 구하기

# 한번 체크해보자.

if not cap.isOpened():
    print("Camera open failed!")
    exit()

# 캠이 제대로 열렸는지 확인

fps = cap.get(cv.CAP_PROP_FPS)
# 한 프레임당 시간을 구하기 위해 fps를 구한다.
# 프레임은 초당 몇장의 사진을 찍는지를 의미한다.

delay = round(1000 / fps)

# 1000으로 나누는 이유는 ms단위로 바꾸기 위해서이다.

# 저장할 비디오 만들기
outputVideo = cv.VideoWriter(
    "output.avi", fourcc, fps, (width, height),0)

if not outputVideo.isOpened():
    print("File open failed!")
    exit()

flag = True

beforeBrightnessAvgFrame = 0

while True:
    ret, frame = cap.read()


    if not ret:
        print("Frame read failed!")
        exit()

    BrightnessAvgFrame = np.mean(frame)
    # 평균 밝기 한번 찍어보기
    print("BrightnessAvgFrame : ", BrightnessAvgFrame)

    if flag:
        # flag가 True일때는 그냥 저장. 최초 1회 처리
        beforeBrightnessAvgFrame = BrightnessAvgFrame
        flag = False

    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # 현재 프레임이 직전 프레임보다 이미지 전체의 평균 밝기가 30 넘게 바뀔 경우
    if abs(BrightnessAvgFrame - beforeBrightnessAvgFrame) >= 30:
        print("30 차이 발생")
        sec = 0
        # 3초간 반전시켜서 output.avi로 저장해주세요.
        start = int(time.time())
        print("start : ", start)
        while True:
            ret, frame = cap.read()

            if not ret:
                break
            frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            inversed = ~frame

            outputVideo.write(inversed)
            cv.imshow('frame', frame)

            if cv.waitKey(delay) == 27:
                break
            end = int(time.time())
            if end - start > 3:
                print("end : ", end)
                print("rst : ", end - start)
                break
            # grayscale 변환..

    else:
        outputVideo.write(frame)
        cv.imshow('frame', frame)

    if cv.waitKey(delay) == 27:
        break

    beforeBrightnessAvgFrame = BrightnessAvgFrame

print("good end")
cv.destroyAllWindows()
