'''
implement an animal class. 
create attributes for animal name, breed and diet. 
For an instance 
dog = Animal('Gordon', 'dog','omnivore')

Create method for printing the diet
Create a method for printing the name
Use suitable method names
'''

# class Animal:
#     def __init__(self,animal_name,breed,diet):
#         self.diet=diet
#         self.animal_name=animal_name
#         self.breed=breed
    
#     def print_name(self):
#         print(f"the animal's name is {self.animal_name}")
#         self.print_diet()
    
#     def print_diet(self):
#         print(f"{self.animal_name}'s diet is {self.diet}")


# animal1= Animal("frizzy","chichi","carnivore")
# animal1.print_name()
# animal1.print_diet()


# animal2= Animal("rino","unnatural","herbivores")


'''
Rishka: self given

Task: Counter class

Create a class Counter that:
starts with a value (default 0)
has methods:
increment() → adds 1
decrement() → subtracts 1
reset() → sets value back to 0
get_value() → returns current value
'''

# class counter():
#     def __init__(self,to_increase,to_decrease):
#         self.to_increase=to_increase
#         self.to_decrease=to_decrease

#         self.counterer()
    
#     def counterer(self):
    
#         if self.to_increase:
#             self.to_increase+=1
       
#         if self.to_decrease:
#             self.to_decrease-=1
#         # self.reset=reset 
#         # if reset:
#         #     value=0
#         print(f"values that increased is {self.to_increase}, values that decreased is {self.to_decrease}")

# num1=counter(10,2)


#improved version
# class Counter:

#     def __init__(self, value=0):
#         self.value = value

#     def increment(self):
#         self.value += 1

#     def decrement(self):
#         self.value -= 1

#     def reset(self):
#         self.value = 0


# count = Counter(3)

# count.increment()
# print(count.value)

# count.decrement()
# print(count.value)

# count.reset()
# print(count.value)

'''
Task: BankAccount class

Create a class that:
stores:
owner name
balance
methods:

deposit(amount)
withdraw(amount)
get_balance()

Rules:
You cannot withdraw more than the balance
If invalid, print "Insufficient funds"
'''
# class Bank_account():
#     def __init__(self,owner_name,balance):
#         self.owner_name=owner_name
#         self.balance=balance
#         self.total=[]
#         self.deposit()
    
#     def deposit(self):
#         while True:
#             amnt=input("enter deposit amnt")
#             if amnt=="done":
#                 break
#             amnt=int(amnt)
#             self.total.append(amnt)
#         if sum(self.total)>self.balance:
#             print("you can't withdraw more than the balance")
#         else:
#             print("you can withdraw that amount")

# bank=Bank_account("rishka",3000)




#improved version
# class Bank_account():
#     def __init__(self,owner_name,balance):
#         self.owner_name=owner_name
#         self.balance=balance
#         self.listdep=[]
        
#     def deposit(self):
#         num=int(input("pls enter how many deposits u want to keep"))
#         for i in range(num):
#             deposit = int(input("pls enter your deposits"))
#             self.listdep.append(deposit)
#             self.update_balance(deposit)
#         self.withdraw()
        
#     def update_balance(self,deposit):
#         self.balance+=deposit
#         print(f"balance is {self.balance}")
        
#     def withdraw(self):
#         while True:
#             lmk=input("pls enter how much u wanna withdraw:")
#             if lmk=="done":
#                 break
#             lmk=int(lmk)
#             if lmk > self.balance:
#                 print("You cannot withdraw more than the balance")


# bank=Bank_account("rishka",30)
# bank.deposit()

'''
when counting in dictionary:
self given qs to understand more 09/01:
Write a program that:

asks the user to enter words one by one

stops when the user enters "done"

stores how many times each word appears using a dictionary

prints the final dictionary
'''
# full_count={}
# while True:
#     user=input("pls enter words one y one")
#     if user == "done":
#         break 
#     if user not in full_count:
#         full_count[user]=1
#     else:
#         full_count[user]+=1

# for name,count in full_count.items():
#     print(f"{name}:{count}")

'''
Q2. Movie Rating Tracker

Goal: dictionary values that are lists

Create a class MovieRatings with:
ratings → dictionary of movie_name : list_of_ratings

Tasks:
Add a movie with an empty list
Add multiple ratings for a movie (stop at -1)
Ensure ratings are between 1 and 5
Print each movie’s average rating
'''

# class Movieratings():
#     def __init__(self):
#         self.movie_name={}
    
#     def add(self,movie):
#         self.movie_name[movie]=[]

#     def multiple(self,movie):
#         while True:
#             user=int(input("pls enter ratings"))
#             if user==-1:
#                 break
#             if user>=1 and user<=5:
#                 self.movie_name[movie].append(user)
#             else:
#                 print("only enter no listed above")
        
