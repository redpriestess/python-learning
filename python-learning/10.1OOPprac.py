'''
Stage 1 — Pure Class Foundations

Goal: become very comfortable with class + self + methods

Exercise 1

Create a Book class.

Attributes

title

author

pages

Method

describe() → prints book details.

Create 3 book objects and call describe().

'''

# class Book:
#     def __init__(self,title,author,pages):
#         self.title=title
#         self.author=author
#         self.pages=pages 
    
#     def describe(self):
#         print(f"{title}:{author}:{pages}")


# book1=Book("harry potter","jk rowling","23")
# book1.describe()
# book2=Book("harry pp","jk rowling","23")
# book2.describe()

'''
Exercise 3

Create a Student class.

Attributes

name

student_id

gpa

Method

describe()

Store 5 students in a list and print them using a loop.
'''

# # class student:
# #     def __init__(self,name,student_id,gpa):
# #         self.name=name
# #         self.student_id=student_id
# #         self.gpa=gpa
    
# #     def printing(self):
# #         print(f"{self.name}, {self.student_id},{self.gpa}")
        

# # student1=student("Rishka",444,1)
# # student2=student("Risha",477,2)
# # student3=student("Rihka",986,3)

# # students=[student1,student2,student3]
# # for student in students:
# #     student.printing()


'''
Exercise 4

Create a Movie class.

Attributes

title

rating

Store movies in a list.

Loop through the list and print only movies with rating > 8.
'''

# class Movie:
#     def __init__(self,title,rating):
#         self.title=title
#         self.rating=rating 
    
#     def printing(self):
#         if self.rating>8:
#             print(f"{self.title} has rating of {self.rating} ")

# movie1=Movie("kukulala",2)
# movie2=Movie("Princess",39) 
# movies=[movie1,movie2]

# for movie in movies:
#     movie.printing()



# class student:
#     def __init__(self,name,id,gpa):
#         self.name=name
#         self.id=id
#         self.gpa=gpa
    
#     def describe(self):
#         print(f"name:{self.name},gpa:{self.gpa}")
    

# student1=student("Rishka",444,1)
# student2=student("pops",333,8) 

# students={}
# students[student1.id]=student1
# students[student2.id]=student2

# for student in students.values():
#     student.describe()
#     if student.gpa>3.5:
#         print(student.name)


# for ID,person in students.items():
#     print(f"student ID:{person.id}, name:{person.name}") 

'''
Create a base class Animal.

Attributes

name

age

Method

describe()

Create child classes:

Dog
Cat

Add method:

make_sound()

Dog → bark
Cat → meow
'''

class animal:
    def __init__(self,name,age):
        self.name=name 
        self.age=age 

    def describe(self):
        print(f"{self.name} is {self.age} years old")

class dog(animal):
    def noise(self):
        print("woof")

class cat(animal):
    def noise(self):
        print("meow") 

animal1=dog("joku",23)
animal1.noise()
animal2=cat("puuss",12)
animal2.noise()



    


