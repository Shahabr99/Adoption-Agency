from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Optional


class PetAdoptionForm(FlaskForm):
    """Form for adopting pets"""

    name= StringField('Pet name', validators = [InputRequired()])
    Species= StringField('Species')
    Photo_URL= StringField('Photo')
    Age= IntegerField('Pet age')
    Notes= TextAreaField('Notes', validators = [Optional()])