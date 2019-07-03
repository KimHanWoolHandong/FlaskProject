from flask import Flask, request
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

#상태 변화를 줄 수있음


@app.route('/projects/')
def do_the_login():
    return 'The project page'

@app.route('/about')
def show_the_login_form():
    return 'The about page'
