import pandas as pd
l1={"A":[1,2,3,4,5],
    "B":[6,7,8,9,10]}
l2={"A":[1,2,3,4,5],
    "C":[11,12,13,14,15]}
var1=pd.DataFrame(l1)
var2=pd.DataFrame(l2)
var3=pd.merge(var1,var2,on="A")
print(var3)
