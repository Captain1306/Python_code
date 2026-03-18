import numpy as np

print("1dimension array")
var= np.array([1,2,3,4])
print(var[2])
print(var[-2])


print("2 dimension arays")
var2=np.array([[1,2,3],[4,5,6]])
print(var2[0,2])
print(var2[1,1])
print(var2[-1,-2])


print("3 dimension array")
var3=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(var3)
print(var3[0,2,1]) #8
print(var3[0,1,0]) #4