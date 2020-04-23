
""" decimal """


import decimal 
from decimal import Decimal


decimal.getcontext().prec = 4 # set how many digits
d = Decimal(1) / Decimal (11)
 

""" String """

t = 'this is a string object'
t.capitalize()
t.split()
t.find('this') # if there do not have that word, it will response -1
t.replace('','|') # change character
t.strip('this')



""" date """
import re
series = """
'01/18/2014 13:00:00', 100, '1st'; '01/18/2014 13:30:00', 110, '2nd';
'01/18/2014 14:00:00', 120, '3rd' """
dt = re.compile("'[0-9/:\s]+'") # datetime
result = dt.findall(series)
result


from datetime import datetime
pydt = datetime.strptime(result[0].replace("'", ""), '%m/%d/%Y %H:%M:%S')
pydt
print(pydt)
print(type(pydt))



""" Basic data structure """
# tuple
t = (1, 2.5, 'data')
type(t) # tuple
type(t[0]) # int
type(t[2]) # str


# list
l = list(t)
l.append([4, 3]) # append list at the end
l.extend([1.0, 1.5, 2.0]) # append elements of list
l.insert(1, 'insert') # insert object before index position
l.remove('data') # remove first occurrence of object
p = l.pop(3) # removes and returns object at index
l[2:5]


r = range(0, 8, 1) # start, end, step width
type(r)

""" loop """

for i in range(2, 5): 
    print(l[i]**2)

for i in range(1, 10): 
    if i % 2 == 0: # % is for modulo 
        print("%d is even" % i)
    elif i % 3 == 0: 
        print("%d is multiple of 3" % i)
    else: print("%d is odd" % i)
    
total = 0
while total < 100: 
    total += 1
print(total)

m = [i ** 2 for i in range(5)] 
m

def f(x): 
    return x ** 2
f(2)

def even(x):
    return x % 2 ==0
even(1)

list(map(even, [1,2,3])) # if use list() before,  then you need add list in front of the function
list(map(lambda x: x ** 2, range(10)))

def cumsum(l): 
    total = 0 
    for elem in l: 
        total += elem
    return total 
cumsum(range(10))
