"""
Exception Handling

Types of Error:-
1- Syntax Error / Compile Time Error
An error in your written code, from which program can not
execute and error flaged by interpreter at the time of
compling
Example:-
a = 10
print("Hello"a)
print("Hello",a

YOU HAVE TO FIX THIS ERROR!




2- Runtime Error / Logical Error / Exception 
In runtime error, program will execute and show the error
on console screen, and this error can not be flagged by
interpreter

WE CAN HANDLE THIS ERROR/EXCEPTION




3- Symantic Error
a = 20
b = 10
print("Addition :",a-b)
YOU NEED TO DEBUG THIS ERROR
This kind of error can not be flagged by interperted and
it will not raise on runtime



Runtime Error/Exception Handle
    try , except , finally , else


try:
    Mention code where, where an error can occur
except:
    An alternative code to handle the error


a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
print("Division :",a/b)
print("Program Complete")




a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
try:
    print("Division :",a/b)
except:
    print("Division Can Not Possible")
print("Program Complete")



try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
except:
    print("Division Can Not Possible")
print("Program Complete")



You can mention the Exception name

try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
except ZeroDivisionError as e:
    print("Error :",e)
print("Program Complete")




Nested except

try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
except ZeroDivisionError as e:
    print("Error :",e)
except ValueError as e:
    print("Error :",e)
print("Program Complete")



li = [2,5]
try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
    print(li[2])
except ZeroDivisionError as e:
    print("Error :",e)
except ValueError as e:
    print("Error :",e)
except IndexError as e:
    print("Error :",e)
print("Program Complete")



li = [2,5]
try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
    print(li[2])
except ZeroDivisionError as e:
    print("Error :",e)
except ValueError as e:
    print("Error :",e)
except Exception as e:
    print("Error :",e)
print("Program Complete")


li = [2,5]
try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
    print(li[2])
except Exception as e:
    print("Error :",e)
print("Program Complete")

Exception class is the mother class or every exception class



Finally

It will work always

try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
except Exception as e:
    print("Error :",e)
finally:
    print("ye to hamesha chalega")
print("Program Complete")




try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
except ZeroDivisionError as e:
    print("Error :",e)
finally:
    print("ye to hamesha chalega")
print("Program Complete")

ELSE
"""
