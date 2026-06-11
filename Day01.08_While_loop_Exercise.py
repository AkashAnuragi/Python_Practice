'''
Python While Loop Exercise 
Part 1 – Basic Level 
1. Print numbers from 1 to 10 using a while loop.
n =1
while n <=10 :
    print(n)
    n+=1
    

2. Print even numbers from 1 to 20. 
n =1
while n <=20 :
    if n%2==0:
        print(n)
    n+=1
   
3. Print odd numbers from 1 to 20. 
n =1
while n <=20 :
    if n%2!=0:
        print(n)
    n+=1
   
4. Print numbers from 10 to 1 (reverse order). 
 
n =10
while n >=1 :
    print(n)
    n-=1
    
5. Print multiplication table of 5 using while loop. 

n=1
num = int(input("Enter the Number: "))
while n <=10:
    print(num,"*",n,"=",n*num)
    n+=1


Part 2 – Intermediate Level 
6. Find the sum of first 10 natural numbers using while loop. 
7. Find factorial of a number entered by user. 
8. Count number of digits in a given number. 
9. Reverse a number using while loop. 
10. Check whether a number is palindrome or not using while loop.

Part 3 – Pattern Based 
11. Print pattern: 
* 
** 
*** 
**** 
*****

n=1
while n<=5:
    print("*"*n)
    n+=1


12. Print pattern: 
1 
12 
123 
1234 
12345


n=1
num=""
while n<=5:
    num =num+str(n)
    print(num)
    n+=1

Part 4 – Logical / Real Scenario 
13. Ask user to enter password until correct password is entered. 
valid_pass = "Akash123"
password = input("Enter your password: ")

while valid_pass != password:
    print("Invalid Password! Try again")

    password = input("Enter your Password: ")

print("Loggin Successfully...")



# Or

valid_pass = "Akash123"

while True:
    password = input("Enter Your Password: ")
    if(valid_pass == password):
        print("Loggin Successfully")
        break
    else:
        print("Invalid Password")

14. Create a number guessing game: 
• Generate a random number (1–10) 
• Keep asking user until they guess correctly 
15. Keep taking input numbers until user enters 0, then print total sum.
'''





















