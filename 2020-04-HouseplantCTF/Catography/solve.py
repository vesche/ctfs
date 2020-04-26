import re

def do_thing(s):
    deg, minutes, seconds, direction = re.split('[°\'"]', s)
    return (float(deg) + float(minutes)/60 + float(seconds)/(60*60)) * (-1 if direction in ['W', 'S'] else 1)

with open('gps.txt','r') as f:
    data = f.read().splitlines()

for line in data:
    deg1, _, m1, s1, dir1, deg2, _, m2, s2, dir2 = line.split()[3:]
    deg1 += '°'
    deg2 += '°'
    dir1 = dir1.rstrip(',')
    dir2 = dir2.rstrip(',')
    conv1 = deg1 + m1 + s1 + dir1
    conv2 = deg2 + m2 + s2 + dir2
    print(str(do_thing(conv1)) + ', ' + str(do_thing(conv2)))