from flask import Flask
from .errors import errors
from .views import db_test
from .extensions import db, ma, migrate
import os


def create_app(test_config=None):
    """Creating application instance"""

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        """Update the configuration if test_config is given """
        app.config.update(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return 'hello wolrd'

    # registeriingg blueprint
    app.register_blueprint(db_test)
    app.register_blueprint(errors)

    # registering extensiions
    extensions(app)

    return app


def extensions(app):
    """
    Function registering each extension the pproject depend on
    :param app: Flask instance
    :return : None
    """
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    return None
