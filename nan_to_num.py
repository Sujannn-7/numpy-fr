import numpy as np

arr = np.array([1, 2, np.nan, 4, np.nan, 6, np.nan])

cleaned_arr = np.nan_to_num(arr, nan = 34)
print(cleaned_arr)