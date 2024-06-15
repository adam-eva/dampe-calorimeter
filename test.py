import numpy as np

X1 = np.array([[1, 2], [3, 4], [5, 6]])
X2 = np.array([[7, 8, 9], [10, 11, 12], [13, 14, 15]])

X_combined = np.hstack((X1, X2))

print(X1)
print(X2)
print(X_combined)
