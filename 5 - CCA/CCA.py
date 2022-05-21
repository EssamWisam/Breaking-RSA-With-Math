from locale import MON_1
from ipynb.fs.full.Library import GCD, ModInv, ModExp, sign_up, Num2Str
import json
import os
import glob

def Choose_Y(C, r, n, e):
   assert GCD(r, n) == 1
   Y = (C * (ModExp(r, e, n))) % n
   return Y

def Find_M(X, r, n):
   r_inv = ModInv(r, n)
   M = (r_inv * X) % n
   return M


def CCA(p, q, e, C, permission=True):
   _, _, _, _, n, _, d, err_msg = sign_up(str(p), str(q), str(e))
   if err_msg == '':
      if C > n: return "There is no unique message corresponding to the target ciphertext (it's too long).", -1, -1
      r = 2
      while GCD(r, n) != 1:
         r += 1
      Y = Choose_Y(C, r, n, e)
      if permission:
         X =  ModExp(Y, d, n)
         M = Find_M(X, r, n)
         M_actual = ModExp(C, d, n)
         return "", M, M_actual
      else:
         return "Target denied signing.", -2, -2
   else:
      return err_msg, -3, -3
      

# Read files initially:
for filename in glob.glob(os.path.join('./Input-Tests', '*.json')):  
    with open(filename, encoding='utf-8', mode='r') as test_case:
        json_file = test_case.read().replace('\n', '')
        inp = json.loads(json_file)
        p, q, e, C = int(inp['p']), int(inp['q']), int(inp['e']), int(inp['C'])
        msg, M, M_actual = CCA(p, q, e, C)
        with open('./Output-Tests/'+filename[-6:-5]+'.txt', encoding='utf-8', mode='w') as out_test_case:
         if msg=='':
               M1 = Num2Str(M)
               M_actual1 = Num2Str(M_actual)
               out_test_case.write(f"Attack Successful, the M corresponding to C = {C} is M = {M1}. \n")      
               out_test_case.write(f"The vitctim has disclosed that indeed  M = {M_actual1} !! \n")      
               out_test_case.write(f"The numeric plaintext is: {M} = {M_actual}")      

         else:
               out_test_case.write(msg)

        
        


# Interactice Mode:
while True:

   C = input(" \n Please enter the target ciphertext: ")
   if not C.isdigit():
      print("invalid Input: it should be an integer.")
      continue
   p = input("Please enter the victim's secret prime p: ")
   if not p.isdigit():
      print("invalid Input: it should be an integer.")
      continue
   q = input("Please enter the victim's secret prime q: ")
   if not q.isdigit():
      print("invalid Input: it should be an integer.")
      continue
   e = input("Please enter the victim's public e:  ")
   if not e.isdigit():
      print("invalid Input: it should be an integer.")
      continue

   msg, M, M_actual = CCA(int(p), int(q), int(e), int(C))

   if msg=='':
      M = Num2Str(M)
      M_actual = Num2Str(M_actual)
      print(f"Attack Successful, the M corresponding to C={C} is M = {M}. ")      
      print(f"The vitctim has disclosed that indeed  M = {M_actual} !! \n")      

   else:
      print(msg)


