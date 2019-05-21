from sayhello import app, db

app.config.update(
    TESTING=True,
    WTF_CSRF_ENABLED=False,
    SQLALCHEMY_DATABASE_URI='sqlite:///:memory:'
)
db.create_all()


