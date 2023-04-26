from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import Reservation, connect_to_db, db
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
        flash(f"Hello!  You are now logged in!")
        return render_template('search.html', username=user.username)


@app.route("/logout")
def logout_user():
    """Log out user."""
    # Remove user from session when user clicks "logout" 
    session.clear()
    flash("You have logged out. Goodbye!")
    return redirect('/')


@app.route('/search_results')
def view_search_results():
    """Show search results"""

    return render_template('search_result.html')


@app.route('/view_reservations')
def view_booked_reservations():
    """Show booked reservations"""
    username = session.get("username")
    display = crud.get_reservations(username)

    return render_template('reservations.html', reservations=display)


@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        username = int(request.form['username'])
        date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
        start_time = datetime.strptime(request.form['start_time'], '%H:%M').time()
        start_datetime = datetime.combine(date, start_time)
        end_datetime = start_datetime + timedelta(minutes=30)
        existing_reservations = Reservation.query.filter_by(date=date).all()
        for r in existing_reservations:
            if start_datetime >= r.start_time and start_datetime < r.end_time:
                return "Error: appointment overlaps with existing reservation"
            if end_datetime > r.start_time and end_datetime <= r.end_time:
                return "Error: appointment overlaps with existing reservation"
            if r.username == username:
                return "Error: user already has a reservation on this date"
        reservation = Reservation(username=username, start_time=start_datetime, end_time=end_datetime, date=date)
        db.session.add(reservation)
        db.session.commit()
        return redirect('/')
    else:
        username = request.args.get('username')
        if username:
            username = int(username)
            reservations = crud.get_user(username)
            return render_template('reservations.html', username=username, reservations=reservations)
        else:
            date_str = request.args.get('date')
            if date_str:
                date = datetime.strptime(date_str, '%Y-%m-%d').date()
            else:
                date = datetime.now().date()
            timeslots = crud.get_available_timeslots(date)
            return render_template('book.html', date=date, timeslots=timeslots)



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)