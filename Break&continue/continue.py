#continue (terminate current case and move on next statemnts.)
i = 0
while i <= 10:
    if(i == 6):
        i += 1
        continue        #acts a skip.
    print(i)
    i += 1

#print odd numbers 
i = 0
while i <= 50:
    if(i % 2==0):
        i +=1
        continue
    print(i)
    i +=1

#print even numbers 
i = 0
while i <= 50:
    if(i % 2 !=0):
        i +=1
        continue
    print(i)
    i +=1         