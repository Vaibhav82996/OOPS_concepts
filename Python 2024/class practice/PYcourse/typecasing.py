a = "1"
b = "2"
print(a+b) #Here a and b is taken as a string data type coz its in double quote.
a = 1
b = 2
print(a+b) #now it is taken as int datatype
    #Second method
a = "1"
b = "2"
print(int(a)+int(b)) 

#Typecastig are of two type.
#-------------------------------------#
# 1: explicit : the conversin of one datatype into another dt,done via devloper or user manually as per the requirement,
#can be achive by fun like int(),float(),str(),hex(),oct(). its also called typecasting coz the user caste [changes th DT of obj]
#example;
string = "15"
number = 7
string_number =int(string)
sum = number + string_number
print("The sum will be : ",sum)
print(type(sum))

#2: implicit : one dt is converted into another dt by python interpretor itself automatically.
#example;
a = 8
print(type(a))
b = 2.4
print(type(b))
c = a + b
print(c)
print(type(c))