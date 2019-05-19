from flask import render_template

from sayhello import app


@app.errorhandler(404)
def not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def server_err(e):
    return render_template('errors/500.html'), 500
