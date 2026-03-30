'''
07/08//01/2026
1. Library Membership and Borrowing Log
   A local library wants to track members and the books they borrow.

* Create a Member class with attributes name, member_id, and borrowed_books (a list).
* Create a method to borrow a book that asks the user for a book title and adds it to borrowed_books only if the member has borrowed fewer than 3 books.
* Use an if condition to prevent borrowing more than 3 books.
* Create a method to return a book that asks the user for a title and removes it from the list if it exists.
* Use a for loop to display all currently borrowed books.
'''
# class Member:
#    def __init__(self,name,member_id):
#       self.name=name
#       self.member_id=member_id
#       self.borrowedbooks=[]

#    #if user enters more than 3, and you want it to restart
#    def borrowing(self):
#       while True:
#          user=input("pls enter book titles")
#          if user=="done":
#             break
#          if len(self.borrowedbooks)<3:
#             self.borrowedbooks.append(user)
#          else:
#             print("too many borrowed")
#             self.borrowedbooks=[]
#             continue 
   
#    # #u wanna fix the amount of books they can enter frm the start
#    # def borrowing(self):
#    #    while len(self.borrowedbooks)<3:
#    #       user=input("pls enter book titles")
#    #       self.borrowedbooks.append(user)
   
#    def returning(self):
#       print(self.borrowedbooks)
#       while True:
#          user=input("pls enter book title")
#          if user=="done":
#             break 
#          if user in self.borrowedbooks:
#             self.borrowedbooks.remove(user)
   
#    def what(self):
#       for books in self.borrowedbooks:
#          print(f"borrowed books is {books}")
   
# member1=Member("rishka",23)
# member1.borrowing()
# member1.returning()
# member1.what()
      

'''
2. Grocery Store Shopping Cart
   A grocery store wants to simulate a shopping cart system.

* Create a ShoppingCart class with attributes items (a dictionary of item_name: price) and total_cost.
* Create a method to add items by repeatedly asking the user for item names and prices until the user enters "done".
* Use a while loop for repeated input.
* Use a dictionary to store items and prices.
* Create a method to calculate the total cost using a for loop over the dictionary values.
* Use an if condition to reject negative prices.
'''

# # class shopping_cart():
# #    def __init__(self):
# #       self.total_cost=0.0
# #       self.items = {}
   
# #    def things(self):
# #       while True:
# #          items=input("pls enter item names")
# #          if items == "done":
# #             break
# #          prices=float(input("pls enter prices:"))
# #          if prices<0:
# #             print("pls enter positive numbers only")
# #             continue
            
# #          self.items[items]=prices
   
# #    def finding_total(self):
# #       for prices in self.items.values():
# #          self.total_cost+=prices
# #       print(f"the total costs is {self.total_cost}, for items {self.items}")
         

# # shopping1=shopping_cart()     
# # shopping1.things()
# # shopping1.finding_total()


'''
3. Fitness Tracker Daily Steps
   A fitness app wants to track a user's daily steps over a week.

* Create a FitnessTracker class with attributes username and daily_steps (a list).
* Create a method to record steps that asks the user to enter steps for each day of the week using a for loop.
* Use if conditions to reject negative step counts.
* Create a method to calculate the average steps per day.
* Create a method that checks if the user met a daily goal of 8000 steps on each day and prints the days they failed to meet the goal.
'''
# # class fitnesstracker():
# #    def __init__(self,username):
# #       self.username=username
# #       self.daily_steps=[]
# #       self.daily_days=[]
   
# #    def weeklysteps(self):
# #          days=["mon","tues","Wed","thurs","fri"]
# #          for day in days:
# #             steps=int(input("pls enter no.steps"))

# #             if steps<0:
# #                print("only positive numbers")
# #                continue

# #             self.daily_steps.append(steps)
# #             self.daily_days.append(day)
   
# #    def average_steps(self):
# #       ave = sum(self.daily_steps)/len(self.daily_steps)
# #       print(f"no of average steps per day is {ave}")

