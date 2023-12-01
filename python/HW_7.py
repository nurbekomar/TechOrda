# def factorial(n):
#     res = 1
#     for i in range(1, n):
#         res *= i
#     return res


# print(factorial(4))

# ==========================

# def convert(C):
#     return (C * 9/5) + 32


# print(convert(0))

# ==========================
# import math


# def lcm(a, b):
#     return (a * b) // math.gcd(a, b)


# print(lcm(12, 13))

# ==========================

# def calc(sk, mps, kp):
#     return sk * (mps * ((1+mps)**kp)/((1 + mps)**kp) - 1)


# print(calc(1400000, 13, 36))

# ==========================

def is_palindrome_number(number):
    num = number
    rev = 0
    while number > 0:
        dig = number % 10
        rev = rev * 10 + dig
        number = number // 10
    if (num == rev):
        return 'yes'
    else:
        return 'no'

print(is_palindrome_number(122))