"""
Looping:- we can execute a same task again and again using loop
Types of loop:-
for
while

FOR
Syntax:-
for variable_name in range(start , stop , step):
    statements

Example:-
print( *range(1,11,2) )
print( *range(1,11,1) )


for a in range(1,5,1): 
    print("Hello")


for a in range(1,11,1):
    print("Hello")


for a in range(1,11,2): 
    print("Hello")


for a in range(1,11,3): 
    print("Hello")


for a in range(1,11,1):
    print(a)


for a in range(1,11,2):
    print(a)


# by default step = 1
for a in range(1,11):
    print(a)


# by default step = 1
for a in range(5,9):
    print(a)


# by default start = 0
# by default step = 1
for a in range(5):
    print(a)


# WAP to print counting from 1 to 10
for i in range(1,11):
    print(i)


# WAP to print table of a number
num = int(input("Enter A Number : "))
for i in range(1,11):
    print(i*num)


# WAP to print table of a number
    3 * 1 = 3
    3 * 2 = 6

num = int(input("Enter A Number : "))
for i in range(1,11):
    print(num,"*",i,'=',i*num)

# WAP to print factors of a number
# HINT: 12 => 1,2,3,4,6,12

num = int(input("Enter A Number : "))
for i in range(1,num+1):
    if num%i==0:
        print(i)


# WAP to count the factors of a number
# HINT:- 12 => 1,2,3,4,6,12 => 6 factors

count = 0
num = int(input("Enter A Number : "))
for i in range(1,num+1):
    if num%i==0:
        print(i)
        count = count+1
print("Total Factors :",count)


# WAP to check a number is Prime or not

count = 0
num = int(input("Enter A Number : "))
for i in range(1,num+1):
    if num%i==0:
        print(i)
        count+=1
print("Total Factors :",count)
if count==2:
    print("Prime")
else:
    print("not Prime")


count = 0
num = int(input("Enter A Number : "))
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print("Prime")
else:
    print("not Prime")



count = 0
num = int(input("Enter A Number : "))
for i in range(2,num//2+1):
    if num%i==0:
        count+=1
        break
if count==0:
    print("Prime")
else:
    print("not Prime") 

"""
