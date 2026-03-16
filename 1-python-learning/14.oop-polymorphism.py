'''
poly- many
morphing- changing 

polymorphing- single method, many forms

one god - 

'''

class ATM():
   def __init__(self, balance, daily_limit):
      self.balance = balance
      self.daily_limit = daily_limit
      self.transaction_history = []

   def deposit(self, amount):
      if amount > 0:
         self.balance += amount
         print(
             f"You deposited {amount} dollars. New balance is {self.balance}")
      else:
         print(f"Amount needs to be positive!!")

   def withdrawal(self, amount):
      if amount > self.daily_limit:
         print("u can't take out more than the daily limit")
         return
      if amount > self.balance:
         print("u r poor, u dont have enough to withdraw that much")
      else:
         self.balance -= amount
      print(
          f"the amnt u have withdrawn is {amount} and your current balance is {self.balance}")
      
class RHBATM(ATM):
    def __init__(self, balance, daily_limit, bank_name, safety_cam):
        super().__init__(balance,daily_limit)
        self.bank_name=bank_name
        self.safety_cam=safety_cam
        
    def deposit(self, amount):
      if amount > 0:
         self.balance += amount
         print(
             f"You deposited {amount} dollars to your RHB account. New balance is {self.balance}. Live long and prosper !!")
      else:
         print(f"Amount needs to be positive!!")
    
    def check_activity(self):
        '''accesses the webcam inside the ATM Cubicle'''
        return "image"
        


atm1=ATM(90,30)
# atm1.deposit(100)
# atm1.withdrawal(50)


rhb_atm1=RHBATM(80,100,'RHB','logitech c270')
# rhb_atm1.deposit(100)

atms=[atm1,rhb_atm1]
for atm in atms:
    atm.deposit(80)




   

