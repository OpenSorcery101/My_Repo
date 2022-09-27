import time
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
print("The screen will clear in \n3", end='', flush = True)
time.sleep(1)
print("\n2", end='', flush=True)
time.sleep(1)
print("\n1")
time.sleep(1)
clear()