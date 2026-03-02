import numpy as np

arr_2d = np.array([[1, 2], 
                   [3, 4]])
new_arr = np.append(arr_2d, [[5, 6]], axis=0)
print(new_arr)
new_arr1 = np.append(arr_2d, [[5], [6]], axis=1)
print(new_arr1)