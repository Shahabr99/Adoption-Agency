from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, NumberRange, Optional, URL, AnyOf


class PetAdoptionForm(FlaskForm):
    """Create adoption form"""

    name=StringField('Pet name', validators= [InputRequired()])
    species = StringField('Species', validators=[Optional(), AnyOf(values=['cat', 'dog', 'porcupine', 'Cat', 'Dog', 'Porcupine'], message="Invalid species")])
    photo = StringField('Photo URL', validators=[URL(require_tld=True)])
    age = IntegerField('Age', validators=[InputRequired(), NumberRange(min=1, max=30)])
    notes = StringField('Notes', validators=[Optional()])