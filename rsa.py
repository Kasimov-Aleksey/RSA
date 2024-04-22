from random import randint
from sympy import randprime
import math
data_rsa ={}
def generating_prime_numbers_and_test_Fermat(variables, data_rsa):
    bits = 2048
    t = math.ceil(-(math.log(0.0001, 2)))
    list_test_t = []
    while True:
        prime_number = randprime(2**(bits-1), 2**bits-1)
        if t > prime_number:
            t = prime_number
        flag = True
        for num in range(2, 10):  # Проверка делимости на числа от 2 до 9
            if prime_number % num == 0:
                flag = False
                break
        if flag:
            list_test_t.clear()
            len_test_t = t
            while len_test_t > 0:
                test_t = randint(2, prime_number - 1)
                if test_t not in list_test_t:
                   list_test_t.append(test_t)
                   len_test_t -= 1

            for test_t in list_test_t:  # Производим t итераций теста Ферма
                if pow(test_t, prime_number - 1, prime_number) != 1:
                    flag = False
                    break
        if flag:
            data_rsa[variables] = prime_number
            return data_rsa



def the_product_the_product_of_two_numbers_qp(data_rsa):
    data_rsa["n"] = data_rsa["q"] * data_rsa["p"]
    return data_rsa

def the_Euler_function_of_n(data_rsa):
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
        if x2 * max(data) + y2 * min(data)!=1:
            data_rsa.clear()
            pq = generating_prime_numbers_and_test_Fermat("p", data_rsa)
            q = generating_prime_numbers_and_test_Fermat("q", data_rsa)
            n = the_product_the_product_of_two_numbers_qp(data_rsa)
            φ_from_n = the_Euler_function_of_n(data_rsa)
            e = generating_prime_numbers_and_test_Fermat("e", data_rsa)
        else:
            data_rsa["d"] = y2 % max(data)
            return data_rsa

def generating_key(data_rsa):
    data_keys = {}
    data_keys["public_key"] = (data_rsa["e"], data_rsa["n"])
    data_keys["private_key"] = (data_rsa["d"], data_rsa["n"])
    return data_keys

def privat_key(data_keys):
    with open("private_key", "w") as privat_key:
        for key in data_keys["private_key"]:
            privat_key.write(str(key) + "\n")

def public_key(data_keys):
    with open("public_key", "w") as public_key:
        for key in data_keys["public_key"]:
            public_key.write(str(key) + "\n")

def key():
    # 1
    p = generating_prime_numbers_and_test_Fermat("p", data_rsa)
    q = generating_prime_numbers_and_test_Fermat("q", data_rsa)
    # 2
    n = the_product_the_product_of_two_numbers_qp(data_rsa)
    # 3
    φ_from_n = the_Euler_function_of_n(data_rsa)
    # 4
    e = generating_prime_numbers_and_test_Fermat("e", data_rsa)
    # 5
    d = evklid(data_rsa)
    # 6
    data_keys = generating_key(data_rsa)
    privat_key(data_keys)
    public_key(data_keys)
    return data_keys

data_keys = key()