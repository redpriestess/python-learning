# root = tk.Tk()

# root.title("Rishka's First GUI")

# root.geometry("400x300")

# root.mainloop()

# import tkinter as tk


# root=tk.Tk()

# root.title("rishka's GUI")

# root.geometry("400x600")


# label=tk.Label(root,text="Hobbies")
# label.pack()

# root.mainloop()





# self learnnnnnnn
# import tkinter as tk

# root=tk.Tk()
# root.title("Rishka HMS")
# root.geometry("600x1000")

# def add_patient_record():
#     name=patient_name_entry.get()
#     age=age_entry.get()
#     address=address_entry.get()
    
#     print(f"Patient name: {name}\nPatient age: {age}\nPatient address: {address}")

# form_title=tk.Label(root,text="Patient Registration Form",font=("Arial",24))
# form_title.pack()

# patient_name_label=tk.Label(root,text="Full name of the patient",font=("Arial",12))
# patient_name_label.pack(anchor="w",padx=15,pady=5)

# patient_name_entry=tk.Entry(root,text='')
# patient_name_entry.pack(padx=15,pady=5,fill='x')

# age_label=tk.Label(root,text="Age",font=("Arial",12))
# age_label.pack(anchor="w",padx=15,pady=5)

# age_entry=tk.Entry(root,text='',font=("Arial",12))
# age_entry.pack(anchor='w',padx=15,pady=5,fill='x')

# address_label=tk.Label(root,text="Address",font=("Arial",12))
# address_label.pack(anchor="w",padx=15,pady=5)

# address_entry=tk.Entry(root,text='',font=("Arial",12))
# address_entry.pack(anchor='w',padx=15,pady=5,fill='x')

# add_data_button = tk.Button(root,text='Add record',command=add_patient_record)
# add_data_button.pack()





# data=tk.Label(root,text="\n•hospitalname\n•department\n•trial description\n•doctorname\n•contact",
#               font=("Arial",12),
#               justify="left")


# data.pack()
# root.mainloop()

# -------------------------------------------------------------------------------------------------
# import tkinter as tk

# window=tk.Tk()
# window.title("Rishka's Hospital")
# window.geometry("600x1000")

# def buttonsz():
#     name=patient_name_entry.get()
#     age=patient_age_entry.get()
#     address=patient_address_entry.get()

#     # print(f"patient {name} is {age} years old and lives at {address}")
#     result_text=(f"patient {name} is {age} years old and lives in {address}")
#     patient_result.config(text=result_text)


# patient_registration_form=tk.Label(window,text="Patient registration form",font=("Aptos",20))
# patient_registration_form.pack()

# patient_name_label=tk.Label(window,text="Patient name",font=("Aptos",15))
# patient_name_label.pack(anchor="w",padx=5,pady=5)

# patient_name_entry=tk.Entry(window,text='',font=("Aptos",10))
# patient_name_entry.pack(anchor="w",padx=5,pady=5,fill='x')

# patient_age_label=tk.Label(window,text="Patient's age",font=("Aptos",15))
# patient_age_label.pack(anchor="w",padx="5",pady="5")

# patient_age_entry=tk.Entry(window,text='',font=("Aptos",10))
# patient_age_entry.pack(anchor="w",padx=5,pady=5,fill="x")

# patient_address_label=tk.Label(window,text="Patient's address",font=("Aptos",15))
# patient_address_label.pack(anchor="w",padx="5",pady="5")

# patient_address_entry=tk.Entry(window,text='',font=("Aptos",10))
# patient_address_entry.pack(anchor="w",padx=5,pady=5,fill="x")

# addbutton= tk.Button(window,text="Done",font=("Aptos",10),command=buttonsz)
# addbutton.pack()

# patient_result=tk.Label(window,text="Patient's result:",font=("Aptos",15))
# patient_result.pack(pady=20)

# patient_result=tk.Label(window,text=print(buttonsz),font=("Aptos",15))
# patient_result.pack(pady=5)


# window.mainloop()

# -------------------------------------------------------------------------------------------------

