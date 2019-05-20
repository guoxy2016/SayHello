import unittest

import click
from faker import Faker

from sayhello import db, app
from sayhello.models import Message

fake = Faker('zh_CN')


@app.cli.command()
@click.option('--drop', is_flag=True, help='drop after create')
def init_db(drop):
    """initialize database."""
    if drop:
        click.confirm('All data well be delete, do you want to continue?', abort=True)
        db.drop_all()
        click.echo('drop all database.')
    db.create_all()
    click.echo('database initialized')


@app.cli.command(name='forge')
@click.option('--count', default=20, help='Quantity of messages, default is 20.')
def forge(count):
    """Generate faker messages"""
    click.echo('Generating %d messages ...' % count)
    for i in range(count):
        message = Message()
        message.username = fake.name()
        message.body = fake.text()
        message.timestamp = fake.date_time_this_month()
        db.session.add(message)
    db.session.commit()
    click.echo('Done!')


@app.cli.command()
def test():
    """Run unit tests."""
    test_site = unittest.TestLoader().discover('test_sayhello')
    unittest.TextTestRunner(verbosity=2).run(test_site)
