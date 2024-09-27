x = 35e3
y = 42e4
z = -87.8e100
print(x)
print(y)
print(z)
#2
a = 4+5j
print("type of a is",type(a))
print("a is complex number",isinstance(4+5j,complex))
#3
x = 5
y = 4.5
z = 1+4j
a= int(y)
b = complex(y)
print(type(a),a)
print(type(b),b)
#4
c = float(x)
d = complex(x)
print(type(c),c)
print(type(d),d)
#5
import random
print(random.random())
print(type(random.random))
print(random.randrange(1,10))
print(type(random.randrange(1,10)))
# random.randrange(start,stop,step)
#start-(optional)-an interger specificing at which positon to start,default 0. 
#stop-(required)- and integer specifng at which position to end.
#step-(optional)- an integer specifing the incrementtaion ,default is 1.
#example
print(random.randrange(200,400,7))
print(random.randrange(500))
#random.getrandbits()   # this return the int formed with bits binary sequence. if n is 2 then it can generate 

#4
import random
print(random.choice([50,40,45,30,42]))
mylist = ["apple","banana","cherry"]
random.shuffle(mylist)
print(mylist)
#python boolean
#boolean type provides to builtin values,true and false.it denotes by the class bool
#almost any value is evaluated if it has some sort of content
#any string is true if it expect string
#any number is true expect 0
#any list,tuple ,set,dictionry are true expect empty one.
#bool fun. allows u to evaluate any value and retrn true or false 
#example
bool()
bool(123) #true
bool("123") #true
bool(["apple","banana"]) #true
#casting
#the process of converting the value of one datat type to another dt is caleed typ comversion.python hSs two type of type of cnversion
#elif 
# color =(input("Enter the color:"))
# if(color=="red"):
#     print("Color is red")
# elif(color=="blue"):
#     print("Color is blue")
# elif(color=="green"):
#     print("color is green")
# else:
#     print("color is neigther blue,green or red")
#nested if
#num=float(input("Enter the number :"))
# if(num<=0):
#     if (num==0)
#         print("number is zero")
#     else:
#         ("number is positive")
# else:
#     print("number is negative ")
a = 10
b = 20
min = a if a<b else b