import string
import re
import platform
import os
import time

def converter():
    original_file = open("TIAMO_EXPORT.csv", "r")
    new_file = open("TIAMO_EXPORT_UPLOAD.csv","w")
    for row in original_file:

        original_row = re.sub(r',','.', row)
        modified_row = re.sub(r';',',', original_row)
        new_file.write(modified_row)

def file_dates(path_to_csv, path_to_converter ):
    if platform.system() == 'Windows':
        csv_modification_date = time.ctime(os.path.getmtime(path_to_csv))
        converter_modification_date = time.ctime(os.path.getmtime(path_to_converter))

        csv_modification_date = csv_modification_date.split(":")      
        csv_modification_date = str(":".join(csv_modification_date[:-1]))
        
        converter_modification_date = converter_modification_date.split(":")
        converter_modification_date = str(":".join(converter_modification_date[:-1]))

        s_time = time.ctime()
        s_time = s_time.split(":")
        s_time = str(":".join(s_time[:-1]))

        print("Time: {0}".format(s_time))
        print("Last converter modification: {0}".format(converter_modification_date))

        if (s_time != converter_modification_date):
            print("Executing...")
            converter()
            
            os.system("gdrive update 1HQM1QUSSMDgE5-nZ5m2UaBaMwDWv_ZkBX8LdzHCR4Pc TIAMO_EXPORT_UPLOAD.csv")
        else:
            print("Everything is updated")    

        




file_dates('TIAMO_EXPORT.csv','TIAMO_EXPORT_UPLOAD.csv')
