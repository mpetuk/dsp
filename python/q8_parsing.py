# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

reader=csv.DictReader(open('football.csv'))

mindiff = None
team_x = None
for row in reader:
   diff=abs(int(row['Goals']) - int(row['Goals Allowed']))
   if mindiff is None or mindiff > diff:
      mindiff = diff
      team_x = row['Team']
print ("The team with the smallest difference in 'for' and 'against' goals of", mindiff,"is", team_x)
