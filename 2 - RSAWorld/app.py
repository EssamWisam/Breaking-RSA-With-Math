from flask import Flask, request, render_template, redirect
from library import sign_up, encrypt, decrypt, ConvertToInt,ConvertToStr
import subprocess
app = Flask(__name__)

PU = (-1, -1)
PR = -1
name = ''

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
    global PU
    global PR
    global name
    if request.method == 'POST':
        enc_msg, dec_msg = -1, -1
        
        if  "encrypt" in request.form:
            M = request.form["plaintext"]
            enc_msg, err_msg = encrypt(PU[1], PU[0], M)
            
            for i in range(len(enc_msg)):
                enc_msg[i]=str(ConvertToInt(enc_msg[i]))
            enc_msg = '\n'.join(enc_msg)

            if err_msg == '':
                return render_template('home.html', good_input=True, err_msg=err_msg, enc_input=True, dec_input=False, submitted=True, enc_msg = enc_msg, dec_msg = dec_msg)
            else:
                return render_template('home.html', good_input=False, err_msg=err_msg, enc_input=True, dec_input=False, submitted=True)
        elif "decrypt" in request.form:
            C = request.form["ciphertext"]

            if not C.isdigit():
                err_msg = 'C must be a number'
            else:
                C = ConvertToStr(int(C))
                dec_msg, err_msg = decrypt(PU[1], PR, C)

            if err_msg == '':
                return render_template('home.html', good_input=True, dec_input=True, enc_input=False, err_msg=err_msg, submitted=True, enc_msg = enc_msg, dec_msg = dec_msg)
            else:
                return render_template('home.html', good_input=False, dec_input=True, enc_input=False, err_msg=err_msg, submitted=True)
        else:                                                       # CCA Attack
                return render_template('home.html', hacked=True)

    elif request.method == 'GET':
        if PR != -1:
            subprocess.Popen(['pythonw', 'Script.py', name, str(PU[1]), str(PU[0]), str(PR)])
            return render_template('home.html', n=PU[1], e=PU[0], d=PR, name=name)
        else:
            return redirect("/", code=302)



if __name__ == '__main__':
    app.run(debug=True)

