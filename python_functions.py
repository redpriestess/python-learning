#default parameters in functions
def greet_user(name,country='China'):
    return f'hello {name} from {country}'

print(greet_user('Rishka'))
print(greet_user('Praveen','Sri Lanka'))

#labeled parameters
print(greet_user(country='Malaysia',name='Rishka'))

# #variable length arguments
def add_two_numbers(num1,num2):
    return num1 + num2

def add_numbers(*nums):
    # result=0
    # for num in nums:
    #     result+=num
    # return result

    return sum(nums)
    
print(add_numbers(1,2))
print(add_numbers(1,2,3,4))
print(add_numbers(1,4,240,0,402,503,45,403,304,0))

#keyword arguments
def print_user_info(name,country):
    print(f'Hello {name} from {country}')
    
def print_user_info2(**info):
    print(info)
    
print_user_info2(name='Jonathan Harker',country='England')
print_user_info2(name='Jonathan Harker',occupation='lawyer',spouse='Mina Harker',enemy='Count Dracula')

def print_user_info3(**info):
    print(f'Hello {info.get('name','unknown user')} from {info.get('country','unknown country')}')

print_user_info3(name='Jonathan Harker',country='England')
print_user_info3(name='Jonathan Harker',occupation='lawyer',spouse='Mina Harker',enemy='Count Dracula')
'''
You are building a function that sends notifications for a system.
The function must be scalable, meaning new options can be added later without changing the function signature.

Write a function called send_notification that uses keyword arguments to control its behavior.

 Requirements

1. The function must accept:

   * One required positional argument: message
   * Any number of keyword arguments using kwargs

2. Supported keyword arguments:

   * email (bool): whether to send the message as an email
   * sms (bool): whether to send the message as an SMS
   * push (bool): whether to send the message as a push notification
   * priority (str): "low", "normal", or "high"

3. Use if conditions to decide what actions to perform based on the keyword arguments.

4. Behavior rules:

   * If priority is "high", print "High priority message!" before anything else.
   * If email=True, print Sending email: <message>
   * If sms=True, print Sending SMS: <message>
   * If push=True, print Sending push notification: <message>
   * If no delivery method is provided, print No delivery method selected.

5. The function should not crash if extra keyword arguments are passed.
   Ignore unknown options silently. Real systems do this all the time.
'''
def send_notifications(message,**kwargs):

    delivered= False
    if kwargs.get("priority")=="high":
        print("High priority package")
        delivered= True
    if kwargs.get("email"):
        print(f"sending email message : {message}")
        delivered= True
    if kwargs.get("push"):
        print(f"sending push notification: {message}")
        delivered= True
    if kwargs.get("SMS"):
        print(f"SMS is {message}")
        delivered= True
    if not delivered:
        print("no delivery method selected")


send_notifications("hello",sender="aryan", email=True,SMS=True,push=True,priority="high")

'''
Create a function called process_order that follows these rules:

1️⃣ Function requirements

The function must accept:

One required positional argument: order_id
Any number of keyword arguments using **kwargs

2️⃣ Supported keyword arguments

pickup (bool): whether the order is picked up
delivery (bool): whether the order is delivered
express (bool): whether the order is express
priority (str): "low", "normal", or "high"

3️⃣ Behaviour rules
If priority is "high", print
"High priority order!" before anything else
If pickup=True, print
Order <order_id> is ready for pickup
If delivery=True, print
Order <order_id> will be delivered
If express=True, print
Express processing enabled
If none of pickup, delivery, or express is provided, print
No processing method selected
'''

def process_order(order_id,**kwargs):
    delivered= False
    if kwargs.get("priority")=="high":
        print(f"{order_id} is a high priority order")
        delivered= True
    if kwargs.get("pickup"):
        print(f"{order_id} is ready for pickup")
        delivered= True
    if kwargs.get("delivery"):
        print(f"{order_id} will be delivered")
        delivered= True
    if kwargs.get("express"):
        print(f"{order_id}: express processing enabled")
        delivered= True 
    if not delivered:
        print(f"No processing method selected")

process_order("3334",pickup=True,delivery=False,express=True,priority="high")



'''
Requirements

Write a function called notify_user that accepts:

One required positional argument: text
Any number of keyword arguments using **kwargs

Supported keyword arguments:
in_app (bool): send an in-app notification
email (bool): send an email notification
sms (bool): send an SMS
urgent (bool): whether the message is urgent

Behaviour rules:
If urgent=True, print
"URGENT MESSAGE" before anything else
If in_app=True, print
In-app notification sent: <text>
If email=True, print
Email sent: <text>
If sms=True, print
SMS sent: <text>
If no communication method is chosen, print
No notification method chosen

Ignore any unsupported keyword arguments silently.
'''


