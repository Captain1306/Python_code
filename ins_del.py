import numpy as np
y=np.array([1,2,3,4,5])
y2=np.array([[10,20],[30,40],[50,60]])
x2=np.insert(y2,1,1000,axis=1)
print(x2)
x=np.insert(y,4,100)
#delete program
print(x)
z=np.delete(y,1)
print(z)
z1=np.delete(y2,1)
print(z1)
