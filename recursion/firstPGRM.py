#Basic syntax example for recursive function.
def show(n):
    if(n == 0):     #Base case..
         return
    print(n)
    show(n-1)       #Recursion..
    print("End")
show(10)