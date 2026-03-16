'''
Function: A block of code, that can be reused and designed for a specific purpose 

Block of code: 
Reusability: 
Specific purpose: 
'''

#most simplest form of a function 
#creating a tool: is used to print same thing again and again
def greet():   
    print("hello world")
    print("its a wonderful life")
    print("be thankful")
    print("chao")    
    print("--------------------")
# #using the tool 

greet()
# greet()
# greet()


def voting_age_checker(name,age):
    if age>=18:
        print(f"Hi {name}, please proceed to the voting center")
    else:
        print(f"Hi {name}, you are old enough to vote")
        
# # Create a function that will take two numbers, add them and print the result

def add_two_numbers(number_1,number_2):
    return number_1 + number_2

# result=add_two_numbers(2,3)
# print(result)

# #use the above add_numbers function you created to get the sum of all the numbers in the nums list
# nums = [10,20,30,40]
# # print(nums[0]+nums[1]+nums[2]+nums[3])

# #function chaining
# final=add_two_numbers(add_two_numbers(nums[0],nums[1]),add_two_numbers(nums[2],nums[3]))
# print(final)





    
'''
Gather scores that are between 0 and 100 from ther user continuously
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

    
def get_numbers_from_user():
    nums=[]
    while True: 
        user_input=input("Please enter a number between 0 and 100: ")
        if user_input== 'done':
            break
        else:
            if user_input.isnumeric():
                nums.append(int(user_input)) 
    return nums

def get_average_from_list(nums):
    return sum(nums)/len(nums)

rar=get_numbers_from_user() 
avg=get_average_from_list(rar)
print(f"average is {avg}")

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
# sensor1 = [25, 30, -45, None, 28, "error", 31, 27]
# cleaned = []
# def clean_sensor_readings(readings):
#     for num in readings:
#         if isinstance(num,int):
#             if num>-20 and num<60:
#                 cleaned.append(num)
#     print(cleaned)
#     return cleaned

# sensor1_cleaned=clean_sensor_readings(sensor1)
# sensor_2 = [15, 60, 75, None, "error", 18, -5]
# sensor2_cleaned=clean_sensor_readings(sensor_2)


