from flask import Flask, session, redirect, url_for, escape, request
from flask import make_response, render_template

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/', methods=['GET', 'POST'])
def index():
    if not 'username' in session:
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            return redirect(url_for('logout'))
        return 'Logged in as %s' % escape(session['username']) + '''
            <form method="post">
            
                <p><input type=submit value=Logout>
            </form>
        '''




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return 'You are not logged in' + '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))