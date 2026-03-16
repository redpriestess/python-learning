'''
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
# branches = [
#     [['Bread', 3, 1], ['Cake', 0, 0], ['Muffin', 2, 3]],
#     [['Croissant', 5, 2], ['Pie', 0, 4]],
#     [['Donut', 6, 0], ['Bagel', 1, 5]]
# ]


# stale_days = 0
# for row in range(len(branches)):
#     for column in range(len(branches[row])):
#         quantity = branches[row][column][1]
#         item_name = branches[row][column][0]
#         days = branches[row][column][2]
#         branch = row+1
#         # if quantity == 0:
#             # print(f"Out of stock:{item_name} at branch {branch}")

#         if days < 2:
#             print(f"stale item: {item_name} at branch {branch}")
#             stale_days +=1
#             print(f" the total stale items found is {stale_days}")




  #   2 WAYS TO DO LAST QS:
#         if age_item > 2: #1
#             print(f"Stale item,{item_name} at branch{branch_number}")
#             # branches.count(age_item>2) >count(x) only works if the list directly stores the thing you’re looking for (x).
#             stale_count += 1
# print(f"total stale count: {(stale_count)}")
#                          #OR 
#          if age_item > 2:   
#             stale_count.append(age_item)
# print(f"total stale count: {len(stale_count)}")

# School Grades Report
# You are given a list of classes. Each class has a list of students, and each student is represented as [name, grade].
# Print each student’s name and grade.
# If a student’s grade is below 40, print: "Fail: {name} in Class {class_number}".
# At the end, print how many students passed in total.
# '''
# passed_students = 0
# students = [
#     [["rishka",100],["jeff",45],["siddarth",10],["Aryan",89]],
#     [["annie",43],["raj",34]],
#     ]
# # for row in students:
# #     for column in students[row]: Python crashes, because row is a list, not an integer index.
# #         print([row][column])
# for row in range(len(students)):
#     for item in range(len(students[row])):
#         print(students[row][item])
#         passing_grade = 40
#         name = students[row][item][0]
#         grade = students[row][item][1]
#         class_number = row
#         if grade < passing_grade:
#             print(f"Student {name} in class {class_number} failed")
#         else:
#              print(f"Student {name} in class {class_number} passed")
#              passed_students+= 1
# print(passed_students)

'''
You are given data about several school libraries. Each library has a list of books,
and each book is represented as a list with three elements:

The book title (string)
Number of copies available (int)
Days since last borrowed (int)

Task:
Write a program that does the following:
Loop through each library and then through each book using nested for loops.
For each book:
If the number of copies is 0, print:
'Out of stock: {book title} at Library {library number}'
If the book has not been borrowed for more than 30 days, print:
'Old stock: {book title} at Library {library number}'
At the end, print how many total “old stock” books were found across all libraries.
'''
libraries = [
    [['Harry Potter', 3, 10], ['Percy Jackson', 0, 5], ['Matilda', 2, 45]],
    [['Sherlock Holmes', 1, 60], ['Jungle Book', 0, 20]],
    [['Cinderella', 5, 31], ['Moby Dick', 2, 2]]
]


# total_old_stocks = 0

# for row in range(len(libraries)):
#     for column in range(len(libraries[row])):
#         name = libraries[row][column][0]  #all must be kept under 2nd for
#         no_copies = libraries[row][column][1]
#         days_borrowed = libraries[row][column][2]
#         library = row+1
        

    # if no_copies == 0:             WRONG KEEP IT IN THE LOOP
#     #     print(f"out of stock:{name} at library number {library} ")
        
        # if no_copies == 0:  #CORRECT, KEEP IN BOTH LOOPS NOT JS ONE
            # print(f"out of stock:{name} at library number {library} ")

#         if days_borrowed < 30:
#             print(f"Old stock: {name} at library number {library}")
#             total_old_stocks +=1
#             print(f"the total number is {total_old_stocks}")


            


'''
USING ENUMERATE = UNPACKING
for lib_num, library in enumerate(libraries, start=1): #keep enumerate(lib)> gives row number to each row and lists out which row values its assigned to.
    for title, no_copies, days_borrowed in library:      # direct unpacking
        if no_copies == 0:
            print(f"Out of stock: {title} at Library {lib_num}")
'''


