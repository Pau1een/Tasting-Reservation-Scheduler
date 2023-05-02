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


def get_user_by_username(username):
    """Return a user object by username"""

    return User.query.filter_by(username=username).first()


def get_reservations(username):
    """Return all reservations by username."""

    return Reservation.query.filter_by(username = username).all()


def get_available_timeslots(date):
    taken_timeslots = Reservation.query.filter_by(date=date).all()
    timeslots = []
    start_time = datetime(date.year, date.month, date.day, 9, 0, 0)
    while start_time:
        if current_time not in [r.start_time for r in taken_timeslots]:
            timeslots.append(current_time)
        current_time += timedelta(minutes=30)

    return timeslots


def create_reservation(username, date, start_time):
    """Create a reservation."""

    # Check if the reservation already exists
    reservation = Reservation.query.filter_by(username=username, date=date, start_time=start_time).first()
    if reservation:
        raise ValueError("Reservation already exists")
    # Create a new reservation
    reservation = Reservation(username=username, date=date, start_time=start_time)
    db.session.add(reservation)
    db.session.commit()

    return reservation


def get_reservation_by_date_time(date, start_time):
    """Return date and time"""
    return Reservation.query.filter_by(date=date,
                                        start_time=start_time).first()

def user_has_reservation_on_date(user, date):
    """Check if user has a reservation scheduled for a specific date."""

    reservation = Reservation.query.filter_by(user=user, date=date).first()
    return reservation is not None

    

if __name__ == "__main__":
    from server import app

    connect_to_db(app)