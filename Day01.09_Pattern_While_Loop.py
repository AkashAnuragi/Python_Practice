"""
Nested Loop
Pattern Programs

*****
*****
*****
*****
*****


print("*****")
print("*****")
print("*****")
print("*****")
print("*****")

print("*****\n*****\n*****\n*****\n*****\n")

print("*****\n"*5)

for i in range(5):
    print("*****")

# columns
*****# row
*****
*****
*****
*****


for i in range(1,6):  
    for j in range(1,6):  
        print("*",end='')
    print()


*
**
***
****
*****


for i in range(1,6):
    for j in range(1,i+1):
        print("*",end='')
    print()


1
12
123
1234
12345


for i in range(1,6):  
    for j in range(1,i+1): 
        print(j,end='')
    print()



1
22
333
4444
55555


for i in range(1,6): 
    for j in range(1,i+1): 
        print(i,end="")
    print()



1
23
456
78910

k = 1
for i in range(1,5):
    for j in range(1,i+1):
        print(k,end="")
        k = k+1
    print()


0
12
345
6789


k = 0
for i in range(1,5):
    for j in range(1,i+1):
        print(k,end="")
        k = k+1
    print()


1
23
456
7890


k = 1
for i in range(1,5):
    for j in range(1,i+1):
        if k!=10:
            print(k,end="")
        else:
            print(0,end='')
        k = k+1
    print()


k = 1
for i in range(1,5):
    for j in range(1,i+1):
        print(k%10,end="")
        k = k+1
    print()


1
01
010
1010
10101

k = 1
for i in range(1,6):
    for j in range(1,i+1):
        print(k%2,end="")
        k=k+1
    print()

A
AB
ABC
ABCD
ABCDE


for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end="")
    print()


A
AB
ABC
ABCD
ABCDE


for i in range(1,6):
    for j in range(1,i+1):
        print(chr(j+64),end="")
    print()

A
BB
CCC
DDDD
EEEEE


for i in range(1,6):
    for j in range(1,i+1):
        print(chr(i+64),end="")
    print()


A
BC
DEF
GHIJ
KLMNO

k = 65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(k),end="")
        k=k+1
    print()


    *
   **
  ***
 ****
*****


for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print('*',end="")
    print()

    *
   * *
  * * *
 * * * * 
* * * * *


for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print('* ',end="")
    print()


   *
  ***
 *****
*******
 *****
  ***
   *

*****
****
***
**
*

i = 1
m = 1
while i>=1:
    for k in range(4,i,-1):
        print(end=' ')
    for j in range(1,2*i):
        print("*",end="")
    print()
    i = i+m
    if i==4:
        m=-1


"""