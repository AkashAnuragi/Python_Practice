"""
SET :- Set is a collection of unique hetreogenous elements
s = {32,43,56,46,87,89}

s = {32,43,56,46,87,89}
s = set()
s = set([2,43,56,678])
s = set((2,43,56,678))
s = {23,23.546,'Aman'}
print(s)

Order is not preserved in SET
SET has no INDEX
SET can not be sliced
SET can not be Replicate
But, Set can be traverse

s = {32,34,67,789,89,76}
print(s)
for a in s:
    print(a)

Built-in functions
    sum , max , min , len

s = {32,34,67,789,89,89,76}
print(s)
print( sum(s) )
print( max(s) )
print( min(s) )
print( len(s) )


SET's Methods
    add , pop , remove , discard , clear

s = {32,34,67,789,89,89,76}
print(s)
s.add(99)
print(s)
s.pop()
print(s)
s.remove(89)
print(s)
# s.remove(101)  # raise an error because 101 key is not available
s.discard(789)
print(s)
s.discard(101)   # will not raise any error if key is not available
print(s)
s.clear()
print(s)


SET's Methods
intersection , union , difference , symmetric_difference

s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
print( s1.intersection(s2) )  # common element
print( s1.union(s2) )  # elements of both sets (remove duplicates)
print( s1.difference(s2) )  # will remove elements from s1 which are also in s2
print( s1.symmetric_difference(s2) )  # remove common elements

SET's Operations

s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
print( s1&s2 )     # Intersection
print( s1|s2 )     # Union
print( s1-s2 )     # difference
print( s1^s2 )     # symmetric_difference


Dictionary:- Dictionary is a collection of key:value pair which is
called item.
key can not be duplicate
values can be duplicate


s = {1:232,2:567,5:677,'A':677,'Aman':568}
print(s)
print( s[5] )


Dictionary do not support INDEX
Dictionary works on KEYs
Dictionary can not be sliced
Dictionary can not be Replicate
But Dictionary can be Traverse

d = {1:232,2:567,5:677,'A':677,'Aman':568}
print(d)
for a in d:  # By default key traverse
    print(a)


Dictionary's Methods
    keys , values , items

d = {1:232,2:567,5:677,'A':677,'Aman':568}
print(d)
for a in d.keys():
    print(a)

d = {1:232,2:567,5:677,'A':677,'Aman':568}
print(d)
for a in d.values():
    print(a)


d = {1:232,2:567,5:677,'A':677,'Aman':568}
print(d)
for a in d.items():
    print(a)


d = {1:232,2:567,5:677,'A':677,'Aman':568}
print(d)
for k,v in d.items():
    print(k , v)


Dictionary's Methods
    get , pop , update

d = {1:232,2:567,5:677,'A':677,'Aman':568}
print(d)
print(d[2])
# print(d[200])   # raise an error because of 200 key is not available
print( d.get(2) )
print( d.get(200 , 'Not Available') )
d.pop('A')
print(d)
d2 = {3:99 , 4:88 , 5:66}
d.update(d2)
print(d)

"""
d = {1:232,2:567,5:677,'A':677,2:999,'Aman':568}
print(d)