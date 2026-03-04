def count(n):
    if n == 0:
        return
    print("The Count : ", n)
    count(n - 1)  # Subtracts 1 each time so it eventually hits 0

count(5)


def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n - 1)

print(fac(5))

    
