import pandas as pd
var1=pd.read_csv("D:\\Programming\\test_Book1.csv")
var1.loc[0,"NaN"]="Python"
print(var1.head(2))
print(var1.loc[[1,2],["Region","Rep"]])