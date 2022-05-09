from ipynb.fs.full.Library import GCD, ModInv, IsPrime, GenRandPrime, Encrypt, Decrypt, log, floor

def sign_up(p, q, e):
   #! what condition should I generate the numbers on (Should the be small or large)?
   K=1000 #TODO: what is the value of K?
   if p == '':
      p = str(GenRandPrime(K))
   if q == '':
      q = str(GenRandPrime(K))

   err_msg = ''
   if not p.isdigit() and err_msg == '':
      err_msg = 'p must be a number'
   if not q.isdigit() and err_msg == '':
      err_msg = 'q must be a number'

   p = int(p)
   q = int(q)
   n = p*q
   phi_n = (p - 1) * (q - 1)

   if not IsPrime(p) and err_msg == '':
      err_msg = 'p is not prime'
   if not IsPrime(q) and err_msg == '':
      err_msg = 'q is not prime'

   if e == '':
      e = str(GenRandPrime(phi_n))

   if not e.isdigit() and err_msg == '':
      err_msg = 'e must be a number'
   e = int(e)
   if e <= 1  and err_msg == '':
      err_msg = 'e should be greater than 1'
   if e >= phi_n and err_msg == '':
      err_msg = 'e should be less than (p - 1) * (q - 1)'
   if GCD(e, phi_n) != 1 and err_msg == '':
      err_msg = 'e is not coprime with (p - 1) * (q - 1)'

   #?That is isn't reqired but it is a good idea to check it.
   #TODO:Should we leave it?
   if p == q and err_msg == '':
      err_msg = 'p and q are the same that is a bad idea'

   d = ModInv(e, phi_n)
   e_inv = d + n #?To me that is no logical?
   return p, q, e, e_inv, n, phi_n, d, err_msg


def encrypt(n, e, M):
   err_msg=''
   if M == '':
      err_msg = 'Empty message'
   if not isinstance(M, str):
      err_msg = 'M must be a string'
   
   TrancationLen= floor(log(n ,256))
   M = list(M)
   M = [''.join(M[i:i+TrancationLen]) for i in range(0, len(M), TrancationLen)]
   C = [Encrypt(m, n, e) for m in M]
   C = ''.join(C)
   return C, err_msg


def decrypt(n, d, C):
   err_msg = ''
   if C == '':
      err_msg = 'Empty message'
   if not isinstance(C, str):
      err_msg = 'C must be a string'
   
   TrancationLen= log(n ,256)
   C = list(C)
   C = [''.join(C[i:i+TrancationLen]) for i in range(0, len(C), TrancationLen)]
   M = [Decrypt(c, n, d) for c in C]
   M = ''.join(M)
   return M, err_msg