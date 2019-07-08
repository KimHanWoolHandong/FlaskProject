from flask import request
from flask import Flask
from flask import make_response
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
#'username'이라는 쿠키 가져오기.
#get함수를 쓴다


@app.route('/set')
def set():
    resp = make_response(render_template('register.html'))
    resp.set_cookie('username', 'the username')
    return resp
#쿠키 저장하기
#set_cookie를 쓴다