from flask import Flask, url_for, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_static_url()

def do_the_login():
    return 'do_the_login()'

def show_the_static_url():
    url = (url_for('static', filename='styles.css'))
    print(url)                   # print in console
    return url                   # print in html page
'''
with app.test_request_context():
    print(url_for('static', filename='styles.css'))
'''