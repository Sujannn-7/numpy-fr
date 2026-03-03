import numpy as np

arr = np.array([1, 2, np.inf, 3, np.inf, np.inf, -np.inf])
print(np.isinf(arr))
print(np.isneginf(arr))

cleaned_arr = np.nan_to_num(arr, posinf= 16, neginf= 12)
print("\n", cleaned_arr)