"""
String's Validation Methods
    isdigit , isalpha , isalnum

st = "2375"
print( st.isdigit() )
print( st.isalpha() )
print( st.isalnum() )
st = "aman"
print( st.isdigit() )
print( st.isalpha() )
print( st.isalnum() )
st = 'aman123'
print( st.isdigit() )
print( st.isalpha() )
print( st.isalnum() )
st = "aman123@gmail.com"
print( st.isdigit() )
print( st.isalpha() )
print( st.isalnum() )

UDF :- User Define Functions
Function is a set/group of statement which perform a specific task
and return a value

Syntax:-
def funtion_name(parameters):
    definition/statements

function_name(arguments)

Example:-

def greet():
    print("Good Morning")


greet()
greet()
greet()


def greet(val):
    print("Good",val)


greet("Morning")
greet("Noon")
greet("After Noon")


def add(a,b):
    print(a+b)

add(10,20)



def add(a,b):
    return a+b

print( add(10,20) )
print( add(45,57) )


def add(a,b,c,d,e,f,g):
    return a+b+c+d+e+f+g

print( add(10,20,45,78,89,67,45) )



def add(a,b,c=0,d=0,e=0,f=0,g=0):
    return a+b+c+d+e+f+g

print( add(10,20,45,78,89,67,45) )
print( add(10,20,45) )
print( add(10) ) # at least two arguments



def add(a=0,b=0,c=0,d=0,e=0,f=0,g=0):
    return a+b+c+d+e+f+g

print( add(10,20,45,78,89,67,45) )
print( add(10,20,45) )
print( add(10) )
print( add() )  
print( add(324,45,67,7,6543,34) )
print( add(324,45,67,7,6543,34,34,5667,78,65,43,34) ) # more tha


def add( *a ):         # args
    print( type(a) )
    return sum(a)

print( add() )
print( add(10) )
print( add(10,34) )
print( add(10,34,5456,67,78,89,90,46) )


def add( **a ):        # kargs
    print(type(a))
    return a

print( add(name='Rahul Kumar' , course='B.Tech') )


# Recursion
A recursion is a property of a function in which a functions call
itself

def hello():
    print("Hello India")
    hello()
    
hello()


# WAP to add all the natural numbers using recursion

def add(n):
    if n==1:
        return 1
    else:
        return n+add(n-1)   

print( add(50) )


"""