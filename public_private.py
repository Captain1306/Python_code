class account:
    def __init__(self,acc_no,acc_pass):
        self.account=acc_no
        self.__password=acc_pass

    def show(self):
        print(self.account)
        print(self.__password)
    

a=account("786786","abcsd")
a.show()
print(a.__password) #this shows error bcz cannot directly access privte attributes
print(a.acc_no)

    