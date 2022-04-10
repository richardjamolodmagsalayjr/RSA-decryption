import key_generation as kg


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


if __name__ == "__main__":
    print("--------------------Key Generation---------------------")
    keys = kg.gen_key(2333, 8951)
    public_key = keys[0]
    private_key = keys[1]
    print(f"public_key: {public_key}")
    print(f"private_key: {private_key}")

    print("---------------Encryption and Decryption---------------")
    plaintext = input("Plaintext: ")

    encrypted_message = rsa2(public_key, c2i(plaintext, alphabet))
    decrypted_message = i2c(rsa2(private_key, encrypted_message), alphabet)

    print(f"Encrypted message: {encrypted_message}")
    print(f"Decrypted message: {decrypted_message}")
