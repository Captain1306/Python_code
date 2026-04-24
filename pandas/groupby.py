import pandas as pd
var=pd.DataFrame({"Name": ["a","b","c","d","b","a","b","c"],
                    "S1": [10,30,40,70,29,69,43,12],
                    "S2": [30,29,45,38,58,29,56,84]})
var2=var.groupby("Name")
# print(var2)
# for  x,y in var2:
#     print(x)
#     print(y)
#     print()
# print(var2.get_group("c"))
print(var2.max())
print(var2.min())