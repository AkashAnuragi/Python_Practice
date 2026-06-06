'''

PART 1 – Basic For Loop Questions

Q1. Print Numbers : Use a for loop to print numbers from 1 to 10.
for i in range(1,11):
    print(i)


Q2. Print Even Numbers : Print all even numbers between 1 and 20.
for i in range(2,21,2):
    print(i)


# OR

for i in range(1,21):
    if(i%2==0):
        print(i)


Q3. Find Sum : Print the sum of numbers from 1 to 10 using a for loop. 
sum =0
for i in range(1,11): 
    sum +=i; # 1+2+3+4+5+6+7+8+9+10=55
print(sum)
    
Q4. Multiplication Table : Take a number from the user and print its multiplication table up to 10.

num = int(input("Enter a Number: "))

for i in range(1,11):
    print(num,"*",i,"=",num*i)

Q5. Count Characters : Take a string and count the total number of characters using a for loop.
str = input("Enter a String: ")
count =0
for char in str:
    count +=1
print("Total Number of character: ",count)



PART 2 – Break Related Questions 

Q6. Stop at 5 
Print numbers from 1 to 10. 
Stop the loop when the number becomes 5.

for i in range(1,11):
    if(i==5):
        break
    print(i)

Q7. Search in List 
Search for number 25 in a list. 
If found, print "Found" and stop the loop.
li = [1,3,4,25,123,43]
for i in  li:
    if i ==25:
        print("Found")
        break
else:
    print("Not Found")


Q8. First Negative Number 
Given a list of numbers, print the first negative number and stop the loop.
li = [1,2,-354,45,-23,12]

for i in li:
    if i < 0:
        print("First Negative Number:",i)
        break



PART 3 – Continue Related Questions
Q9. Skip 5 
Print numbers from 1 to 10. 
Skip number 5.

for i in range(1,11):
    if i ==5:
        continue
    else:
        print(i)
        

Q10. Skip Even Numbers 
Print numbers from 1 to 20. 
Skip all even numbers.

for i in range(1,21):
    if i%2 ==0:
        continue
    else:
        print(i)


Q11. Skip Letter 
Print each character of the string "PYTHON". 
Skip the letter "O".

str = "PYTHON"

for char in str:

    if char =="O":
        continue
    else:
        print(char)


PART 4 – Pass Related Questions 
Q12. Empty Loop 
Run a loop from 1 to 5 but do nothing inside the loop using pass.

for i in range(1,6):
    pass

    
Q13. Skip Using Pass 
Loop from 1 to 10. 
If number is 6, just use pass.
for i in range(1,11):
    if i ==6:
        pass
    else:
        print(i)

PART 5 – For-Else Questions 
(Remember: else runs only if the loop is not stopped by break.)
# this loop run Normally
for i in range(1,11):
        print(i)
else:
    print("Loop finised Successfully")
 # Or

 # If the loop stops because of break, then else will not run.
for i in range(1,11):
    if(i==5):
        break
    print(i)
else:
    print("Loop finised Successfully")
        
Q14. Search Number Using for-else 
Search for number 100 in a list. 
If found, print "Found". 
If not found, print "Not Found".

li = [121,13,1234,12,100]
num = int(input("Enter the Number: "))
for i in li:
    if i==num:
        print("Found")
        break
else:
    print("Not Found")


Q15. Prime Number Check 
Take a number from the user and check whether it is prime using for-else.

num = int(input("Enter the Number:"))
for i in range(2,num):
    if num%i ==0:
        print("Not Prime")
        break
else:
    print("Prime Number")

PART 6 – Pattern Questions 
Q16. Star Pattern 
Print: 
* 
** 
*** 
**** 
*****

for i in range(1,6):
    print("*"*i)
print()

Q17. Reverse Star Pattern 
Print: 
***** 
**** 
*** 
** 
*
for i in range(5,0,-1):
    print("*"*i)
print()

Q18. Number Pattern 
Print: 
1 
12 
123 
1234 
12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

# OR

l=''

for i in range(1,6):
    print(l+ str(i))
    l = l + str(i)


Q19. Same Number Pattern 
Print: 
1 
22 
333 
4444 
55555

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()

# OR

for i in range(1,6):
    print(str(i)*i)
    


Q20. Pyramid Pattern 
Print: 
        * 
       *** 
      ***** 
     ******* 
    ********* 
for i in range(1,6):
    for k in range(6-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()
# OR

for i in range(1,6):
    print(" "*(6-i)+"*"*(2*i-1))


Q21. Inverted Pyramid 
Print: 
 ********* 
  *******
   ***** 
    *** 
     * 
for i in range(5):

    for j in range(i):
        print(" ", end="")

    for k in range(9 - 2 * i):
        print("*", end="")

    print()

   #OR
   
for i in range(5):
    print(" "*(i)+"*"*(9-2*i))\

Bonus Question 
Q22. Break in Pattern

for i in range(1, 6):
    if i == 4:
        break
    print("*" * i)

    
     *
    ***
   *****
  *******
 *********
  *******
   *****
    ***
     *
      
'''



''' 
for i in range(1,6):
    for k in range(6-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()
for i in range(5):
    for k in range(i+2):
        print(" ",end="")
    for j in range(7-2*i):
        print("*",end="")
    print()
'''


