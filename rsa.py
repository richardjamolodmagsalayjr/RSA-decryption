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

text_message = "I love programming!"

# public key = (i,n)
# k = (i,n) such that i,n are key pair
i = int(input("Input i: "))
n = int(input("Input n: "))
k = (i, n)

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
        integer_message.append(i)
    return integer_message


def expmod(base, exp, n):
    # implement rigth to left binary exponentiation
    pass


def rsa2(k, c):
    # Implement message encryption
    pass


if __name__ == "__main__":
    # print(i2c(rsa(k, c1), alphabet))
    # print(i2c(rsa(k, c2), alphabet))
    print(c2i(text_message, alphabet))
    print(i2c(c2i(text_message, alphabet), alphabet))
