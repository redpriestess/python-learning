'''Gather scores that are between 0 and 100 from ther user continuously
Do this until the user enter 'done'
Once the user is done calculate the average of the responses

1. Get numbers from the user 
    1.1. use a while loop and an input function 
    1.2. check if number between 0 and 100 
`     1.2.1 reject if not 
      1.2.2 append to list if it is 
      
2. Get the average 
  2.1. get the sum 
  2.2. get the length 
  2.3. calculate average 
'''
# # def num_frm_user():
# #     num=[]
# #     while True:
# #         user_num = input("Please enter number:")
# #         if user_num == "done":
# #             break
# #         if user_num.isnumeric():
# #             user_num = int(user_num)
# #             if user_num>0 and user_num<100:
# #                 num.append(user_num)
# #             else:
# #                 print("only enter number frm 0-100")
# #         else:
# #             print("you can only enter numbers")
    
# #     print(num)
# #     return(num)

# # num_frm_user()

# # def num_average(rar):
# #     return sum(rar)/len(rar)

# # num_list = num_frm_user()
# # average_list = num_average(num_list)
# # print(f"{num_list}and {average_list}")
    


#improvedversion

# # def num_frm_user():
# #     user=[]
# #     while True:
# #         # user=[] #KEEP OUTSIDE LOOP OTHERWISE every time the loop repeats, it resets to an empty list again, so you’ll only keep the last number entered.
# #         num = input("pls enter number")
# #         if num=='done':
# #             break
# #         if num.isnumeric():
# #             # int(num) ONLY TEMPORARILY STAYS A INTGER NEED TO DO BELOW:
# #             num = int(num)
# #             if num>0 and num<100:
# #                 user.append((num))
# #             else:
# #                 print("only enter number from 0 to 100")
# #         else:
# #             print("only enter a number")
    
# #     print(user)
# #     return user#make sure to keep this as last thing, dont need it here as i js want to print whats in list

# #     # num_frm_user() WRONG DONT KEEP HERE
# # # num_frm_user() this is correct, unless u want to do 2 functions, cz then it prints twice
  
# # def average(user):
# #     return sum(user)/len(user)

# # saved_list=num_frm_user()
# # avg = average(saved_list)
# # print(avg)


'''
Cleaning Temperature Sensor Data

A weather station records daily temperature readings from multiple sensors in Celsius. 
However, the data sometimes includes invalid entries such as negative values below -20°C, 
missing readings (None), or strings like "error".

Your task is to clean the data and prepare it for further analysis.

Step 1 - Using Only Loops
Write code that:

1. Takes a list of temperature readings such as
   readings = [25, 30, -45, None, 28, "error", 31, 27]
2. Creates a new list containing only valid readings between -20 and 60°C.
3. Converts all valid readings from Celsius to Fahrenheit.
4. Prints both cleaned Celsius and Fahrenheit lists.

Step 2 - Rewrite Using a Function
Now rewrite your code using a function called clean_and_convert(readings) that:

* Takes a list of readings as input.
* Returns two lists: cleaned Celsius readings and Fahrenheit equivalents.
  Then test it with two different datasets:
  sensor_1 = [25, 30, -45, None, 28, "error", 31, 27]
  sensor_2 = [15, 60, 75, None, "error", 18, -5]

Step 3 - Reflection

1. How did using a for loop help in step 1?
2. What made step 2 easier when using functions?
3. If you had 50 sensors, which version would you prefer to maintain and why?

'''
# readings = [25, 30, -45, None, 28, "error", 31, 27,-18]
# # celcius = []

# # for num in readings:
# #     if isinstance(num,(int,float)) and -20<num<60:
# #         celcius.append(num)
# # print(celcius)

# # fahren = []
# # for c in celcius:
# #     f = (c*9/5)+32
# #     fahren.append(f)
# # print(fahren)


# # def celsius():
# #     cleaned_celsius = []
# #     while True:
# #         readings = input("please enter your readings")
# #         if readings == "done":
# #             break
# #         # if isinstance(readings,(int,float)) and -20<readings<60: #not gonna work cz input always gives string, range is int aso
# #         # if isinstance(readings,(int,float,str)) and -20<readings<60:#also not gonna work cz the range is int
# #         #but then no choice to convert readings to int immediately but then if user types "fwf" programme will crash so we use "Try"
# #         try:
# #             readings = float(readings)
# #             if readings>-20 and readings<60:
# #                 cleaned_celsius.append(readings)
# #         except ValueError:
# #             print("Invalid input. Please enter a number.")

# #     print(cleaned_celsius)
# #     return cleaned_celsius

