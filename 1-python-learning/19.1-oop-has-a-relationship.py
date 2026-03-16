'''
Has-a-relationship

A car has an engine

create a radio class. attach it to the car class. 
the radio should start playing when  the car engine starts
'''

# class Car:
#     def __init__(self,make,model,milage,engine,radio):
#         self.make=make
#         self.model=model
#         self.milage=milage
#         self.engine=engine
#         self.radio=radio
    
#     def drive(self):
#         self.engine.start()
#         print("brmmm brmm")
#         self.radio.playing()
        
        
# class Engine: 
#     def __init__(self,capacity, fuel_type):
#         self.capacity=capacity
#         self.fuel_type=fuel_type
        
#     def start(self):
#         print("engine started")

# class Radio:
#     def __init__(self, station):
#         self.station=station
#     def playing(self):
#         print(f"{self.station} on radio is playing")
    
        
# radio1=Radio("Hitz fm")   
# engine1_5l=Engine(1.5,'petrol')
# camry=Car('Toyota','Camry',100000,engine1_5l,radio1)
# camry.drive() 
        
'''
Hospital Management System

Person
    - name
    - age
    - address
    
Doctor(Person)
    -specialization
    
Patients(Person)
    - registration form object
   
    
Nurses(Person)
    - speciliazation

Disease
    - treatment options
    - tests requird
    
Registration Form
    - ward
    - doctor
    - nurses 
    - diseases
    
--------------------
patients- 
    name
    age
    address
    registration form 
        ward
        doctor
            name
            age
            address
            speciialization
        nurse1
            name
            age
            addresss
            spe
        nurse2
            name
            age
            address
            spe

    
'''

# class Person:
#     def __init__(self,name,address, age):
#         self.name=name
#         self.address=address
#         self.age=age
        
# class Doctor(Person):
#     def __init__(self,name,address,age,specialization):
#         super().__init__(name,address,age)
#         self.specialization=specialization
        
# class Nurse(Person):
#     def __init__(self,name,address,age,specialization):
#         super().__init__(name,address,age)
#         self.specialization=specialization
        
# class Disease:
#     def __init__(self,disease_name,treatment_options,tests_required):
#         self.disease_name=disease_name
#         self.treatment_options=treatment_options
#         self.tests_required=tests_required
        
# class RegistrationForm:
#     def __init__(self,ward,doctor,nurses,diseases):
#         self.ward=ward
#         self.doctor=doctor
#         self.nurses=nurses
#         self.diseases=[diseases]

# class Patient(Person):
#     def __init__(self,name,address,age,registration_form):
#         super().__init__(name,address,age)
#         self.registration_form=registration_form
        
# doctor1=Doctor("Dr. Smith","123 Main St",45,"Cardiology")
# doctor2=Doctor("Dr. Angie","123 Main St",45,"Cardiology")
# nurse1=Nurse("Nurse Joy","456 Elm St",30,"Pediatrics")
# nurse2=Nurse("Nurse John","789 Oak St",28,"General Care")
# disease1=Disease("Flu",["Rest","Hydration"],["Blood Test"])
# disease2=Disease("fever",["Running","Panadol"],["Blood Test"])
# registration_form1=RegistrationForm("Ward A",doctor1,nurse1,disease1)
# registration_form2=RegistrationForm("Ward B",doctor2,nurse2,disease2)
# patient1=Patient("Alice","321 Pine St",25,registration_form1)
# patient2=Patient("Annie","321 Pine St",25,registration_form2)

# print(patient1.registration_form.diseases[0].treatment_options)
# #print the treatment options for the diesease patient1 is having
# print(patient2.registration_form.diseases[0].treatment_options)



'''
REPEAT
Hospital Management System

Person
    - name
    - age
    - address
    
Doctor(Person)
    -specialization
    
Patients(Person)
    - registration form object
   
    
Nurses(Person)
    - speciliazation

Disease
    - treatment options
    - tests requird
    
Registration Form
    - ward
    - doctor
    - nurses 
    - diseases
    
--------------------
patients- 
    name
    age
    address
    registration form 
        ward
        doctor
            name
            age
            address
            speciialization
        nurse1
            name
            age
            addresss
            spe
        nurse2
            name
            age
            address
            spe

    
'''

# class Person:
#     def __init__(self,name,address, age):
#         self.name=name
#         self.address=address
#         self.age=age
        
# class Doctor(Person):
#     def __init__(self,name,address,age,specialization):
#         super().__init__(name,address,age)
#         self.specialization=specialization
        
# class Nurse(Person):
#     def __init__(self,name,address,age,specialization):
#         super().__init__(name,address,age)
#         self.specialization=specialization
        
