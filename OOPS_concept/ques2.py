#Create account with 2 attributes - balance & acc.no and create a method for debit,credit & priinting the balance..
class account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_num = acc

    def debited(self,amount):
        self.balance -= amount
        print("RS: ", amount , "was debited")
        print("Total balance = ",self.get_balance())

    def credited(self,amount):
        self.balance  += amount
        print("RS: ",amount, "was credited")
        print("Total balance = ",self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = account(10000, 123456)
print("Your current balance is :",acc1.balance, "and your account number is : ",acc1.account_num)
acc1.debited(1000)
acc1.credited(500)
acc1.credited(2000)
acc1.credited(300)