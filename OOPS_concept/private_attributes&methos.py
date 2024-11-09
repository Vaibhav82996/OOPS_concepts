#private(like) attributes & methods...
#private attributes & methods are ment to be used only within the class and are not accessible from outside the class.

class account :
    def __init__(self,acc_num,acc_pass):
        self.acc_num = acc_num
        self.acc_pass = acc_pass

acc1 = account("123456","abcde")

print(acc1.acc_num)
print(acc1.acc_pass)        #This is publicly accessible whic is not safe

#print(acc1.__acc_pass)  .. this is now private by applying __ before acc_pass which become __acc_pass..