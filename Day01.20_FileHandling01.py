"""
File Handling (Text , Binary)
Binary File (data stores in the form object)

file_handler = open( 'filename.extension' , 'mode' )
# mode => rb , wb ,  ab , rb+ ,  ab+ , wb+

import pickle
import joblib

dump => to write data
pickle.dump( 'data' , file_handler )
joblib.dump( 'data' , file_handler )

load => to read data
pickle.load(file_handler)
joblib.load(file_handler)


# Example
file = open('employee.bin' , 'wb')
file.close(e)


import pickle
file = open('employee.bin' , 'wb')  # erase past data and write new data
pickle.dump('Rahul Kumar Sharma' , file)
file.close()



import pickle
file = open('employee.bin' , 'ab')  # add new data with old data
pickle.dump('Renu Singh' , file)
file.close()



import pickle
file = open( 'employee.bin' , 'rb' )
data = pickle.load(file)
print(data)
file.close()



import pickle
file = open( 'employee.bin' , 'rb' )
for i in range(2):
    data = pickle.load(file)
    print(data)
file.close()



import pickle
file = open( 'employee.bin' , 'rb' )
try:
    while True:
        data = pickle.load(file)
        print(data)
except:
    print("\nData Read Successfully!")
file.close()



"""