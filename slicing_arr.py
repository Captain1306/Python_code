import numpy as np

var = np.array([1,2,3,4,5,6,7,8])
print("Slicing", var[1:6])
print("Slicing", var[1:])
print("Slicing", var[:6])

print("Slicing 2 dimension array")
var2 = np.array([[1,2,3,4],[5,6,7,8]])
print(var2[1,0:3]) #5 6 7

print("Slicing array 3 dimension")
var3 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
print(var3[0,2,0:3]) #9 10 11 