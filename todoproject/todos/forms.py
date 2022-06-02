from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TodosForm(FlaskForm):

    text = StringField('Todo: ', validators=[DataRequired()])
    submit = SubmitField('Submit')
