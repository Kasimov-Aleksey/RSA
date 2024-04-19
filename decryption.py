import gmpy2
def calling_open_key_generation():
    data_open_keys = []
    with open("open_key") as open_key:
        open_key = open_key.readlines()
        for key in open_key:
            data_open_keys.append(int(key[:-1]))
    return data_open_keys


def calling_privat_key_generation():
    with open("privat_key") as data_privat_key:
        data_privat_key = int(data_privat_key.readline())
    return data_privat_key


def open_ciper_text():
    with open("cipher_text") as cipher_text:
        cipher_text = cipher_text.read()
    return cipher_text


def decryptor(cipher_text):
    decimal_number = gmpy2.mpz(cipher_text, base=2)
    return int(decimal_number)

def cripto(data_open_keys,data_privat_key, decimal_number ):
    m = pow(decimal_number, data_privat_key, data_open_keys[1])
    m = bin(m)[2:]
    return m

def decriptor_text(m):
    chunks = [m[i:i + 8] for i in range(0, len(m), 8)]
    text = ''.join([chr(int(chunk, 2)) for chunk in chunks])
    return text


data_open_keys = calling_open_key_generation()
data_privat_key = calling_privat_key_generation()
cipher_text = open_ciper_text()
decimal_number = decryptor(cipher_text)
m = cripto(data_open_keys,data_privat_key, decimal_number )
text = decriptor_text(m)
print(text)