"""
PART 1 – Basic For Loop Questions

Q1. Print Numbers 
Use a for loop to print numbers from 1 to 10.
for i in range(1,11):
    print(i)

Q2. Print Even Numbers 
Print all even numbers between 1 and 20.
for i in range(1,21):
    if(i%2==0):
        print(i)

Q3. Find Sum 
Print the sum of numbers from 1 to 10 using a for loop. 
sum = 0
for i in range(1,11):
    sum +=i
print("The Sum of numbers from 1 to 10 is: ",sum)

Q4. Multiplication Table 
Take a number from the user and print its multiplication table up to 10.
n = int(input("Enter the Number: "))
for i in range(1,11):
    print(n,"x",i, "=",n*i)

Q5. Count Characters 
Take a string and count the total number of characters using a for loop.
str = "Akash Anuragi"
count = 0
for i in str:
    count +=1
print("Total Count is: ",count)


For Loop Exercise
 PART 6
Q16. Star Pattern 
Print: 
* 
** 
*** 
**** 
*****

# mordern way
for i in range(1,6):
 print("*"*i)

# Traditional way
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end='')
    print()    

Q17. Reverse Star Pattern 
Print: 
***** 
**** 
*** 
** 
* 

# Traditional Way
for i in range(6,1,-1):
    for i in range(1,i):
        print("*",end="")
    print()

# Modern Way
for i in range(5,0,-1):
    print("*"*i)

Q18. Number Pattern 
Print: 
1 
12 
123 
1234 
12345

# Traditional Way 
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

# Modern Way
k=""
for i in range(1,6):
    k = k+str(i)
    print(k)

Q19. Same Number Pattern 
Print: 
1 
22 
333 
4444 
55555

# Traditional Way 
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()

# Modern Way
for i in range(1,6):
    print(str(i)*i)

Q20. Pyramid Pattern 
Print: 
     * 
    *** 
   ***** 
  ******* 
 *********
# traditional way 
for i in range(1,6):
    for k in range(i,5):
        print(" ",end="")
    for j in range(0,2*i-1):
        print("*",end="")
    print()

# Modern Way
m = 5
for i in range(1,10,2):
    print(" "*m +"*"*i)
    m -= 1

Q21. Inverted Pyramid 
Print: 
********* 
 ******* 
  ***** 
   *** 
    *


# traditional way 
for i in range(6,0,-1):
    for k in range(i,6):
        print(" ",end="")
    for j in range(0,2*i-1):
        print("*",end="")
    print()

# Modern Way
m = 0
for i in range(9,0 ,-2):
    print(" "*m +"*"*i)
    m += 1

Bonus Question 
Q22. Break in Pattern 
Print a star pattern. 
Stop printing when the row number reaches 4. 
for i in range(1,6):
    if(i==4):
        break
    print("*"*i)

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
li = [12,23,34,45,25,231,1]
for i in li:
    if(i == 25):
        print("Found")
        break

Q8. First Negative Number 
Given a list of numbers, print the first negative number and stop the loop.
"""
li = [12,23,34,-45,25,231,1]
for i in li:
    if(i < 0):
        print("Negative number is:",i)
        break









