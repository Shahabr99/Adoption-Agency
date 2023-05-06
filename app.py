from flask import Flask, redirect, render_template, request
from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt';
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

with app.app_context():
    db.create_all()


@app.route('/')
def show_pets():
    """Shows a list of pets available"""

    pets = Pet.query.filter(Pet.available == True).all()

    return render_template('home.html', pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Showing form for adding pets"""
    return render_template('petform.html')