class BankAccount:
    def __init__(self,balance):
        self.balance=balance
        self.deposit(100)

    def withdrawal(self,amount):
        if amount< self.balance:
            self.balance-=amount
            print(f"withrdrawed {amount}, remaining balance {self.balance}")
        else:
            print("You don't have enough balance for this withdrawal")
            
    def deposit(self,amount):
        self.balance+=amount
        print(f"depost if {amount} made, new balance: {self.balance}")
  
#january first       
rba=BankAccount(300)

#next week
rba.withdrawal(100)

#in two more weeks
rba.deposit(500)
# a week after
rba.withdrawal(100)
#in 4 more weeks
rba.deposit(1000)

#a week after 
rba.withdrawal(200)

        
    