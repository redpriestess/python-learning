
"1️⃣ Accessing values"
fruit_prices = {'apple': 3,
                'banana': 2, 
                'orange': 4, 
                'mango': 6}

"Q1: Print the price of 'orange'"
# print(fruit_prices['orange'])

"Q2: Print the price of 'mango'"
# print(fruit_prices['mango'])
# "2️⃣ Modifying values"
# "Q3: Change the price of 'banana' to 3"
# fruit_prices['banana']+=2
# print(fruit_prices)

"3️⃣ Adding new key–value pairs"
# # "Q4: Add a new fruit 'grapes' with price 7"
# # fruit_prices['grapes']=7

"4️⃣ Removing key–value pairs"
"Q5: Remove 'apple' from the dictionary"
# # fruit_prices.pop('apple')

"5️⃣ Looping through dictionary"
"Q6: Print each fruit name and its price in the format: 'apple costs 3'"
# # for fruit in fruit_prices:
# #     print(f"name {fruit} costs {fruit_prices[fruit]}")

"6️⃣ Using .items(), .keys(), and .values()"
"Q7: Print all fruit names using .keys()"
# # print(fruit_prices.keys())

"Q8: Print all fruit prices using .values()"
# # print(fruit_prices.values())
"Q9: Print both fruit and price together using .items()"
# # print(list(fruit_prices.items()))

"Q12 Small Challenge"
# # menu = {'Burger': 8, 'Pasta': 12, 'Sandwich': 6, 'Pizza': 10}

"Q13: Add 2 to the price of every item in the dictionary"

# # # for food in menu:
# # #     menu[food]+=2
# # #     print(menu)

# # for food,price in menu.items():
# #   menu[food]+=2  #cant keep [price], as in the dict it is not a list it is an integer so u can't update the dictionary. only w list u can.
# # print(menu) #KEEP PRINT HERE SO IT DONT PRINT ONLY ONE BY ONE

"KEY TAKEAWAY : CAN'T CHANGE VALUE BY DICT[VALUE] IF IT IS A INT, NEED USE DICT[KEY]
'''NEED ACCESS THE VALUE VIA THE KEY!'''


"1️⃣ Accessing values"
# student_score = {'Alice': 80, 'Bob': 72, 'Charlie': 90, 'Diana': 65,'Anna':11}

"Q1: Print the score of 'Charlie'"
# # print(student_score['Charlie'])

"Q2: Print the score of 'Diana'"
# # print(student_score['Diana'])

"2️⃣ Modifying values"
"Q3: Increase Bob's score by 5"
# # student_score['Bob']+=5
# # print(student_score)

"Q4: Decrease Diana's score by 10"
# student_score['Diana']-=10
# print(student_score)

"3️⃣ Adding new entries"
"Q5: Add a new student 'Eve' with score 88"
# student_score['Eve']=88
# print(student_score)

"4️⃣ Removing entries"
"Q7: Remove 'Alice' from the dictionary and store the removed score in a variable"
# removed_variable= student_score.pop('Alice')
# print(student_score)
# print(removed_variable)####

"5️⃣ Looping through dictionary"
"Q9: Print each student and score in the format: 'Alice scored 80'"

# for student in student_score:
#     print(f"student {student} has a score of {student_score[student]}")

"Q10: Print only the students who scored more than 80"

# # for student in student_score:
# #     if student_score[student]>80:
# #         print(f"congrats {student} u have brains") ####################### compare

# for student,score in student_score.items():
#     if score>80:
#         print(f"congrats {student} u have brains") #################### 

# #HERE U CAN USE .items() and use VALUE as u R NOT UPDATING DICTIONARY,N USING IF LOOP JUSR GETTING VALUES SO CAN!


"7️⃣ Updating values with loops"
"Q14: Increase every student's score by 3 using a loop" 
# #THINK: ARE VALUES INT OR LIST?
# # U WANT TO INCREASE THE VALUE, SINCE INT, NEED USE KEY TO ACCESS THE VALUE TO CHANGE IT

# for student in student_score:
#     student_score[student]+=3
# print(student_score) #kEEP HERE OUT LOOP SO PRINT ALL AT ONCE


"8️⃣ Small challenges"
"Q17: Double the score of any student who scored less than 70"

# for student in student_score:
#     if student_score[student]<70:
#         student_score[student]*=2
# print(student_score)


"Q18: Remove last student"

# # removed_pair = student_score.popitem()
# # print(removed_pair)
# # print(student_score) 

"Q18.5: Remove bob from list, print value "
# removed_pair = student_score.pop('Bob')
# print(removed_pair)
# print(student_score)

"Q19:Remove all students who scored less than 70"

# # for student in student_score:
# #     if student_score[student]<70:
# #     student_score[student].pop
    '''for student in student_score: THIS WONT WORK HERE ANYMORE. .POP CHANGES STRUCTURE OF DICT, LOOP KEEPS TRACK OF WHERE KEY IS. 
WHEN CHANGE STRUCTURE MID LOOPING, PYTHON GETS CONFUSED ON ACCURATE LOCATION OF KEY. SO NEED TO CONVERT TO LIST.
LIST IS USED AS COPY OF DICTIONARY, THATS FIXED SO WONT CHANGE MID LOOPING:
'''
# for student in list(student_score):
#     if student_score[student]<70:
#         student_score.pop(student)
# print(student_score)
   

"Q19: Merge another dictionary {'George': 85, 'Hannah': 92} into student_scores"

# new = {'George': 85, 'Hannah': 92}
# student_score.update(new)
# print(student_score)

"Q20: Create a new dictionary with only students who scored more than 80"

# smart = {}
# for student in list(student_score):
#     if student_score[student]>80:
#         # smart.append(student)#APPEND IS ONLY TO ADD an item to a list, not a key–value pair.
#         smart[student]=student_score[student]
# print(smart)

'REMOVING ENTRIES'
student_score_info = {'Roy':45,
                      'Sharon':32,
                      'Therese':67,
                      'Niran':89,
                      'Ravi':32}

'Q1: Remove \'Sharon\' from the dictionary and print the updated dictionary'
# student_score_info['Sharon'].pop
# print(student_score_info)

# student_score_info.pop('Sharon')
# print(student_score_info)

'Q2: Remove and return the last item from the dictionary using popitem()'


'MERGING AND UPDATING'
extra_scores = {"Alice": 78, "Bob": 82}

'Q3: Update student_score_info with extra_scores'
'Q4: Add a new student \'David\' with score 55 to student_score_info'

'CLEARING DICTIONARY'
'Q5: Clear all entries in student_score_info and print it'

'CREATING DICTIONARY FROM SEQUENCES'
animal_sounds = [('dog','bark'),('horse','neigh'),('cat','meow')]

'Q6: Convert animal_sounds to a dictionary'
'Q7: Print the sound of \'cat\' from the dictionary'

scores = [15,45,32,67,89,32]
names = ['Roy','Sharon','Therese','Niran','Ravi']


'''

