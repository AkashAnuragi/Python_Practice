"""
class
object
Encapsulation + Constructor   ( __init__ )


class myclass:
    x = 100
    def myfun(self):
        print("I am myfun and I am in myclass")
        print("value :",self.x) 
    def __init__(self):
        print("I am constructor")
    def myfun2():
        print("I am fun2 and I am in class myclass")

obj1 = myclass()
obj1.myfun()
myclass.myfun2()


# Decorator
class myclass:
    x = 100
    @staticmethod
    def myfun2():
        print("I am fun2 and I am in class myclass")

obj = myclass()
obj.myfun2()


Inheritance
# Single Inheritance
class A:
    def myfun1(self):
        print("I am myfun1 from class A")
class B(A):
    def myfun2(self):
        print("I am myfun2 from class B")

obj = B()
obj.myfun1()

# Multiple Inheritance

class A:
    def myfun1(self):
        print("I am myfun1 from class A")
class B:
    def myfun2(self):
        print("I am myfun2 from class B")
class C(A,B):
    def myfun3(self):
        print("I am myfun3 from class C")

obj = C()
obj.myfun1()
obj.myfun2()
obj.myfun3()



# MultiLevel Inhertiance

class A:
    def myfun1(self):
        print("I am myfun1 from class A")
class B(A):
    def myfun2(self):
        print("I am myfun2 from class B")
class C(B):
    def myfun3(self):
        print("I am myfun3 from class C")

obj = C()
obj.myfun1()
obj.myfun2()
obj.myfun3()
obj = B()
obj.myfun1()
obj.myfun2()

# Heerarchial Inheritance

class A:
    def myfun1(self):
        print("I am myfun1 from class A")
class B(A):
    def myfun2(self):
        print("I am myfun2 from class B")
class C(A):
    def myfun3(self):
        print("I am myfun3 from class C")

obj = C()



# Hybrid Inheritance

class A:
    def myfun1(self):
        print("I am myfun1 from class A")
class B(A):
    def myfun2(self):
        print("I am myfun2 from class B")
class C(A):
    def myfun3(self):
        print("I am myfun2 from class B")
class D(B,C):
    def myfun4(self):
        print("I am myfun2 from class B")

obj = C()


# Polymorphishm => (poly(many) + morphism(forms))
# Function Overloading

class myclass:
    def add(self , a , b):
        print( a+b )

obj = myclass()
obj.add(10,20)
obj.add("Aman","Kumar")
obj.add( [1,2,3],[4,5,6] )


# Function Overridding

class A:
    def myfun(self):
        print("I am myfun from class A")
class B(A):
    def myfun(self):
        print("I am myfun from class B")
        
obj = B()
obj.myfun()

# Abstraction

"""
from abc import ABC , abstractmethod
class abs_example(ABC):
    @abstractmethod
    def document(self):
        print("I am service1")
    def service2(self):
        print("I am service2")
    def service3(self):
        print("I am service3")
    
class myclass(abs_example):
    def document():
        pass
    def welcome(self):
        print("Welcome")

obj = myclass()
obj.welcome()
obj.service2()

