from os import environ, path

basedir = path.abspath(path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'key'
    SQLITE = 'sqlite:///'
    DATABASE_NAME = 'database.db'
    SQLALCHEMY_DATABASE_URI = SQLITE + DATABASE_NAME
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #Celery configuration
    CELERY_BROKER_URL = 'redis://10.151.150.245:6379/0'
    CELERY_RESULT_BACKEND = 'redis://10.151.150.245:6379/0'

    # THEME SUPPORT
    #  if set then url_for('static', filename='', theme='')
    #  will add the theme name to the static URL:
    #    /static/<DEFAULT_THEME>/filename
    # DEFAULT_THEME = "themes/dark"
    DEFAULT_THEME = None


class ProductionConfig(Config):
    DEBUG = False

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        environ.get('GENTELELLA_DATABASE_USER', 'gentelella'),
        environ.get('GENTELELLA_DATABASE_PASSWORD', 'gentelella'),
        environ.get('GENTELELLA_DATABASE_HOST', 'db'),
        environ.get('GENTELELLA_DATABASE_PORT', 5432),
        environ.get('GENTELELLA_DATABASE_NAME', 'gentelella')
    )


class DebugConfig(Config):
    DEBUG = True


config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
