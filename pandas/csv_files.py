import pandas as pd
data1={"Employee":['ALi','Jhon','Peter','Ahmed'],
       "Language":['Python','Java','C++','Js'],
       "Experiance":[10,12,8,9]}
var1=pd.DataFrame(data1)
print(var1)
var1.to_csv("test_new.csv",index=False)
