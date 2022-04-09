# rsa key generation module
import random


"""
Note: ea_gcd and eea_gcd should return a SINGLE VALUE
      the greatest common divisor of two number a and b
"""


def gen_key(p, q):
    """
    Implement rsa key generation, public and private key
    p, q are prime numbers less than 10,000
    ((d,n), (e,n)) is a tuple of keys: private (d,n), public (e,n)
    """
    n = p * q
    p = (p - 1) * (q - 1)  # phi or totient of n, refers to the number of coprimes of n

    while True:
        # will be the value of e if it is coprime n
        # e must be an integer in between 1 < e < phi of n (p)
        a = random.randint(2, p - 1)
        if ea_gcd(a, p) == 1:
            e = a
            break

    d = eea_gcd(e, p)  # first parameter is the larger number
    print(f"e: {e},phi_n: {p}, n: {n}, d: {d}")


def ea_gcd(a, b):
    """
    Euclid's algorithm to find e
    "a" must be the greater numbe or the totient of n
    """
    if a < b:
        temp = a
        a = b
        b = temp
    if b == 0:
        return a
    else:
        return ea_gcd(b, a % b)


def eea_gcd(a, b):
    """
    Extended Euclidean algorithm to find d
    """
    m0 = b
    y = 0
    x = 1

    if b == 1:
        return 0

    while a > 1:

        # q is quotient
        q = a // b

        t = b

        # m is remainder now, process
        # same as Euclid's algo
        b = a % b
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

    # Make x positive
    if x < 0:
        x = x + m0

    return x


gen_key(2, 17)
