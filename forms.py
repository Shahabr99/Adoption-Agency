from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Email, Optional


class PetAdoptionForm(FlaskForm):
    """Create adoption form"""

    name=StringField('Pet name', validators= [InputRequired()])
    species = StringField('Species', validators=[Optional()])
    photo = StringField('Photo URL')
    age = IntegerField('Age', validators=[InputRequired()])
    notes = StringField('Notes', validators=[Optional()])