from ipynb.fs.full.Library import Encrypt, Decrypt


p = 1000000007
q = 1000000009
e = 23917
n = p * q

c = Encrypt("CMP", n, e)
m = Decrypt(c, p, q, e)
print(m)