#         for movie,rating in self.movie_name.items():
#             ave=sum(rating)/len(rating)
#             print(f"for movie {movie} the average ratings were {ave}")
    
# movie1=Movieratings()
# movie1.add("narnia")
# movie1.multiple("narnia")


'''
Q3. User Profile System

Goal: nested dictionaries

Create a class UserProfiles with:

users → dictionary structured as:

{
  "alice": {"age": 20, "city": "Berlin"},
  "bob":   {"age": 22, "city": "Paris"}
}


Tasks:

Add a user with age and city

Update a user’s city

Print all user profiles using a for loop

'''
# class Userprofiles():
#     def __init__(self):
#         self.names={}
    
#     def things(self):
#         while True:
#             name=input("pls enter names")
#             if name=="done":
#                 break
#             self.names[name]={}
#             age=int(input("pls enter your age"))
#             city=input("pls enter your city")
#             self.names[name]= {"age":age,
#                               "city":city
#                               } 
        
#         for name,values in self.names.items():
#             ask=input("are u still living in this city?")
#             if ask=="no":
#                 new_city=input("then tell me where r u living now:")
#                 self.names[name]["city"]=new_city
        
#         for name,values in self.names.items():
#             print(f"user {name} is {values['age']} years old and lives in {values['city']}")

# user=Userprofiles()
# user.things()


'''
Q4. Order Management System

Goal: understand structure choice
Create a class OrderManager with:
orders → list of dictionaries, each containing:
"order_id"
"product"
"price"

Tasks:
Add new orders
Display all orders
Calculate total revenue
'''
# class ordermanager():
#     def __init__(self):
#         self.orders=[]
    
#     def order(self):
#         while True:
#             order_id=int(input(f"pls enter ID"))
#             if order_id==-1:
#                 break
#             product=input("pls enter name of product")
#             price=int(input("pls enter your price"))


#         ord= [{"orderid":order_id, 
#                        "product":product,
#                        "price":price
#                        }]
#         self.orders.append(ord)
#         print(self.orders)

#         for items in self.orders.items():
#             items['price']+=price
#             print(f"the total price is {items['price']}")

# order1=ordermanager()
# order1.order()

'''
Q5. Attendance Tracker

Goal: safely handle missing keys

Create a class Attendance with:

records → dictionary of student_name : days_present

Tasks:
Mark attendance (increment count)
If student doesn’t exist, add them
Display all attendance records

'''
# class records():
#     def __init__(self):
#         self.attendance={}
    
#     def students(self):
#         while True:
#             student=input("pls enter your name")
#             if student == "done":
#                 break
#             if student in self.attendance:
#                 continue 
#             else:
#                 self.attendance[student]=0
        
#             count=0
#             days="mon","tues","wed","thurs","fri"
#             for i in range(len(days)):
#                 user=input(f"did you go to school on {days[i]}?")
#                 if user=="yes":
#                     count+=1
#                 self.attendance[student]=count
#             print(self.attendance) 
            
#         for person,days in self.attendance.items():
#             print(f" student {person} attended school for {days} days")


# record1= records()
# record1.students()

# class records():
#     def __init__(self):
#         self.attendance={}
    
#     def students(self):
#         while True:
#             student=input("pls enter your name")
#             if student == "done":
#                 break
        
#             count=0
#             days="mon","tues","wed","thurs","fri"
#             for i in range(len(days)):
#                 user=input(f"did you go to school on {days[i]}?")
#                 if user=="yes":
#                     self.attendance[student]=self.attendance.get(student,0)+1
#             print(self.attendance) 
            
#         for person,days in self.attendance.items():
#             print(f" student {person} attended school for {days} days")


# record1= records()
# record1.students()

'''
Create a class GradeAnalyzer with:

grades = {
  "A": 0,
  "B": 0,
  "C": 0,
  "F": 0
}
Tasks:
Input scores until -1
Categorise into A/B/C/F
Display grade counts
'''
class Gradeanalyser():
    def __init__(self):
        self.grades={}
    
    def review(self):
        name=input("pls enter subject")
        self.grades[name]=  {"A":0,
                             "B":0,
                             "C":0,
                             "D":0,
                             "F":0} 
        while True:
            scores=int(input("pls enter your score:"))
            if scores==-1:
                break
            if scores>80:
                self.grades[name]['A']+=1
            if scores>70:
                self.grades[name['B']]+=1
            if scores>60:
                self.grades[name]['C']+=1
            if scores>50:
                self.grades[name]['D']+=1
            if scores<50:
                self.grades[name]['F']+=1
        
        for subject,grades in self.grades.items():
                print(f"for subject {subject}, the students grades were {grades}")

            
grade1=Gradeanalyser()
grade1.review()
