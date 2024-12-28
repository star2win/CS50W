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
    flights = db.execute(text("SELECT origin, destination, duration FROM flights")).fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination} in {flight.duration} minutes.")

if __name__ == "__main__":
    main()