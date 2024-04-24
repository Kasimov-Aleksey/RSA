import math

def calling_key_private():
    data_keys = []
    with open("private_key") as file:
        private_key = file.readlines()
        for key in private_key:
            data_keys.append(int(key[:-1]))
    return data_keys


def decrypt_block(open_text_block, public_key, module, block_size):
    block_int = int(open_text_block, 2)
    block_int = pow(block_int, public_key, module)
    block_encrypt_bin = bin(block_int)[2:].zfill(block_size)

    return block_encrypt_bin
def decrypt(data_keys, cipher_text):
    with open(cipher_text, "rb") as file:
        cipher_text = file.read()

    private_key = data_keys[0]
    module = data_keys[1]
    cipher_text_bin = bin(int.from_bytes(cipher_text, byteorder="big", signed=False))[2:]
    block_size = math.floor(math.log(module, 2))
    block_size_extended = block_size + 1
    blocks_count = math.ceil(len(cipher_text_bin) / block_size_extended)

    decrypted_text_bin = ""

    for i in range(1, blocks_count + 1):
        begin = -(i * block_size_extended)
        finish = -(i * block_size_extended - block_size_extended)

        if not finish:
            finish = None

        print(cipher_text_bin[begin:finish])
        decrypted_block_bin = decrypt_block(cipher_text_bin[begin:finish], private_key, module, block_size)
        decrypted_text_bin = decrypted_block_bin + decrypted_text_bin

    decrypted_text_int = int(decrypted_text_bin, 2)
    _len = math.ceil(len(decrypted_text_bin) / 8)
    decrypted_text_bytes = bytearray(int.to_bytes(decrypted_text_int, length=_len, byteorder="big", signed=False))

    for index, i in enumerate(decrypted_text_bytes):
        if i != 0:
            decrypted_text_bytes = decrypted_text_bytes[index:]
            break

    with open("decrypted_text.txt", "wb") as file:
        file.write(decrypted_text_bytes)

decrypt(
    calling_key_private(),
    "encrypted_text.txt"
)