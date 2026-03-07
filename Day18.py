"""
Python Programming Questions – LIST 
Basic Level 

1. Write a Python program to create a list of integers and print its elements.

li =[12,23,34,45,65,67]
print("The List is:",li)


2. Write a program to find the sum and average of all elements in a list.
li =[12,23,34,45,65,67]
total =sum(li)
average = total/len(li)
print("This is the List",li)
print("The Sum is:",total)
print("the Average of List is:",average)

3. Write a program to find the largest and smallest element in a list. 
li =[12,23,34,45,65,67]
print("The Maximum element is",max(li))
print("The Minimum element is",min(li))

4. Write a Python program to count the number of elements in a list without using len().
li =[12,23,34,45,65,67]

count = 0
for i in li:
    count+=1
print("the length of List is:",count)


5. Write a program to reverse a list without using built-in functions. 
li =[12,23,34,45,65,67]

reversed_list = []

i = len(li) - 1
while i >= 0:
    reversed_list.append(li[i])
    i -= 1

print("Original List:", li)
print("Reversed List:", reversed_list)


6. Write a program to check if an element exists in a list. 
7. Write a Python program to remove duplicate elements from a list. 
8. Write a program to sort a list in ascending and descending order.
"""
























