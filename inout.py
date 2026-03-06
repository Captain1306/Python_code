f=open("demo.txt","r")
data = f.read()
data2 = f.readline()
print(data)
print(data2)
f.close()
f=open("demo.txt", "w")
f.write("I want to learn python")
f.close()
f=open("demo.txt","a+")
f.write("\n I am mid in c++ :) ")
print(f.readline())
f.close()
with open("demo2.txt", "r") as f:
    data = f.readline()
    print(data)
with open("demo2.txt", "w") as g:
    g.write("New data is stored")




