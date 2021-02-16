''' Genereate a key using this script before using the password manager '''

from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)

file = open('key.txt', 'wb')
file.write(key)
file.close()