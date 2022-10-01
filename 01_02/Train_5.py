import numpy as np

nums = np.array([1, 4, 2, 5, 3])

print(nums[1])
print(nums[:3])
print(nums[2:4])
print(nums[::2])

# 슬라이싱 -> 표준 python문법
# 배열명[start:stop]
# 배열명[start:stop:step]
# 값이 지정되지 않은 경우 기본값 사용
