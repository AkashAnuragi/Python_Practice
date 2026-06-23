
'''
String:-
String is a Collection of Characters
String is behave like tuple

string_name = "characters"
st.lower() 
print(st.capitalize())
print(st.trim)= "Akash"

st = "Akash"
st = str(123)
st = "!@#$%^&*(r758973492)"
st =""
print(st)
print(type(st))

String works on INDEX

STRING can be Sliced
st = "AkashAnuragi"
print(st[3])
print(st[2:7])

STRING can be replicates

st = "AkashAnuragi"
print(st*3)

STRING supports traversing/itratoion
st = "AkashAnuragi"
for i in st:
    print(i)

Built-in-function
max, min, len

String works on ASCII value
A = 65 , B = 66 --- Z = 90
a = 97 , b = 98 --- z = 122


st = "AkashAnuragi"
print(max(st))
print(min(st))
print(len(st))

String's Method 
upper, lower, capitalize,title, strip,lstrip,rstrip


st = "   Akash Anuragi   "
print(st.upper())
print(st.lower())
print(st.title()) # capitalize first character of 1st latter
print(st.capitalize())
print(st.strip())   # the strip() method removes any whitespace from the beginning or the end: 
print(len(st.strip()))
print(st.lstrip())
print(st.rstrip()) 


replace, split
st = "I am Akash Anuragi"
print(st)
print(st.replace("Akash", "Sagar"))

st= "I@am@Akash@Anuragi"
print(st.split('@'))

find,index,count


st = "pythonprogramming"
print(st)
print(st.count('p')) # will count p
print(st.find('o'))
print(st.find('o',5))
print(st.find('program'))
print(st.index('o'))
print(st.find("akash")) # return -1 if not found
print(st.index('sa')) # it return Error if not found



JOIN

st = ['I','Love','India']
print(st)
print(''.join(st))
print(' '.join(st))
print('$'.join(st))

st = 'Honesty is the best policy'

print(st.split('is')) #['Honesty ', ' the best policy']

CHECKING STRING CONTENT
isaplha, isdigit, isalnum, islower, isupper

s = 'akash'
print(s.isalpha())
s ='akash543'
print(s.isalpha())

s='123'
print(s.isdigit())
s='123'
print(s.isalnum())
s='akash'
print(s.isalnum())
s= 'akash@1234'
print(s.isalnum())
s= 'akash'
print(s.islower())
print(s.isupper())


#WAP to convert into uppercase all first characters of words of a sentence.

s = 'sagar is my Younger Brother'
st = ""

for i in s.split():
    st = st+i.capitalize()+" "
print(st)




s = 'akash'
st = ""
print(s)
for ch in s:
    st = st+chr(ord(ch)-32)
print(st)


# WAP to convert a word into toggle case
s= 'AKashANURAgi'  
str= ""
flag = 0
for ch in s:
    if flag ==0:
        str = str+ch.lower()
        flag =1
    else:
        str =str+ch.upper()
print(str)

'''
def f(**a):
    print(a)
f(name="akash")