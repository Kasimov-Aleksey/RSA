#гененрция простых чисел

data_rsa ={}
from random import randint
def generating_prime_numbers(variables,data_rsa, a, b):
    for elem in variables:
        while True:
            prime_number = randint(a, b)
            for num in range(2, (prime_number//2)+1):
                if prime_number % num == 0:
                    break
            else:
                data_rsa[elem] = prime_number
                break
    return data_rsa


def the_product_the_product_of_two_numbers_qp(prime_numbers,data_rsa):
    data_rsa["n"] = prime_numbers["q"] * prime_numbers["p"]
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
            pq = generating_prime_numbers(["p"], data_rsa, 75, 345)
            q = generating_prime_numbers(["q"], data_rsa, 75, 345)
            n = the_product_the_product_of_two_numbers_qp(pq, data_rsa)
            φ_from_n = the_Euler_function_of_n(data_rsa)
            e = generating_prime_numbers(["e"], data_rsa, 45, 120)
        else:
            data_rsa["d"] = y2 % max(data)
            return data_rsa

def generating_key(data_rsa):
    data_keys = {}
    data_keys["open_key"] = (data_rsa["e"], data_rsa["n"])
    data_keys["close_key"] = (data_rsa["d"])
    return data_keys
#1
pq = generating_prime_numbers(["p"], data_rsa, 75, 345)
q = generating_prime_numbers(["q"], data_rsa, 75, 345)
#2
n = the_product_the_product_of_two_numbers_qp(pq, data_rsa)
#3
φ_from_n = the_Euler_function_of_n(data_rsa)
#4
e = generating_prime_numbers(["e"], data_rsa, 45, 120)
#5
d = evklid(data_rsa)
#6
data_keys = generating_key(data_rsa)

print(data_rsa)
print(data_keys)


