import numpy as np

nums = np.array([1, 4, 2, 5, 3])
# index는 0,1,2,3,4 순서로 0부터 시작합니다.

ref = nums[1:4]
cpy = nums[1:4].copy()

print(ref)
print(cpy)
nums[2] = 10
print(ref)
print(cpy)

# ref는 nums의 1,2,3번째 요소를 참조합니다.
# cpy는 nums의 1,2,3번째 요소를 복사합니다.
# 값 변경시 ref는 nums의 값도 변경되지만 cpy는 nums의 값은 변경되지 않습니다.
# 원본에도 영향을 주고 싶다면 ref를 사용하고 원본에 영향을 주지 않고 싶다면 cpy를 사용합니다.
