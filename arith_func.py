import numpy as np

var = np.array([1,2,3,4,5])
print("minimum is: ",np.min(var)," and index is: ",np.argmin(var))

print("maximum is: ",np.max(var)," and index is: ",np.argmax(var))

print(np.sin(var))
print(np.cos(var))

print(np.cumsum(var)) #it is used to calculate the accumylative frequecy

var2=np.array([[1,2,3,4],[1,2,3,4]])
print(var2)
print()
print(var2.shape)

#Reshaping array
x=np.array([1,2,3,4,5,6])
y=x.reshape(3,2)
print(y)
print(y.shape)