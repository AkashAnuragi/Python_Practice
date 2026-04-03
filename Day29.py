"""
Python File Handling
Binary Files ( .bin , .dat etc )

pickle module/library

import pickle
pickle.dump()    # to write data into binary files
pickle.load()    # to read data from binary files

file_handler = open( 'file_name.extension' , 'mode' )
mode:-  rb , wb , ab , rb+ , wb+ , ab+

file = open('employee.bin' , 'ab')
file.close()


# WAP to write data into a file

import pickle
file = open('employee.bin' , 'ab')
pickle.dump('Aman Kumar',file)
file.close()



import pickle
file = open('employee.bin' , 'ab')
name = input("Enter A Name : ")
pickle.dump(name,file)
file.close()



import pickle
ch = 'Y'
file = open('employee.bin' , 'ab')
while ch in "yY":
    name = input("Enter A Name : ")
    pickle.dump(name,file)
    ch = input("Do You Want To Continue(Y/n) : ")
file.close()



# WAP to read data from a file.

import pickle
file = open('employee.bin','rb')
print( pickle.load(file) )
file.close()


import pickle
file = open('employee.bin','rb')
try:
    while True:
        print( pickle.load(file) )
except:
    print("File Read Successfully!")
file.close()


# WAP to store student's information

import pickle
file = open("student.bin",'ab')
sid = input("Enter Student's ID : ")
sname = input("Enter Student's Name : ")
sadd = input("Enter Student's Address : ")
smob = input("Enter Student's Mobile : ")
pickle.dump(sid,file)
pickle.dump(sname,file)
pickle.dump(sadd,file)
pickle.dump(smob,file)
print("Student Added Successfully!")
file.close()



# WAP to read data from a file

import pickle
file = open('student.bin','rb')
try:
    while True:
        data = pickle.load(file)
        print(data)
except:
    print("\nData Read Successfully!")
file.close()



import pickle
file = open('student.bin','rb')
print("SID\tSNAME\tSADD\tSMOBILE\n")
try:
    while True:
        for i in range(4):
            data = pickle.load(file)
            print(data,end="\t")
        print()
except:
    print("\nData Read Successfully!")
file.close()



# WAP to delete a student

import pickle
import os
file1 = open('student.bin','rb')
file2 = open('temp.bin','ab')
sid = 102
try:
    while True:
        data = pickle.load(file1)
        if data == sid:
            pickle.load(file1)
            pickle.load(file1)
            pickle.load(file1)
        else:
            pickle.dump(data,file2)
except:
    print("Delete Successfully!")
file1.close()
file2.close()
os.remove('student.bin')
os.rename('temp.bin','student.bin')

"""
