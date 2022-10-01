import numpy as np

mat1 = np.zeros((3, 3), dtype=np.uint8)
mat2 = np.ones((3, 3), dtype=np.uint8)
mat3 = np.identity(3, dtype=np.uint8)

print(mat1)
print(mat2)
print(mat3)

# dtype으로 int형으로 만들어 줄 수 있다.
