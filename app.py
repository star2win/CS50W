import datetime
from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
         note = request.form.get("note")
         #notes.append(note)
         session["notes"].append(note)
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    #new_year = True
    return render_template("index.html", new_year=new_year, notes=session["notes"])

@app.route("/bye")
def bye():
    headline = "Goodbye!"
    return render_template("bye.html", headline=headline)

@app.route("/names")
def names():
    names = ["Alice", "Bob", "Charlie", "David"]
    return render_template("names.html", names=names)

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/doublemore")
def doublemore():
    return render_template("doublemore.html")

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)