from flask import redirect, url_for, render_template, flash

from sayhello import app, db
from sayhello.forms import HelloForm
from sayhello.models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = HelloForm()
    if form.validate_on_submit():
        message = Message()
        message.username = form.username.data
        message.body = form.body.data
        db.session.add(message)
        db.session.commit()
        flash('发布成功')
        return redirect(url_for('index'))
    return render_template('index.html', messages=messages, form=form)
