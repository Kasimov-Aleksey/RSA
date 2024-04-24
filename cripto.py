import math

def calling_key_public():
    data_keys = []
    with open("public_key") as public_key:
        public_key = public_key.readlines()
        for key in public_key:
            data_keys.append(int(key[:-1]))
    return data_keys

def encrypt_block(open_text_block, public_key, module, block_size):
    block_int = int(open_text_block, 2)
    block_int = pow(block_int, public_key, module)
    block_encrypt_bin = bin(block_int)[2:].zfill(block_size)

    return block_encrypt_bin

def encrypt(data_keys, open_text):
    with open(open_text, "rb") as file:
        open_text = file.read()

    public_key = data_keys[0]
    module = data_keys[1]
    open_text_bin = bin(int.from_bytes(open_text, byteorder="big", signed=False))[2:]
    block_size = math.floor(math.log(module, 2))
    block_size_extended = block_size + 1
    blocks_count = math.ceil(len(open_text_bin)/block_size)

    encrypted_text_bin = ""

    for i in range(1, blocks_count + 1):
        begin = -(i * block_size)
        finish = -(i * block_size - block_size)

        if not finish:
            finish = None

        print(open_text_bin[begin:finish])
        encrypted_block_bin = encrypt_block(open_text_bin[begin:finish], public_key, module, block_size_extended)
        encrypted_text_bin = encrypted_block_bin + encrypted_text_bin

    encrypted_text_int = int(encrypted_text_bin, 2)
    _len = math.ceil(len(encrypted_text_bin) / 8)
    encrypted_text_bytes = bytearray(int.to_bytes(encrypted_text_int, length=_len, byteorder="big", signed=False))

    with open("encrypted_text.txt", "wb") as file:
        file.write(encrypted_text_bytes)


encrypt(
    calling_key_public(),
    "input_text"
)