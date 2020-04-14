
import base64
import codecs
import socket
import requests

from affine import decrypt as affine_decrypt

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'ctf.umbccd.io'
port = 5200
remote_ip = socket.gethostbyname(host)
sock.connect((remote_ip, port))

atbash_table = {
    'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
    'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
    'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
    'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
    'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B',
    'Z' : 'A', '{' : '{', '}' : '}'
}

def atbash(message):
    cipher = str()
    for letter in message:
        cipher += atbash_table[letter]
    return cipher

def decryptFence(cipher, rails=3, offset=0):
    plain = ''
    if offset:
        t = encryptFence('o'*offset + 'x'*len(cipher), rails)
        for i in range(len(t)):
            if(t[i] == 'o'):
                cipher = cipher[:i] + '#' + cipher[i:]
    length = len(cipher)
    fence = [['#']*length for _ in range(rails)]
    i = 0
    for rail in range(rails):
        p = (rail != (rails-1))
        x = rail
        while (x < length and i < length):
            fence[rail][x] = cipher[i]
            if p:
                x += 2*(rails - rail - 1)
            else:
                x += 2*rail
            if (rail != 0) and (rail != (rails-1)):
                p = not p
            i += 1
    # read fence
    for i in range(length):
        for rail in range(rails):
            if fence[rail][i] != '#':
                plain += fence[rail][i]
    return plain

while True:
    data = sock.recv(4096).decode('utf-8')
    print(data.rstrip())
    cipher = data.split('\n')[-2]
    # print(cipher)

    # affine
    if '{' in cipher:
        try:
            solve = affine_decrypt([9,6], cipher)
            if 'DOGECTF' in solve:
                print('SOLVED AFFFINE: ' + solve)
                sock.sendall(solve.encode() + b'\n')
                continue          
        except: pass

    # railfence
    if '{' in cipher:
        try:
            solve = decryptFence(cipher)
            if 'DOGECTF' in solve:
                print('SOLVED RAILFENCE: ' + solve)
                sock.sendall(solve.encode() + b'\n')
                continue
        except: pass   

    # atbash
    if '{' in cipher:
        try:
            solve = atbash(cipher)
            if 'DOGECTF' in solve:
                print('SOLVED ATBASH: ' + solve)
                sock.sendall(solve.encode() + b'\n')
                continue
        except: pass

    # rot_n
    if '{' in cipher:
        r = requests.get('http://theblob.org/rot.cgi?text=' + cipher)
        solve = None
        for line in r.text.splitlines():
            if 'DogeCTF' in line:
                solve = line.split()[-1].rstrip('<br>')
        if solve:
            print('SOLVED ROT_N: ' + solve)
            sock.sendall(solve.encode() + b'\n')
            continue

    # base64
    try:
        solve = base64.b64decode(cipher).decode('utf-8')

        if 'DogeCTF' in solve:
            print('SOLVED BASE64: ' + solve)
            sock.sendall(solve.encode() + b'\n')
            continue
    except:
        pass

    # base32
    try:
        solve = base64.b32decode(cipher).decode('utf-8')
        if 'DogeCTF' in solve:
            print('SOLVED BASE32: ' + solve)
            sock.sendall(solve.encode() + b'\n')
            continue
    except:
        pass

    # base16
    try:
        solve = base64.b16decode(cipher).decode('utf-8')
        if 'DogeCTF' in solve:
            print('SOLVED BASE16: ' + solve)
            sock.sendall(solve.encode() + b'\n')
            continue
    except:
        pass
