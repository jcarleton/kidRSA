def loadvars():
    ciphertext = input("ciphertext")
    ciphertext = ciphertext.split(',')

    for i in range(len(ciphertext)):
        ciphertext[i] = int(ciphertext[i])


    a = int(input("input a"))
    b = int(input("input b"))
    a1 = int(input("input a1"))
    b1 = int(input("input b1"))

    M = (a * b) - 1
    e = (a1 * M) + a
    d = (b1 * M) + b
    n = ((e * d) - 1) / M

    for elements in ciphertext:
        rsaDecrypt(elements, d, n)


def rsaDecrypt(ciphertext, d, n):
    plaintext = (ciphertext * int(d)) % int(n)
    print(str(chr(plaintext)))


def crypt():
    loadvars()


crypt()