'''
Unpacking focus
CONCEPT:
for group_num, group in enumerate(groups, start=1):
    for a, b, c in group:   # unpacking directly
'''
''''      
 Q/ Given a list of movie theaters, where each theater has movies in the form [title, seats_left, days_running], 
unpack the values directly in the loop.
Print Sold out: {title} at Theater {theater number} if seats_left == 0.
Print Long running: {title} at Theater {theater number} if days_running > 100.
At the end, print the total number of long-running movies 
'''
theaters = [
    [["Avengers", 0, 120], ["Inception", 20, 50], ["Frozen", 5, 200]],
    [["Titanic", 0, 300], ["Joker", 15, 90]],
    [["Avatar", 10, 150], ["Shrek", 0, 20]]
]

# long_running = 0
# for theater_num, theater in enumerate(theaters,start =1):
#     for title, seats_left,days_running in theater:
#         if seats_left == 0:
#             print(f"Sold out {title} at theater {theater_num}")
#         if days_running>100:
#             print(f"Long running: {title} at Theater {theater_num}")
#             long_running += 1
#             print(long_running)

"""
Q:
- Print "Out of stock: {dish} at Restaurant {number}" if quantity == 0.
- Print "Expensive: {dish} at Restaurant {number}" if price > 15.
- At the end, print how many "Japanese" dishes are in stock
  and how many expensive dishes were found.
 
"""

restaurants = [
    [["Pasta", 12.5, 0, "Italian"], ["Burger", 8.0, 15, "Fastfood"]],
    [["Sushi", 20.0, 2, "Japanese"], ["Ramen", 10.0, 0, "Japanese"]],
    [["Steak", 25.0, 5, "Grill"], ["Salad", 6.5, 20, "Healthy"]]
]

# exp_dish = 0
# in_stock = 0
# for restaurant_num,restaurant in enumerate(restaurants):
#     for dish, price, quantity, cuisine in restaurant:
#         if quantity == 0:
#             print(f"Out of stock:{dish} at {restaurant_num}")
#         else:
#             in_stock += 1
#             print(f"There are {in_stock} number of dishes in stock")
#         if price > 15:
#             print(f"Expensive: {dish} at Restaurant {restaurant_num}")
#             exp_dish+=1
#             print(f"there are {exp_dish} number of dishes that are expensive")


hospitals = [
    [["John", 45, "Critical", 10], ["Anna", 30, "Stable", 2]],
    [["Mike", 70, "Critical", 20], ["Sara", 60, "Stable", 15]],
    [["Raj", 50, "Critical", 5], ["Lily", 25, "Stable", 1]]
]
"""
Q:
- Print "Urgent: {name} at Hospital {number}" if condition == "Critical"
  and days_in_hospital > 7.
- Print "Long stay: {name} at Hospital {number}" if days_in_hospital > 10.
- At the end, count how many urgent patients and how many long stays overall.
Each entry: [name, age, condition, days_in_hospital]
"""
# critcal_hospital = 0
# too_long = 0

# for hospital_num,hospital in enumerate(hospitals):
#     for name, age, condition, days_in_hospital in hospital:
#         if condition == "Critical":
#             if days_in_hospital>7:
#                 print(f"Urgent:{name} at {hospital_num}")
#                 critcal_hospital+= 1
#                 print(f"theres {critcal_hospital} number of critical patients")
#         if days_in_hospital>10:
#             print(f"{name} has been at hospital {hospital_num} for too long")
#             too_long+= 1
#             print(f"there's been {too_long} ppl that been here too long")

       
'''
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

# '''
# total_stale = 0

# branches = [
#     [['Bread', 3, 1], ['Cake', 0, 0], ['Muffin', 2, 3]],
#     [['Croissant', 5, 2], ['Pie', 0, 4]],
#     [['Donut', 6, 0], ['Bagel', 1, 5]]
# ]

# for branch_num,branch in enumerate(branches):
#     for item_name,quantity,days_baked in branch:
#         if quantity == 0:
#             print(f"{item_name} is Out of stock at branch {branch_num}")
#         if days_baked > 2:
#             print(f"{item_name}  is a stale item at branch {branch_num}") 
#             total_stale +=1
#             print(f"the total stale number of items is {total_stale}")

''''
.pop(index) → remove by position> NEED index
.remove(value) → remove by matching the VALUE

you cannot .pop("Banana"), because "Banana" is not an index.

'''

