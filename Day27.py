"""
File Handling
It is use to handle a file
Types of file
    - Text File (.txt , .docx , .xlsx etc)
    - Binary File ( .dat , .bin etc ) (data stored in encoded form)

Text File

file_handler = open( 'file_name.extension' , 'mode' )
mode =>  r , w , a , r+ (rw) , w+ (wr) , a+ (ar) 

file = open( 'student.txt' , 'w' )
file.close()


# WAP to write data into a file
file = open( 'student.txt' , 'a' )
file.write("\nShiva Yadav")
file.close()


file = open( 'student.txt' , 'a' )
file.writelines("Abhishek Chauhan")
file.close()

# write and writelines are same
# write can write only one string at a time
and writeline can add a collection or multiple strings


# WAP to read a file
file = open( 'student.txt' , 'r' )
data = file.read()    # read complete file
print(data)
file.close()



file = open( 'student.txt' , 'r' )
data = file.read(10)   # read only 10 characters
print(data)
file.close()


file = open( 'student.txt' , 'r' )
data = file.readline()   # read only one line
print(data)
data = file.readline()
print(data)
file.close()



file = open( 'student.txt' , 'r' )
for i in range(5):
    data = file.readline()
    print(data,end="")
file.close()


file = open( 'student.txt' , 'r' )
while True:
    data = file.readline()
    print(data,end="")
    if len(data)==0:
        break
file.close()


file = open( 'student.txt' , 'r' )
data = file.readline(10)  #  read only 10 characters from 1st line only
print(data,end="")
file.close()



file = open( 'student.txt' , 'r' )
data = file.readlines()  #  read all lines from file and hold in a list
print(data,end="")
file.close()


file = open( 'student.txt' , 'r' )
data = file.readlines()  
for line in data:
    print(line)
file.close()


file = open( 'student.txt' , 'r' )
data = file.readlines(30)  
print(data)
file.close()



file = open( 'student.txt' , 'r' )
print(file.tell())  # tell will tell you the current position of the cursor
data = file.read()  
print(data)
print(file.tell())
file.close()


file = open( 'student.txt' , 'r' )
print(file.tell())
data = file.read(20)  
print(data)
print(file.tell())
file.close()


file = open( 'student.txt' , 'r' )
print(file.tell())
file.seek(10)  #  it will skip 10 characters
data = file.read(10)
print(data)
print(file.tell())
file.close()
    
"""
