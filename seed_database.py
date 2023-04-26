import os
import json
from random import choice, randint
from datetime import datetime, timedelta

import crud, model, server

os.system('dropdb melon')
os.system('createdb melon')

model.connect_to_db(server.app)
model.db.create_all()


with open('data/reservations.json') as reserv:
    reservations_data = json.loads(reserv.read())

with open('data/users.json') as userr:
    user_data = json.loads(userr.read())


# Create test users
users_in_db = []
for userr in user_data:
    username = user_data.get("username")
    if username:
        db_user = crud.create_user(username=username)
        users_in_db.append(db_user)

model.db.session.add_all(users_in_db)
model.db.session.commit()


# Create test reservations
reservations_in_db = []
for reserv in reservations_data:
    username = reservations_data.get("username")
    date = reservations_data.get("date")
    start_time = reservations_data.get("start_time")
    end_time = reservations_data.get("end_time")
    if username and date and start_time and end_time:
        db_reservation = crud.create_reservation(username=username,
                                                date=date,
                                                start_time=start_time,
                                                end_time=end_time)
        reservations_in_db.append(db_reservation)

# # Write seed data to file
# seed_data = []
# for reservation in reservations:
#     seed_data.append({
#         "username": reservation.username,
#         "date": str(reservation.date),
#         "start_time": str(reservation.start_time),
#         "end_time": str(reservation.end_time)
#     })

print('Seed data created successfully!')


