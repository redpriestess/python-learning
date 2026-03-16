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
#VET MANAGEMENT SYSTEM
class Animal():
    def __init__(self,name=None,breed=None,diet=None,heathHistory=None):
        self.name=name
        self.breed=breed
        self.diet=diet
        self.heathHistory=heathHistory
    def describe(self):
        return (f"{self.name} is an animal of which's breed is {self.breed} who eats {self.diet}")
    
    def name(self):
        return self.name 
    
    def breed(self):
        return self.breed 
    
    def diet(self):
        return self.diet 
    
    def set_name(self,new_name):
        if new_name.isnumeric():
            print("you can only enter name, not numbers")
            
    def set_health_history(self,disease):
        self.heathHistory.append(disease)
    
    def collect_info(self):
        self.name=input("pls enter its name:")
        self.breed=input("pls enter the breed:")
        self.diet=input("pls enter its diet:")
        
    def updates(self):
        self.name=input("Please enter the new name: ")
        self.breed=input("Please enter the new breed: ")
        self.diet=input("Please enter the new diet: ")


class Dog(Animal):
    def __init__(self,name=None,breed=None,diet=None,pedigree=None,rabies_vaccinated=None):
        super().__init__(name,breed,diet)
        self.pedigree=pedigree
        self.rabies_vaccinated=rabies_vaccinated
    def describe(self):
        return(f"{self.name}:dog, breed:{self.breed}, eats:{self.diet},pedigree : {self.pedigree}, vaccinated against rabies:{self.rabies_vaccinated}")
        
    def collect_info(self):
        super().collect_info()
        self.pedigree=bool(input("is it a pedigree dog ('True'/'False'): "))
        self.rabies_vaccinated=bool(input("is it vaccinated against rabies('True'/'False'): "))
        
class Cat(Animal):
    def __init__(self,name=None,breed=None,diet=None,no_brainscells=None,fur_colour=None):
        super().__init__(name,breed,diet)
        self.no_brainscells=no_brainscells
        self.fur_colour=fur_colour
    def describe(self):
        return(f"{self.name}:cat, breed:{self.breed}, eats:{self.diet},no_brainscells : {self.no_brainscells}, fur_colour:{self.fur_colour}")
    
    def collect_info(self):
        super().collect_info()
        self.no_braincells=input("pls enter the number of braincells:")
        self.fur_color=input("pls enter fur color:") 
    
    def updates(self):
        global animals_vet
        if name in animals_vet:
            new_braincells=input(f"pls enter new number of brain cells for {name}:")
            animals_vet[name].no_braincells=new_braincells 
            print("animal updated successfully")
        else:
            print("animal not found") 


Tom=Cat("Pitta","cat","cat food",4,"brown")
Pitta=Dog("Pitta","dog","dog food",True,False)
# Tom.describe()
# Pitta.describe() 


welcome_msg='''
************************************
 Vetenarary Clinic Management System
 ***********************************
 
          ,    /-.
         ((___/ __>
         /      }
         \ .--.(    ___
          \\   \\  /___\
    
-------------------------------------
'''

def get_int_choice(prompt,options):
    ''' Get a prmopt and a list options
    - reject any non numerical inputs
    - check if the user enters a valid input
        - If there are 3 options, user should enter a number between 1 and 3 
    - keep asking the user until they provide a valid answer or decide quit by entering quit
    '''
    while True:
        print(prompt)
        #print the options
        for i,option in enumerate(options):
            print(f"{i+1}. {option}")

        choice=input(f"Please enter your choice as a number between 1 and {len(options)}\nEnter 'quit' to go back: ")
        #check if a number
        if choice.isnumeric():
            choice=int(choice)
            if choice>0 and choice<=len(options):
                print(f"You chose [{options[choice-1]}]")
                return choice
            else:
                print(f"Your number must be between 1 and {len(options)}")
            
        else:
            if choice.upper()=='QUIT': 
                return 0
            else:
                print(f"your choice must be a number between 1 and {len(options)}")
        
        
print(welcome_msg)

main_menu_options=['Register Animal','List all animals','Modify Animal','Quit']
global animals_vet
animals_vet={}
while True:
    choice=get_int_choice('Please select an action from below',main_menu_options)
    print(choice)
    
    if choice == 1:
        animal_type=input("Pls enter animal type:")
            
        if animal_type=="dog":
            animal=Dog()
            animal.collect_info()
        
        elif animal_type == "cat":
            animal=Cat()
            animal.collect_info()
            
        else:
            print("Unknown animal type")
            continue 
        
        animals_vet[animal.name]=animal
        # <time_component_
        # <202601261149566757555858_mac_addres>
        print(f"{animal.name} registered successfully!")
    
    
    elif choice == 2:
        for name,data in animals_vet.items():
            print(data.describe())
    
    elif choice == 3:
        animal_to_update=input("please enter the name of the animal to update: ")
        if animal_to_update in animals_vet:
            animals_vet[animal_to_update].update()
        
    
    elif choice == 4:
        print("bye, thanks")
        break

        
        

        

