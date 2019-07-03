from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'
    # session의 username을 확인해서 없으면 안되어있다고, 있으면 Logged in as로 넘어감

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''
#input된 내용을 session의 dir로 넣은뒤 post상태로 변화되면 index로 돌아가게 만듦
# form method를 통해서 상태를 변화할 수 있음

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))