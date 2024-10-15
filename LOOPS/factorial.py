#wap to find factorial of first n numbers.(using while loop)
#Factorial of any number is multiple of all numbers till where we actuaslly want like factorial of 5 is 1*2*3*4*5
# . which is 120.
# n = 6
# fact = 1
# i = 1
# while i <= n:                                   
#     fact *= i
#     i += 1

# print("Factorial = ",fact)

#with for loop.
n = 4
fact = 1
for i in range (1,n+1):
    fact *= i
print("Factorial =",fact)