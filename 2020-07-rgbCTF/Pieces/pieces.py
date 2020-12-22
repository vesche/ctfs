s = '9|2/9/:|4/7|8|4/2/1/2/9/'
tokens = [s[i:i+2] for i in range(0, len(s), 2)]
solution = str()

for t in tokens:
    if '|' in t:
        m = 0
    elif '/' in t:
        m = 1
    solution += chr(ord(t[0])*2+m)

print('rgbCTF{%s}' % solution)