"""
Tuple:- Tuple is a collection of hetregenous elements
Syntax:-
t = (23,45,89,74,15,34)

t = (23,45,89,74,15,34)
t = (45,52.46,'A',True,'Aman',2+8j)
t = ()
t = tuple()
t = tuple([23,45,56,78,943])
t = tuple((634,46,63,52,24))
print(t)
print(type(t))


Tuple works on INDEX
backward (-1,-2,-3,..), forward(0,1,2,3,4..)
tuple_name[index]

t = (23,45,89,74,15,34)
print(t)
print( t[2] )
print( t[-3] )

Tuple can be sliced also
tuple_name[start_index:stop_index:step]

t = (23,45,89,74,15,34)
print( t )
print( t[2:5] )
print( t[-4:-1] )

Replication
t = (23,45,67,89)
print(t)
print(t*3)


Traversing
t = (23,45,67,89)
for x in t:
    print(x)

Built-in functions
    sum , max , min , len

t = (23,45,67,89)
print(t)
print( sum(t) )
print( max(t) )
print( min(t) )
print( len(t) )

Tuple's Method
    index , count

t = (23,45,7,23,45,67,23,45,56)
print(t)
print( t.count(23) )
print( t.index(7) )


Tuple is immuteable, you can not change anything in the tuple
Tuple is faster than the list because of its immuteabilty

SET :- Set is also a collection of unique hetreogenous
elements

Syntax:-
s = {34,45,67,78,90}

s = {23,3,56,787,654}
s = {234,567.323,'Aman',True}
s = set()
s = set([34,56,677,89,57])
print(s)
print(type(s))


s = {34,56,77,45,897,65,42}
print( s )  # print elements on random positions

s = {21,34,34,45,54,23,32,4,23,23,23,45,45}
print(s) # remove duplicate elements

"""