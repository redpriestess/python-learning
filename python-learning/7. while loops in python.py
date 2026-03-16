'''
1. data types and variables = record data into our program 
2. if conditional - how to make data driven decision 
3. list - record data into our progoram in scale
4. for loops- manipulate data at scale
5. tuples - enforce convention (protected collections) among other thigns
7. while - we can do things until something happens or not happens


don't keep for loop in while loop:"having small bike in car"
'''

#counting from 1 to 10 
# for i in range(1,11):
#     print(i)

# print("-"*10)   
#simulating a for loop using a while loop 
# i=0
# while i<10:
#     i=i+1
#     print(i)

# print("-"*10)  
 
#same task but condition based    
# i=0
# while True:
#    i=i+1
#    print(i)
#    if i>9:
#        break    
   
'''Get the marks from the user. Make sure the marks are between 0 and 100. 
The program should be able to handle wrong inputs and warn the user accordingly. For an instace
The input should not have a space
The input should always be numerical i.e: use answer.isnumeric() to check if the answer only 
has numbers or not 
If the marks are above 50, add them to pass_list. If not add them to fail_list. 
The program should some how get an answer from the user. 
The program should exit when the user enters 'done''''

pass_list = []
failures = []
# marks = int(input("Please enter your marks"))
# if marks>

instructions=""" Welcome to the marks wizard!
Please enter your marks between 0 and 100. 
Marks outside this range will not be accepted
Only numbers will be accepted as marks.
"""

# print(instructions)
# while True:
#     answer=input("Please enter your marks: ")
#     if answer=='done':
#         break
#     if answer.isnumeric():
#         #the answer is numeric
#         answer=int(answer)
#         if answer>0 and answer<100:
#             if answer>50:
#                 pass_list.append(answer)
#             else:
#                 failures.append(answer)
#         else:
#             print("Marks entered shoud be between 0 and 100. Try again..")
#     else:
#         print("Only numerical answers are accepted. Try again..")
# print(f"Good children: {pass_list}")
# print(f"Failures: {failures}")
        
#check if the answer is numerical
#if it is numerical, convert it to an integer and then below
#    - check if the number is between 0 and 100. If not discard
#     -if the range is correct, do the if loop to append to the correct list

'''
# Example: Skip even numbers and print only odd numbers from 1 to 10
number%2 
numbers =list(range(1,21,1))
'''
index = 0
while true:
    if numbers[index]%2==0:
        print(numbers[index])
    else:
        print("only even numbers. try again")
    index=index+1

    if index>len(numbers)
    break


# index=0
# while index<len(numbers):
    
#     number=numbers[index]
#     if number%2==0:
#         continue
    
#     print(number) 
    
#     index=index+1
    



# odd_list=[]
# even_list=[]

# for number in numbers:
#     if number%2 == 0:
#         even_list.append(number)
#     else:
#         odd_list.append(number)
# print(odd_list)
# print(even_list)


