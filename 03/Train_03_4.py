import numpy as np
import cv2 as cv


nums = np.array([1, 4, 2, 5, 3])

ref = nums[1:4]
cpy = nums[1:4].copy()

print(ref)
print(cpy)

nums[2] = 10

print(ref)
print(cpy)

# cpy만 별도로 메모리를 할당했기에 원본이 변화해도 적용되지 않는다.
