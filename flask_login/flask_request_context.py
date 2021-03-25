from flask import Flask, url_for, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

def do_the_login():
    print(request.method)
    return 'do_the_login()'

def show_the_login_form():
    print(request.method)
    print(url_for('static', filename='styles.css'))
    return 'show_the_login_form()'

@app.route('/hello/')
def hello_world():
    return 'Hello, World!'

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    print(request.path)
    assert request.method == 'POST'
    print(request.method)