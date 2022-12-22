from api.app import create_app
from api.extensions import db
from flask_migrate import Migrate
from flask.cli import FlaskGroup


app = create_app()
migrate = Migrate(app, db)
cli = FlaskGroup(app)


@app.shell_context_processor
def make_shell_context():
    """Function to add instance to shell for easy debugging"""
    return dict(app=app, db=db)


@cli.command('create_db')
def create_db():
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()
