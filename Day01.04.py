"""
4. Membership Operator (Check Existance)
    in , not in        (Boolean Answer)

a = "aman"
b = "amankumar"
print( a in b )
print( 'ankum' in b )
print( 'ka' in b )
print( 'ka' not in b )


5. Identity Operator  (Chect Exact Match)
    is , is not       (Boolean Answer)

a = "aman"
b = 'amankumar'
c = 'aman'
print( a is b )
print( a is c )   # check memory
print( a==c )     # check

a = [1,2,3]
b = [1,2,3]
print( a is b )  # different memory (Object)
print( a == b )  # check data


6. Logical Operator
    and , or , not
and:- if both/all inputs are True, Then result is True
    otherwise False
print( 10>5 and 20>9 ) 
print( 10>5 and 20>90 ) 
print( 10>50 and 20>90 )

or:- if both/all inputs are False, Then result is False
    otherwise True
print( 10>5 or 20>9 ) 
print( 10>5 or 20>90 ) 
print( 10>50 or 20>90 )


not:- not is also called the inverter gate
it works on only one input and
if input is True, output will be False and vice-versa

print( not 10>5 )
print( not False )


# 0 , 1 => low Signal , High Signal => False , True

print( int(True) )   # 1
print( int(False) )  # 0


print( bool(False) )  # False
print( bool(0) )      # False
print( bool() )       # False
print( bool(None) )   # False
print( bool(1) )      # All are True
print( bool('Aman') )
print( bool(3874) )
print( bool(-374.5467) )
print( bool('A') )


print( True + True * False )
# 1 + 1*0
# 1 + 0
# 1


print( 10>5 + 20>30 )
# 10>5+20>30
# 10>25>30
# 10>25 and 25>30
# False and False
# False


print( (10>5) + (20>30) )
# True + False
# 1 + 0
# 1


    and , or , not

a = 7
b = 5
print( a and b )
print( b and a )
# Last value will be answer if there is no zero
a = 7
b = 0
print( a and b )   # 0
print( b and a )   # 0


a = 7
b = 5
print( a or b )  # 7
print( b or a )  # 5
# first value will be answer always if there is no zero
a = 7
b = 0
print( a or b )   # 7
print( b or a )   # 7


not
print( not 0 )
print( not None )
print( not 5 )


7. Bitwise Operator
    and -> &
    or  -> |
    not -> ~

a = 21
b = 28
print( a & b )  # 20
print( a | b )  # 29

~  (not)
        -(x+1)

x = -4
print( ~x )

"""
