import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5, 6])
reshaped_array = arr_1d.reshape(2, 3)
reshaped_array1 = arr_1d.reshape(3, 2)
reshaped_array2 = arr_1d.reshape(6, 1)
print(reshaped_array)
print(reshaped_array1)
print(reshaped_array2)