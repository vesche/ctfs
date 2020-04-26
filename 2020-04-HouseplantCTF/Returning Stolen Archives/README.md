## Returning Stolen Archives

This was the challenge text:
```
Returning Stolen Archives - 50 Points

So I was trying to return the stolen archives securely, but it seems that I had to return them one at a time, and now it seems the thieves stole them back! Can you help recover them once and for all? It seems they had to steal them one at a time...

Dev: William
Hint! Well you sure as hell ain't going to solve this one through factorization.

* intercepted.txt
* returningstolenarchives.py
```

Given the `intercepted.txt` file, we know the values of n, e, and the cipher text letters (ct). Looking at the python code in `returningstolenarchives.py` what we need to figure out is: ((some char) ^ e) % n == cipher letter

Therefore, we can brute force to recover the plaintext:
```python
from string import printable

for cipher_letter in ct:
    for letter in printable:
        if (ord(letter) ** e) % n == cipher_letter:
            print(letter, end='')
            break
```

This gives us the flag:
```
$ python solve.py
rtcp{cH4r_bY_Ch@R!}
```
