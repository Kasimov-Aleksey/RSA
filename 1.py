# def evklid():
#     data = [17, 8200]
#     a, b = max(data), min(data)
#     q, r, x, y = "-", "-", "-", "-"
#     x2, x1, y2, y1 = 1, 0, 0, 1
#     print(f"q={q}, r={r}, x={x}, y={y}, a={a}, b={b}, x2={x2}, x1={x1}, y2={y2}, y1={y1} ")
#     while b != 0:
#         q, r = (a // b), (a % b)
#         x = (x2 - q * x1)
#         y = (y2 - q * y1)
#         a, b, x2, y2, x1, y1 = b, r, x1, y1, x, y
#         print(f"q={q}, r={r}, x={x}, y={y}, a={a}, b={b}, x2={x2}, x1={x1}, y2={y2}, y1={y1} ")
#     r = [y2,data[1]]
#     return r
# r = evklid()
#
# print(pow(17,-1,8200))
# print(r[0]%r[1])
#

#
# def char_to_binary(char):
#     binary_repr = bin(ord(char))[2:].zfill(8)
#     return binary_repr
#
# # Пример использования:
# char = 'e'
# binary = char_to_binary(char)
# print(f"Двоичное представление символа '{char}': {binary}")

# import math
# print(math.floor(math.log(8383, 2)))
# print(int("0101100010111", 2))
# print(bin(2839)[2:].zfill(13))
# print()
#
# print(pow( 7420 ,6753,8383))
print(bin(3429)[2:].zfill(13))