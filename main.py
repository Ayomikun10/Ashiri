#############################CREATED BY ADEJORO AYOMIKUN ################################
#############################WEBSITE 6kitworks.com ######################################


import base64
import random
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


charSalt = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
char_list = list(charSalt)
random.shuffle(char_list)
randomized_salt = bytes("".join(char_list), 'utf-8')


# Generate a key using PBKDF2
userPassword = input('Passwords are used for both encryption and decryption. \nWhat is your Password?  ')
password = bytes(userPassword, 'utf-8')
salt = randomized_salt
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256,
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))

fernet = Fernet(key)

ask = int(input('''Choose the following \n1. Encryptor \n2. Decryptor \n'''))

if ask == 1:
    userMessage  = input('Type your message...   ')
    message = bytes(userMessage, 'utf-8')
    encrypted_message = fernet.encrypt(message)
    print(encrypted_message)


elif ask == 2:

    userHash = input('Enetr your encrypted message...   ')
    hash = bytes(userHash, 'utf-8')
    # Decrypt the message using the key
    decrypted_message = fernet.decrypt(hash)

    # Verify that the original message and the decrypted message are the same

    #kassert message == decrypted_message
    print(decrypted_message)
else:
    print('Error follow the instructions again')





