'''
INTEGERS/INDEXES

Q1.
You are given a list of ages:

ages = [12, 17, 20, 35, 8, 65, 40, 15]
Write a program that separates the ages into two lists:

minors (below 18)
adults (18 and above)
Print both lists at the end.
'''
# ages = [12, 17, 20, 35, 8, 65, 40, 15]

# minors = []
# adults = []
# for i in ages:
#     if i >=18:
#         adults.append(i)
#     else:
#         minors.append(i)
# print(minors)
# print(adults)


'''''

Q2.
Ask the user how many temperatures they want to enter.

Take that many temperatures one by one.

Put values greater than 30 into a hot_days list.

Put values less than or equal to 30 into a cool_days list.
Finally, print both lists.

'''
# hot_days = []
# cold_days = []

# how_many_temp = int(input("how many temp u want enter:"))
# for i in range(how_many_temp):
#     temp_is = int(input("what's the temp:"))
#     if temp_is > 30:
#         hot_days.append(temp_is)
#     else:
#         cold_days.append(temp_is)
# print(hot_days)
# print(cold_days)

''''
Q3.
You are given a list of numbers:

numbers = [10, 15, 22, 33, 40, 55, 60]


Create two new lists:

div_by_5 (numbers divisible by 5)

not_div_by_5 (all the rest).
Print both lists.


'''
# numbers = [10, 15, 22, 33, 40, 55, 60]
# div_5 = []
# not_div5 = []
# for i in numbers:
#     if i % 5 ==0:
#         div_5.append(i)
#     else:
#         not_div5.append(i)
# print(div_5)
# print(not_div5)


'''''''''
Q4.
Ask the user to enter 7 city names (one by one).

Store them in a list.

Print only the cities that start with the letter "S" into a new list called s_cities.
Print that list at the end.

'''

# s_cities = []
# for i in range(7):
#     what_names = input("enter city names")
#     if what_names[0]=="s":
#         s_cities.append(what_names)
# print(s_cities)
'''''''''

Q5.
You are given a list of marks:

marks = [23, 67, 50, 89, 45, 99, 10, 73]


Use a for loop to separate them into 3 lists:

fail (< 50)

pass_list (50–74)

distinction (75 and above).
Print all three lists.
'''
# fail = []
# pass_list = []
# distinction = []


# marks = [23, 67, 50, 89, 45, 99, 10, 73]
# for i in marks:
#     if i >= 75:
#         distinction.append(i)
#     elif i>=50 and i<=74:
#         pass_list.append(i)
#     else:
#         fail.append(i)
# print(distinction)
# print(pass_list)
# print(fail)




'''
''
PRACTICING STRINGS:

You are given a list of words:

words = ["apple", "banana", "pear", "grape", "cherry", "kiwi", "plum"]


👉 Create two new lists:

long_words → words with length greater than 4

short_words → words with length 4 or less
'''''''''

# words = ["apple", "banana", "pear", "grape", "cherry", "kiwi", "plum"]

# long_words = []
# short_words = []
# for word in words:
#     if len(word)>4:
#         long_words.append(word)
#     else:
#         short_words.append(word)
# print(long_words)
# print(short_words)

''''''

''''''''''
You are given a list of animals:

animals = ["cat", "elephant", "dog", "ant", "tiger", "cow"]
👉 Create two new lists:
long_animals → animals with length ≥ 4
short_animals → animals with length < 4

'''
# long_animals = []
# short_animals = []
# animals = ["cat", "elephant", "dog", "ant", "tiger", "cow"]

# for animal in animals:
#     if len(animal)>=4:
#         long_animals.append(animal)
#     else:
#         short_animals.append(animal)
# print(long_animals)
# print(short_animals)



''''
(INT AGAIN)
Create two new lists:
div_by_3 → numbers divisible by 3
not_div_by_3 → numbers not divisible by 3

'''
# div_by_3 = []
# not_div_by_3 = []

# for i in range(7):
#     what_number = int(input("pls enter number:"))
#     if what_number % 3 == 0: #wrong= must keep what_number, not i 
#         div_by_3.append(what_number)
#     else:
#         not_div_by_3.append(what_number)
# print(div_by_3)
# print(not_div_by_3)


''
'''''
Q3.
You are given a list of numbers:
numbers = [10, 15, 22, 33, 40, 55, 60]
Create two new lists:

div_by_5 (numbers divisible by 5)
not_div_by_5 (all the rest).
Print both lists.
'''

# numbers = [10, 15, 22, 33, 40, 55, 60]
# div_5 = []
# not_div5 = []
# for i in numbers:
#     if i % 5 ==0:
#         div_5.append(i)
#     else:
#         not_div5.append(i)
# print(div_5)
# print(not_div5)

''''''

'''
2.
Ask the user how many temperatures they want to enter.

Take that many temperatures one by one.

Put values greater than 30 into a hot_days list.

Put values less than or equal to 30 into a cool_days list.
Finally, print both lists.

'''
# hot_days = []
# cold_days = []

# how_many_temp = int(input("how many temp u want enter:"))
# for i in range(how_many_temp):
#     temp_is = int(input("what's the temp:"))
#     if temp_is > 30: 
#         hot_days.append(temp_is) #if keep i here, itll give index
#     else:
#         cold_days.append(temp_is)
# print(hot_days)
# print(cold_days)
'''

print every odd name in the below list
names  
print every odd name in the below list using a for loop
Hint: use a range object. Call each name using its index

names = ['Roy','Sharon','Therese','Ravi','Shanti','Nelum','Hillary','Niran']
'''
# for i in range(0, len(names), 2): 
#     print(names[i])


