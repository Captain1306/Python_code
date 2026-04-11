import pandas as pd
x=[1,2,3,4,5]
a=pd.Series(x)
print(a)
dict={"Name":['python','java','c++'],"ranking":['1','2','3'],"user friendly":[True,False,False]}
b=pd.Series(dict)
print(b)
