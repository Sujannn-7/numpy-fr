import numpy as np

matrix = np.zeros((3, 3))
print(matrix)

for i in range(3):
    for j in range(3):
        matrix[i][j] = int(input(f"Enter the element at row{i+1} and column {j+1}\n"))



print("User entered matrix:")
print(matrix)