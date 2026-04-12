import pandas as pd
# var1=pd.read_csv("D:\\Programming\\test_Book1.csv")
# print(var1)
# to get data till specific point
# var2=pd.read_csv("D:\\Programming\\test_Book1.csv",nrows=11)
# print(var2)
# if you want specific columns
# var3=pd.read_csv("D:\\Programming\\test_Book1.csv",usecols=["Region","Rep","Item"]) #you can also use[0,1] for column
# print(var3)
#you can also skip rows
var4=pd.read_csv("D:\\Programming\\test_Book1.csv",skiprows=[3])
print(var4)
