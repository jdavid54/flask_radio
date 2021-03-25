from flask import Flask, url_for, request, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/hello/')        #http://localhost:5000/hello/
@app.route('/hello/<name>')  #http://localhost:5000/hello/jd54
def hello(name=None):
    return render_template('hello.html', name=name)