# class Disease:
#     def __init__(self,disease_name,treatment_options,tests_required):
#         self.disease_name=disease_name
#         self.treatment_options=treatment_options
#         self.tests_required=tests_required
        
# class RegistrationForm:
#     def __init__(self,ward,doctor,nurses,diseases):
#         self.ward=ward
#         self.doctor=doctor
#         self.nurses=nurses
#         self.diseases=diseases

# class Patient(Person):
#     def __init__(self,name,address,age,registration_form):
#         super().__init__(name,address,age)
#         self.registration_form=registration_form
        
# doctor1=Doctor("Dr. Smith","123 Main St",45,"Cardiology")
# nurse1=Nurse("Nurse Joy","456 Elm St",30,"Pediatrics")
# # nurse2=Nurse("Nurse John","789 Oak St",28,"General Care")
# disease1=Disease("Flu","Rest","Blood Test")
# registration_form1=RegistrationForm("Ward A",doctor1,nurse1,disease1)
# patient1=Patient("Alice","321 Pine St",25,registration_form1)

# disease2=Disease("Cold","Medication","Nasal Swab")
# patient2Registration_form1=RegistrationForm("Ward B",doctor1,nurse2,disease1)



# # print(patient1.registration_form.diseases.disease_name)
# # #print the treatment options for the diesease patient1 is having
# # print(patient1.registration_form.diseases.treatment_options)
# # print(patient2.registration_form.diseases.tests_required)

'''what is the age of bobs nurse'''
# # print(patient2.registration_form.nurses.name)
'''where does alice's doctor live'''
# # print(patient1.registration_form.doctor.address)
        
'''
SELF PRACTICE:
University Course Registration System
Person
    - name
    - email

Lecturer (Person)
    - office

Student (Person)
    - student_id
    - enrollment_record

Course
    - course_code
    - title
    - credits

EnrollmentRecord
    - semester
    - lecturer
    - courses
# '''

# # class Person:
# #     def __init__(self,name,email):
# #         self.name=name
# #         self.email=email 

# # class Lecturer(Person):
# #     def __init__(self,name,email,office):
# #         super().__init__(name,email)
# #         self.office=office

# # class Student(Person):
# #     def __init__(self,name,email,student_id,enrollment_record):
# #         super().__init__(name,email)
# #         self.student_id=student_id
# #         self.enrollment_record=enrollment_record 

# # class Course:
# #     def __init__(self,course_code,title,credits):
# #         self.course_code=course_code
# #         self.title=title
# #         self.credits=credits

# # class EnrollmentRecord:
# #     def __init__(self,semester,lecturer,courses):
# #         self.semester=semester
# #         self.lecturer=lecturer
# #         self.courses=courses


# # lecturer1=Lecturer("Olaf","Olafkk@gmail.com","Harvard")
# # courses1=Course("55-3","Biology","10 ECTS")
# # enrollmentrec1=EnrollmentRecord("sem2",lecturer1,courses1)
# # student1=Student("rishka","rr@gmail.com","23RR",enrollmentrec1)


# # print(student1.enrollment_record.lecturer.office)
# # print(student1.name)
# # print(student1.enrollment_record.lecturer.name)

'''
SELF GIVEN
Person
    - name
    - age

Librarian(Person)
    - employee_id

Member(Person)
    - membership_id
    - borrowing_record

Book
    - title
    - author
    - genres (list)

BorrowingRecord
    - section
    - librarian
    - books (list)
3️⃣ Write code to print:
a) The title of the first book the member borrowed
b) The genres of the first book
c) The name of the librarian who handled the borrowing

'''
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# class Librarian(Person):
#     def __init__(self,name,age,employee_id):
#         super().__init__(name,age)
#         self.employee_id=employee_id

# class Member(Person):
#     def __init__(self,name,age,membership_id,borrowingrecord):
#         super().__init__(name,age)
#         self.membership_id=membership_id
#         self.borrowingrecord=borrowingrecord

# class Book:
#     def __init__(self,title,author,genres):
#         self.title=title
#         self.author=author
#         self.genres=genres

# class BorrowingRecord:
#     def __init__(self,section,librarian,books):
#         self.section=section
#         self.librarian=librarian
#         self.books=books
        

# librarian1=Librarian("tom",12,"OD34")
# Book1=Book("Pony","miriam",["romance","comedy"])

# Book2=Book("Harry Potter","Rishka",["Action","Fantasy"])
# borrowingrecord2=BorrowingRecord(3,librarian1,[Book1,Book2])
# member2=Member("rishka",24,"OD33",borrowingrecord2)

