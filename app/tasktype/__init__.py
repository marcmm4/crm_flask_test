from flask import Blueprint

blueprint = Blueprint(
    'tasktype_blueprint',
    __name__,
    url_prefix='/task/tasktype',
    template_folder='templates',
    static_folder='static'
)