# # def fahren(rar):
# #     fahren_list = []
# #     for temp in rar:
# #         fahren_list.append((temp * 9/5) + 32)
# #     return fahren_list


# # cel_list = celsius()
# # fah_list = fahren(cel_list)
# # print(f"celsius list is :{cel_list}, fahrenheit list is : {fah_list}")

# "using functions to answer with data given"

# # sensor_1 = [25, 30, -45, None, 28, "error", 31, 27]
# # celsius_cleaned=[]

# # def celsius():
# #     for num in sensor_1:
# #         if isinstance(num,(int,float)):
# #             if -20<num<60:
# #                 celsius_cleaned.append(num)
# #     print(celsius_cleaned)
# #     return celsius_cleaned

# # def fahrenheit(fahren):
# #     cleaned_fahrenheit=[]
# #     for num in fahren:
# #         cleaned_fahrenheit.append((num*9/5)+32)
# #     return cleaned_fahrenheit

# # celsiusvariable = celsius()
# # fahvariable = fahrenheit(celsiusvariable)
# # print(celsiusvariable,fahvariable)


# # "using functions to answer with 2 datasets given"
# # sensor_1 = [25, 30, -45, None, 28, "error", 31, 27]
# # sensor_2 = [15, 60, 75, None, "error", 18, -5]

# # def temperature(readings):
# #     celsius_cleaned=[]
# #     cleaned_fahrenheit=[]
# #     for num in readings:
# #          if isinstance(num,(int,float)):
# #             if -20<num<60:
# #                 celsius_cleaned.append(num)
# #                 cleaned_fahrenheit.append((num*9/5)+32)
# #     return celsius_cleaned,cleaned_fahrenheit


# # print(temperature(sensor_1))
# # print(temperature(sensor_2))

# # sensor1 = [25, 30, -45, None, 28, "error", 31, 27]
# # cleaned = []
# # def clean_sensor_readings(readings):
# #     for num in readings:
# #         if isinstance(num,int):
# #             if num>-20 and num<60:
# #                 cleaned.append(num)
# #     print(cleaned)
# #     return cleaned

# # sensor1_cleaned=clean_sensor_readings(sensor1)
# # sensor_2 = [15, 60, 75, None, "error", 18, -5]
# # sensor2_cleaned=clean_sensor_readings(sensor_2)


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
# # def welcome_employee():
# #    print("Welcome to our company!")

# # # welcome_employee("rar") WONT WORK no where to put rar.

# # def employee_greeting(employee_name="employee"):
# #    print(f"hello {employee_name}")

# # employee_greeting("rar")
# # employee_greeting()

'''3. Define a function named calculate_hourly_wage that accepts two parameters: hours_worked and hourly_rate. 
The function should calculate the total wage (hours multiplied by rate) and print the result.'''

# # def calculate_hourly_wage(hours_worked,hourly_rate):
# #    total_wage = hours_worked*hourly_rate
# #    print(f"total wage is {total_wage}")
# #    return total_wage

# # # calculate_hourly_wage(5,9)


'''4. Now modify the calculate_hourly_wage function to return the calculated wage instead of printing it.
5. Implement a function total_monthly_payroll that accepts a list of employee wages and returns the total payroll amount using the previously defined wage 
calculation function. Do not use any built-in Python functions except print().'''

# # def total_monthly_payroll(wages):
# #    total=0
# #    for wage in wages:
# #       total+=wage
# #    return total
   

# # full_wage = [
# #    calculate_hourly_wage(4,5),
# #    calculate_hourly_wage(7,9)
# # ]
# # print(f"some of the full_wage is {full_wage}")

# # monthly_total= total_monthly_payroll(full_wage)
# # print(f"the total wage in month is {monthly_total}")

'''6. Write a function named calculate_bonus with parameters salary and an optional parameter bonus_percentage defaulting to 5%.
 The function should return the bonus amount calculated on the salary.'''

# # def calculate_bonus(salary,bonus_percentage=5):
# #    bonus=salary*(bonus_percentage/100)
# #    return bonus

# # print(calculate_bonus(200))
# # print(calculate_bonus(200,10))

'''7 Create a function total_expenses that can accept any number of expense amounts (variable number of arguments) and returns their sum.'''
# # def total_expenses():
# #    expenses_list=[]
# #    while True:
# #       expenses=input("pls enter expenses")
# #       if expenses == "done":
# #          break
# #       if expenses.isnumeric():
# #          expenses_list.append(int(expenses))
# #       else:
# #          print("pls type number")
# #    total= sum(expenses_list)
# #    print(f"total expenses is {total}")

# # total_expenses()
'''
8. Define a function employee_details that takes two keyword arguments, name and department, and prints the details in the format 
"Employee [name] works in the [department] department.'''

