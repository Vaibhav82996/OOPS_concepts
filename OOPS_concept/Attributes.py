#Class & instance attrivbutes..
class student:
  
  def __init__(self,name,marks):  
    self.name = name
    self.marks = marks
    print("Adding new students and their marks in database..")

s1 = student("Vaibhav pandey", 34)
print("Name = ",s1.name,",", "Marks = ",s1.marks)

s2 = student("Karan singh", 87)
print("Name = ",s2.name,",", "Marks = ",s2.marks)