class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def show(self):
        print(self.real,"i+",self.img,"j")
    def __add__(self,n2):
        real_no=self.real+n2.real
        img_no=self.img+n2.img
        return complex(real_no,img_no)
    def __sub__(self,n2):
        real_no=self.real-n2.real
        img_no=self.img-n2.img
        return complex(real_no,img_no)

n1=complex(10,5)
n2=complex(15,30)
n1.show()
n2.show()
n3=n1+n2
n3.show()
n4=n1-n2
n4.show()