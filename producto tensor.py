import numpy as np

x = np.array([[2 + 3j, 4 + 5j], [4 + 5j, 6 + 7j]])
print("Primera matriz:")
print(x)

y = np.array([[8 + 7j, 5 + 6j], [9 + 10j, 1 + 2j]])
print("segunda matriz:")
print(y)

z = np.tensordot(x, y)
print("su producto tensor es:")
print(z)