from flask import Flask, url_for, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

def do_the_login():
    return 'do_the_login()'

def show_the_login_form():
    print(url_for('static', filename='styles.css'))
    return 'show_the_login_form()'
'''
with app.test_request_context():
    print(url_for('static', filename='styles.css'))'''