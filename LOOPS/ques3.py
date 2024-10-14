#find the number x form the tuple using loop.
tup = (1,2,4,49,33,45,77,56,100,49,58)
x = int(input("Enter the num: "))
idx = 0
for element in tup:
    if(element == x):
        print("Element found at index",idx)
       # break                   #use if u want to find only single element from it.
    idx +=1