import numpy as np

# numpy 내장함수를 사용한 배열 생성

# 기본
print(np.zeros((2, 2)))
print(np.ones((1, 2)))
print(np.full((2, 2), 7))

# zeros는 0으로 채워진 numpy 배열을 생성합니다.
# ones는 1로 채워진 numpy 배열을 생성합니다.
# full은 지정한 값으로 채워진 numpy 배열을 생성합니다.

# zeors는 2x2 numpy 배열을 생성합니다. 이때 값은 0
# ones는 1x2 numpy 배열을 생성합니다. 이때 값은 1
# full은 2x2 numpy 배열을 생성합니다. 이때 값은 7


# numpy 내장함수를 사용한 단위행렬 생성

print(np.eye(3))
print(np.eye(3, k=1))
print(np.eye(3, k=-2))

print(np.identity(3))

# eye는 대각선이 1인 numpy 단위행렬을 생성합니다.
# eye는 k값에 따라 이동하게 됩니다.
# identity는 eye와 같은 기능을 합니다. 이때 숫자에 따른 단위행렬을 생성합니다.


# 랜덤생성

print(np.random.random((2, 2)))

# random은 0~1 사이의 랜덤값을 생성합니다.
# random은 2x2 numpy 배열을 생성합니다.
# random.normal(shape) -> 정규분포를 따르는 난수
# random.randint(low, high, shape) -> low~high 사이의 정수 난수 (high는 포함하지 않음)

print(np.linspace(0, 1, num=5, endpoint=True))
print(np.linspace(0, 1, num=5, endpoint=False))
print(np.linspace(0, 1, num=5, endpoint=False, retstep=True))

# linspace는 시작과 끝을 포함하여 균등하게 나눈 numpy 배열을 생성합니다.
# linspace는 0~1 사이의 num개의 숫자를 생성합니다.
# endpoint는 끝을 포함할지 여부를 결정합니다. 기본값은 True입니다. True면 끝을 포함합니다.
# retstep은 간격을 반환할지 여부를 결정합니다. True면 간격을 반환합니다.

print(np.arange(0.4, 1.1, 0.1))

# arange는 시작과 끝을 포함하지 않고 균등하게 나눈 numpy 배열을 생성합니다.
# arange는 0.4~1.1 사이의 0.1 간격의 숫자를 생성합니다.
# arange는 끝을 포함하지 않습니다.
# dtype을 지정할 수 있습니다.
# dtype을 지정하지 않으면 float64로 지정됩니다.
# dtype을 지정하면 지정한 타입으로 지정됩니다.
