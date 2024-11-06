#Abstraction : hiding implementation details and showing important details only to users..
class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started..")

car1 = car()
car1.start()  

#Encapsulation : Wrapping up data and functions into single unit(object)..