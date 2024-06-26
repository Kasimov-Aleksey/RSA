import math
def read_public_key():
    key_data = []  # Инициализация списка для хранения данных открытого ключа
    with open("public_key") as public_key:
        public_key = public_key.readlines()
        for key in public_key:
            key_data.append(int(key))  # Добавление открытого ключа в список
            key_data.append(len(bin(int(key))[2:]))  # Добавление длины ключа в битах в список
    return key_data  # Возврат списка данных открытого ключа


def dectption_no_licenzy():
    key_data = read_public_key()  # Загрузка данных открытого ключа
    mod = int(key_data[2])  # Извлечение модуля из данных открытого ключа
    lower_bit_limit = 2 ** (key_data[1] - 1)  # Вычисление нижнего предела для поиска простого числа q
    while True:
        if mod % lower_bit_limit == 0:  # Проверка, является ли нижний предел делителем модуля
            q = lower_bit_limit  # Найденное простое число q
            break
        lower_bit_limit += 1  # Увеличение нижнего предела для поиска простого числа q
    φ_from_n = (mod // q - 1) * (q - 1)  # Вычисление значения функции Эйлера от модуля
    hack_private_key = [pow(int(key_data[0]), -1, φ_from_n), mod]  # Взлом закрытого ключа RSA
    x = 4444  # Число для проверки корректности взлома
    y = pow(x, key_data[0], mod)  # Шифрование числа x с использованием открытого ключа
    z = pow(y, hack_private_key[0],
            hack_private_key[1])  # Дешифрование числа y с использованием взломанного закрытого ключа
    return hack_private_key  # Возврат взломанного закрытого ключа RSA


def record_hack_private_key():
    hack_private_key = dectption_no_licenzy()  # Получение взломанного закрытого ключа
    with open("hack_private_key", "w") as file_hack_private_key:
        for key in hack_private_key:
            file_hack_private_key.write(str(key) + "\n")  # Запись взломанного закрытого ключа в файл



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




def record_hack_text():
    decrypted_text_bytes = decrypt(
        calling_key_private(name_private_key="hack_private_key"),  # Загрузка взломанного закрытого ключа
        "encrypted_text.txt"  # Имя файла с зашифрованным текстом
    )  # Дешифрование текста с использованием взломанного закрытого ключа
    with open("hack_text.txt", "wb") as file:
        file.write(decrypted_text_bytes)  # Запись дешифрованного текста в файл


record_hack_private_key()  # Запись взломанного закрытого ключа в файл
record_hack_text()
