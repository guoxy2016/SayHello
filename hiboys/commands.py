import click

from hiboys import db, app
from hiboys.models import Message


@app.cli.command(name='init_db')
@click.option('--drop', is_flag=True, help='drop after create')
def init_db(drop):
    """initialize database."""
    if drop:
        click.confirm('Drop database?', abort=True)
        db.drop_all()
        click.echo('drop all database.')
    db.create_all()
    click.echo('database initialized')


@app.cli.command(name='fake')
@click.option('--count', default=20, help='Quantity of messages, default is 20.')
def faker_data(count):
    """Generate faker messages"""
    from faker import Faker

    fake = Faker('zh_CN')
    click.echo('Generating...')
    for i in range(count):
        message = Message()
        message.username = fake.name()
        message.body = fake.text()
        message.timestamp = fake.date_time_this_month()
        db.session.add(message)
    db.session.commit()
    click.echo('Done.')
    click.echo('Complete %s message' % count)