def notify_user(text,**kwargs):
    method=False
    if kwargs.get("urgent"):
        print(f"{text} is URGENT MESSAGE")
        method=True
    if kwargs.get("in_app"):
        print(f"{text} in app is sent")
        method=True
    if kwargs.get("email"):
        print(f"{text} in email is sent")
        method=True
    if kwargs.get("sms"):
        print(f"SMS sent")
        method=True
    if not method:
        print("no communication method has been chosen")

notify_user("Hello",urgent=True,in_app=False,email=True,sms=False,hehe="booooooooo")


'''
Q2: Order Notification System

Write a function handle_order that accepts:

Required argument: order_id
Default argument: status="processing"

Keyword arguments:
email (bool)
sms (bool)
urgent (bool)

Rules
If urgent=True, print "URGENT ORDER" first
Print: Order <order_id> is <status>
If email=True, print Email sent for order <order_id>
If sms=True, print SMS sent for order <order_id>
If no delivery method is chosen, print No notification sent
'''

def handle_order(order_id,status="processing",**kwargs):
    delivery=False
    if kwargs.get("urgent"):
        print(f"Email sent for {order_id}")
        delivery=True
    if kwargs.get("sms"):
        print(f"sms sent for {order_id}")
        delivery==True
    if not delivery:
        print("no notification sent")

handle_order(333,status="jju",urgent=True,sms=False)
    
'''
Write a function track_expenses that:

Accepts:
Any number of numbers using *expenses
Keyword arguments using **kwargs
Supported keyword arguments:
category (str)
priority (str): "low" or "high"
Rules
If priority="high", print "High priority expenses!"
Print total expenses
If category exists, print Category: <category>
Must work even if no keyword arguments are given
'''



def track_expenses(*expenses,**kwargs):
    nums=0
    for num in expenses:
        nums+=num
    print(f"the total number of expenses is {nums}")
    if kwargs.get("priority")=="high":
        print("high priority expenses")
    if kwargs.get("category"):
        print(f"the category value is {kwargs.get('category')}")
    
track_expenses(222,222,222,222,222,222,222,priority="high",category="foodie")

'''
Write smart_notify with:

Required: message

Keyword arguments:
email
sms
push

priority
log (bool)

Rules
If priority is "high", print "!!! HIGH PRIORITY !!!"
If more than one delivery method is True, print "Multiple delivery methods selected"
Print each delivery action
If log=True, print "Message logged"
If no delivery method chosen → print "No delivery method"
'''
def smart_notify(message,**kwargs):
    delivery=0
    if kwargs.get("priority")=="high":
        print("HIGH PRIORITY")
        delivery+=1
    if kwargs.get("email"):
        print(f"{message} sent via email")
        delivery+=1
    if kwargs.get("sms"):
        print(f"{message} sent via sms")
        delivery+=1
    if kwargs.get("push"):
        print(f"{message} sent via push")
        delivery+=1
    if delivery>1:
        print("Multiple delivery methods selected")
    if not delivery:
        print("no delivery method chosen")

smart_notify("it's okay girlie",priority="high", email=True, sms=True,push=True )

    
'''
Q1: Travel Profile Generator

Write a function create_profile(name, country="Unknown", **kwargs).

Supported keyword arguments:

age (int)
passport (bool)
vaccinated (bool)

Rules:
Always print: Profile for <name> from <country>
If passport=True, print "Passport verified"
If vaccinated=True, print "Vaccination cleared"
If neither passport nor vaccinated is provided, print "Incomplete travel documents"
Ignore extra keyword arguments
'''

def create_profile(name,country="Unknown",**kwargs):
    print(f"profile for {name} from country {country}")
    Passport=kwargs.get("Passport")
    if Passport:
        print(f"{name}'s Passport from {country} is verified")
    Vaccination=kwargs.get("Vaccination")
    if Vaccination:
        print(f"{name} from {country} is vaccinated")
    if not Passport and not Vaccination:
        print("Incomplete travel documents") 

# create_profile("rishka","malaysia",Passport=True,Vaccination=False)
# python .\python_functions.py  

'''
Question 1: Attendance Logic

Create a function that:
Can accept any number of student names
Has an optional setting that controls the minimum number of students required (default is 1)
Rules:
Print how many students attended
If attendance is below the minimum, print "Class cancelled"
Otherwise print "Class proceeding"
'''
def attendance(*student_names,min_num=1):
    nums=0
    for num in student_names:
        nums+=1
    print(nums)
    if nums<2:
        print("class cancelled")
    else:
        print("class onz")

