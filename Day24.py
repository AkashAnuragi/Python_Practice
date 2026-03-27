"""
Advance Python
Generator
lambda , map , filter , reduce

# WAF to calculate the cube of number
def cube(num):
    return num**3
    
cube = lambda num: num**2

print( cube(4) )



li = [x for x in range(1,11)]  # list comprehension
print(li)


li = [x for x in range(2,21,2)]
print(li)

li = [x for x in range(1,21) if x%2==0]
print(li)



cube = lambda num: num**2
li = [x for x in range(1,11)]
print(li)
for i in li:
    print( cube(i) )


MAP
map is use to apply a function/property on every element
of a collection

cube = lambda num: num**3
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(li)
result  = list( map( cube , li ) )
print( result )



findEven = lambda val : 'Even' if val%2==0 else 'Odd'
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = list( map(findEven , li) )
print(res)



FILTER

findEven = lambda val : True if val%2==0 else False
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = list( filter(findEven , li) )
print(res)


findVowel = lambda v : v in "AEIOUaeiou"
res = list( filter(findVowel,"RAHUL KUMAR") )
print(res)


findVowel = lambda v : v in "AEIOUaeiou"
res = list( filter(findVowel,"My name is aman singh") )
print(res)



REDUCE

from functools import reduce

add = lambda a,b:a+b
li = [1,2,3,4,5,6,7,8,9,10]
res = reduce( add , li )
print( res )




from functools import reduce
li = [ 1,2,3,4,5,6,7,8,9,10 ]
res = filter( lambda x:x%2==0 , li )
res = map( lambda x:x**3 , res )
res = reduce(lambda a,b:a+b , res )
print(res)




from functools import reduce
li = [ 1,2,3,4,5,6,7,8,9,10 ]
res = list(filter( lambda x:x%2==0 , li ))
print(res)
res = list(map( lambda x:x**3 , res ))
print(res)
res = reduce(lambda a,b:a+b , res )
print(res)


from functools import reduce
li = [ 1,2,3,4,5,6,7,8,9,10 ]
print( reduce( lambda a,b:a+b , map(lambda x:x**3 , filter(lambda x:x%2==0 , li)) ) )



"""

from functools import reduce
li = [ 1,2,3,4,5,6,7,8,9,10 ]
print( reduce( lambda a,b:a+b , map(lambda x:x**3 , filter(lambda x:x%2==0 , li)) ) )
