'''
Built-in-librarues
math , random

import library_name

library_name.function_name(arguments)

import math
print(math.sqrt(9))
print(math.pow(5,3))


from library_name import function name
Example
from math import factorial  # only run factorial
print(factorial(5))

import random

print(random.random())
print(random.random()*100)
print(random.randint(1,9))
print(random.randint(100000,999999))

li = ["Data Science","Data Analyst", "Data Engineer"]
print(random.choice(li))
print(random.choices(li,k=2))

UDF: User Define functions

 def function_name(Parameter):
    definition of function
function_name(argument)
 
what is function?
function is a block of statement that perform a specific tast and return a value.

def greet():
    print("akash")
greet()

def greet(val):
    print("Akash",val)
greet("Anuragi")
greet("Sharma")
greet("Singh")
greet("Kumar")

def add(a,b):
    print(a+b)
add(2,3)

def add(a,b=0):
    print(a+b)
add(2)
add(2,4)


def add(a=0,b=0,c=0):
    print(a+b+c)
add(2)
add(2,4)
add(1,2,4)


def add(*a):  # this behave like a tuple (2),(2,4),(1,2,4)
    print(sum(a))
add(2) #2
add(2,4) #6
add(1,2,4) #7


def add(a,b,c=0):
    c=a+b
    print(c)
z = add(1,2)


def add(a,b):
    c=a+b
    return c
z=add(1,2)
print(z)



def f(a, b):
    a = a + b
    return a
x = 5
f(x, 3)
print(x)


def f():
    return 1, 2, 3
a, b ,c= f()
print(a,b,c)

def f(lst=[]):
    lst.append(1)
    return lst
print(f())
print(f())


def f(x):
    if x == 1:
        return 1
    return x * f(x - 1)
print(f(4))     


'''
'''
def f(k):
    print("Akash")
    f(k-1)
f(5)'''


'''
def pattern(n,ans=""):
    if(len(ans)==5):
        print(ans)
        return
    for i in range(len(n)):
        pattern(n[:i]+n[i+1:],ans+n[i])
    
pattern("ABCDE")'''

from functools import reduce



'''
for i in li:
    if i%2 == 0:
         m = i*i*i
         print(m)
'''
# OR 

li = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda val:val%2==0,li))
print(even)

cube = list(map(lambda n:n**3,even))
print(cube)

red = reduce(lambda n1,n2:n1+n2,cube)
print(red)




