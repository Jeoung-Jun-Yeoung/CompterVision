# Numpy 배열의 데이터 타입
# 명시적으로 데이터 타입을 설정하기 위해서는 dtype 인수를 사용한다.

import numpy as np
arr = [1, 4, 2, 5, 3]
n_arr = np.array(arr, dtype=np.float32)
print(arr)
print(type(arr))
print(n_arr)
print(type(n_arr))


# numpy에 저장되는 결과를 내가 원하는 데이터 타입으로 바꿀 수 있다.
# arr = ["3.14", 4, 2, 5, 3]
# 해당 배열을 ndarray로 변환했다면 문자열로 바뀌었겠지만 dtype을 사용하면 해당 타입으로 캐스팅된다.
# 무조건 상위타입으로 사용하는것이 좋은것 아니다. 왜냐하면 float32를 쓰다 float64를 쓰면 저장공간을 2배로 쓰는것이기 때문.
# 다를 데이터의 최소치의 타입으로 사용하는것을 권장.
