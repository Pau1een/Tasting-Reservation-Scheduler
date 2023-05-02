from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import Reservation, User, connect_to_db, db
import crud
import os
from datetime import datetime, timedelta
import json
from jinja2 import StrictUndefined
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def login():
    """View login page."""

    return render_template('login.html')


@app.route('/create_user', methods=["POST"])
def create_user():
    """Create a new user account."""

    username = request.form.get("username")

    user = crud.get_user(username)
    
    if user:
        flash("An account already exists with that username. Try again.")
        return redirect('/')
    else:
        new_user = crud.create_user(username)
        db.session.add(new_user)
        db.session.commit()
        flash("Account created! Please log in")

        return redirect('/')


@app.route('/login', methods=["POST"])
def process_login():
    """Process user login."""

    username = request.form.get("username")
        #Check if username is correct or existing
    user = crud.get_user(username)
    if not user:
        flash("The username you entered was incorrect or you need to create an account.")
        return redirect('/')
    else:
        # Log in user by storing the user's username in session
        session["username"] = user.username
        flash(f"Hello!  You are now logged in, {user.username}!")
        return render_template('search.html', username=user.username)

@app.route('/logout')
def logout_user():
    """Log out user."""
    # Remove user from session when user clicks "logout" 
    session.clear()
    flash("You have logged out. Goodbye!")
    return redirect('/')



@app.route('/search')
def search_reservations():
    """Search page"""
    username = session.get("username")
    flash(f"You are logged in {username}!")
    return render_template('search.html')



@app.route('/book', methods=['POST'])
def book_reservation():
    """Search and add a reservation."""
    
    if 'username' not in session:
        return jsonify({'success': False, 'message': 'Please log in.'})
        
    user = crud.get_user_by_username(session['username'])

    data = request.json
    date = data.get('date')
    start_time = data.get('start_time')

    existing_user_date = crud.user_has_reservation_on_date(user, date)
    if existing_user_date:
        return jsonify({'success': False, 'message': 'You already have a reservation for this date'})

    existing_date_time = crud.get_reservation_by_date_time(date, start_time)
    if existing_date_time:
        return jsonify({'success': False, 'message': 'Timeslot taken. Please choose another time.'})
    # if crud.get_reservation_by_date_time(date, start_time):
    #     return jsonify({'success': False, 'message': 'Timeslot taken. Please choose another time.'})

    booked_reservation= Reservation(username=user.username,
                            date=date,
                            start_time=start_time)

    db.session.add(booked_reservation)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Reservation taken!'})



@app.route('/view_reservations')
def view_booked_reservations():
    """Show booked reservations"""
    username = session.get("username")
    display = crud.get_user_by_username(username)
    reservations = display.reservations
    user = crud.get_user(username)
    flash(f"Reservations for {user.username}")

    return render_template('reservations.html', display=display, reservations=reservations)



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)