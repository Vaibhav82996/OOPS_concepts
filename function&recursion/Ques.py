#1: waf to print the length of a list (list ius the parameter)..
cities = ["delhi", "mumbai", "chennai", "pune", "noida"]
food = ["burger","pizzqa", "noodles", "icecream"]

def calc_len(list):
    print(len(list))

calc_len(cities)
calc_len(food)

#2: waf to print the elements of list in single line.
cars = ["BMW", "audi", "mercides", "mcleran", "Porsche"]

def print_list(list):
    for item in list:
        print(item, end=" ")                #here end= is used to give space and print in same line all the elements.
    
print_list(cars)    

#waf to find factorial of n.
def calc_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

calc_fact(6)


#waf to convert USD to INR.....
def converter(usd_value):
    inr_value = usd_value * 84.06
    print(usd_value,"USD =", inr_value,"INR")

converter(230)