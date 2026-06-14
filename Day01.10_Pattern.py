"""
    *
   * *
  *   *
 *     *
*********

for i in range(1,6):
    for s in range(5,i,-1):
        print(" ",end="")
    for j in range(1,2*i):
        if j==1 or j==(2*i-1) or i==5:
            print("*",end="") 
        else:
            print(" ",end="")
    print()



*****
*****
*****
*****
*****


for i in range(1,6):
    print("*"*5)


*
**
***
****
*****

for i in range(1,6):
    print("*"*i)

1
22
333
4444
55555

for i in range(1,6):
    print(str(i)*i)

1
12
123
1234
12345

st = ""
for i in range(1,6):
    st = st+str(i)  
    print(st)

    *
   **
  ***
 ****
*****

for i in range(1,6):
    print(" "*(5-i),"*"*i)


A
BB
CCC
DDDD
EEEEE

for i in range(1,6):
    print(chr(i+64)*i)

A
AB
ABC
ABCD
ABCDE

st = ""
for i in range(1,6):
    st = st +chr(i+64)
    print(st)


break , continue , pass , else

# break:- it will take exit from the current loop
for i in range(1,6):
    if i==3:
        break
    print(i)


# break:- it will take exit from the current loop
for i in range(1,6):
    print(i)
    if i==3:
        break


# continue :- Continue take the cursor to the next itteration
# continue will skip the upcoming code
for i in range(1,6):
    if i==3:
        continue
    print(i)



# continue :- Continue take the cursor to the next itteration
# continue will skip the upcoming code
for i in range(1,6):
    print(i)
    if i==3:
        continue

# pass :- pass do nothing
# pass :- just pass the cursor to the next line
for i in range(1,6):
    if i==3:
        pass
    print(i)


# pass :- pass do nothing
# pass :- just pass the cursor to the next line
if 10>5:
    pass

print("Hello")
# here we are using pass to complete the indentation


else
for i in range(1,7):
    print(i)
else:
    print(0)


for i in range(1,7):
    if i==4:
        break
    print(i)
else:
    print(0)


else will not work if loop will "break"

i = 1
while i<=5:
    print(i)
    i=i+1
    if i==4:
        break
else:
    print(0)



i = 1
while i<=5:
    print(i)
    if i==3:
        continue
    i=i+1
else:
    print(0)



i = 1
while i<=5:
    print(i)
    if i==3:
        pass
    i=i+1
else:
    print(0)



"""