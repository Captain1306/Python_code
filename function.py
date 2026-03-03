def avg(a,b,c):
    ans=a+b+c/3
    print("THe avg is : ", ans)

def fac(n):
    ans=1
    for i in range(1,n+1) :
        ans=ans*i
    return ans


avg(10,20,30)
avg(25,50,100)
avg(5,7,20)

num = int(input("ENter number to find factorial"))
print("FActorial is : ",fac(num))
