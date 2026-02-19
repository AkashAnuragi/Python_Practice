"""
hello = 200
print("hello akash", hello)

# 2+2=4 Addition
#2+2=22 Concatination
#when we use input it work a concatination it takes all the input like a string. for doing a addition we need int syntax for example
a = input("Enter A number: " )   
b = input("Enter B number: ")
c = a+ b;
print(c)


# it give inter value(non decimal value) if you need a decimal value you  can use float keyword
a = int(input("Enter A number: " )) 
b = int(input("Enter B number: "))
c = a+ b;
print(c)


a = float(input("Enter A number: " )) 
b = float(input("Enter B number: "))
c = a+ b;
print(c)

WAP to calculate the gross salary of employee where HRA is 20% and DA is 30% of his basic salary.
HINT: Gross_Salary = Basic_Salary + HRA +DA

bs = float(input("Enter the Employee Basic Salary: "))
HRA = bs*20/100 
DA = bs*30/100 
Gross_Salary = bs + HRA + DA
print(Gross_Salary)

WAP to calculate the cube of the user input
N = float(input("Enter the number: "))
print("Cube of user Input is :", N**3)

WAP to calculate the Area of Circle


"""
radius = float(input("Enter the Radius of Circle: "))
Area = 3.14*radius*radius
print("Area of Circle are: ", Area)