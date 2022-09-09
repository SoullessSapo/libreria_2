import random

import numpy as np

x = complex(random.randint(1,10))
y= complex(random.randint(1,10))
z = complex(random.randint(1,10))
e = complex(random.randint(1,10))
w = complex(random.randint(1,10))
j = complex(random.randint(1,10))

v1= np.array([x,y,z])
v2 = np.array([e, w, j])


s = np.sqrt(np.sum(np.square(v1-v2)))
print("los vectores son:", v1,v2)
print("la distancia entre estos vectores es",s)