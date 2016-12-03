import os
dir_name = 'Variables_economicas'

for file_name in os.listdir(dir_name):
    csv_file = open('./'+dir_name+'/'+file_name,'r+')
    csv_file_string = csv_file.read();
    csv_file.truncate(0)
    csv_file.write((csv_file_string.replace(',','.')).replace(';',','))
    