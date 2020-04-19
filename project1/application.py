import os
import datetime
from flask import Flask, session,render_template,request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
#engine = create_engine(os.getenv("DATABASE_URL"))
#db = scoped_session(sessionmaker(bind=engine))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register",methods =["GET","POST"])
def register():
    if request.method=="POST" :
        var=request.form.get("email")
        var1=request.form.get("psw")
        timestamp=datetime.datetime.now()
        user = User(email=var,password=var1,timestamp=timestamp)
        db.session.add(user)
        db.session.commit()
        if not var:
            text = "Enter email address"
            return render_template("gmails.html",gmails=text,msg="ERROR")
        elif not var1:
            text = "Enter password"
            return render_template("gmails.html", gmails=text,msg ="ERROR")
        else:
            return render_template("gmails.html",msg="SUCCESS")
    return render_template("register.html")


def main():
    app.app_context().push()
    db.create_all()


if __name__ == "__main__":
    main()