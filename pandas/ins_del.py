import pandas as pd
var1=pd.DataFrame({"A": [1,2,3,4,5],"B": [6,7,8,9,10]})
var1.insert(1,"Z",[20,30,40,50,60])
print(var1)
var1["X"]=var1["Z"][:3] #copying limited data using slicing
print(var1)
var1.pop("A")
print(var1)
