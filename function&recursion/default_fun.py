#Default parameters.
# def calc_prod(a,b):
#     print(a*b)
#     return a*b
# calc_prod()       #this will give error becausee arguments arer missing.

def calc_prod(a = 2,b = 6):
    print(a*b)
    return a*b
calc_prod()         #in this we can add values in parameters which automatic takes a argument.

def calc_prod(a,b = 3):
    print(a*b)
    return a*b
calc_prod(5)            #Another way.