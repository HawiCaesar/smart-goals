from flask_wtf import FlaskForm

from wtforms import StringField, BooleanField, PasswordField

from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
    fullname = StringField('Fullname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])