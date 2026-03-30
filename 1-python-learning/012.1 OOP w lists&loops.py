'''1. Library Book Tracker

Create a class Library.

Attribute: books (list of book titles)

Ask the user to enter 5 book titles

Create a method to display all books

Create a method to count how many books have titles longer than 5 characters'''

class library:
    def __init__(self):
        self.books=[]
    def titles(self):
        while True:
            user=input("pls enter 5 book titles")
            if user=="done":
                break
            self.books.append(user)
            if len(self.books)>5:
                print("too many books")
                self.books=[]
                continue
                
        for book in self.books:
            print(book)
    def length(self):
        count=0
        for book in self.books:
            if len(book)>5:
                count+=1
        print(count)

# lib1=library()
# lib1.titles()
# lib1.length() 

'''Create a class StudentGrades.

Attributes:

students = ["Ali", "Ben", "Chloe", "Dan"]

marks = [78, 45, 90, 60]

Create a method to print each student’s name with their mark

Create a method to print only students who scored below 50'''

class grades:
    def __init__(self):
        self.students=["Ali", "Ben", "Chloe", "Dan"]
        self.marks=[78, 45, 90, 60]
    def transcript(self):
        for i in range(len(self.marks)):
            print(f"{self.students[i]} has marks of {self.marks[i]}")
    def fails(self):
        for i in range(len(self.marks)):
            if self.marks[i]<50:
                print(f"{self.students[i]} scored less than 50")

# g1=grades()
# g1.transcript()
# g1.fails()

'''4. Daily Temperature Logger

Create a class Temperature.

Attribute: temps (empty list)

Ask the user to enter temperatures for 7 days

Create a method to calculate the average temperature

Create a method to print temperatures above 30 and which day'''

class temperature:
    def __init__(self):
        self.temps=[]
        self.days=[]
    def temp(self):
        for i in range(7):
            user=int(input("pls enter temperatures"))
            self.temps.append(user) 
        print(self.temps) 
    def averagess(self):
        overall=sum(self.temps)/len(self.temps) 
        print(overall)
    def forecast(self):
        for i in range(7):
            days=input("pls enter which day")
            self.days.append(days)
        for i in range(len(self.temps)):
            print(f"on {self.days[i]},the temperature was {self.temps[i]} ")
    
    
# t1=temperature()
# t1.temp()
# t1.averagess()
# t1.forecast()

'''1. Mismatched Data Detection

Create a class DataCheck.

Attributes:

names = ["Ali", "Ben", "Chloe", "Dan"]

scores = [80, 50, 90]

Create a method to print only valid pairs (matching indexes)

Create a method to detect and print if lengths are mismatched'''

class datacheck:
    def __init__(self):
        self.names=["Ali", "Ben", "Chloe", "Dan"]
        self.scores=[80, 50, 90] 
    
    def match(self):
        if len(self.names)!=len(self.scores):
            print("there's a mismatch")
        
        for i in range(min(len(self.names), len(self.scores))):#min requires 2 values. Need to use min as one list has more values than the other. if don't use min, it'll crash
            print(f"{self.names[i]} has a score of {self.scores[i]}") 


d1=datacheck()
d1.match()
