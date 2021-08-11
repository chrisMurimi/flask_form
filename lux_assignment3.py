from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from model import Result

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('home.html', title = "chris form")

@app.route('/form', methods = ["POST"])
def form():
    first_name = request.form.get('First name')
    second_name = request.form.get('Second name')
    surname = request.form.get('surname')
    return render_template('form.html', title = "thank you")

if __name__ == '__main__':
    app.run(debug=True)