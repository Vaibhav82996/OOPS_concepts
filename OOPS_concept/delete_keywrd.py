#del keyword....
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

s1= student("vaibhav pandey",55)
s2 = student("Hello world",66)

m1 = student("Math",33)
m2 = student("science",66)
#del s2         this is del keyword...
print(s2.name)
print(s1.name)
print("sub:",m1.name ,"marks: ",m1.marks)
print("sub:",m2.name ,"marks: ",m2.marks) 