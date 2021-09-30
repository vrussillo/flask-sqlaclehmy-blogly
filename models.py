from enum import unique
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):    
    db.app = app
    db.init_app(app)


# MODELS GO BELOW

class User(db.Model):

        __tablename__ = "users"

        id = db.Column(db.Integer,
            primary_key=True,
            autoincrement=True)

        first_name = db.Column(db.String(50),
            nullable=False,
            unique=True)

        last_name = db.Column(db.String(30), 
            nullable=False,
            unique=True)

        image_url = db.Column(db.String,
            nullable=True
            )

        posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")

        @property
        def full_name(self):

                return f"{self.first_name} {self.last_name}"


class Post(db.Model):

        __tablename__ = "post"

        id = db.Column(db.Integer,
            primary_key=True,
            autoincrement=True)

        title = db.Column(db.Text,
        nullable=False,)

        content = db.Column(db.Text,
        nullable=False,)

        created_at = db.Column(db.DateTime,
        nullable=False,
        default=datetime.datetime.now)

        user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

        @property
        def friendly_date(self):

                return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")