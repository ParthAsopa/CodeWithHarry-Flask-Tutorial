from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/blog'
db = SQLAlchemy(app)

class Contacts(db.Model):
    srno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)
    message = db.Column(db.String(80), nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/post.html')
def post():
    return render_template('post.html')

@app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        #add entry to the database.
        name = request.form.get("name")
        phone = request.form.get("phone")
        message = request.form.get("message")
        email = request.form.get("email")
        date = datetime.datetime.now()
        entry=Contacts(name=name, email=email, phone=phone, message=message, date=date)
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')

app.run(debug=True)