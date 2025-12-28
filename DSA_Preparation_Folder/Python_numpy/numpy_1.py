
import numpy as np 
from numpy import random
a= np.random.randint(15, size=(3,5))
print(a.mean)
print(a.shape)
print(a.ndim)
print(a.dtype)
print(a.size)
print(type(a))     

for i in range(len(dir(np))):
    print(dir(np)[i])