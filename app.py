from flask import Flask, request, redirect, render_template
from models import db, connect_db, Pet
from forms import PetAdoptionForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Nedaismywifeforever'
app.config['WTF_CSRF_INCLUDES_GET'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://shahab:Codingisfun9!@localhost/adopt'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home_page():
    """Loads home page with a list of pets"""

    pets = Pet.query.all()
    return render_template('home.html', pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Loads a form for user to add a pet"""
    form = PetAdoptionForm()
    if form.validate_on_submit():
        name= form.name.data
        species = form.species.data
        photo= form.photo.data
        age = form.age.data
        notes= form.notes.data
        pet = Pet(name=name, species=species, photo_url=photo, age=age, notes=notes)

        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('petform.html', form=form)