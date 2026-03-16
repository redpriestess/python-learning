'''
Make decisions or take actions based on data

CONDITION will always evaluate to a boolean 
TYPE 1- if loop
if CONDITION:
    STATEMENT
    
Type 2: if else loop 
if CONDITION:
    STATEMENT1
else:
    STATEMENT2
    
Type 3: if elif, else (used if you want to keep ranges in)
if CONDITION: 
    STATEMENT1
elif CONDTION:
    STATEMENT2
else:
    STATEMENT

TYPE 4: nested if loops: if loop inside if loop 

if CONDITION: 
    if CONDITION: 
        STATEMENT1
    else:
        STATEMENT2
else:
    STATEMENT3

'''

rishka=2<3
if rishka:
    print("hello")
if False:
    print("world!")

# rishka_has_time=False # assignment (one equal)

# if rishka_has_time==True: #comparison (two equal signs)
#     print("Rishka will have breakfast at home")
    
# if rishka_has_time==True:
#     print("Rishka will have breakfast at home")
# else:
#     print("Rishka will have breakfast at school")
    
#get the users age. If they are 18 or above, print "you can vote now"
#otherwise print "you cannot vote yet"

# user_age = int(input("Please enter your age"))
# if user_age >= 18:
#     print("You can vote now")
# else:
#     print("You can't vote")
    
'''
Get the user's score and assign the grade as below
marks between 0(0 included) and 25 (Fail)
25(included) and 50 (C)
50(included) and 75 (B)
75 (included) and 100 (A)


0--------25-----------50------------75--------100
     F          C             B           A 
'''

# user_marks=int(input('Please enter your marks: '))

# if user_marks>=75:
#     grade = 'A'
# elif user_marks>=50 and user_marks<75:
#     grade = 'B'
# elif user_marks>=25 and user_marks<50:
#     grade = 'C' 
# else:
#     grade = 'F'
    
''' 
--------------- TYPE 2 if loop homework ----------------

Write a Python program to get the user’s age and print their life stage as shown below:

Age between 0 (included) and 12 → Child
Age between 12 (included) and 19 → Teenager
Age between 19 (included) and 60 → Adult
Age between 60 (included) and 120 → Senior

0------12------19----------------60---------------120
 Child   Teen    Adult              Senior

'''
# user_age = int(input("Please enter your age: "))    

# if user_age>120:
#     print("life_stage = Senior")
# elif user_age<120 and user_age>=60:
#     print("Life stage = Senior")
# elif user_age<60 and user_age>= 19:
#     print("Life stage= Adult")
# elif user_age<19 and user_age>=12:
#     print("Life stage = Teenager")
# else:
#     print("Life stage = Child")
    


'''
Write a program that determines if a student is eligible for a school field trip based on their grade 
and parental consent. 
Use nested if statements with only one inner if loop.

The student must be in Grade 4, 5, or 6 to be eligible.
If the student is not in these grades, they are not eligible for the trip.
Parental Consent:

If the student is in an eligible grade, ask if they have parental consent.
If the answer is "yes", they can join the trip.
Otherwise, they cannot join the trip.
'''
# grade = int(input('Please enter student grade: '))
# consent = input('please enter the parents consent(yes/ no): ')

# if grade == 4 or grade ==5 or grade ==6:
#     print("grade is eligble")
    
#     if consent == "no":
#         print("Student does not have parental consent. You can't join the trip")
#     else:
#         print("Student has parental consent. You can join the trip")
                
# else:
#     print("The student is not from grade 4,5 or 6 and therefore not eligible")
    
'''
 Write a program that determines if a person is eligible for a library membership based on their age and residency status. 
 Use nested if statements and the or keyword.

Rules:
Age Requirements:

The person must be 12 years or older to be eligible.
If the person is younger than 12, they are not eligible for membership.
Residency Requirement:

If the person meets the age requirement, check if they are a resident of the town.
A person is considered a resident if they answer "yes" or "y".
If they are a resident, they are eligible for membership.
Otherwise, they are not eligible.

'''
# age = int(input("Please enter user age: "))
# town = input("Are you a resident of the town (Yes/No)")

# if age>=12:
#     print("You meet the first criteria for a library membership")

#     if town == "no":
#         print("You do not meet the second criteria to get a library membership")
#     else:
#         print("You fulfill both criterias to get a library membership")
# else:
#     print("You do not fulfill the first criteria to get a library membership")
        


'''
A library categorizes books based on their genre and popularity. They use the following classification system:

If a book is of the "Fiction" genre:

If its popularity rating (out of 10) is 7 or above, classify it as "Popular Fiction."
Otherwise, classify it as "Regular Fiction."
If a book is of the "Non-Fiction" genre:

If its popularity rating (out of 10) is 7 or above, classify it as "Popular Non-Fiction."
Otherwise, classify it as "Regular Non-Fiction."

'''
# genre = input("Please enter genre of the book(fiction/non fiction): ")
# popularity = int(input("Please enter popularity of the book(1-10) : "))


# if popularity>=7 and genre == 'fiction':
#     print("This book is popular fiction")
# else:
#     print("This is regular fiction")
#     if popularity>= 7 and genre== "non fiction":
#         print("This book is popular non fiction")
#     else:
#         print("Regular Non-Fiction")

# if genre == "fiction":
#     if popularity>=7:
#         print("This book is popular fiction")
#     else:
#         print("book is regular fiction")
# else:
#     if popularity>=7:
#         print("popular non fiction")
#     else:
#         print("Regular non fiction")


    
print("Thank you for telling me")

