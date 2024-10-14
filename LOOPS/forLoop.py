#For loop.
list = (1,2,3,4,5,6,7,8)

for val in list:
    print(val) 

#we can print  chaeracters from string.
str = "vaibhav pandey"

for char in str:
    if(char == 'd'):
        print("d found")
        break
    print(char)
else:                 #Optional.
    print("end")