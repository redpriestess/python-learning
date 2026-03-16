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

'''

class Animal():
    def __init__(self,name,breed,diet):
        self.name=name
        self.breed=breed
        self.diet=diet 
        
    def describe(self):
        print(f"{self.name},breed:{self.breed},diet:{self.diet}")
    
    def collectinfo(self):
        self.name=input("pls enter name of animal")
        self.breed=input("pls enter its breed:")
        self.diet=input("pls enter animal diet")

class Cat(Animal):
    def __init__(self,name,breed,diet,no_braincells,fur_color):
        super().__init__(name,breed,diet)
        self.no_braincells=no_braincells
        self.fur_color=fur_color
    
    
    def describe(self):
        print(f"Cat {self.name}:breed{self.breed},diet:{self.diet},no.brain cells: {self.no_braincells},fur_color:{self.fur_color} ")
    
    def collectinfo(self):
        super().collectinfo()
        self.braincells=input("pls enter no.braincells:")
        self.fur_color=input("pls enter fur colour:")
    
    def update(self):
        if self.name in animals:
            new_braincells=input("pls enter new no of braincells")
            animals[animal_name].no_braincells=new_braincells
        else:
            print(f"that animal isnt here")


class dog(Animal):
    def __init__(self,name,breed,diet,pedigree, rabies_vaccinated):
        super().__init__(name,breed,diet)
        self.pedigree=pedigree
        self.rabies_vaccinated= rabies_vaccinated
    
    def describe(self):
        print(f"dog {self.name}:breed{self.breed},diet:{self.diet},pedigree: {self.pedigree}, rabies_vaccinated:{self.rabies_vaccinated} ")
    
    def collectinfo(self):
        super().collectinfo()
        self.pedigree=bool(f"Is {self.name} a pedigree: enter True/False")
        self.rabies_vaccinated=bool(f"Is {self.name} rabies vaccinated, enter True/False")
    
    def update(self):
        if self.name in animals:
            new_diet=input("pls enter new diet")
            animals[animal_name].diet=new_diet 
        else:
            print(f"that animal isnt here")

print("Hey there!")
options=["view animals","register animals","modify animal","quit"]
animals={}

while True:
    for i,value in enumerate(options):
        print(f"{i+1}:{value}")

    user=int(input("pls enter which option you want:")) ##h
    choice=options[user-1]
    if choice == 1:
        for name,things in animals:
            print(f"{name}:{things}")
        
    elif choice== 2:
        animaltype = input("pls enter animal type")
        if animaltype == "dog":
            animal=dog()
            dog.describe()
        if animaltype == "cat":
            animal=Cat()
            Cat.describe()
        animal_name= input("pls enter animal name:")
        animals[animal_name]=animal 
        
    elif choice==3:
        animal.update()
    elif choice==4:
        print("you have quit the programme")
        break
    
            

