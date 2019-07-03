from flask import abort, redirect,url_for
from flask import render_template
from flask import make_response
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(404)
    this_is_never_executed()


@app.errorhandler(404)
def page_not_found(error):
    resp = make_response(render_template('page_not_found.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

#redirect errors에서 똑같은 예제를 make_response로 객체를 만들어 보여줄 수 있음
