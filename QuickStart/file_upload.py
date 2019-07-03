from flask import request
from flask import Flask
#from werkzeug.utils import secure_filename
app = Flask(__name__)

from flask import request

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')

        #f.save('/var/www/uploads/' + secure_filename(f.filename))