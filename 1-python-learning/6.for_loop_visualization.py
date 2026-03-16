
'''
1 2  3  4  5
2 4  6  8 10
3 6  9 12 15
4 8 12 16 20
'''
# numbers=[[1, 2 , 3  ,4 , 5]  
# [2, 4 , 6 , 8 ,10],
# [3, 6 , 9 ,12 ,15],
# [4 ,8 ,12 ,16, 20]]


# num_cols=5
# num_rows=4

# for row in range(1,num_rows+1):
#    for col in range(1,num_cols+1):
#       print(col*row,end='')
#       print(' ',end='')
#    print()

'''
Print a rectangle of * with 4 rows and 6 columns.

******
******
******
******
'''
num_rows = 4
num_columns = 6
for rows in range(1,num_rows+1):
   for columns in range(1,num_columns+1):
      print(rows*columns)