"""
NESTED FOR LOOPS+ APPENDING/REMOVING/EXTENDING
Q:
- Use enumerate for store numbering.
- If quantity == 0, append the fruit to an out_of_stock list,
  and pop() it from the store’s list.
- If quantity < 5 (but not 0), insert "Restock soon: {fruit}" into a warnings list.
- At the end, extend a results list with out_of_stock and warnings.

[0] = fruit_name, [1] = quantity
"""
stores = [
    [["Apple", 5], ["Banana", 0], ["Mango", 10]],
    [["Orange", 0], ["Pear", 3]],
    [["Kiwi", 7], ["Grapes", 0]]
]

# out_stock = []
# warning_list= []
# results = []
# for store_num,store in enumerate(stores):
#     for fruit_name,quantity in store:
#         if quantity == 0:
#             out_stock.append(fruit_name)
#             store.remove([fruit_name,quantity])   #here use remove as we are removing a value

        
# for store_num, store in enumerate(stores, start=1):
#    for i in range(len(store)-1,-1,-1):#done to get i value
#     fruit_name,quantity = store[i] #unpacking
#     if quantity == 0:
#         out_stock.append(fruit_name)
#         store.pop(i)
#     if quantity<5 and quantity>0:
#         warning_list.append(f"restock soon:{fruit_name}")
#     results = out_stock + warning_list

        
# print(out_stock)
# print("Stores after popping:", stores)
# print(warning_list)
# print(results)

'''
for i in range(len(store)-1,-1,-1):
store = [["Apple", 5], ["Banana", 0], ["Mango", 0]]

makes: len(Store)=3

1. range(2, -1, -1) is created
This makes a sequence: [2, 1, 0].
Python doesn’t run the loop body yet, it just prepares these numbers.

2. First iteration starts: i = 2
Python takes the first number from the range.

3. fruit_name, quantity = store[i]
Python looks at store[2] and unpacks it.

Example: if store[2] = ["Mango", 0] →
fruit_name = "Mango", quantity = 0.

4. if quantity == 0:
Python checks the condition.
If it’s True, move inside the if.
If False, skip the pop(i).

5. store.pop(i) (only if the if was True)
Removes the element at index i.
In this case, it removes ["Mango", 0].

6. Next iteration: i = 1
Go back to Step 3, repeat.

7. Last iteration: i = 0
Again, repeat Steps 3–5.

⚡ In short:
range comes first (before loop runs).
'''


"""
Q:
- Use enumerate(schools, start=1) for school numbering.
- If score < 40, append the student name to fail_list
- If score >= 90, append the student name to honors_list.
- After all schools are checked, extend all_results with fail_list + honors_list.
"""
# order for each student: [0] = name, [1] = score
# schools = [
#     [["Alice", 85], ["Bob", 35], ["Cara", 55]],
#     [["Dan", 90], ["Eva", 20]],
#     [["Finn", 70], ["Gina", 40], ["Henry", 95]]
# ]

# fail_list = []
# honor_list = []
# for school_num,school in enumerate(schools):
#     for i in range(0,len(school),1):
#         name,grade = school[i]
#         if grade <40:
#             fail_list.append(f"{name} got {grade}")
#         elif grade>=90:
#             honor_list.append(f"{name} got {grade}")

# print(fail_list)
# print(honor_list)

"""
Q:
- Use enumerate(tech_stores, start=1) for store numbering.
- If stock == 0, append gadget name to sold_out list AND remove() it from the store.
- If price > 1000, insert gadget name at the front (index 0) of premium list.
- At the end, extend final_report with sold_out + premium.

"""
# order for each gadget: [0] = name, [1] = price, [2] = stock
stores = [
    [["Phone", 800, 5], ["Laptop", 1500, 0]],
    [["Tablet", 400, 2], ["Smartwatch", 200, 10]],
    [["Camera", 1200, 0], ["Headphones", 100, 15]]
]

sold_out = []
premium_list = ["Samsung","iPhone"]

for store_num,store in enumerate(stores):
    for i in range(len(store)-1,-1,-1):
        name,price,stock = store[i]
        if stock == 0: 
            sold_out.append(name)
            store.pop(i) 
        
        if price>1000:
            premium_list.insert(0,name)

print(premium_list)























