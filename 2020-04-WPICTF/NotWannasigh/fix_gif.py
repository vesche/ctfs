#!/usr/bin/env python

#
# fix_gif.py
#

# read in the encrypted gif
with open('flag-gif.EnCiPhErEd', 'rb') as f:
    encrypted_bytes = [i for i in f.read()]

# read in the srand numbers we generated in C
with open('srand_bytes.txt', 'r') as f:
    srand_bytes = list(map(int, f.read().split()))

# XOR the encrypted bytes and the srand_bytes
gif = []
for a, b in zip(encrypted_bytes, srand_bytes):
    gif.append(a ^ b)

# write the XOR'd data
with open('flag.gif', 'wb') as f:
    f.write(bytearray(gif))
