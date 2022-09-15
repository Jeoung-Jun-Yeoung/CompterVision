import numpy as np

print(np.__version__)

arr = [3.14, 2, 5, 3]
arr2 = ["3.14", 2., 5, 3]
# 실수를 넣으면 어떻게 될까?
n_arr = np.array(arr)
n_arr2 = np.array(arr2)

print(arr)
print(type(arr))
print(n_arr)
print(type(n_arr))
print(arr2)
print(n_arr2)
print(type(n_arr2))


# Output: arr은 실수형으로 변환되어 출력됨. n_arr2는 내부 요소가 String으로 바뀌어 표현됌
