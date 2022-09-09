import numpy as np
import random
import cmath
x = complex(random.randint(1,10))
y= complex(random.randint(1,10))
z = complex(random.randint(1,10))
e = complex(random.randint(1,10))

v1= np.array([x,y,z])

s = v1 *e
print("el vector es:", v1, "el escalar es:", s)
print("el resultado del prodcuto es",s)