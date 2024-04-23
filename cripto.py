import math


def calling_key_generation():
    data_keys = []
    with open("public_key") as public_key:
        public_key = public_key.readlines()
        for key in public_key:
            data_keys.append(int(key[:-1]))
    print({
        'public_key': data_keys[0],
        'modulus': data_keys[1],
        'public_key_length': len(bin(data_keys[0])[2:]),
        'modulus_length': len(bin(data_keys[1])[2:])
    })
    return data_keys


def get_len_block(data_keys):
    len_block = int(math.log(data_keys[1], 2))
    print({
        'len_block': len_block
    })
    return len_block


def splitting_into_bits(len_block):
    data_blocks_text = []
    with open("input_text", "rb") as input_text:
        input_text = input_text.read()
    bits = ''.join(format(byte, '08b') for byte in input_text)
    while len(bits) > 0:
        add_bin = bits[-len_block:]
        add_bit = int(add_bin, 2)
        data_blocks_text.append(add_bit)
        bits = bits[:-len_block]
    return data_blocks_text


def mod(data_keys, data_blocks_text):
    data_num = []
    for num in data_blocks_text:
        enc_block_int = pow(num, data_keys[0], data_keys[1])
        data_num.append(enc_block_int)
    return data_num


def bits_plus_zero(data_num):
    data_bits = []
    for bits in data_num:
        bit = bin(bits)[2:].zfill(len_block_full)
        print(len(bit))
        data_bits.append(bit)

    return data_bits

def checker_bits(data_num):
    sum_bits = 0
    for bits in data_num:
        bit = bin(bits)[2:].zfill(len_block)
        sum_bits += math.ceil(len(bit)/8)
    print(sum_bits)
    return sum_bits




def record_cipher(data_bits, sum_bits):
    data_bits = "".join(data_bits)
    data_int = int(data_bits, 2)
    data_bytes = int.to_bytes(data_int, sum_bits, byteorder='big', signed=True)
    with open("cipher_text.txt", "wb") as output_text:
        output_text.write(data_bytes)


data_keys = calling_key_generation()
len_block = get_len_block(data_keys)
len_block_full = get_len_block(data_keys) + 1
data_blocks_text = splitting_into_bits(len_block)
data_num = mod(data_keys, data_blocks_text)
data_bits = bits_plus_zero(data_num)
sum_bits = checker_bits(data_num)
record_cipher(data_bits, sum_bits)
