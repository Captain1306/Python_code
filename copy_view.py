import numpy as np
var=np.array([1,2,3,4])
co=var.copy()
print("Orignal: ",var)
print("Copy: ",co)
var2=np.array([6,7,8,9,0])
v=var2.view()
print("variable: ",var2)
print("viewed: ",v)
#the main diff between them is copy func copy the data in new array but view func represent the orignal data change in view will represent the change in orignal
co[1]=40
v[1]=40
print(co)
print(v)