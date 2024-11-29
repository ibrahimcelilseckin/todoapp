import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mreliteE@-_-')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'postgresql://app.db',
        'postgresql://postgres:200420@localhost/todo_app'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False