# def employee_details(*,name,department):
#    print(f"employee {name} works in department{department}")

# employee_details(name="rishka",department="yay")

# # Lastly, create a flexible function employee_record that accepts any number of keyword arguments and prints the employee's full information as a dictionary.
# def employee_record(**kwargs):
#     print(kwargs)
# employee_record(name="maya",dob="7nov",salary="677",gender="unkown")


# def add_numbers(rar):
#     total = 0
#     for num in rar:
#         total += rar
#     print(f"Total = {total}")

# add_numbers(2, 4, 6, 8)

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

# def select_movie():   
#    name = ['barbie','oppenheimer','mission impossible','spider man']
#    selected_movies=[]
#    for i in range(len(name)):
#       print(f"{i+1} {name[i]}")

#    while True:
#       user = input("pls enter a number:")
#       if user == "done":
#          break
#       if user.isnumeric():
#          user=int(user)
#          if 1<=user<=len(name):
#                # print(f"u are selecting {name[user-1]}")
#             selected_movies.append(name[user-1])
#             print(selected_movies)
#          else:
#             print("only enter within range 1-4")      
#       else:
#             print("only type numbers")
#    return selected_movies
      
# # select_movie()
# movie_list=select_movie()

# def choose_seats(movie_list):
#    available_seats=list(range(1,11))
#    booked_seats=[]
#    print(f"available seats are {available_seats}")

#    while True:
#       input_no=input("pls enter a seat number")
#       if input_no=="done":
#          break
#       if len(booked_seats)==3:
#          print("you've booked 3 seats")
#          break
#       if input_no.isnumeric():
#          input_no=int(input_no)
#       if input_no not in available_seats:
#          print(f"seat{input_no} not available,try booking another seat")
#       else:
#          booked_seats.append(input_no)
#          available_seats.remove(input_no)
#          print(f"thanks for booking these seats so far:{booked_seats}")
#          print(f"these r available:{available_seats}")
#    print(f"final booked seats {booked_seats}")
#    return booked_seats
   
# seats_list=choose_seats(movie_list)

# # def booking_summary(movie_list, seats_list):
# #     print("\n--- Booking Summary ---")
    
# #     for i, seat in enumerate(seats_list, start=1):
# #         print(f"Seat {i}: {seat}")
    
# #     print(f"\nMovie chosen: {movie_list}")
# #     print(f"Seats reserved: {seats_list}")

# # booking_summary(movie_list, seats_list)
# #      # while True:
# #    #    tell_me=int(input("pls type seat number"))
# #    #    if tell_me==len(3):
# #    #       print("youve booked enough")
# #    #    if tell_me=="done":
# #    #       break
# #    #    if tell_me.isnumeric():
# #    #       tell_me=int(tell_me)
# #    #       if tell_me is not in available_seats:
# #    #          print("seats not available")
# #    #       else:
# #    #          booked_seats.append(tell_me)
# #    #          available_seats.remove(tell_me)
# #    #          print(f"Seat {tell_me} booked successfully!")
# #    #          print(f"Available seats now: {available_seats}")

# #    #  return choose_seats





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




# # def find_item(item_name,inventory):
# #    for item in inventory:
# #       if item["name"].lower()==item_name.lower():        #==must keep if
# #          return item
# #    return None

# # inventory = [
# #     {"name": "apple", "quantity": 10},
# #     {"name": "banana", "quantity": 5}
# # ]



# # def add_item(inventory):
# #    while True:
# #       name = input("pls enter name:")
# #       if name.lower()=="done":
# #          break
# #       quantity=int(input("pls enter a quantity:"))
   
# #       existing_item= find_item(name,inventory)
# #       if existing_item:   #keep up here
# #          existing_item["quantity"]+= quantity
# #          print(f"{name}now has stock of {existing_item["quantity"]}")
# #       else:
# #          new_item={"name":name,"quantity":quantity}
# #          inventory.append(new_item)
# #          print(f"what has been updated is {new_item}")
# #    print(f"the new dictionary is now {inventory}")

# # add_item(inventory)


# # def find_item(item_name, inventory):
# #     matches = []
# #     for item in inventory:
# #         if item["name"].lower() == item_name.lower():
# #             matches.append(item)
# #     return matches

