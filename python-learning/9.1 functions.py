def greet_user(name='John',country='Malaysia'):
    print(f"Hi {name} from {country}!")
    
greet_user(country="malaysia",name="aryan")
greet_user(country='Canada')

#variable length arguments
# def add_two_numbers(num1,num2):
#     return num1+num2

# def add_numbers(nums):
#     # return sum(nums)
#     res=0
#     for num in nums:
#         res=res+num
#     return res

# print(add_numbers([23,54,42,75,34,67,88]))

def add_numbers(*nums):
    # res=0
    # for num in nums:
    #     res=res+num
    # return res
    return sum(nums)

add_numbers(2,53,23,12,4,11)

def greet_user_2(**info):
    print(f"Hi {info['name']} from {info['country']}!")
    
    
greet_user_2(name='Nadia',country='UAE')
