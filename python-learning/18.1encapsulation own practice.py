'''
🟡 LEVEL 2 — Medium
4️⃣ Bank Account (Like Your Example 🏦)

Create a class BankAccount with:

_balance

getter: get_balance() → only show balance if password is correct

setter: set_balance(amount) → only allow balance < 10,000

💡 Task:

Create an account with balance 5000.

Try changing the balance to 20,000 (should fail).

# '''

# class BankAccount():
#     def __init__(self,balance,pwd):
#         self.balance=balance
#         self.pwd=pwd #hardcode the password PER account
        
#     def balances(self,pwd):
#         # def balances(self,pwd):if keep like this, all accounts will have same password
#         # pwd=pls enter your password
#         amount=input("pls enter the password")
#         if amount == self.pwd:#this is done to check if password hardcoded n password entered matches
#             return self.balance 
#         else:
#             return "scram noob"
#     def setbalance(self,newbalance):
#         if newbalance<10000:
#             self.balance=newbalance
#         else:
#             print("only less than 10,000")

# account1=BankAccount(234,"malaysia")
# account1.balances()
'''
Create a class GameCharacter with:

_health (starting at 100)

Getter:

get_health() → returns health.

Setter:

set_health(new_health):

If new_health > 100 → set to 100

If new_health < 0 → set to 0

💡 Task:

Try setting health to 150 and -20.
'''
# class GameCharacter():
#     def __init__(self):
#         self._health=100
#     def get_health(self):
#         return self._health 
#     def set_health(self,new_health):
#         if new_health>100:
#             self._health=100
#         elif new_health>0:
#             self._health=new_health 
#         elif new_health<0:
#             self._health=0
        
# aryan=GameCharacter()
# print(aryan.get_health())
# aryan.set_health(20)
# print(aryan.get_health())


'''
Create an enum AccountStatus:

ACTIVE

SUSPENDED

CLOSED

Then create a class BankAccount with:

_status (use the enum!)

Getter:

get_status() → returns status.

Setter:

set_status(new_status) → only allow valid enum values.

💡 Task:

Set status to ACTIVE.

Try setting status to something invalid like "HACKED".
'''

# class Status:
#     ACTIVE = "active"
#     SUSPENDED = "suspended"
#     CLOSED = "closed"

# print(Status.poop)









'''

            DATA MODEL
CLASSES, OBJECTS, METHODS AND ATTRIBUTES
Create an animal class. 
It should have attributes such as name, breed, diet
it should have a method that describes the animal (just print a senteence like "Tommy is a cat that meows")

Create a cat and a dog object. 
Call the describe methods of each object

---------------------------------
INHERITANCE
Dogs will have a pedigree (bool), rabies_vaccinated (bool)
Cat will have number_of_brain_cells (int), fur_color(str)

Create two subclasses from the Animal class
and create cat and dog objects from those classes
---------------------------------------

PROGRAM BEHAVIOUR 

You are an application for vetenerary clinic management system (VCMS)
When the program starts, greet the user
Show below actions and the choice from the user and execute the correct action. if the user provides an invalid input
print an appropriate error messge and the show the options again. this shouold on repeat until the user decides to quit. 

1. View Animals
        - should list all animals registered in the clinic
2. Register animal 
        - Should collect information based on the type of animal and then create a new animal entry
3. Modify Animal 
        - Should show list of availble animals and then start modifying it
4. Quit

- classes, objects, methods and attributes
- init method, self
- inheritance 
- polymorphism

- encapsulation (getters, setters)
- has-a-relationship
- abstraction 

- libraries, virtual enviroments
- file manipulation (read from and write to files)
-----------------------------------------------------


'''
# class Animal():
#     def __init__(self,name=None,breed=None,diet=None):
#         self.name=name
#         self.breed=breed
#         self.diet=diet 
    
#     def collectinfo(self):
#         self.name=input("pls enter your name:")
#         self.breed=input("pls enter your breed:")
#         self.diet=input("pls enter your diet:")
    
#     def describe(self):
#         print(f"{self.name} is breed {self.breed} and it's diet is {self.diet}")
    
#     def modifyanimal(self):
#         newdiet=input("pls enter new diet")
#         self.diet=newdiet

# class Dogs(Animal):
#     def __init__(self,name=None,breed=None,diet=None,pedigree=None,rabiesvaccine=None):
#         super().__init__(name,breed,diet)
#         self.pedigree=pedigree
#         self.rabiesvaccine=rabiesvaccine
    
#     def collectinfo(self):
#         super().collectinfo()
#         self.pedigree=bool(input("is this dog a pedigree?:"))
#         self.rabiesvaccine=bool(input("is this dog rabies vaccinated?:"))
    
#     def modifyanimal(self):
#         super().modifyanimal()
#         rabiesvaccineupdate=input("is the dog vaccinated now?")
#         self.rabiesvaccine=rabiesvaccineupdate
    
#     def describe(self):
#         super().describe()
#         print(f"{self.name} is breed {self.breed} and it's diet is {self.diet}, pedigree:{self.pedigree}, rabiesvaccine:{self.rabiesvaccine}")
    
    
# class Cat(Animal):
#     def __init__(self,name=None,breed=None,diet=None,nobraincells=None,furcolor=None):
#         super().__init__(name,breed,diet)
#         self.nobraincells=nobraincells
#         self.furcolor=furcolor
    
#     def collectinfo(self):
#         super().collectinfo()
#         self.nobraincells=input("how many brain cells does this cat have?:")
#         self.furcolor=input("what is the cat furcolor?:")

#     def describe(self):
#         super().describe()
#         print(f"{self.name} is breed {self.breed} and it's diet is {self.diet}, nobraincells:{self.nobraincells}, furcolor:{self.furcolor}")
    

# print("hey girl")
# options=["register animals","view animals","modify animal","quit"]
# animallist={}
# while True:       
#     for i,option in enumerate(options):
#         print(i+1,option) 
#     user=int(input("pls enter which option u want to pick:"))
    
#     if user==1:
#         animaltype=input("pls enter animal type:")

#         if animaltype == "cat":
#             cat1=Cat()
#             cat1.collectinfo()
#             animallist[cat1.name]=cat1

#         elif animaltype=="dog":
#             dog1=Dogs()
#             dog1.collectinfo() 
#             animallist[dog1.name]=dog1 

#     if user==2:
#         for name,info in animallist.items():
#             info.describe()
    
#     if user==3:
#         animalname=input("pls enter animal name")
#         if animalname in animallist:
#             animallist[animalname].modifyanimal()
    
#     if user==4:
#         print("goodbye")
#         break












