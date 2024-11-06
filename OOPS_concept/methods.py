#Methods...
class student:
  
  def __init__(self,fullname,marks):   
    self.name = fullname
    self.marks = marks
    print("Adding new students in database..")

  def welcom(self):
   print("Welcom student..",self.name)

  def get_marks(self):
   return self.marks
  
s1 = student("Vaibnhav",22)
s1.welcom()
print(s1.get_marks())