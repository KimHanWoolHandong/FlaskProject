from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

#set FLASK_APP = "hello.py"
#python -m flask run

