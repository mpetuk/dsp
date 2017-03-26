# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are sequences; lists are mutable (can be modified) while tuples are immutable. You can view a tuple as a coherent unit. Also, lists arehomogeneous and tuples are heterogeneous (and can contain data of different type). Tuples will work as keys in dictionary because they are immutable.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Both sets and lists are collections, but sets are unordered collection of unique elements while lists are ordered and may contain duplicates. 
#Sets:
set1={11,12,13}
set2={6,9,12,13}
#Union the sets:
set3=set1.union(set2)
print(set3)

{11,12,14,6,9}

#Lists:
list1=[11,12,13]
list2=[6,9,12,13]
list3=list1+list2
print(list3)

[11,12,13,6,9,12,13]

Lists perform better than sets when it comes to iterating over their content. Sets are faster when it comes to determining presence of an object in the set. This is due to lists having their content indexed and sets have hashtable as an underlying structure.
---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambdas are small, anonymous, "thow away" functions created on a fly as and where needed. They are not tied to a name; are limited to one expression only and the result of which is a return value.

Example: 
 >>> sorted(['Some', 'words', 'sort', 'differently'], key=lambda word: word.lower())
['differently', 'Some', 'sort', 'words']

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are ways of describing that enables transforming one list into another list.
#Example:
L1=[1,2,3]
L2=[x*2 for x in L1 if x % 2==0]
print (L2)

[4]
#Equivalent with `map` and `filter`
L2=map(lambda x: x * 2, L1)
L3=filter(lambda x: x % 2==0,L2)
print(L3)

[4]

List comprehensions achieve same results as a combination of map() and filter() but in a clean, consitent, and elegant way.

A set comprehension can take (but don't need to) take a set as an input. Like list comprehensions can contain `if`clause.
>>> a_set={1,2,3}
>>> {x*2 for x in a_set if x % 2 == 0}
{4}

A dictionary comprehension is like a list comprehension, but it constructs a dictionary (key:value pairs) instead of a list.
>>> a_dict = {'a': 1, 'b': 2, 'c': 3}
>>> {value:key for key, value in a_dict.items()}
{1: 'a', 2: 'b', 3: 'c'}






--

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





