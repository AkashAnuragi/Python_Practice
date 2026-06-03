"""
7. Bitwise Operator
    and -> &
    or  -> |
    not -> ~

a = 19
b = 26
print( a & b ) # 18
print( a | b ) # 27

~  NOT
    -(x+1)
a = -8
print( ~a )

^  XOR
if inputs are same, then output is 0 , otherwise 1
0 0 - 0
0 1 - 1
1 0 - 1
1 1 - 0

a = 12
b = 5
print(a^b)
# a =>  1100
# b =>  0101
#a^b=>  1001 => 9


left shift    <<
right shift   >>

a = 19
print( a>>1 ) # => 9
print( a>>2 )  # => 4
print( a>>3 )   # => 2


a = 9
print( a<<1 )   # 18
print( a<<2 )   # 36
print( a<<3 )   # 72



a = 3
b = 2
a *= b + 1   # a *= 3  # a = a*3 => a = 9
print(a)


print(5 + True * False + (not False))
# 5 + 1*0 + 1
# 5+1
# 6


print((not 0) * (False or 1))
# True * True
# 1 * 1
# 1


x = 10
y = 20
print(x & y | x ^ y)

# x = 01010
# y = 10100
# & = 00000
# | = 11110
# ^ = 11110  => 30


Python Data Types
1- Number
    - int (integer)   54 , -56 , 0
    - float (decimal value) 345.67 , -45.67 , 5/2 , 34.0
    - complex  a+bj , 3+8j
        a = 4+8j
        print(a)
        print( a.real )
        print( a.imag )
    - binary (101001011) 0b11011
        a = 0b10011
        print(a)
    - Octal Number (01234567)  0o344 , 0o215
        a = 0o165
        print( a )
    - Hexadecimal Number (0123456789ABCDEF) 0x234 , 0x125AC
        a = 0x1FA     
        print( a )
2- String
    - 'A' , "A" , 'Aman' , "Aman" , '''AMAN''' all are string
3- Boolean
    - True , False
4- Sequence Data Type
    - List , Tuple
        a = [3,67,56]  List
        a = (34,67,89)  Tuple
5- Hash Data Type
    - Set , Dictionary
        a = {34,56,89}    Set
        a = {1:34,2:56,3:678}  Dictionary
"""
