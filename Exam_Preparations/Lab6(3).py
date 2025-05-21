import numpy as np

a = np.array([[3, 2, 1], [2, 4, 3], [1, 1, 2]])
b = np.array([1, 2, 3])
am = np.linalg.inv(a)
x = np.dot(am, b)
print(f"X = {x[0]:.2f} , Y = {x[1]:.2f} , Z = {x[2]:.2f}")
