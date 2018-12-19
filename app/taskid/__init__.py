from flask import Blueprint

blueprint = Blueprint(
    'taskid_blueprint',
    __name__,
    url_prefix='/task/taskid',
    template_folder='templates',
    static_folder='static'
)
