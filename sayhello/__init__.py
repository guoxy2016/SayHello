from flask import Flask
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy, get_debug_queries

app = Flask('sayhello')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.config.from_pyfile('settings.py')

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
toolbar = DebugToolbarExtension(app)

from sayhello import views, commands, errors  # noqa


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, bootstrap=bootstrap)


@app.after_request
def query_profiler(response):
    for q in get_debug_queries():
        print('%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n' % (
        q.statement, q.parameters, q.start_time, q.end_time, q.duration, q.context))
        print('-' * 120)
    return response
