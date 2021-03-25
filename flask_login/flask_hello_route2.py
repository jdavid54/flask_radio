from flask import Flask
app = Flask(__name__)

# https://flask.palletsprojects.com/en/1.1.x/quickstart/
# http://localhost:5000/route2

@app.route('/route2')
def hello_world():
    return 'Hello, World!'