import numpy as np

l = []

for i in range(5):
    num=int(input("Enter an integer number: "))
    l.append(num)

y=l

print(np.array(y))
print(y.ndim)

y=np.array([1,2,3,4])
print(y)
print(y.ndim)

arr2=np.array([[1,2,3,4],[5,6,7,8]])
print(arr2)
print(arr2.ndim)

arr3=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
print(arr3)
print(arr3.ndim)
