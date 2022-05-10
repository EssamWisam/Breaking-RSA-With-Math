from flask import Flask, request, render_template, redirect
from library import sign_up, encrypt, decrypt
app = Flask(__name__)

PU = (-1, -1)
PR = -1
name = ''

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
            return render_template('index.html', good_input=True, err_msg=err_msg, submitted=True, p=p, q=q, e=e, n=n, phi_n=phi_n, d=d, e_inv=e_inv)

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
    if request.method == 'POST':
        enc_msg, dec_msg = -1, -1
        
        if  "encrypt" in request.form:
            M = request.form["plaintext"]
            enc_msg, err_msg = encrypt(PU[1], PU[0], M)
            if err_msg == '':
               return render_template('home.html', good_input=True, err_msg=err_msg, enc_input=True, dec_input=False, submitted=True, enc_msg = enc_msg, dec_msg = dec_msg)
            else:
                return render_template('home.html', good_input=False, err_msg=err_msg, enc_input=True, dec_input=False, submitted=True)
        elif "decrypt" in request.form:
            C = request.form["ciphertext"]
            dec_msg, err_msg = decrypt(PU[1], PR, C)

            if err_msg == '':
                return render_template('home.html', good_input=True, dec_input=True, enc_input=False, err_msg=err_msg, submitted=True, enc_msg = enc_msg, dec_msg = dec_msg)
            else:
                return render_template('home.html', good_input=False, dec_input=True, enc_input=False, err_msg=err_msg, submitted=True)
        else:                                                       # CCA Attack
                return render_template('home.html', hacked=True)

    elif request.method == 'GET':
        if PR != -1:
            return render_template('home.html', n=PU[1], e=PU[0])
        else:
            return redirect("/", code=302)



if __name__ == '__main__':
    app.run(debug=True)

