with open('fl4g.jpeg', 'rb') as f:
    data = [b for b in f.read()]

new_data = list()

for i in range(0, len(data), 4):
    new_data += data[i:i+4][::-1]

with open('fl4g_solve.jpeg', 'wb') as f:
    f.write(bytearray(new_data))
