import os
os.system('pip install pycrypto')
from Crypto.Cipher import AES
obj = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')

message = "something"

# Hash Key
ciphertext = obj.encrypt(message)
print(ciphertext)

# Answer 
obj2 = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
obj2.decrypt(ciphertext).decode('UTF-8')
