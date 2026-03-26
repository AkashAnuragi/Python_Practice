"""
UDF:- User Define Functions

def add(a=0,b=0,c=0):
    return a+b+c


print( add() )
print( add(10) )
print( add(10,20) )
print( add(10,20,30) )



def add(a,b=0,c=0):
    return a+b+c


print( add(10) )



def add(a,b,c=0):
    return a+b+c


print( add(10,20) )




def add(a,b,c):
    return a+b+c


print( add(10,20,30) )



# Assign the default value from the right side always

def add(*a):
    return sum(a)

print( add(23,78,89,978,67,56,54,23) )





def add(*args):
    return sum(args)

print( add(23,78,89,978,67,56,54,23) )





def add(**kargs):
    return kargs

print( add(name="Aman" , clas='XII') )




# WAF to calculate the cube of a number

def cube(val):
    return val**3


print( cube(6) )


Advance Python
    lambda , map , filter , reduce
Syntax:-
lambda_expression_name = lambda parameter: definition

# WAF to calculate the cube of a number

cube = lambda val: val**3

print( cube(6) )


# WAP to calculate the cube of all elements of a list

cube = lambda val:val**3

li = [ 1,2,3,4,5,6,7,8,9,10 ]
for x in li:
    print( cube(x) )



checkEven = lambda a : 'Even' if a%2==0 else 'Odd'
print( checkEven(6) )



checkEven = lambda a : 'Even' if a%2==0 else 'Odd'
li = [23,45,56,543,78,746,3356,53,34]

for x in li:
    print(x,"is",checkEven(x))




MAP
Syntax:-
    map( function_name , collection )

map will itterate a collection and apply a function
on each element of the collection

abc = lambda name:name[0:3].upper()

li = ['india','america','africa','germany']

print( list(map( abc , li )) ) 



# WAP to find cube of all elements of a list
cube = lambda val:val**3
li = [1,2,3,4,5,6,7,8,9,10]

result = list( map( cube , li ) )
print( result )



li = [1,2,3,4,5,6,7,8,9,10]
result = list( map( lambda val:val**3 , li ) )
print( result )




result = list( map( lambda val:val**3 , [1,2,3,4,5,6,7,8,9,10] ) )
print( result )




print(list( map( lambda val:val**3 , [1,2,3,4,5,6,7,8,9,10] ) ))

"""
