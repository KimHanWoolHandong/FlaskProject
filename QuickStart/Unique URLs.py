from flask import Flask
app = Flask(__name__)

@app.route('/projects/')
def projects():
    return 'The project page'

#폴더처럼 사용가능

@app.route('/about')
def about():
    return 'The about page'

#파일의 pathname임. 여기에 /를 붙이면 Not found가 생김