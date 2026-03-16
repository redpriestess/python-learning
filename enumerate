"""
Q:
- Use enumerate(libraries, start=1) for library numbering.
- If copies == 0, append title to out_of_stock and pop() the book from that library.
- If days_since_borrowed > 30, append title to old_stock.
- At the end, extend summary with out_of_stock + old_stock.
"""
# order for each book: [0] = title, [1] = copies, [2] = days_since_borrowed
libraries = [
    [["BookA", 0, 15], ["BookB", 3, 45]],
    [["BookC", 5, 10], ["BookD", 0, 60]],
    [["BookE", 2, 31]]
]

# out_stock = []
# old_stock = []

# for library_num,library in enumerate(libraries):
#     for i in range(len(library)-1,-1,-1):
#         title,copies,days_borrowed = library[i]
#         if copies == 0:
#             out_stock.append(title)
#             library.pop(i)
#         if days_borrowed > 30:
#             old_stock.append(title)
#         summary = out_stock+old_stock
# print(out_stock)
# print(old_stock)
# print(summary)


"""
Use enumerate(warehouses, start=1) for warehouse numbering.
- If quantity == 0, append the item name to out_of_stock and remove() it from that warehouse.
- If quantity < 3, append the item name to low_stock.
- At the end, print out_of_stock and low_stock.
"""
# order: [0] = name, [1] = quantity
warehouses = [
    [["Bolts", 0], ["Nails", 2], ["Screws", 10]],
    [["Hammers", 1], ["Drills", 5]],
    [["Wrenches", 0], ["Saws", 7]]
]

# out_of_stock = []
# low_stock = []

# for ware_num,warehouse in enumerate(warehouses,start=1):
#     for i in range(len(warehouse)-1,-1,-1):
#         name,quantity = warehouse[i]
#         if quantity == 0:
#             out_of_stock.append(name)
#             warehouse.pop(i)
#         elif quantity< 3:
#             low_stock.append(name)


# print(out_of_stock)
# print(low_stock)

"""
Use enumerate(classes, start=1) for class numbering.
- Count how many students scored exactly 100 and store in perfect_scores.
- Access and print the third student in each class if it exists.
- At the end, print perfect_scores.
"""
# order: [0] = student, [1] = score
classes = [
    [["Ravi", 55], ["Mei", 100], ["Ali", 77]],
    [["Sara", 100], ["Liam", 100]],
    [["Nora", 45], ["Tom", 60], ["Jin", 100]]
]

# perfect_scores = []
# the_count = 0

# for class_num,classe in enumerate(classes):
#     for student,score in classe:
#         if score == 100:
#             perfect_scores.append(student)
#             the_count+=1
#             # print(f"the total number of students who got 100 is {the_count}")> keep at bottom so dont print 4 times
# print(f"{perfect_scores} got 100")
# print(f"the total number of students who got 100 is {the_count}")

"""
Use enumerate(carts, start=1) for cart numbering.
- If an item == 'Chips', insert 'Dip' right before it.
- If an item == 'Cola', append 'Ice' after it.
- Pop the first item in each cart and store in removed_items.
- At the end, print removed_items.
"""
# cart items
carts = [
    ["Bread", "Chips", "Juice"],
    ["Cola", "Candy"],
    ["Water", "Chips"]
]

#Get the marks from the user. Make sure the marks are between 0 and 100. 
#The program should be able to handle wrong inputs and warn the user accordingly. For an instace
#The input should not have a space
#The input should always be numerical i.e: use answer.isnumeric() to check if the answer only 
#has numbers or not 
# If the marks are above 50, add them to pass_list. If not add them to fail_list. 
# The program should some how get an answer from the user. 
#The program should exit when the user enters 'done

# pass_list = []
# fail_list = []
# instructions = "only enter numbers, otherwise nothing will happen"
# print(instructions) 
# while True:
#     marks = input("what is your marks:")
#     if marks == "done":
#         break 
#     if marks.isnumeric(): #didntkeep()
#         marks = int(marks) #didnttype back marks = int(marks)
#         if marks > 0 and marks < 100:
#             if marks >50:
#                 pass_list.append(marks)
#             else:
#                 fail_list.append(marks)
#         else: 
#             print("marks need to be in range 0-100")
#     else:
#         print("you can only enter numbers")

