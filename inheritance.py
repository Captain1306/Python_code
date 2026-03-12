class car:
    colour="Black"
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car stopped")
class bmw(car):
    def __init__(self,name,model):
        self.name=name
        self.model=model

car1=bmw("m3","G80")
car2=bmw("m5","f90")
print(car1.name)
print(car1.model)
car1.start()
print(car2.name)
print(car2.model)
car2.stop()

