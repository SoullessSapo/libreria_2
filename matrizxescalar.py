import numpy as np
import  random

x = np.array([[2 + 3j, 4 + 5j], [4 + 5j, 6 + 7j]])
print("primera matriz es:")
print(x)
y = complex(random.randint(1,10))
print("el escalar es:")
print(y)
z = x*y
print("su producto es:")
print(z)