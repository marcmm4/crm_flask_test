from flask import Blueprint

blueprint = Blueprint(
    'automation_blueprint',
    __name__,
    url_prefix='/automation',
    template_folder='templates',
    static_folder='static'
)
