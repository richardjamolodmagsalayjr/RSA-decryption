from email import message
import math

alphabet = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ.!?,"
encrypted_message = [
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
"""
k = (e,n) such that i,n are key pair
c is the integer message
public key = (e,n) = (12847, 19177)
"""
d = input("Input d: ")
n = input("Input n: ")
k = (d, n)
decrypted_message = []
text_message = []


def rsa(k):
    m = 1
    e = int(k[0])
    n = int(k[1])

    for character in encrypted_message:
        message = character
        for i in range(0, e):
            message *= int(character)
        decrypted = message % n
        decrypted_message.append(decrypted)
    return decrypted_message


def index_of_c(m, alphabet):
    for text in decrypted_message:
        temp = ''
        for index in str(text):
            temp += alphabet[int(index)]
        text_message.append(temp)
    return text_message


# print(math.pow(14203, 12847))
# m = int(rsa(d))
print(rsa(k))
print(index_of_c(rsa(k), alphabet))
