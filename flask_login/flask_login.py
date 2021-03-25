from flask import Flask, url_for, request, render_template
from markupsafe import escape
import subprocess

#from predefines import host, port
host = '0.0.0.0'
port = '5000'
import webbrowser

app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        print('POST')
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        if valid_login(username, password):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
            print(error)
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html')

def valid_login(name,pwd):
    print(name,pwd)
    return name=='jd54' and pwd=='test'

def log_the_user_in(name):
    print(name)
    return render_template('success.html')

# under apache
'''
if __name__ == '__main__': 
    app.run(host=host, port=port, debug=True)
    # launch flask web page 
    webbrowser.open("http://localhost:1234", new=1)
'''
