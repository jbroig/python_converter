import string
import re
import platform
import os
import time

# original_file = open("origen.csv", "r")
# new_file = open("new_csv.csv","w")
original_file = open("a.txt", "r")
new_file = open("b.txt","w")

def converter():
    for row in original_file:

        original_row = re.sub(r',','.', row)
        modified_row = re.sub(r';',',', original_row)
        new_file.write(modified_row)

def file_dates(path_to_csv, path_to_converter ):
    if platform.system() == 'Windows':
        csv_modification_date = time.ctime(os.path.getmtime(path_to_csv))
        converter_modification_date = time.ctime(os.path.getmtime(path_to_converter))

        csv_modification_date = csv_modification_date.split(":")      
        csv_modification_date = ":".join(csv_modification_date[:-1])
        
        converter_modification_date = converter_modification_date.split(":")
        converter_modification_date = ":".join(converter_modification_date[:-1])


        if (csv_modification_date != converter_modification_date):
            print("Executing...")
            # converter()
            
            
        print("Last csv modification: %s" % csv_modification_date)
        print("Last converter modification: %s" % converter_modification_date)




# file_dates(r'C:\\Users\Administrador\\Desktop\\python_converter\\new_csv.csv','C:\\Users\\Administrador\\Desktop\\python_converter\\converter.py')
file_dates(r'C:\\Users\Administrador\\Desktop\\a.txt','C:\\Users\\Administrador\\Desktop\\b.txt')