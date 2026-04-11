import pandas as pd
var1=pd.DataFrame({"A":[1,2,3,4,5],"B":[5,6,7,8,9]})
var1["C"]=var1["A"]+var1["B"]
var1["D"]=var1["A"]-var1["B"]
var1["E"]=var1["A"]*var1["B"]
print(var1)