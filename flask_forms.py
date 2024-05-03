from flask_wtf import FlaskForm, CSRFProtect
from flask import Flask, render_template, request, redirect, url_for
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length

app = Flask(__name__) 
csrf = CSRFProtect(app)

class sign_up_form(FlaskForm):
    username = StringField('Enter username', validators=[DataRequired()])
    password = StringField('Enter password', validators=[DataRequired()])
    organization = StringField('Enter your organization ID', validators=[DataRequired()])
    submit = SubmitField('Submit')

class log_in_form(FlaskForm):
    username = StringField('Enter username', validators=[DataRequired()])
    password = StringField('Enter password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class create_new_org_form(FlaskForm):
    username = StringField('Enter username', validators=[DataRequired()])
    password = StringField('Enter password', validators=[DataRequired()])
    organization = StringField('Enter your new organization name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class create_user_form(FlaskForm):
    username = StringField('Enter username', validators=[DataRequired()])
    password = StringField('Enter password', validators=[DataRequired()])
    organization = StringField('Enter your organization', validators=[DataRequired()])
    is_admin = BooleanField('Is Admin?')
    submit = SubmitField('Submit')

class delete_user_form(FlaskForm):
    username = StringField('Enter username', validators=[DataRequired()])
    submit = SubmitField('Submit')