'''
Python Tkinter Programming Problem

Create a Simple Electricity Bill Estimator application using Tkinter.

You must build a graphical user interface with the following requirements:

1. The window should have a suitable title.

2. Add a Label that says:
   "Enter customer name"

3. Add an Entry box below it for the user to type the customer name.

4. Add another Label that says:
   "Enter units consumed (kWh)"

5. Add an Entry box below it for the user to type the number of electricity units consumed.

6. Add a Button labeled:
   "Calculate Bill"

7. When the button is clicked:

   * Retrieve the name and units entered.
   * Convert the units to a number.
   * Use if conditions to calculate the bill using the following rules:
     If units are less than or equal to 100, rate is 0.50 per unit.
     If units are between 101 and 300, rate is 0.75 per unit.
     If units are above 300, rate is 1.00 per unit.
   * Calculate the total bill amount.
   * Display the result in a new Label below the button in the format:
     Customer <name> must pay <amount>

8. Use the pack layout manager for all widgets.

Your solution must use:

* Tkinter window
* Labels
* Entry widgets
* Button
* pack layout manager
* if conditions inside the button command function
'''


# import tkinter as tk
# window=tk.Tk() 
# window.title("Electricity Bill Estimator")
# window.geometry("600x1000")

# def calculate():
#     name=customer_name_entry.get()
#     units_consumed=units_consumed_entry.get()
#     if units_consumed.isnumeric():
#         units_consumed=int(units_consumed)
#         if units_consumed<=100:
#             total_consumed=100*0.50
#         elif units_consumed>=101 and units_consumed<300: 
#             total_consumed=units_consumed*0.75
#     result_text= (f"{name} is required to pay {total_consumed}")
#     print(result_text)
#     calculator.config(text=result_text)


# form_label=tk.Label(window,text="Electricity Bill Estimator",font=("Aptos",20))
# form_label.pack()

# customer_name_label=tk.Label(window,text="Customer name",font=("Aptos",15))
# customer_name_label.pack(anchor="w",padx=5,pady=10)

# customer_name_entry=tk.Entry(window,text='',font=("Aptos",10))
# customer_name_entry.pack(fill='x',padx=5,pady=5)

# units_consumed_label=tk.Label(window,text="Units consumed(Kwh)",font=("Aptos",15))
# units_consumed_label.pack(anchor="w",padx=5,pady=10)

# units_consumed_entry=tk.Entry(window,text='',font=("Aptos",10))
# units_consumed_entry.pack(fill='x',padx=5,pady=5)

# calculate_bill= tk.Button(window,text="Calculate bill",font=("Aptos",12),command=calculate)
# calculate_bill.pack()

# calculator=tk.Label(window,text="",font=("Aptos",10))
# calculator.pack()

# window.mainloop()

'''
Create a Student Course Registration and Grade Calculator application using Tkinter and Object Oriented Programming.

You must design a GUI application with the following requirements.

1. Create a class called Student.

The class must have:

* name
* student_id
* course_name
* assignment_mark
* exam_mark

Add the following methods:

* calculate_total() which returns assignment_mark + exam_mark
* calculate_grade() which returns:
  A if total is 75 or above
  B if total is 60 to 74
  C if total is 50 to 59
  F if total is below 50

2. Create another class called StudentApp.

Inside this class:

* Create the Tkinter window.

* Use the pack layout manager for all widgets.

* Add Labels and Entry widgets for:
  Student Name
  Student ID
  Course Name
  Assignment Mark
  Exam Mark

* Add a Button labeled:
  "Generate Result"

3. When the button is clicked:

* Retrieve all values from the Entry boxes.
* Convert marks to integers.
* Create a Student object using the entered data.
* Call the calculate_total() method.
* Call the calculate_grade() method.
* Display the following results using Labels:
  Student Name
  Course Name
  Total Marks
  Grade

4. Add another Button labeled:
   "Clear"

When clicked:

* Clear all Entry boxes.
* Clear all result Labels.

5. The application must:

* Use at least two classes.
* Use object creation.
* Use methods inside classes.
* Use if conditions inside the grade calculation.
* Use labels, entry boxes, and buttons.
* Use the pack layout manager for placing widgets.

Create a Student Course Registration and Grade Calculator application using Tkinter and Object Oriented Programming.

You must design a GUI application with the following requirements.

'''

