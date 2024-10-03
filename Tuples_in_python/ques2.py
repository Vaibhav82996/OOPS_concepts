#checking palindrom element.(a element which is same in reading whether it is read from back or front).
list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("List is palindrom")
else:
    print("List is not a palindrom")