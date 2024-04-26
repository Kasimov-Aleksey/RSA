import math

def calling_key_private(name_private_key):
    # Функция для загрузки закрытого ключа из файла "private_key"
    data_keys = []
    with open(name_private_key) as file:
        private_key = file.readlines()
        for key in private_key:
            data_keys.append(int(key[:-1]))  # Загружаем ключи из файла в список
    return data_keys

def decrypt_block(open_text_block, public_key, module, block_size):
    # Функция для расшифрования блока текста
    block_int = int(open_text_block, 2)  # Преобразуем текст в целое число
    block_int = pow(block_int, public_key, module)  # Дешифруем блок
    block_encrypt_bin = bin(block_int)[2:].zfill(block_size)  # Преобразуем расшифрованный блок в бинарную строку
    return block_encrypt_bin

def decrypt(data_keys, cipher_text):
    # Функция для расшифрования всего текста
    with open(cipher_text, "rb") as file:
        cipher_text = file.read()  # Читаем зашифрованный текст из файла

    private_key = data_keys[0]  # Загружаем закрытый ключ
    module = data_keys[1]  # Загружаем модуль
    cipher_text_bin = bin(int.from_bytes(cipher_text, byteorder="big", signed=False))[2:]  # Преобразуем текст в бинарную строку
    block_size = math.floor(math.log(module, 2))  # Вычисляем размер блока
    block_size_extended = block_size + 1  # Увеличиваем размер блока на единицу для безопасности
    blocks_count = math.ceil(len(cipher_text_bin) / block_size_extended)  # Вычисляем количество блоков

    decrypted_text_bin = ""

    for i in range(1, blocks_count + 1):
        begin = -(i * block_size_extended)
        finish = -(i * block_size_extended - block_size_extended)

        if not finish:
            finish = None

        decrypted_block_bin = decrypt_block(cipher_text_bin[begin:finish], private_key, module, block_size)  # Расшифруем блок текста
        decrypted_text_bin = decrypted_block_bin + decrypted_text_bin

    decrypted_text_int = int(decrypted_text_bin, 2)  # Преобразуем расшифрованный текст в целое число
    _len = math.ceil(len(decrypted_text_bin) / 8)  # Вычисляем длину текста в байтах
    decrypted_text_bytes = bytearray(int.to_bytes(decrypted_text_int, length=_len, byteorder="big", signed=False))  # Преобразуем расшифрованный текст в байтовый массив

    for index, i in enumerate(decrypted_text_bytes):
        if i != 0:
            decrypted_text_bytes = decrypted_text_bytes[index:]
            break
    return decrypted_text_bytes

def record_decrypted_text():
    decrypted_text_bytes = decrypt(
        calling_key_private(name_private_key="private_key"),  # Загрузка закрытого ключа
        "encrypted_text.txt"  # Имя файла с зашифрованным текстом
    )

    with open("decrypted_text.txt", "wb") as file:
        file.write(decrypted_text_bytes)  # Записываем расшифрованный текст в файл

record_decrypted_text()