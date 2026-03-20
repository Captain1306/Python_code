import numpy as np

x=np.array([1,2,3,4])
for i in x:
    print(i)

# #Two dimension array
y=np.array([[1,2,3,4],[5,6,7,8]])
for i in y:
    print(y)

for i in y:
    for k in i:
        print(k)

# 3 dimension array
print("By manual process")
z=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
for i in z:
    for j in i:
        for k in j:
            print(k)
print("using function")
z=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
for i in np.nditer(z):
    print(i)
for i,d in np.ndenumerate(z):
    print(i,d)