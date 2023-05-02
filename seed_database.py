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
for user in user_data:
    username = user.get("username")
    if username:
        db_user = crud.create_user(username=username)
        users_in_db.append(db_user)

model.db.session.add_all(users_in_db)
model.db.session.commit()

# Create test reservations
reservations_in_db = []
for reserv in reservations_data:
    username = reserv.get("username")
    date = reserv.get("date")
    start_time = reserv.get("start_time")
    if username and date and start_time:
        db_reservation = crud.create_reservation(username=username,
                                                  date=date,
                                                  start_time=start_time)
        reservations_in_db.append(db_reservation)

model.db.session.add_all(reservations_in_db)
model.db.session.commit()

print('Seed data created successfully!')