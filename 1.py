from random import randint, sample
from sympy import randprime
import math
data_rsa ={}
def generating_prime_numbers_and_test_Fermat(variables, data_rsa):
    bits = 2048
    t = math.ceil(-(math.log(0.0001, 2)))
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
            for _ in range(t):  # Производим t итераций теста Ферма
                a = randint(2, prime_number - 1)
                if pow(a, prime_number - 1, prime_number) != 1:
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
            # print(q, r, x, y, a, b, x2, x1, y2, y1)
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
    data_keys["open_key"] = (data_rsa["e"], data_rsa["n"])
    data_keys["close_key"] = (data_rsa["d"])
    return data_keys
#1
p = generating_prime_numbers_and_test_Fermat("p", data_rsa)
q = generating_prime_numbers_and_test_Fermat("q", data_rsa)
#2
n = the_product_the_product_of_two_numbers_qp(data_rsa)
#3
φ_from_n = the_Euler_function_of_n(data_rsa)
#4
e = generating_prime_numbers_and_test_Fermat("e", data_rsa)
#5
d = evklid(data_rsa)
#6
data_keys = generating_key(data_rsa)

print(data_rsa)
print(data_keys)


