from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model):
    """Creating a table for pets"""

    __tablename__='pets'

    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String, nullable=False)
    species=db.Column(db.Text, nullable=True)
    photo_url=db.Column(db.String(300), nullable=True)
    age=db.Column(db.Integer, nullable=True)
    notes=db.Column(db.String(500), nullable=True)
    available= db.Column(db.Boolean, nullable=False, default=True)


def connect_db(app):
    db.app = app
    db.init_app(app)