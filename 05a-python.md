# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists and tuples are similar becayse they are used to store one or more objects/value in a specific order. One big difference between the two is that tuples are immutable while lists are mutable and for this reason, tuples work as keys for dictionaries. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Lists and sets both are used to store expressions. List is an ordered sequence of elements whereas Set is a distinct list of elements which is unordered. List comprehension, indexing, and slicing makes it easier to find elements in lists compared to sets. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

The lambda operator or lambda function is a way to create small anonymous functions, i.e. functions without a name. These functions are throw-away functions, i.e. they are just needed where they have been created.


```
class Student:
        def __init__(self, name, grade, age):
                self.name = name
                self.grade = grade
                self.age = age
        def __repr__(self):
                return repr((self.name, self.grade, self.age))
        def weighted_grade(self):
                return 'CBA'.index(self.grade) / float(self.age)

student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
]
sorted(student_objects, key=lambda student: student.age)  

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x=="Python", languages)
```
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions are a powerful way to generate lists using the for/in and if keywords. 
Example of list comprehensions: 
```
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50
```


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```
```
from datetime import datetime
 y = datetime.strptime(date_start, '%m-%d-%Y')
 z = datetime.strptime(date_stop, '%m-%d-%Y')
 delta= z-y
 print delta
``` 
delta= 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```
```
from datetime import datetime
 y = datetime.strptime(date_start, '%m%d%Y')
 z = datetime.strptime(date_stop, '%m%d%Y')
 delta= z-y
 print delta
``` 
 delta = 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```
```
from datetime import datetime
 y = datetime.strptime(date_start, '%d-%b-%Y')
 z = datetime.strptime(date_stop, '%d-%b-%Y')
 delta= z-y
 print delta
``` 
 delta= 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





