global name
name= 'Anwar'

print(name)

def modify_and_print_name():
    global name
    name='Rishkar'
    print(name)
    
modify_and_print_name()

print(name)

'''
Anwar
Rishkar
Anwar
'''