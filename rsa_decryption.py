from email import message


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
e = 12847
n = 19177
k = (e, n)


def rsa(k):
    decrypted_message = []
    e = int(k[0])
    n = int(k[1])

    for character_number in encrypted_message:
        message = character_number
        for i in range(1, e):
            message *= int(character_number)
        decrypted = message % n
        decrypted_message.append(decrypted)
    return decrypted_message


def index_of_c(m, alphabet):
    message = []
    for text in m:
        text_character = alphabet[text]
        message.append(text_character)
    return message


# print(index_of_c(encrypted_message, alphabet))
# print(index_of_c(rsa(k), alphabet))

print(len(rsa(k)))
print(len(encrypted_message))
print(index_of_c(rsa(k), alphabet))

