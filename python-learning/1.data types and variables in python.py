
# #single line comment 

# '''
# The first line of a multiline comment
# This is second line
# '''

# name = 'Jonathan' #string (str)- names, locations, sentences 
# age = 34 # integer (int)- 10,1,0,1000000,-67
# weight = 65.5 # floating point numbers (float) - 10.56,-98.5,0.000012, 1.0
# hasPet = False # Boolean (bool)- To represent variables with only two outcomes 
# petName = None # None type variable (None)- to represent nothingneses, create references for empty variables

# # Use the above primitive data types to describe anything you want

name = "Lady Gaga"
age = 98
weight = 52.789
hasPet = True
petName = "Bella" 

# print(name)
# print(name,age)

# #I met a person called riri and they are 98 years old
# #1. string concatenation 
# print("Hello world!")
# print("I met a person called "+ name + " and they are " + str(age) + " years old")

#I met a sweet friend called riri who vibes with me so well she is 98 years old and weighs 900.789 kgs
print("I met a sweet friend called "+name+" who vibes with me so well she is "+str(age)+" and weighs "+str(weight)+" kgs")

#I met a sweet friend called riri who weighs 900.789 kgs who has a pet called riri2
print("I met a sweet friend called "+petName+" who weighs "+str(weight)+" kgs who has a pet called "+name)

#f- strings 
print(f"I meet a sweet friend called {petName} who weights {weight} kgs who has a pet called {name}")

'''
VARIABLE NAMING RULES IN PYTHON 

1. You cannot have spaces in your variable name 
The big red car- invalid variable name 
Thebigredcar- valid (but hard to read)

VARIABLE NAMING CONVENTION
the_big_red_car - snake case (variable naming)
TheBigRedCar - Pascal case (Class naming)
theBigRedCar- Camel case (variable naming)

2. Cannot start with a number. There can be a number from the second character and onwards. 
2pp- invalid
p2p- valid

3. Allowed characters are a-z, A-Z, 0-9, _

4. Cannot have reserved keywords in python. 
Eg: Str, Float, Int, Bool, None, print, for, in, while, do, class, def, True, False

5. Only start variable with a _ for special purpose (private variables)- OOP

EXERCISE: Mark invalid variable names and mention why they are invalid

userName 
2nd_place (start w number)
total$amount (this symbol is not allowed)
final_score
employee-name (not allowed)
_hiddenValue 
while - not allowed (type of a loop in python)
MAXSPEED 
pi_3.14 - (. is not allowed)
first name (have space)
student_123
True(not allowed)
__private_var- mangled name in python
discount% (symbol not allowed)
myVariable

'''

#getting user input 
# name=input('Please enter your name: ')
# print(f"Hello {name}")

#Get the name, item price and item count from the user. print the statment
# "Hello John, you final bill is 45 USD" (the final bill is item_count x item_price)

name=input('please enter your name: ')
item_count=int(input("Please enter the number of items you purchased: "))
item_price=int(input("Please enter the item price"))
print(f"Hello, {name} your final bill is {item_count*item_price} USD")

'''
#----------------------------------------- HOMEWORK 1 -------------------------------------------------------

Ahmed manages patient records at a local clinic and wants to create a simple program to track patient details such as name, age, body temperature, gender, and cancer history. He plans to use Python variables and data types effectively to store patient information.

1. Define a variable named 'patientName' and store the name 'Alice' in it. Which Python data type will you use for this?
patient_name = "Alice",str

2. Create a variable named 'patientAge' to store Alice's age, which is 27 years. What data type is appropriate here?
patient_age = 27 , Int

3. Alice's body temperature was measured at 38.3 degrees Celsius. Store this in a variable called 'bodyTemperature'. Identify the suitable data type.
body_temperature = 38.3 , float

4. Create a variable named 'isFemale' to indicate Alice's gender as True or False. What Python data type fits here?
is_female = True , Boolean

5. The clinic records a patient's cancer history, which might not always be known immediately. Initialize a variable named 'cancerHistory' to indicate the history is currently unknown. What special Python value should you use?

6. Ahmed created a variable named '2patient' but received an error. Explain why this variable name is invalid based on Python variable naming rules, and suggest a valid alternative.
He started the variable with a number so python did not recognise it, swap it to patient2 instead, start it with a word NOT number

7. Ahmed is deciding between using 'patient_health_data', 'PatientHealthData', and 'patientHealthData' to store general patient information. Which naming convention is best suited for a regular variable according to Python best practices?
patient_health_data

name = input("enter patient's name:")
patient_age = int(input("Please enter patient age:"))
body_temp = float(input("Please enter patient body temp:"))
gender = input("Please enter patient gender(Male/Female)")
cancer_history = input("please enter if your history is known or not:" )
print(f"Patient name {name} is {patient_age} years old who has a body temperature of {body_temp} who is a {gender} and has a cancer history which is {cancer_history}")
'''

