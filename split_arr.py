import numpy as np
# ar=np.array([1,2,3,4,5,6])
# sp=np.array_split(ar,3)
# print(sp)
ar2=np.array([[1,2],[3,4],[5,6]])
sp2=np.array_split(ar2,3)
print(sp2)
sp3=np.array_split(ar2,3,axis=1)
print(sp3)