'''
3. Remove from inventory: remove_item
   Define a function remove_item(inventory) that:

* Asks the user for the name and quantity of an item to remove.
* Uses the find_item function to locate the item:

  * If it doesn't exist, notify the user.
  * If the quantity to remove is greater than available, show an error.
  * If valid, subtract the quantity, and if it reaches zero, remove the item from the list entirely.
* This function should also run in a loop until the user types 'done'.

4. Display inventory: show_inventory
   Create a function that:

* Prints all current inventory items with their quantities using a for loop.
* If inventory is empty, display an appropriate message.

Use all these functions in a main program loop to let the user repeatedly add, remove, and view items until they choose to exit. 
The find_item function should be reused in both add_item and remove_item for centralized item lookup.

'''
# # def remove_item(inventory):
# #    while True:
# #       name=input("what u want to remove?:")
# #       if name=="done":
# #          break
# #       quantity=int(input("what quantity u want to remove?:"))

# #       looking_item=find_item(name,inventory)
# #       if not looking_item:
# #          print(f"{name} doesn't exist")
# #          continue
# #       if quantity> looking_item["quantity"]:
# #          print(f"error, the available quantity is only {looking_item["quantity"]}")
# #       elif quantity==looking_item["quantity"]:
# #          print(f"there is no more left now")
# #          inventory.remove(looking_item)
# #       else:
# #          looking_item["quantity"]-=quantity
# #          print(f"updated quantity is now {looking_item["quantity"]}") 
# #    print("Updated inventory:")
   
# # remove_item(inventory)

   
# # def show_inventory(inventory):
# #    for item in inventory:
# #       print(f"Name: {item['name']}, Quantity: {item['quantity']}")
# #    if len(inventory)==0:
# #       print(f"inventory is empty")


# # remove_item(inventory)

'''You are a programmer building a simple payroll management tool for a small company. 
Your task is to create various functions to automate payroll calculations. 
This problem will test your understanding of Python functions, parameters, default arguments, return statements, 
and handling multiple arguments.

1. Write a simple function called welcome_employee that takes no parameters and prints "Welcome to our company!".

2. Create a function called employee_greeting that takes one parameter called employee_name with a default value of 'Employee'.
 It should print a greeting message like "Hello Employee!".

3. Define a function named calculate_hourly_wage that accepts two parameters: hours_worked and hourly_rate. 
The function should calculate the total wage (hours multiplied by rate) and print the result.
'''


# # def welcome_employees():
# #    print("welcome to the company")

# # welcome_employees()

# # def employee_greeting(employee_name):
# #    print(f"hello {employee_name}")

# # employee_greeting("rishka")

'''
4. Now modify the calculate_hourly_wage function to return the calculated wage instead of printing it.

5. Implement a function total_monthly_payroll that accepts a list of employee wages and returns the total payroll amount using the previously defined wage 
calculation function. Do not use any built-in Python functions except print().
'''
# def calculate_hourly_wage(hours_worked,hourly_rate):
#    total_wage=hours_worked*hourly_rate
#    print(f"total_wage hourly is {total_wage}")
#    return total_wage

# def total_monthly_payroll(wages):
#    total=0  #need start w this cz total doesnt exist yet
#    for wage in wages:
#       total+=wage
#    print(f"The monthly total is {total}")
#    return total

# # the_list=calculate_hourly_wage(5,6)no work cz this will return 30 >is int, u have a for loop which can't iterate integer.need ekeep list
# wage_list= [calculate_hourly_wage(4,5),
#             calculate_hourly_wage(4,2)]
# #above you saved the function under variable wage_list
# the_monthly=total_monthly_payroll(wage_list)

'''6. Write a function named calculate_bonus with parameters salary and an optional parameter bonus_percentage defaulting to 5%.
 The function should return the bonus amount calculated on the salary.'''

# def calculate_bonus(salary,bonus_percent=5):#dont keep "5"
#    # for sal in salary:
#    #    bonus_amount= 5/100*sal
#    #    print(f"the bonus amount is {bonus_amount}")
#    bonus_amnt= salary*(bonus_percent/100)
#    print(f"the bonus amount is {bonus_amnt}")

# bonus=calculate_bonus(the_monthly) #can use this function to calculate bonus frm other functions which calculated buildup form  the hourly,monthly salary
# calculate_bonus(456,3)#or can separately find for a salary, rate u r interested in

'''7 Create a function total_expenses that can accept any number of expense amounts (variable number of arguments) and
 returns their sum.'''
# def total_expenses():
#    expenses_list=[]
#    while True:
#       expenses=input("pls enter expenses")
#       if expenses == "done":
#          break
#       if expenses.isnumeric():
#          expenses_list.append(int(expenses))
#       else:
#          print("pls type number")
#    total= sum(expenses_list)
#    print(f"total expenses is {total}")

# total_expenses()

