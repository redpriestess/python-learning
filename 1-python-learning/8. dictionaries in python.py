'''
1. data types and variables = record data into our program 
2. if conditional - how to make data driven decision 
3. list - record data into our progoram in scale
4. for loops- manipulate data at scale
5. tuples - enforce convention (protected collections) among other thigns
7. while - we can do things until something happens or not happens
8. dictionaries-provides data cohesion

word -> meaning
we use the word to get to the meaning

key -> value
map -> treasure
key, value pairs

'''

student_names=['Roy','Sharon','Ravi','Therese','Niran','Shanthi']

scores =[45,76,86,33,24,67]

#Roy scored 45
for i in range(len(student_names)):
    print(f"{student_names[i]} scored {scores[i]}") 
    

student_score_info={'Roy':56,
                'Sharon':76,
                'Ravi':86,
                'Thereses':33,
                'Niran':24,
                'Shanthi':67}

for student in student_scores:
    print(f"{student} got {student_scores[student]}") #“Go to the dictionary student_scores, and find the value for this key (student).”
    
for student, score in student_scores.items():
    print(f"{student} got {score}")

#ACCESSING DICTIONARY DATA
print(student_score_info['Roy'])

print(student_score_info)
#MODIFY AN ELEMENT
student_score_info['Roy']=65

#ADDING A NEW KEY VALUE PAIR 
student_score_info['Shiromi']=99
#dictionaries are ordered. so the new value will append to the end. 

print(student_score_info)

#DICTIONARY METHODS

#GETTING A LIST OF KEYS
print(student_score_info.keys())
print(list(student_score_info.keys()))

# GETTING A LIST OF VALUES
print(student_score_info.values())

#GETTING A LIST OF KEY,VALUE PAIRS
print(student_score_info.items())

#CHECKING MEMBERSHIP
if "Roy" in student_score_info:
	print("Roy’s score is recorded")
 


'''
This problem is about managing the daily sales record of a small fruit stand using Python dictionaries. 
You will use concepts such as defining a dictionary, accessing and modifying entries, adding new key-value pairs, retrieving keys, 
values and items, iterating over entries, checking membership and safely retrieving values.

1. Create a dictionary called daily_sales that records the number of each fruit sold today using the following data
   a. apples: 30
   b. bananas: 45
   c. cherries: 25
   d. dates: 15
   e. elderberries: 10

2. Print the number of bananas sold by accessing the appropriate value in daily_sales

3. Print the entire daily_sales dictionary

4. A customer bought 5 more apples. Update the apples entry in daily_sales accordingly

5. The stand just started selling buah nanas and sold 12 of them. Add buah nanas to daily_sales with the correct count

6. Print a list of all fruit names sold today by retrieving the keys from daily_sales

7. Print a list of all quantities sold today by retrieving the values from daily_sales

8. Print a list of tuples where each tuple contains a fruit name and its quantity by retrieving 
the items from daily_sales

9. Use a for loop to iterate over daily_sales and print statements of the form Fruit: quantity sold

10. Check if grapes are in daily_sales and print an appropriate message if they are or are not

11. Safely attempt to get the number sold of grapes from daily_sales using a method that does not raise an error and print the result
'''


#1
daily_sales = {
    'apel':87,
    'pisang':98,
    'ceri':86,
    'tarikh':76,
    'elderberry':54
    }
#2
print(daily_sales['pisang'])
#3
print(daily_sales)
#4
daily_sales['apel']=daily_sales['apel']+5
print(daily_sales['apel'])
#5
daily_sales['buah nanas']=12

#6
print(list(daily_sales.keys()))
#7
print(list(daily_sales.values()))
#8
print(list(daily_sales.items()))

for daily in daily_sales:
    print(f"buah buahan {daily} : {daily_sales[daily]}")

if 'anggur' in daily_sales:
    print("anggur in daily sales")
    print(daily_sales['anggur'])

else:
    print("anggur not in daily sales")

print(daily_sales.get('anggur','Buah buahan tidak sdalem'))

daily_sales['anggur']= 90
print(daily_sales)

'''

'''
#REMOVING ENTRIES

student_score_info = {'Roy':45,
                      'Sharon':32,
                      'Therese':67,
                      'Niran':89,
                      'Ravi':32}

#REMOVING A KEY VALUE PAIR AND RETURNING VALUE
#(POP REQUIRES THE KEY TO WORK)
value=student_score_info.pop('Ravi')
print(student_score_info)
print(value)

#REMOVING A KEY VALUE PAIR AND RETURNING THE PAIR
#(POPITEM DOES NOT REQUIRE AN ARGUMENT TO WORK)
pair=student_score_info.popitem()
print(student_score_info)
print(pair)


#MERGING AND UPDATING 
extra_scores = {"Alice": 78, "Bob": 82}
student_score_info.update(extra_scores)    # bulk-add or overwrite

#CLEARING
student_score_info.clear()
print(student_score_info)

#CRATE A DICTIONARY FROM A SEQUENCES

# creating a dictionary from a list of tuples
animal_sounds= [('dog','bark'),('horse','neigh'),('cat','meow')]
animal_sounds_dict=dict(animal_sounds)
print(animal_sounds_dict)

scores = [15,45,32,67,89,32]
names = ['Roy','Sharon','Threse','Niran','Ravi']

dict_from_seq=dict(zip(names,scores))
print(dict_from_seq)

#NESTED DICTIONARIES 
students_info={
    'Roy':{'Math':44,'Science':43,'Env. studies':98},
    'Sharon':{'Math':45,'Science':43,'Env. studies':98}
    }
