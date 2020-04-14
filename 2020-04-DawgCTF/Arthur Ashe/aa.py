import random
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'arthurashe.ctf.umbccd.io'
port = 8411
remote_ip = socket.gethostbyname(host)
s.connect((remote_ip, port))

_ = s.recv(4096)
s.sendall('Y')

table = {
    'love': 15, '1':10, '2':20, '3':30, '4':40, '5':50, '10':10, '20':20, '30':30,
    '40':40, '50':50, 'game': 100, 'set': 1000, '15':15
}

while True:
    data = s.recv(4096)
    print(data)

    if 'YOU CANNOT BE SERIOUS' in data:
        break
    if 'The result of this' not in data:
        break

    them, us = data.split()[-1].rstrip('.').split('-')
    them, us = table[them], table[us]

    print(them, us)
    if them == us:
        n = '1'
    if them > us:
        n = '0'
    if us > them:
        n = '1'

    print('n = ' + n)
    s.sendall(n)

