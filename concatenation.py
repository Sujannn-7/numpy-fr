import numpy as np

arr = np.array([1, 2, 3])
arr1 = np.array([4, 5, 6])
new_arr = np.concatenate((arr, arr1))
print(new_arr)