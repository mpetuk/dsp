import csv, string, re, collections
reader=csv.DictReader(open('faculty.csv'))

degrees=[]
titles=[]
emails=[]
domains=[]
p = re.compile(r'\W+')
for row in reader:
  s=row[" degree"]
  s2=s.translate({ord("."):None})
  degrees.append(p.split(s2))

  s1=row[" title"]
  s21=re.sub(r'\bis\b','of',s1)
  titles.append(s21)

  e=row[" email"]
  emails.append(e)
  
  d=e[e.find("@")+1:]
  domains.append(d)
  
  #Alternative way for domain accumulation
  #d = re.search("@[\w.]+", e)
  #d1= d.translate({ord("@"):None})
  #domains.append(d.group()) 

#print(degrees)
import itertools
one_list= filter(None,list(itertools.chain.from_iterable(degrees)))


#print(one_list)
from collections import Counter
freqs_degrees=Counter(one_list)
freqs_titles=Counter(titles)
freqs_domains=Counter(domains)

print(freqs_degrees)
print(freqs_titles)
print(emails)
print(freqs_domains)

