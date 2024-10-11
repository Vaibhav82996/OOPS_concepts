# #print numbers 1 to 100.
# i = 1
# while i <=100:
#     print(i)
#     i +=1
# print("Counting end")

# #Print 0 to 100.
# j = 100
# while j >= 1:
#     print(j)
#     j -= 1
# print("Counting ends")

# #multiplication table of n. 
# n = int(input("Enter the number : "))
# k = 1
# while k <=10:
#     print(n*k)
#     k += 1
# print("Here is the table of ",n)

#print the element of list using loop.
# num = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(num):
#     print(num[idx])
#     idx +=1

# #another question.
# hero = ["ironman", "superman", "batman", "thor"]
# i = 0
# while i< len(hero):
#     print(hero[i])
#     i += 1

#Search the number X  in tuple using loops.
tup = (1,4,9,16,25,36,49,64,81,100)
x = 25
i = 0
while i < len(tup):
    if(tup[i] == x):
        print("Fount at index",i)
    else:
        print("finding...")
        i +=1 
    print("Loop end here")