
# Adding data to the script

name = 'Jonathan' #string (str)- names, locations, sentences 
age = 34 # integer (int)- 10,1,0,1000000,-67
weight = 65.5 # floating point numbers (float) - 10.56,-98.5,0.000012, 1.0
hasPet = False # Boolean (bool)- To represent variables with only two outcomes 
petName = None # None type variable (None)- to represent nothingneses, create references for empty variables

#Recording the scores a class of 4000 students got for mathematics
# charliesSCores=int(input("Please enter charlies scores"))
# lydiaSCores=int(input("Please enter lydia scores"))

'''
COLLECTIONS IN PYTHON 

lists<<<<<<<<
tuples
dictionaries
sets

list_name = [45,78,49,23,67,23,75,23,89,65,53]

'''
#int list- homogenous
scores = [45,78,49,23,67,23,75,23,89,65,53,78,49,23,67,23,75,23,89,65,5,78,49,23,67,23,75,23,89,65,5]

#functions- regular radios
# print()
# type()
# input()

#methods- car radios
# append()
# insert()
# extend()

print(scores)

#index= the unique address of each element
#index start with 0  and increment by 1 for each element
#each element has a postive index and a negative one

#string list- homogenous
names = ['Roy','Sharon','Therese', 'Ravi']
#          0       1         2        3
#         -4      -3        -2       -1
       

#non-homegeous list 
info=['Jonathan',45,67.5,False,['Dean',21,45.6,True]]

#printing using positive indexing 
print(names[3])
#printing using negative indexing
print(scores[-2])

#list slicing
#list_name[start:end:step_size]
# print(names[0:3:1]) here use col(:)
scores = [45,78,49,23,67,23,75,23,89,65,53,78,49,23,67,23,75,23,89,65,5,78,49,23,67,23,75,23,89,65,5]
# print(scores[0:8:2])

#print 23, 89, 78, 67
print(scores[5:16:3])

#Modifying lists

#Adding values to a list

#adding an element to the end of the list 
print(names)
names.append('shanthi')
print(names)


#creating an empty list 
locations= []

#A real example of append method in use
# guest_list=[]
# while True:
#     guest_name=input("Please enter your name (Enter done to exit program): ")
#     if guest_name=='done':
#         break
#     else:
#         guest_list.append(guest_name)
#         print(guest_name)
        

#adding an element at the middle of the list
print(names)
names.insert(2,'Hillary')
print(names)

#niranjala, claude, antony, marian

names2=['niranjala','claude','antony','marian']

#create a new list by combining the original list and additional list (original data is preserved)
all_names= names + names2
print(all_names)

# extending the original  list
print(names)
names.extend(names2)
print(names)

'''
Create a program to manage a grocery shopping list.  

1. Start by creating an empty shopping list. 
2. Add the following items to the list using the appropriate method:
   - Milk
   - Bread
   - Eggs
3. Realize you forgot to add "Butter" to the end of the list and "Bananas" at the beginning.
4. Access and print the third item on the list (using indexing).  #help
5. Replace "Bread" with "Whole Grain Bread". 
6. A friend gives you their list of items: ["Apples", "Oranges", "Cheese"]. Add all of these items to your list in one step.  
7. Remove "Cheese" from the list 
8. Remove "Whole grain bread" from the list 

Print the list after every step to make sure that you changes worked. 

'''
grocery = [] #qs1help- is this right
grocery = ["milk","bread","eggs"] #qs2
print(grocery)
grocery.insert(0,"bananas") #qs3
grocery.append("butter")  #qs3help when i keep -1 it doesnt go to end but when i keep 4 it does??
print(grocery)
grocery[2]="whole grain bread" #qs5
print(grocery)
grocery_2 = ["Apples", "Oranges", "Cheese"] #qs6
all_grocery = grocery + grocery_2 
print(all_grocery)
all_grocery.remove("Cheese") #qs7
print(all_grocery)
all_grocery.remove("whole grain bread")#qs8
print(all_grocery)

#pop method
print(names)
removed_name=names.pop()
print(names)
print(removed_name)

print('------------------')
# removing an element using the remove method
#this will remove the first occurence of the element in question
names.append('John')
names.append('antony')
print(names)
names.remove('antony')
print(names)

#using the pop method with the index
names.pop(2)
print(names)

names.clear()
print(names)

# Strings are character lists
first_name='Dean' # ['D','e','a','n']
middle_name= 'Matthew'
last_name = 'Winchester'

#Create the name with initialis using the first_name, middle_name and last_name
#Use f strings to print it
print(f"{first_name[0]}. {middle_name[0]}. {last_name}")

#print the full name 
print(f"{first_name} {middle_name} {last_name}")

full_name=first_name + ' ' + middle_name + ' ' + last_name
print(full_name)

