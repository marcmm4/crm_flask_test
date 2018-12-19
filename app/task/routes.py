'''
from app.users import blueprint
from flask import render_template
from flask_login import login_required
'''

from flask_login import (
    login_required,
)

from flask import render_template

from app.task import blueprint
from app.base.models import User


@blueprint.route('/<template>', methods=['GET', 'POST'])
@login_required
def route_template(template):
    users = User.query.all()
    return render_template(template + '.html', users=users)
