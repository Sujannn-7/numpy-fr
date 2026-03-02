import numpy as np

arr_2d = np.array([[1, 2],
                   [3, 4]])

arr_2d_1 = np.array([[4, 5],
                     [6,7]])

new_arr = np.concatenate((arr_2d, arr_2d_1), axis = 0)
print(new_arr)

new_arr1 = np.concatenate((arr_2d, arr_2d_1), axis=1)
print(new_arr1)