# # # 8. Define a function employee_details that takes two keyword arguments, name and department, 
# # and prints the details in the format 
# # # "Employee [name] works in the [department] department.
# def employee_details(name,department): #"employee law works in dep rishka"
#    print(f"hello {name} who works in department {department}")

# employee_details("rishka","lawyer")

# #vs

# def employee_details(*,name,department): #fixed, not positional
#    print(f"employee {name} works in department{department}")

# employee_details(name="rishka",department="yay")

# # # Lastly, create a flexible function employee_record that accepts any number of keyword arguments 
# # and prints the employee's full information as a dictionary.

# def employee_record(**kwargs):
#     print(kwargs)
# employee_record(name="maya",dob="7nov",salary="677",gender="unkown")


# # def add_numbers(rar):
# #     total = 0
# #     for num in rar:
# #         total += rar
# #     print(f"Total = {total}")

# # add_numbers(2, 4, 6, 8)



'''
You are helping a small delivery company track daily packages. Write a program that does the following:

1. Ask the user how many package IDs they want to enter. Use a for loop to collect each package ID and store them in a list.

2. Create a function called check_priority that takes a package ID and returns True if the ID contains the letter P, otherwise returns False.

3. After building the list, use another for loop to go through each package ID. 
For every package ID, call check_priority and print a message saying whether it is a priority package or a regular package.

4. Ask the user for a city name. If the city is New York, Chicago, or Boston, print that same day delivery is available for all priority packages. 
Otherwise print that only regular delivery is available.

5. Create a function called count_priority that takes the full list of package IDs and returns how many of them are priority packages. Print the final count.

'''
# amount = int(input("enter the amount of packages u wanna enter:"))

# package_id = []

# for i in range(amount):
#    user = input("please enter the package ids:")
#    package_id.append(user)

# def check_priority(package_id):
#    if "p" in package_id.lower():
#       return True
#    else:
#       return False

# for x in package_id:
#    print(check_priority(x))
#    if check_priority(x):
#       print((f"{x} is a priority package"))
#    else:
#       print((f"{x} is a regular package"))

# where=input("where u live")
# if where in ("boston", "chicago", "new york"):
#    print("only regular delivery can")

# def count_priority(package_id):
#    count = 0
#    for num in (package_id):
#       if check_priority(num):
#          count+= 1
#    return(count)
      
# print(f"number of priorityyy is {count_priority(package_id)}")

'''
1. Ask the user how many device serial numbers they want to enter.
Use a for loop to collect each serial number and store them in a list.

2. Create a function called check_urgent
This function takes one serial number and
returns True if the serial number contains the letter U (uppercase or lowercase)
otherwise returns False

3. After building the list, use another for loop
For each serial number:
call check_urgent
print whether it is an urgent repair or a normal repair

4. Create a function called count_urgent
This function takes the full list of serial numbers and returns how many of them are urgent.

At the end of the program, print:
Total urgent devices: X

'''

# user = int(input("How many serial numbers u want to enter"))
# list_serialno = []

# for x in range(user):
#    serial_number = input("enter the serial numbers")
#    list_serialno.append(serial_number)

# def check_urgent(serial_no):
#    if "u" in serial_no.lower():
#       return True
#    else:
#       return False

# for s in list_serialno:
#     if check_urgent(s):
#         print(f"{s} needs urgent repair")
#     else:
#         print(f"{s} is normal repair")

# def count_urgent(full_list):
#     count = 0
#     for num in full_list:
#         if check_urgent(num):
#             count += 1
#     return count

# print(f"the full list is {count_urgent(list_serialno )}")

'''
 Cleaning Temperature Sensor Data

A weather station records daily temperature readings from multiple sensors in Celsius. 
However, the data sometimes includes invalid entries such as negative values below -20°C, 
missing readings (None), or strings like "error".

Your task is to clean the data and prepare it for further analysis.

Step 1 - Using Only Loops
Write code that:

1. Takes a list of temperature readings such as
   readings = [25, 30, -45, None, 28, "error", 31, 27]
2. Creates a new list containing only valid readings between -20 and 60°C.
3. Converts all valid readings from Celsius to Fahrenheit.
4. Prints both cleaned Celsius and Fahrenheit lists.

Step 2 - Rewrite Using a Function
Now rewrite your code using a function called clean_and_convert(readings) that:

* Takes a list of readings as input.
* Returns two lists: cleaned Celsius readings and Fahrenheit equivalents.
  Then test it with two different datasets:
  sensor_1 = [25, 30, -45, None, 28, "error", 31, 27]
  sensor_2 = [15, 60, 75, None, "error", 18, -5]

Step 3 - Reflection

1. How did using a for loop help in step 1?
2. What made step 2 easier when using functions?
3. If you had 50 sensors, which version would you prefer to maintain and why?
'''
#NO FUNCTIONS

