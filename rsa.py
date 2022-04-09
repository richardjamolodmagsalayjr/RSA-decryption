from email import message
import key_generation as kg


alphabet = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ.!?,"
# c is a list of encrypted interger message
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


# rsa decryption algo
def rsa(k, c):
    decrypted_message = []

    # code from scratch exponentiation function
    # then get modulo
    for character in c:
        decrypted_message.append((character ** k[0]) % k[1])
    return decrypted_message


# convert integer message into text, reverse to c2i, algo 3
def i2c(m, alphabet):
    message = ""
    for i in m:
        c = alphabet[i]
        message += c
    return message


# convert text into integer message, algo 2, prog_ass 2 task 1, tested
def c2i(c, alphabet):
    integer_message = []
    for character in c:
        i = alphabet.index(character)
        integer_message.append(int(i))
    return integer_message


def expmod(base, exp, n):
    # implement left to right binary exponentiation
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
    # Implement message encryption, using binary expoentiation
    # for efficient calculation for large numbers
    i = k[0]
    n = k[1]
    encrypted_message = []
    # c_ in c means each item in the list c, uses c_ to distiguish item and list c
    for c_ in c:
        encrypted_message.append(expmod(c_, i, n))
    return encrypted_message


if __name__ == "__main__":
    print("--------------Key Generation--------------")
    keys = kg.gen_key(83, 13)
    public_key = keys[0]
    private_key = keys[1]

    print(f"public_key: {public_key}")
    print(f"private_key: {private_key}")

    plaintext = input("Plaintext: ")

    encrypted_message = rsa2(public_key, c2i(plaintext, alphabet))

    # use rsa2 for decryption to make computation of large numbers feasible
    decrypted_message = i2c(rsa2(private_key, encrypted_message), alphabet)

    print(f"Encrypted message: {encrypted_message}")
    print(f"Decrypted message: {decrypted_message}")

    # n = int(input("Input n: "))
    # k = (i, n)

    # if action == 1:
    #     text_message = input("Input text message: ")
    #     print(f"Translated message to integer message: {c2i(text_message,alphabet)}")
    #     print(f"Encrypted integer message: {rsa2(k,c2i(text_message,alphabet))}")
    # else:
    #     # used the direct method of moduar exponentiation
    #     print(f"Decrypted message c1: {i2c(rsa(k,c1), alphabet)}")
    #     print(f"Decrypted message c2: {i2c(rsa(k,c2), alphabet)}")
