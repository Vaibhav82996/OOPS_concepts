#logical operator.( NOT, AND , OR)
#NOT = gives opposite answer.
#AND = works on two values.it give true when both value are true .
#OR = it give answer true ,when any one value is true. 
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
print(not(a>b))

val1 = int(input("Enter the val1 : "))
val2 = int(input("enter the val2 : "))
print("AND operator will give : ", (val1 >= 50) and (val2 < 100))

num1 = int(input("Enter the num1 : "))
num2 = int(input("Enter the num2 : "))
print("OR operator will give : ", (num1 >=40) or (num2 < 50))