import numpy as np

x = np.matrix([[2 + 3j, 4 + 5j], [4 + 5j, 6 + 7j]])
print("primera matriz es:")
print(x)

z = x.getH()
print("su inversa es:")
print(z)