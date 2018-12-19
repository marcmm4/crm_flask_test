from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField

## login and registration


class LoginForm(FlaskForm):
    username = TextField('Username', id='username_login')
    password = PasswordField('Password', id='pwd_login')


class CreateAccountForm(FlaskForm):
    username = TextField('Username', id='username_create')
    email = TextField('Email')
    password = PasswordField('Password', id='pwd_create')


class ModifyAccountForm(FlaskForm):
    id = TextField('Id')
    username = TextField('Username', id='username_create')
    email = TextField('Email')
    firstname = TextField('Firstname')
    lastname = TextField('Lastname')
    password = PasswordField('Password', id='pwd_create')
