from flask import Flask, render_template, request
import sqlite3
import pandas as pd
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/saurabhlaptop/data/projects/flask_sb/images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])



app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/', methods=['GET','POST'])
def home():
        return render_template('admission_form.html')


@app.route('/admission-data', methods=['GET','POST'])
def admission_data():
        name=request.form.get('name')
        contact=request.form.get('contact')
        address=request.form.get('address')
        date=request.form.get('date')
        f = request.files['file']
        f.save(secure_filename(f.filename))
        #file = request.files['photo']
        #upload = Upload(filename=file.filename, data=file.read())
        #filename = secure_filename(file)
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('admission_form.html')
    



if __name__ == "__main__" :
    app.run(debug=True,host='0.0.0.0')


