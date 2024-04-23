import math


def calling_privat_key_generation():
    data_keys = []
    with open("private_key") as public_key:
        public_key = public_key.readlines()
        for key in public_key:
            data_keys.append(int(key[:-1]))
    # print({
    #     'private_key': data_keys[0],
    #     'modulus': data_keys[1],
    #     'private_key_length': len(bin(data_keys[0])[2:]),
    #     'modulus_length': len(bin(data_keys[1])[2:])
    # })
    return data_keys

def get_len_block(data_keys):
    len_block = int(math.log(data_keys[1], 2))
    print({
        'len_block': len_block
    })
    return len_block

def splitting_into_bits(len_block):
    data_blocks_text = []
    with open("cipher_text.txt", "rb") as cipher_text:
        cipher_text = cipher_text.read()
    bits = ''.join(format(byte, '08b') for byte in cipher_text)
    while len(bits) > 0:
        data_blocks_text.append(int(bits[-len_block:], 2))
        bits = bits[:-len_block]
    return data_blocks_text

def decryptor(data_keys, data_blocks_text):
    data_num = []
    for num in data_blocks_text:
        data_num.append(pow(num, data_keys[0], data_keys[1]))
    # print(data_num)
    return data_num


def checker_bits(data_num):
    sum_bits = 0
    for bits in data_num:
        bit = bin(bits)[2:].zfill(len_block)
        sum_bits += math.ceil(len(bit)/8)
    return sum_bits





def bits_plus_zero(data_num):
    data_bits = []
    for bits in data_num:
        bit = bin(bits)[2:].zfill(len_block)
        data_bits.append(bit)
        # print(len(bit))
    return data_bits

def record_cipher(data_bits, sum_bits):
    data_bits = "".join(data_bits)
    data_int = int(data_bits, 2)
    data_bytes = int.to_bytes(data_int, sum_bits, byteorder='big', signed=True)
    print(data_bytes[0] == 0)
    while data_bytes[0] == 0:
        print(data_bits)
        data_bytes = data_bytes[1:]
    with open("decrypt_text.txt", "wb") as output_text:
        output_text.write(data_bytes)


data_privat_key = calling_privat_key_generation()
len_block_full = get_len_block(data_privat_key) + 1
len_block = get_len_block(data_privat_key)
data_blocks_text = splitting_into_bits(len_block_full)
data_num = decryptor(data_privat_key, data_blocks_text)
data_bits = bits_plus_zero(data_num)
sum_bits = checker_bits(data_num)
record_cipher(data_bits,sum_bits)
print(sum_bits)