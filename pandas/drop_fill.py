import pandas as pd
var1=pd.read_csv("D:\\Programming\\test_sub.csv")
print(var1)
print(var1.dropna())
print(var1.dropna(inplace=True))
print(var1.dropna(thresh=1))
print(var1.fillna("python"))