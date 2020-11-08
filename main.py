# from Cryptodome.PublicKey import RSA
from binascii import hexlify, unhexlify

f = open("rsa.txt", "r")
n = int(f.readline().split()[2])
e = int(f.readline().split()[2])
c = int(f.readline().split()[2])


def pick(letterarray):
    if len(letterarray) == 4:
        m = int(hexlify(str.encode("nactf{" + letterarray + "}")), 16)
        test = pow(m, e, n)
        if test == c:
            print("nactf{" + letterarray + "}")
            return True
        else:
            return False
    else:
        for i in range(26):
            if pick(letterarray + chr(97 + i)):
                return True
        return False


print("Calculating...")
pick("")