# print(f"good job yall passed:{pass_list}")
# print(f"Failures: {fail_list}")




"""
Ask the user to enter grocery items one by one.  
Stop when they type 'done'.  
Do not allow spaces in the item name.  
If the item already exists in the list, warn the user.  
At the end, print the grocery list.  
"""
grocery_list = []

# user = "enter grocery items one by one, keep no spaces in item name"
# print(user)

# while True:
#     grocery = input("Please enter grocery items one by one:")
#     if grocery == "done":
#         break
#     if " " in grocery:
#         print("no spaces allowed")
#     elif grocery in grocery_list:
#         print("that item is mentioned twice")
#     else:
#         grocery_list.append(grocery)
# print(grocery_list)



'''''''''
Q:
- Use enumerate(tech_stores, start=1) for store numbering.
- If stock == 0, append gadget name to sold_out list AND remove() it from the store.
- If price > 1000, insert gadget name at the front (index 0) of premium list.
- At the end, extend final_report with sold_out + premium.

'''
# order for each gadget: [0] = name, [1] = price, [2] = stock
# stores = [
#     [["Phone", 800, 5], ["Laptop", 1500, 0]],
#     [["Tablet", 400, 2], ["Smartwatch", 200, 10]],
#     [["Camera", 1200, 0], ["Headphones", 100, 15]]
# ]

# sold_out = []
# premium_list = ["Samsung","iPhone"]

# for store_num,store in enumerate(stores):
#     for i in range(len(store)-1,-1,-1):
#         name,price,stock = store[i]
#         if stock == 0: 
#             sold_out.append(name)
#             store.pop(i) 
        
#         if price>1000:
#             premium_list.insert(0,name)

# print(premium_list)
# print(sold_out)
# print(stores)


'''
# Example: Skip even numbers and print only odd numbers from 1 to 10
number%2 
numbers =list(range(1,21,1))
'''
# numbers =list(range(1,21,1))
# index = 0
# while True:
#     if numbers[index]%2==0:
#         print(numbers[index])
#     else:
#         print("only even numbers. try again")
#     index+=1

#     if index>len(numbers):
#         break

#EASIER WAY: but WRONG:
# index=0
# while index<len(numbers):
    
#     number=numbers[index]
#     if number%2==0:
#         continue  #when keep> python jumps back to top of the loop. this will skip the index += 1
    
#     print(number) 
#     index+=1
#so When number is even (e.g., 2),
#it runs continue and never increases index.
#So index stays the same forever → infinite loop! 🔁😵
    
#CORRECT:
# numbers =list(range(1,21,1))
# index=0
# while index<len(numbers):
#     number=numbers[index]

#     if number%2==0:
#         index+=1
#         continue
#     print(number) 




#Look at what humans has to do reflect a fraction of our power

# odd_list=[]
# even_list=[]

# for number in numbers:
#     if number%2 == 0:
#         even_list.append(number)
#     else:
#         odd_list.append(number)
# print(odd_list)
# print(even_list)



'''
Function: A block of code, that can be reused and designed for a specific purpose 

Block of code: 
Reusability: 
Specific purpose: 
'''

#most simplest form of a function 
#creating a tool 
def greet():
    print("hello world")
    print("its a wonderful life")
    print("be thankful")
    print("chao")    
    print("--------------------")
#using the tool 

# greet()
# greet()
# greet()

#creating a function with a parameter
# def greet(name):
#     print(f"Hello {name}!")
    
# greet("Rishka")
# greet("riri")


# def voting_age_checker(name,age):
#     if age>=18:
#         print(f"Hi {name}, please proceed to the voting center")
#     else:
#         print(f"Hi {name}, you are old enough to vote")
        
# # Create a function that will take two numbers, add them and print the result

# def add_two_numbers(number_1,number_2):
#     return number_1 + number_2

# result=add_two_numbers(2,3)
# print(result)

# #use the above add_numbers function you created to get the sum of all the numbers in the nums list
# nums = [10,20,30,40]
# # print(nums[0]+nums[1]+nums[2]+nums[3])

# #function chaining
# final=add_two_numbers(add_two_numbers(nums[0],nums[1]),add_two_numbers(nums[2],nums[3]))
# print(final)

# print(2+2)