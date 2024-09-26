a = 3
b = 6
sum = a + b
print("The sum of a + b is : ",sum)
#Examples of operators
print(5+3)
print(4-2) 
print(4*3)
print(3/5)      
print(3//5)         #floair division
print(3%5)
print(5**3) # Exponential operator  
#operators are used to perform operations on variables and values. python dividesoperatos in folowing groups
#comparision values: (return true or false){==,!=,<,>,<=,>=}
#relational op: use to combine conditional statement.(AND,OR,NOT)
#example: (x>5 AND x<3),(x>5 OR x<10)
#bitwise op : (&,|,^,~,>>,<<)and,or,x-or,negation,shift right,shift left.
a = 20
b = 30
c = a&b
d = a|b
e = a^b
f = a>>2
g = a<<2
print(c,d,e,f,g)
#identity op: evaluates to do if the variables on eithr side of the operators point to the same object and false otherwise.
#x = ['apple','banana']
#y = ['apple','banana']
#z= x
#print(x is z)
#print(x is y)
#print(x == y)
#4 object refrences : python is a highely obj oriented language. infact virtually every iteam of datain python pgrm 
#is an obj of a specific type or class.
#example: \
#print(300) #it create int obj
#gives it a value 300
#display it to the console 
#a python variable is a symbolic name that is a refrence or pointer to an obj. onse an obj is assingned to a variable we can refer to the obj by that name but the data itself is still contain within the obj there is no longer any refrence to the int obj 300. it is orphand and there is no way to access it 
#id  functon: the bultin py fun. id returns an obj int identifer. using the id function we can verify that two variables indeed point to to the same varibale 
# n = 300
# m = n
# print(id(m))
# print(id(n))
#python provide two buil-in methon to read the data from keybpoard.
#the input funautomatically converts the user input itno str. we need to explictly convert the input using typecasting 
# name = input("Enter your name : ")
# print(name)
