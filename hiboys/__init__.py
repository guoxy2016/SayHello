import click
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask('hiboys')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.config.from_pyfile('settings.py')

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

from hiboys import views


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, bootstrap=bootstrap)


@app.cli.command(name='init-db')
@click.option('--drop', is_flag=True, help='drop after create')
def init_db(drop):
    """initialize database."""
    if drop:
        click.confirm('Drop database?', abort=True)
        db.drop_all()
        click.echo('drop all database.')
    db.create_all()
    click.echo('database initialized')
