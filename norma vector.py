import numpy as np
import random
import cmath
x = complex(random.randint(1,10))
y= complex(random.randint(1,10))
z = complex(random.randint(1,10))
e = complex(random.randint(1,10))

v1= np.array([x,y,z])

s = np.linalg.norm(v1)
print("el vector es:", v1)
print("la norma del vector es",s)