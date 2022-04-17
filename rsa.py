import random

alphabet = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ.!?,"
# c is a list of encrypted integer message
# each item in the list represents single character
# c1 and c2 are lists of encrypted message
c1 = [
    16669,
    8825,
    7907,
    9622,
    16100,
    552,
    8825,
    9622,
    13300,
    8825,
    11291,
    0,
    8825,
    15014,
    0,
    11291,
    12294,
]
c2 = [
    14203,
    13300,
    11291,
    18556,
    17918,
    0,
    2178,
    552,
    12294,
    8825,
    176,
    13300,
    2704,
    8825,
    2178,
    13300,
    8825,
    1,
    3558,
    8825,
    15014,
    13300,
    3449,
    8825,
    9502,
    13300,
    13501,
]


def rsa(k, c):
    # A direct approach for encrypting and decrypting message.
    # To encrypt or decrypt message, its format must be in integer.
    # e.g c = [1, 23, 34, 43]
    # k = (i,n)
    message = []
    for character in c:
        message.append((character ** k[0]) % k[1])

    return message


def i2c(m, alphabet):
    # convert integer message into text/characters
    message = ""
    for i in m:
        c = alphabet[i]
        message += c

    return message


def c2i(c, alphabet):
    # convert text/message into integer message
    integer_message = []
    for character in c:
        i = alphabet.index(character)
        integer_message.append(int(i))

    return integer_message


def expmod(base, exp, n):
    # Implemented right to left binary exponentiation over modulo
    if n == 1:
        return 0
    res = 1
    base = base % n
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % n
        exp = exp >> 1
        base = (base * base) % n

    return res


def rsa2(k, c):
    # Implement message encryption, using binary expoentiation.
    # To efficiently calculate exponetiation on large numbers.
    i = k[0]
    n = k[1]
    message = []
    # c_ in c means each item in the list c, uses c_ to distiguish item and list c
    for c_ in c:
        message.append(expmod(c_, i, n))
    return message


"""
Note: ea_gcd and eea_gcd should return a SINGLE VALUE
      the greatest common divisor of two number a and b
"""


def gen_key(p, q):
    """
    Implement rsa key generation, public and private key
    ((d,n), (e,n)) is a tuple of keys: private (d,n), public (e,n)
    """
    n = p * q  # product of to large prime numbers less than 10,000
    p = (p - 1) * (q - 1)  # phi or totient of n, refers to the number of coprimes of n

    while True:
        """
        e must be an integer in between 1 < e < phi of n (p)
        Loop breaks if gcd is 1
        """

        temp = random.randint(2, p - 1)  # randint has inclusive range,
        if ea_gcd(temp, p) == 1:
            e = temp
            break

    # first parameter must be the larger number,d is the multiplicative inverse if e and p
    # e and p must be co primes
    d = eea_gcd(e, p)

    return ((d, n), (e, n))


def ea_gcd(a, b):
    """
    Euclid's algorithm to find e
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
    m = b
    y = 0
    x = 1

    if b == 1:
        return 0

    while a > 1:
        quotient = a // b
        t = b
        b = a % b
        a = t
        t = y
        y = x - quotient * y
        x = t

    # x must be positive
    if x < 0:
        x = x + m

    return x  # multiplicative inverse of e and p


if __name__ == "__main__":
    print("--------------------Key Generation---------------------")
    keys = gen_key(2333, 8951)  # random large prime numbers, returns
    public_key = keys[1]
    private_key = keys[0]
    print(f"public_key: {public_key}")
    print(f"private_key: {private_key}\n")

    print("---------------Encryption and Decryption---------------")
    plaintext = input("Plaintext: ")
    encrypted_message = rsa2(public_key, c2i(plaintext, alphabet))
    decrypted_message = i2c(rsa2(private_key, encrypted_message), alphabet)

    print(f"Encrypted message: {encrypted_message}")
    print(f"Decrypted message: {decrypted_message}")