# class Student:
#   def __init__(self,name,student_id,course_name,assignment_mark,exam_mark):
#     self.name=name
#     self.student_id=student_id
#     self.course_name=course_name
#     self.assignment_mark=assignment_mark
#     self.exam_mark=exam_mark

#   def calculate_total(self):
#     if not self.exam_mark.isnumeric() or not self.assignment_mark.isnumeric():
#       return None 
#     exammark = int(self.exam_mark)
#     assignmentmark = int(self.assignment_mark)
#     total = exammark + assignmentmark
#     return total

#   def calculate_grade(self):
#     total = self.calculate_total()
#     if total>=75:
#       return "A"
#     elif total>=60 and total<=74:
#       return "B"
#     elif total>=50 and total<=59:
#       return "C"
#     elif total<=50:
#       return "F"
      

# import tkinter as tk

# class StudentApp:
#   def __init__(self):
  
#     self.mygrades=tk.Tk() 
#     self.mygrades.title("my grades")
#     self.mygrades.geometry("800x2000")
#     self.create_form()
#     self.mygrades.mainloop()
  
#   def create_form(self):
#     label=tk.Label(self.mygrades,text="Student Course Registration & Grade Calculator", font=("Aptos",20))
#     label.pack() 

#     label_name=tk.Label(self.mygrades,text="Student name ", font=("Aptos",15))
#     label_name.pack(anchor="w",padx=5,pady=5) 

#     self.entry_name=tk.Entry(self.mygrades,text="", font=("Aptos",10))
#     self.entry_name.pack(anchor="w",fill="x",padx=5,pady=5) 

#     label_student_id=tk.Label(self.mygrades,text="Student_ID", font=("Aptos",15))
#     label_student_id.pack(anchor="w",padx=5,pady=5) 

#     self.entry_student_id=tk.Entry(self.mygrades,text="", font=("Aptos",10))
#     self.entry_student_id.pack(anchor="w",fill="x",padx=5,pady=5) 

#     label_course_name=tk.Label(self.mygrades,text="Course name", font=("Aptos",15))
#     label_course_name.pack(anchor="w",padx=5,pady=5) 

#     self.entry_course_name=tk.Entry(self.mygrades,text="", font=("Aptos",10))
#     self.entry_course_name.pack(anchor="w",fill="x",padx=5,pady=5)

#     label_assignment_mark=tk.Label(self.mygrades,text="Assignment mark", font=("Aptos",15))
#     label_assignment_mark.pack(anchor="w",padx=5,pady=5) 

#     self.entry_assignment_mark=tk.Entry(self.mygrades,text="", font=("Aptos",10))
#     self.entry_assignment_mark.pack(anchor="w",fill="x",padx=5,pady=5) 

#     label_exam_mark=tk.Label(self.mygrades,text="Exam mark", font=("Aptos",15))
#     label_exam_mark.pack(anchor="w",padx=5,pady=5) 

#     self.entry_exam_mark=tk.Entry(self.mygrades,text="", font=("Aptos",10))
#     self.entry_exam_mark.pack(anchor="w",fill="x",padx=5,pady=5) 

#     label_button=tk.Button(self.mygrades,text="Generate result",font=("Aptos",15),command=self.generate_results)
#     label_button.pack()

#     label_student_name_result=tk.Label(self.mygrades,text="Student name",font=("Aptos",15))
#     label_student_name_result.pack()

#     self.label_student_name_result_entry=tk.Label(self.mygrades,text="",font=("Aptos",10))
#     self.label_student_name_result_entry.pack()

#     label_course_name_result=tk.Label(self.mygrades,text="Course name",font=("Aptos",15))
#     label_course_name_result.pack()
    
#     self.label_course_name_result_entry=tk.Label(self.mygrades,text="",font=("Aptos",10))
#     self.label_course_name_result_entry.pack()

#     label_total_marks=tk.Label(self.mygrades,text="Total marks",font=("Aptos",15))
#     label_total_marks.pack()
    
#     self.label_total_marks_entry=tk.Label(self.mygrades,text="",font=("Aptos",10))
#     self.label_total_marks_entry.pack()

#     grade_label=tk.Label(self.mygrades,text="Grade",font=("Aptos",15))
#     grade_label.pack()

