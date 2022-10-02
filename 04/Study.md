# OpenCv의 주요 기능

카메라와 동영상 파일 다루기
다양한 그리기 함수
이벤트 처리
OpenCv 데이터 파일 입출력
유용한 OpenCv기능

# 카메라와 동영상 파일 다루기

## 동영상의 처리

동영상: 일련의 정지 영상을 압축하여 파일로 저장한 형태. -프레임(Frame): 저장되어 있는 일련의 정지 영상 -> 1장 단위

동영상을 처리하는 작업 순서 -프레임 추출 -각각의 프레임에 영상 처리 기법을 적용

컴퓨터에 연결된 카메라 장치를 사용하는 작업도 카메라로부터 일정 시간 간격으로 정지영상 프레임을 받아와서 처리하는 형태

카메라와 동영상 파일을 다루는 작업은 연속적인 프레임 영상을 받아와서 처리한다는 공통점이 있음.
OpenCv에서는 VideoCapture라는 하나의 클래스를 이용
-> 카메라 또는 동영상 파일로부터 정지영상 프레임을 받아 올 수 있음.

## VideoCapture 클래스

-동영상 파일을 불러오기 위해서 VideoCapture 객체를 생성할때 생성자에 동영상 파일 이름을 지정

python에서는 간단하게 사용이 가능하지만 isOpende()를 통해 제대로 호출이 되었는지 확인은 필요

- cap.get() - 현재 열려 있는 카메라 장치 또는 동영상 파일로부터 여러가지 정보를 받아오기 위해 사용

<pre>
<code>
import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpende():
    print("Camera open Failed!")
    exit()

print("Frame width:",int(cap.get(cv.CAP_PROP_FRAME_WIDTH)))
print("Frame hieight:",int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
</code>
</pre>

filename 인자에는 동영상 파일 이름을 전달

- .avi, .mpg, .mp4 등의 확장자를 갖는 파일
- 현재 실행 폴더에 동영상 파일이 있으면 video.mp4 형태로 파일 이름만 지정하면 됨
- 다른폴더에 동영상 파일이 있다면 절대경로 혹은 상대경로를 추가하여 파일 이름을 지정

<pre>
<code>
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    inversed = ~frame
    cv.imshow("frame", frame)
    cv.imshow("inversed", inversed)

    if cv.waitKey(10) == 27:
        break
    
    cv.destroyAllwindows()
</code>
</pre>

- 사용자로부터 키 입력을 받아서 ESC인 경우 loop를 종료. 27 = ESC
- waitKey(int)

  - 키 입력을 받을때까지 대기할 시간을 지정
  - 이때 원본처럼 보고 싶으면 딜레이 값을 계산해서 넣는다.
  - 10 = 0.001sec

- 반복문 내에서 카메라로부터 프레임을 받아오고 나면, 각 프레임에 다양한 정지 영상 처리 기법을 적용 가능
- 즉, 동영상에도 정지 영상에 대한 기법 적용 가능
- 예제에서 매 프레임에 대하여 영상의 반전을 수행하고, 그 결과를 화면에 출력
- 추후 다양한 영상 처리 기법을 적용하여 사람의 얼굴을 검출하는 등의 작업도 수행가능

<pre>
<code>
print("Frame width:",int(cap.get(cv.CAP_PROP_FRAME_WIDTH)))
print("Frame hieight:",int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
</pre>
</code>

- Get 함수에서는 카메라/동영상의 정보를 받아올 수 있음

## 동영상 파일 처리하기

- 대부분의 동영상 파일은 고유의 코덱을 이용하여 압축된 형태로 저장 됨
- OpenCV는 현재 널리 사용되고 있는 MPEG-4, H.264등의 코덱에 대한 해석 기능을 제공
- VideoCapture 클래스를 활용하여 동영상 파일을 쉽게 불러와서 사용 가능
- OpenCV에서 동영상 파일을 다루는 방법은 앞서 살펴본 카메라 입력 처리와 매우 유사

---

- 동영상 파일이 현재 작업 폴더와 같은 경로에 있을경우 VideoCaputre 생성자에 파일명을 넣어서 초기화

- 동영상 파일의 경우 초당 프레임수 (FPS) 값을 가지고 있음
- FPS값을 고려하지 않을 경우 동영상이 너무 빠르거나 느리게 재생되는 경우가 발생
- OpenCV에서 동영상의 FPS값을 확인하기 위해서는 CAP_PROP_FPS를 활용

<pre>
<code>
fps = cap.get(cv.CAP_PROP_FPS)
print("fps:", fps)
</pre>
</code>

- 동영상 파일의 FPS값을 이용하면 매 프레임 사이의 시간 간격을 계산 가능
- delay = round(1000 / fps)
- example) 초당 30프레임을 재생할 경우 delay는 33ms이며, 각 프레임을 33ms간격으로 출력해야 함
- 위에서 계산한 delay값을 활용하여 추후 waitKey()함수의 인자로 사용

## 동영상 파일 저장하기

- OpenCV는 프레임을 동영상 파일로 저장하는 기능도 제공
- 동영상 파일을 생성하고 프레임을 저장하기 위해서는 VideoWriter 클래스를 사용

- fourcc는 동영상 압축 코덱을 표현하는 4-문자코드
- 각각 코덱, 압축방식, 색상 혹은 픽셀 포맷 등을 정의하는 정수값.
- fourcc()함수를 사용하여 생성 할 수 있음

<pre>
<code>
fourcc = cv.VideoWriter_fourcc(*"DIVX")
</pre>
</code>

<pre>
<code>
outputVideo = cv.VideoWriter("output.avi", fourcc, fps, (w,h))
</pre>
</code>
- 순서대로 저장할 파일의 이름, 픽셀포맷, fps값, 너비,높이
- write() 함수를 사용하여 프레임을 추가할 수 있으나 새로 추가하는 image 프레임의 크기는 동영상 파일을 생성할 때 지정했던 크기와 일치해야 함.