# readings = [25, 30, -45, None, 28, "error", 31, 27] 
# reading = [5, 0, -5, None, 8, "error", 1, 7]
# all_readings = readings + reading 
# cleaned = []

# for num in all_readings:
#     if isinstance(num,(int,float)) and -20<num<60:
#         cleaned.append(int(num))
# print(cleaned)

# fahren = []
# for num in cleaned:
#     f = (num*9/5)+32
#     fahren.append(f)
# print(fahren)

# FUNCTIONS:
    

# readings = [25, 30, -45, None, 28, "error", 31, 27]
# reading = [5, 0, -5, None, 8, "error", 1, 7]
# all_readings = readings + reading
# readingz = [3,4,-2,4,44]

# def clean_and_convert(inputs):
#     cleaned_celsius=[]
#     for num in inputs:
#         if isinstance(num,(int,float)) and -20<num<60:
#             cleaned_celsius.append(int(num))
#     return cleaned_celsius

# def fahren(cleaned_cel):
#     fahren=[]
#     for num in cleaned_cel:
#         f=(num*9/5)+32
#         fahren.append(f)
#     return fahren

# celsius= clean_and_convert(reading+readings)
# celsius += clean_and_convert(readingz)
# fahrenheit=fahren(celsius)
# print(f"the celsius is {celsius} and fahrenheit is {fahrenheit}")

# OR



# def celsius():
#     cleaned_celsius = []
#     while True:
#         readings = input("please enter your readings")
#         if readings == "done":
#             break
#         # if isinstance(readings,(int,float)) and -20<readings<60: #not gonna work cz input always gives string, range is int 
#         # if isinstance(readings,(int,float,str)) and -20<readings<60:#also not gonna work cz the range is int
#         #but then no choice to convert readings to int immediately but then if user types "fwf" programme will crash so we use "Try"
#         try:
#             readings = float(readings)
#             if readings>-20 and readings<60:
#                 cleaned_celsius.append(readings)
#         except ValueError:
#             print("Invalid input. Please enter a number.")

#     print(cleaned_celsius)
#     return cleaned_celsius

# def fahren(rar):
#     fahren_list = []
#     for temp in rar:
#         fahren_list.append((temp * 9/5) + 32)
#     return fahren_list


# cel_list = celsius()
# fah_list = fahren(cel_list)
# print(f"celsius list is :{cel_list}, fahrenheit list is : {fah_list}")



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

# def welcome_employee():
#     print("welcome to our company")

# def employee_greeting(name="Employee"):
#     print(f"welcome to our company {name}")

# def calculate_hourly_wage(hours_worked,hourly_rate):
#     total_wage=hours_worked*hourly_rate
#     return total_wage

# full_wage = [
#     calculate_hourly_wage(4,5),
#     calculate_hourly_wage(6,7)
# ]
# print(f"the full wages is {full_wage}")

# #USE PREVIOUS FUNCTION TO GET BONUS VALUE

# def calculate_bonus(salary,bonus_percentage=5):
#     full_wage_list=[]
#     for num in salary:
#         bonus=num*(bonus_percentage/100)
#         full_wage_list.append(bonus)
#     return full_wage_list

# print(calculate_bonus(full_wage,9))

# #GIVE SALARY AN INDIVIDUAL  VALUE

# # def calculate_bonus(salary,bonus_percentage=5):
# #     bonus=salary*(bonus_percentage/100)
# #     return bonus

# # bonuses = [
# #     calculate_bonus(salary,7),
# #     calculate_bonus(salary,4)
# # ]

# # bonuses = [
# #     calculate_bonus(34,7),
# #     calculate_bonus(2,4)
# # ]
   
# # print(f"the bonus amount is {bonuses}")

# # def expenses():
# #     expenses=[]
# #     while True:
# #         user=input("pls enter expenses:")
# #         if user =="done":
# #             break
# #         if user.isnumeric():
# #             expenses.append(int(user))
# #     total=sum(expenses)
# #     print(f"total expenses is {total}")

# # expenses()

# def employee_details(name,department):
#     print(f"employee {name} works in department {department}")

# employee_details("kegan","fish")

# def employee_record(**kwargs):
#     print(kwargs)
# employee_record(name="maya",dob="7nov",salary="677",gender="unkown")


