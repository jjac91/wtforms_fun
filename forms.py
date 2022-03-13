##from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    name = StringField("Pet name", validators=[InputRequired()])
    species = SelectField("Pet species", choices=[(
        'Cat', 'Cat'), ('Dog', 'Dog'), ('Porcupine', 'Porcupine')], validators=[InputRequired()])
    photo_url = StringField("Picture Url", validators=[Optional(), URL()])
    age = IntegerField("Pet age", validators=[Optional(), NumberRange(0, 30)])
    notes = TextAreaField("Notes", validators=[Optional()])


class EditPetForm(FlaskForm):
    photo_url = StringField("Picture Url", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available?")
