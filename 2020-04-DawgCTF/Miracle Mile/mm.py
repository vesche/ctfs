import socket
import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'ctf.umbccd.io'
port = 5300
remote_ip = socket.gethostbyname(host)
sock.connect((remote_ip, port))

while True:
    data = sock.recv(4096).decode('utf-8')
    print(data)

    if not data:
        break

    for line in data.split('\n'):
        if "What's my pace?" in line:
            miles = float(line.split()[2])
            h, m, s = map(int, line.split()[4].split(':'))
            minutes = h*60 + m + s/60
            rate = str(datetime.timedelta(minutes=minutes/miles))[2:10] + '\n'
            sock.sendall(rate.encode())
            print(rate)

