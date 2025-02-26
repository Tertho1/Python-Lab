import numpy as np

A = np.array([
    [3, 2, 1],
    [2, 4, 3],
    [1, 1, 2]
])

B = np.array([1, 2, 3])

A_inv = np.linalg.inv(A)

Y = np.dot(A_inv, B)

X = np.linalg.solve(A, B)

print("Solution for X (x, y, z):", X)

print("Solution for Y (x, y, z):", Y)
