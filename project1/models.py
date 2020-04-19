from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
      __tablename__ = "users"
      id = db.Column(db.Integer, primary_key=True)
      email = db.Column(db.String, nullable=False)
      password = db.Column(db.String, nullable=False)
      timestamp = db.Column(db.String,nullable=False)



