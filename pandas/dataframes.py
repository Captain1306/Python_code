import pandas as pd
l=[10,20,30,40,50,60]
x=pd.DataFrame(l)
print(x)

d={'Ali': [10,20,70,90],'Ahmed':[90,100,40,70],'Ali': [90,100,100,100]}
y=pd.DataFrame(d)
print(y)
z=pd.DataFrame(d,columns=['Ali']) #if you only want to add single column in dataframe
print(z)
