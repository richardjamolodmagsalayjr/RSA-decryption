a = int(input("a: "))
b = int(input("b: "))


def euclidean_gcd(a, b):
    if b == 0:
        print(a)
    # if a < b:
    #     temp = a
    #     a = b
    #     b = temp
    else:
        euclidean_gcd(b, a % b)


euclidean_gcd(a, b)
