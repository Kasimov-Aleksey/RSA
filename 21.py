from decryption import decrypt, calling_key_private  # Импорт функций дешифрования и загрузки закрытого ключа

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


def record_hack_text():
    decrypted_text_bytes = decrypt(
        calling_key_private(name_private_key="hack_private_key"),  # Загрузка взломанного закрытого ключа
        "encrypted_text.txt"  # Имя файла с зашифрованным текстом
    )  # Дешифрование текста с использованием взломанного закрытого ключа
    with open("hack_text.txt", "wb") as file:
        file.write(decrypted_text_bytes)  # Запись дешифрованного текста в файл


record_hack_private_key()  # Запись взломанного закрытого ключа в файл
record_hack_text()  # Запись дешифрованного текста в файл