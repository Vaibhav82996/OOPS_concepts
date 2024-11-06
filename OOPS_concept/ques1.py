#Getting avg marks..
class student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def avg_mark(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Congrats..",self.name,"Your AVG score is : ", sum/5)

s1 = student("Vaibhav apndey", [88,89,99,79,87])
s1.avg_mark()