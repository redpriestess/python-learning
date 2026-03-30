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

            
# grade1=Gradeanalyser()
# grade1.review()



'''
You are a programmer building a simple payroll management tool for a small company. Your task is to create various functions to automate payroll calculations. 
This problem will test your understanding of Python functions, parameters, default arguments, return statements, and handling multiple arguments.

1. Write a simple function called welcome_employee that takes no parameters and prints "Welcome to our company!".
2. Create a function called employee_greeting that takes one parameter called employee_name with a default value of 'Employee'.
 It should print a greeting message like "Hello Employee!".

3. Define a function named calculate_hourly_wage that accepts two parameters: hours_worked and hourly_rate. 
The function should calculate the total wage (hours multiplied by rate) and print the result.

4. Now modify the calculate_hourly_wage function to return the calculated wage instead of printing it.

5. Implement a function total_monthly_payroll that accepts a list of employee wages and returns the total payroll amount using the previously defined wage 
calculation function. Do not use any built-in Python functions except print().

6. Write a function named calculate_bonus with parameters salary and an optional parameter bonus_percentage defaulting to 5%.
 The function should return the bonus amount calculated on the salary.

7. Create a function total_expenses that can accept any number of expense amounts (variable number of arguments) and returns their sum.

8. Define a function employee_details that takes two keyword arguments, name and department, and prints the details in the format 
"Employee [name] works in the [department] department."

9. Lastly, create a flexible function employee_record that accepts any number of keyword arguments and prints the employee's full information as a dictionary.

Demonstrate each of these functions with appropriate calls.
'''
def welcome_employee():
    print("welcome to our company")

def employee_greeting(employee_name="employee"):
    print(f"hello {employee_name}")

def calculate_hourly_wage(hours_worked,hourly_rate):
    total_wage=hours_worked*hourly_rate 
    return total_wage  

total= [calculate_hourly_wage(34,98),
        calculate_hourly_wage(89,98)] 

# data= [(34,90),(77,90)] 
# for hours,rate in data:
#     print(calculate_hourly_rage(hours,rate))

def total_payroll(employee_wages): 
    count=0
    for number in employee_wages:
        count+=number 
    print(f"total monthly payroll is {count}") 

total_payroll(total) 

def calculate_bonus(salary,bonus_percentage=5):
        discount=(bonus_percentage/100)*salary
        return discount 

calculate_bonus(56,9)

def total_expenses(*args):
    total=sum(args) 
    return total 

total_expenses(56,44,556,33,44,55)

def employee_details(**kwargs):
    for key,name in kwargs.items():
        print(f"{key}:{name}")


employee_details(name="rishka",age=22,employed=2026,salary=6000)


def deets(**kwargs):
    print(kwargs)

deets(name="rishka",age=22,employed=2026,salary=6000) 




'''

----------------------------------------------------------------------------------------------

You are developing a program for a cinema theater that allows users to reserve movie tickets.
 This task tests your understanding of functions, conditional statements, loops, lists, and getting user input in Python.

1. Movie selection
   Create a function called select_movie that performs the following tasks:

* Stores a list of available movies: 'Oppenheimer', 'Barbie', 'Mission Impossible', and 'Spider-Man'.
* Displays the movies with numbers to the user and asks them to select a movie by entering a number.
* Uses an if condition to validate the user's choice. If the choice is invalid, inform the user and ask again until a valid movie is selected.
* Return the selected movie name.

2. Seat selection
   Define another function called choose_seats that:

* Accepts the selected movie name as an input parameter.
* Creates a list of available seat numbers from 1 to 10.
* Continuously prompts the user to choose seat numbers, each time verifying with an if condition if the seat is available.
* Once a seat is selected, remove that seat number from the available seats list.
* Use another if condition to stop taking seat reservations when the user has booked 3 seats or when the user types 'done'.
* Return the list of booked seats.

3. Booking summary
   Define a third function called booking_summary that:

* Accepts two parameters: the selected movie name and the list of booked seats.
* Uses a for loop to neatly display each booked seat number.
* Prints a summary statement showing the movie chosen and all reserved seats.

Finally, call these three functions sequentially in your main program to run the cinema ticket reservation system.

'''
def select_movie():
    movies=["barbie","oppenheimer","mission imp","spiderman"]
    for i in range(len(movies)):
        print(f"{i+1}:{movies[i]}") 
    user=input("pls enter a number:")
    num=int(user)
    if 1<=num<=len(movies): 
        print(f"you have selected {movies[num-1]}")
    return movies[num-1]
def seats(place):
    seats=[1,2,3,4,5,6,7,8,9,10]
    total=[]
    while True:
        user=input("pls pick a seat number")
        if user=="done":
            break
        inted=int(user)
        if inted in seats:
            total.append(inted)
            seats.remove(inted)
        print(f"Total number of seats is {total}")
    return total
def booking_summary(name,seats):
    for seat in seats: 
        print(f"movie {name} has seats: {seat} selected")
   
# movie=select_movie()
# seat=seats(movie)
# booking_summary(movie,seat) 

'''
---------------------------------------------------------------

You're building a simple warehouse inventory system for a small business. 
The system should allow the user to add items, remove items, and view current stock. 
This problem requires you to break the logic into interconnected functions, where one utility function is reused multiple times across the program.
 You'll practice functions, lists, conditionals, loops, and user input.

1. Core utility function: find_item
   Create a function find_item(item_name, inventory) that:

* Accepts an item_name (string) and an inventory (list of dictionaries).
* Searches for the item in the inventory list. Each item in the list is a dictionary with 'name' and 'quantity'.
* If found, returns the dictionary object.
* If not found, returns None.

2. Add or update inventory: add_item
   Define a function add_item(inventory) that:

* Prompts the user to enter the name and quantity of an item to add.
* Calls find_item to check if the item already exists:

  * If it does, increase its quantity.
  * If not, add it as a new dictionary to the inventory list.
* Repeat the process until the user types 'done'.
'''
inventory_list=[{"name":"rishka","stock":3},{"name":"car","stock":5}]

def find_item(name,inventory):
    for things in inventory:
        if things["name"]==name:
            return things #i returned name
        else:
            return None


def add_item():
    while True: 
        user=input("pls enter item:")
        if user=="done":
            break 
        amount=int(input("pls enter how much stock is present:")) 
        existing_item=find_item(user,inventory_list)

        if existing_item:
            existing_item["stock"]+=amount 
            print(f"updated amount, {existing_item}") #didntkeepearlier

        else:
            updated_item={"name":user,"stock":amount} 
            inventory_list.append(updated_item) 
            print(f"updated new item:{updated_item}")

add_item() 


