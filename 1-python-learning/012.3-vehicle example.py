'''
Create a vehicle example with attributes like model, make, year, milage

create a method that will start the car (simply print 'brrrmmmm')
create a metho that will drive the car a certain distance (this should increse the milage by the amout of miles driven )
create a method that will check if service is needed ( service is needed after 5000 miles)

'''

class vehicle():
    def __init__(self,model,make,year,milage):
        self.model=model
        self.make=make 
        self.year=year
        self.milage=milage
        
    def start(self):
        print("brrm")
    
    def drive(self,amount):
        self.milage+=amount 
        print(f"the car has {self.milage} amount of milage")

    def service(self):
        if self.milage>5000:
            print("service is needed") 

# vehicle1=vehicle("bmw","X5",2022,9000)
vehicle1.drive(222)
# vehicle1.service()

def add_numbers(num1,num2):
    print(num1+num2)
    
add_numbers(3,6)



