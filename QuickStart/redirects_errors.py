from flask import abort, redirect,url_for
from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(404)
    this_is_never_executed()

#redirect로 login을 바로 가게 만듦. 하지만 abort로 바로 오류를 보내줘 다음을 실행 안하게 함

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
#숫자에 해당하는 오류가 나올때 템플렛에 해당하는 창이 뜨게 만들어줌