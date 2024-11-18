#INHERITANCE : When one class (child/derived)derives the properties& methods of another class(parent/base)
#Syntax....
# class Car:
#class toyotaCar(Car):

#single level inheritance..
class Car:
    @staticmethod
    def start():
        print("Car started") 

    @staticmethod
    def stop():
        print("Car stopped")

class TototaCar(Car):
        def __init__(self,name):
            self.name=name

Car1 = TototaCar("Fortuner")
Car2 = TototaCar("Yaris")
print(Car1.name)
print(Car1.start())
print(Car2.name)
print(Car2.stop())   