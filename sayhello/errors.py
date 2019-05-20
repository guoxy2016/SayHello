from flask import render_template

from sayhello import app


@app.errorhandler(404)
def not_found(e):
    return render_template('errors/errors.html', code=e.code, name=e.name, description=e.description), 404


@app.errorhandler(500)
def server_err(_):
    return render_template('errors/500.html'), 500
