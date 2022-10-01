import imp


import numpy as np

nums = np.array([1, 2, 3, 4, 5])

print(nums)
print(nums.ndim)
print(nums.shape)
print(len(nums.shape))
print(nums.size)

# Rank의 개념
# Rank는 차원의 수
# ndim 속성을 통해 확인 가능
# shape는 각 차원의 크기를 튜플로 표현 (모양을 확인할수있음)

# shape
# 배열의 모양
# shape 속성을 통해 확인 가능 -> tuple로 정보 반환

# shape의 응용 -> len()사용을 통해 차원의 수를 산출 가능
