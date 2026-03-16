'''
We have a way to create data in bulk 
But how do we manipulate in bulk 

'''
#add 10 each score and print back 
scores2 = [45,78,49,23,67,23,75,23,89,65,53,78,49,23,67,23,75,23,89,65,5,78,49,23,67,23,75,23,89,65,5]
# nums= range(0,1000000,1)
scores= [10,20,30]

# print(scores[0]+10)
# print(scores[1]+10)
# print(scores[2]+10)

# for hehe in scores2:
#     print(hehe+10)
    
#range function - 
#range(start,end,step_size)> function not list(;)

# numbers= list(range(0,10,1))
# print(numbers)

#print all the even numbers from 10 to 20
# numbers= range(10,21,2)
# print(numbers)

# for number in numbers:
#     print(number)
    
#print every odd name in the below list
# names  
#print every odd name in the below list using a for loop
#Hint: use a range object. Call each name using its index

# names = ['Roy','Sharon','Therese','Ravi','Shanti','Nelum','Hillary','Niran']

# for i in range(0, len(names), 2):  # start at index 0, jump by 2
#     print(names[i])

# for names in names(range(1,8,1))
#     print(names)

# Exercises

# print every even name in the below list, print every odd name in the below list using a for loop
# Hint: use a range object. Call each name using its index
# names = ['Roy','Sharon','Therese', 'Ravi','Shanti','Nelum','Hillary','Niran']

# for o in range(0, len(names), 2):  #ODD NUMBERS
#     print(names[o])

# for e in range (1,len(names),2): #EVEN NUMBERS
#     print(names[e])

'''
You are given a list of numbers. 
Write a program that will: 

1. Go through the list using a FOR LOOP.
2. Use an IF condition to separate the numbers:
   - Even numbers go into the "even_list"
   - Odd numbers go into the "odd_list"
3. Finally, print both lists.

'''

# numbers = [1,2,3,4,5,6,7,8,9]
# even_list=[]
# odd_list=[]

# for number in numbers:
#     if number in range(0,len(numbers),2):  
#         print(numbers[i],"this number is in even list")
#         # print(list(range(0,len(numbers),2)))
       
# else:
#     print("these numbers are in odd list:")
#     print(list(range(1,len(numbers),2)))

# for index in range(0,len(numbers),2): #odd numbers
#     odd_list.append(numbers[index])
    
# for index in range(1,len(numbers),2): #even numbers
#     even_list.append(numbers[index])

# print(f"even numbers: {even_list}")
# print(f"odd numbers: {odd_list}")


'''
1. Ask the user to enter 5 test scores (one by one).
2. Store these scores in a list.
3. Use a FOR LOOP and IF condition:
   - If the score is 50 or more, put it in the "pass_list".
   - Otherwise, put it in the "fail_list".
4. Print both lists at the end.

'''
# fail_list = []
# pass_list = []
# for i in range(5):
#     test_scores = int(input("enter test scores:"))
#     if test_scores>=50:
#         pass_list.append(test_scores)
#     else:
#         fail_list.append(test_scores)

# print(pass_list)
# print(fail_list)

'''
Ask the user how many numbers they want to enter.  
2. Take that many numbers as input from the user, one by one.  
3. Store the numbers in a list.  
4. Use a FOR LOOP and IF conditions to create three lists:
   - positive_numbers
   - negative_numbers
   - zeros
5. Print all three lists at the end.'''

# numbers = []
# positive_numbers = []
# negative_numbers = []
# zeros = []


# number_of_inputs = int(input("how many numbers do you want to enter"))
# for i in range(number_of_inputs):
#     user_input=int(input("Enter your number: "))
    
#     #check whether the number is pos, neg or 0 and add to relevent list
    
#     if user_input > 0:
#         positive_numbers.append(user_input)
#     elif user_input < 0:
#         negative_numbers.append(user_input)
#     else:
#         zeros.append(user_input)
# print(positive_numbers)
# print(negative_numbers)
# print(zeros)



# for i in range(len(list)): → i is an index → use list[i].
# for item in list: → item is already the value → no [] needed.



# scoresz = [2,3,5,6,7,8,9,12,4,6]


# for x in scoresz:
#     if x in range (0,len(scoresz),2):  #how is this only printing even numbers
#         print(x)
#         print(scoresz(x))
#         # print(list(range (0,len(scoresz),2)))


