"""
Exception Handling :-
    try , except , finally , else

try:
    keep your code here, where you have doubt (Exception)
except:
    keep alternate code here(execute if an error occur)
else:
    this part will be excute, when there is no error in try block
finally:
    it will execute always


# Example
a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
try:
    print("Division :",a/b)
except Exception as e:
    print("Error :",e)
else:
    print("Division Complete!")
finally:
    print("Program Complete!")


# assert

using assert keyword you can raise a custom exception
age = int(input("Enter Your Age : "))
assert age>17
print("Welcome!")


age = int(input("Enter Your Age : "))
assert age>17 , "Age Should Be 18+"
print("Welcome!")



age = int(input("Enter Your Age : "))
try:
    assert age>17 , "Age Should Be 18+"
    print("Welcome!")
except:
    print("Sorry!, You can not login!")


age = int(input("Enter Your Age : "))
try:
    assert age>17 , "Age Should Be 18+"
    print("Welcome!")
except Exception as e:
    print("Sorry!, You can not login!")
    print("Reason :",e)


# raise
raise is use to raise a custom exception (error)

age = int(input("Enter Your Age : "))
if age<18:
    raise ZeroDivisionError("Age Should Be 18+")
print("Welcome!")


age = int(input("Enter Your Age : "))
if age<18:
    raise ValueError("Age Should Be 18+")
print("Welcome!")



class AgeError(Exception):
    pass

age = int(input("Enter Your Age : "))
if age<18:
    raise AgeError("Age Should Be 18+")
print("Welcome!")


try , except , finally , else , assert , raise

"""
