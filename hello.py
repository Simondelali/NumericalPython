import numpy as np

arr = np.array((1, 2, 3, 4, 5))

print(arr)
print(type(arr))

# 0-D Arrays
arr = np.array(42)
print(arr)

# 1-D Arrays
arr = np.array((1, 2, 3, 4, 5))
print(arr)

# 2-D Arrays
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr.ndim)

# 3-D Arrays
arr = np.array([[[1,2,3],[4,5,6]], [[1,2,3,],[4,5,6]]])
print(arr)
print(arr.ndim)