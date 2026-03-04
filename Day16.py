"""
A. Python IF (Single Condition)

1. Write a Python program to check if a number is positive. 

num = int(input("Enter the Number: "))
if(num <0):
    print("Number is Negative")
else:
    if(num==0):
        print("0 is a Neutral Number")
    else:
        print("Number is Positive")

2. Print "Eligible to vote" if age is 18 or above. 
age = int(input("Enter the Age: "))
if(age>=18):
    print("Eligible to Vote")
else:
    print("Not Eligible")

3. Check if a number is divisible by 7. 
num = int(input("Enter the Number: "))
if(num%7==0):
    print("Divisible")
else:
    print("Not Divisible")

4. Print "Pass" if marks are greater than 40. 
marks = int(input("Enter the Marks: "))
if(marks>40):
    print("Pass")
else:
    print("Fail")

5. Check if a number is greater than 100. 
num = int(input("Enter the Number: "))
if(num>100):
    print("Greater than 100")
else:
    print("Less than 100")

6. Display a message if temperature exceeds 45°C. 
temp = int(input("Enter the Temperature: "))
if(temp>100):
    print("Alert! Temperature is exceeds 45 °C")
else:
    print("Normal")

7. Check if a string length is more than 8 characters. 
str = input("Enter the String: ")
if(len(str) >8):
    print("More than 8 characters")
else:
    print("less than 8 characters")

8. Print "Logged In" if password matches "admin123". 
password = input("Enter the Password: ")
if(password =="admin123"):
    print("Logged In")
else:
    print("Wrong Password!")

9. Check if a number is a multiple of 10. 
num = int(input("Enter the Number: "))
if(num%10==0):
    print("It is Multiple of 10")
else:
    print("Not a Multiple of 10")

10. Print a warning if balance is below minimum limit. 
balance = int(input("Enter the Balance: "))
if(balance<1000):
    print("Warning! Low Balance...")
else:
    print(balance)

B. Python IF–ELSE (Two Conditions) 

11. Check whether a number is even or odd. 

num = int(input("Enter the Number: "))
if(num%2 ==0):
    print(num," is a Even Number")
else:
    print(num," is a Odd Number")

12. Find the largest of two numbers.

num1 = int(input("Enter the Number1: "))
num2 = int(input("Enter the Number2: "))
if(num1>=num2):
    if(num1==num2):
        print("both are equal")
    else:
        print(num1,"is a greater than",num2)
else:
    print(num2,"is greater than",num1)


13. Check whether a person is eligible for driving license. 

age = int(input("Enter the Age: "))
if(age >= 18):
    print(age,"person is eligible for driving license")
else:
    print(age,"person is not eligible for driving license")

14. Print "Pass" or "Fail" based on marks. 

marks = int(input("Enter your marks: "))
if marks >= 30:
    print("Pass")
else:
    print("Fail")

15. Check whether a number is positive or negative.

num = int(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive Number")
else:
    print("Negative Number")


16. Check whether a character is a vowel or consonant. 
char = input("Enter the Character: ")
if(char.upper() in "AEIOU"):
    print("Vowels")
else:
    print("Constant")

17. Check if a year is leap or not.
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

18. Print "Valid Password" or "Invalid Password". 
password = input("Enter your password: ")
if len(password) >= 8:
    print("Valid Password")
else:
    print("Invalid Password")

19. Determine whether salary is taxable or not. 
salary = float(input("Enter your salary: "))
if salary > 25000:
    print("Taxable")
else:
    print("Not Taxable")

20. Check whether a number is greater than 50 or not. 
num = int(input("Enter a number: "))
if num > 50:
    print("Number is greater than 50")
else:
    print("Number is not greater than 50")

21. Find the largest of three numbers. 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b:
    if a > c:
        print("Largest is", a)
    else:
        print("Largest is", c)
else:
    if b > c:
        print("Largest is", b)
    else:
        print("Largest is", c)

22. Check whether a number is positive, negative, or zero. 
num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")

23. Assign grades: 
● A → marks ≥ 90 
● B → marks ≥ 75 
● C → marks ≥ 60 
● Fail → below 60

marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
else:
    if marks >= 75:
        print("Grade B")
    else:
        if marks >= 60:
            print("Grade C")
        else:
            print("Fail")

24. Check whether a triangle is equilateral, isosceles, or scalene. 
a = int(input("Enter side1: "))
b = int(input("Enter side2: "))
c = int(input("Enter side3: "))
if a == b:
    if b == c:
        print("Equilateral")
    else:
        print("Isosceles")
else:
    if a == c or b == c:
        print("Isosceles")
    else:
        print("Scalene") 

25. Check whether a character is uppercase, lowercase, digit, or special character.
ch = input("Enter a character: ")
if ch.isalpha():
    if ch.isupper():
        print("Uppercase")
    else:
        print("Lowercase")
else:
    if ch.isdigit():
        print("Digit")
    else:
        print("Special Character")


26. Calculate electricity bill using slab-wise rates.
not  solved

27. Validate login using username and password. 
username = input("Enter username: ")
password = input("Enter password: ")
if username == "akash":
    if password == "1234":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")

28. Check student result using marks of 3 subjects. 
m1 = int(input("Enter marks1: "))
m2 = int(input("Enter marks2: "))
m3 = int(input("Enter marks3: "))
if m1 >= 40 and m2 >= 40 and m3 >= 40:
    total = m1 + m2 + m3
    avg = total / 3
    print("Pass")
    print("Average:", avg)
else:
    print("Fail")

29. Find the second largest number among three numbers. 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a < c:
        print("Second Largest:", a)
    elif b > c:
        print("Second Largest:", b)
    else:
        print("Second Largest:", c)
else:
    if b < c:
        print("Second Largest:", b)
    elif a > c:
        print("Second Largest:", a)
    else:
        print("Second Largest:", c)

30. Check loan eligibility using age, salary, and credit score. 

age = int(input("Enter age: "))
salary = int(input("Enter salary: "))
credit = int(input("Enter credit score: "))

if age >= 21:
    if salary >= 25000:
        if credit >= 700:
            print("Loan Approved")
        else:
            print("Low Credit Score")
    else:
        print("Low Salary")
else:
    print("Underage - Not Eligible")

D. Python ELIF (Multiple Conditions)

31. Print day name using day number (1–7).
day = int(input("Enter day number (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid Day Number")


32. Print month name using month number.
month = int(input("Enter month number (1-12): "))

if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Invalid Month")

    
33. Display grade based on percentage.
per = float(input("Enter percentage: "))

if per >= 90:
    print("Grade A")
elif per >= 75:
    print("Grade B")
elif per >= 60:
    print("Grade C")
elif per >= 40:
    print("Grade D")
else:
    print("Fail")


34. Display bonus percentage based on experience years.
exp = int(input("Enter years of experience: "))

if exp >= 10:
    print("Bonus 20%")
elif exp >= 5:
    print("Bonus 10%")
elif exp >= 2:
    print("Bonus 5%")
else:
    print("No Bonus")

    
35. Identify traffic signal meaning.
color = input("Enter signal color: ").lower()

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Ready")
elif color == "green":
    print("Go")
else:
    print("Invalid Signal")

    
36. Categorize temperature as Cold / Warm / Hot.
temp = int(input("Enter temperature: "))

if temp <= 15:
    print("Cold")
elif temp <= 30:
    print("Warm")
else:
    print("Hot")
37. Categorize employee based on salary range.
salary = int(input("Enter salary: "))

if salary >= 100000:
    print("High Level")
elif salary >= 50000:
    print("Mid Level")
elif salary >= 20000:
    print("Junior Level")
else:
    print("Entry Level")
38. Print discount percentage based on purchase amount.
amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    print("20% Discount")
elif amount >= 3000:
    print("15% Discount")
elif amount >= 1000:
    print("10% Discount")
else:
    print("No Discount")
    
39. Identify number type: single-digit / double-digit / multi-digit.
num = int(input("Enter a number: "))

if -9 <= num <= 9:
    print("Single Digit")
elif -99 <= num <= 99:
    print("Double Digit")
else:
    print("Multi Digit")
    
40. Assign performance rating: Poor / Average / Good / Excellent.
score = int(input("Enter performance score (0-100): "))

if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Good")
elif score >= 50:
    print("Average")
else:
    print("Poor")

E. Python COMPLEX CONDITIONS (AND / OR / NOT)

41. Check whether a number is divisible by 5 and 11.
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both")

42. Check if a person is eligible for loan: 
● age ≥ 21 
● salary ≥ 25,000 
● credit score ≥ 700

age = int(input("Enter age: "))
salary = int(input("Enter salary: "))
credit = int(input("Enter credit score: "))

if age >= 21 and salary >= 25000 and credit >= 700:
    print("Loan Approved")
else:
    print("Loan Not Approved")

43. Validate login using username AND password.
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")

44. Check student pass condition: 
● All subjects ≥ 40 
● Average ≥ 50

m1 = int(input("Enter marks1: "))
m2 = int(input("Enter marks2: "))
m3 = int(input("Enter marks3: "))

average = (m1 + m2 + m3) / 3

if m1 >= 40 and m2 >= 40 and m3 >= 40 and average >= 50:
    print("Pass")
else:
    print("Fail")
45. Check if a number lies between 10 and 100.
num = int(input("Enter a number: "))

if 10 <= num <= 100:
    print("Number lies between 10 and 100")
else:
    print("Number does not lie in range")

46. Check exam eligibility: 
● attendance ≥ 75% OR 
● medical certificate available

attendance = int(input("Enter attendance percentage: "))
medical = input("Medical certificate available? (yes/no): ").lower()

if attendance >= 75 or medical == "yes":
    print("Eligible for exam")
else:
    print("Not Eligible")

47. Validate a date using conditions.
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if 1 <= month <= 12 and 1 <= day <= 31 and year > 0:
    print("Valid Date (Basic Check)")
else:
    print("Invalid Date")

48. Check whether an email format is valid.
not solved


49. Determine insurance eligibility using age, health status, and income.
age = int(input("Enter age: "))
health = input("Health status (good/bad): ").lower()
income = int(input("Enter income: "))

if 18 <= age <= 60 and health == "good" and income >= 20000:
    print("Eligible for Insurance")
else:
    print("Not Eligible")

50. Check leap year using complete leap year logic.
year = int(input("Enter year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

F. INTERVIEW-LEVEL PYTHON LOGIC QUESTIONS

51. Write a Python program to calculate income tax using slabs.
income = float(input("Enter annual income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = (250000 * 0.05) + (income - 500000) * 0.20
else:
    tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30

print("Total Tax:", tax)


52. Create an ATM withdrawal program with balance checks.
balance = 10000
pin = 1234

entered_pin = int(input("Enter PIN: "))

if entered_pin == pin:
    amount = float(input("Enter withdrawal amount: "))
    if amount <= balance:
        balance -= amount
        print("Withdrawal Successful")
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance")
else:
    print("Incorrect PIN")
    

53. Check promotion eligibility using experience and performance.
exp = int(input("Enter experience: "))
rating = int(input("Enter performance rating (1-10): "))

if exp >= 5 and rating >= 8:
    print("Eligible for Promotion")
else:
    print("Not Eligible")

    

54. Implement a grading system using nested if–else.
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
else:
    if marks >= 75:
        print("Grade B")
    else:
        if marks >= 60:
            print("Grade C")
        else:
            print("Fail")

55. Validate strong password using multiple conditions.
not solved

56. Calculate delivery charges based on location and order amount.
amount = float(input("Enter order amount: "))
location = input("Enter location (city/outside): ").lower()

if location == "city":
    if amount >= 500:
        print("Free Delivery")
    else:
        print("Delivery Charge: ₹30")
else:
    print("Delivery Charge: ₹50")

57. Determine online exam qualification.
attendance = int(input("Enter attendance %: "))
dues = input("Any dues? (yes/no): ").lower()

if attendance >= 75 and dues == "no":
    print("Eligible for Online Exam")
else:
    print("Not Eligible")

58. Create movie ticket pricing logic based on age & show time.
age = int(input("Enter age: "))
show = input("Show time (day/night): ").lower()

if age < 12:
    price = 100
elif age > 60:
    price = 150
else:
    price = 200

if show == "night":
    price += 50

print("Ticket Price:", price)

59. Determine bank account type based on balance.
balance = float(input("Enter balance: "))

if balance >= 100000:
    print("Premium Account")
elif balance >= 50000:
    print("Gold Account")
elif balance >= 10000:
    print("Savings Account")
else:
    print("Basic Account")

60. Create a menu-driven program using if–elif–else.
not solved


    
"""











































    
