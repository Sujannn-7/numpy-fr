import numpy as np

arr = np.array([10, 20, 30, 40])
new_arr = np.append([50, 60, 70], arr)
print(new_arr)
new_arr1 = np.append(arr, [50, 60, 70])
print(new_arr1)