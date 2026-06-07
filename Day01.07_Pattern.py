'''
    *
   ***
  *****
 *******
*********
'''

'''for i in range(1,6):
    for k in range(5-i):
        print(" ",end="")
    for j in range(0,2*i-1):
        print("*",end="")
    print()

'''
# OR
'''
for i in range(1,6):
    print(" "*(5-i)+"*"*(2*i-1))

    '''
'''
# OR
rows = 5
i = 1
while i<= 5:
    space =rows - i
    stars = 2*i-1
    print(" "*space + "*"*stars)

    i+=1
'''

'''
      A 
     A B 
    A B C 
   A B C D 
  A B C D E
'''
'''
for i in range(1,6):
    for k in range(0,6-i):
        print(" ",end="")
    for j in range(i):
        print(chr(65+j),end=" ")
    print()
'''
'''
    1
   123
  12345
 1234567
123456789
'''
'''
for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,2*i):
        print(j,end="")
    print()

'''

'''
*********
 *******
  *****
   ***
    *
'''
'''
for i in range(5,0,-1):
    for k in range(5-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()
'''

'''
1
01
010
1010
10101
'''
'''
k=1
for i in range(1,6):
    for j in range(0,i):
        print(k%2,end="")
        k+=1
    print()

'''
'''
    *    
   * *   
  *   *  
 *     * 
*********
'''
'''
for i in range(1,6):
    for s in range(5,i,-1):
        print(" ",end="")
    for j in range(1,2*i):
        if j==1 or j==(2*i-1) or i==5:
            print("*",end="") 
        else:
            print(" ",end="")
    print()
'''
'''
n=5
for i in range(1,n+1):
    for j in range(1,2*n):
        if j==n-i+1  or  j==n+i-1 or i==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()


    '''


'''
* 
* * 
* * * 
* * * * 
* * * * *
'''
'''
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()
'''
#OR 

for i in range(1,6):
    print("*",end="")
print()

'''
l=[True,False,True,False,True]
print(any(l)) #true
print(all(l))  #false
print(id(l[2]))  # For Display address 
'''

'''
li =[1,2,3,4,5,6,7]

rev=[]
for i in li:
    rev.insert(0,i)
print(rev)
    '''


'''
rev= ""
count=0
for i in l:
    #print(l[0+count])
    count +=1
#print(count)
len = count-1
for i in l:
    print(l[len],end="")
    len = len-1
'''
'''
l="AKash"
rev=""
for i in l:
    rev=i+rev
    
print(rev)
'''
'''
import sys

l = [1, 2, 3, 4, 5]
t = (1, 2, 3, 4, 5)

print(sys.getsizeof(l))
print(sys.getsizeof(t))

'''

li =[1,2,3,4,5,32435]

max = 0
min = li[0]
count =0
for  i in li:
    count +=1
    if max<i:
        max=i
    if min > i:
        min = i
print("max: ",max)
print("min ",min)
print("Total length: ",count)


# Today question- 4-6-12
'''
a =[1,2,4,5,6]
b =a 
b.append(7)
print(a)

t = (1, 2, [3, 4])
t[2].append(5)
print(t)    

a = (1, 2, 3)
b = (1, 2, 3)
print(a == b, a is b)

x = [1, 2, 3]
print(x * 2 + [0])

t = 1, 2, 3
print(type(t), t)

lst = [10, 20, 30, 40, 50]
print(lst[1:4:2])

t = (10, 20, 30, 40)
print(t[-1], t[-3])


a = [3, 1, 2]
a.sort()
print(a)
b = sorted([3,1,2])
print(b is a)

a = (5)
b = (5,)
print(type(a), type(b))

result = [x**2 for x in range(5) if x % 2 == 0]
print(result)

'''
