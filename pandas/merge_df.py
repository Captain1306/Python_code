import pandas as pd
# l1={"A":[1,2,3,4,5],
#     "B":[6,7,8,9,10]}
# l2={"A":[1,2,3,4,5],
#     "C":[11,12,13,14,15]}
# var1=pd.DataFrame(l1)
# var2=pd.DataFrame(l2)
# var3=pd.merge(var1,var2,on="A")
# print(var3)
R1={"X":[1,2,3,4,5],
    "Y":[6,7,8,9,10]}
R2={"X":[1,2,3,4,5],
    "Y":[11,12,13,14,15]}
da=pd.DataFrame(R1)
db=pd.DataFrame(R2)
dc=pd.merge(da,db,left_index=True,right_index=True)
print(dc)

