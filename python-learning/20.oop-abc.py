'''

ABC- Abstract Base Class
-------------------------
Engineers, Draftmen, Technicians, Laborours, HR Staff

HR department
Design design departmnet
labour department

classes, objects, methods and attributes
inheritance
polymorphism
Encapsulation
abstraction 
has a relationship

System features: 

Keep track of employee details: 
    - salary 
    - OT
    - Benefits
    - Attendance
    - Professional conduct
    - Promotions (pending)
    
names
salary
employee id
reporting officer


employee
    - HR
        - HR staff
            salary_calculation
    - Labour
        - Labourer
    - Design
        - Draftsman
        - Engineer
HR

Has a relationship 
Hr department object HAS all hr employees
    -
'''
from abc  import ABC, abstractmethod
#Abstract Base Class
#OOP

class Employee(ABC):
    def __init__(self,name,employee_id,salary,reporting_officer):
        self.name=name
        self.employee_id=employee_id
        self.salary=salary
        self.reporting_officer=reporting_officer
    
    @abstractmethod
    def overtime_calculation(self):
        return 0
    
class Engineer(Employee):
    def __init__(self,name,employee_id,salary,reporting_officer,engineering_certification):
        super().__init__(name,employee_id,salary,reporting_officer)
        self.engineering_certification=engineering_certification
        
    def overtime_calculation(self):
        return 50000
    
        
class HR(Employee):
    def __init__(self,name,employee_id,salary,reporting_officer,hr_certification):
        super().__init__(name,employee_id,salary,reporting_officer)
        self.hr_certification=hr_certification
    
    def calculate_overtime(self):
        return 30000

managing_director=HR("Mrs. Pauline",323,120000,None,'iso4030')
engineer1=Engineer('John Doe',123,50000,managing_director,'iso9001')
draftsman1=HR('John Johnes',342,11000,managing_director,'iso4030')
hr_clerk1=HR("Calvers",323,23000,managing_director,'iso4030')

emps = [managing_director,draftsman1,hr_clerk1,engineer1]

for emp in emps:
    print(emp.overtime_calculation())
    





