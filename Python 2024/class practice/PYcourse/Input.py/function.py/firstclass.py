def add(x,y):
    z = x+y
    print("Sum is : ",z)
    
def Max1(x,y):  
    if(x>y):
        print("max value  :",x)
    else:
        print("max value : ",y)
        
def Max3(x,y,z):
    if(x>=y) and (x>=z):
        print("max value :",x)
    elif(y>=x) and (y>=z):
        print("max value :",y)
    else:
        print("max value is :",z)
        
def R_number(x): #Reverse of numbers;
    sum = 0
    while(x!=0):
        rem = x%10
        sum = sum*10 + rem;
        x = x//10
    print("Reverse is : ",sum)
    
def P_number(x): #Palindrom number;
        y = x
        sum = 0
        while(x!=0):
            rem = x%10
            sum = sum*10 + rem
            x = x//10
        if(y==sum):
            print("Number is palindrom")
        else:
            print("Number is not palindrom")
def Main():
    while True:
        opt = int(input("Enter option: \n1.Add two number: \n2.Find Max value: \n3.Find Max value in three digits: \n4.Reverse the number: \n5.Find Palindrom number: "))
        
        if(opt==1): 
         x = int(input("Enter a number : ")) 
         y = int(input("Enter another number : "))    
         add(x,y)   
         
        elif(opt==2):
         x = int(input("Enter first number :"))  
         y = int(input("Enter second number :"))
         Max1(x,y)
         
        elif(opt==3):
         x = int(input("Enter the first number :"))
         y = int(input("Enter the second number :"))
         z = int(input("Enter the third number :"))
         Max3(x,y,z)
         
        elif(opt==4):
         x = int(input("Enter a number : "))
         R_number(x)
         
        elif(opt==5):
         x = int(input("Enter the number :"))
         P_number(x)
         
        else:
            print("Enter the valid option")
            
Main()