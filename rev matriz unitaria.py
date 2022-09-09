import numpy as np

x = np.array([[2 + 3j, 4 + 5j], [4 + 5j, 6 + 7j]])
print("primera matriz es:")
print(x)

z = np.linalg.inv(x)

print("su inversa es:")
print(z)
w = np.linalg.inv(x)
print( "su determinante es")
print(w)
print("su adjunta es")
print(w*z)
l= w*z
q= np.array([[1,0],[0,1]])
if x*l == q:
    print("la matriz es unitaria")
else:
    print(" la matriz no es unitaria")