patient_name='Alice' #str

'''

------------------------- HOMEWORK 2 -----------------------------

Sarah runs a weather station at her home and records data such as daily temperature, rainfall amount, humidity levels, and whether it rained that day. She wants to create a Python program to manage this data effectively using variables and data types.

1. Sarah recorded today's temperature as 29.7 degrees Celsius. Which data type should she use for the variable 'todayTemperature'?
float

2. She measured today's rainfall as 5 millimeters. What is the best Python data type to store the value of 'rainfallToday'?
int

3. Sarah wants to note whether it rained today. Create a variable 'didRain' to store this information. What Python data type is most suitable?
string

4. Sarah tries to define a variable named 'rain fall', but Python gives an error. Explain why this variable name is invalid according to Python naming rules, and suggest a valid alternative.
There is a space between rain and fall, remove the space and it'll work

5. Sarah wants to store a description for today's weather, 'Partly cloudy with a chance of rain'. Which Python data type should she use for the variable 'weatherDescription'?
str

6. She initializes a variable named 'humidityLevel' with the value None because her humidity sensor is currently broken. Explain what 'None' signifies in Python and why Sarah might use it here.
Since her humidity sensor is broken there will be no value for humidity.

today_temperature = float(input("What was the temperature today?:"))
today_rainfall = int(input("How much rainfall was there today?: "))
rain = input("Did it rain today?: ")
print(f"Today's temperature was {today_temperature} degrees it {rain} and the rainfall was {today_rainfall} mm")


---------------------------- HOMEWORK 2 ----------------------------

Question: Coffee Shop Inventory Tracker

1. You need to store information about a coffee menu item: its name, price per cup, whether it is in stock, and the number of cups sold today. For each piece of information, choose an appropriate variable name and data type, then assign it a sample value (for example: “Espresso”, 2.50, True, 85).

coffee_name = "caramel frappucino"  
# #str
price_per_cup = 16
# #int
in_stock = True
# #bool
sold_today = 20
# #int

2. Write code that prints each variable’s value and its data type. You can get the data type using the type() function. 
For an instance: print(type(first_name)), will print the type of the variable.

print(type(coffee_name))
print(type(price_per_cup))
print(type(in_stock))
print(type(sold_today))


3. Later in the day, 15 more cups are sold. Update the cups-sold variable accordingly and print the new total.
You can modify and already defined variable in the same way you have defined it. For an instance"
age = 36
will update age from 34 to 36

sold_today = 35

4. The price of the item increases by 0.25. Update the price variable and print a message that shows the old price and the new price.

new_price_per_cup = 16.25
print(f"The old price of the cup was {price_per_cup}, but now it is {new_price_per_cup}")

5. Finally, change the in-stock flag to False and print a message indicating that the item is sold out.

in_stock = False
print("the item is sold out")

'''

This is how you name variables: words should have double quotes
name = "Lady Gaga"
age = 98
weight = 52.789
hasPet = True
petName = "Bella" 

Use #fstrings to print out different variables(string/integers) into a sentence
#using f- strings 
print(f"I meet a sweet friend called {petName} who weights {weight} kgs who has a pet called {name}")

Use #type to get the type of data it is:
print(type(first_name)), will print the type of the variable.

print(type(name))>string
print(type(age))>integer
print(type(hasPet))>boolean
print(type(weight))>float

#usingboolean
The correct way:
in_stock = input("Please enter if item in stock(yes or no)")
if in_stock == "yes":
    print("The item is in stock")
else:
    print("The item is sold out")

The WRONG way:
in_stock = input("Please enter if item in stock(yes or no)")
in_stock = True
if in_stock:
    print("The item is in stock")
else:
    print("The item is sold out")

WRONG no matter what user keeps, yes or no,python will print the item is in stock 
as we forced the condition to ALWAYS be true by equating THAT variable= true

