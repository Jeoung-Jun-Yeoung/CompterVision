import numpy as np

nums = np.array([[1, 4, 2], [7, 5, 3]])

print(nums[1, 1])
print(nums[1, 0:2])
print(nums[:2, 2:])
print(nums[0:3, :2])
