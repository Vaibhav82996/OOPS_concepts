tup = (1,4,9,16,25,36,49,64,81,100)
x = 25
i = 0
while i < len(tup):
    if(tup[i] == x):
        print("Fount at index",i)
        break
    else:
        print("finding...")
        i +=1 
    print("Loop end here")