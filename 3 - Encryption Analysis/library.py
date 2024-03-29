from ipynb.fs.full.Library import GCD, ModInv, IsPrime, GenRandPrime, Encrypt, Decrypt, log, floor, ConvertToStr, ConvertToInt

def sign_up(size,p='', q='', e=''):
   BITSNUM=size
   if p == '':
      if e=='':
         if q == '':
            p = str(GenRandPrime(BITSNUM))
         else:
            p = str(GenRandPrime(int(log(int(q), 2)+1)))
      else:
         if int(e)%2 !=0:
            if q == '':
               p = str(GenRandPrime(BITSNUM))
               while GCD(int(p)-1, int(e)) != 1:
                  p = str(GenRandPrime(BITSNUM))
            else:
               p = str(GenRandPrime(int(log(int(q), 2)+1)))
               while GCD(int(p)-1, int(e)) != 1:
                  p = str(GenRandPrime(int(log(int(q), 2)+1)))

   if q == '':
      if e=='':
         if p == '':
            q = str(GenRandPrime(BITSNUM))
         else:
            q = str(GenRandPrime(int(log(int(p), 2)+1)))
      else:
         if int(e)%2 !=0:
            if p == '':
               q = str(GenRandPrime(BITSNUM))
               while GCD(int(q)-1, int(e)) != 1:
                  q = str(GenRandPrime(BITSNUM))
            else:
               q = str(GenRandPrime(int(log(int(p), 2)+1)))
               while GCD(int(q)-1, int(e)) != 1:
                  q = str(GenRandPrime(int(log(int(p), 2)+1)))


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
   if p == 2 and err_msg == '':
      err_msg = 'p must be greater than 2'
   if q == 2 and err_msg == '':
      err_msg = 'q must be greater than 2'
      
   if e == '':
      e = str(GenRandPrime(int(log(phi_n,2))))

   if not e.isdigit() and err_msg == '':
      err_msg = 'e must be a number'
   e = int(e)
   if e%2 == 0 and err_msg == '':
      err_msg = 'e must be odd'
   if e <= 1  and err_msg == '':
      err_msg = 'e should be greater than 1'
   if e >= phi_n and err_msg == '':
      err_msg = 'e should be less than φ(n)'
   if GCD(e, phi_n) != 1 and err_msg == '':
      err_msg = 'e is not coprime with φ(n)'

   #?That is isn't reqired but it is a good idea to check it.
   #TODO:Should we leave it?
   if p == q and err_msg == '':
      err_msg = 'p and q are the same that is a bad idea'

   d = ModInv(e, phi_n)
   e_inv = d + n
   return p, q, e, e_inv, n, phi_n, d, err_msg


def encrypt(n, e, M):
   err_msg=''
   if M == '':
      err_msg = 'Empty message'
   if not isinstance(M, str):
      err_msg = 'M must be a string'
   
   TruncationLen= floor(log(n ,256)) if floor(log(n ,256)) > 0 else 1
   M = list(M)
   M = [''.join(M[i:i+TruncationLen]) for i in range(0, len(M), TruncationLen)]
   C = [Encrypt(m, n, e) for m in M]
   return C, err_msg


def decrypt(n, d, C):
   err_msg = ''
   if not isinstance(C, list):
      C=[C]
   for c in C:
      if c == '':
         err_msg = 'Empty message'
   M = [Decrypt(c, n, d) for c in C]
   M = ''.join(M)
   return M, err_msg