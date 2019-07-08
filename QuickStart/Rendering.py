from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('register.html', name=name)

#html파일을 렌더링해서 넣을 수있음 이 파일 안에 있는 것임
#template 파일은 그 파일 있는 디렉토리에 templates라는 디렉토리가 필요함. 거기 안에 html파일을 넣어야함