'''
26/09
    Understanding diff when i is a value/loop/index

1️⃣ Divisible numbers (user input)
Ask the user for 5 numbers.
Put numbers divisible by 4 in div_by_4.
Put the rest in not_div_by_4.

'''

# div_by_4 = []
# not_div_by_4 = []

# for i in range(5):
#     numbers = int(input("enter your no:"))
#     if numbers % 4 == 0:
#         div_by_4.append(numbers)
#     else:
#         not_div_by_4.append(numbers)

# print(not_div_by_4)
# print(div_by_4)


'''

2️⃣ Temperatures with a threshold

Ask the user how many temperatures they want to enter.

Put temperatures ≥ 25 into warm_days.

Put temperatures < 25 into cool_days.

Print the order each temperature was entered.

'''
# warm_days = []
# cool_days = []

# how_many_temp = int(input("how many temp you want to enter"))
# for i in range(how_many_temp):
#     what_temp = int(input("what temp you want to enter"))
#     if what_temp>= 25:
#         warm_days.append(what_temp)
#     else:
#         cool_days.append(what_temp)

# print(warm_days)
# print(cool_days)
    
'''Homework

Description: You manage an online bookstore and have recorded today’s book sale prices in a list.
 Your task is to analyze these prices using if conditions, list operations and for loops.

1. Given the list sales_prices = [12.99, 45.00, 9.50, 75.20, 22.00, 150.00, 5.99], write a for loop to iterate over each price.
2. Inside the loop, use if conditions to classify each price as “budget” (price < 20), “standard” (20 <= price <= 50) or “premium” (price > 50).
3. Maintain three variables budget_count, standard_count and premium_count and increment the appropriate one for each price.
4. Create an empty list premium_sales and append every price classified as “premium” to this list.
5. After the loop finishes, print the values of budget_count, standard_count, premium_count and the premium_sales list.'''


# budget_count = [] 
# standard_count = []
# premium_count = []
# premium_sales = []

# sales_prices = [12.99, 45.00, 9.50, 75.20, 22.00, 150.00, 5.99]
# for i in sales_prices:
#    if i < 20 :
#       budget_count.append(i)
#    elif i > 50 :
#       premium_count.append(i)
#       premium_sales.append(i)
#    elif i >= 20 and i <= 50:
#       standard_count.append(i)
    
      

# print(budget_count)
# print(standard_count)
# print(premium_count)
# print(premium_sales)

'''

-----------------------------------------------

Description: You run a smart home system that logs daily electricity usage (in kWh) alongside the average outside temperature.
 Your task is to analyze the data using if conditions, list operations, and for loops.

1. Given the lists
   days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
   energy_usage = [1.2, 1.5, 2.1, 2.4, 1.7, 1.3, 2.0]
   outside_temps = [15, 16, 20, 22, 18, 14, 19]
   verify that all three lists are the same length.
2. Create an empty list efficiency_ratios. Write a for loop that iterates by index,
 computes ratio = energy_usage[i] / outside_temps[i], and appends the result to efficiency_ratios.
3. Inside the same loop (or immediately after), use if conditions to classify each day’s usage as
 “low” (energy_usage < 1.5), “normal” (1.5 <= energy_usage <= 2.0) or “high” (energy_usage > 2.0),
  and maintain three counters: low_count, normal_count, high_count.
4. Whenever a day is classified as “high”, append days[i] to a list high_usage_days.
5. After processing all entries, compute total_usage as the sum of energy_usage and average_ratio 
as the sum of efficiency_ratios divided by the number of days.
6. Print low_count, normal_count, high_count, total_usage, average_ratio (rounded to three decimal places), and the high_usage_days list.

'''
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# energy_usage = [1.2, 1.5, 2.1, 2.4, 1.7, 1.3, 2.0]
# outside_temps = [15, 16, 20, 22, 18, 14, 19]
# efficiency_ratios = []
# low_count = 0
# normal_count = 0
# high_count = 0
# high_usage = []

# length_same = []
# if len(days) == len(energy_usage)==len(outside_temps):
#     print("all list same length")
# else:
#     print("not the same length") 
# # for i in range(energy_usage): # WRONG range(...) needs an integer (like 7) to know how many steps to make. 
# #energy_usage is a list ([1.2, 1.5, 2.1, ...]).Python doesn’t know how to turn a list directly into a number
# for i in range(len(energy_usage)):#or range(7)
#     ratio = energy_usage[i]/outside_temps[i]
#     efficiency_ratios.append(ratio)
# for i in range(len(energy_usage)):          #prev kept for i in energy usage not range. but didn't work when it came to qs 4 as i need it 
#     if energy_usage[i] > 2:                 #to be an index so it can match the index of the days and they will print the days.  
#         high_count+=1                       #before they printed 1.2 and 2.4 not the names of the days. i rep index, so if i kept
#         high_usage.append(days[i]) #i>2, it prints not energy_usage values more than 2 but the index values more than 2
# #so like Thursday", "Friday", "Saturday", "Sunday", that's why need to keep energy_usage[i], so it can take which value gives more than 2
# #and the index of that, compare it to the index of the days and give us that.
#     elif energy_usage[i]>= 1.5 and energy_usage[i] <=2:
#         normal_count+=1
#     else:
#         low_count+=1
# average_ratios = sum(efficiency_ratios)/len(days)   #cant put sum here as it is not a list, it is single integer  
# total_usage = sum(energy_usage)+(average_ratios)

# print(low_count)
# print(normal_count)
# print(high_count)
# print(efficiency_ratios)
# print(total_usage)
# print(average_ratios)
# print(high_usage)

'''
