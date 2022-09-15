import numpy as np


nums = np.array([[1, 4, 2], [7, 5, 3]])

print(nums)
print(nums[0:1, ])
print(nums[0:1, :])
print(nums[:, 1:2])
print(nums[1, 1:])
print(nums[0:, 1:])
