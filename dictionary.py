info = {
    "name": "SHeri",
    "Department": "Computer Science",
    "Rollno": 34,
    "Cgpa": 3.4,
    "Subjects": ["Algebra", "Dsa", "Database", "Sf"],
    "Marks": (40, 50, 60, 70, 80)
}

print(info)
print(info["Marks"])
print(info["Subjects"])
nest = {
    "name" : "SHeri",
    "Subjects" : {
        "Dsa" : 20,
        "Cn" : 50,
        "Algebra" : 70,
        "Dbms" : 90,
    }
}
print(nest)
print(nest["Subjects"])
print(nest["Subjects"]["Dbms"])
nest.update({"City" : "Gujrat"})
print(nest)