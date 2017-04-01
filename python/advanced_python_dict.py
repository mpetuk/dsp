import csv, string, re, collections
reader=csv.DictReader(open('faculty.csv'))

names=[]
lnames=([])
fnames=[]

degrees=[]
titles=[]
emails=[]

combo=[]

for row in reader:
    name=row["name"]
    lname=name.split()[-1]
    fname=name.split()[0]
    
    lnames.append(lname)
    fnames.append(fname)
    
    degree=row[" degree"]
    degrees.append(degree)

    title=row[" title"]
    titles.append(title)

    e=row[" email"]    
    emails.append(e)
   
    combo.append((degree,title,e))
    names.append((fname,lname))


#Q6: Creating dictionary with multiple list values
from collections import defaultdict
faculty_dict = defaultdict(list)
for nm, cm in zip(lnames,combo):
    faculty_dict[nm].append(cm)

#print (faculty_dict)

#Print first 3 pairs
first3pairs_1 = {k: faculty_dict[k] for k in list(faculty_dict.keys())[:3]}

print(first3pairs_1)

#Q7: Dictionary with unique keys
professor_dict = {}
for i in range(len(names)):
   professor_dict[names[i]] = combo[i]

#Print first 3 pairs
first3pairs_2 = {k: professor_dict[k] for k in list(professor_dict.keys())[:3]}

print(first3pairs_2)

#Q8:
from collections import OrderedDict
OrderedDict(sorted(professor_dict.items(), key=lambda t: sorted(names.items())))


#print(names)
#print(lnames)
#print(fnames)
