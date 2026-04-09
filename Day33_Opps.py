"""
OOPs => Object Oriented Programming
    Python
class , object
encapsulation , inheritance , polymorphism , abstraction

class:- Class is a virtual entity
class is a blue print of an object
class is a representation of encapsulation

Object:- Object is a Real entity
Object is a instance/implementation of a class

Syntax:-
class class_name:
    definition

class myclass:
    name = 'A30 S'
    color = 'red'

obj = myclass()
obj2 = myclass()
obj.color = "Black"
print( obj )
print( obj.color )
print( obj.name )
print( obj2.color )


Encapsulation:- All data members and methods should in
one unit(class).
Encapsulation is the representation of class.

class myclass:
    name = 'A30 S'
    color = 'red'
    def myfun():
        print("My Name is myclass")


class myclass:
    x = 10
    def myfun(self):
        print("I am in myclass")

obj = myclass()
obj.myfun()



Constructor:- Constructor is a property of a method, where
a method call automatically when an object will create.
constructor method name should be __init__ .

class myclass:
    x = 10
    def __init__(self):
        print("I am in myclass")

obj = myclass()


"""

class myclass:
    x = 10
    def __init__(self):
        print("I am in myclass")
    def __init__(self):
        print("Hello Everyone!")
    

obj = myclass()  # last constructor will be called due to overwrite

