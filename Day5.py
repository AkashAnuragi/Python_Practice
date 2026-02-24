"""
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

"""




