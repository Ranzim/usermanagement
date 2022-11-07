from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
datetime import datetime

from usermanagement import app
# add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////User.db'
# initalize the database
db = SQLAlchemy(app)
# create model

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.route("/")
def signup():
    return  render_template('signup.html')

@app.route("/login")
def login():
    return  render_template('login.html')


