from datetime import datetime

from hiboys import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True)
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
