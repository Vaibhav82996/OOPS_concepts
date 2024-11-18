class person:
    __name = "Anonymus"

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()

p1 = person()
print(p1.welcome())     #we can't call __hello directly so we call welcome and welcome will call __hello function for me.