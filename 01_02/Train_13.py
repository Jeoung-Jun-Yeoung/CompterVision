import numpy as np

sap = np.array(["MMM", "ABT", "ABBV", "ACN", "ACE", "ATVI", "ADBE", "ADT"])
print(sap)
sap2d = sap.reshape(2, 4)
print(sap2d)

# numpy 배열의 형태 변형

# reshape() 함수를 사용하여 배열의 형태를 변형할 수 있다.
# 기존 배열과 새로운 배열의 요소 개수는 같아야 한다.

# 전치
# Transpose
# 배열의 행과 열을 바꾸는 것을 전치라고 한다.

print(sap2d.T)

# 함수호출이 아닌 속성 T를 사용하여 전치할 수 있다.
# (2,4) -> (4,2)로 변형된다.
# 축을 바꾸어 처리하는 과정


print(sap2d.swapaxes(0, 1))


# 축1과 축2를 서로 맞바꾼다.
# swapaxes() 함수를 사용하여 축을 바꿀 수 있다.
# swqpaxes(0,1)은 sap2d.T와 같다.

print("=======================================")
print("\n")
sap3d = sap.reshape(2, 2, 2)
print("=======================================")
print("\n")
print(sap3d, '\n')
print("=======================================")
print("\n")
print(sap3d.swapaxes(1, 2))
# 3차원 배열에서의 swapaxes()
# 3차원 배열에서는 축을 3개 사용할 수 있다.
# 이미지 순서는 유지하면서 각 이미지가 Transpose되는 경우에 사용할 수 있다.

print(sap2d.swapaxes(0, 1))
print(sap2d.transpose(1, 0))
print(sap2d.transpose(0, 1))
