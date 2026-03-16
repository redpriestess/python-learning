

'''
1. data types and variables = record data into our program 
2. if conditional - how to make data driven decision 
3. list - record data into our progoram in scale
4. for loops- manipulate data at scale
5. tuples - enforce convention (protected collections) among other thigns
'''

#TUPLES ARE JUST LIKE LISTS(FOR THE MOST PART)
names = ['Varyion', 'Octobar','Loraline']
names[0]='Milly'
print(names)
#--------------------

#TUPLES ARE IMMUTABLE (THEY CANNOT BE CHANGED AFTER CREATION)
names2 = ('Varyion', 'Octobar','Loraline')
# names2[0]='Milly'
#print(names)

#ILLEGALLY MODIFY A TUPLE
names2=list(names2)
names2=list(names2) > #converts the tuple into a list
names2[0]='Milly'#modify the list
names2=tuple(names2)#change it back to tuple
print('-'*50)#for space
print(names2)

#NESTED TUPLES
nested = ( (1,2), (3,4) )

#CREATING A SINGLE ELEMENT TUPLE- TUPLE HINTING(lists vs tuple)
little_name_list = ['Nuada']
print(type(little_name_list))

little_name_tuple = ('Nuada',) # only if add coma, knows it is tuple or if more than 2>knows tuple.no coma+ one word= string
print(type(little_name_tuple)) #"," is TYPE HINTING> to hint it is a tuple

#WHY BRACKETS ARE IGNORED
a=1*3
print(a)  #in the above, w no coma, it'll be a str, as python thinks its math eq so ignores the bracket as seen here
b =(1*3)+2
print(b)

#PACKING
name='Jonathan'
name,age='Jonathan',45
print(name,age)

information='Jonathan',45,'Denmark'
print(type(information)) 

#UNPACKING
person_name,person_age,person_country=information
print(information) #prints it as tuple ('Jonathan', 45, 'Denmark')
print(person_name,person_age,person_country) #prints as normal> Jonathan 45 Denmark

#CAN'T PACK THINGS INTO ANYTHING OTHER THAN A TUPLE. IT WILL GET CONVERTED INTO A TUPLE!!
#BECAUSE OF THIS, PARENTHESIS is OPTIONAL WHEN PACKING

information2 = 'Jonathan', 'Kelsington',56,True
#ABOVE LINE IS EQUAL TO ...
information2 = ('Jonathan', 'Kelsington',56,True)
print(information2)

#TUPLE CONCATENATION> joins t1 and t2 together
t1 = (1,2)
t2 = (3,4)
t3 = t1 + t2  > (1, 2, 3, 4)

#TUPLE SLICING
'''
LIST SLICING SYNTAX
list_name[start:end+1:step size]
'''
nums = [10, 20, 30, 40, 50]
print(nums[1:3:1])
print(nums[1:4:2])

nums = (10, 20, 30, 40, 50)
print(nums[1:3:1])
print(nums[1:4:2])

#MEMBERSHIP TESTING
if 10 in nums: 
    print("10 is in there")
    
#TUPLE REPETION
first_names=('yo',) 
print(first_names)
print(first_names*10)

#GENERIC FUNCTIONS
print(len(nums))
print(min(nums))
print(max(nums))
print(sum(nums))

new_nums = (1,2,2,3)
new_nums.count(2)   #shows how many times 2 has appeared in the tuple
new_nums.index(3)   #index of the first occurence of 3 and only for that 3, if got another one dont show

'''
Write a program that filters a list of student score tuples into pass and fail lists 
based on a user-defined passing score, then demonstrates list slicing and membership tests 
and prints results.

1. initialize a list named students containing tuples of the form (student_name, score), 
for example ("alice", 78), ("bob", 52), ("carol", 89), ("dave", 45), ("eve", 92).

2. hard code the passing score to be 40 

3. use a for loop and if conditions to iterate over students and build two lists: passed 
(tuples where score >= passing score) and failed (tuples where score < passing score).

4. using list slicing, print the first two entries in the passed list; then use an if 
condition to check whether ("bob", 52) is in the failed list and print an appropriate message.

5. use a for loop to iterate over passed and print each student's name in uppercase.

'''

fail_list = []
pass_list = []

students = [("rar",100),("Aryan",5),("reyna",18),("Anita",55),("meesha",89),("bob", 52)]
passing_score = 40
# for i in students: can't compare a tuple to a number(i is a tuple), need to extract score part
for name, score in students:
    if score>= passing_score:
      # if score in students[0:2:1]: WRONG cannot compare score(a number) with tuple. slicing is done W PRINTING
      #   pass_list.append(name,score): keep another bracket
         pass_list.append((name,score))
    else:
        fail_list.append((name,score))
   # if ("bob", 52) in fail_list:                     DOESNT NEED TO BE IN FOR LOOP AS ONLY LOOKING FOR ONE PERSON
   #       print("bob is in the fail list")
   #       else:
   #          print("bob is not in the fail list")
if ("bob", 52) in fail_list:                     
   print("bob is in the fail list")
else:
   print("bob is not in the fail list")
      
print(pass_list)
print(fail_list)
print(pass_list[0:2:1])

for name,score in pass_list:
   # print((upper(name),score))   WRONG> its name.upper
   print((name.upper(),score))
