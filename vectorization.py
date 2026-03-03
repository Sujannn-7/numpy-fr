# # Using loop:

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# result = [x+y for x, y in zip(list1, list2)]
# print(result)

#Using Numpy

import numpy as np

arr1 = np.array(list1)
arr2 = np.array(list2)

result = arr1 + arr2
print(result)


