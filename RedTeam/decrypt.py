import os

#Fernet is a encrytption method
from cryptography.fernet import Fernet


#find the files

files = []
#[] is an empty list

#add files to the list
for file in os.listdir():
    if file == "Ranasomeware.py" or file == "TheKey.key" or file == "decrypt.py" or file == "Guiransome.py" or file == "hacker.png" or file == "Guidecrtpy.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("TheKey.key", "rb") as key:
    secretkey = key.read()


# Open file and  read, use key to decrypt, write back to file
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)

import Guidecrtpy

