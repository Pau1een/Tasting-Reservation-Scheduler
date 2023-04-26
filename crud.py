"""CRUD operations."""

from model import db, User, Reservation, connect_to_db
from datetime import datetime, timedelta 


def create_user(username):
    """Create a new user and add it to database."""

    # Check if the username already exists
    if User.query.filter_by(username=username).first():
        raise ValueError("Username already exists")
    
    new_user= User(username=username)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def get_user(username):
    """Return a user."""

    return User.query.filter(User.username == username).first()



def get_reservations(username):
    """Return all reservations by username."""

    return Reservation.query.filter_by(username = username).all()



def get_available_timeslots(date):
    taken_timeslots = Reservation.query.filter_by(date=date).all()
    timeslots = []
    start_time = datetime(date.year, date.month, date.day, 9, 0, 0)
    end_time = datetime(date.year, date.month, date.day, 17, 30, 0)
    current_time = start_time
    while current_time < end_time:
        if current_time not in [r.start_time for r in taken_timeslots]:
            timeslots.append(current_time)
        current_time += timedelta(minutes=30)

    return timeslots



def create_reservation(username, date, start_time, end_time):
    """ Create a reservation. """

    new_reservation = Reservation.query.filter(Reservation.username==username, Reservation.date==date, Reservation.start_time==start_time, Reservation.end_time==end_time).first()
    print(new_reservation)
    db.session.add(new_reservation)
    db.session.commit()

    return new_reservation



if __name__ == "__main__":
    from server import app

    connect_to_db(app)