from random import randint, sample
import math
data_rsa ={}
def generating_prime_numbers_and_test_Fermat(variables, data_rsa, a, b):
    while True:
        prime_number = randint(a, b)
        t = math.ceil(-(math.log(0.0001, 2)))
        if t > prime_number:
            t = prime_number
        list_test_t = sample(range(2, (prime_number - 1)), t)  # шаг1: создаем список Выбираем а[2, n-1]
        for elem_s in list_test_t:
            r = elem_s**(prime_number - 1) % prime_number
            if r != 1:
                break
        else:
            data_rsa[variables] = prime_number
            return data_rsa

q = generating_prime_numbers_and_test_Fermat("p", data_rsa, 75, 345)
q = generating_prime_numbers_and_test_Fermat("q", data_rsa, 75, 345)
print(data_rsa)