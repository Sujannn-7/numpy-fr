import numpy as np

arr_1d = np.array([1, 2])
arr_2d = np.array([[1, 2], [2, 3], [3,4]])
arr_3d = np.array([[[1, 2], [2, 3], [3, 4], [5, 6]]])
arr = np.array(["Sujan", "Adhikari", 3, 4])

print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)
print(arr_3d.dtype)
print(arr.dtype)