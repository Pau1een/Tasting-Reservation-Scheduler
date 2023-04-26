import os
import json
from random import choice, randint
from datetime import datetime, timedelta

import crud, model, server

os.system("dropdb melon")
os.system("createdb melon")

model.connect_to_db(server.app)
model.db.create_all()


# Create test users
users_in_db = []
for user in user_data:
    username = user.get("username")
    if username:
        db_user = crud.create_user(username=username)
        users_in_db.append(db_user)

model.db.session.add_all(users_in_db)
model.db.session.commit()

# Create seed data
reservations = []
for reservation_data in reservations_data:
    username = reservation_data.get("username")
    date = reservation_data.get("date")
    start_time = reservation_data.get("start_time")
    end_time = reservation_data.get("end_time")
    if username and date and start_time and end_time:
        db_reservation = crud.create_reservation(username=username,
                                                date=date,
                                                start_time=start_time,
                                                end_time=end_time)
        reservations.append(db_reservation)

# Write seed data to file
seed_data = []
for reservation in reservations:
    seed_data.append({
        "username": reservation.username,
        "date": str(reservation.date),
        "start_time": str(reservation.start_time),
        "end_time": str(reservation.end_time)
    })

with open('seed_data.json', 'w') as f:
    json.dump(seed_data, f, indent=4)

print('Seed data created successfully!')


