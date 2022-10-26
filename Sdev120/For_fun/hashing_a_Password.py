from getpass import getpass
from hashlib import md5

'''
password = getpass("Enter your password:")
print(password)
encoded = password.encode("UTF-8")
print(encoded)
hashed = md5(encoded)
print(hashed)
hexed = hashed.hexdigest()
print(hexed)
'''

#password = md5(getpass("Enter your password: ").encode("UTF-8")).hexdigest()
#print(password)

def passwd(prompt="Enter your password: "):
    return md5(getpass(prompt).encode("UTF-8")).hexdigest()

pass1 = passwd()
pass2 = passwd("Confirm your password: ")
if pass1 == pass2:
    print(f"{pass1}\n{pass2}")
else:
    print("The passwords did not match")
