import gmpy2
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
        bits = input_text.read()
    # print(bits)
    while len(bits)>0:
        # if len(bits) <= len_block:
        #     bits = "0"*(len_block-len(bits)) + bits
        data_blocks_text.append(int(bits[-len_block:], 2))
        bits = bits[:-len_block]
    return data_blocks_text



def calling_privat_key_generation():
    with open("privat_key") as data_privat_key:
        data_privat_key = int(data_privat_key.readline())
    return data_privat_key


def open_ciper_text():
    with open("cipher_text", encoding='utf-8') as cipher_text:
        cipher_text = cipher_text.read()
    return cipher_text


def decryptor(cipher_text):
    decimal_number = gmpy2.mpz(cipher_text, base=2)
    return int(decimal_number)



data_keys = calling_key_generation():
data_privat_key = calling_privat_key_generation()
cipher_text = open_ciper_text()
decimal_number = decryptor(cipher_text)
m = cripto(data_open_keys,data_privat_key, decimal_number )
text = decriptor_text(m)
print(text)