'''
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
# def select_movie():
#     name=["oppenheimer","barbie","mission impossible","spider man"]
#     for i in range(len(name)):
#         print(f"{i+1}:{name[i]}")

#     selected_movies=[]
#     while True:
#         user= input("enter a no:")
#         if user == "done":
#             break
#         if user.isnumeric():
#             user=int(user) 
#             if 1<=user<=len(name):
#                 print(f"u are selecting {name[user-1]}")
#                 selected_movies.append(name[user-1])
#             print(f"the movie you selected is {selected_movies}")
#         else:
#             print("only enter numbers")
#     return(selected_movies)


# def seats(movies):
#     seat_list=[]
#     seat_no = [1,2,3,4,5,6,7,8,9,10]
#     while True:
#         user=input("please enter a seat number")
#         if user == "done":
#             break
#         if user.isnumeric():
#             user=int(user)
#             if len(seat_list)==3:
#                 print("you've booked 3 seats which is the limit")
#                 break
#             if user in seat_no:
#                 seat_list.append(user)
#                 seat_no.remove(user)
#                     # seat_list.append(f"{user},{movie}")
#                 print(f"thanks for booking these seats so far {seat_list}")
#                 print(f"these are available seats {seat_no}")
#                 print(f"the final seats chosen is {seat_list}")
                    
#             else:
#                 print("you've chosen the same seat, choose another one")
#     return seat_list
                
                    

# def booking_summary(movies,seats):
#     print(f"booking summary for movies is : {movies}")
#     for seat in seats:
#         print(f"seat number:{seat}")
        



# # movies=select_movie()
# # seatss= seats(movies)
# # booking_summary(movies,seatss)

'''
Wildlife Research Tracker

You are helping a wildlife research team record information about animals spotted during a field study. Write a program that does the following:

1. Ask the user how many animal IDs they want to enter. Use a loop to collect each ID and store them in a list.

2. Create a function named is_endangered that takes an animal ID and returns True if the ID contains the letter E, otherwise False.

3. After the list is built, loop through every ID.
   For each ID, call is_endangered and print whether the animal is classified as endangered or not.

4. Ask the user for the region where the team is working.
   If the region is Amazon, Congo, or Borneo, print that special monitoring rules apply to endangered animals.
   Otherwise print that normal monitoring rules apply.

5. Create another function called count_endangered that receives the full list and returns both:
   • the number of endangered animals
   • the number of non-endangered animals
   Then print both results.

6. Finally, create a new list that contains only the endangered animal IDs. Print this filtered list.

'''

# def animal_id():
#     animal_id=[]
#     count=int(input("how many ids do you want to enter:"))

#     for i in range(count):
#         user=input("pls enter id numbers:")
#         if user=="done":
#             break
#         animal_id.append(user)
#     return animal_id

# def is_endangered(animal_id):
#     endangered_list=[]
#     notendangered_list=[]
#     endangered_count=0
#     notendangered_count=0
#     for animal in animal_id:
#         if "E" in animal:
#             print (f"{True},{animal} is endangered")
#             endangered_list.append(animal)
#             endangered_count+=1
#             print(endangered_count)

#         else:
#             print (f"{False},{animal} is not endangered")
#             notendangered_list.append(animal)
#             notendangered_count+=1
#             print(notendangered_count)

#     print(f"total endangered: {endangered_list}")
#     print(f"total notdangered: {notendangered_list}")

#     while True:
#         user=input("which area are you working?:")
#         if user == "done":
#             break
#         if user in ("amazon","congo","borneo"):
#             print("special monitoring rules apply to endangered animals")
#         else:
#             print("normal monitoring rules apply")
    
# # id=animal_id()
# # endangered=is_endangered(id)

'''
You're developing a simple plant care reminder app. The app should allow users to add plants, check plant watering status, 
and remind them to water their plants. This problem tests your understanding of functions, if conditions, loops, lists, and user input.

1. Add Plants
   Write a function called add_plants that:

* Initializes an empty list called plants.
* Continuously asks the user to input the names of their plants.
* The loop stops when the user types 'stop'.
* Returns the list of plants.

2. Check Watering Status
   Define a function called check_watering_status that:

* Takes the plants list as an argument.
* Loops through each plant, asking the user "Did you water [plant]? (yes/no)".
* Uses an if condition to check user input:

  * If 'no', adds the plant name to another list needs_watering.
  * If 'yes', continues without action.
* Returns the list of plants that need watering.

3. Show Watering Reminder
   Define a function called watering_reminder that:

* Accepts the list needs_watering as input.
* If the list is empty, prints "Great! All plants are watered.".
* Otherwise, prints "You need to water:" followed by a list of plants using a for loop.

