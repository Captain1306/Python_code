import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,0])
z=np.concatenate((x,y))
print(z)
print(np.hstack((x,y))) #along row
print(np.vstack((x,y))) #along column
print(np.dstack((x,y))) #along height
#genraly stack is btter then height
ar1=np.array([[1,2],[3,4]])
ar2=np.array([[5,6],[7,8]])
ar_new=np.concatenate((ar1,ar2),axis=1)
print(ar1)
print(ar2)
print(ar_new)
print(np.hstack((ar1,ar2))) #along row
print(np.vstack((ar1,ar2))) #along column
print(np.dstack((ar1,ar2))) #along height