# #    def goals(self):
# #       for i in range(len(self.daily_steps)):
# #          if self.daily_steps[i] <8000:
# #             print(f"you failed to meet your gaol on {self.daily_days[i]}")

# # fitnesstracker1=fitnesstracker("rishka")
# # fitnesstracker1.weeklysteps()
# # fitnesstracker1.average_steps()
# # fitnesstracker1.goals()




'''
4. Simple Classroom Grade Book
   A teacher wants a program to manage student grades.

* Create a GradeBook class with attributes course_name and grades (a dictionary of student_name: list_of_scores).
* Create a method to add a student and initialize an empty score list.
* Create a method to add multiple scores for a student using a while loop until the user enters -1.
* Use if conditions to ensure scores are between 0 and 100.
* Create a method to calculate and display each student’s average using a for loop.
'''
# # class StudentGrades():
# #    def __init__(self,course_name):
# #       self.course_name=course_name
# #       self.transcript={}
   
# #    def add_students(self,student_name):
# #       if student_name in self.transcript:
# #          print("girl your name is in here already bye")
# #       else:
# #          self.transcript[student_name]=[]
# #          print(f"{student_name} was added")
# #    def scores(self,student_name):
# #       while True:
# #          scores=int(input("pls enter student scores"))
# #          if scores == -1:
# #             break
# #          if scores>=0 and scores<=100:
# #             self.transcript[student_name].append(scores)
         
# #    def student_average(self):
# #       for student,scores in self.transcript.items():
# #          if len(scores)==0:
# #             print(f"{student} has no scores")
# #          else:
# #             average= sum(scores)/len(scores)
# #             print(f"{student}'s average score is {average}")

            
# # student1=student_grades("biology")
# # student1.add_students("rishka")
# # student1.scores("rishka")
# # student1.student_average()
         
# # student2=student_grades("maths")
# # student2.add_students("aryan")
# # student2.scores("aryan")
# # student2.student_average()
   
   
'''
3. Fitness Tracker Daily Steps
   A fitness app wants to track a user's daily steps over a week.

* Create a FitnessTracker class with attributes username and daily_steps (a list).
* Create a method to record steps that asks the user to enter steps for each day of the week using a for loop.
* Use if conditions to reject negative step counts.
* Create a method to calculate the average steps per day.
* Create a method that checks if the user met a daily goal of 8000 steps on each day and prints the days they failed to meet the goal.
'''

# class fitnesstracker:
#    def __init__(self,username):
#       self.username=username
#       self.daily_steps=[]
   
#    def daily_update(self):
#       self.days=["monday","tuesday","wednesday","thursday","friday"]
#       for i in self.days:
#          ran=int(input(f"pls enter how much you ran on {i}"))
#          if ran<0:
#             print("only positive values")
#             continue
#          self.daily_steps.append(ran)
   
#    def average(self):
#       average=sum(self.daily_steps)/len(self.daily_steps)
#       print(f"average you have run is {average}")
   
#    def goal(self):
#       for day,steps in zip(self.days,self.daily_steps):
#          if steps<8000:
#             print(f"you reached less than 8k steps on {day}")
#       # for i in range(len(self.daily_steps)):
#       #    if self.daily_steps[i]<8000:
#       #       print(f"On {self.days[i]} you ran less than 8000 steps")


# fitness1=fitnesstracker("rishka")
# fitness1.daily_update()
# fitness1.average()
# fitness1.goal()




'''
4. Simple Classroom Grade Book
   A teacher wants a program to manage student grades.

* Create a GradeBook class with attributes course_name and grades (a dictionary of student_name: list_of_scores).
* Create a method to add a student and initialize an empty score list.
* Create a method to add multiple scores for a student using a while loop until the user enters -1.
* Use if conditions to ensure scores are between 0 and 100.
* Create a method to calculate and display each student’s average using a for loop.
'''
    
# class Gradebook:
#    def __init__(self,course_name):
#       self.course_name=course_name
#       self.grades={} 
   
#    def student(self):
#       scores=[]
#       name=input("pls enter your name: ") 
#       while True:
#          grades=int(input("pls enter your scores: "))
#          if grades== -1:
#             break
#          if grades>0 and grades<100:
#             scores.append(grades)
      
