"""

def cube(num):
    return num**3

print( cube(9) )
print( cube(5) )


Advance Python
lambda Expression
    map , filter , reduce

function_name = lambda parameter : definition

# Lambda Expression
cube = lambda num : num**3

print( cube(9) )
print( cube(5) )


def checkEven(num):
    if num%2==0:
        return 'Even'
    else:
        return 'Odd'

li = [23,45,67,78,7665,43,32,4,56,78]
for i in li:
    print( i,'\t',checkEven(i) )



checkEven = lambda num: 'Even' if num%2==0 else 'Odd'

li = [23,45,67,78,7665,43,32,4,56,78]
for i in li:
    print( i,'\t',checkEven(i) )


checkEven = lambda num : num%2==0

li = [23,45,67,78,7665,43,32,4,56,78]
for i in li:
    print( i,'\t','Even' if checkEven(i) else 'Odd' )


square = lambda num:num**2

li = [23,45,67,78,7665,43,32,4,56,78]
for i in li:
    print( i,'\tSquare -> ',square(i) )


    map , filter , reduce

square = lambda num:num**2
li = [23,45,67,78,76,65,43,32,4,56,78]
print(li)
res = list( map(square , li) )
print(res)


cube = lambda num:num**3
li = [1,2,3,4,5,6,7,8,9,10]
res = list( map(cube , li) )
print(res)



checkEven = lambda num : num%2==0
li = [23,56,89,57,3,2,54,5,8,86,64,35]
for i in li:
    if checkEven(i):
        print(i)

    filter

checkEven = lambda num : num%2==0
li = [23,56,89,57,3,2,54,5,8,86,64,35]
res = list( filter(checkEven , li) )
print(res)


add = lambda a,b:a+b
li = [1,2,3,4,5,6,7,8,9,10]
res = 0
for i in li:
    res = add(res,i)
print(res)


    reduce

from functools import reduce
add = lambda a,b:a+b
li = [1,2,3,4,5,6,7,8,9,10]
res = reduce(add , li)
print( res )


# WAP to add cubes of all even numbers of a list

from functools import reduce
li = [2,3,3,4,5,5,7,7,8,9,5,4]
res = filter( lambda num:num%2==0 , li )
res = map( lambda num:num**3 , res )
res = reduce( lambda a,b:a+b , res )
print(res)

"""
