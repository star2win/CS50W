import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_name = os.environ.get("DB_NAME")

DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(DATABASE_URL)
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights = db.execute(text("SELECT * FROM flights")).fetchall()
    return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
    """Book a flight."""
    
    # Get form information
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")
    
    if db.execute(text("SELECT * FROM flights WHERE id = :id"), {"id": flight_id}).rowcount == 0:
        return render_template("error.html", message="No such flight with that id.")
    db.execute(text("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)"),
                    {"name": name, "flight_id": flight_id})
    db.commit()
    return render_template("success.html", message="You have successfully booked your flight!")

@app.route("/flights")
def flights():
    """Lists all flights."""
    flights = db.execute(text("SELECT * FROM flights")).fetchall()
    return render_template("flights.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """Lists details about a single flight."""

    # Make sure flight exists.
    flight = db.execute(text("SELECT * FROM flights WHERE id = :id"), {"id": flight_id}).fetchone()
    if flight  is None:
        return render_template("error.html", message="No such flight.")
    
    # Get all passengers.
    passengers = db.execute(text("SELECT name FROM passengers WHERE flight_id = :flight_id"), {"flight_id": flight_id})
    return render_template("flight.html", flight=flight, passengers=passengers)
