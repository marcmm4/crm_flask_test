from flask import Blueprint

blueprint = Blueprint(
    'users_blueprint',
    __name__,
    url_prefix='/management/users',
    template_folder='templates',
    static_folder='static'
)
