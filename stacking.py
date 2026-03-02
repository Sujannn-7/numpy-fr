import numpy as np

arr = np.array([1, 2, 3])
arr1 = np.array([4, 5, 6])

print(np.vstack((arr, arr1)), "\n")
print(np.hstack((arr, arr1)))