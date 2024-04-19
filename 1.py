import math
def calling_key_generation():
    data_keys = []
    with open("open_key") as open_key:
        open_key = open_key.readlines()
        for key in open_key:
            data_keys.append(int(key[:-1]))
    return data_keys

def len_block(data_keys):
    len_block = int(math.log(data_keys[1], 2))
    return len_block

def splitting_into_bits(len_block):
    data_blocks_text = []
    with open("input_text", "rb") as input_text:
        input_text = input_text.read()
    bits = ''.join(format(byte, '08b') for byte in input_text)
    # print(bits)
    while len(bits)>0:
        # if len(bits) <= len_block:
        #     bits = "0"*(len_block-len(bits)) + bits
        data_blocks_text.append(int(bits[-len_block:], 2))
        bits = bits[:-len_block]
    return data_blocks_text


def mod(data_keys, data_blocks_text):
    data_num = []
    for num in data_blocks_text:
        data_num.append(pow(num, data_keys[0], data_keys[1]))
    return data_num

def bits_plus_zero(data_num):
    data_bits = []
    for bits in data_num:
        data_bits.append("0" + bin(bits)[2:])
    return data_bits

def record_cipher(data_bits):
    data_bits = "".join(data_bits)
    print(data_bits)
    with open("cipher_text", "w") as cipher_text:
        cipher_text.write(data_bits)







data_keys = calling_key_generation()
len_block = len_block(data_keys)
data_blocks_text= splitting_into_bits(len_block)
data_num = mod(data_keys, data_blocks_text)
data_bits = bits_plus_zero(data_num)
record_cipher(data_bits)
# print(data_bits)
# print(input_text)
# print(data_keys)