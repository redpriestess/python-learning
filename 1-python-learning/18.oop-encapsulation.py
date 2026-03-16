class BankAccount:
    def __init__(self,balance,pwd):
        self._balance= balance
        self._pwd=pwd
    
    def withdraw(self,amount):
        self._balance -= amount
        
    def deposit(self,amount):
        self._amount += amount
        
    #getters
    def show_balance(self):
        pwd=input("Please enter your password: ")
        if pwd=='riri':
            return self._balance
        else:
            return 'scram'
        
    #setter
    def set_balance(self,new_balance):
        if new_balance<1000000:
            self._balance = new_balance
        
        
    
        
rishkas_acct=BankAccount(1000,'riri')
# print(rishkas_acct.balance)
# print(rishkas_acct.show_balance())