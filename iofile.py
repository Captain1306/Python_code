# with open("p.txt", "w") as f:
#     f.write("Hi everyone \n we are learning I\O \n ")
#     f.write("using python \n i like python")
with open("p.txt", "r") as f:
    data = f.read()
new_data=data.replace("Python","c++")
print(new_data)
with open("p.txt", "w") as f:
    data = f.write(new_data)
