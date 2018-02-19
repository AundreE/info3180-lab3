from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class Myform(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    email = StringField('E-mail',validators=[DataRequired()])
    address = StringField('Address',validators=[DataRequired()])
    subject = StringField('Subject',validators=[DataRequired()])
    message = TextAreaField('Message',validators=[DataRequired()])

    