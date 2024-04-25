import math

def calling_key_public():
    # Функция для чтения открытого ключа из файла и его загрузки
    data_keys = []
    with open("public_key") as public_key:
        public_key = public_key.readlines()
        for key in public_key:
            data_keys.append(int(key[:-1]))  # Загружаем ключи из файла в список
    return data_keys

def encrypt_block(open_text_block, public_key, module, block_size):
    # Функция для шифрования блока текста
    block_int = int(open_text_block, 2)  # Преобразуем текст в целое число
    block_int = pow(block_int, public_key, module)  # Шифруем блок
    block_encrypt_bin = bin(block_int)[2:].zfill(block_size)  # Преобразуем зашифрованный блок в бинарную строку
    return block_encrypt_bin

def encrypt(data_keys, open_text):
    # Функция для шифрования всего текста
    with open(open_text, "rb") as file:
        open_text = file.read()  # Читаем открытый текст из файла

    public_key = data_keys[0]  # Загружаем открытый ключ
    module = data_keys[1]  # Загружаем модуль
    open_text_bin = bin(int.from_bytes(open_text, byteorder="big", signed=False))[2:]  # Преобразуем текст в бинарную строку
    block_size = math.floor(math.log(module, 2))  # Вычисляем размер блока
    block_size_extended = block_size + 1  # Увеличиваем размер блока на единицу для безопасности
    blocks_count = math.ceil(len(open_text_bin) / block_size)  # Вычисляем количество блоков

    encrypted_text_bin = ""

    for i in range(1, blocks_count + 1):
        begin = -(i * block_size)
        finish = -(i * block_size - block_size)

        if not finish:
            finish = None

        encrypted_block_bin = encrypt_block(open_text_bin[begin:finish], public_key, module, block_size_extended)  # Шифруем блок текста
        encrypted_text_bin = encrypted_block_bin + encrypted_text_bin

    encrypted_text_int = int(encrypted_text_bin, 2)  # Преобразуем зашифрованный текст в целое число
    _len = math.ceil(len(encrypted_text_bin) / 8)  # Вычисляем длину текста в байтах
    encrypted_text_bytes = bytearray(int.to_bytes(encrypted_text_int, length=_len, byteorder="big", signed=False))  # Преобразуем зашифрованный текст в байтовый массив

    with open("encrypted_text.txt", "wb") as file:
        file.write(encrypted_text_bytes)  # Записываем зашифрованный текст в файл

# Запуск процесса шифрования
encrypt(
    calling_key_public(),  # Загрузка открытого ключа
    "input_text"  # Имя файла с открытым текстом
)
