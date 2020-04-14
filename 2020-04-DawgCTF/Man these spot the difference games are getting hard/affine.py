WIDTH = 26
ASC_A = ord('A')

def encrypt(key, words):
    return ''.join([shift(key, ch) for ch in words.upper()])

def decrypt(key, words):
    a, b = modInverse(key[0], WIDTH), -key[1]
    d = str()
    for ch in words.upper():
        if ch == '{':
            d += '{'
            continue
        elif ch ==  '}':
            d += '}'
            continue
        d += unshift([a, b], ch)
    return d

def shift(key, ch):
    if str.isalpha(ch):
        offset = ord(ch) - ASC_A
        return chr(((key[0] * offset + key[1]) % WIDTH) + ASC_A)
    return ''

def unshift(key, ch):
    offset = ord(ch) - ASC_A
    return chr(((key[0] * (offset + key[1])) % WIDTH) + ASC_A)

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def modInverse(a, m):
    if gcd(a, m) != 1:
        print("Error")
        quit()
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

