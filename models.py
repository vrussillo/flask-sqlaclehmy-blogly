from enum import unique
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):    
    db.app = app
    db.init_app(app)


# MODELS GO BELOW

class User(db.Model):
    __tablename__ = "users"


    def __repr__(self):
        p = self
        return f"<Pet id={p.id} name={p.name} species={p.species} hunger={p.hunger}>"

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

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"
