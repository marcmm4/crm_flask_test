from flask import Blueprint

blueprint = Blueprint(
    'management_blueprint',
    __name__,
    url_prefix='/management',
    template_folder='templates',
    static_folder='static'
)
