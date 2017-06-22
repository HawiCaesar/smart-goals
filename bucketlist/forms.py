from flask_wtf import FlaskForm

from wtforms import StringField, BooleanField, PasswordField, TextAreaField, SubmitField

from wtforms.validators import DataRequired, Email, EqualTo

class SignUpForm(FlaskForm):
    fullname = StringField('Fullname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),
                                                                     EqualTo('password')])

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class BucketlistForm(FlaskForm):
    bucketlistname = StringField('Bucketlist name', validators=[DataRequired()])
    simple_description = TextAreaField("Simple Description", validators=[DataRequired()])
    submit = SubmitField("Add Bucketlist")