#     self.grade_label_entry=tk.Label(self.mygrades,text="",font=("Aptos",10))
#     self.grade_label_entry.pack()

#     clear_button=tk.Button(self.mygrades,text="Clear",font=("Aptos",15),command=self.clear_fields)
#     clear_button.pack()

#   def clear_fields(self):
#     self.entry_name.delete(0,tk.END)
#     self.entry_student_id.delete(0,tk.END)
#     self.entry_course_name.delete(0,tk.END)
#     self.entry_assignment_mark.delete(0,tk.END)
#     self.entry_exam_mark.delete(0,tk.END)

#     self.label_student_name_result_entry.config(text="")
#     self.label_course_name_result_entry.config(text="")
#     self.label_total_marks_entry.config(text="")
#     self.grade_label_entry.config(text="")


#   def generate_results(self):
#     name=self.entry_name.get()
#     student_id=self.entry_student_id.get()
#     course = self.entry_course_name.get()
#     assignment_mark=self.entry_assignment_mark.get()
#     exam_mark=self.entry_exam_mark.get()

#     student=Student(name,student_id,course,assignment_mark,exam_mark)

#     total=student.calculate_total()
#     grade=student.calculate_grade()
    
#     self.label_student_name_result_entry.config(text=f"{name}")
#     self.label_course_name_result_entry.config(text=f"{course}")
#     self.label_total_marks_entry.config(text=f"{total}")
#     self.grade_label_entry.config(text=f"{grade}")


# app = StudentApp()

'''
Python Tkinter Programming Problem(self practise)

Create a Simple Electricity Bill Estimator application using Tkinter.

You must build a graphical user interface with the following requirements:

1. The window should have a suitable title.

2. Add a Label that says:
   "Enter customer name"

3. Add an Entry box below it for the user to type the customer name.

4. Add another Label that says:
   "Enter units consumed (kWh)"

5. Add an Entry box below it for the user to type the number of electricity units consumed.

6. Add a Button labeled:
   "Calculate Bill"

7. When the button is clicked:

   * Retrieve the name and units entered.
   * Convert the units to a number.
   * Use if conditions to calculate the bill using the following rules:
     If units are less than or equal to 100, rate is 0.50 per unit.
     If units are between 101 and 300, rate is 0.75 per unit.
     If units are above 300, rate is 1.00 per unit.
   * Calculate the total bill amount.
   * Display the result in a new Label below the button in the format:
     Customer <name> must pay <amount>

8. Use the pack layout manager for all widgets.

Your solution must use:

* Tkinter window
* Labels
* Entry widgets
* Button
* pack layout manager
* if conditions inside the button command function
'''

# class methods:
#   def __init__(self,name,units):
#     self.name=name
#     self.units=units 

#   def getting(self):
#     if not self.units.isnumeric():
#       return None 
#     else:
#       number=int(self.units)
#       if number<=100:
#         self.rate=0.50*number
#       elif number>=101 and number<=300:
#         self.rate=0.75*number
#       elif number>300:
#         self.rate=1*number 

#   def calculate(self):
#     rate=self.getting()
#     return rate 

# import tkinter as tk

# class GUI:
#   def __init__(self):
#     self.app=tk.Tk()
#     self.app.title("Electricity bill estimator") 
#     self.app.geometry("600x1000")
#     self.layout()
#     self.app.mainloop()

#   def layout(self):
#     title_label=tk.Label(self.app,text="Electricity bill estimator",font=("Aptos",20))
#     title_label.pack()
#     label_customername=tk.Label(self.app,text="Customer name",font=("Aptos",20))
#     label_customername.pack(anchor="w",padx=5,pady=5)
#     self.entry_customername=tk.Entry(self.app,text="",font=("Aptos",10))
#     self.entry_customername.pack(anchor="w",padx=5,pady=5,fill="x")

#     label_unitsconsumed=tk.Label(self.app,text="units consumed",font=("Aptos",20))
#     label_unitsconsumed.pack(anchor="w",padx=5,pady=5)
#     self.entry_unitsconsumed=tk.Entry(self.app,text="",font=("Aptos",10))
#     self.entry_unitsconsumed.pack(anchor="w",padx=5,pady=5,fill="x")

#     button=tk.Button(text="calculate bill",font=("Aptos",20),command=self.converting)
#     button.pack()

