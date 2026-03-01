import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5, 6])
print(arr_1d)
new_arr = np.insert(arr_1d, 6, 9, axis=0)
print(new_arr)
new_arr = np.insert(arr_1d, [5, 6], [7, 8], axis=0)
print(new_arr)