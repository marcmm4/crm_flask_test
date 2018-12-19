from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField

## login and registration

class ModifyUserForm(FlaskForm):
    id = TextField('Id')
    username = TextField('Username', id='username_create')
    email = TextField('Email')
    firstname = TextField('Firstname')
    lastname = TextField('Lastname')
    password = PasswordField('Password', id='pwd_create')