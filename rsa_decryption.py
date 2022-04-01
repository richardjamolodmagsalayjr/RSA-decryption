import math

alphabet = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ.!?,"
# c is a list of encrypted interger message
# each item in the list represents single character
c = [
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
        message = character
        for i in range(1, k[0]):
            message *= int(character)
        message = message % k[1]
        decrypted_message.append(message)
    return decrypted_message


# covert decrypted integer message into text, reverse to c2i, algo 2
def i2c(m, alphabet):
    message = ""
    for i in m:
        c = alphabet[i]
        message += c
    return message


if __name__ == "__main__":
    print(i2c(rsa(k, c), alphabet))