"Print the titles of all books the member borrowed."
# for book in member2.borrowingrecord.books:
#     print(book.title) #[books1],[books2] kept in books,r kept in book, one by one

"Print each genre of each book, one line at a time."
# for book in member2.borrowingrecord.books:
#     for genre in book.genres:#genres kept in genre one by one
#         print(genre)

"Print the total number of books borrowed."
# for book in member2.borrowingrecord.books:
#     print(book)

'Print only the books that belong to the genre "Fantasy".'
# for book in member2.borrowingrecord.books:
#     if book.genres=="Fantasy":
#         print(book.title)

'''
"book.genres is a LIST
"Fantasy" is a STRING
Example:
["Action", "Fantasy"] == "Fantasy"   # ❌ False

CORRECT:

for book in member2.borrowingrecord.books:
    if "Fantasy" in book.genres:
        print(book.title)

'''
'Print the first genre of each book'
# for book in member2.borrowingrecord.books:
#     print(book.genres[0])




# print(member2.borrowingrecord.books[0].title)

# for book in member2.borrowingrecord.books:
#     print(book.title)

# for genre in member2.borrowingrecord.books:
#     print(genre.genres)

# for book in member2.borrowingrecord.books:
#     print(book.title,book.genres)

# print(member2.borrowingrecord.librarian.name)


'''
🔹 Problem Statement

A company has different people, tasks, and projects.

Each project:

has one owner

has multiple contributors

has multiple tasks

Each task:

has a difficulty level

behaves differently depending on who completes it

Different types of people handle tasks differently.

🔹 Requirements
1️⃣ Create classes to represent:

people in a company

tasks that need to be completed

projects that group tasks and people

2️⃣ Every person must:

have a name and years of experience

have a method called work_on_task(task)

return different output depending on the person type

(You decide how many person types make sense.)

3️⃣ Every task must:

have a title and difficulty level

be stored inside a project

4️⃣ Every project must:

contain one owner

contain multiple contributors

contain multiple tasks

5️⃣ Write code that:

Creates at least 3 different types of people

Creates multiple tasks

Assigns them to a project

Loops through contributors and calls

work_on_task(task)


for the same task, showing different behavior

'''
class Owner:
    def __init__(self,name):
        self.name=name
class People:
    def __init__(self,name,work_exp):
        self.name=name
        self.work_exp=work_exp 
    
    def work_on_task(self):
        print(f"{self.name} is working on task:")

class Tasks():
    def __init__(self,title,difficulty_level):
        self.title=title
        self.difficulty_level=difficulty_level 
    
    def listing(self):
        print(f"{self.name} is working on title {self.title} which has a difficulty level of {self.difficulty_level}")
    
class Coding(People):
    def __init__(self,name,work_exp):
        super().__init__(name,work_exp)
    
    def work_on_task(self):
        print(f"{self.name} is working on coding:")

class Experiments(People):
    def __init__(self,name,work_exp):
        super().__init__(name,work_exp)
    
    def work_on_task(self):
        print(f"{self.name} is working on experiments:")

class Authors(People):
    def __init__(self,name,work_exp):
        super().__init__(name,work_exp)
    
    def work_on_task(self):
        print(f"{self.name} is working on publishing the data:")

class Contributors():
    def __init__(self,coding,experiments,authors):
        self.coding=coding
        self.experiments=experiments
        self.authors=authors

    def work_all(self):
        self.coding.work_on_task()
        self.experiments.work_on_task()
        self.authors.work_on_task()
    

class Projects():
    def __init__(self,owners,contributors,tasks):
        self.owners=owners
        self.contributors=contributors
        self.tasks=tasks

owner1=Owner("Rishka")
coder1=Coding("Rishka Ann","Professional coder")
experiments1=Experiments("Jeff","PRO")
author1=Authors("Aljitawi","Max pro") 
tasks1=Tasks("projext save earth",100)
contributors1=Contributors(coder1,experiments1,author1)
project1=Projects(owner1,contributors1,tasks1)

contributors1.work_all()

# print(project1.contributors.coding.name)
#i basically want to print all the "names" in contributors. but if i'd do so now i'd need to print it manually...one by one so there is 1 smart option:
#(i) add same method into the contributor class
    # def work_all(self):
    #     self.coding.work_on_task()
    #     self.experiments.work_on_task()
    #     self.authors.work_on_task()



# contributors1=Contributors([coder1,experiments1,author1])
# for name in contributors1.people:
#     print()


# class Contributors:
#     def __init__(self, people):
#         self.people = people

