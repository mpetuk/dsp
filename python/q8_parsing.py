# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

f=open('./football.csv', 'rb')
reader=csv.reader(f)

rownum = 0
for row in reader:
   if rownum == 0:
      header = row
   else:
      colnum = 0
for col in row:
   colnum += 1
   rownum +=1


print (row)


f.close()