# attendance("kayla","rishka","maya","anna","aryan")

'''
Question 2: Application Feature Configuration

Create a function that:

Takes the name of an application
Accepts an open-ended set of feature flags (on/off)
Possible features include:
chat
payments
analytics
ads
Rules:
Print "Configuring <app name>"
Print each feature that is enabled
If no features are enabled, print "No features enabled"
If more than two features are enabled, print "Advanced configuration active"

'''

def app(name,**kwargs):
    print(f"name of application is {name}")
    feature=0
    chat=kwargs.get("chat")
    if chat:
        feature+=1
        print("this feature chat is enabled")
    payments=kwargs.get("payments")
    if payments:
        feature+=1
        print("this feature payments is enabled")
    analytics=kwargs.get("analytics")
    if analytics:
        feature+=1
        print("this feature analytics is enabled")
    ads=kwargs.get("ads")
    if ads:
        feature+=1
        print("this feature ads is enabled")
    if feature==0:
        print("no features are enabled")
    if feature>2:
        print("advanced configuration active")

    
# app("rari",chat=False,payments=False,analytics=False,ads=False)

'''
Question 3: Bill Processing

Create a function that:
Can accept any number of numeric bill values
Can optionally receive settings that affect how totals are calculated

Rules:
Calculate and print the total bill amount
If tax is enabled, add 5% tax
Print the currency (default should be USD)
If no bills were provided, print "No bills to process"
'''

def function(*args,**kwargs):
    nums=0
    for num in args:
        nums+=num
    print(f"the total bill is {nums}")
    if kwargs.get("taxes"):
        new=(0.05*nums)+nums
    print(f"the total bill with tax is ${new}")
    if nums==0:
        print("no bills were provided")

# function(4,5,6,taxes=True)

'''
Question 4: Secure Access Check

Create a function that:
Takes a person’s name
Accepts multiple authentication methods as optional inputs
Possible methods:
badge
biometric
manager override
Rules:
Access is granted only if at least two methods are True
Print "Access granted" or "Access denied"
Print which authentication methods were used
Ignore any unknown inputs
'''
def func(name,**kwargs):
    print(f"person's name is {name}")
    authentication=0
    authentication_methods=["badge","biometric","manager_override"]
    keys=[]

    for key,value in kwargs.items():
        if key in authentication_methods and value:
            authentication+=1
            keys.append(key)
    if authentication>=2:
        print(f"access granted with these factors:{keys}")
    else:
        print("Access denied")

# func("rishka",manager_override=True,password=True)

'''
Question 5: Music Playlist Logic

Create a function that:
Can accept any number of song titles
Can accept optional playback settings

Possible settings:
shuffle
repeat

Rules:
Print how many songs were added
Print each song title
If both shuffle and repeat are enabled, print "Party mode enabled"
If no songs were provided, print "Playlist empty"
'''

def music(*args,**kwargs):
    songs=0
    for song in args:
        songs+=1
    print(f"total number of songs is {songs} and their titles are {args}")

    if kwargs.get("shuffle") and kwargs.get("repeat"):
        print("party mode enabled")
    
    if songs==0:
        print("playlist empty")

# music("cance queen","slaytastic",shuffle=True,repeat=True)

'''
Question 6: Message Styling

Create a function that:
Takes a message text
Accepts optional formatting instructions

Possible instructions:
convert text to uppercase
add a prefix
add a suffix

Rules:
Prefix is applied first (if present)
Uppercase is applied next (if enabled)
Suffix is applied last (if present)
Print the final formatted message
'''

def punct(message,**kwargs):
    prefix=kwargs.get("prefix")
    if prefix:
        message=prefix + message
    uppercase=kwargs.get("uppercase")
    if uppercase:
        message=message.upper()
    suffix=kwargs.get("suffix")
    if suffix:
        message=message+ suffix
    print(f"final message is {message}")


# punct("happy",prefix="Un",uppercase=True,suffix=False)

'''
Question 7: Order Data Builder

Create a function that:
Takes an order identifier
Accepts any number of item names
Accepts optional metadata about the order

Possible metadata:
priority (default: "normal")
delivery method (default: "standard")

Rules:
Return a dictionary containing:
order identifier
list of items
number of items
priority
delivery method
'''

def nums(identifier,*items,**metadata):
    dictionary={
        "order id": identifier,
        "items": list(items),
        "length_items":len(items),
        "metadata":metadata.get("priority","normal"),
        "delivery":metadata.get("delivery","standard")
        }
    print(dictionary)

nums(4444,"kuku","lulu","momo","rrr","rrrrrr",priority="High")





