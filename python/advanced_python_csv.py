import csv
reader=csv.DictReader(open('faculty.csv'))

emails=[]
for row in reader:
     e=row[" email"]
     emails.append(e)

print(emails)

with open('emails.csv','w') as output:
   writer=csv.writer(output,lineterminator='\n')
   for val in emails:
      writer.writerow([val])
   
