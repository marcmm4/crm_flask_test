'''
from app.users import blueprint
from flask import render_template
from flask_login import login_required
'''

import app.celery_tasks
from flask_login import (
    login_required,
)

from flask import render_template

from app.tasktype import blueprint
from app.base.models import User




@blueprint.route('/long_task', methods=['POST'])
@login_required
def task():
    task = app.celery_tasks.long_task.apply_async()
    return task.id, 202