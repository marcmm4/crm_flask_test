'''
from app.users import blueprint
from flask import render_template
from flask_login import login_required
'''
import app.celery_tasks
from flask_login import (
    login_required,
)
from flask import jsonify
from app.taskid import blueprint



@blueprint.route('/<template>', methods=['GET', 'POST'])
@login_required
def route_template(template):
    task_id = str(template)
    task = app.celery_tasks.celery.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)