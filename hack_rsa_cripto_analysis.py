from random import randint

import math


def read_public_key():
    key_data = []
    with open("public_key") as public_key:
        public_key = public_key.readlines()
        for key in public_key:
            key_data.append(int(key))
            print(bin(int(key))[2:])
            key_data.append(len(bin(int(key))[2:]))
    return key_data


def generate_prime_numbers_and_test_Fermat(variables, rsa_data, key_data, ni):
    bits = key_data[1]
    t = math.ceil(-(math.log(0.0001, 2)))
    test_t_list = []
    while True:
        prime_number = pow(2, (bits - 1)) + ni

        if t > prime_number:
            t = prime_number
        flag = True
        for num in range(2, 10):
            if prime_number % num == 0:
                flag = False
                break
        if flag:
            test_t_list.clear()
            len_test_t = t
            while len_test_t > 0:
                test_t = randint(2, prime_number - 1)
                if test_t not in test_t_list:
                    test_t_list.append(test_t)
                    len_test_t -= 1

            for test_t in test_t_list:
                if pow(test_t, prime_number - 1, prime_number) != 1:
                    flag = False
                    break
        if flag:
            rsa_data[variables] = prime_number
            return rsa_data


def calculate_product_of_two_numbers_qp(rsa_data):
    rsa_data["n"] = rsa_data["q"] * rsa_data["p"]
    return rsa_data


def Euler_function_of_n(rsa_data):
    rsa_data["φ(n)"] = (rsa_data["p"] - 1) * (rsa_data["q"] - 1)
    return rsa_data


def euclid(rsa_data,n):
    data = [rsa_data["e"], rsa_data["φ(n)"]]
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
            rsa_data.clear()
            key_data = read_public_key()
            pq = generate_prime_numbers_and_test_Fermat("p", rsa_data, key_data, n)
            q = generate_prime_numbers_and_test_Fermat("q", rsa_data, key_data, n)
            n = calculate_product_of_two_numbers_qp(rsa_data)
            φ_from_n = Euler_function_of_n(rsa_data)
            e = generate_prime_numbers_and_test_Fermat("e", rsa_data)
        else:
            rsa_data["d"] = y2 % max(data)
            return rsa_data


def generate_key():
    ni = 0
    rsa_data = {}
    key_data = read_public_key()
    while True:
        p = generate_prime_numbers_and_test_Fermat("p", rsa_data, key_data, ni)
        q = generate_prime_numbers_and_test_Fermat("q", rsa_data, key_data, ni)
        n = calculate_product_of_two_numbers_qp(rsa_data)
        φ_from_n = Euler_function_of_n(rsa_data)
        e = generate_prime_numbers_and_test_Fermat("e", rsa_data, key_data, ni)
        d = euclid(rsa_data, n)

        if key_data[0] == rsa_data["e"] and key_data[2] == rsa_data["n"]:
            generated_key_data = {}
            generated_key_data["public_key"] = (rsa_data["e"], rsa_data["n"])
            generated_key_data["private_key"] = (rsa_data["d"], rsa_data["n"])
            return generated_key_data
        else:
            ni += 1

            print((rsa_data["e"], rsa_data["n"]))
            print((rsa_data["d"], rsa_data["n"]))
            rsa_data.clear()


generated_key_data = generate_key()
print("Finish", generated_key_data)
decrypt(
    calling_key_private(name_private_key="private_key"),  # Загрузка закрытого ключа
    "encrypted_text.txt"  # Имя файла с зашифрованным текстом
)