import numpy as np
var=np.array([1,2,3,4])
co=var.copy()
print("Orignal: ",var)
print("Copy: ",co)
var2=np.array([6,7,8,9,0])
v=var2.view()
print(v)