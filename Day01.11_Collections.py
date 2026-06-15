"""
Collection:- List , Tuple , Set , Dictionary , String
Sequence DataType
    List , Tuple
List:- List is a collection of hetreogenous(different)
elements
syntax:-
list_name = [ele1,ele2,ele3..]

li = [2,5,78,89,76,45,45]
li = [234,34.56,-45.67,True,'A',3+8j,'Aman']
li = []
li = list()
li = list([23,56,56,67,89])
li = list((23,56,56,67,89))
print(li)
print(type(li))


List works on INDEX
forward   0,1,2,3,4,..
backward  -1,-2,-3....
list_name[index]

li = [23,45,67,45,23,56,78]
print(li)
print(li[2])
print(li[-3])

Slicing
    list_name[start_index:stop_index:step_index]

li = [23,45,67,45,23,56,78]
print(li)
print(li[3:6:1])
print(li[3:6])
print(li[3:6:2])
print(li[-2:-6:-1])
print(li[-6:-2])


Replication
li = [1,2,3,4,5]
print( li )
print( li*3 )  # it will repeat all elemets from 3 times

Traversing
li = [23,89,67,34,45,78,90]
print(li)
for x in li:   # itteration
    print(x)


Built-in functions
    sum , max , min , len

li = [23,89,67,34,45,78,90]
print(li)
print( sum(li) )
print( max(li) )
print( min(li) )
print( len(li) )
print( sum(li)/len(li) )


List's Methods
    append , extend , insert

li = [1,34,45,67,9,34,56]
print(li)
li.append(99)
print(li)
li.insert( 2,88 )
print(li)
li2 = [11,22,33,44]
li.extend(li2)
print(li)


    pop , remove , del , clear

li = [234,456,78,7,654,32]
print(li)
li.pop()  # delete last element by default
print(li)
li.pop(2)   # pop(index)
print(li)
li.remove(7)   # remove(value)
print(li)
del li[1]     # del keyword
print(li)
li.clear()
print(li)


        sort , reverse

li = [78,23,67,45,682,63]
print(li)
li.reverse()
print(li)
li.sort()
print(li)
li.sort(reverse=True)
print(li)

        index , count

li = [23,67,89,63,48,35,63,457,76,45,63]
print(li)
print( li.count(63) )
print( li.index(48) )
print( li.index(63,4) )
print( li.index(63,4,7) )

# WAP to print sum of all elements of a list

li = [24,85,34,58,25]
print(li)
add = 0
for x in li:
    add=add+x
print(add)

"""