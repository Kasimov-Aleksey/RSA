import math

def calling_key_generation():
    data_keys = []
    with open("open_key") as open_key:
        open_key = open_key.readlines()
        for key in open_key:
            data_keys.append(int(key[:-1]))
    print(data_keys)
    return data_keys

def len_block(data_keys):
    len_block = int(math.log(data_keys[1], 2))
    # print(len_block)
    return len_block

def division_into_blocks(len_block, data_keys):
    with open("input_text", "rb") as input_text:
        input_text = input_text.read()
        bits = ''.join(format(byte, '08b') for byte in input_text)
    data_blocks = []
    if len(bits) % len_block != 0:
        bits = "0" * (len(bits) % len_block) + bits
    while len(bits) > 0:
        data_blocks.append([bits[:len_block]])
        bits = bits[len_block:]
    return data_blocks


def conversion_to_cipher(data_blocks, data_keys):
    data_cripto = []
    for binary_number in data_blocks:
        # print(binary_number)
        decimal_number = int("".join(binary_number), 2)
        # print(decimal_number)
        c = pow(decimal_number, data_keys[0], data_keys[1])
        binary_number = "0" + bin(c)[2:]
        data_cripto.append(binary_number)
    return data_cripto

def ciphertext_recording(data_cripto):
    data_cripto = "".join(data_cripto)
    # print(data_cripto)
    with open("cipher_text", "w") as ciphertext:
        ciphertext.write(data_cripto)
    return ciphertext


data_keys = calling_key_generation()
len_block = len_block(data_keys)
data_blocks = division_into_blocks(len_block, data_keys)
data_cripto = conversion_to_cipher(data_blocks, data_keys)
# print(data_cripto)
ciphertext_recording(data_cripto)

