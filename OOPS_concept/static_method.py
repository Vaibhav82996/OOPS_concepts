#Static methods : methods that don't use the self parameter (work at class level)
class student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    @staticmethod   ## DECORATOR, for changing behavior of a function into static function..
    def Hello():
        print("Hello")

    def avg_mark(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Congrats..",self.name,"Your AVG score is : ", sum/5)

s1 = student("Vaibhav apndey", [88,89,99,79,87])
s1.avg_mark()
s1.Hello()