from random import randint
from sympy import randprime
import math


def generating_prime_numbers_and_test_Fermat(variables, data_rsa, bits = 8):
    t = math.ceil(-(math.log(0.0001, 2)))  # Вычисляем t для теста Ферма
    list_test_t = []  # Создаем список для хранения случайных чисел для теста Ферма
    while True:
        # Генерируем случайное простое число
        prime_number = randprime(2**(bits-1), 2**bits-1)
        if t > prime_number:
            t = prime_number
        flag = True  # Флаг для проверки простоты числа
        # Проверяем делимость на числа от 2 до 9
        for num in range(2, 10):
            if prime_number % num == 0:
                flag = False
                break
        if flag:
            list_test_t.clear()  # Очищаем список для нового числа
            len_test_t = t
            while len_test_t > 0:
                # Генерируем случайное число для теста Ферма
                test_t = randint(2, prime_number - 1)
                if test_t not in list_test_t:
                   list_test_t.append(test_t)
                   len_test_t -= 1
            # Производим t итераций теста Ферма
            for test_t in list_test_t:
                if pow(test_t, prime_number - 1, prime_number) != 1:
                    flag = False
                    break
        if flag:
            # Если число прошло тест Ферма, добавляем его в словарь
            data_rsa[variables] = prime_number
            return data_rsa

def the_product_the_product_of_two_numbers_qp(data_rsa):
    # Вычисляем произведение двух чисел q и p
    data_rsa["n"] = data_rsa["q"] * data_rsa["p"]
    return data_rsa

def the_Euler_function_of_n(data_rsa):
    # Вычисляем функцию Эйлера от числа n
    data_rsa["φ(n)"] = (data_rsa["p"]-1)*(data_rsa["q"]-1)
    return data_rsa

def evklid(data_rsa):
    data = [data_rsa["e"], data_rsa["φ(n)"]]
    a, b = max(data), min(data)
    q, r, x = "-", "-", "-"
    x2, x1, y2, y1 = 1, 0, 0, 1
    while True:
        while b != 0:
            q, r = (a // b), (a % b)
            x = (x2 - q * x1)
            y = (y2 - q * y1)
            a, b, x2, y2, x1, y1 = b, r, x1, y1, x, y
        if x2 * max(data) + y2 * min(data) != 1:
            # Если не выполняется условие, генерируем новые ключи
            data_rsa.clear()
            pq = generating_prime_numbers_and_test_Fermat("p", data_rsa)
            q = generating_prime_numbers_and_test_Fermat("q", data_rsa)
            n = the_product_the_product_of_two_numbers_qp(data_rsa)
            φ_from_n = the_Euler_function_of_n(data_rsa)
            e = generating_prime_numbers_and_test_Fermat("e", data_rsa)
        else:
            # Вычисляем d и добавляем его в словарь
            data_rsa["d"] = y2 % max(data)
            return data_rsa

def generating_key(data_rsa):
    # Генерируем открытый и закрытый ключи RSA
    data_keys = {}
    data_keys["public_key"] = (data_rsa["e"], data_rsa["n"])
    data_keys["private_key"] = (data_rsa["d"], data_rsa["n"])
    return data_keys

def privat_key(data_keys, name_private_key):
    # Записываем закрытый ключ в файл "private_key"
    with open(name_private_key, "w") as privat_key:
        for key in data_keys["private_key"]:
            privat_key.write(str(key) + "\n")

def public_key(data_keys, name_public_key):
    # Записываем открытый ключ в файл "public_key"
    with open(name_public_key, "w") as public_key:
        for key in data_keys["public_key"]:
            public_key.write(str(key) + "\n")

def check(data_keys):
    x = 7
    e = data_keys["public_key"][0]
    d = data_keys["private_key"][0]
    mod = data_keys["private_key"][1]
    y = pow(x, e, mod)
    z = pow(y, d, mod)
    if bool(x != z):
        # Проверяем соответствие x и z, если не совпадает - генерируем новые ключи
        key()
    return bool(x == z)

def key(bits = 8, name_private_key= "private_key", name_public_key="public_key"):
    data_rsa = {}  # Словарь для хранения данных RSA
    # Генерируем ключи RSA
    p = generating_prime_numbers_and_test_Fermat("p", data_rsa, bits)
    q = generating_prime_numbers_and_test_Fermat("q", data_rsa, bits)
    n = the_product_the_product_of_two_numbers_qp(data_rsa)
    φ_from_n = the_Euler_function_of_n(data_rsa)
    e = generating_prime_numbers_and_test_Fermat("e", data_rsa, bits)
    d = evklid(data_rsa)
    data_keys = generating_key(data_rsa)
    privat_key(data_keys, name_private_key)
    public_key(data_keys, name_public_key)
    check(data_keys)

key()  # Запускаем процесс генерации ключей
