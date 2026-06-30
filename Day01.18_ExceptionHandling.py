"""
Exception Handling

Errors:- A mistake in your code
Types of error
1- Syntax Error
A typo mistake in your code
    print("Hello')  we should close with " commas
you need to fix the code, remove the error
This error will flag by interpreter and will not allow to run

2- Runtime Error
A mistake in the logic mostly happen at the time of user input
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)   # denominator should not zero
This error can not flag by interpreter, and this program will run
and crash at the running time that why its a Runtime Error
and its also called Exception
In this case you can handle or bypass the error

3- Symmetric Error/Logical Error
A error in your logic thats why sometimes you are not getting
desired output
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Addition :",a*b)  #  it should + not *
We need to debug the code and fix the error


RunTime / Exception Handling
    try , except , finally
try:
    your doubtful code here
except:
    Alternative Code here

Example

a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
try:
    print("Division :",a/b)
except:
    print("Division is not Possible")
print("Program Finished!")



try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
    print("Hello")
except:
    print("Division is not Possible")
print("Program Finished!")


Nested Except Block

try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
    a[0]
except ZeroDivisionError as e:
    print("Error :",e)
except ValueError as e:
    print("Error :",e)
print("Program Finished!")

try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
    a[0]
except ZeroDivisionError as e:
    print("Error :",e)
except ValueError as e:
    print("Error :",e)
except Exception as e:
    print("Error :",e)
print("Program Finished!")


try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
    a[0]
except Exception as e:
    print("Error :",e)
print("Program Finished!")


finally
this block will execute always
try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
except Exception as e:
    print("Error :",e)
finally:
    print("It will execute always")
print("Program Finished!")



try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
except ZeroDivisionError as e:
    print("Error :",e)
finally:
    print("It will execute always")
print("Program Finished!")


try:
    doubtful Code
except:
    Alternative Code
else:
    code will run if there is no error
finally:
    it will execute always


try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
except ZeroDivisionError as e:
    print("Error :",e)
else:
    print("Division Complete!")
finally:
    print("It will execute always")
print("Program Finished!")


Custom Condition

age = int(input("Enter Age : "))
if age>17:
    print("Login")
else:
    print("Age Should Be 18+")


assert for Custom Condition

age = int(input("Enter Age : "))
assert age>17  
print("Login")


age = int(input("Enter Age : "))
assert age>17, "Age Should Be 18+"
print("Login")



age = int(input("Enter Age : "))
try:
    assert age>17, "Age Should Be 18+"
    print("Login")
except Exception as e:
    print("Error :",e)



     raise for custom condition
     
age = int(input("Enter Age : "))
if age>17:
    print("Login")
else:
    raise ValueError("Age Should Be 18+")



age = int(input("Enter Age : "))
if age>17:
    print("Login")
else:
    raise ZeroDivisionError("Age Should Be 18+")



class AgeError(Exception):
    pass

age = int(input("Enter Age : "))
if age>17:
    print("Login")
else:
    raise AgeError("Age Should Be 18+")




class AgeError(Exception):
    pass

age = int(input("Enter Age : "))
if age>17:
    print("Login")
else:
    try:
        raise AgeError("Age Should Be 18+")
    except Exception as e:
        print("Error :",e)


""" 