#!/usr/bin/env python

import os

os.system('tshark -r error_reporting.pcap -T fields -e data > data.raw')

with open('data.raw') as f:
    data = ''.join(f.read().splitlines()[1:])

array = [int(data[i:i+2], 16) for i in range(0, len(data), 2)]

with open('flag.jpg', 'wb') as f:
    f.write(bytearray(array))