#       self.grades[name]=scores 

#    def ind(self):
#       for name,score in self.grades.items():
#          averages=sum(score)/len(score)
#          print(f"student {name} has an average score of {averages} in course {self.course_name}")



# grade1=Gradebook("Biology")
# grade1.student()
# grade1.ind()
   


'''

5. ATM Simulation System
   A bank wants to simulate an ATM with basic controls.

* Create an ATM class with attributes balance, transaction_history (a list), and daily_limit.
* Create a method to deposit money that asks the user for an amount and updates balance.
* Create a method to withdraw money that checks the daily_limit and available balance using if conditions.
* Store each transaction as a dictionary with keys type and amount and append it to transaction_history.
* Use a for loop to display all transactions at the end of the session.
'''

# class ATM:
#    def __init__(self,daily_limit,balance):
#       self.daily_limit=daily_limit
#       self.balance=balance 
#       self.transaction_history=[]
   
#    def update(self):
#       user=int(input("pls enter how much u wanna deposit: "))
#       self.balance+=user
#       ttype={"type":"deposit",
#             "amount": user}
      
#       self.transaction_history.append(ttype)

   
#    def withdraw(self):
#       user=int(input("pls enter how much u wanna withdraw: ")) 
#       if user<self.balance and user<self.daily_limit:
#          self.balance-=user 
#       ttype={"type":"withdraw",
#             "amount": user}
      
#       self.transaction_history.append(ttype) 
   
#    def ending(self):
#       for name in self.transaction_history:
#          print(f"your transaction type is {name["type"]} and amount is {name["amount"]}")

# atm1=ATM(5000,4500)
# atm1.update()
# atm1.ending()
      
'''
2. Grocery Store Shopping Cart
   A grocery store wants to simulate a shopping cart system.

* Create a ShoppingCart class with attributes items (a dictionary of item_name: price) and total_cost.
* Create a method to add items by repeatedly asking the user for item names and prices until the user enters "done".
* Use a while loop for repeated input.
* Use a dictionary to store items and prices.
* Create a method to calculate the total cost using a for loop over the dictionary values.
* Use an if condition to reject negative prices.
'''
# class shoppingcart:
#    def __init__(self):
#       self.products={}
   
#    def items(self):
#       while True:
#          name=input("pls enter item name:")
#          if name=="done":
#             break
#          price=int(input("pls enter item price")) 
#          self.products[name]=price
   
#    def calculate(self):
#       total=0
#       for name,price in self.products.items():
#          if price<0:
#             print("no negative prices")
#          else:
#             total+=price
#       print(total)

# shopping1=shoppingcart()
# shopping1.items()
# shopping1.calculate()
'''
3. Fitness Tracker Daily Steps
   A fitness app wants to track a user's daily steps over a week.

* Create a FitnessTracker class with attributes username and daily_steps (a list).
* Create a method to record steps that asks the user to enter steps for each day of the week using a for loop.
* Use if conditions to reject negative step counts.
* Create a method to calculate the average steps per day.
* Create a method that checks if the user met a daily goal of 8000 steps on each day and prints the days they failed to meet the goal.
'''

class fitnesstracker:
   def __init__(self,username):
      self.username=username
      self.daily_steps=[]
   
   def steps(self):
      self.days=["mon","tues","wed","thurs","fri","sat","sun"]
      for day in self.days:
         while True:
            steps=int(input("pls enter no.steps")) 
            if steps<0:
               print("no negative numbers")
            else:
               self.daily_steps.append(steps)
               break 
   def overall(self):
      ovarll=sum(self.daily_steps)/len(self.daily_steps)
      print(f"{self.username} had average of {ovarll} steps") 
   
   def goals(self):
      for i in range(len(self.days)):
         if self.daily_steps[i]<8000:
            print(f"on {self.days[i]}, you only ran {self.daily_steps[i]}")

# f1=fitnesstracker("rishkyyyy")
# f1.steps()
# f1.overall()
# f1.goals()


 






