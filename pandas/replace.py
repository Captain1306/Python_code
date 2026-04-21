import pandas as pd
var1=pd.read_csv("D:\\Programming\\test_Book1.csv")
print(var1.replace(to_replace=1.29,value=22))
print(var1.replace(to_replace="Binder",value="sheri"))

