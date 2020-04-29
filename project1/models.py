from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
      __tablename__ = "users"
      id = db.Column(db.Integer, primary_key=True)
      email = db.Column(db.String, nullable=False)
      password = db.Column(db.String, nullable=False)
      timestamp = db.Column(db.String,nullable=False)

class Book(db.Model):
      __tablename__="books"
      id = db.Column(db.Integer, primary_key=True)
      isbn = db.Column(db.String, nullable=False)
      title = db.Column(db.String, nullable=False)
      author = db.Column(db.String, nullable=False)
      year_published = db.Column(db.Integer, nullable=False)
      review = db.Column(db.String, nullable=True)




