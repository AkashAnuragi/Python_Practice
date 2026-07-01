"""
File Handling:- To write/read data from a file
Two types
1- Text File (.xlsx , .txt , .csv etc)
2- Binary File  (.bin , .dat etc)

file_handler = open('file_name.extension','mode')
mode:- r , w , a , r+ , w+ , a+

TEXT FILE

file = open('student.txt','w')
file.close()


# WAP to write data in a file

# w mode - erase old data
file = open('student.txt','w')
file.write("Hello World")
file.close()


file = open('student.txt','a')
file.write("\nMohit Agarwal")
file.close()
# using write method you can write only one data point


# To write multiple data points

names = ['\nAnu','\nManu','\nYogesh']
file = open('student.txt','a')
file.writelines(names)
file.close()



# To read data from a text file

file = open('student.txt','r')
data = file.read()    # read all data from a file
print(data)
file.close()


file = open('student.txt','r')
data = file.read(20)   # read only 20 characters
print(data)
file.close()


file = open('student.txt','r')
data = file.readline()  # Read only one line
print(data)
file.close()


file = open('student.txt','r')
data = file.readline()  # Read first line
print(data)
data = file.readline()  # Read second line
print(data)
data = file.readline()  # Read third line
print(data)
file.close()


file = open('student.txt','r')
data = file.readlines()  # read all lines in a list
print(data)
file.close()


file = open('student.txt','r')
data = file.readlines()
for names in data:
    print(names)
file.close()



file = open('student.txt','r')
data = file.readlines(25)
print(data)
file.close()



"""


file = open('student.txt','r')
data = file.readlines(25)
print(data)
file.close()