"""
while loop
Syntax:-

initilization
while condition:
    statements
    incr/decr

Example:-

a = 1
while a<=5:
    print("Hello")
    a = a+1


a = 1
while a<=5:
    print(a)
    a = a+1


a = 1
while a<=10:
    print(a)
    a = a+1


# WAP TO PRINT TABLE OF 2
a = 2
while a<=20:
    print(a)
    a = a+2


a = 5
while a<=50:
    print(a)
    a = a+5


num = int(input("Enter A Number : "))
a = 1
while a<=10:
    print(a*num)
    a = a+1


num = int(input("Enter A Number : "))
a = 1
while a<=10:
    print(a*num)
    a = a+1


choice = 'Y'
while choice in "Yy":
    name = input("Enter Name : ")
    mob = input("Enter Mobile : ")
    choice = input("Do You Want To Continue(Y/n) : ") 


# WAP TO add all digits of a number
# 754 =>  7+5+4 => 16

add = 0
num = int(input("Enter A Number : "))
while num>0:
    rem = num%10   
    add = add+rem  
    num = num//10  
print("Addition of Digits :",add)


# WAP to reverse a Number

add = 0
num = int(input("Enter A Number : "))   
while num>0:
    rem = num%10    
    add = add*10+rem  
    num = num//10     
print("Reverse Number :",add)

"""
