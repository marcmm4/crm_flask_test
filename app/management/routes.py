'''
from app.users import blueprint
from flask import render_template
from flask_login import login_required
'''

from flask_login import (
    login_required,
)

from app import db, login_manager
from flask import render_template, request, jsonify

from app.management import blueprint
from app.base.models import User


@blueprint.route('/<template>', methods=['GET', 'POST'])
@login_required
def route_template(template):
    if "users" == str(template):
        users = User.query.all()
        return render_template(template + '.html', users=users)