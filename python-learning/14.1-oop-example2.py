'''
A library has different types of books (fiction, fantasy, horror)
Each book has title, author, isbn 

Implement seperate description methods for each type of book 
'''

# class Book:
#     def __init__(self,title,author,isbn):
#         self.title=title
#         self.author=author
#         self.isbn=isbn
        
#     def borrow(self,borrower):
#         print(f"{self.title} has been borrowed by {borrower}")
        
#     def return_book(self,borrower):
#         print(f"{self.title} has been returned by {borrower}")
        
#     def describe(self):
#         print(f"The {self.title} is a book written by {self.author} which has an isbn of {self.isbn}")
        
# class horror(Book):
#     def __init__(self,title,author,isbn,horror_category):
#         super().__init__(title,author,isbn)
#         self.horror_category=horror_category
    
#     def describe(self):
#         super().describe()
#         print(f"Horror category is {self.horror_category}")
        
    


# hp1=Book("Harry Potter and the sorceres stone",'JK Rowling',88559494)
# hp1.describe()

# shining=horror('The shining','Stephen King',392993929,'Haunting')
# shining.describe()

'''
INHERITANCE QS CHATGPT :

A small animal clinic wants to store information about pets.
Create a class called Animal with attributes for name and age.
Add a method that prints a short description of the animal.
Ask the user to enter details for one animal.
Use an if condition to check if the animal is older than 5 years and print an extra message if true.
Store the created object inside a list and print its details by calling the method.
'''
# class Animal():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def summary(self):
#         print(f"the name of the animal is {self.name} and age is {self.age}")
#         if self.age>5:
#             print(f"animal {self.name} is more than 5 years old")
    
# name=input("pls enter your name")
# age=int(input("pls enter the age of the animal"))

# animal1=Animal(name,age)

# ages=[]
# ages.append(animal1)

# for animal in ages:
#     animal.summary()
        
'''
A pet shop wants to separate dogs and cats.
Create a base class Animal with name and sound attributes.
Create two child classes Dog and Cat that inherit from Animal.
Each child class should override a method that prints the sound the animal makes.
Ask the user how many animals they want to add.
Use a while loop to collect animal type and details.
Store all objects in a list.
Use a for loop and if conditions to call the correct sound method for each animal.

'''
# class Dog(Animal):
#     def animal_noise(self):
#         print(f"{self.name} barks!")
        
# class Cat(Animal):
#     def animal_noise(self):
#         print(f"{self.name} meows!")

# count= int(input("pls enter how many animals u wanna enter:"))
# animals=[]
# i=0
# while i<count:
#     species=input("pls enter if it is a cat or dog")
#     name=input("pls enter name")
#     age=int(input("pls enter its age"))

#     if species=="dog":
#         animals.append(Dog(name,age))
#     elif species=="cat":
#         animals.append(Cat(name,age))
#     i+=1 

# for animal in animals:
#     animal.animal_noise()




'''
A zoo management system tracks different animals and their food habits.
Create a base class Animal with a method get_diet.
Create child classes Herbivore and Carnivore that override get_diet with different behavior.
Store several animal objects in a list.
Create a dictionary where keys are animal names and values are tuples containing animal type and diet.
Use a for loop to populate the dictionary.
Use if conditions to print a warning if any carnivore is found.

'''

# class Animal():
#     def __init__(self,name):
#         self.name=name        
#     def get_diet(self):
#         print(f"all animals like {self.name} need to eat their own food")
    
# class Herbivore(Animal):
#     def get_diet(self):
#         return "eats plants"

# class Carnivore(Animal):
#     def get_diet(self):
#         return "eats meat"

# animalthings=[]
# i = 0
# count=int(input("pls enter how many animals u r gonna type"))
# while count>i:
#     name=input("pls enter animal name") 
#     animaltype=input("pls enter type of the animal:")

#     if animaltype == "herbivore":
#         animalthings.append(Herbivore(name))
#         i+=1
#     elif animaltype == "carnivore":
#         animalthings.append(Carnivore(name))
#         i+=1

# animalsummary={}
# for animal in animalthings:
#     if isinstance(animal,Herbivore):
#         animaltype="herbivore"
#     elif isinstance(animal,Carnivore):
#         animaltype="carnivore"
#         print("careful, issa carnivore")

#     diet=animal.get_diet() 
#     animalsummary[animal.name]=(animaltype,diet)
# print(animalsummary)



