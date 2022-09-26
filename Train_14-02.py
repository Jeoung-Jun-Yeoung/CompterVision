from re import A
from turtle import right
import numpy as np

x = np.array([1, 2, 3])
y = np.array([3, 2, 1])

print(np.concatenate([x, y]))

# concatenate() 함수는 배열을 연결할 때 사용한다.
# numPy 배열 2개의 연결예제

z = np.array([4, 5, 6])
print(np.concatenate([x, y, z]))

# concatenate() 함수는 배열을 연결할 때 사용하며 순서대로 연결한다.
# 2개 이상의 배열도 연결할 수 있다.

grid = np.array([[1, 2, 3],
                [4, 5, 6]])

print(np.concatenate([grid, grid]))

# 2차원 배열의 연결
# 보통 image를 이어야 할 때 사용한다.

print(np.concatenate([grid, grid], axis=1))

# axis=1을 사용하여 열을 기준으로 연결한다.
# 즉 축을 지정할 수 있다.

# NumPy 배열의 연결 - vstack(), hstack()

# 수직 방향으로 병합

x = np.array([9, 8, 7])
grid = np.array([[1, 2, 3], [4, 5, 6]])
print(np.vstack([x, grid]))

# vstack() 함수는 수직 방향으로 병합한다.

y = np.array([[9], [8]])
print(np.hstack([y, grid]))

# hstack() 함수는 수평 방향으로 병합한다.

# Numpy 배열의 분할

# split(), vsplit(), hsplit()


x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])
print(x1, x2, x3)

# split() 함수는 배열을 분할할 때 사용한다.
# index는 미포함하여 분할한다.
# split(배열명, 분할 지점의 리스트)

grid = np.arange(16).reshape((4, 4))
print(grid)

# 2차원 배열을 분할
# 2차원 배열의 초기화가 포함

upper, lower = np.split(grid, [2])

print(upper)
print(lower)

# 다른 방향으로 분할하고자 할 경우
upper, lower = np.split(grid, [2], axis=1)

print(upper)
print(lower)

# vsplit() 함수는 수직 방향으로 분할한다.

grid = np.arange(16).reshape((4, 4))
upper, lower = np.vsplit(grid, [1])
print(upper)
print(lower)

# axis = 0 이면 가로로 선을 그어서 분할한다.
# axis = 1 이면 세로로 선을 그어서 분할한다.

# hsplit() 함수는 수평 방향으로 분할한다.

grid = np.arange(16).reshape((4, 4))
left, right = np.hsplit(grid, [1])
print(left)
print(right)

# numpy 배열의 연산

arr = [100, 80, 70, 90, 110]

for i in range(len(arr)):
    arr[i] = int(arr[i] - 32) * 5 / 9

print(arr)

# 배열의 연산을 위해서는 반복문을 사용해야 한다.

narr = np.array(arr)
print((narr-32)*5/9)

# numpy 배열은 반복문 없이 연산이 가능하다.
# 각 요소에 접근해서 연산하지 않고 한번에 동일한 영산을 처리한다.
# 1920 size를 단순 for문 연산시에는 200만번이 넘는 연산을 해야한다. 그렇기에 numpy 배열이 효율적이다.

x = np.array(4)
print("x\t=", x)
print("x+5\t=", x+5)
print("x-5\t=", x-5)
print("x*2\t=", x*2)
print("x/2\t=", x/2)

# phtyon의 기본 연산자를 사용하여 numpy 배열의 연산을 할 수 있다.


# 브로드캐스팅

a = np.array([0, 1, 2])
b = np.array([5, 5, 5])

print(a+b)
# 연산 대상인 두 배열들의 차원이 같은 경우 각 요소 단위로 연산을 수행한다.


# broadcasting
# 연산 대상 둘 중 하나가 스칼라 값인 경우 배열로 확장 혹은 복제 후 처리하는 형태

a = np.array([0, 1, 2])
b = 5
print(a+b)

# example

noise = np.eye(4) + 0.01 * np.ones((4,))
print(np.eye(4))
print(np.ones((4,)))
print(noise)

# noise example is broadcasting twice

# 브로드캐스팅 규칙
# 1. 두 배열의 차원수가 다르면 더 작은수의 차원을 가진 배열 형상 앞쪽(왼쪽)을 1로 채운다.
# 2. 두 배열의 형상이 어떤 차원에서도 일치하지 않는다면 해당 차원의 형상이 1인 배열이 다른 형상과 일치하도록 늘어난다.
# 3. 두 배열의 형상이 어떤 차원에서도 일치하지 않는다면 오류가 발생한다.

# 브로드캐스팅이 안되는 경우
# M.shape(3,2) , a.shape(3,) 인 경우. 규칙1이 적용되어 a.shape(1,3)으로 변한다
# 이후 a.shape(1,3)을 다른 형상과 일치하도록 3을 곱해 a.shape(3,3)으로 변한다.
# 그러나 M.shape(3,2)와 a.shape(3,3)은 일치하지 않기에 오류가 발생한다.

# 기타 유니버셜 함수들

a = np.array([0, -1, 2])
print(abs(a))

# numpy 배열의 각 요소에 절대값을 취하는 함수

# 배열의 집계 함수

# 원소 전체의 합계 구하기

grid = np.array([[1, 2, 3], [4, 6, 2]])
print(np.mean(grid))

# mean은 전체 평균, axis 지정시 해당 축 평균을 구한다.

print(np.mean(grid, axis=0))
print(np.mean(grid, axis=1))

# Boolean 배열 numpy 배열에는 산술 연산자 외에 비교 연산자 활용 가능

# when use? 특정 지점을 찾고 싶을때 사용

rng = np.random.RandomState(0)
x = rng.randint(10, size=(3, 4))
print(x)
print(x < 6)

# 비교 연산자를 사용하여 각 요소의 비교 결과를 Boolean 배열로 반환
# True = 1, false = 0으로 해석
# count_zero 함수를 통해 True 숫자 파악가능

print(np.count_nonzero(x < 6))


# 각 행별로 6보다 작은 숫자가 몇개인지 파악
print(np.count_nonzero(x < 6, axis=1))


# 값 중 하나라도 참이 있는지 확인
print(np.any(x > 8))

# 모든 값이 참인지 확인
print(np.all(x < 6, axis=1))

# Boolean 배열을 마스크로 사용

print(x[x < 5])


# 구조화된 Numpy 배열의 생성

# 서로 관련된 이종 데이터를 구조화하여 저장 가능

# step 1 저장할 공간 생성

name = ["Alice", "Bob", "Cathy", "Doug"]

age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]
data = np.zeros(
    4, dtype={'names': ('name', 'age', 'weight'), 'formats': ('U10', 'i4', 'f8')})
print(data)

data['name'] = name
data['age'] = age
data['weight'] = weight

print(data)

print(data[data[data['age'] > 30]['name']]['weight' > 80]['name'])
