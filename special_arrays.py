import numpy as np
arr1=np.zeros(4)
arr2=np.zeros((3,4))
print(arr1)
print()
print(arr2)

arr_one=np.ones(4)
arr_one2=np.ones((3,4))
print(arr_one)
print()
print(arr_one2)

emp_arr=np.empty(4)
print(emp_arr)

ran_arr=np.arange(6)
print(ran_arr)

iden=np.eye(3)
print(iden)

arr_ls=np.linspace(0,20,5)
print(arr_ls)

y=np.array([1,2,3,4,5])
x=y.astype(float)
print(y)
print(type(y))
print(x)
print(type(x))
