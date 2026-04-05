import numpy as np
var=np.array=([1,2,3,4,5])
y=np.resize(var,(2,3)) #(2,3) it means 2 rows and 3 data in each
print(y)
#now converting two dimension into one dimension
print(y.flatten()) #you can change order by flatten(order='K') or 'C' 'F' 'A' 'K'
print(y.ravel()) #both flatten and revel do tha same job
