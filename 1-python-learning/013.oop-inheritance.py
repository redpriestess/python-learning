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
         print("u ccan't take out more than the daily limit")
         return
      if amount > self.balance:
         print("u r poor, u dont have enough to withdraw that much")
      else:
         self.balance -= amount
      print(
          f"the amnt u have withdrawn is {amount} and your current balance is {self.balance}")


# class RHBATM():
#     def __init__(self, balance, daily_limit, bank_name, safety_cam):

#         self.balance = balance
#         self.daily_limit = daily_limit
#         self.transaction_history = []
#         self.bank_name = bank_name
#         self.safety_cam = safety_cam

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"You deposited {amount} dollars. New balance is {self.balance}")
#         else:
#             print(f"Amount needs to be positive!!")

#     def withdrawal(self,amount):
#         if amount>self.daily_limit:
#             print("u ccan't take out more than the daily limit")
#             return
#         if amount>self.balance:
#             print("u r poor, u dont have enough to withdraw that much")
#         else:
#             self.balance-=amount 
#         print(f"the amnt u have withdrawn is {amount} and your current balance is {self.balance}")
    
    
#     def check_activity(self):
#         '''accesses the webcam inside the ATM Cubicle'''
#         return "image"
      
class RHBATM(ATM):
    def __init__(self, balance, daily_limit, bank_name, safety_cam):
        super().__init__(balance,daily_limit)
        self.bank_name=bank_name
        self.safety_cam=safety_cam
    
    def check_activity(self):
        '''accesses the webcam inside the ATM Cubicle'''
        return "image"
        
# atm1=ATM(90,30)
# atm1.deposit(100)
# atm1.withdrawal(50)
# atm1.deposit(20)
# atm1.withdrawal(10)

rhb_atm1=RHBATM(80,100,"rishka","seen")
rhb_atm1.deposit(100)



# menu = '''
# Please select action: 

# 1. Deposit
# 2. Withdraw

# Enter 'done' to quit program: 
# '''

# while True: 
#    user_input=input(menu)
#    if user_input=='1':
#       deposit_amt=int(input("Please enter deposit amount: "))
#       atm1.deposit(deposit_amt)
#       continue
#    elif user_input=='2':
#       pass
#    elif user_input=='done':
#       print("Nice chatting with you!! Byee!!")
#       break
#    else:
#       print("Unsupported input")
#       continue
   
   