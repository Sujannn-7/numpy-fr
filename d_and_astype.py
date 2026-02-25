import numpy as np

arr = np.array(["Sujan", "Adhikari", 3, 4])
print(arr.dtype)
l =np.array(["1", "2", "3", "4", "5"])
print(l.dtype)
l = l.astype(int)
print(l)
print(l.dtype)