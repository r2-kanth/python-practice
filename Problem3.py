import os
#this is the folder path where you want to list the contents.
directory_path = r"C:\Users\kanth\Desktop\Python"

contents = os.listdir(directory_path)

for item in contents:
    print(item)