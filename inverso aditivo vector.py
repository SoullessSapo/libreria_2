import numpy as np
import random
import cmath

x = complex(random.randint(1,10))
y= complex(random.randint(1,10))
z = complex(random.randint(1,10))
v1= np.array([x,y,z])
v2 = v1*-1

s = v1 + v2
print( "el vector inicial es:", v1)
print("el inverso aditivo es:", v2)