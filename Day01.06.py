"""
Built-in Functions:-   print , input , int , float , type

WAP to calculate gross salary of an employee where HRA is
20% and DA is 30% of his basic salary.
HINT:- Gross Salary  = Basic Salary + HRA + DA

bs = float(input("Enter Basic Salary : "))
hra = bs*0.20
da = bs*0.30
gs = bs + hra + da
print("Gross Salary :",gs)


Conditional Statements
if , if else, Nested if else , elif , complex condition
Looping:-   for , while

if
Syntax:-
if condition:
    True_Statement

if 10>5:
    print("Hello")   # it will print hello (cond it True)


if 10>50:
    print("Hello") # it will print nothing (cond is False)


if_else
if condition:
    True_Statement
else:
    False_Statement



if 10>50:
    print("Hello")
else:
    print("India")


if 10>50:
    print("Hello")
else:
    print("India")
print("World")  # this statement is out of if_else


# WAP to find a greater value b/w two

a = 100
b = 200
if a>b:
    print("Greater Value",a)
else:
    print("Greater Value",b)


# WAP to check an entered number is EVEN/ODD
# % (modulus) it is use to calculate the remainder

num = int(input("Enter A Number : "))
if num%2 == 0:
    print("Even")
else:
    print("Odd")


Nested if else
Syntax:-

if condition:
    if condition:
        true_statement
    else:
        false_statement
else:
    if condition:
        true_statement
    else:
        false_statement

# WAP to check a number is positive , negative or zero

num = 0
if num>0:
    print("Positive Number")
else:
    if num<0:
        print("Negative Number")
    else:
        print("Zero!")


# WAP to check an entered character is vowel/consonant
# Lets Assume :-   A,E,I,O,U (Vowel)

ch = 'M'
if ch=='A':
    print("Vowel")
else:
    if ch=='E':
        print("Vowel")
    else:
        if ch=='I':
            print("Vowel")
        else:
            if ch=='O':
                print("Vowel")
            else:
                if ch=='U':
                    print("Vowel")
                else:
                    print("Consonant")


ELIF

# WAP to check an entered character is vowel/consonant
# Lets Assume :-   A,E,I,O,U (Vowel)

ch = 'H'
if ch=='A':
    print("Vowel")
elif ch=='E':
    print("Vowel")
elif ch=='I':
    print("Vowel")
elif ch=='O':
    print("Vowel")
elif ch=='U':
    print("Vowel")
else:
    print("Consonant")


Complex Condition # (write all conditions together using logical operator)   

# WAP to check an entered character is vowel/consonant
# Lets Assume :-   A,E,I,O,U (Vowel)

ch = 'E'
if ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
    print("Vowel")
else:
    print("Consonant")


ch = 'M'
if ch in "AEIOUaeiou":
    print("Vowel")
else:
    print("Consonant")

Exercise:-
C : Nested if_else
21. Find the largest of 3 numbers.

a = 100
b = 200
c = 30
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)
        
"""
