def sign_up(p, q, e):
   #TODO: Implement RSA Key Generation
   #* If any of the 3 fields is missing then it should autogenerate it correctly
   #* Otherwise (and anyway), it should check if they are all set correctly. 
   #* The returned err_msg string should be returned empty if all is good.
   #* Otherwise, return an indicative message as to why the sign up couldn't be processed
   #* The keys from this function should be made available to the window chat script.
   #* The window chat script shouldn't go through unless it knows that sign up was successful first.
   p = int(p)
   q = int(q)
   e = int(e)
   n = p*q
   phi_n = 22
   d = 15
   err_msg = ''
   e_inv = 12
   return p, q, e, e_inv, n, phi_n, d, err_msg

   
def encrypt(n, e, M):
   #TODO: Implement RSA encryption (check GCD and inequality condition)
   #* If encryption is possible return result in c along with an empty string
   #* Otherwise, return a non-empty err_msg describing the problem
   err_msg = 'Do it right!!!!'
   C = n * e * M
   C = "LKDVKLDVSMSJKD SJDFNCKMA DA SDJKNO QWIDMOPWASDNM OKSCMD"
   return C, err_msg


def decrypt(n, d, C):
   #TODO: Implement RSA encryption (check GCD and inequality condition)
   #* If encryption is possible return result in c along with an empty string
   #* Otherwise, return a non-empty err_msg describing the problem
   err_msg = ''
   M = n * d * C
   M = """Mohamed M. Atalla was an Egyptian-American engineer, physical chemist, cryptographer, inventor and entrepreneur. He was a semiconductor pioneer who made important contributions to modern electronics. He is best known for inventing the MOSFET (metal–oxide–semiconductor field-effect transistor, or MOS transistor) in 1959 (along with his colleague Dawon Kahng), which along with Atalla's earlier surface passivation and thermal oxidation processes, revolutionized the electronics industry. He is also known as the founder of the data security company Atalla Corporation (now Utimaco Atalla), founded in 1972. He received the Stuart Ballantine Medal (now the Benjamin Franklin Medal in physics) and was inducted into the National Inventors Hall of Fame for his important contributions to semiconductor technology as well as data security.
       """
   return M, err_msg