#membership test
if 'D' in full_name:
    print("The letter D is in the person's name")
else:
    print("The letter is not there")
   
#USEFUL BUILT IN FUNCTIONS
scores = [43,56,35,23,78,34,87,56,35,24]
names = ['olivia', 'farid','anaya', 'petra', 'farid', 'arun', 'farid']

total = sum(scores)
highest = max(scores)
lowest = min(scores)
count = names.count("farid")

#multi dimensional - matrix
numbers = [[1,2,3],
           [4,5,6],
           [7,8,9]]

print(numbers[0][1])
print(numbers[1][1])

'''

------------------- Homework 1----------------------------
Your program will manage a music playlist and use conditional statements to handle a task.

1. Initialize an empty playlist.
2. Add the songs "Imagine", "Bohemian Rhapsody", and "Hotel California" to the playlist.
3. Realize you forgot to add "Stairway to Heaven" at the end and "Yesterday" at the beginning.
4. Check if "Imagine" is the first song of the list. 
If that is the case check if "Bohemian Rhapsody" is the second song. If so add the song "Hymn for the weekend" to the playlist. If not remove the third song from the list.  
5. Create another playlist with 3 of your favourite songs and add them to the original playlist.

''' 

playlist = [] #1
playlist = ["Bohemian Rhapsody","Hotel California"] #2
print(playlist)
playlist.append("Stairway to Heaven")#3
playlist.insert(0,"Yesterday")#3
print(playlist)
if playlist[0]=="imagine":#4
    if playlist[1]=="Bohemian Rhapsody":#4
        playlist.append("Hymn for the weekend")#4
        print(playlist)
    else:
        playlist.pop(2)
        print(playlist)
else:
    playlist.pop(1)#4
    print(playlist)

rishka_fav = ["no broken hearts","woa","pocketful of sunshine"]#5
playlist_2 = playlist + rishka_fav
print(playlist_2)
        


'''
------------------------- Homework 2 --------------------------

Your program will calculate a customer’s monthly phone bill based on usage and plan, then demonstrate list operations on the history of bills.

1. Use input() to prompt for the customer’s name and store it in a variable called customer_name.
2. Use input() to prompt for the total minutes used (as a float) and store it in minutes_used.
3. Use input() to prompt for the plan type ("Standard" or "Premium") and store it in plan_type.
4. If minutes_used is 200 or less, set rate to 0.20; if it’s between 201 and 500 inclusive, set rate to 0.15; otherwise set rate to 0.10.
5. Calculate bill_before_discount by multiplying minutes_used by rate.
6. If plan_type is "Premium", set discount_rate to 0.05; otherwise set discount_rate to 0.0.
7. Calculate discounted_amount by subtracting bill_before_discount × discount_rate from bill_before_discount.
8. Apply a 7% tax to discounted_amount and store the result in final_bill.
9. Use an f-string to print:
   Customer {customer_name}, your final bill for {minutes_used} minutes on the {plan_type} plan is ${final_bill:.2f}.
10. Define an empty list called bill_history.
11. Append final_bill to bill_history.
12. Access and print the first bill in bill_history using positive indexing.
13. Access and print the most recent bill using negative indexing.
14. If the first bill in bill_history is greater than 100, replace it with 100.
15. If there is a bill equal to 0 in bill_history, remove it.
16. Create another list called extra_charges containing [5.0, 10.0] and extend bill_history with it.
17. Print the updated bill_history list.
'''

customer_name = input("Please enter your name:")
minutes_used = float(input("How many minutes were used:"))
plan_type = input("what was the plan type(standard or premium?:)")



if minutes_used<=200:
    rate = 0.20
elif minutes_used>=201 and minutes_used <= 500:
    rate = 0.15
else:
    rate = 0.10

bill_before_discount = minutes_used * rate
print("bill before discount:",bill_before_discount) 

if plan_type == "premium":
    discount_rate = 0.05
else:
        discount_rate = 0
print("discount rate:",discount_rate)

bill_after_discount = bill_before_discount-(discount_rate * bill_before_discount)
print("bill after discount:",bill_after_discount) 
final_bill = bill_after_discount + (bill_after_discount*0.07)
print("final bill after discount with 7% tax:",final_bill)
print(f"Customer {customer_name}, your final bill for {minutes_used} minutes on the {plan_type} plan is ${final_bill:.2f}")

bill_history = []
bill_history.append(final_bill)
print("first bill:",bill_history[0])
print("most recent bill:",bill_history[-1])
if bill_history[0] > 100:
    bill_history[0] = 100
if bill_history == 100:
    bill_history.clear[0]
print(bill_history)

extra_charges = [5.0, 10.0]
updated_bill_history = extra_charges + bill_history
print(updated_bill_history)