numbers = [23,30,60,35,23]
for number in numbers:
   print(number)
 
print('-----------------')  
for index in range(len(numbers)):
   if index%2 == 0: 
      print(numbers[index])


   
print('-------------------')
for i,value in enumerate(numbers):
   if i%2==0:
      print(value)
      
digits = [0, 1, 5]
for i in digits:
    print(i)
else:
   print("No items left.")




    

#Homework
'''
Description: You manage an online bookstore and have recorded today’s book sale prices in a list.
 Your task is to analyze these prices using if conditions, list operations and for loops.

1. Given the list sales_prices = [12.99, 45.00, 9.50, 75.20, 22.00, 150.00, 5.99], write a for loop to iterate over each price.
2. Inside the loop, use if conditions to classify each price as “budget” (price < 20), “standard” (20 <= price <= 50) or “premium” (price > 50).
3. Maintain three variables budget_count, standard_count and premium_count and increment the appropriate one for each price.
4. Create an empty list premium_sales and append every price classified as “premium” to this list.
5. After the loop finishes, print the values of budget_count, standard_count, premium_count and the premium_sales list.

'''
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
----------------------------------------------

(Nested for loop problem)
Branch Inventory Freshness Checker

You are given data about several bakery branches. Each branch has a list of baked items,
 and each item is represented as a list with three elements:

1. The item name (string),
2. Quantity available (int),
3. Days since baked (int).

Write a program that does the following:
1. Loop through each branch and then through each item in the branch using nested for loops.
2. For each item:

   * If the quantity is 0, print: 'Out of stock: {item name} at Branch {branch number}'
   * If the item is more than 2 days old, print: 'Stale item: {item name} at Branch {branch number}'
3. At the end, print how many total stale items were found across all branches.

**Example Input Structure:**
Expected use of concepts: nested for loops to iterate over branches and items, 
if conditions to check freshness and stock, and list indexing to access item details.

'''
branches = [
    [['Bread', 3, 1], ['Cake', 0, 0], ['Muffin', 2, 3]],
    [['Croissant', 5, 2], ['Pie', 0, 4]],
    [['Donut', 6, 0], ['Bagel', 1, 5]]
]
stale_count = 0
stale_count = []

# item_name = branches[row][column]     WRONG ROW AND COLUMN DONT EXIST YET, keep it under line 548 as there its defined!
# quantity = branches[row][column][1]
# branch_number = 

for row in range(len(branches)):
    for column in range(len(branches[row])):
        # print(branches[i],[j])    #wrong dont keep a comma 
        # [i]"which row number(branch)"
        # [j]"which item at that row(branch)"
        # branches[0][1] >That means: in row 0, take the 2nd item → "Cake" with quantity 0, days old 2.
        # if just keep branches[0]> get all branches at that branch >['Bread', 3, 1], ['Cake', 0, 0], ['Muffin', 2, 3]]
        #  if want names only>  print(branches[i][j][0]), quantity only>print [i][j][1]
        item_name = branches[row][column][0]     
        quantity = branches[row][column][1]
        branch_number = row+1
        age_item = branches[row][column][2]
        if quantity== 0:
            print(f"Out of stock,{item_name} at branch {branch_number}")

            #   2 WAYS TO DO LAST QS:
        if age_item > 2: #1
            print(f"Stale item,{item_name} at branch{branch_number}")
            # branches.count(age_item>2) >count(x) only works if the list directly stores the thing you’re looking for (x).
            stale_count += 1
print(f"total stale count: {(stale_count)}")
                         #OR 
         if age_item > 2:   
            stale_count.append(age_item)
print(f"total stale count: {len(stale_count)}")

# WHY BRANCHES.COUNT WONT WORK
# If you ask Python:
# ages = [1, 2, 3, 3, 4]
# ages.count(3)

# 👉 Python looks inside the list directly:
# Does this element equal 3?
# Yes / No
# Count them up.
# That’s why it works: the list itself has numbers (1,2,3,4).

# So instead of 3 sitting directly in the list, you have a basket like ["Bread", 3, 1].
# If you try:
# branches.count(3)
# 👉 Python goes:
# First basket = ["Bread", 3, 1] … is this the same as 3? ❌ No.
# Second basket = ["Cake", 0, 0] … is this the same as 3? ❌ No.
# Third basket = ["Donut", 2, 3] … is this the same as 3? ❌ No.
# So the answer is 0.

