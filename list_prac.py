arr=[1,2,3,4,5]
arr.reverse()
print(arr)
arr.reverse()
reversed_arr = arr[::-1]
print(arr)
print(reversed_arr)
array=[1,2,3,4,4,5,2,1]
unique = list(set(array))
print(unique)
my_list = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input(f"Enter integer number {i+1}: "))
    my_list.append(element)
print(my_list)
my_list.sort()
print(my_list[n-2])

