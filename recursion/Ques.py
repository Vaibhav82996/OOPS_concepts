#1: write a recursive function to ca;lculate the sum of first n natural num,bers..
def sum(n):
    if(n == 0):
        return 0
    return sum(n-1) + n
sum = sum(10)
print(sum)

#write a recursive function to print all elements in a list.(use list& index as a parameter..)
def print_list(list, idx= 0):
    if(idx == len(list)):
        return
    print(list(idx))
    print_list(list, idx+1)

food = ["mango", "apple", "banana", "apple"]
print_list(food)