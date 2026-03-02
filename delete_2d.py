import numpy as np

arr_2d = np.array([[1, 2],
                   [3, 4], 
                   [5, 6]])

new_arr = np.delete(arr_2d, 2)
print(new_arr)

new_arr1 = np.delete(arr_2d, 2, axis=0)
print(new_arr1)

new_arr2 = np.delete(arr_2d, 1, axis=1)
print(new_arr2)