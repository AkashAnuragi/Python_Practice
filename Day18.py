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
numbers = [10, 20, 30, 40, 50]

element = int(input("Enter the element to search: "))

if element in numbers:
    print("Element exists in the list")
else:
    print("Element does not exist in the list")

7. Write a Python program to remove duplicate elements from a list.
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_list = list(set(numbers))

print("List after removing duplicates:", unique_list)

8. Write a program to sort a list in ascending and descending order.
numbers = [5, 2, 9, 1, 7]

# Ascending order
numbers.sort()
print("Ascending order:", numbers)

# Descending order
numbers.sort(reverse=True)
print("Descending order:", numbers)

Intermediate Level 
9. Write a program to merge two lists and remove duplicates. 
li1 = [12,23,34,45,56,67,87]
li2 = [23,34,12,34,45,21,32]
li3 = li1 + li2
print(li3)
print(set(li3)


10. Write a program to find common elements between two lists. 
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = []

for i in list1:
    if i in list2:
        common.append(i)

print("Common elements:", common)

11. Write a program to split a list into even and odd numbers. 
12. Write a program to rotate a list by n positions. 
13. Write a Python program to find the second largest number in a list. 
14. Write a program to flatten a nested list. 
15. Write a program to count frequency of each element in a list. 
16. Write a program to replace all negative numbers with zero in a list. 

"""
      


























