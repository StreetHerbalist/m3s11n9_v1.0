import json
import requests
import hashlib 
import random
import string

class password_generator():
    PASSWORDS = []
    PASSWORDS_HASHED = []
    HOST = ""
    def make_an_list_of_random(self)-> None: 
        letters_up = string.ascii_uppercase()
        letters_down = string.ascii_lowercase()
        numbers = [0,(range(1,9))]
        separator  = " "
        every_letter = separator.join(f'{letters_up}{letters_down}')
        list_of_every_sign = numbers + every_letter
        for _ in range(1,100):
            password = random.sample(list_of_every_sign, 16) 
            self.PASSWORDS.append(password)
            pasword_hashed = hashlib.md5(password.encode())
            self.PASSWORDS_HASHED.append()
    print(f'Your paswwords are: {PASSWORDS}')
    print(f'Your hashed paswwords are: {PASSWORDS_HASHED}')

instance = password_generator()
instance.make_an_list_of_random