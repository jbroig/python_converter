import string
import re
import platform
import os
import time

original_file = open("origen.csv", "r")
new_file = open("new_csv.csv","w")


def converter():
    for row in original_file:

        original_row = re.sub(r',','.', row)
        modified_row = re.sub(r';',',', original_row)
        new_file.write(modified_row)

def file_dates(path_to_csv, path_to_converter ):
    if platform.system() == 'Windows':
        
	    csv_modification_date = time.ctime(os.path.getmtime(path_to_csv))
        converter_modification_date = time.ctime(os.path.getmtime(path_to_converter))

        if (csv_modification_date != converter_modification_date):
            print("Executing...")
            converter()

        print("Last csv modification: %s" % csv_modification_date)
        print("Last converter modification: %s" % converter_modification_date)




file_dates(r'C:\\Users\Administrador\\Desktop\\python_converter\\new_csv.csv','C:\\Users\\Administrador\\Desktop\\python_converter\\converter.py')
