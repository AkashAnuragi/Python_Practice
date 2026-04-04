"""
Python + MySQL

pip install mysql.connector
pip install mysql.connector.python

"""
# -------- Build MySQL Connection and Cursor --------
import mysql.connector
conn = mysql.connector.connect(
host = '127.0.0.1',      # localhost
port = 3306 ,
user = 'root' ,
password = '553655' ,
database = 'croma'
    )
cur = conn.cursor()
# ---------------------------------------------------

"""

# WAP to CREATE database
query = "CREATE DATABASE croma"
cur.execute(query)


# WAP to create a table

q = "USE croma"
cur.execute(q)
query = '''
CREATE TABLE student(
sid INT ,
sname TEXT ,
sadd TEXT ,
scourse TEXT
)
'''
cur.execute(query)


# WAP to insert a data into table
query = 'insert into student value(101,"Raj","Noida","DS")'
cur.execute(query)
print( cur.rowcount )
conn.commit()



sid = input("Enter Student ID : ")
sname = input("Enter Student Name : ")
sadd = input("Enter Student Address : ")
scourse = input("Enter Student Course : ")
query = f'insert into student value({sid},"{sname}","{sadd}","{scourse}")'
try:
    cur.execute(query)
    if cur.rowcount>0:
        print("Student Recorded Successfully!")
    else:
        print("Student Recording Failed!")
except:
    print("Student Recording Failed!")
conn.commit()


sid = input("Enter Student ID : ")
sname = input("Enter Student Name : ")
sadd = input("Enter Student Address : ")
scourse = input("Enter Student Course : ")
data = (sid,sname,sadd,scourse)
query = 'insert into student value(%s,%s,%s,%s)'
cur.execute(query,data)
if cur.rowcount>0:
    print("Student Recorded Successfully!")
else:
    print("Student Recording Failed!")
conn.commit()


# WAP to read data from database

query = "SELECT * FROM student"
cur.execute(query)
print("SID\tSNAME\tSADD\tSCOURSE\n")
for stu in cur.fetchall():
    print(stu[0],'\t',stu[1],'\t',stu[2],'\t',stu[3])

"""
