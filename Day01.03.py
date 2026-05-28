"""
Bilt-in Function
print, input, int, float


print is used to print a statement to console


print("Hello Akash")
print("Hello World")
print('''
Hello!

My name is Akash Anuragi.
I am From Meerut''')

a = 10
print(a)

print('Value of a is :',a)

a =278
b=384
print("Value of a is",a,"and value of b is",b)
print(f"Value of a is {a} and Value of b is {b}")

a = 10
b = 20
c = a+b
print("Addition :",c)


input  is use to ask value from the user
input always return a text/string value

a = input("Enter A Number : ")
b = input("Enter B Number : ")
c = a+b
print("Addition :",c)  # Concatenation

int    is use convert a string/text to numeric (do not support to decimal/point value)

a = int( input("Enter A Number : ") )
b = int( input("Enter B Number : ") )
c = a+b
print("Addition :",c)  # Addition


loat (support to decimal/point value)

a = float( input("Enter A Number : ") )
b = float( input("Enter B Number : ") )
c = a+b
print("Addition :",c)  # Addition

WAP to calculate the gross salary of an employee where
HRA is 20% and DA is 30% of his basic salary.
HINT:- Gross_Salary = Basic_Salary + HRA + DA


bs = float(input("Enter Basic Salary : "))
hra = bs*0.20
da  = bs*0.30
gs  = bs+hra+da
print( "Gross Salary :",gs )

# Python is a dynamic Programming Language
a = 34
print( type(a) ) 
a = 34.45
print( type(a) ) 
a = 'aman'
print( type(a) )


 Operators
        a+b  =>  a,b ->  (operand)  ,  + (operator)
        operator operates on operands
1. Arithmetic Operator
    + - * / % // **

a = 7
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print( a%b )  # % modulus (use to calculate the remainder)
print( 11%4 )
print( a//b ) # // floor division / truncation
print( 11//4 )# remove decimal part
print( 2**5 ) # ** Exponential (to calculate the power)
print( 5**3 ) # 5 to the power 3 =>  5*5*5


2. Assignment Operator
        =
    += , -= , *= etc

a = 10
a += 1    #=>   a = a+1
a *= 2    #=>   a = a*2
print(a)


3. Relational Operator (return boolean Answer)
                Boolean -> True/False
    > < >= <= == !=

a = 7
b = 5
print( a>b )
print( a<b )
print( a>=b )
print( a<=b )
print( a!=b )  # is not equal to
print( a==b )  # is equal to


4. Membership Operator (check existance)
    in  ,  not in   (return boolean True/False)

a = "aman"
b = "amankumar"
print( a in b )
print( 'ankum' in b )
print( 'ka' in b )
print( 'ka' not in b )


a = [1,2,3]
b = [1,2,3]
print ( a in b )  # False
a = [1,2,3]
b = [1,2,[1,2,3],3]
print ( a in b )  # True

"""


