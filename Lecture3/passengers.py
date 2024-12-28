import os

from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker


db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_name = os.environ.get("DB_NAME")

DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(DATABASE_URL)
db = scoped_session(sessionmaker(bind=engine))

def main():

    # List all flights
    flights = db.execute(text("SELECT id, origin, destination, duration FROM flights")).fetchall()
    for flight in flights:
        print(f"Flight {flight.id}: {flight.origin} to {flight.destination} in {flight.duration} minutes.")

    #Prompt user to choose a flight
    flight_id = int(input("\nFlight ID: "))
    flight = db.execute(text("SELECT origin, destination, duration FROM flights WHERE id = :id"),
                        {"id": flight_id}).fetchone()

    if flight is None:
        print("Error: No such flight.")
        return
    
    #List passengers
    passengers = db.execute(text("SELECT name FROM passengers WHERE flight_id = :flight_id"),
                            {"flight_id": flight_id}).fetchall()
    
    if not passengers:
        print(f"No passengers on flight #{flight_id}")
        return
    
    print("\nPassengers:")
    for passenger in passengers:
        print(passenger.name)

    


if __name__ == "__main__":
    main()