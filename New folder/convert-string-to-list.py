import os

folders = input("please provide the proper paths separated by comma:").split()

for folder in folders:
    files =os.listdir(folder)
        
    for file in files:
        print (file)
