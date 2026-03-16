from pprint import pprint
class House:
    def __init__(self,br=6,bath=2,doors=3,windows=4,hasOpenKitchen=False):
        self.br=br
        self.bath=bath
        self.doors=doors
        self.windows=windows
        self.hasOpenKitchen=hasOpenKitchen
        print('I am buildingggggggg')
    
    def describe_house(self):
        print(f"This house has {self.br} bed rooms, {self.bath} bathrooms, {self.doors} doors and {self.windows} windows")
        if self.hasOpenKitchen:
            print("This house has open kitchen as well")
            
    def check_for_open_kitchen(self):
        if self.hasOpenKitchen:
            return True
        else:
            return False
        
        
house1=House()
house2=House(3,1,2,3)
house3=House(3,1,2,3,True)

# if house3.check_for_open_kitchen():
#     print("house 3 has open kitchen")
    
    
# houses=[]
# for i in range(500):
#     house_object=House()
#     house_object.describe_house()
#     houses.append(house_object)
     
# print(house1.doors)
# print(house2.hasOpenKitchen)
# print(house3.hasOpenKitchen)

# implementing same thign using dictionary 

# hasopenKitchen=False

# houses_dict_list= {'house1':{'br':4,'bath':2,'doors':3,'windows':4},
#          'house2':{'br':3,'bath':1,'doors':2,'windows':3},
#          'house3':{'br':3,'bath':1,'doors':2,'windows':3,'hasopenKitchen':True}
# }

# house_id=0
# for i in range(500):
#     houses_dict_list[f"house{house_id}"]={'br':4,'bath':2,'doors':3,'windows':4,'hasOpenKitchen':False}
#     house_id+=1    

# # print(houses['house3']['hasopenKitchen/'])
# pprint(houses_dict_list)


# for house_id,house in houses_dict_list.items():
#     house['br']=6

'''
🔹 Task: Create a Person class

1️⃣ Create a class called Person

2️⃣ The __init__ method should take:
name
age
country and store them using self

3️⃣ Create a method called introduce() that:
prints:"Hi, my name is ___, I am ___ years old and I am from ___."

4️⃣ Create a method called is_adult() that:
returns True if age is 18 or above otherwise returns False

5️⃣ Create two Person objects:
one adult, one under 18

6️⃣ Call both methods on both objects
'''

class person:
    def __init__(self,name,age,country):
        self.name=name
        self.age=age
        self.country=country
        self.introduce()

    def introduce(self):
        print(f"Hi,my name is {self.name}, i am {self.age} years old and i am from {self.country}")
        print(self.is_adult())
    
    def is_adult(self):
        if self.age>=18:
            return True
        else:
            return False

person1= person("rishka",21,"Malaysia")
person2=person("aryan",23,"Malaysia")

def things(name,age,country):
    print(f"Hi my name is {name}, my age is {age}, country is {country}")

things("Rishka",21,"Malaysia")
things("Aryan",23,"Malaysia")