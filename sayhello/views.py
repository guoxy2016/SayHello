from flask import redirect, url_for, render_template, flash, request, current_app

from sayhello import app, db
from sayhello.forms import HelloForm
from sayhello.models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, int)
    per_page = current_app.config['SAYHELLO_PER_PAGE']
    pagination = Message.query.order_by(Message.timestamp.desc()).paginate(page, per_page)
    messages = pagination.items
    form = HelloForm()
    if form.validate_on_submit():
        message = Message()
        message.username = form.username.data
        message.body = form.body.data
        db.session.add(message)
        db.session.commit()
        flash('发布成功')
        return redirect(url_for('index', page=1))
    return render_template('index.html', messages=messages, form=form, pagination=pagination)
