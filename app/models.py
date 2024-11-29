from . import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    is_complete = db.Column(db.Boolean, default=False)
