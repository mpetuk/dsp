import csv, string, re, collections
reader=csv.DictReader(open('faculty.csv'))

degrees=[]
titles=[]
p = re.compile(r'\W+')
for row in reader:
  s=row[" degree"]
  s2=s.translate({ord("."):None})
  degrees.append(p.split(s2))

  s1=row[" title"]
  s21=re.sub(r'\bis\b','of',s1)
  titles.append(s21)

#print(degrees)
import itertools
one_list= filter(None,list(itertools.chain.from_iterable(degrees)))


#print(one_list)
from collections import Counter
freqs=Counter(one_list)
freqs2=Counter(titles)

print(freqs)
print(freqs2)


