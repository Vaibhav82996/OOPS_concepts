#Factorial with recursion.
#n! = (n-1)! * n    recurance relation..
#to do recursion in facvtroial we should first do as:
# fact(n) = fact(n-1) * n
#              or
#fact(n-1) = fact(n-2) * (n-1)

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n
print(fact(6))