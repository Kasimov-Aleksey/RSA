from random import randint
from sympy import randprime
import math
data_rsa ={}

def calling_key_generation():
    data_keys = []
    with open("public_key") as public_key:
        public_key = public_key.readlines()
        for key in public_key:
            data_keys.append(int(key[:-1]))
            data_keys.append(len(bin(int(key[2:]))))
    return data_keys




data_keys_and_len_key = calling_key_generation()

print(data_keys_and_len_key )