Call these three functions sequentially in the main program to implement your plant watering reminder app.
'''

# def add_plants():
#     plants=[]
#     while True:
#         user = input("enter names of plants:")
#         plants.append(user)
#         if user=="stop":
#             break
#     return plants

# def check_watering_status(plants):
#     needs_watering=[]
#     for plant in plants:
#         user=input(f"did you water plant {plant}")
#         if user=="no":
#             needs_watering.append(plant) 
#     return needs_watering

# def watering_reminder(needs_watering):
#     if len(needs_watering)==0:
#         print("Great all the plants are watered")
#     else:
#         print(f"you need to water {needs_watering}")
        
# # plants=add_plants()
# # watering_stat=check_watering_status(plants)
# # watering_reminder(watering_stat)


'''
You are helping a small delivery company track daily packages. Write a program that does the following:

1. Ask the user how many package IDs they want to enter. Use a for loop to collect each package ID and store them in a list.

2. Create a function called check_priority that takes a package ID and returns True if the ID contains the letter P, otherwise returns False.

3. After building the list, use another for loop to go through each package ID. 
For every package ID, call check_priority and print a message saying whether it is a priority package or a regular package.

4. Ask the user for a city name. If the city is New York, Chicago, or Boston, print that same day delivery is available for all priority packages. 
Otherwise print that only regular delivery is available.

5. Create a function called count_priority that takes the full list of package IDs and returns how many of them are priority packages. Print the final count.
'''

# count = int(input("how many package ID's do you want to enter?"))

# IDs=[]
# for i in range(count):
#     user= input("enter user ID's:")
#     IDs.append(user)

# def check_priority(package_id):
#     if "P" in package_id:
#         return True
#     else:
#         return False

# for package_id in IDs:
#     # if check_priority(package_id):
#         print (f"this PACKAGE :{package_id} is priority package")
#     # else:
#         print(f"this PACKAGE :{package_id} is regukar package")

# # person=input("give a city name")
# # if person == ("Boston","chicago","new york"):
# #     print("same day delivery is avaiable for priority packages")
# # else:
# #     print("only regular delivery is available")

# def count_priority(IDs):
#     priority=0
#     regular=0
#     for package_id in IDs:
#         # if check_priority(package_id):
#             priority+=1
#         # else:
#             regular+=1
#     print(priority)
#     print(regular)

# # count_priority(IDs)


'''
Ask the user how many patient IDs they want to enter and store them in a list.

Create a function called is_emergency that takes one patient ID and returns True if the ID contains the letter E.

Loop through the list and print whether each patient is an emergency case or a regular case.

Create a function called count_emergency that takes the full list and returns how many emergency patients there are.
'''

# count = int(input("how many ids do u want to enter?: "))
# user_list=[]
# for i in range(count):
#     user=input("pls enter patient IDs: ")
#     user_list.append(user)

# def is_emergency(patient):
#     if "E" in patient:
#         return True
#     else:
#         return False
    
# for patient in user_list:
#     # if is_emergency(patient):
#         print("emergency case")
#     # else:
#         print("regular case")

# def count_emergency(user):
#     count=0
#     for patient in user_list:
#         # if is_emergency(patient):
#             count+=1
#     print(f"total emergency patients is {count}")

# # count_emergency(user_list)

'''
You are helping a gym manage memberships.

Create a function called is_premium that takes one membership ID and returns True if it contains the letter G.

Ask the user how many membership IDs they want to enter and store them in a list.

Call the function inside a loop to print whether each member is premium or standard.

Create a function called count_premium that returns how many premium members there are.

Ask the user for the gym branch. If the branch is Downtown, Central, or West, print that premium members get free classes.
'''

# def is_premium(membership_id):
#     if "P" in membership_id:
#         return True
#     else:
#         return False

# user = int(input("how many IDs do you want to enter?"))
# id_list=[]
# for i in range(user):
#     IDs= input("enter the IDs:")
#     id_list.append(IDs)

# for ID in id_list:
#     if is_premium(ID):
#         print(f"{ID} is premium ID")
        
#     else:
#         print(f"{ID} is regular ID")
        

# def count_premium(total):
#     count=0
#     for id in id_list:
#         if is_premium(id):
#             count+=1
#         print(count)

# count_premium(id_list)


# user = int(input("how many IDs do you want to enter?"))
# id_list=[]
# for i in range(user):
#     IDs= input("enter the IDs:")
#     id_list.append(IDs)

# def is_baller(name):
#     for n in name:
#         if "p" in n:
#             print(f"{n} is priority")
#         else:
#             print(f"{n} isnt a priority")

# is_baller(id_list)



def print_user_info3(**info):
    print(f'Hello {info.get('name','unknown user')} from {info.get('country','unknown country')}')

print_user_info3(country='England')
print_user_info3(name='Jonathan Harker',occupation='lawyer',spouse='Mina Harker',enemy='Count Dracula')