#     label_totalbill=tk.Label(self.app,text="total bill",font=("Aptos",20))
#     label_totalbill.pack()
#     self.result_totalbill=tk.Label(self.app,text="",font=("Aptos",20))
#     self.result_totalbill.pack()
  
#   def converting(self):
#     name=self.entry_customername.get()
#     units_consumed=self.entry_unitsconsumed.get() 
#     methods1=methods(name,units_consumed)
#     methods1.getting()
#     rate=methods1.calculate()
#     self.result_totalbill.configure(text=f"{name}'s total bill is {rate}")

# gui1=GUI()
# gui2=GUI()



'''
self given
🏥 Patient Health Record & BMI Processing System

Design a GUI-based application using Tkinter and Object-Oriented Programming.
The program should allow a user to enter information about a patient and compute their health classification.

Functional Requirements

The application must allow the user to:
Enter personal details of a patient.
Enter physical measurements required for health assessment.
Generate a health result based on those measurements.
View a final health classification for the patient.
Clear all input and output fields.

Behaviour Requirements

When the user clicks a button to calculate results:
The program should retrieve all entered data.
The program should perform necessary numeric processing.
The program should compute a health metric using the provided measurements.
The program should determine a classification based on defined health ranges.
The program should display the relevant information back to the user.

The classification rules are:

BMI below 18.5 → Underweight
BMI 18.5 to 24.9 → Normal
BMI 25 to 29.9 → Overweight
BMI 30 or above → Obese

When the user clicks the Clear button:
All inputs must reset.
All displayed results must disappear.
'''
# class Patient:
#   def __init__(self,name,BMI):
#     self.name=name
#     self.BMI=BMI
#     self.convert_BMI()
#     self.calculate_BMI()
  
#   def convert_BMI(self):
#     if not self.BMI.isnumeric():
#       return None
#     else:
#       bmi=int(self.BMI) #if separate n user types in alphabet will it still show error
#       return bmi

#   def calculate_BMI(self):
#     bmi=self.convert_BMI() 
#     if bmi<18.5:
#       return " underweight"
#     if bmi>=18.5 and bmi<=24.9:
#       return "normal "
#     if bmi>=25 and bmi<=29:
#       return "overweight"
#     if bmi>=30:
#       return " obese"

# import tkinter as tk
# class Application:
#   def __init__(self):
#     self.app=tk.Tk() 
#     self.app.title("BMI Calculation")
#     self.app.geometry("600x1000")
#     self.design()
#     self.app.mainloop()
  
#   def design(self):
#     label1=tk.Label(self.app,text="Patient Health Record & BMI Processing System", font=("Aptos,20"))
#     label1.pack() 

#     label2=tk.Label(self.app,text="Patient name", font=("Aptos,20"))
#     label2.pack(anchor="w",padx=5,pady=5) 
#     self.Entry1=tk.Entry(self.app,text="", font=("Aptos,15"))
#     self.Entry1.pack(fill="x",padx=5)

#     label2=tk.Label(self.app,text="Patient BMI", font=("Aptos,20"))
#     label2.pack(anchor="w",padx=5,pady=5) 
#     self.Entry2=tk.Entry(self.app,text="", font=("Aptos,15"))
#     self.Entry2.pack(fill="x",padx=5)

#     button1=tk.Button(self.app,text="Generate health result",font=("Aptos",20),command=self.action)
#     button1.pack()

#     label3=tk.Label(self.app,text="Health result", font=("Aptos,20"))
#     label3.pack()

#     self.label4=tk.Label(self.app,text="", font=("Aptos,15"))
#     self.label4.pack()

#     button2=tk.Button(self.app,text="Clear",font=("Aptos",20),command=self.delete)
#     button2.pack()
  
#   def action(self):
#     name=self.Entry1.get()
#     BMI=self.Entry2.get()
#     patient1=Patient(name,BMI)
#     bmigiven=patient1.calculate_BMI()
#     self.label4.configure(text=f"patient{name} has BMI that is in category {bmigiven}")
  
#   def delete(self):
#     self.Entry1.delete(0,tk.END)
#     self.Entry2.delete(0,tk.END) 

#     self.label4.configure(text="")


# app1=Application()






