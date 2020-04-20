import os
import datetime
from flask import Flask, session,render_template,request,redirect,url_for
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
        users1= User.query.all()
        for user in users1:
            if var==user.email:
                return "<h2 Style='color: red;text-align:center'>You already have registered !Please Login </h2>"       
        if not var:
            text = "Enter email address"
            return render_template("gmails.html",gmails=text,msg="ERROR")
        elif not var1:
            text = "Enter password"
            return render_template("gmails.html", gmails=text,msg ="ERROR")
        else:
            user = User(email=var,password=var1,timestamp=timestamp)
            db.session.add(user)
            db.session.commit()
            return render_template("gmails.html",msg="SUCCESS")
    return render_template("register.html",flag=True)


@app.route("/admin")
def admin():
    users2=User.query.all()
    return render_template("userslist.html",name=users2)

@app.route("/auth",methods=["GET","POST"])
def userhome():
    if (request.method=="POST"):
        var=request.form.get("email")
        var1=request.form.get("psw")
        users3= User.query.all()
        for user in users3:
            if user.email==var:
                if user.password==var1:
                    session["var"]=user.email
                    return redirect(url_for('user'))
        return render_template("register.html",flag=False)
    if (request.method=="GET"):
        return redirect(url_for('register'))

@app.route("/logout")
def sessiontimeout():
    session.pop("var",None)
    return redirect(url_for('register'))

@app.route("/user")
def user():
    if session.get("var") is not None:
        return render_template("user.html")
    return redirect(url_for('register'))

def main():
    app.app_context().push()
    db.create_all()


if __name__ == "__main__":
    main()