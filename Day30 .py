"""
Python + MySql

important library
 pip install mysql.connector
 pip install mysql.connector.python
 
"""


#---------- Build MySQL Connection and  Cursor -------
import  mysql.connector
conn= mysql.connector.connect(
    host = '127.0.0.1', #localhost
    port = 3306,
    user = 'root',
    password = '12345',
    database = 'croma'
    )

curr = conn.cursor()
# -----------------------------------------------------

"""
# WAP to create Database
query = "create Database croma"

curr.execute(query)


# WAP to create Table


q = "use Croma"

curr.execute(q)

query = '''
Create table school(
sid  INT,
sname TEXT,
sadd TEXT,
scourse TEXT
)
'''

curr.execute(query)

#WAP to to insert Value in table

query = 'Insert into school values(101,"Akash", "Noida", "Data Science")'
curr.execute(query)
print(curr.rowcount)
conn.commit()


sid = input("Enter Student ID: ")
sname = input("Enter Student Name: ")
sadd = input("Enter Student Address: ")
scourse = input("Enter Student Course: ")

query = f'Insert into school values({sid},"{sname}", "{sadd}","{scourse}")'
try:
    curr.execute(query)
    if curr.rowcount > 0:
        print("Studnet Recorded Successfully")
    else:
        print("Studnet Recording failed!")
except:
    print("Student Recording failed!")
conn.commit();


sid = input("Enter Student ID : ")
sname = input("Enter Student Name : ")
sadd = input("Enter Student Address : ")
scourse = input("Enter Student Course : ")
data = (sid,sname,sadd,scourse)
query = 'insert into school value(%s,%s,%s,%s)'
curr.execute(query,data)
if curr.rowcount>0:
    print("Student Recorded Successfully!")
else:
    print("Student Recording Failed!")
conn.commit()

"""




# WAP to read data from database

query = "SELECT * FROM school"
curr.execute(query)
print("SID\tSNAME\t\tSADD\tSCOURSE\n")
for stu in curr.fetchall():
    print(stu[0],'\t',stu[1],'\t',stu[2],'\t',stu[3])




