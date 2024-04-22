import math



def calling_key_generation():
    data_keys = []
    with open("private_key") as private_key:
        public_key = private_key.readlines()
        for key in public_key:
            data_keys.append(int(key[:-1]))
    return data_keys


data_keys = calling_key_generation()
print(data_keys)