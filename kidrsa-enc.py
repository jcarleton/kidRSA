def loadvars():
    plaintext = str(input("plaintext"))

    a = int(input("input a"))
    b = int(input("input b"))
    a1 = int(input("input a1"))
    b1 = int(input("input b1"))

    M = (a * b) - 1
    e = (a1 * M) + a
    d = (b1 * M) + b
    n = ((e * d) - 1) / M

    for element in plaintext:
      rsaEncrypt(ord(element), e, n)


def rsaEncrypt(plaintext, e, n):
    ciphertext = (plaintext * int(e)) % int(n)
    print(ciphertext)


def crypt():
    loadvars()


crypt()
