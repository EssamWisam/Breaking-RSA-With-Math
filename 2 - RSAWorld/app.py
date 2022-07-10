from flask import Flask, request, render_template, redirect
from library import sign_up, encrypt, decrypt, Str2Num, Num2Str, ModExp, ModInv
import subprocess
app = Flask(__name__)

PU = (-1, -1)
PR = -1
name = ''

cipher_text = -1
two_e = -1;
hack_text = -1;
d_hack_text = -1;        
hacked_msg = -1;
real_msg = -1;

opened = False

def t(stringo):
    return (stringo[:32] + '...') if len(stringo) > 32 else stringo

def check_long(stringo):
    return 1 if len(stringo) > 32 else 0


@app.route('/', methods=['POST', 'GET'])
def sign_up_page():
    global PU
    global PR
    global name
    if request.method == 'POST':
        name = request.form["name"]
        p = request.form["p"]
        q = request.form["q"]
        e = request.form["e"]
        p, q, e, e_inv, n, phi_n, d, err_msg = sign_up(p, q, e)

        if err_msg == '':
            PU = (e, n)
            PR = d
            return render_template('index.html', good_input=True, err_msg=err_msg, submitted=True, p=t(str(p)), q=t(str(q)), e=t(str(e)), n=t(str(n)), phi_n=t(str(phi_n)), d=t(str(d)), e_inv=t(str(e_inv)), p_minus1=t(str(p-1)), q_minus1 = t(str(q-1)), check_long=check_long(str(n)))
        else:
            return render_template('index.html', good_input=False, err_msg=err_msg, submitted=True)

    elif request.method == 'GET':
        PU = (-1, -1)
        PR = -1
        return render_template('index.html')




@app.route('/home', methods=['POST', 'GET'])
def home_page():
    global PU, PR, name, two_e, hack_text, d_hack_text, hacked_msg, real_msg, cipher_text, opened
    if request.method == 'POST':
        enc_msg, dec_msg = '', ''
        
        if  "encrypt" in request.form:
            M = request.form["plaintext"]
            enc_msg, err_msg = encrypt(PU[1], PU[0], M)
            
            for i in range(len(enc_msg)):
                enc_msg[i]=str(Str2Num(enc_msg[i]))
            enc_msg = '\n'.join(enc_msg)

            file_object = open('static/channel-in.txt', 'a')
            file_object.write(enc_msg + '\n')
            file_object.close()

            if err_msg == '':
                return render_template('home.html', good_input=True, err_msg=err_msg, enc_input=True, dec_input=False, submitted=True, enc_msg = enc_msg, dec_msg = dec_msg)
            else:
                return render_template('home.html', good_input=False, err_msg=err_msg, enc_input=True, dec_input=False, submitted=True)
        elif "decrypt" in request.form:
            C = request.form["ciphertext"]
            C_arr = C.split(' ')
            for C in C_arr:
                if not C.isdigit():
                    err_msg = 'C must be a number'
                    break
                else:
                    C = Num2Str(int(C))
                    dec_msg_temp, err_msg = decrypt(PU[1], PR, C)
                    dec_msg += dec_msg_temp
                    if err_msg != '':
                        break

            if err_msg == '':
                return render_template('home.html', good_input=True, dec_input=True, enc_input=False, err_msg=err_msg, submitted=True, enc_msg = enc_msg, dec_msg = dec_msg)
            else:
                return render_template('home.html', good_input=False, dec_input=True, enc_input=False, err_msg=err_msg, submitted=True)
        else:                                                       # CCA Attack
                return render_template('home.html', hacked=True)

    elif request.method == 'GET':
        if PR != -1:
            if not opened:
                subprocess.Popen(['pythonw', 'Script.py', name, str(PU[1]), str(PU[0]), str(PR)])
                #opened = True
            n = PU[1]
            e = PU[0]
            d = PR
            with open('./static/channel-in.txt', 'r') as f:
                cipher_text = int(f.readlines()[-1])
            two_e = ModExp(2, e, n );
            hack_text = (cipher_text * two_e) % n; 
            d_hack_text = ModExp(hack_text, d, n);
            r_inv = ModInv(2, n)
            hacked_msg_n = (r_inv * d_hack_text) % n
            hacked_msg =  Num2Str(hacked_msg_n)
            print(hacked_msg)
            real_msg = ModExp(cipher_text, d, n);
            return render_template('home.html', n=n, e=e, d=d, name=name, cipher_text=cipher_text,
            two_e=two_e, hack_text=hack_text, hack_text_str=str(hack_text), d_hack_text=d_hack_text, hacked_msg=hacked_msg,hacked_msg_n=hacked_msg_n, real_msg=real_msg)
        else:
            return redirect("/", code=302)


if __name__ == '__main__':
    app.run(port=5000)