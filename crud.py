"""CRUD operations."""

from model import db, User, Reservation, connect_to_db
from datetime import datetime, timedelta 


def create_user(username):
    """Create a new user and add it to database."""

    new_user= User(username=username)

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

# def save_appointment(username, appointment_date):
#     """Save and return appointment."""

#     saved_appointment = Appointment(username=username, appointment_date=appointment_date)

#     return saved_appointment



# def update_appointment(updated_appointment, username, appointment_date):
#     """ Update appointment. """

#     updated_appointment = Appointment.query.filter(Appointment.username==username, Appointment.appointment_date==appointment_date).first()
#     print(updated_appointment)
#     updated_appointment.appointment_date = updated_appointment
#     db.session.add(updated_appointment)
#     db.session.commit()

#     return updated_appointment



if __name__ == "__main__":
    from server import app

    connect_to_db(app)