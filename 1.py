# from rsa import key
from decryption import decrypt, calling_key_private
def read_public_key():
    key_data = []
    with open("public_key") as public_key:
        public_key = public_key.readlines()
        for key in public_key:
            key_data.append(int(key))
            # print("key", key[:-2])
            # print(bin(int(key))[2:])
            key_data.append(len(bin(int(key))[2:]))
    return key_data

def dectption_no_licenzy():
    key_data = read_public_key()
    mod = int(key_data[2])
    lower_bit_limit = 2**(key_data[1]-1)
    while True:
        if mod % lower_bit_limit == 0:
            q = lower_bit_limit
            break
        lower_bit_limit +=1
    φ_from_n = (mod//q -1) * (q-1)
    hack_private_key = [pow(int(key_data[0]), -1, φ_from_n), mod]
    print(hack_private_key)
    x = 4444
    y = pow(x, key_data[0], key_data[2])
    z = pow(y,hack_private_key[0], hack_private_key[1])
    print(key_data)
    print(x==z)
    return hack_private_key

def record_hack_private_key():
    hack_private_key = dectption_no_licenzy()
    with open("hack_private_key", "w") as file_hack_private_key:
        for key in hack_private_key:
            file_hack_private_key.write(str(key) + "\n")

def record_hack_text():
    decrypted_text_bytes = decrypt(
        calling_key_private(name_private_key="hack_private_key"),  # Загрузка закрытого ключа
        "encrypted_text.txt"  # Имя файла с зашифрованным текстом
    )
    with open("hack_text.txt", "wb") as file:
        file.write(decrypted_text_bytes)



record_hack_private_key()
record_hack_text()



