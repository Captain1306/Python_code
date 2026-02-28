info = ["Sheri" , 20 , "Failed"]
print(info)
info[2] = "Pass"
print(info)
marks = [60,70,90,100]
print(marks)
marks.append(99)
print(marks)
marks.insert(1,19)
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
marks.pop(2)
print(marks)
marks.remove(99)
print(marks)
movies = []
m1 = input("ENter movie 1")
movies.append(m1)
m2 = input("ENter movie 2")
movies.append(m2)
m3 = input("Enter movie 3")
movies.append(m3)
print(movies)
pali = [1,2,2,1]
pali1=pali.copy
pali1.reverse()
if(pali==pali1):
    print("yes its palindrome")
else:
    print("No its not palindrome")