print(students_info['Roy']['Science'])





#CHATGPT QS

# "1️⃣ Accessing values"
fruit_prices = {'apple': 3,
                'banana': 2, 
                'orange': 4, 
                'mango': 6}

# "Q1: Print the price of 'orange'"
# print(fruit_prices['orange'])

# "Q2: Print the price of 'mango'"
# print(fruit_prices['mango'])

# "2️⃣ Modifying values"
# "Q3: Change the price of 'banana' to 3"
# # fruit_prices['banana']= fruit_prices['banana']+1
# # print(fruit_prices)
# fruit_prices['banana']+=1
# print(fruit_prices)
# "3️⃣ Adding new key–value pairs"
# "Q5: Add a new fruit 'grapes' with price 7"
# fruit_prices['grapes']=7
# print(fruit_prices)

# "4️⃣ Removing key–value pairs"
# "Q7: Remove 'apple' from the dictionary"
# fruit_prices.pop('apple')
# print(fruit_prices)


# "5️⃣ Looping through dictionary"
# "Q9: Print each fruit name and its price in the format: 'apple costs 3'"
# for fruit in fruit_prices:
#     print(f"{fruit} costs {fruit_prices[fruit]}")



# "6️⃣ Using .items(), .keys(), and .values()"
# "Q10: Print all fruit names using .keys()"
# print(fruit_prices.keys())

# "Q11: Print all fruit prices using .values()"
# print(fruit_prices.values())

# "Q12: Print both fruit and price together using .items()"
# print(fruit_prices.items())


# "2)"
# food = ['Burger', 'Pasta', 'Sandwich']
# price = [8, 12, 6]

# "Q1: Create a dictionary called menu where each food name is the key and its price is the value"
# menu = {'burger':8,
#         'pasta':12,
#         'sandwich':6}

# "Q2: Print the menu dictionary"
# print(menu)

# "Q3 Small Challenge"
# menu = {'Burger': 8, 'Pasta': 12, 'Sandwich': 6, 'Pizza': 10}

# "Q4: Add 2 to the price of every item in the dictionary"

# for food in menu:
#     menu[food]+=2
#     print(f"{food} costs {menu[food]} ")

# "Print the updated dictionary"




'''--------------------- HOMEWORK 1 ------------------------------
A small online bookshop wants to analyze customer reviews to determine how many books have been marked as 'recommended' by readers. 
The data is stored as a nested dictionary where each key is a customer name and the value is another dictionary containing book titles
 and whether the customer recommended them or not. Use for loops to iterate through the data and if conditions to count 
 and display information.'''



# 1. Define a nested dictionary named `customer_reviews` with the following structure:
# '''
# customer_reviews = {
#     'Alice': {'1984': True, 'Dune': False, 'The Hobbit': True},
#     'Bob': {'Dune': True, '1984': True},
#     'Catherine': {'The Hobbit': False, 'Dune': False},
#     'Daniel': {'1984': True, 'The Hobbit': True, 'Dune': True}
# }

# '''
# 2. Write a program that uses a for loop to go through each customer.

# '''
# book_recommendations = {}
# # for names in range(len(customer_reviews)):#only used for lists, do .items() for dictionaries!!
# for customer, reviews in customer_reviews.items():
#     # print(f"customer name:{customer}{reviews}") #printseverything
#     # for books,recommended in customer_reviews.items(): #WRONG, loop over INNER PART ONLY
#     for books,recommended in reviews.items():
#         if recommended:
#             if books in book_recommendations:
#                 book_recommendations[books]+=1
#             else:
#                 book_recommendations[books]=1
        
# for book,count in book_recommendations.items():
#     print(f"book name {book} has {count} recommendations")


'''---------------------------- HOMEWORK 2 -----------

You are building a basic patient triage system for a small clinic. The system should take patient names and symptoms, 
then use a dictionary to classify them into severity levels. This exercise involves  dictionaries, nested if conditions, 
lists, and a while loop to continuously process patients.

Problem: Patient Triage System Using Dictionary, While Loops, and Nested If Statements

1. The clinic wants to maintain a list of patients and categorize them into one of three urgency levels:
 'high', 'medium', or 'low'. The categorization is based on symptom severity.

2. Initialize an empty dictionary called triage with keys 'high', 'medium', and 'low'. Each key should map to an empty list.

3. Set up a while loop that keeps running until the user types 'done' when prompted for a patient name.

4. For each patient, prompt the user to enter a symptom (e.g., 'chest pain', 'headache', 'fever', etc.).

5. Use a nested if-elif-else structure to classify the patient:

   * If the symptom is 'chest pain' or 'breathing difficulty', categorize as 'high'.
   * If the symptom is 'fever' or 'headache', categorize as 'medium'.
   * All other symptoms should be treated as 'low'.

6. Append the patient's name to the appropriate list inside the triage dictionary.

7. After the loop ends, print out the names of patients under each triage category.'''


# triage = {
#     "high": [],
#     "medium": [],
#     "low": []
# }

# while True:

#     user = input("Enter patient name: ")

#     if user == "done":
#         break

#     symptom = input("Enter symptom: ")

#     if symptom in ["chest pain", "breathing difficulty"]:
#         triage["high"].append(user)

#     elif symptom in ["fever", "headache"]:
#         triage["medium"].append(user)

#     else:
#         triage["low"].append(user)

# print("High urgency:", triage["high"])
# print("Medium urgency:", triage["medium"])
# print("Low urgency:", triage["low"])



